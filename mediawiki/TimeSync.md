[[include ref=WikiHeader]]

[TOC]

= Time Synchronization Mechanism =

== Description ==

The Post Install Advice is part of this design, therefore read [https://sourceforge.net/p/whonix/wiki/Post%20Install%20Advice/#network-time-syncing Network Time Syncing] first please. Also please read the Advanced Security Guide chapter [https://sourceforge.net/p/whonix/wiki/Advanced%20Security%20Guide/#network-time-synchronization Network Time Syncing] as well.

For understanding Whonix's Time Synchronization Mechanism, it is required to know Virtual Box's time synchronization features:

* Virtual Box uses the hosts time if it needs to correct the time for guests.
* (Some of Virtual Box time synchronization features depend on guest additions.)
* By default Virtual Box corrects Virtual Machine guests virtual hardware system clock,
** when the they get powered on,
** when they resume from suspension and
** when their clock is more than X minutes off.

Facts: People have been using:

* the Tor Browser Bundle and Mozilla Firefox in parallel
* Tails inside VMs and Firefox on the host
* Tor Browser inside Whonix-Workstation and Mozilla Firefox on the host

Other facts:

* Almost no one and no operating system, is using Secure Network Time Synchronization or External Clocks by default. Most systems synchronize the system clock using unauthenticated NTP. An adversary tampering with NTP replies or malicious NTP server makes things even worse. Even if there were authenticated NTP there is a requirement for a distributed trust model.
* A system not using NTP or using authenticated NTP stands out form most other users.

Definitions:

* Time Sanity Check in context of Whonix: Is an init.d script, which checks, if the system clock is between build timestamp and expiration date (17 MAY 2033 10:00:00).

Attacks A correct system clock is crucial for many reasons:

* Attack (1) Replay attacks <sup>1</sup>
* Attack (2) Feeding old/outdated/known vulnerable updates and (https) certificates <sup>2</sup>
* Attack (3) deanonymizing <sup>3</sup>
* Attack (4) Linking all sessions to the same pseudonym <sup>4</sup>
* Attack (5) Locating hidden services. <sup>5</sup>

<font size="-3"> ,, <sup>1</sup> Replay old Tor consensus, see [https://tails.boum.org/contribute/design/Time_syncing/ Tails: Time syncing] for detailed explanation. <sup>2</sup> Cryptographic verification depends on system clock, i.e. a clock two years in past will accept certificates/updates, which have been expired/revoked for two years. <sup>3</sup> Javascript is enabled in Tor Button by default and javascript can be used to read the client's clock, see https://ip-check.info for demonstration. Also other applications do leak the client's clock, such as Thunderbird (patch has been proposed by TorBirdy developers) and https. Imagine the user connects to an adversary controlled webserver with Mozilla Firefox and connects to another adversary controlled websever with Tor Browser. As long as TBB upstream [https://trac.torproject.org/projects/tor/ticket/3059 Bug #3059: Find some way to deal with time-based fingerprints] is open, the adversary can link the anonymous and non-anonymous session, thus deanonymizing. <sup>4</sup> If the clock is too much off, it's also easy for an adversary's webserver to detect &quot;Oh, that's the Tor Browser user who's clock is X in past/future.&quot;, thus allowing the adversary to link all sessions to the same pseudonym. See Tor Browser upstream bug #3059: [https://trac.torproject.org/projects/tor/ticket/3059 Find some way to deal with time-based fingerprints]. <sup>5</sup> For hidden services a correct clock is curial, see: [http://www.cl.cam.ac.uk/~sjm217/papers/ccs06hotornot.pdf Hot or Not: Revealing Hidden Services by their Clock Skew]; [http://caia.swin.edu.au/talks/CAIA-TALK-080728A.pdf An improved clock-skew measurement technique for revealing hidden services]; [http://people.cs.umass.edu/~elisha/Papers/SkewMask%20-%20final%20version.pdf SkewMask: Frustrating Clock Skew Fingerprinting Attempts] </font>

Whonix's Time Synchronization Mechanism:

* Whonix leaves the host's system clock or time synchronization mechanism untouched.
* Whonix-Gateway and Whonix-Workstation are based on Virtual Box and therefore have their own virtual hardware system clocks.
* Most Virtual Box time synchronization features get disabled by Whonix.
** Guest additions time synchronization gets disabled in ''/etc/init.d/htpdate'' at run time. See Virtual Box bug report [https://www.virtualbox.org/ticket/10828 VBoxService --disable-timesync broken]. They say it's actually not a bug. It's a missing feature, that running instances of VBoxService can not be modified in their settings. Whonix would need to edit ''/etc/init.d/vboxadd-service'' by adding ''--disable-timesync'' [https://www.virtualbox.org/ticket/2928 source]. Whonix developer adrelanos does not see a reliable way to do so. If the guest additions get automatically updated in future the option would get overwritten. That's why Whonix added a line in ''/etc/init.d/htpdate'' to turn it off completely. Guest additions time synchronization gets disabled, but the rest of the guest additions continues to work fine. Unless you have a better idea, it's an acceptable workaround.
** built in time synchronization features get disabled by ''VBoxManage setextradata &quot;$VMNAME&quot; &quot;VBoxInternal/Devices/VMMDev/0/Config/GetHostTimeDisabled&quot; &quot;1&quot;'' at build time.
* Whonix-Gateway and Whonix-Workstation
** When get powered on, they still get their time from the host. The user is advised to modify the biossystemtimeoffset in Advanced Security Guide, chapter [https://sourceforge.net/p/whonix/wiki/Advanced%20Security%20Guide/#network-time-synchronization Network Time Synchronization]. <sup>6</sup>
** 0.6.2 and above: Time Sanity Check before tails_htp will be executed, this ensures, that the host clock is sane and not slow in 1980. User gets advised to fix its host clock in such cases.
** After they are connected to the Tor network, they use a modified [https://tails.boum.org/contribute/design/Time_syncing/ tails_htp] to set the system clock. <sup>7</sup>
** 0.6.2 and above: Time Sanity Check after tails_htp was executed. This should catch eventual bigger bugs and attacks. User gets informed if it fails.
* On Whonix-Workstation,
** Using Boot Clock Randomization (Whonix 0.6.2 and above), i.e. after boot, the clock is set randomly between 5 and 180 seconds into the past or future. This is useful to enforce the design goal, that the host clock and Whonix-Workstation clock should always slightly differ. It's also useful to obfuscate the clock when tails_htp itself is running, because naturally at this time, tails_htp hasn't finished.
** Every hour, at a random time, tails_htp will set the clock again. This is useful for machines running for long time periods without reboot.
** An adversary could guess if someone is running a hidden services with constant clock adjustments, that it's hosted inside a Whonix-Workstation. It's unknown if the clock adjustments by tails_htp are big enough to enable an adversary to guess that.
*** '''TODO''': Open question... &quot;''ntpd adjusts the clock in small steps so that the timescale is effectively continuous and without discontinuities''&quot; - is that possible with an tails_htp like appraoch as well?
* Whonix-Gateway
** Doesn't use Boot Clock Randomization. If the assumption is correct, that the ISP can detect clock jumps by observing Tor's TLS client hello, clock jumps should be avoided to prevent fingerprinting Whonix users.
** Uses tails_htp after booting.
** Using it at all is better against Attack (1) when using a bridge.
** '''TODO''': Open question, run tails_htp also every hour at a random time on Whonix-Gateway?
*** The entry guard or bridge can see the time through TCP timestamp. <sup>10</sup>; <sup>11</sup>
*** Continuous clock jumps could help the entry guard or bridge guessing, that a Whonix-Gateway is connected.
*** '''TODO''': Open question... &quot;''ntpd adjusts the clock in small steps so that the timescale is effectively continuous and without discontinuities''&quot; - is that possible with an tails_htp like appraoch as well?
* Hardware Clock:
** Whonix-Gateway: since Whonix 0.5.6, set to UTC. Tor leaks it <sup>10</sup> <sup>11</sup>, but that is of no concern. Tor in running on Linux and Linux is expected to be run in UTC. Therefore there is no point to set it to the local time zone of the user.
** Whonix-Workstation: set to UTC
* tails_htp runs at non predictable times to prevent the ISP or Tor guard/bridge node to guess, that the user is running Whonix.
* Implementation details are in Design-Shared, chapter [https://sourceforge.net/p/whonix/wiki/Design-Shared/#timesync TimeSync] and in [Dev_timesync].
* That will reach the design goal, that all clocks, the host's, Whonix-Gateway's and Whonix-Workstation's slightly differ.

Thus,

* Attack (1) is a general Tor problem. It is impossible to solve for Whonix. It is unsolved in other projects as well.
* Attack (2) gets partially defeated.
** Whonix-Gateway and Whonix-Workstation are immune.
** This problem is unsolved in other projects as well.
*** This is general problem with all operating systems.
*** The host is still at risk.
*** [http://brainstorm.ubuntu.com/idea/30050/ Ubuntu Brainstorm Idea #30050: Secure Network Time Synchronization]
*** [http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=%23687166 Debian Bug Report ntp: NTP security vulnerability because not using authentication by default]
*** [https://bugs.launchpad.net/ubuntu/+source/ntp/+bug/1039420 Ubuntu Bug Report NTP security vulnerability because not using authentication by default]
** Manual workaround: Check your clock manually and read [https://sourceforge.net/p/whonix/wiki/OtherOperatingSystems/#about-ubuntu About Ubuntu] (stale mirror attack). ([https://bugs.launchpad.net/launchpad/+bug/716535 Bug #716535: Please support Valid-Until in release files for security.ubuntu.com])
* Attack (3) gets defeated, Whonix adds additional security.
* Attack (4) gets defeated, Whonix adds additional security.
* Attack (5) is a general Tor problem, which can not be solved by Whonix and which is unsolved in other projects as well. Since host, Whonix-Gateway and Whonix-Workstation time all differ, this attack at least becomes harder against Whonix.

When the user powers on Whonix-Gateway and the host time is too much off, it will not be able to connect to the Tor network. It is advised, when powering on Whonix-Gateway, to check that the host time is no more than 1 hour in past or more than 3 hour in future. <sup>8</sup> An adversary tampering with the users clock while the user doesn't recognize can't do any more damage to Whonix than he could do the the Tor Browser Bundle. All that happens is a denial of service. On the other hand, an adversary capable of actively tampering with the traffic between the user and it's entry guard or bridge poses much bigger risks to Tor in general. <sup>9</sup>

<font size="-3"> ,, <sup>6</sup> Developer information: If we needed or wanted to render the hardware clock unusable, we could set Virtual Box ''--biossystemtimeoffset'' several decades in past or future. <sup>7</sup> Stream isolation has been added, for Whonix's tails_htp implementation, see [Dev_timesync] i.e. people using Tor Browser prevent notifying their exit node, that they are tails_htp or Whonix users. <sup>8</sup> [https://lists.torproject.org/pipermail/tor-talk/2012-February/023264.html source of information] <sup>9</sup> General Tor problems, Tor is known to be broken against many active attacks. This can not be solved by Whonix. When an adversary is capable of running active attacks, tampering with the time leading into a denial of service is the least of the worries. The adversary could also disrupt the service easier. And as for active attacking in general, there are other attacks which are easier to deploy and which pose a greater danger. Not a Whonix specific problems. <sup>10</sup> [https://trac.torproject.org/projects/tor/ticket/7277 torproject.org #7277: timestamp leaked in TLS client hello] <sup>11</sup> [https://trac.torproject.org/projects/tor/ticket/4852 torproject.org #4852: Clients send NETINFO with time] </font>

== Implementation ==

See Design-Shared, chapter [https://sourceforge.net/p/whonix/wiki/Design-Shared/#timesync TimeSync] and [Dev_timesync].

== curl timeout ==

[https://mailman.boum.org/pipermail/tails-dev/2013-February/002635.html Tails-dev Endless Data Attack and Defense]

== Previous Discussion ==

* [https://lists.torproject.org/pipermail/tor-talk/2011-January/008551.html System time in anonymity oriented LiveCDs]

== Other Projects ==

* [https://tails.boum.org/contribute/design/Time_syncing/ Tails Design: Time synching]
* https://docs.google.com/a/chromium.org/document/d/1ylaCHabUIHoKRJQWhBxqQ5Vck270fX7XCWBdiJofHbU/edit

== Comparison with Others ==

[https://sourceforge.net/p/whonix/wiki/Comparison%20with%20Others/#network-time-related Network Time related]

== External Clock ==

This topic is still under research. Help is welcome.

It might make sense to add an external clock, such as a GPS, or even better an atomic clock. (Can we get an atomic USB clock?) This clock should be added to the host and/or Whonix-Gateway and/or Whonix-Workstation?

Open question: would the GPS/atomic clock be too accurate and would that make more Whonix fingerprintable?

== Tickets ==

* [https://trac.torproject.org/projects/tor/ticket/6894 torproject.org #6894 answer network time requests]
* [https://tails.boum.org/todo/robust_time_syncing/ Tails Todo: robust time syncing]
* [https://tails.boum.org/todo/safer_tordate_parameters/ Tails Todo: safer tordate parameters (always use tordate)]
* [https://tails.boum.org/todo/bridge_mode_vs_tordate_timeouts/ Tails Todo: bridge mode vs tordate timeouts]
* [https://tails.boum.org/todo/when_htp_fails_the_user_should_be_prompted/ Tails Todo: when htp fails the user should be prompted]

= Footer =

[[include ref=WikiFooter]]

