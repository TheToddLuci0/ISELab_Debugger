Working With PCAPs
==================

Once you have a PCAP file, you can upload it.

Once uploaded, the application will run a set of rules against the packets in the PCAP, attempting to
find any potential attack traffic. A list of rules is below.

.. autofunction:: pcap_parsing.tests.ping_flood

.. autofunction:: pcap_parsing.tests.http_malicious_auth