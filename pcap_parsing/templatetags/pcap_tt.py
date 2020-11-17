from django import template
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter
from scapy.layers.inet import TCP, Ether, UDP

register = template.Library()


@register.tag()
def pcap_cards(parser, token):
    return PcapCardNode()


class PcapCardNode(template.Node):
    def render(self, context):
        res = []
        for p in context['packets']:
            if Ether not in p.layers():
                # Not writing in support for non-ethernet at the moment
                res.append(render_to_string('pcap_parsing/snippets/packet_snippet.html',
                                            {"error": "Non-Ethernet frames not currently supported",
                                             'border': 'border-danger'}))
                continue
            subcontext = {'p': p.summary}
            if TCP in p.layers():
                subcontext['border'] = 'border-success'
            elif UDP in p.layers():
                subcontext['border'] = 'border-primary'
            else:
                subcontext['border'] = 'border-danger'
            subcontext['ether_src'] = p['Ether'].src
            subcontext['ether_dst'] = p['Ether'].dst
            subcontext['ether_type'] = p['Ether'].type
            res.append(render_to_string('pcap_parsing/snippets/packet_snippet.html', subcontext))
        return '\n'.join(res)
