from django.views.generic.base import View, TemplateResponseMixin
from . import actions, forms


##########
# Base Classes
##########
class BaseView(View):
    """
    Override Django's default dispatch method to include the context in handler calls.
    """
    page_title = "ISELab Debugger"

    # Override this method in a subclass if the page title cannot be a simple string.
    # E.g. contains some kind of variable.
    def get_page_title(self, request, context):
        return self.page_title

    # This function is used to get the context for the current app. e.g. base has a different
    # default context than blue or green.
    def app_context(self, request):
        return actions.get_context(request)

    # This function is used to add class properties to the context, such as page_title.
    def _view_context(self, request, context, *args, **kwargs):
        return {
            'page_title': self.get_page_title(request, context),
        }

    def modify_context(self, request, context, *args, **kwargs):
        pass

    def dispatch(self, request, *args, **kwargs):
        # Try to dispatch to the right method; if a method doesn't exist,
        # defer to the error handler. Also defer to the error handler if the
        # request method isn't on the approved list.
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed

        self.request = request
        self.args = args
        self.kwargs = kwargs

        # Setup the app context for the particular area
        context = self.app_context(request)

        # Let the subclasses add/edit items in the context before calling the method handler.
        self.modify_context(request, context, *args, **kwargs)

        # _view_context is used by other superclass views to add class properties to the context,
        # such as the page title.
        view_context = getattr(self, '_view_context', {})
        if callable(view_context):
            view_context = view_context(request, context, *args, **kwargs)
        context.update(view_context)

        return handler(request, context, *args, **kwargs)

    def get(self, request, context, *args, **kwargs):
        raise NotImplementedError("GET method not implemented on the view.")

    def post(self, request, context, *args, **kwargs):
        raise NotImplementedError("POST method not implemented on the view.")

    def put(self, request, context, *args, **kwargs):
        raise NotImplementedError("PUT method not implemented on the view.")

    def delete(self, request, context, *args, **kwargs):
        raise NotImplementedError("DELETE method not implemented on the view.")

    def head(self, request, context, *args, **kwargs):
        raise NotImplementedError("HEAD method not implemented on the view.")


class BaseTemplateView(BaseView, TemplateResponseMixin):

    def get(self, request, context, *args, **kwargs):
        return self.render_to_response(context)


# Create your views here.
class IndexView(BaseTemplateView):
    template_name = "base/index.html"

    def get(self, request, context, *args, **kwargs):
        return self.render_to_response(context)


class NetworkTestView(BaseTemplateView):
    template_name = "base/network-test.html"

    def get(self, request, context, *args, **kwargs):
        context['form'] = forms.NetTestForm(
            initial={'proxy_address': '199.100.16.100', 'test_site': 'https://google.com'})
        return self.render_to_response(context)

    def post(self, request, context, *args, **kwargs):
        form = forms.NetTestForm(request.POST)
        context['form'] = form
        if form.is_valid():
            # Do net tests
            results = {}
            gate_success, gate_err = actions.ping_server(form.cleaned_data['gateway_address'])
            if not gate_success:
                results['gateway'] = gate_err
            else:
                results['gateway'] = "OK"
                proxy_success, proxy_err = actions.ping_server(form.cleaned_data['proxy_address'])
                if not proxy_success:
                    results['proxy'] = proxy_err
                else:
                    results['proxy'] = "OK"
                    site_success, site_err = actions.test_http_site(form.cleaned_data['test_site'])
                    results['site'] = site_err if not site_success else "OK"
            context['results'] = results

        return self.render_to_response(context)


################
# Service Checks
################


class ServiceCheckView(BaseTemplateView):
    template_name = 'base/service_check.html'


class SSH_ServiceCheckView(BaseTemplateView):
    template_name = 'base/services/ssh.html'

    def get(self, request, context, *args, **kwargs):
        context['form'] = forms.SSHServiceForm(initial={'port': 22, 'cmd': 'date'})
        return self.render_to_response(context)

    def post(self, request, context, *args, **kwargs):
        form = forms.SSHServiceForm(request.POST)
        context['form'] = form
        if form.is_valid():
            success, message, exception = actions.test_ssh(
                form.cleaned_data['address'],
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                cmd=form.cleaned_data['cmd'],
                port=form.cleaned_data['port']
            )
            if success:
                context['okay_text'] = message
            else:
                context['err_text'] = message
        return self.render_to_response(context)


class HTTP_ServiceCheckView(BaseTemplateView):
    template_name = 'base/services/http.html'

    def get(self, request, context, *args, **kwargs):
        context['form'] = forms.HTTPServiceForm()
        return self.render_to_response(context)

    def post(self, request, context, *args, **kwargs):
        form = forms.HTTPServiceForm(request.POST)
        context['form'] = form
        if form.is_valid():
            okay, status = actions.test_http_site(address=form.cleaned_data['address'],
                                                  ignore_ssl=form.cleaned_data['bypass_ssl'],
                                                  username=form.cleaned_data['username'],
                                                  password=form.cleaned_data['password'])
            if okay:
                context['okay'] = True
            elif isinstance(status, Exception):
                context['error'] = status
            else:
                context['status_code'] = status
        return self.render_to_response(context)


class DNS_ServiceCheckView(BaseTemplateView):
    template_name = 'base/services/dns.html'

    def get(self, request, context, *args, **kwargs):
        context['form'] = forms.DNSServiceForm()
        return self.render_to_response(context)

    def post(self, request, context, *args, **kwargs):
        form = forms.DNSServiceForm(request.POST)
        context['form'] = form
        if form.is_valid():
            okay, message = actions.test_dns(dns_server=form.cleaned_data['server'],
                                             lookup_target=form.cleaned_data['hostname'],
                                             lookup_type=form.cleaned_data['lookup_type'])
            if okay:
                arr = []
                for m in message:
                    s_arr = m.to_text().split('\n')
                    for i in s_arr:
                        arr.append(i)
                context['response_arr'] = arr
            else:
                context['err'] = message
        return self.render_to_response(context)
