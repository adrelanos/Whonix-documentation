[[include ref=WikiHeader]]

[TOC]

# Anonymity Network
## Introduction
This page describes, why Tor has chosen for the *Whonix Example Implementation* as anonymity network and also discussed alternatives, which also have been considered.

## Tor
Tor has been chosen for the *Whonix Example Implementation*, because it's the best researched and most used network. Whonix developer adrelanos believes Tor is currently the most secure anonymity network legally available to most users. See [anonbib](http://freehaven.net/anonbib/) for a collection about research papers about Tor and other anonymity networks.

Many users are important, because you can only be anonymous within a big group of people. More secure networks exist in theory, such as the mixminion high latency network, but without enough users, in practice they are less secure. See [Roger Dingledine explanation](http://www.mail-archive.com/liberationtech@lists.stanford.edu/msg00022.html) for details.

On the [Warning](https://sourceforge.net/p/whonix/wiki/Warning/) page are some shortcomings of Tor listed.

## Whonix and other Anonymity Networks
The *Whonix Framework* is agnostic about the Anonymity Network being used. In theory also Tor could be completely exchanged with any other suited anonymizing network, see [Whonix Framework](https://sourceforge.net/p/whonix/wiki/Technical%20Introduction/#whonix-framework). Development in this area stalled due to lack of interest from users, upstream developers and Whonix developers. Anyway, there has been some research, theoretical and practical work done towards such integration, see [Inspiration] in case you are interested.

## Security considerations
Any successful attacks against Tor, does also work against Whonix and will result in a compromise of location/identity. ^1^

Whonix does not try to defend against network attacks, like a massive amount of evil Tor nodes, end-to-end correlation attacks and so on. The Tor software package from the Debian repository is installed in Whonix. There are no modifications to Tor software. This is left to to the Tor developers and Debian packagers.

If TransPort, DnsPort or SocksPort, which Whonix heavily relies on, can be exploited, then it's also game over.

There is no known bug (or "feature") to obtain the users real IP address through either SocksPort, TransPort or DnsPort. If there were such a bug found in the future, which is possible, it would be a major bug in Tor. We would hope, that the Tor developers fix that bug. We hope that compile time hardening features will be added. [Bug #5210: Enable gcc and ld hardening by default in 0.2.3.x](https://trac.torproject.org/projects/tor/ticket/5210) has been fixed. [Bug #5024: compile time hardening of TBB (RELRO, canary, PIE)](https://trac.torproject.org/projects/tor/ticket/5024) is still open.

There are other attacks thinkable, which we can not defend against. For example, if an adversary controls your entry node or can observe your ISP and has access to the Whonix-Workstation. He can simply use "morse" (5 seconds much traffic, 10 seconds no traffic...) And then observe it's incoming connections. Then it's game over as well.

<font size="-3">
,,
^1^ Unless Tor is combined with other means of anonymization (available as optional feature).
</font>

## Other Anonymity Networks reviewed for Whonix
### High latency networks
In theory, high latency networks would be safer than Tor. Unfortunately there is no high latency network, with enough users, which is well designed, developed and maintained.

### AdvOR
Not suited for Whonix at all.

[AdvOR](http://sourceforge.net/projects/advtor/), the "Advanced" Onion Router is not suited for Whonix. Reasons:

* No interest from the research community.
* No source control, i.e. git.
* Licensing issues (See Nick Mathewson's (Tor's Chief Architect) analysis below.)
* Absence in the Tor community.
* No Linux support.
* Whonix developer believes the Tails developers and the Tor developers to be modest and genuine. Doing their best on providing fine software. They generally work thoroughly, come to, in adrelanos opinion, clever conclusions. A Tails developer and a Tor developer wrote about AdvOR. Adrelanos believes it's best not to summarize the their writings. Please read it yourself, in case you're interested.
    * [Answer from a Tails developer about AdvOR](https://tails.boum.org/forum/Facebook_doesn__39__t_block_a_profile_if_logged_into_thru_AdvOR/#comment-6a1f9df007aadf7126f5b2420f02c11e).
    * The [Nick Mathewson's (Tor's Chief Architect) analysis](http://archives.seul.org/or/talk/Oct-2010/msg00026.html) and recommends against.
* In adrelanos opinion: less safe than Tor.

### i2p
#### Review
It is not possible to reliably replace the Tor network with the [i2p network](http://www.i2p2.de) for Whonix-Gateway. The i2p network is mainly designed to host all services inside the i2p network. We have to update the Whonix-Workstation's operating system and software packages. That is not possible with i2p. Outproxies existed in past (http, https and socks), but too few of them. And they are not suited for use with Whonix. They are too unreliable (too often offline). At time of writing the i2p chapter (March 2012) there where no working https or socks outproxies, which we could use for apt-get.

<font size="-3">i2p can only be used as an addition to Whonix (tunnel ip2 over Tor).</font>

Even if there where enough reliable outproxies, there is one question which would have to be answered. Is i2p designed for withholding the external IP from a Workstation, i.e. does the i2p webinterface spill the external IP and if yes, can it be configured, not to?

There was [development idea](https://sourceforge.net/p/whonix/wiki/Inspiration/#i2p) to install Tor and optionally i2p on Whonix-Gateway, but stalled due to lack from Whonix developers and i2p community.

That i2p is not in Debian package sources would also make integration harder.

[i2p users can be deanonymized using browser fingerprinting](http://trac.i2p2.de/ticket/726). ([w](http://www.webcitation.org/6EQgYfFNf))

#### Summary
Not suited for Whonix for the Default-Download-Version.

* No out proxies at the moment. (Can not connect to any servers outside the i2p network. i2p is much different than Tor.) Clearnet websites could not be reached, apt-get wouldn't work, etc.
* Less interest from the research community.
* No interest from the i2p community.
* In adrelanos opinion: less safe than Tor.

### JonDonym
Not suited for Whonix for the Default-Download-Version.

This JonDonym chapter is a summary of the [JonDonym](https://sourceforge.net/p/whonix/wiki/Inspiration/#jondonym) chapter from the "Inspiration" page, which is about adding an option to Whonix to use JonDonym instead of Tor and a summary of the [JonDonym](https://sourceforge.net/p/whonix/wiki/JonDonym/) introduction chapter, which reflects adrelanos's opinion about the JonDonym network security.

* Less interest from the research community.
* Too less help (interest?) from upstream developers to create a JonDoBOX (See [JonDonym](https://sourceforge.net/p/whonix/wiki/Inspiration/#jondonym) chapter from the "Inspiration" page.).
* Free version too limited.
* In adrelanos opinion: less safe than Tor.

### VPN
Not suited for Whonix for the Default-Download-Version. This is a summary of [Comparison of Tor and VPN services](https://sourceforge.net/p/whonix/wiki/ComparisonOfTorProxiesCGIproxiesProxyChainsAndVPNServices/#comparison-of-tor-and-vpn-services).

* Fail open, which is bad. Ok, that could be prevented developing a [Fail Closed Mechanism](https://sourceforge.net/p/whonix/wiki/VPN/#fail-closed-mechanism) or developing/using a VPN-Gateway.
* No distributed trust, just a single trusted provider.
* Affected by identity correlation.
* No free ones without restrictions.
* In adrelanos opinion: less safe than Tor.

### Freenet
Not suited for Whonix for the Default-Download-Version.

Replacing Tor with Freenet is impossible, as Freenet is a separated network, not designed to exit the network, i.e. clearnet websites could not be reached, apt-get wouldn't work, etc.

There was a [development idea](https://sourceforge.net/p/whonix/wiki/Inspiration/#freenet) to install Tor and optionally Freenet on Whonix-Gateway. It would pose the questions. Is Freenet designed for withholding the external IP from a Workstation, i.e. does the Freenet webinterface spill the external IP and if yes, can it be configured, not to?

### RetroShare
Not suited for Whonix for the Default-Download-Version.

In fact [RetroShare](http://retroshare.sourceforge.net) is not an [anonymizing network](https://en.wikipedia.org/wiki/Anonymizer), it is a [friend-to-friend](https://en.wikipedia.org/wiki/Friend-to-friend) (F2F) network, or optionally a [darknet](https://en.wikipedia.org/wiki/Darknet_(file_sharing)). RetroShare has a very different audience and threat model. RetroShare does not support using an outproxy yet, for this reason, it can not replace Tor on the Whonix-Gateway.

### Proxies / Proxy Chains
This is a summary of [Comparison of Tor, Proxies, CGIproxies and Proxy Chains](https://sourceforge.net/p/whonix/wiki/ComparisonOfTorProxiesCGIproxiesAndProxyChains).

"(High) Anonymous" Proxies or even "Elite" Proxy Chains are not suited for Whonix for the Default-Download-Version.

* Inferior to Onion Routing (Tor). Just two strong points (many more exist): no encryption between the user and the proxy possible (only end-to-end encryption possible); no onion routing alright (changing circuits).
* Difficult (impossible?) to find a free, stable proxy, which is supposed to be legally used as proxy and which could handle enough Default-Download-Version users.
* In adrelanos opinion: less safe than Tor.

### Combinations of Anonymity Networks
Not suited for Whonix for the Default-Download-Version.

There is too much controversy, see [Tor Plus VPN or Proxy](https://trac.torproject.org/projects/tor/wiki/doc/TorPlusVPN).

Controversy is avoided as a political project strategy with the goal to protect the project:

Quoted from the [FAQ]:
*"Whonix tries to be as less special as possible to ease security auditing of Whonix. Any changes to the Tor routing algorithm should be proposed, discussed and eventually implemented upstream in Tor on torproject.org. And if discussion fails, a Tor fork could be created. Tor has already been forked at least once. Doing such changes directly in Whonix would limit discussions about Whonix to the security of the modified routing algorithm. To allow further exploration of Whonix security, it is required to be as agnostic as possible about all parts of Whonix."*

The user is able to tunnel Other Anonymizing Networks over Tor (see [OtherAnonymizingNetworks] in case you're interested).

## Tunneling other Other Anonymizing Networks over Tor
It's possible with Whonix. (See [OtherAnonymizingNetworks] in case you're interested).

# Footer #
[[include ref=WikiFooter]]