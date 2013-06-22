[[include ref=WikiHeader]]

[TOC]

= Introduction =

The Tor software [https://trac.torproject.org/projects/tor/ticket/7830 does not support UDP itself yet]. Whonix provides a limited workaround for using UDP anyway, in the best possible secure manner.

= VPN method (WORKING) =

Read first: [https://trac.torproject.org/projects/tor/wiki/doc/TorPlusVPN Tor Plus VPN] and [https://sourceforge.net/p/whonix/wiki/Authorship/#whonix-vpn-disclaimer Whonix VPN disclaimer].

This tutorial uses OpenVPN. <font size="-3">Other VPN implementations, such as PPTP, might be useful as well, but we haven't researched that yet. Maybe there are other VPN implementations, which also support UDP, and which are free and allow UDP. We haven't researched that yet.</font>

Before setting up the VPN, you should make yourself with curl and rdate familiar. The rdate command line switch -p results in just showing the date and time, without setting it. -u uses UDP instant of TCP (default).

Test if your Whonix setup is working in general.

<pre>## Enforcing SSL.
/usr/bin/curl --tlsv1 --proto =https https://check.torproject.org

## Alternatively, not enforcing SSL, because some VPN services seem to block SSL.
/usr/bin/curl http://check.torproject.org</pre>
Which should show &quot;Congratulations. Your browser is configured to use Tor.&quot;.

Install rdate for UDP and TCP testing.

<pre>sudo apt-get install rdate</pre>
Commands for TCP testing are.

<pre>rdate -p time.u.washington.edu
rdate -p time.nist.gov
rdate -p ptbtime1.ptb.de</pre>
Commands for UDP testing are.

<pre>rdate -u -p time.u.washington.edu
rdate -u -p time.nist.gov
rdate -u -p ptbtime1.ptb.de</pre>
Your tests should reveal, that without a VPN, you can run TCP over Tor, but not UDP.

Obviously a VPN provider is required. Instructions setting one up can be found on the [TestVPN] page, the riseup and the usaip example is known to work for this purpose.

Test rdate again, first in TCP mode, then in UDP mode. Both should work.

= OnionCat =

See [[#onioncat|OnionCat]].

= SSH method (NOT DOCUMENTED) =

In theory we can also use SSH servers to tunnel UDP over Tor. Unfortunately we can't provide instructions here. Free SSH services are rarely available, that makes developing such as solution impossible. The existing free SSH services are blocking certain ports, which does not make this easier as well. Even though SSH can provide a socks5 proxy, it is not capable of providing [http://zarb.org/~gc/html/udp-in-ssh-tunneling.html support for tunneling UDP itself]. Extra software installed on the client, and even worse on the server is required (needs root). Most admins will not do this. The link in the instructions are most likely only useful for you, if you have your own server. But even then, you are probable better off, using the VPN method.

= socks5 proxy method (FAILED) =

Moved to [Dev] Archiv Tunneling UDP over Tor.

= Footer =

[[include ref=WikiFooter]]

