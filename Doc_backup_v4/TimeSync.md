[[include ref=WikiHeader]]

[TOC]

# Time Synchronization Mechanism #
## Description ##
The Post Install Advice is part of this design, therefore read [Network Time Syncing](https://sourceforge.net/p/whonix/wiki/Post%20Install%20Advice/#network-time-syncing) first please. Also please read the Advanced Security Guide chapter [Network Time Syncing](https://sourceforge.net/p/whonix/wiki/Advanced%20Security%20Guide/#network-time-synchronization) as well.

For understanding Whonix's Time Synchronization Mechanism, it is required to know Virtual Box's time synchronization features:

* Virtual Box uses the hosts time if it needs to correct the time for guests.
* (Some of Virtual Box time synchronization features depend on guest additions.)
* By default Virtual Box corrects Virtual Machine guests virtual hardware system clock,
    * when the they get powered on,
    * when they resume from suspension and
    * when their clock is more than X minutes off.

Facts: 
People have been using:

* the Tor Browser Bundle and Mozilla Firefox in parallel
* Tails inside VMs and Firefox on the host
* Tor Browser inside Whonix-Workstation and Mozilla Firefox on the host

Other facts:

* Almost no one and no operating system, is using Secure Network Time Synchronization or External Clocks by default. Most systems synchronize the system clock using unauthenticated NTP. An adversary tampering with NTP replies or malicious NTP server makes things even worse. Even if there were authenticated NTP there is a requirement for a distributed trust model.
* A system not using NTP or using authenticated NTP stands out form most other users.

Attacks 
A correct system clock is crucial for many reasons:

* Attack (1) Replay attacks ^1^
* Attack (2) Feeding old/outdated/known vulnerable updates and (https) certificates ^2^
* Attack (3) deanonymizing ^3^
* Attack (4) Linking all sessions to the same pseudonym ^4^
* Attack (5) Locating hidden services. ^5^

<font size="-3">
,,
^1^ Replay old Tor consensus, see [Tails: Time syncing](https://tails.boum.org/contribute/design/Time_syncing/) for detailed explanation. 
^2^ Cryptographic verification depends on system clock, i.e. a clock two years in past will accept certificates/updates, which have been expired/revoked for two years. 
^3^ Javascript is enabled in Tor Button by default and javascript can be used to read the client's clock, see https://ip-check.info for demonstration. Also other applications do leak the client's clock, such as Thunderbird (patch has been proposed by TorBirdy developers) and https. Imagine the user connects to an adversary controlled webserver with Mozilla Firefox and connects to another adversary controlled websever with Tor Browser. As long as TBB upstream [Bug #3059: Find some way to deal with time-based fingerprints](https://trac.torproject.org/projects/tor/ticket/3059) is open, the adversary can link the anonymous and non-anonymous session, thus deanonymizing. 
^4^ If the clock is too much off, it's also easy for an adversary's webserver to detect "Oh, that's the Tor Browser user who's clock is X in past/future.", thus allowing the adversary to link all sessions to the same pseudonym. See Tor Browser upstream bug #3059: [Find some way to deal with time-based fingerprints](https://trac.torproject.org/projects/tor/ticket/3059).
^5^ For hidden services a correct clock is curial, see:
[Hot or Not: Revealing Hidden Services by their Clock Skew](http://www.cl.cam.ac.uk/~sjm217/papers/ccs06hotornot.pdf);
[An improved clock-skew measurement technique for revealing hidden services](http://caia.swin.edu.au/talks/CAIA-TALK-080728A.pdf);
[SkewMask: Frustrating Clock Skew Fingerprinting Attempts](http://people.cs.umass.edu/~elisha/Papers/SkewMask%20-%20final%20version.pdf)
</font>

Whonix's Time Synchronization Mechanism:

* Whonix leaves the host's system clock or time synchronization mechanism untouched.
* Whonix-Gateway and Whonix-Workstation are based on Virtual Box and therefore have their own virtual hardware system clocks.
* Most Virtual Box time synchronization features get disabled by Whonix.
    * Guest additions time synchronization gets disabled in */etc/init.d/htpdate* at run time. See Virtual Box bug report [VBoxService --disable-timesync broken](https://www.virtualbox.org/ticket/10828). They say it's actually not a bug. It's a missing feature, that running instances of VBoxService can not be modified in their settings. Whonix would need to edit */etc/init.d/vboxadd-service* by adding *--disable-timesync* [source](https://www.virtualbox.org/ticket/2928). Whonix developer adrelanos does not see a reliable way to do so. If the guest additions get automatically updated in future the option would get overwritten. That's why Whonix added a line in */etc/init.d/htpdate* to turn it off completely. Guest additions time synchronization gets disabled, but the rest of the guest additions continues to work fine. Unless you have a better idea, it's an acceptable workaround.
    * built in time synchronization features get disabled by *VBoxManage setextradata "$VMNAME" "VBoxInternal/Devices/VMMDev/0/Config/GetHostTimeDisabled" "1"* at build time.
* When Whonix-Gateway or Whonix-Workstation get powered on, they still get their time from the host, but the user is advised to modify the biossystemtimeoffset. ^6^
* After Whonix-Gateway and Whonix-Workstation are connected to the Tor network, they use a modified [tails_htp](https://tails.boum.org/contribute/design/Time_syncing/) to set the system clock. ^7^
* On Whonix-Workstation,
    * every hour, at a random time, tails_htp will set the clock again.
    * This is useful for machines running for long time periods without reboot.
    * An adversary could guess if someone is running a hidden services with constant clock adjustments, that it's hosted inside a Whonix-Workstation. It's unknown if the clock adjustments by tails_htp are big enough to enable an adversary to guess that.
        * **TODO**: Open question... "*ntpd adjusts the clock in small steps so that the timescale is effectively continuous and without discontinuities*" - is that possible with an tails_htp like appraoch as well?
* Whonix-Gateway
    * Uses tails_htp after booting.
    * Using it at all is better against Attack (1) when using a bridge.
    * **TODO**: Open question, run tails_htp also every hour at a random time on Whonix-Gateway?
        * The entry guard or bridge can see the time through TCP timestamp. ^10^; ^11^
        * Continuous clock jumps could help the entry guard or bridge guessing, that a Whonix-Gateway is connected.
        * **TODO**: Open question... "*ntpd adjusts the clock in small steps so that the timescale is effectively continuous and without discontinuities*" - is that possible with an tails_htp like appraoch as well?

* Hardware Clock:
    * Whonix-Gateway: since Whonix 0.5.6, set to UTC. Tor leaks it ^10^ ^11^, but that is of no concern. Tor in running on Linux and Linux is expected to be run in UTC. Therefore there is no point to set it to the local time zone of the user.
    * Whonix-Workstation: set to UTC
* tails_htp runs at non predictable times to prevent the ISP or Tor guard/bridge node to guess, that the user is running Whonix.
* Implementation details are in [Dev_timesync].
* That will reach the design goal, that all clocks, the host's, Whonix-Gateway's and Whonix-Workstation's slightly differ.

Thus,

* Attack (1) is a general Tor problem. It is impossible to solve for Whonix. It is unsolved in other projects as well.
* Attack (2) gets partially defeated.
    * Whonix-Gateway and Whonix-Workstation are immune.
    * This problem is unsolved in other projects as well.
        * This is general problem with all operating systems.
        * The host is still at risk.
        * [Ubuntu Brainstorm Idea #30050: Secure Network Time Synchronization](http://brainstorm.ubuntu.com/idea/30050/)
        * [Debian Bug Report ntp: NTP security vulnerability because not using authentication by default](http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=%23687166)
        * [Ubuntu Bug Report NTP security vulnerability because not using authentication by default ](https://bugs.launchpad.net/ubuntu/+source/ntp/+bug/1039420)
    * Manual workaround: Check your clock manually and read [About Ubuntu](https://sourceforge.net/p/whonix/wiki/OtherOperatingSystems/#about-ubuntu) (stale mirror attack). ([Bug #716535: Please support Valid-Until in release files for security.ubuntu.com](https://bugs.launchpad.net/launchpad/+bug/716535))
* Attack (3) gets defeated, Whonix adds additional security.
* Attack (4) gets defeated, Whonix adds additional security.
* Attack (5) is a general Tor problem, which can not be solved by Whonix and which is unsolved in other projects as well. Since host, Whonix-Gateway and Whonix-Workstation time all differ this attack at least becomes harder against Whonix.

When the user powers on Whonix-Gateway and the host time is too much off, it will not be able to connect to the Tor network. It is advised, when powering on Whonix-Gateway, to check that the host time is no more than 1 hour in past or more than 3 hour in future. ^8^ An adversary tampering with the users clock while the user doesn't recognize can't do any more damage to Whonix than he could do the the Tor Browser Bundle. All that happens is a denial of service. On the other hand, an adversary capable of actively tampering with the traffic between the user and it's entry guard or bridge poses much bigger risks to Tor in general. ^9^

<font size="-3">
,,
^6^ Developer information: If we needed or wanted to render the hardware clock unusable, we could set Virtual Box *--biossystemtimeoffset* several decades in past or future. 
^7^ Stream isolation has been added, for Whonix's tails_htp implementation, see [Dev_timesync] i.e. people using Tor Browser prevent notifying their exit node, that they are tails_htp or Whonix users. 
^8^ [source of information](https://lists.torproject.org/pipermail/tor-talk/2012-February/023264.html)
^9^ General Tor problems, Tor is known to be broken against many active attacks. This can not be solved by Whonix. When an adversary is capable of running active attacks, tampering with the time leading into a denial of service is the least of the worries. The adversary could also disrupt the service easier. And as for active attacking in general, there are other attacks which are easier to deploy and which pose a greater danger. Not a Whonix specific problems.
^10^ [torproject.org #7277: timestamp leaked in TLS client hello](https://trac.torproject.org/projects/tor/ticket/7277)
^11^ [torproject.org #4852: Clients send NETINFO with time](https://trac.torproject.org/projects/tor/ticket/4852)
</font>

## Previous Discussion ##
* [System time in anonymity oriented LiveCDs](https://lists.torproject.org/pipermail/tor-talk/2011-January/008551.html)

## Other Projects ##
* [Tails Design: Time synching](https://tails.boum.org/contribute/design/Time_syncing/)

## Comparison with Others ##
[Network Time related](https://sourceforge.net/p/whonix/wiki/Comparison%20with%20Others/#network-time-related)

## External Clock ##
This topic is still under research. Help is welcome.

It might make sense to add an external clock, such as a GPS, or even better an atomic clock. (Can we get an atomic USB clock?) This clock should be added to the host and/or Whonix-Gateway and/or Whonix-Workstation?

Open question: would the GPS/atomic clock be too accurate and would that make more Whonix fingerprintable?

## Tickets ##
* [torproject.org #6894 answer network time requests](https://trac.torproject.org/projects/tor/ticket/6894)
* [Tails Todo: robust time syncing](https://tails.boum.org/todo/robust_time_syncing/)
* [Tails Todo: safer tordate parameters (always use tordate)](https://tails.boum.org/todo/safer_tordate_parameters/)
* [Tails Todo: bridge mode vs tordate timeouts](https://tails.boum.org/todo/bridge_mode_vs_tordate_timeouts/)

# Footer #
[[include ref=WikiFooter]]