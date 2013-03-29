[[include ref=WikiHeader]]

[TOC]

# Threat Model #
## Note ##
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt). 

## The Threats ##
First let's quickly consider all the possible threats we could face. We can put threats against computer systems into five categories:

(1) Non-technical/non-computer-based and legal attacks
E.g. "rubber hose cryptanalysis", mandatory key disclosure, subpoena, real police work/espionage (done by real humans, not bots), bugs, surveillance cameras...

(2) Hardware attacks through physical access.
RAM and Hard disk Forensics, keylogger, TEMPEST, Evil Maid attack...

(3) Backdoors
Intentional weaknesses or additional hidden "functionality" put into your system by a manufacturer, vendor or distributor (hardware or software) allowing remote access^1^ Can be put in anywhere between design/source code, manufacturing/compilation or distribution.

(4) Vulnerabilities
Coding or hardware design errors that can be exploited to gain remote access^1^ Vulnerabilities and Backdoors in practice can look exactly the same, only the way they are created differ.

(5) Design flaws
Even in a backdoors-free, error-free system with perfect physical and legal protection (no such thing in reality) perfect security may still be impossible. This is especially true for anonymity systems. While with cryptography a perfect design exists (the one time pad) anonymity isn't binary. You are not either anonymous or not, you only have some non-zero but not-perfect degree of anonymity. Your anonymity depends on hiding amongst others. Anonymity networks require trust and a large and diverse userbase. A perfect security system wouldn't require trusting other parties or depending on such extraneous factors. Any design of a complex (but still usable) system (all computer systems are complex) needs to make tradeoffs. That's why pretty much everything uses non-perfect cryptography instead of the one-time-pad...

Bug [Research: IP discovery through Tor behind isolated network](https://trac.torproject.org/projects/tor/ticket/5928) seems to only be about learning the IP address which a Tor client connects to the Internet through. It doesn't mention other information leaks.

<font size="-3">
,,^1^ Used in the broadest sense, can be classic remote code execution, privilege escalation, DoS... Essentially they all allow remote parties to send your system instructions that diverge from the allowed security policy
</font>

## Attacker capabilities ##
* Legal/Non-technical "attacks" and physical access is expensive
Anything that requires real humans to do work instead of letting computers and algorithms do it is prohibitively expensive against more than a small target group.

* Backdoors (hardware or software) are expensive
It is hard to make one and it's risky. The more you use it the more likely it is it will be caught and closed. Adversaries are not going to waste it on anything but high profile targets. However, well hidden passive "backdoors" are of a concern, they can practically be impossible to detect and remain functional for years. Imagine a backdoor in a compiler affecting the PRNG. The cost for such backdoor is high (for this example an attacker need patience, non-trivial coding and social engineering as well as some crypto skills) but the "ROI" would be great too...

* Software attacks are cheap
A good 0day can still cost a lot and isn't useful for very long once you start using it. But new vulnerabilities are found all the time, new exploits can be written. Compared to physical access and backdoors it is cheap. It can be fully automated against a large target set.
If you are wondering how realistic or important the client application 0day threat is consider pwn2own 2012. A semi-legal but most certainly immoral and reckless company demonstrated how they can exploit every web browser circumventing all state of the art security features (MAC, Sandbox, ASRL, NX, etc). This is not too surprising, we already established how big code bases always have bugs and a subset of those bugs will always be exploitable. The noteworthy news here is that this company doesn't report their findings to the developers, they sell it to governments (and/or the highest bidder) as offensive "cyber weapons" (naturally not their term).
It's only likely that also Tor vulnerabilities are sold behind closed doors. You MUST act accordingly and never rely on Tor alone if your threat model demands "reasonably strong anonymity" even from not-nearly-global but well funded adversaries.

* Crypto-attacks are enormously expensive
If you know how to break currently used crypto you will try keep this a secret at all costs. Most crypto attacks will most likely require enormous computing power.

* Attacking design flaws: it depends...
The costs can vary greatly but in every case, once you attack a design flaw and it becomes publicly known the target will fix the flaw and will become harder to attack in the future. This can result in an arms race and often neither party wants to go that way. A grave problem for the defender side can be that some systems are so widely used that it becomes almost impossible to mitigate away to a more secure design. The best example for that is the certificate authority system. It's design is flawed on so many levels yet it's relied upon, often solely for all authentication and confidentiality, to this day by pretty much everyone who's ever used a computer. Similarly, a lack of crypto and hash agility in many applications results in a dependence on weak and broken algorithms, not because we don't know any better but because backwards compatibility and some bad apples spoil it for everyone. There's certainly a threshold, were, if an attacker plays it slow and carefully, he can stay just below the radar for a long time and let everyone believe that it's not "that bad yet". For example, a [collision attack](https://en.wikipedia.org/wiki/Collision_attack#Attack_scenarios) against SHA-1 (which would affect software updates, version control systems as well as Tor, GPG, TLS and pretty much everything that uses public key crypto) is known to be "within the reach of a powerful adversary" since 2005, with Moore's Law and Schneier/NSA's Law ("Attacks always get better; they never get worse") in play the range of potential adversaries only got larger. SHA-1 will probably be relied on pretty universally until someone publicly demonstrates a collision. Not because we don't know any better, but because to cost of switching are so high.

## Our Goals ##
* Hiding our Location and Identity when transmitting information
* Confidentiality, Integrity, Authenticity and Availability of transmitted data

## Our Attack Surface ##
Basically any part used by us to achieve our goals can be attacked:

* We REQUIRE physical security and privacy. It's obvious that anonymity and confidentiality is difficult or impossible to achieve otherwise.
* Tor, the code, the design, the whole network (see [Anonymity Network] for more)
We also can't look at Tor as an isolated piece of software, we SHOULD consider its whole TCB because if any part of a TCB can be subverted the Tor process can be subverted. The attack surface in case of backdoors is the full TCB, in case of vulnerabilities "only" the network facing parts of the TCB.
	* The Whonix-Gateway Hardware
	* GNU/Linux/OS: kernel, essential userland, apt-get and all software update packages provided by the OS distributor/vendor
	* Tor itself
	* The build system (gcc...)
Using Virtualization (instead of Physical Isolation) increases the TCB significantly. In addition to the above:
	* Host Kernel
	* Host applications
	* Host software updater
	* Virtualization software
* We REQUIRE software we use doesn't do more than absolutely necessary to reduce our anonymity set through protocol leaks, identity correlation through Tor circuit sharing and fingerprinting. For that we also have to rely on the Whonix-Workstation and the TCB of the applications we use. (for more see [Whonix's Protocol-Leak-Protection and Fingerprinting-Protection]).

