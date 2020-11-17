from django import forms


class PcapUploadForm(forms.Form):
    file = forms.FileField(label="PCAP to analyze")
