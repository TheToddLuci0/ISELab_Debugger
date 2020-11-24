from django import template
from django.template.loader import render_to_string
from django.conf import settings
from scapy.layers.inet import TCP, Ether, UDP, IP
from scapy.packet import Raw, Padding
from scapy.utils import hexdump

register = template.Library()


@register.tag()
def pcap_cards(parser, token):
    return PcapCardNode()


class PcapCardNode(template.Node):
    def render(self, context):
        res = []
        packet_count = 0
        for p in context['packets']:
            layers = p.layers()
            subcontext = {'p': p.summary, 'num': packet_count}
            if TCP in layers:
                subcontext['border'] = 'border-success'
            elif UDP in layers:
                subcontext['border'] = 'border-primary'
            else:
                subcontext['border'] = 'border-danger'
            if IP in layers:
                subcontext['ip_version'] = p['IP'].version
                subcontext['ip_len'] = p['IP'].len
                subcontext['ip_id'] = p['IP'].id
                subcontext['ip_flags'] = p['IP'].flags
                subcontext['ip_ttl'] = p['IP'].ttl
                subcontext['ip_chksum'] = p['IP'].chksum
            if TCP in layers:
                subcontext['tcp_sport'] = p['TCP'].sport
                subcontext['tcp_dport'] = p['TCP'].dport
                subcontext['tcp_seq'] = p['TCP'].seq
                subcontext['tcp_ack'] = p['TCP'].ack
                subcontext['tcp_flags'] = p['TCP'].flags
                subcontext['tcp_chksum'] = p['TCP'].chksum
            if UDP in layers:
                subcontext['udp_sport'] = p['UDP'].sport
                subcontext['udp_dport'] = p['UDP'].dport
                subcontext['udp_len'] = p['UDP'].len
                subcontext['udp_chksum'] = p['UDP'].chksum
            if Raw in layers:
                subcontext['raw_load'] = hexdump(p['Raw'].load, dump=True)
            if Padding in layers:
                subcontext['padding'] = p['Padding'].load
            if Ether in layers:
                subcontext['ether_src'] = p['Ether'].src
                subcontext['ether_dst'] = p['Ether'].dst
                subcontext['ether_type'] = p['Ether'].type
            res.append(render_to_string('pcap_parsing/snippets/packet_snippet.html', subcontext))
            packet_count += 1
            # Debug.
            if settings.DEBUG:
                for l in layers:
                    if l not in [UDP, TCP, Ether, Raw, IP, Padding]:
                        print("{} Not currently supported. Please open an issue at "
                              "https://github.com/TheToddLuci0/ISELab_Debugger/issues/new?assignees=TheToddLuci0&labels"
                              "=Packet+Layer+Request%2C+enhancement&template=add-packet-layer.md&title=Add+Packet+Layer"
                              "+LAYER_NAME".format(l))
        return '\n'.join(res)