For Confidentiality, Integrity and Authenticity we (we all, not just Whonix...) are still way too heavily dependent on TLS (Transport Layer Security, the "s" in https). Further we depend on:

* The complete Host (Hardware and Software)
* all software in Whonix-Workstation
* TLS/PKI infrastructure
* In case of hidden services: The full location/identity TCB.
* The "other end", the security of whoever you are communicating with, unless it's symmetric key crypto and you got the only key.

To achieve Availability of information we depend on:

* the upstream internet provider, uptime and connectivity 
* Tor network resilience against DoS
* resilience of webservers you connect to against DoS
* Your own system's resilience against DoS

## Applying the threat model to Whonix ##
First of all, you don't want to end up in the "high profile target" list of any of your resourceful adversaries. Because, if you do, neither Whonix nor any other computer based system can protect you. 

Whonix is mostly a software project. There isn't a lot we can do on the hardware and physical side of things. Hardware security would be a much smaller problem if we weren't using monolithic systems where dozens of parts have full system access through DRM (or indirectly though hardware drivers that all run in kernel space). Have a look at Qubes OS for state of the art hardware deprivileging. It requires modern hardware, <s>software support still needs to catch up</s> and a bigger user base, therefore this isn't available in Whonix yet, although it shouldn't be hard to port Whonix to Qubes OS if anyone were willing to do it. 

We assume the hardware is trustworthy, we assume the physical location is not compromised. We RECOMMENDED to use "clean" computers made of parts manufactured by reputable companies and to pay in cash so as to not have hardware IDs leak our identity. 

To protect against forensic analysis we SHOULD on the host use full disk encryption and wipe the RAM on shutdown.

