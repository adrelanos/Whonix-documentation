[[include ref=WikiHeader]]

[TOC]

# SSL #
[SSL in Wikipedia](https://en.wikipedia.org/wiki/Transport_Layer_Security)

The public SSL certificate authority system is not to be trusted. Too many security breaches happened. (See [DigiNotar](https://en.wikipedia.org/wiki/DigiNotar) and [Comodo](http://www.scmagazine.com/two-more-comodo-resellers-owned-in-ssl-hack/article/199620/)).

SSL certificates, especially for https://check.torproject.org (check.tpo) are not yet pinned in Whonix. Eventually that will be done in future. That needs some more discussion. How that technically could be done is documented under [Dev_sslcertpinning]. This has low priority for Whonix, since not even the Tor Browser Bundle does pin the check.tpo SSL certificate, which is a much bigger issue. Whonix developer adrelanos does not aggree with "low priority" in TBB. See [TBB: hardcode SSL cert check to prevent MITM](https://trac.torproject.org/projects/tor/ticket/3555).

# Footer #
[[include ref=WikiFooter]]