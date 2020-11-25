Adding New Rules
================

To add a new rule, there are a few basic rules you must follow. Beyond these, it is up to you how you detect potential
attacks.

- Each test must be individually imported in __init__.py.
- Each test must accept exactly one argument of type ``scapy.plist.PacketList``.
- Each test must return either a list of strings containing warnings about potential attacks, or ``None``.
- These tests are run in a web call, so efforts should be made to make each test as performant as possible.

Once you have written your rule, it is highly encouraged that you share it with the world by opening a pull request on
GitHub. If you choose to do so, the only additional requirement is that you update the docs.