* Implementation status: Because Whonix doesn't include a host operating system yet, we RECOMMEND users to do that themselves in Whonix documentation.

Further some pointers:

* DMA is bad, IOMMU is good, avoid attaching untrusted (or any for that matter) devices on FireWire and PCI* interfaces.
* Use open source hardware or at least open source friendly that makes specifications public. Open source means that multiple companies can implement the hardware, the Linus law of "many eyeballs and all bugs are shallow" applies, backdoors are harder to hide.
* Simple is beautiful, complexity is the enemy Nr.1 of security. Whonix-Gateway could run on very simple hardware like the Raspberry Pi. 

Crypto is even worse, the only thing we can do is to use [cascades](https://en.wikipedia.org/wiki/Multiple_encryption) of different cipher and hash families. This is slightly more complicated than it sounds and we don't know of any software that does it right.

As established above in "Attacker capabilities" the main attack vector we need to concern (and we can actually do something about) is software attacks.

To protect against software backdoors and vulnerabilities:

* The source needs to be audited, preferably by yourself and many others and should ideally be bug free.
Popular open source projects are your best bet. Whonix is fully open source, anyone can audit and patch.  
* If you rely on others (you do), you need to make sure that you get the same code as everyone else Hash sums + signatures, the more public they are, the better. If completely transparent signing is used (as common in proprietary systems) it's much more difficult to determine that you get the same files as everybody else. By default signing is only concerned with making sure that you get code by someone with access to the key. This protects against 3rd parties but not insiders.
Checksums and signatures of Whonix and updates are publicly available.
* The code you use SHOULD have a good track record, know issues must be corrected immediately.
Code that doesn't get checked but has zero known problems is worse than code that has hundreds of known and patched security issues but is constantly being reviewed and worked on. However, a trustworthy code should have very few if any security issues despite having been audited thoroughly. After all, projects that constantly need security patches are constantly insecure. But it's not really about numbers, check the severity of the bugs. Linux needs many security patches but fatal flaws that would affect Whonix are few and far between (i.e. remote code execution with root privileges). Fatal flaws in user facing applications (like browsers, pdf readers, media players, IRC) are frequent and therefore such software is not be part of the TCB (see below).
* Checking the source is not enough, you need trustworthy binaries.
Analyzing binaries is a lot more difficult than analyzing source code. If you rely on source code auditing you absolutely REQUIRE a trustworthy compiler (and a complete trusted system to run it on) and use [DCC](http://www.dwheeler.com/trusting-trust/). Similarly you already need a trusted system to check signature and hashes. This is the bootstrapping chicken and egg problem we mentioned earlier. Generally, to address it you need to use at least two different diverse systems that are completely independent (includes their parent build system and compiler) and set up the system in such a way that both would have to be compromised by the same adversary in a compatible way in order to result in a fatal security breach.

If the code base is huge and complex code auditing isn't a realistic strategy, therefore we need to reducing complexity and attack surface by:

* making the TCB small 
and

* using privilege separation:
The TCB for identity/anonymity is as small as it gets on a monolithic general purpose OS. It could be smaller (e.g. a custom kernel, busybox, uclibc instead of libc and gnu-utils) but that comes at the cost of maintainability, security updates and ease of use. (And still leaves us with a comparably huge monolithic kernel and a gigantic gcc infrastructure.)
Linux/Xorg (with DAC or even MAC) isn't very good with privilege separation (e.g. no trusted path). The strongest privilege separation is offered by using multiple physical computers, that's what we RECOMMEND, [PhysicalIsolation] and [multiple Whonix-Workstations](https://sourceforge.net/p/whonix/wiki/Multiple%20Whonix-Workstations/). The more practical, but less secure alternative is virtualization. For details about privilege separation between IRC/Browser/Clients and Tor see [Technical Intro](https://sourceforge.net/p/whonix/wiki/Security/#technical-intro)

We've thought a lot about making Whonix yet more secure but with the (free and open source) tools available today it doesn't seem possible. What we'd need is an isolation kernel, that would offer some strong guarantees of isolation between the different subsystems and ideally would be verified, so you don't have to worry about sophisticated backdoors (apart from the compiler, see "Trusting trust"/chicken and egg), software vulnerabilities and even some hardware backdoors and vulnerabilities (through IOMMU and microkernel design one can put hardware and firmware components, apart from the CPU, out of the TCB).
For Fingerprint/Protocol leaks and the [CIA Triad](https://en.wikipedia.org/wiki/CIA_triad#Key_concepts) we are depending on the Whonix-Workstation TCB. This is a hopelessly large TCB/attack surface. For this reason we use yet another approach which can be called "security through non-persistence". That is, you should extensively make use of the snapshot and roll back feature of the virtual machine. Instead of privilege separation within a Tor-Workstation (e.g. by using a Mandatory Access Control framework) which would come at great usability costs, we recommend to use the coarse-grained isolation provided through multiple VMs (also see [About grsecurity](https://sourceforge.net/p/whonix/wiki/Advanced%20Security%20Guide/#about-grsecurity)).

To protect against software attacks (vulnerabilities) in particular:

* make software hard to attack
ASLR, canaries, NX, kernel hardening, (See the Debian section [About Debian](https://sourceforge.net/p/whonix/wiki/OperatingSystem/#about-debian). Note that this makes attacks "harder" but not impossible. Hardening is no replacement for fixing bugs. In a really trustworthy system hardening would not be necessary.

To mitigate Design flaws, the primary strategy is eliminating single points of failure. You SHOULD NOT not rely on Tor alone, use wifi or tunnel through another system running VPN. You SHOULD NOT rely on TLS alone, use GPG as well (and vice versa). You SHOULD NOT rely on a software monoculture, you SHOULD NOT have to rely on Debian infrastructure to never be compromised. We are currently guilty of not following this advice. To lessen the impact of a potential compromise of the update infrastructure (which includes developer machines, build systems, key security and cryptographic primitives like PRNG - remember openssl or Flame?) we do not enable automatic software updates. After all, they are essentially remote root level backdoors (although with some checks in place).

### Notes about securing Confidentiality, Integrity and Authenticity ###
This is no different than in any other computer system without Tor. You MUST use end to end public key encryption, there is not really an alternative to that. But there are alternative implementations: TLS, SSH, GPG... End-to-End means, both ends need to be secure, one end is the Whonix-Workstation, which you can control and secure. In case of hidden services, the Whonix-Gateway is ALSO part of the TCB! 

Whonix-Worstation isn't specifically hardened because hardening a Desktop system to a degree that makes it actually secure against a serious adversary makes the system unusable. Instead we follow the nuke and restore approach, see [Multiple Whonix-Workstations](https://sourceforge.net/p/whonix/wiki/Multiple%20Whonix-Workstations/) and [Recommendation to use multiple Snapshots](https://sourceforge.net/p/whonix/wiki/Security/#recommendation-to-use-multiple-vm-snapshots).

About Availability: The most resilient approach is probably a distributed data store, like Tahoe-LAFS or Freenet. i2p offers multi-homing built in. For Tor we don't know of any solutions ready for general usage.

#### Notes about End-to-end security of Hidden Services ####
Moved to https://sourceforge.net/p/whonix/wiki/Hidden%20Services/#notes-about-end-to-end-security-of-hidden-services

## Attack on Whonix ##
There is a comparison of TBB, Tails, Whonix Standard/Download version (host+VM+VM) and Whonix with Physical Isolation in chapter [Attacks against Whonix](https://sourceforge.net/p/whonix/wiki/Comparison%20with%20Others/#attacks).

## Design Document, innovations and research ##
Whonix developer adrelanos is also interested in serious design documents. There is only one design documents with respect to Tor, transparent/isolated proxying, isolation and Virtual Machines. Adrelanos has read the old design paper "A Tor Virtual Machine Design and Implementation" from 2009, which can be found at [DesignDocumentBase]. After reading, adrelanos forked that paper, removed non-essential, non-security relevant stuff and made sure, all considerations from the old design paper, were implemented into Whonix. The forked paper can be found at [DesignDocument].

The whole Whonix [Documentation] and [Design] supersede the old design document. Also the [TorifyHOWTO](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO) is co-maintained by adrelanos.

Also the following documents are being monitored.

* [Tails Design](https://tails.boum.org/contribute/index.en.html)
* [Tails Design: specification and implementation](https://tails.boum.org/contribute/design/)
* [Security and Anonymity in Liberté Linux](http://dee.su/liberte-security)
* [Liberté Linux Motivation and Philosophy](http://dee.su/liberte-motivation)

If there are any security/privacy/anonymity updates they will be considered for Whonix.

The Whonix project also enjoys asking good questions, providing useful suggestions and creating useful things.

The following list is to keep track of all discussions and to review them in the future again, to see if something has changed.

* Smarm created serious [LeakTestsOld], which have been scripted by adrealanos (see [LeakTests]) and which are potentially useful for other projects as well.
* [Tails-dev Removing SSL CA dependency for HTP](https://mailman.boum.org/pipermail/tails-dev/2012-June/001245.html)
* [Modified usewithtor to support setting ip and port by command line parameter by adrelanos](https://trac.torproject.org/projects/tor/wiki/doc/torsocks)
* [Research: IP discovery through Tor behind isolated network](https://trac.torproject.org/projects/tor/ticket/5928)
* [Enhance "Transparent Torification (Requires custom transproxy or Tor router)" in Tor Button.](https://trac.torproject.org/projects/tor/ticket/5611)
* Read [Dev] and also read the archives. We don't just do things. Everyone is invited to add some points and then we try to make the best decision.
* [tor-talk Tor Browser disabling Javascript anonymity set reduction](https://lists.torproject.org/pipermail/tor-talk/2012-May/024227.html)
* [tor-talk Awareness for identity correlation through circuit sharing is almost zero.](https://lists.torproject.org/pipermail/tor-talk/2012-March/023535.html); [Add warning related to Identity correlation through circuit sharing](https://trac.torproject.org/projects/tor/ticket/6102)
* [tor-talk Operating system updates / software installation behind Tor Transparent Proxy](https://lists.torproject.org/pipermail/tor-talk/2012-March/023486.html)
* [tor-talk Attack against Tor: Statistic Manipulation Attack](https://lists.torproject.org/pipermail/tor-talk/2012-August/025128.html)
* [Tails-dev tails_htp: exit node can fingerprint Tails users until exit node is changed](https://mailman.boum.org/pipermail/tails-dev/2012-July/001394.html); [2](https://mailman.boum.org/pipermail/tails-dev/2012-August/001421.html)
* [Tails-dev better IRC client, include XChat](https://mailman.boum.org/pipermail/tails-dev/2012-August/001436.html)
* [Tails-dev separate Tor streams](https://mailman.boum.org/pipermail/tails-dev/2012-August/001422.html)

* ...

This list is incomplete...

Searching...

* [Tor project trac, Reporter is proper](https://trac.torproject.org/projects/tor/query?reporter=proper&col=id&col=summary&col=reporter&col=owner&col=type&col=status&col=priority&order=priority)
* site:https://mailman.boum.org/pipermail/tails-dev/ adrelanos
* site:https://lists.torproject.org/pipermail/tor-talk/ adrelanos

## Whonix Threat Model not available as pdf or paper version ##
You may skip this optional chapter. Written by Whonix developer adrelanos.

While I read real papers, like the [Onion routing design paper](https://svn.torproject.org/svn/projects/design-paper/tor-design.pdf) and many others, I can't be coerced into creating a paper "Designing an anonymous operating system" with latex as pdf.

Like Mike Perry, developer of Tor Browser [said](https://lists.torproject.org/pipermail/tor-talk/2012-May/024405.html) "*I find the pdf format heavy and unnerving from a security perspective.*". That also goes for adrelanos and I also find the pdf format inconvenient. It would also take me some time to learn latex, pdf creation, formatting etiquette and so on. Time, which I rather invest into improving the design, developing and so on. The "Onion routing design paper" is now also outdated and I rather have an editable, often updated and revised website compared to a paper/pdf.

Tails does also not have a design paper as pdf and still lots of users and developers. Also TrueCrypt had not design paper about plausible deniability and still got reviewed by Bruce Schneier et al. Therefore I really don't see the benefits of having the threat model available as pdf, but if I have overlooked something, please don't hesitate telling me.

# Footer #
[[include ref=WikiFooter]]