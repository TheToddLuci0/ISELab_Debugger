"""PCAP Tests

This module contains functions for testing a PCAP (represented as a `scapy.plist`)
for potential attack traffic.

Each function should accept one argument, the plist, containing the packets, and
return a list of strings, indicating potential attacks. Functions in this module are
called procedurally, and all at once, so effort should be made to keep all analysis
compute efficient.

"""

from .tests import ping_flood
