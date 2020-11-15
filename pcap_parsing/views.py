from base.views import BaseTemplateView
from . import forms, actions


class PcapIndexView(BaseTemplateView):

    template_name = 'pcap_parsing/index.html'

    def get(self, request, context, *args, **kwargs):
        return self.render_to_response(context)


class PcapUploadView(BaseTemplateView):
    template_name = 'pcap_parsing/pcap_upload.html'

    def get(self, request, context, *args, **kwargs):
        context['form'] = forms.PcapUploadForm()
        return self.render_to_response(context)

    def post(self, request, context, *args, **kwargs):
        form = forms.PcapUploadForm(request.POST, request.FILES)
        context['form'] = form
        if form.is_valid():
            plist = actions.pcap_to_scapy(request.FILES['file'])
            context['packets'] = actions.packlist_to_sanity(plist)
        return self.render_to_response(context)
