from django import forms


class NetTestForm(forms.Form):
    test_site = forms.URLField(label="Test Site", required=True, help_text="Site to use to test HTTP/S connections",
                               widget=forms.URLInput(attrs={'class': 'form-control'}))
    proxy_address = forms.GenericIPAddressField(unpack_ipv4=True, label="Proxy IP",
                                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    gateway_address = forms.GenericIPAddressField(unpack_ipv4=True, label="Gateway Address",
                                                  help_text="By default, this is at .254 of your range",
                                                  widget=forms.TextInput(attrs={'class': 'form-control'}))


class SSHServiceForm(forms.Form):
    address = forms.GenericIPAddressField(unpack_ipv4=True, label="Host Address",
                                          widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    cmd = forms.CharField(label="Command", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    port = forms.CharField(label="Port", required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
