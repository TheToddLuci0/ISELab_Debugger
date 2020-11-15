from django import forms


class PcapUploadForm(forms.Form):
    test = forms.CharField()
    file = forms.FileField(label="PCAP to analyze")
