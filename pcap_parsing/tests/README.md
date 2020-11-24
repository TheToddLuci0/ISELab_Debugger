# PCAP Tests
This module contains the actual tests for trying to spot attack traffic.
Each one is a function which accepts exactly one argument, a `scapy.plist.PacketList`
of the packets. It returns an array of strings if something is found, else `None`.

## Contributing
To add a test, simply write the test function, import it into `__init__.py`, and open a
pull request. Ideally, write a test for it as well, but I haven't done so yet, so I 
can't really complain if you don't either.
