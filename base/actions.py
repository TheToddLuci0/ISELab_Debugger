import subprocess
import re
import sys
import requests
from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, SSHException
from dns.resolver import Resolver as DNSResolver
from dns.name import from_text as dns_from_text
from dns.exception import Timeout as DNS_Timeout
from dns.rdatatype import RdataType as DNS_RdataType

PING_REGEX = re.compile('\A[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\Z')


def get_context(request):
    context = {}
    context['current_url_full'] = request.get_full_path()
    request.session.__setitem__('ip_addr', request.META.get('HTTP_X_FORWARDED_FOR'))
    request.session.__setitem__('recent_path', request.META.get('PATH_INFO'))
    if request.user:
        context['user'] = request.user
    return context


def ping_server(address: str = "199.100.16.100"):
    if PING_REGEX.fullmatch(address):
        # This is a valid IP address
        if sys.platform.startswith('linux'):
            res = subprocess.run("ping -c 1 " + address, capture_output=True, text=True)
        elif sys.platform.startswith('win'):
            res = subprocess.run("ping -n 1 " + address, capture_output=True, text=True)
        else:
            return False, "Sorry, can only run on Windows or Linux"
        if res.returncode != 0:
            return False, res.stdout
        else:
            return True, None
    else:
        return False, "Not a valid IP address"


def test_http_site(address: str, ignore_ssl=False, username=None, password=None):
    try:
        if ignore_ssl:
            r = requests.get(address, verify=False, auth=(username, password))
        else:
            r = requests.get(address, auth=(username, password))
    except Exception as e:
        return False, e
    if r.status_code == 200:
        return True, None
    else:
        return False, r.status_code


def test_ssh(address: str, username: str = 'root', password: str = '', port: int = 22, cmd: str = 'date && pwd'):
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy)
    ex = None
    try:
        client.connect(address, port=port, username=username, password=password, auth_timeout=5)
        std_in, std_out, std_err = client.exec_command(cmd, timeout=15)
        res, msg = True, std_out.read().decode('ascii')
    except AuthenticationException as e:
        res, msg, ex = False, "Invalid Credentials", e
    except SSHException as e:
        res, msg, ex = False, "Failed to establish SSH connection", e
    except TimeoutError as e:
        res, msg, ex = False, "Connection timed out.", e
    except Exception as e:
        res, msg, ex = False, "An unknown error occurred", e
    finally:
        client.close()
    return res, msg, ex


def test_dns(dns_server: str, lookup_target: str, lookup_type):
    from dns.resolver import NXDOMAIN, YXDOMAIN, NoAnswer, NoNameservers
    if isinstance(lookup_type, str):
        lookup_type = DNS_RdataType.from_text(lookup_type)
    try:
        resolver = DNSResolver(configure=False)
        dns_name = dns_from_text(lookup_target)
        resolver.nameservers = [dns_server, ]
        answer = resolver.resolve(dns_name, rdtype=lookup_type)
        return True, answer.response.answer

    except DNS_Timeout:
        return False, "Operation timed out. Is your DNS server running?"
    except NXDOMAIN:
        return False, "The domain does not exist. Are you sure you've loaded your" \
                      "zone files properly?"
    except YXDOMAIN:
        return False, "DNS name too long after DNAME substitution. Do you have a" \
                      "recursive lookup?"
    except NoAnswer:
        return False, "The server did not return a response. Check that your config " \
                      "has the proper records."
    except NoNameservers:
        return False, "No working nameservers at that address."
    except Exception as e:
        return False, "An unknown error has occurred.\n{}".format(e)
