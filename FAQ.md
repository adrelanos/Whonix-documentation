[[include ref=WikiHeader]]

[TOC]

# Why are the Whonix images so big? #
Compared to other "Tor-VM" or "Tor-LiveCD/DVD" projects which sometimes use special minimal or stripped down Linux distributions (e.g. TinyCore, DSL, Puppy) Whonix is larger, both VMs together are currently almost 2 GB.

One reason for that is, that small distributions do not meet our requirements, namely: upstream needs to have a proactive security policy.

* Most "minimal" distributions are small projects that do not have a dedicated security team that audits packages and releases security patches quickly.
* We need a distribution that fully signs updates (this is always desirable but especially so when updating over untrusted exit nodes).
* For such distributions security consist in a small attack surface^1^, but that's about it. A full distributions supports MAC, kernel patches, IDS...
* "Big" projects with many users and developers (many eyeballs) are inherently more trustworthy.
* Debian has loads of Security Features, see (Ubuntu article, but mostly true fro Debian) [Ubuntu Security Features](https://wiki.ubuntu.com/Security/Features/). Small distributions don't have it.

There are maintenance and usability reasons:

* We want to support a wide range of user cases such has hosting hidden services, small distributions usually have limited repositories.
* Whonix, since based on Debian, is complete operating system. An anonymous general purpose operating system, no stripped down minimal system. [OptionalConfigurations]; [Design]
* Debian has much more documentation than small distributions, also about topics such as Security and Hardening, [Ubuntu Security](https://help.ubuntu.com/community/Security); etc.
* Creating a slim system, needs is difficult and requires a lot development time. This should not be Whonix's core competence. There are projects who do not focus on anonymity/privacy/security, but which are dedicated to a slim system.
* To my knowledge, slim systems could never really attract big market shares. I don't know, why they are less favored, if they have worse marketing or for other reasons. It's the fact, that they don't have a huge user base, that matters.
* Slimming down the system will result in many "strange bugs". People who are used to Debian or Ubuntu will wonder why some things do not work and thing Whonix is broken.

Another reason is that Whonix does not play in the anonymity oriented Live CD/DVD market:

Whonix is a new category of anonymity tools. Whonix does not have the requirement to fit on a DVD. (Although in future we may develop an Whonix Live DVD.) While anonymity oriented Live CD/DVD's have to balance between functionality they want to provide and available space and security, Whonix, as an anonymous general purpose operating system can by default or optionally provide any functionality and doesn't has to care so much about space. For example, integrating BitCoin into Whonix would be, except for documentation, quite simple.

Last but not least reason, not putting security over usability:

* Short: I don't put security over more users.
* Long: For example, this interesting statement from Tor developer Roger Dingledine: [Mixminion vs Tor](http://www.mail-archive.com/liberationtech@lists.stanford.edu/msg00022.html). Similar applies here. Mixminion is a high latency remailer, with cover traffic, protection against traffic confirmation (end-to-end correlation), theoretically more secure than Tor. The problem is "theoretically". They couldn't attract enough users and without enough users it's equally (in)secure as Tor. That's why they decided, to no longer work on Mixminion. Whonix also needs also lots of users, to 1) get press/publicity 2) more developers 3) more research and audits. 2) and 3) will result in more security. Creating the most secure and most slim system, would only attract a few geeks. The geeks get hopefully satisfied, because Whonix is highly customizable. Nothing prevents form optionally slimming, hardening and customizing.

<font size="-3">
,,
^1^ Our attack surface is still very small, no network listening services, just a few selected applications.
</font>

# Why is KDE (big) the default desktop environment? Why not use a minimal DE? #
This was a difficult development path decision. Many people, including adrelanos, didn't like the old Openbox interface in TorBOX (deprecated project name) 0.1.3 because it was too inconvenient, non-intuitive, uncommon, difficult, etc. There is no rational unarguable choice for the best desktop.

MATE has not been choosen, because there are no packages in Debian repositories. It is my understanding, that GNOME2 is deprecated and only a friction of GNOME2 users likes GNOME3. Other desktops (LXDE, XFCE, Openbox) are less widespread, not so pretty, in adrelanos opinion harder to use (even difficult to create a desktop shortcut), thus not attracting many users.

Choosing KDE is a personal preference by Whonix developer adrelanos. KDE has one advantage, the only developer likes it and remains interested to maintain and develope Whonix further.

You are free to uninstall KDE and to install any other desktop environment of your own choice.

I recognize, that this is a non-ideal situation. Inspired by [select your webbrowser](http://www.browserchoice.eu/), it would be ideal if Whonix would offer to choose which desktop to install but unfortunately, such a wizard [does not exist yet](http://lists.debian.org/debian-derivatives/2012/09/msg00003.html). There are no development resources to implement such a solution. Help is welcome.

If there where contributors, we could maybe also include other desktop environments by default or offer alternative Whonix builds with different default desktop environments or ideally implement a "choose your desktop" option after first boot of Whonix.

Please also read "Why are the Whonix images so big?" above, the same applies here.

# Why not use a Live CD/DVD as Whonix-Workstation operating system? #
We discussed this and came to the decision, that Live CD/DVDs are not suited for Whonix.

Positive:

* often active maintained
* stabilized
* hardened GNU/Linux distribution
* with advanced features.

Negative:

* no timely security updates
* not persistent
* not flexible enough
* anonymity orientated Live CD/DVD's often have their own Tor enforcement included, which would lead into a [Tor over Tor](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO#ToroverTor) scenario

# Why should I (not) trust Whonix? #
See [Trust] for a long answer.

# Whonix crashes because of PAE? #
See [PAE Crash](https://sourceforge.net/p/whonix/wiki/Starting%20Whonix/#pae-crash).

# You should not waste the Tor network's bandwith by downloading operating system updates over Tor! #
Short answer: We discussed this with torproject.org are allowed to do so.

Long answer: We had a thread about this issue, [updates over Tor, should not waste Tor bandwidth](https://trac.torproject.org/projects/tor/wiki/doc/TorBOX/Dev/ArchivedDiscussion/DOCUMENTATION#updatesoverTorshouldnotwasteTorbandwidthDOCUMENTATIONSOLVED). Discussed thoroughly. We speculated a lot and thought about solutions, until we finally done, what we should have done in the first place. We asked torproject.org, see [tor-talk Operating system updates / software installation behind Tor Transparent Proxy](https://lists.torproject.org/pipermail/tor-talk/2012-March/023486.html). Click [here](https://lists.torproject.org/pipermail/tor-talk/2012-March/subject.html#23507) for an overview of all answers. Andrew Lewman ([Executive Director, Director, press contact](https://www.torproject.org/about/corepeople.html.en)) does also download a lot updates over Tor and did not [not complain](https://lists.torproject.org/pipermail/tor-talk/2012-March/023493.html).

# Alpha? Beta? Stable? Development? Whonix version scheme #
DRAFT!

Is Alpha, Beta or Stable related to security? No, our design makes security issues inherently less likely to occur.

Whonix 0.2.0 will be Alpha.

We are still working heavily on usability, working on some user facing stuff (like zenity). Until those are all integrated and tested we wouldn't be doing our users a favor by calling it not an alpha. They get turned away if things don't work right.

Alpha: 
Features are constantly being added.

Beta: 
Only fix important stuff, test it.

Stable: 
Build and release the current beta with all fixes when we feel it's ready. We expect beta testing to last a month or so, shorter if we can get feedback from more users.

Development version: 
Only goes for the source. Things can be added in order to get feedback from others. The longer things are inside, the longer they are accepted. Doesn't mean they are better tested. Sometimes the source can even break.

# Why do you use the 32 bit operating system, not 64 bit? #
Update:
A critical Virtual Box bug: [Virtual Box ticket #10853: Mouse position repeatedly reset to top and/or left of screen](https://www.virtualbox.org/ticket/10853).

Since Whonix 0.4.0 the build environment uses grml-debootstrap (perhaps kameleon in future) and chroot. Image creation goes much faster and changing the architecture requires only a very few changes. If Whonix revives contributions or due to user feedback it might be possible in future to have 32 and 64 bit downloads.

Old statement:
32bit software runs without problems on 32bit and 64bit hosts. 64bit software no so much. Because we generally don't control what host OS people use I chose to base Whonix on 32bit. Secondly, 64bit software needs more RAM, we already run 3 operating systems on a system which, eats RAM. Let's better minimize that. KVM and other solutions improve RAM usage through page sharing or what it's called, Virtual Box doesn't. Thirdly, according to Brad Spengler and/or PAX team, amd64 is a brain dead instruction set and actually worse than x86, despite the large address space making ASLR more effective. They recommended to use grsec on x86 and I hope we can switch to a grsec kernel (wheezy has one, let's see if they maintain it).

# Why aren't you using OpenBSD, it's the most secure OS ever!!!1! #
OpenBSD fails completely for the Tor threat model which downloading and updating software over untrusted exit nodes. OpenBSD does not offer any signed files, they do not even offer hash sums for all required files (at least the ports tar ball doesn't have one). When asking about that the answer is "buy the CDs" (=something like $80 per year if you want to stay current). As if CDs via post through a 3rd party reseller offer a better trust chain than mirrors with hash sums, let alone proper WOT signatures. There are alternatives to GnuPG if it's just about the license... Further, tracking stable - which is recommended for production systems - is needlessly complex: it requires the user to recompile everything even though there are usually only a few packages that require an update. The most fitting approach would be to just apply the patches from the errata but apparently not all security related fixes in -stable are listed there and OpenBSD admits as much that patch branch is really not userfriendly. Further problems: OpenBSD seems to default to using very "conservative" hash algorithms, md5 or sha1 which are both broken. This clashes with their claimed crypto focus. FDE support is lacking/limited. There doesn't seem to be a modern MAC, instead there's systrace which has been criticized for having fundamental security problems (this may or may not have changed since then). <s>OpenBSD doesn't seem to be using PIE executables by default, meaning, it doesn't really have ASLR.</s> Documentation about such issues is completely lacking. <s>There's also the strange policy of sticking with bind and sendmail when there were secure-by-design alternatives (see [PDF!](http://cr.yp.to/qmail/qmailsec-20071101.pdf)) with much better track record</s>, BIND-9, despite the rewrite, continues to be a security hazard just judging by the OpenBSD errata entries.
OpenBSD would otherwise be a great choice for Whonix-Gateway. It has a very capable firewall, the track record is probably better than of any other OS though they (just like their competition for fairness sakes) prefer to label "potential" code execution vulnerabilities as a DoS. OpenBSD is also a very small OS (small TCB), it's kernel may be the most secure UNIX like kernel, but it's still a monolithic kernel. Their claim of being THE most secure operating system has become more and more dubious since the introduction of actually usable microkernels. In summary: I don't like their attitude and several essential (for Whonix) security properties are missing.

Also see [security vulnerability - NTP not authenticated](http://thread.gmane.org/gmane.os.openbsd.bugs/18754) and it doesn't look they step forward to fix it. The suggestion was to authenticate the connection to the NTP server, which is not possible for Whonix for many reasons. ^1^ 

<font size="-3">
,,
^1^ We need to distribute the trust, not using only one NTP server and we must use free services which are available for anyone and not something requiring an own server.
</font>

OpenBSD's target audience aren't end users, that's why they don't care to provide signed updates for the masses, see [How to check downloaded package on OpenBSD 5.1?](http://unix.stackexchange.com/questions/38041/how-to-check-downloaded-package-on-openbsd-5-1).

OpenBSD's website isn't reachable over SSL or as a Tor hidden service. How are users supposed to securely view the OpenBSD site and not learn things set up by a man in the middle?

If they don't attract the masses, ordinary crackers, hackers and the security research community doesn't get attracted as they do with more popular operating systems. At the same time a targeted attack gets easier, because people who get paid to find exploits can find them more easily.

If this sounds a bit harsh on OpenBSD it's because it could be such a great OS but it isn't (mostly more for political and social/"ego" than technical reasons) which is frustrating.

Update 1:
There is now Qubes OS and I am missing such innovative security improvements from BSD, which claims to be the most secure operating system.

Update 2:
OpenBSD has according to [bststats.org](http://www.bsdstats.org/) ([w](http://www.webcitation.org/6F4tFWwNy)), very few users. 56 at time of writing. I know, that people must undergo a rather complicated manual process to get counted, however compared to 24,168 FreeBSD users, that's not very much.

# Why don't you use FreeBSD, which is more secure?!? #
Does FreeBSD have a secure package manager?

Does it defend [this](https://www.cs.arizona.edu/stork/packagemanagersecurity/) ([w](http://www.webcitation.org/6Ev4smCoD))?

Does it cover the [TUF threat model](https://www.updateframework.com/wiki/Docs/Security) ([w](http://www.webcitation.org/6Ev4owhEP))?

Can every user download from an already existing **signed** repository or is it required to run an own repository?

# Why don't you use OpenWRT, which is more secure?!? #
Does OpenWRT have a secure package manager?

Does it defend [this](https://www.cs.arizona.edu/stork/packagemanagersecurity/) ([w](http://www.webcitation.org/6Ev4smCoD))?

Does it cover the [TUF threat model](https://www.updateframework.com/wiki/Docs/Security) ([w](http://www.webcitation.org/6Ev4owhEP))?

Can every user download from an already existing **signed** repository or is it required to run an own repository?

# How is Whonix different from Tails? #
See [Comparison of Whonix, Tails and TBB](https://sourceforge.net/p/whonix/wiki/Comparison%20with%20Others/).

# Why don't you merge with Tails and join efforts? #
**UPDATE 7:** Rewrite.

**This is a subjective statement of opinion by Whonix developer adrelanos.** (Still open for feedback, corrections, improvements!)

[Tails](https://tails.boum.org/) is a respected project with similar goals (anonymity, privacy and security), which exists for many years and which has multiple developers, experience and a working infrastructure. The Whonix and the Tails developers are no "enemies". They cooperate to some degree and are discussing things, which are related to the projects on the Tails developers mailing list. Parts of Whonix are based on Tails. For example tails_htp was invented by Tails. Whonix also profits from their previous (Debian) upstream efforts (packaging and so on), their old and current discussions, their research, design documents, experience, feedback and so on.

Even though adrelanos highly values Tails, why is Whonix a separate project and not a contribution to Tails?

Whonix can not be merged into Tails by adrelanos. There are technical, skill and political reasons.

Adrelanos doesn't/didn't know how to implement various things into Tails, and don't/didn't know when the Tails developers will add them, which are adrelanos's priorities, but knew how solve them in a separate project (Whonix), at least as in a way, that users are provided with instructions how to do it. Some examples.

**Some of these items may already be either partially or fully solved in Tails by now.**

| (Previous) Tails Todo | Whonix Instructions
------------- |  ------------- |
[remember installed packages](https://tails.boum.org/todo/remember_installed_packages/) | By design, everything persists. ^1^
[Applications Audit](https://tails.boum.org/todo/applications_audit/) | By design, protocol leaks can not deanonymize.
[Two-layered virtualized system](https://tails.boum.org/todo/Two-layered_virtualized_system/) | Done by design, either using VMs or using [Physical Isolation](https://sourceforge.net/p/whonix/wiki/PhysicalIsolation/).
[TorChat](https://tails.boum.org/todo/Torchat_installed_by_default/) | [Chat]
[VPN](https://tails.boum.org/todo/vpn_support/) support | [VPN/Tunnel Support](https://sourceforge.net/p/whonix/wiki/Features/#vpn-tunnel-support).
[JonDo](https://tails.boum.org/todo/Include_JonDo_Software/) over Tor | [JonDonym](https://sourceforge.net/p/whonix/wiki/JonDonym/)
[Freenet](https://tails.boum.org/todo/freenet_project/) over Tor | [Freenet](https://sourceforge.net/p/whonix/wiki/Freenet)
obfsproxy | [Bridges](https://sourceforge.net/p/whonix/wiki/Bridges/)
hide Tor from your ISP | [Hide Tor and Whonix from your ISP](https://sourceforge.net/p/whonix/wiki/Hide%20Tor%20and%20Whonix%20from%20your%20ISP/)
i2p over Tor | [i2p](https://sourceforge.net/p/whonix/wiki/i2p/)
Transparent Proxy as fallback mechanism | Done by design, everything not configured to use a SocksPort will automatically use Tor's TransPort.
use Tor Browser | [Tor Browser](https://sourceforge.net/p/whonix/wiki/TorBrowser/)
[OnionCat](https://tails.boum.org/todo/install_OnionCat/) | [OnionCat](https://sourceforge.net/p/whonix/wiki/OnionCat/)
Stream Isolation | [Stream Isolation](https://sourceforge.net/p/whonix/wiki/Stream%20Isolation/)
[evaluate web fingerprint](https://tails.boum.org/todo/evaluate_web_fingerprint/) | Same as Tor Browser.
[unsafe browser fingerprint](https://tails.boum.org/todo/improve_fingerprint_of_the_Unsafe_Browser/) | [Logging in to captive portals](https://sourceforge.net/p/whonix/wiki/Logging_in_to_captive_portals)
Location Hidden/IP Hidden Servers | [Hosting Location/IP Hidden Servers](https://sourceforge.net/p/whonix/wiki/HostingLocationHiddenServers/)
[Voip](https://tails.boum.org/todo/VoIP_support/) | [Voip](https://sourceforge.net/p/whonix/wiki/Voip/)
... | ...

<font size="-3">
,,
^1^ This is actually also a disadvantage, because that is the opposite of an amnesic system, which also many users prefer.
</font>

Also political and design decisions differ too much.

* As a code contributor to Tails, adrelanos would have to accept decisions made by the Tails decision making process and couldn't simply modify anything as personally desired, preferred or believed to be the best solution. That's the great thing about Free Software. You are free to disagree and to create a fork. Since adrelanos motivation was not about a Live DVD and personally found improving Tails much more difficult than starting fresh, a new project, Whonix, was created.
* Source Code Merge Policy:
    * Whonix: does not yet have a comprehensive merge policy. It's welcome, but not compulsory to write a design or documentation.
    * Tails: In adrelanos opinion, [Tails merge policy](https://tails.boum.org/contribute/merge_policy/) is too strict. This not a complaint or critique. They will have their reasons for that and it has to be noted, that Tails is still doing well and useful for many people. Anyone who does not agree has the freedom to contribute to another project or to start a new project. Adrelanos just made use of that freedom.
* One big difference is, that Tails is a Live DVD and therefore inherits some restrictions and limitations. Tails must fit on a DVD, while Whonix does not have such a requirement. Whonix has higher hardware requirements, but therefore more space to implement features. That means that initially fewer people will be able to use Whonix, but over the years available hardware to people will (hopefully) improve. Whonix is discovering both, theoretically and practically, new designs. Over time, depending on user feedback and general interest, a Live DVD or Live Blu-ray might be created.

# How is Whonix different form the Tor Browser Bundle? #
See [Comparison of Whonix, Tails and TBB](https://sourceforge.net/p/whonix/wiki/Comparison%20with%20Others/).

# Does this mean that, for example, is my IP and location safe when using Skype? #
This answer has been moved to the [Voip] page.

# Isn't Virtual Box an insecure choice? #
Virtual Box is not an ideal choice, I acknowledge it, see: [Virtualization Platform](https://sourceforge.net/p/whonix/wiki/Virtualization%20Platform/), but there are no better alternatives, which are usable by a big amount of people.

It's about different goals. Whonix's main goal is to protect the users IP/location.

At the moment Whonix is practically more secure in many cases, see [Whonix Security in Real World](https://sourceforge.net/p/whonix/wiki/Security%20in%20Real%20World/).

Saying Virtual Box is too weak, is theoretical and does not have any practical implications at the moment. What are the alternatives? Continue running Tor and torified applications on the host? Running TBB and running into another [proxy bypass bug](https://blog.torproject.org/blog/firefox-security-bug-proxy-bypass-current-tbbs)? People failing to correctly torify software? Software [not honoring proxy settings](https://blog.torproject.org/blog/bittorrent-over-tor-isnt-good-idea)?

On the other hand, how many known exploits exist for Virtual Box? Whats the track record of exploits?

I acknowledge, that virtual machine exploits may become a problem in future. Right now, Whonix provides more security out of the box. Whonix right now, advertises and educates the security by isolation principle.

Anyone seriously looking into Whonix for security will, will read the [Documentation], the [Security Guide] and the [Advanced Security Guide] and find out about [PhysicalIsolation]. Whonix is an appetizer for the [Isolating Proxy Concept](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO/IsolatingProxy) and [Security by Isolation](http://theinvisiblethings.blogspot.com/2008/09/three-approaches-to-computer-security.html).

A secure replacement for Virtual Box is already in development. [Qubes OS](http://qubes-os.org/) is already in a productive state, it only lacks hardware support and it's being worked on. [TorVM for Qubes (qubes-tor)](http://qubes-os.org/trac/wiki/UserDoc/TorVM) was [inspired](https://github.com/abeluck/qubes-tor#acknowledgements) by Whonix. (See [Comparison with Others].)

The responsible thing to do form security perspective would have been in past, to switch from Windows to GNU/Linux and nowadays it would be to switch to Qubes OS. If you are most serious about Tor security, using Qubes OS + physical isolation would be the most secure way.

Many users are still on Windows or Linux. Whonix can right now fill the void and improve real world security. They are better using Whonix, which is up to date, actively maintained and developed than any seriously outdated projects like JanusVM.

Whonix can not serve all target audiences. The more security educated/interested people will use things like [PhysicalIsolation] or qubes-tor. Hardcore security educated/interested people will probable build their own custom hardened solutions, but can still profit from Whonix's research and source code. Those more hardened solutions, such as the [Hardened Gentoo Whonix-Gateway](https://sourceforge.net/p/whonix/wiki/HardenedGentooTG/) are more difficult to use and can therefore not be the default for Whonix.

**UPDATE 1**:
Using Whonix on top of Qubes OS looks now much easier. See [blog post](https://sourceforge.net/p/whonix/featureblog/2013/02/running-whonix-on-top-of-qubes-os-anyone-interested-unpacking-ova-images/).

# Will there be a Whonix Live CD or DVD? #
Unless someone joins the projects and contributes, what is very unlikely, this won't happen.

Whonix developer adrelanos has limited knowledge about Live CD/DVD creation. At the moment Whonix is a rather simple project. Many things, get delegated to upstream. Virtual Box features to run on various platforms, Debian provides a fine operating system, hardware support is delegated to the host operating system and Virtual Box, Tor is providing a fine anonymizer. Creating a Live CD /DVDwould be difficult, especially the hardware support. Whonix is also too big and that would be very difficult to fix, see [Why are the Whonix images so big?](https://sourceforge.net/p/whonix/wiki/FAQ/#why-are-the-whonix-images-so-big) above. Adrelanos lacks experience about Live CD/DVD deployment.

Tails and Liberte Linux are playing much better in the Anonymity Live CD/DVD market than adrelanos ever could. Adrelanos has no interest to compete in that market.

A clean way to do it would be to contribute to Tails instead, see [Tails wishlist: Two-layered virtualized system](https://tails.boum.org/todo/Two-layered_virtualized_system/). A similar feature was already implemented in Liberte Linux, but ultimately rejected ([reference](http://archives.seul.org/or/talk/Mar-2012/msg00248.html)).

For an alternative also next question below.

# Is there something like Whonix Live? #
Whonix runs fine when the host operating system is installed on external media.

There is a [Recommendation to use a dedicated host operating system](https://sourceforge.net/p/whonix/wiki/Pre%20Install%20Advice/#recommendation-to-use-a-dedicated-host-operating-system) and a [Recommendation to use Whonix on External Media](https://sourceforge.net/p/whonix/wiki/Pre%20Install%20Advice/#recommendation-to-use-whonix-on-external-media).

It's the user's responsibility to honor that advice.

# Why I can't ping the Whonix-Gateway? #
Whonix-Gateway is firewalled (see */usr/local/bin/whonix_firewall* or in Whonix source code) and does not answer to ping (-like) commands for security reasons. You don't need to ping the Gateway.

If you really want to ping the Gateway and really want some uber special setup you can test wise clear all firewall rules with the */usr/local/bin/dev_clearnet* script. It's for experts only and you need to comment out the *exit 0* at the beginning.

# You should add full disk encryption to Whonix! #
**Short**:
No, you should add full disk encryption to your host!

**Long**:
It is technically impossible to ship Whonix with an encrypted disk for several reasons.

While you can change the password for a luks/TrueCrypt/whatever volume, only the password for the masterkey gets replaced. The masterkey itself remains unchanged. (The masterkey is NOT some kind of backdoor, it's just how things work. Otherwise you would have to re-encrypt each time you want to change the password.)

In Whonix the masterkey would be known to everyone who downloads and changing the password wouldn't change the masterkey.

So all that could be added would be an option to encrypt it with a freshly and locally created masterkey (and user chosen password) after the user downloaded Whonix.

Two problems. There is no "encrypt after installing" software for Linux, like there is TrueCrypt for Windows.

The other one is, that the host can swap to the disk and therefore leak stuff to the perhaps unencrypted host disk.

Therefore the only secure solution is recommend in the Advanced Security Guide:
Full disk encryption should be applied on the host.

# Speed up the Whonix-Gateway? Speed up Tor? #
*Is there a way to configure the number of nodes in a circuit and to allow selection according to their speeds?*

[Remember, Whonix is based on Debian, KDE, VirtualBox and Tor. It is nothing very special.](https://sourceforge.net/p/whonix/wiki/About/#whonix-is-based-on-debian-virtualbox-and-tor) Therefore Whonix does not limit Tor and your options in any way.

If you learn how to configure Tor in such a way in Debian command line, you also learned how to do it in Whonix-Gateway. While it's possible to learn it yourself and do manually, this is recommend against in Whonix-Gateway since also the Tor developers recommend against it.

For this reasons there are no instructions in Whonix documentation how to do it. If you find general instructions the only thing changing would be that you do it in Whonix-Gateway instead on the host.

Please see also next question below.

# Does Whonix modify Tor? #
**NO!**

Tor's configuration file has been adapted for Whonix. There are no patches to Tor. The normal Debian Tor package is being used in Whonix.

Whonix tries to be as less special as possible to ease security auditing of Whonix. Any changes to the Tor routing algorithm should be proposed, discussed and eventually implemented upstream in Tor on torproject.org. And if discussion fails, a Tor fork could be created. Tor has already been forked at least once. Doing such changes directly in Whonix would limit discussions about Whonix to the security of the modified routing algorithm. To allow further exploration of Whonix security, it is required to be as agnostic as possible about all parts of Whonix.

# Why doesn't Whonix improve Tor? #
Please see the question above.

Creating Whonix is difficult and time consuming enough. Improving Tor is left to the people who are better at this job. Any bugs/suggestions related to torproject.org will of course be reported. [Happens.](https://sourceforge.net/p/whonix/wiki/Threat%20Model/#design-document-innovations-and-research)

# Can you improve Tor? #
No.

Any improvements to Tor should be proposed upstream. If adrelanos finds a bug or has a suggestion it will be proposed upstream on torproject.org. [Happens.](https://sourceforge.net/p/whonix/wiki/Threat%20Model/#design-document-innovations-and-research)

For reasons why there is no improved version of Tor in Whonix see the question "Does Whonix modify Tor?" above.

Anyone unhappy with Tor should provide patches upstream and as last resort fork it. Hypothetically, if the fork gets better respected than the original project, then Whonix will of course seriously consider switching.

# You should disable Java Script by default! #
No, this isn't a good idea for many reasons.

Whonix is a anonymity distribution gluing together concepts, which are generally respected by educated people and known to work reliable. It's not a browser project trying to create a secure browser such as "Privacy Browser - solves all browser fingerprinting problems". Whonix does not have to manpower to create such a browser. In theory, and even if it had, it would make more sense to create a new project "Privacy Browser" and when it gets better than Tor Browser to use re-configure Whonix to use "Privacy Browser" instead of Tor Browser. 

Whonix also doesn't modify Tor Browser for the same reasons also listed in the already above answered questions "Does Whonix modify Tor?", "Why doesn't Whonix improve Tor?" and "Can you improve Tor?".

Whonix includes Tor Browser and with only [minor](https://sourceforge.net/p/whonix/wiki/TorBrowser/#tor-browser-in-whonix-differences) differences, such as proxy settings for [Stream Isolation].

Mike Perry, developer of Tor Browser has also made a good posting why it's better to have Java Script enabled in Tor Browser by default, see [tor-talk Tor Browser disabling Javascript anonymity set reduction](https://lists.torproject.org/pipermail/tor-talk/2012-May/024227.html). In summary to his post, Tor Button and the Tor Browser patches to handle the most serious issues related to Java Script. There are no IP/location bypass problems. Although there are outstanding issues ^1^ ^2^, deactivating Java Script by default couldn't attract enough users with without enough users there is also no anonymity. When someone deactivates Java Script it may be even more fingerpintable, depending on how many disable Java Script, what no one really knows.

Last, but definitively not least, Whonix shares the same [Fingerprint] as other Tor Browser Bundle users, which is good for anonymity.

<font size="-3">
,,
^1^ [tbb-fingerprinting](https://trac.torproject.org/projects/tor/query?keywords=~tbb-fingerprinting)
^2^ [tbb-linkability](https://trac.torproject.org/projects/tor/query?keywords=~tbb-linkability)
</font>

# How difficult is it to develop Whonix?
See [FAQ2].

# What is clearnet?
See [FAQ2].

# Can I use DNSCrypt in Whonix?
See [FAQ2].

# Why not use DNSCrypt as default for Whonix?
See [FAQ2].

# Can I use DNSCrypt on the host, in my router, for clearnet?
See [FAQ2].

# Does DNSCrypt on the host or in my router, harm anonymity when using Tor/Whonix?
See [FAQ2].

# Footer #
[[include ref=WikiFooter]]