Service Checks
==============

The tool supports a number of service checks. Those of you familiar with IScorE will notice some overlap on protocols,
but *the code is different*. In other words, just because IScorE and the tool both check HTTP, passing a check with
this tool does not guarantee IScorE will award you points.

HTTP
++++
The HTTP check takes four parameters and one option.

``Health Check URL``: This is the URL to check. For example, ``https://mysite.com:443/``.

``Search Text``: *Optional* Check if the response contains a given string, like "Login Success"

``Username``: *Optional* Username to attempt HTTP BASIC auth with.

``Username``: *Optional* Password to attempt HTTP BASIC auth with. If specified, must pass ``Username``.

``Don't validate SSL``: Select this to ignore SSL errors. Useful if using a self signed certificate.

SSH
+++

The SSH test takes five parameters.

``Host Address``: the ip address of the server to SSH to.

``Username``: Username to use

``Password``: Password to ues.

.. note:: Key-based auth not currently supported

``Command``: A command to run to check that auth was successful. ``date``, ``whoami``, and ``id`` are all good choices.

``Port``: What port to use. 22 is the standard SSH port.


DNS
+++

The DNS check takes three parameters.

``DNS Server Address``: The IP address of the DNS server to use.

``Lookup Target``: The DNS name to look up.

``Lookup Type``: What type to look for. If you're not sure, you probably want ``A``.
