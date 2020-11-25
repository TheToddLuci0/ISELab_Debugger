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
            context['warnings'] = actions.test_pcap(plist)
            context['packets'] = plist.__len__()
        return self.render_to_response(context)
