[[include ref=WikiHeader]]

[TOC]

## Fail Closed Mechanism ##
**This is not a Whonix specific problem. It is a general problem with VPNs.**

**In development. Help welcome!**

If you simply add a VPN using common instructions, it generally fails open. That means, if the VPN breaks down, traffic will be send without the VPN.

It's much safer when it fails closed, i.e. when the VPN connection breaks down, the whole internet connection must be down as long as the VPN connection isn't restored or as long the routing table isn't manually and knowingly modified again.

There are some weak alternative ways to do this. Some "VPN-Monitor" check every, let's say 500 ms, if the VPN IP is still valid, if not, kill a list of applications. This is not very secure, it's a game if that time period is sufficient to stop a leak and if killing the applications is fast enough.

Another more serious option would be to use iptables rules, allow only traffic to the VPN server and to no other targets. This maybe additionally implemented later. However, using iptables for this scenario isn't the most secure option. When the IP of the VPN service gets assigned to another server, you could end up connecting to a malicious server.

The most secure option is to modify the routing table.

[source](http://cranthetrader.blogspot.de/2011/10/dont-allow-non-vpn-traffic.html), Windows related but the routing stuff is valid for Linux as well.

See [VPNBOX](https://sourceforge.net/p/whonix/wiki/Inspiration/#vpns-as-a-tor-replacement-vpnbox) it might help developing this.

# Footer #
[[include ref=WikiFooter]]