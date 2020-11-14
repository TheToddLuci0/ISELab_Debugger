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


class HTTPServiceForm(forms.Form):
    address = forms.URLField(label="Health check URL", widget=forms.URLInput(attrs={'class': 'form-control'}))
    check_text = forms.CharField(label="Search text", required=False,
                                 help_text="If specified, check for this text, and treat it as a failure if the\
                                  response does not contain it",
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Username', required=False,
                               help_text="OPTIONAL. Username to use for HTTP BASIC auth.",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", required=False,
                               help_text="OPTIONAL. Password to use for HTTP BASIC auth. If specified, must specify Username",
                               widget=forms.PasswordInput(attrs={'class': 'form-control'})
                               )
    bypass_ssl = forms.BooleanField(label="Don't validate SSL", required=False,
                                    help_text="Can be helpful in environments with no or self signed certs")
