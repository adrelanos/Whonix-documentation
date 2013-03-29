[[include ref=WikiHeader]]

[TOC]

# Operating System #
## Introduction ##
This chapter applies to the host(s), Whonix-Gateway and Whonix-Workstation.

*Whonix Example Implementation* is currently based on Debian. There are development discussions about switching to [Qubes OS](http://qubes-os.org), BSD, Alpine Linux or other secure operating systems.

Also the [FAQ](https://sourceforge.net/p/whonix/wiki/FAQ/) contains information about this topic.

Whonix can't protect against malicious code inserted into upstream operating system infrastructure. Debian ensures some chain of trust as it requires contributors to sign commits.

## Switch from Ubuntu to Debian ##
Beginning from 0.4.4, *Whonix Example Implementation* is based on Debian. Previously it was based on Ubuntu. From technical view, Ubuntu was a good choice, see [About Ubuntu](https://sourceforge.net/p/whonix/wiki/OtherOperatingSystems/#about-ubuntu) if you are interested.

The switch was due to Ubuntu Trademark issues, see [About Ubuntu Trademark](http://www.ubuntu.com/aboutus/trademarkpolicy). The terms are long and complicated. Since Whonix's changes are beyond a *remix* (as defined in Ubuntu Licensing), Whonix would either to have to ask for a license, which they reserve to revoke. Such a legally insecure state is not acceptable. Or Whonix would have to rebrand Ubuntu. It would be possible in theory, but in practice it would require a lot work to remove all Ubuntu strings. [Even new apt mirrors would be required](https://lists.ubuntu.com/archives/ubuntu-users/2012-September/263760.html), which is much beyond the manpower of the Whonix project.

Debian is much more free. According to Debian project leader Stefano Zacchiroli (in private mail), there are no trademark issues as long as the derivative does not claim to be Debian. That is easy to fulfill.

Derivatives of Debian are even encouraged to use Debian infrastructure, see [Derivatives/Guidelines](http://wiki.debian.org/Derivatives/Guidelines). Debian even supports derivatives. There is a lot documentation, see [Derivatives](http://wiki.debian.org/Derivatives) and even a [debian-derivatives mailing list](http://lists.debian.org/debian-derivatives/).

## About Debian ##
### General ###
As in 2012 Debian Squeeze is still Debian stable and Debian Wheezy is still Debian testing. Thus, as long as Wheezy does not get released as stable, Whonix is based on testing. Wheezy is used as codename in */etc/apt/sources.list*, not testing. Whonix developer adrelanos looks forward for Wheezy becoming the stable distribution.

Although the [Debian security FAQ](http://www.debian.org/security/faq) states, that stable gets more attention from the security team, Wheezy is in adrelanos opinion a better choice. Wheezy, in comparison to Squeeze, has hardening options activated, see [Debian Wiki Hardening](http://wiki.debian.org/Hardening). It can't be so bad anyway, since many distributions are based on Debian testing and/or even Debian sid (unstable).

[checksec.sh](http://www.trapkit.de/tools/checksec.html) --kernel reports good kernel protection: GCC stack protector support, Enforce read-only kernel data, Restrict /dev/mem and /dev/kmem access are all enabled!

Related statements from the FAQ reasoning why Debian is the base for Whonix Example Implementation:

* [Why are the Whonix images so big?](https://sourceforge.net/p/whonix/wiki/FAQ/#why-are-the-whonix-images-so-big)
* [Why not use a Live CDs as Whonix-Workstation operating system?](https://sourceforge.net/p/whonix/wiki/FAQ/#why-not-use-a-live-cds-as-whonix-workstation-operating-system)
* [Why is KDE (big) the default desktop environment? Why not use a minimal DE?](https://sourceforge.net/p/whonix/wiki/FAQ/#why-is-kde-big-the-default-desktop-environment-why-not-use-a-minimal-de)
* [Why aren't you using OpenBSD, it's the most secure OS ever!!!1!](https://sourceforge.net/p/whonix/wiki/FAQ/#why-arent-you-using-openbsd-its-the-most-secure-os-ever1)

General explanation, why so many distributions are based on Debian:

* [why there are so many debian derivatives](http://upsilon.cc/~zack/blog/posts/2011/09/why_there_are_so_many_debian_derivatives/)

Related:

* [Derivatives Census Whonix](http://wiki.debian.org/Derivatives/Census/Whonix)
* [RelationshipWithUpstream]

### Harden Debian ###
moved to https://sourceforge.net/p/whonix/wiki/Advanced%20Security%20Guide/

### Popularity Contest ###
The Debian *popularity-contest* package popcon is **disabled** Whonix.

[popcon readme](http://popcon.debian.org/README) | [popcon faq](http://popcon.debian.org/FAQ) | [popcon bugs](http://bugs.debian.org/cgi-bin/pkgreport.cgi?pkg=popularity-contest) | [popularity contest mailing list](http://lists.alioth.debian.org/cgi-bin/mailman/listinfo/popcon-developers) | [popularity contest mailing list: Drop atime and ctime for privacy reasons possible?](http://lists.alioth.debian.org/pipermail/popcon-developers/2012-October/002172.html)

Some privacy considerations and reasons why it's disabled:

* The connection would obviously need to go over it's own Tor circuit (stream isolation). At the moment popcon tries to go through http and if it fails (no internet connectivity) it goes into the mail queue. (sendmail) Sendmail proable works though TransPort, but I don't know if it can be torified for proper stream isolation.
* (From the popcon readme) "*Each popularity-contest host is identified by a random 128bit uuid (MY_HOSTID in /etc/popularity-contest.conf).*" - This would allow to enumerate a quite good guess about the amount number of Whonix users. I am not sure if sourceforge could already have an insight about that (see whonixcheck) or about any other negative implications.
* MY_HOSTID would probable get created a Whonix build time and all Whonix users would have the same MY_HOSTID, which would make it useless. A new MY_HOSTID would have to be created at first boot of Whonix.
* Popcon runs at a random day. Good.
* If the machine is powered on: it runs at at 6:47, which is bad, because a local adversary (ISP or hotspot) could guess popcon runs over Tor which would likely be a Whonix user.
* If the machine as powered off at 6:47, it sends the report later, only if anachron is installed. It shouldn't run instantly after powering on, also for fingerprinting reasons. The time would have to be truly randomized.
* The transmission is not encrypted, see [popularity-contest should encrypt contents](http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=480860) and it's not planed to encrypt it. Malicious Tor exit nodes could modify the transmission, but this is only a minor issue. Such malicious Tor exit nodes could send fake transmissions on their own.
* It's questionable if and if yes, how long Debian will accept popularity contest transmissions from Tor exit nodes. There is potential for electoral fraud.

For these reasons it's not a good idea to add popcon to Whonix. If you have suggestions or a different view, please get in contact.

## About Ubuntu ##
Moved to [Other Operating Systems / About Ubuntu](https://sourceforge.net/p/whonix/wiki/OtherOperatingSystems/#about-ubuntu).

## Harden Software Repositories ##
Moved to https://sourceforge.net/p/whonix/wiki/Advanced%20Security%20Guide/

## About grsecurity ##
Moved to https://sourceforge.net/p/whonix/wiki/Advanced%20Security%20Guide/

## Why don't you use <your favorite most secure operating system\> for Whonix?
Why do you use Debian, and not...

The operating system must have

* acceptable usability
* must be somewhat popular, because only that leads to sufficient public scrutiny and enough available documentation.
* For redistribution of Whonix, there may also not be any legal/trademark issues such as with Ubuntu. (See "Switch from Ubuntu to Debian" chapter above).
* Must have a secure operating system updater (package manager), i.e. must not fall through the [TUF Threat Model](https://www.updateframework.com/wiki/Docs/Security#AttacksandWeaknesses) ([w](http://www.webcitation.org/6F7Io2ncN)).

Debian is good compromise of security and usability.

By the way, this chapter won't only include examples which fall through Whonix's threat model.

There might be more secure operating systems, such as [Hardenend](http://wiki.gentoo.org/wiki/Hardened_Gentoo) [Genntoo](http://www.gentoo.org/proj/en/hardened/), but in adrelanos opinion mortal users are unlikely to learn how to use them. More paranoids (and others) are welcome to use them for example as host operating system and leave feedback.

OpenBSD is recommend against, because it completely falls through the Whonix threat model, see FAQ entry: [Why aren't you using OpenBSD, it's the most secure OS ever!!!1!](https://sourceforge.net/p/whonix/wiki/FAQ/#why-arent-you-using-openbsd-its-the-most-secure-os-ever1)

FreeBSD and OpenWRT have their own FAQ entries you could look into.

* FreeBSD https://sourceforge.net/p/whonix/wiki/FAQ/#why-dont-you-use-freebsd-which-is-more-secure
* OpenWRT https://sourceforge.net/p/whonix/wiki/FAQ/#why-dont-you-use-openwrt-which-is-more-secure

Ubuntu isn't used as Whonix-Gateway/Workstation operating system for legal reasons (as said above) and was lately negatively perceived due to privacy issues, so it's recommend against as host operating system as well.

Alpine Linux [doesn't package Tor yet](http://bugs.alpinelinux.org/issues/1067). Other than that, I didn't look thoroughly into it.

Fedora yet did **not** fall through Whonix's threat model and could be considered as host and future or alternative Whonix-Gateway/Workstation operating system. Also Qubes OS, an operating system focusing on security by isolation, is based on Fedora. Started considering it, help welcome, see [Fedora].

Qubes OS as host operating system would be most interesting. It just needs someone sufficiently motivated to do a little work to make it reality, see blog post [Running Whonix on top of Qubes OS, anyone interested?](https://sourceforge.net/p/whonix/featureblog/2013/02/running-whonix-on-top-of-qubes-os-anyone-interested-unpacking-ova-images/).

# Footer #
[[include ref=WikiFooter]]