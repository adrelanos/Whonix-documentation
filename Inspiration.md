[[include ref=WikiHeader]]

[TOC]

# WARNING
**This page is intended for people interested in developing Whonix, NOT for users. It contains only partial-finished attempts adding new features to Whonix.**

# Rudimentary Whonix Support for Other Anonymizing Networks #
See https://sourceforge.net/p/whonix/wiki/OtherAnonymizingNetworks/

# i2p #
## Installing i2p on Whonix-Gateway (i2pBOX) ##
Development stalled due to lack of interest from Whonix developers and ip2 community. Development thread: [Dev] "Support for i2p WAIT for contributors/more mature upstream"; [i2p thread](http://forum.i2p2.de/viewtopic.php?t#7037). Anyone feel free it take it.

See also [Anonymity Network / i2p](https://sourceforge.net/p/whonix/wiki/Anonymity%20Network/#i2p) and [i2p].

# JonDonym #
## JonDonym as Tor replacement (JonDoBOX) ##
**Development stalled due to non-responsiveness upstream.**

The sources might contain additional helpful information:

* The [Dev] "SupportforJonDo Whonix dev thread about JonDonym"
* The [thread in the JonDonym forum](https://anonymous-proxy-servers.net/forum/viewtopic.php?f=10&t=6680)
* [JonDonym transocks_ev](https://anonymous-proxy-servers.net/en/help/transocks.html)
* [JonDoDaemon for Debian](https://anonymous-proxy-servers.net/wiki/index.php/JonDoDaemon_for_Debian)

Depending on your threat model (see [Design]), [JonDonym](https://anonymous-proxy-servers.net/) can be potentially used as a replacement for Tor. Prefer the [console version](https://anonymous-proxy-servers.net/wiki/index.php/JonDoDaemon_for_Debian) of 'JonDo – the IP changer', otherwise you would have to install a desktop environment, which needs a lot more RAM, CPU and disc space (not possible on most embedded devices).

Free users can [only only use port 80 (http) and 443 (https)](https://shop.anonymous-proxy-servers.net/bin/payment?lang#en#vorteile). Socks is [only available for paying premium users](https://anonymous-proxy-servers.net/en/help/about.html). Therefore free users can only reach services listening on remote port 80 or 443. Normal browsing will work, other stuff, for example IRC on port 6667 will not work. Paying premium users can use all services.

In comparison to Tor, JonDo does not offer a TransPort or DnsPort. For that reason, transocks_ev ([download here](https://anonymous-proxy-servers.net/en/help/transocks.html)) is needed. Note, that you can not use the firewall rules provided [under transocks_ev](https://anonymous-proxy-servers.net/en/help/transocks.html). You need to adjust the whonix  firewall (/usr/local/bin/whonix_firewall).

# VPN #
## Introduction ##
**Not finished yet.** ***UNTESTED!*** [Dev] "#SupportforVPNsasTorreplacementOPTIONALFEATURE dev thread"

Read first: [A Free example VPN working with Whonix for testing purposes](https://sourceforge.net/p/whonix/wiki/OptionalConfigurations/#a-free-example-vpn-working-with-whonix-for-testing-purposes).

## VPN's as a Tor replacement (VPNBOX) ##
Small update: there is now [VPN-Firewall].

**Development stalled.** ***UNTESTED!*** [Dev] "#SupportforVPNsasTorreplacementOPTIONALFEATURE dev thread"

In this chapter we explain, how you can replace Tor with a VPN. Regarding security see 'Introduction' on this page at the top. It's your responsibility to find a (non-logging, safe) free/paid VPN provider or to stick with Tor.

(1). Test if your host internet connection is working.

(2). Test if your tor internet connection is working.

(3). Store your routing table before starting the VPN and before modifying anything. Type in console:

    route

(4). Start VPN.

    sudo openvpn /etc/openvpn/client.conf

(5). Test if your ISP IP gets replaced with the VPN IP.

(6). Store the modified routing table. Type in console:

    route

(7). Delete your default route and set your new default route to the virtual VPN network adapter.

    sudo route del default
    sudo route add default dev tun0

(8). Test if your VPN IP is still valid.

(9). Store the modified routing table. Type in console:

    route

(10). For testing purposes, kill your OpenVPN connection.

    sudo killall openvpn

(11). Test if you can NOT connect to anything anymore. That's the whole point to prevent any leaks in the clear.

TODO: 

* Testing. 
* Autostart everything. 
* Use up in /etc/network/interfaces. 
* Final step: forwarding traffic from the Workstation to the Gateway.
* Extra: VPNchains (two or more independent VPN providers in a chain)

# Proxy #
## Introduction ##
Required reading: 

* [proxy](https://trac.torproject.org/projects/tor/wiki/doc/proxy)
* [Tor + VPN or Proxy](https://trac.torproject.org/projects/tor/wiki/doc/TorPlusVPN#VPNSSHversusProxy)

## Proxies in addition to Tor ##
See [Advantages of Whonix](https://sourceforge.net/p/whonix/wiki/Security/#advantages-of-whonix), "It is possible to use Whonix setup in conjunction with VPNs, ssh and other proxies....".

## Proxies as a Tor replacement (ProxyBOX) ##
**Development stalled.** **Not finished yet.**

[Dev] "#SupportforproxiesasTorreplacementOPTIONALFEATURE dev thread"

It is possible to replace Tor with local or remote proxies. Note that anonymity is sufficiently lower with (single hop) proxies. The difficulty is, that most proxies lack a TransPort and DnsPort.

It also depends, what kind of proxy you want to use.

See also [Transparent Proxying](https://sourceforge.net/p/whonix/wiki/OptionalConfigurations/#transparent-proxying) (Describes Transparent Proxying inside Whonix-Workstation to an extra proxy, i.e. Whonix-Workstation -> Tor -> Proxy.)

There are two options available. 1. Transparent Proxying Method or 2. The Proxy Settings Method.

### Depending on Proxy type ###
http proxies are not suited, because we would not be able to connect to https protected websites. The setup for https, socks4(a)/5 proxies should be very similar.

### Transparent Proxying Method ###
**Development stalled.** **Not finished.**

Transparent Proxying (like Whonix with Tor's TransPort) is, due to technical limitations, not fully supported by proxies. Proxies do not offer a DnsPort and also do not act as a DNS server. While it's possible to relay TCP and UDP traffic through the proxy on the IP level (using iptables), you would still always require known (you know the IP) DNS server. (i.e. public DNS server such as OpenDNS, Google, httpsdnsd) DNS resolution would look like: Proxy-Workstation -> Proxy-Gateway -> Proxy -> DNS server. It's technically not possible to let the proxy transparently (!) do the DNS resolution (no tools available) - at least not that we know after extended research know of. This is because proxies offer hostname resolution, but not DNS.

<font size="-3">
Future:

This technical limitation may be lifted if redsocks [Feature Request: fake DNS resolver](https://github.com/darkk/redsocks/issues/23) gets implemented.
</font>

Due to the DNS issue, you can't completely hide behind the proxy (using it transparently). You always would have to reveal, that you are using a public (or private) extra DNS resolver. Of course, you would also not only have to trust the proxy, but also the extra DNS server, which can see, log and correlate all your DNS queries.

For TCP and UDP: Proxy-Workstation -> Proxy-Gateway -> network layer -> redsocks -> proxy 
For DNS: Proxy-Workstation -> Proxy-Gateway -> network layer -> redsocks -> proxy -> public DNS server 

<font size="-3">
Sources:

* Leonid Evdokimov (author of [redsocks](https://github.com/darkk/redsocks)) on mailing list, [Transparent Proxy, DNS, without public DNS server](http://librelist.com/browser//redsocks/2012/5/15/transparent-proxy-dns-without-public-dns-server/#e8cb0f54932856f1c0cc9259e24cb089)
* [Bernd Holzmüller](http://tiggerswelt.net/Ueber%20uns/impressum/) (author of [transocks_ev](http://oss.tiggerswelt.net/transocks_ev/)) by e-mail)
</font>

### Proxy Settings Method ###
**Development stalled.** **Not finished.**

Design: The Proxy-Workstation is on an isolated internal LAN (similar to Whonix's Whonix-Workstation design) and can't connect to the internet directly. (Iptables rules on the Proxy-Gateway forbid that.) All applications installed inside the Proxy-Workstation have to use the correct [proxy settings](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO#classicalcommonway:usetheapplicationsproxysettings) or a wrapper https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO#notsocommon:useawrapper:forcetheapplicationtouseaproxytorsocksusewithtor

For TCP, UDP and DNS: Proxy-Workstation -> Proxy-Gateway -> proxy

# Freenet #
## Freenet on the Whonix-Gateway (FreenetBOX) ##
Can be also potentially only be used parallel to Tor. It's impossible to tunnel Freenet through Tor (see above). Also replacing Tor with Freenet is impossible, as freenet is a separated network, not designed to exit the network. Apt-get couldn't work.

Not written yet.

# Retroshare #
## RetroShare as Anonymizer ##
In fact [RetroShare](http://retroshare.sourceforge.net) is not an [anonymizing network](https://en.wikipedia.org/wiki/Anonymizer), it is a [friend-to-friend](https://en.wikipedia.org/wiki/Friend-to-friend) (F2F) network, or optionally a [darknet](https://en.wikipedia.org/wiki/Darknet_(file_sharing)). RetroShare has a very different audience and threat model. RetroShare does not support using an outproxy yet, for this reason, it can not replace Tor on the Whonix-Gateway.

# Footer #
[[include ref=WikiFooter]]