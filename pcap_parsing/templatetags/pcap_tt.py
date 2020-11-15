from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter
from scapy.layers.inet import TCP, Ether, UDP

register = template.Library()

@register.inclusion_tag('pcap_parsing/snippets/packet_snippet.html')
def pcap_card(p):
    subcontext = {}
    if p['TCP']:
        subcontext['border'] = 'border-success'
    elif p['UDP']:
        subcontext['border'] = 'border-primary'
    elif p['ICMP']:
        subcontext['border'] = 'border-danger'
    return subcontext
