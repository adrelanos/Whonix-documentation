[[include ref=WikiHeader]]

[TOC]

# Technical Introduction #
## Introduction ##

Whonix aims to be safer than Tor alone. The main goal is, that no one can find out the users IP and location.

The basic idea is, that all applications are untrustworthy. No application must be able to obtain the users real external IP. Whonix ensures that applications can only connect through Tor. Direct connections (leaks) must be impossible. This is the only way we know of, that can reliably protect your anonymity from client application vulnerabilities and IP/DNS and [protocol leaks](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO#Protocolleaks).^10^

Whonix consists of two machines, which are connected through an isolated network. One machine acts as the client or *Whonix-Workstation*, the other as a proxy or *Whonix-Gateway*, which will route all of the Whonix-Workstation's traffic through Tor. This setup can be implemented either through virtualization and/or Physical Isolation (explained below).

The **Whonix Concept** (see below) is agnostic about everything, the anonymizer, platform, etc. See **Whonix Framework** below.

**Whonix Example Implementation**: Anonymity setup build around **Tor**, two virtual machines using **VirtualBox** and **Debian GNU/Linux**. Whonix can be installed on every computer capable of running [Virtual Box](https://www.virtualbox.org/wiki/Downloads). (Supports Windows, OS X, Linux, BSD and Solaris.)

Physical Isolation describes installing Whonix-Gateway and Whonix-Workstation on two different pieces of hardware. It is more secure than virtual machines alone, requires more physical space, hardware and electricity costs are higher. Keep in mind that you don't need very powerful dedicated servers or desktops. For more information, see [Physical Isolation](https://sourceforge.net/p/whonix/wiki/PhysicalIsolation/).

See below Technical Design for the threat model and security of Whonix.

The [listed](https://sourceforge.net/p/whonix/wiki/Features/) Features, advantages and disadvantages shall give you an overview, what Whonix is useful for, what Whonix can do for you, and what not.

## Whonix Framework ##
The **Whonix Concept** is agnostic about everything. With some development effort you can replace any component. The Whonix developers would like to support each and any use case, but due to limited amount of developers this is impossible and we focus on the **Whonix Example Implementation**.

The Tor network is Whonix's official and best supported anonymizing network. Whonix can also potentially and optionally use [other anonymizing networks](https://sourceforge.net/p/whonix/wiki/OtherAnonymizingNetworks/) (Such as JonDo, i2p, freenet, RetroShare), either in addition (tunneled through Tor) or as a replacement for Tor. See the article for more information.

You can also avoid using virtualization by using [PhysicalIsolation], although that is not recommend, see [Comparison of different Whonix variants](https://sourceforge.net/p/whonix/wiki/Security/#comparison-of-different-whonix-variants) for more information.

It's possible to use other virtualization platforms than Virtual Box, e.g. Qubes OS, VMware, KVM, XEN, Qemu, Bochs, etc. (See [OtherVirtualizationPlatforms].). Only highly experimental support for [VMware](https://sourceforge.net/p/whonix/wiki/VMware/) is available as a proof of concept.

Other operating systems (e.g. Windows; *nix; BSD; etc.) can potentially be used as host and/or guest operating system. See the [OtherOperatingSystems](https://sourceforge.net/p/whonix/wiki/OtherOperatingSystems) for more information.

## Whonix Concept ##
Whonix is an [Isolating Proxy](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO/IsolatingProxy) with an additional [Transparent Proxy](https://trac.torproject.org/projects/tor/wiki/doc/TransparentProxy), which can be optionally disabled. (See [Stream Isolation] chapter for even [Better Protection](https://sourceforge.net/p/whonix/wiki/Stream%20Isolation/#better-protection).

## Security Overview ##
### In layman's terms ###
Shut up or put up! Adrelanos, is Whonix safe?

It is in the nature of security related software, that there is no 100% safety. 
Believe it or not, I use it myself and I keep maintaining and developing it. I believe in some aspects, threat models and use cases Whonix is safer than other tools. There is detailed reasoning for my claims on the Whonix Homepage.

If you are more paranoid or have higher security needs, read everything, full documentation and full technical design, you'll learn about physical isolation and build Whonix from source code and so on.

And no, Whonix [does **not** claim](https://sourceforge.net/p/whonix/featureblog/2013/01/another-statement-on-wakingtimescom-news-article-how-to-evade-government-surveillance-and-stay-anonymous-online---mailed-wakingtimescom/) to protect from very powerful adversaries, to be a perfectly secure system, to provide strong anonymity, or to provide protection from three-letter agencies or government surveillance and such.

See also [Whonix is a work in progress](https://sourceforge.net/p/whonix/wiki/Warning/#whonix-is-a-work-in-progress).

At first glance this site may create the impression that Whonix is completely insecure and everything is a lost cause. We are upfront with things we could do better and we are still working on and try to consider all possibilities and document all thinkable and future threats. You must judge for your own which risks are acceptable for your use cases.

### With more technical terms ###
It's difficult to write a summary of Whonix security features. Both anonymity and security consist of so many different aspects. That's why there is lots of [Documentation] and the whole Technical [Design].

The Technical [Design] intends to document security philosophy, design, goals and current shortcomings of Whonix.

This chapter is only a short introduction. Please read the full [Design].

Whonix follows the principle of security by isolation. We know that making our currently used systems secure is a lost cause. They are too complex and too large to be trustworthy and verifiably free of any bugs. Whonix can't solve this but it tries to minimize attack surfaces and limit what danger exploitable bugs in more exposed parts can do, one primary danger specific to Tor is the danger of exposing the public IP address of a system. Whonix isolates client applications inside the Whonix-Workstation from discovering the external IP address. Specifically, Whonix is designed to prevent direct detection of the IP (not more!) even if an adversary has unrestricted access to the Whonix-Workstation.

Once there is a vulnerability found in Tor (ex: exploiting Tor's ports) or a successful attack against Tor, Whonix fails.

Same goes for iptables. Whonix is a setup based on Linux, iptables, Tor, etc. If any of the underlying projects has a vulnerability, which we can not rule out, of course, Whonix will fail as well.

In summary, Whonix does **not** claim to be a perfectly secure system, does **not** claim to provide anonymity if one faces are very powerful adversary such as various three-letter agencies, governments and so on.

There are [three ways to torify](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO#OverviewaboutdifferentmethodsforTorification). Read the link for a comparison of the security.

Whonix-Workstation has no access to the internet without going through Tor. You can look into our setup. It's all Open Source and well documented.

Whonix uses multiple security layers.

1. IP-forwarding is disabled.
2. IPv6 is disabled.
3. The firewall fails "closed": when Tor is disabled, loses connection, or the Whonix-Gateway crashes, no network connections are possible.
4. Iptables redirects any traffic from Whonix-Workstation to Tor's ports. Local network connections are dropped. No leaks are possible, assuming the TCB is trustworthy.
5. Applications are configured correctly using latest suggestions (correct application and proxy and other privacy settings, [Stream Isolation]). 
6. Firewall rules are enforced and prevent accessing the internet directly, thus leaks are prevented in case some application leaks. 
7. Optionally, [PhysicalIsolation] is documented. 
8. [Whonix's Protocol Leak and Fingerprinting Protection](https://sourceforge.net/p/whonix/wiki/Whonix%27s%20Protocol-Leak-Protection%20and%20Fingerprinting-Protection/).
9. [Whonix's Secure And Distributed Time Synchronization Mechanism](https://sourceforge.net/p/whonix/wiki/TimeSync/).
10. Check.torproject.org is checked (see [whonixcheck]) anyway, even though we are sure, that there are no leaks.
11. Built in update notification for operating system updates, Tor Browser version and Whonix version (see [whonixcheck]).
12. Comprehensive, growing [Documentation].
13. Comprehensive, growing [Technical Design](https://sourceforge.net/p/whonix/wiki/Design/).
14. Openness about weaknesses, shortcomings, etc.
15. Cryptographically signed binary builds and git source code tags.
16. ...

Whonix was tested for leaks, see [LeakTests]. All went negative. Additionally, Skype, which is known for it's ability to punch through firewalls, was not able to establish non-torified connections. Also BitTorrent doesn't leak the IP (there is an online bittorrent leak tester), which of course should never be used through Tor (because it chokes Tor nodes), but for leak testing it was welcome. Right now we don't know of any leak tests which leaks the real IP.

Whonix is safe (not affected) from [Protocol leaks](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO#Protocolleaks), like this the ones listed on [Whonix security in real world](https://sourceforge.net/p/whonix/wiki/Security%20in%20Real%20World/), Skype, Flash or BitTorrent. This already justifies to use a "no non-Tor connections possible" approach.

When you go ahead now, and ask in a cracker forum, they probable won't spread a simple method to get the real IP of Whonix-Workstation. On the other hand, if you run an intelligence service and have 100.000 $ left over, you can announce something like "find a new exploit in Tor's SocksPort and get 100.000 $". Qualified people start looking into it and might find something.

# Footer #
[[include ref=WikiFooter]]