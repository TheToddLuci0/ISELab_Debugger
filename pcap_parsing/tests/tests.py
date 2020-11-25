from scapy.layers.inet import *
from scapy.layers.http import *


def ping_flood(packets: scapy.plist.PacketList):
    """Test for potential ping flood attacks"""
    num_packets = packets.__len__()
    threshold_percent = .5
    min_count = 1000
    if num_packets > min_count and num_packets / packets.filter(lambda p: ICMP in p).__len__() > threshold_percent:
        return ['Potential ICMP Flood attack', ]


def http_malicious_auth(packets: scapy.plist.PacketList):
    """Check for a large number of 400-series HTTP responses

    This could indicate a potential auth attack
    """
    counts = {}
    threshold = 3
    res = []
    http_packets = packets.filter(lambda p: HTTPResponse in p)
    for p in http_packets:
        if 400 <= int(p['HTTPResponse'].Status_Code) < 500:
            try:
                counts[p['IP'].dst] = counts[p['IP'].dst] + 1
            except:
                counts[p['IP'].dst] = 1
    for k in counts.keys():
        if counts[k] > threshold:
            res.append("Potential malicious auth attempts from {}".format(k))
