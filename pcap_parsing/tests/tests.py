from scapy.layers.inet import *


def ping_flood(packets: scapy.plist.PacketList):
    """Test for potential ping flood attacks"""
    num_packets = packets.__len__()
    threshhold_percent = .5
    min_count = 1000
    if num_packets > min_count and num_packets / packets.filter(lambda p: ICMP in p).__len__() > threshhold_percent:
        return ['Potential ICMP Flood attack', ]
