[[include ref=WikiHeader]]

[TOC]

# FAQ 1
[FAQ]

# How difficult is it to develop Whonix?
This is just adrelanos's opinion and feeling.

Whonix source code isn't rocket science. In comparison to other things it's very simple.

I think it's best to make a comparison table.

Legend:
10 * equals very difficult.

    **********

1 * equals very easy.

    *

Table:

    ********** Hand written binary code.
    ********* Cryptographic algorithms development
    ********* Rocket science
    ********* Compiler development
    ******** Assembly language
    ******** Kernel development
    ******** Reverse engineering
    ******* Tor core development
    ****** Programming languages such as C/C++.
    ***** Using Hardened Gentoo
    **** Scripting language
    *** Whonix related anonymity/privacy research
    ** Writing Whonix documentation
    ** Writing Whonix bash scripts
    * Using a computer

# What is clearnet?
This term has two meanings.

a) Connecting to the regular internet not using Tor (or other anonymity networks), and/or
b) Connecting to regular servers (which are not Tor hidden services) (using Tor or not)

# Can I use DNSCrypt in Whonix?
Yes, see [Secondary DNS Resolver].

# Why not use DNSCrypt as default for Whonix?
[DNSCrypt](http://dnscrypt.org/) may have good use cases for clearnet. In context of Whonix it's not useful and should not be installed and activated by default for everyone. It does not do what you may think, does not magically solve all DNS related security issues, does not implement end-to-end DNS encryption to the destination server. (That conceptually can not work. If you knew the IP of the destination server in advance, you wouldn't require DNS in the first place.) The OpenDNS server will still see all DNS requests in cleartext. This is only a short version for the many reasons, why it should not be activated by default for everyone 

More reasons:
Tor is about distributing trust. Tor's DNS server change as circuits change, thus trust is distributed. Circuits are stream isolated (for pre-installed applications) and change every ten minutes. As far I know, there is only one DNSCrypt server run by OpenDNS. Relying on single servers is never a good idea. That would give too much power to OpenDNS servers.

I have no reason to distrust OpenDNS or DNSCrypt. Even if I trusted the people running DNSCrypt server, there server would have to be trusted as well and that's not wise to let DNS security for all Whonix users depend on one single server. It's also about load balancing. If OpenDNS decides to forbid connections from the Tor network (due to the Tor network used to abuse their servers with DDOS or for whatever else reasons) or if their servers go down for maintenance, DNS would break for all Whonix users.

For even more explanations on DNSCrypt, see forum post [one](https://sourceforge.net/p/whonix/discussion/general/thread/3c99944b/#3ea4) and [two](https://sourceforge.net/p/whonix/discussion/general/thread/e659f3ad/#bff5) related to this topic.

# Can I use DNSCrypt on the host, in my router, for clearnet?
Yes, if you want. Read also the FAQ entry below.

# Does DNSCrypt on the host or in my router, harm anonymity when using Tor/Whonix?
Short answer:
No.

Long answer:
No, DNSCrypt on the host or in your router only affects your clearnet activities. Tor assumes your local network and ISP to be totally unsafe and untrustworthy. Neither Tor nor Whonix are affected by DNS settings on your host or in your router.

Whether it is useful for your clearnet activities or not - that isn't clear. There are pro and contra arguments. If you ask me, it's useful foreign or untrusted Wifi networks (shared with others), since they could modify and/or read your DNS requests. Other than that, I think you just moving the trust from one party (ISP) to another (OpenDNS). If OpenDNS is more trustworthy, then it's good. What is more trusted, your ISP or OpenDNS - I don't know.

# Whats the difference of installing a VPN on the host versus installing on Whonix-Gateway?
This assumes, you already decided to use a VPN.

If you did that after reading the [VPN / Tunnel Support](https://sourceforge.net/p/whonix/wiki/Features/#vpn-tunnel-support) documentation, and decided you want to use a VPN, continue reading, otherwise you can skip this FAQ entry.

If the VPN is installed on the host:

* all Whonix traffic goes: user -> VPN -> Tor -> destination
* all host traffic goes through the VPN: user -> VPN -> destination

If the VPN is installed on Whonix-Gateway:

* all Whonix traffic goes: user -> VPN -> Tor -> destination
* all host traffic goes in the clear: user -> destination

When making the decision, you must ask yourself...

What do I want the VPN to see?

Only Tor traffic?
Install the VPN on Whonix-Gateway.

Tor traffic and host traffic?
Install the VPN on the host.

What do I want my ISP to see?

Only VPN traffic?
Install the VPN on Whonix-Gateway.

Just no Tor traffic, but not host traffic?
Install the VPN on Whonix-Gateway.

# Footer #
[[include ref=WikiFooter]]