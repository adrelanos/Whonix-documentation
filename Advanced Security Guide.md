[[include ref=WikiHeader]]

[TOC]

<!--
Copyright:

   Whonix Advanced Security Guide wiki page Copyright (C) Amnesia <amnesia at boum dot org>
   Whonix Advanced Security Guide wiki page Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
   
   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 3 of the License, or
   (at your option) any later version.
		 
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
	  
   You should have received a copy of the GNU General Public License
   along with this program; if not, write to:

	Free Software Foundation, Inc. 
	51 Franklin St, Fifth Floor
	Boston, MA 02110-1301, USA.

On Debian GNU/Linux systems, the complete text of the GNU General Public
License can be found in the /usr/share/common-licenses' directory.

The complete text of the GNU General Public License can also be found online on gnu.org <https://www.gnu.org/licenses/gpl.html>, in Whonix virtual machine images in /usr/share/common-licenses/GPL-3 file or in Whonix wiki on <https://sourceforge.net/p/whonix/wiki/GPLv3/>.
-->

<!--
This wiki page contains material from the of the Tails Protection against cold boot attacks  page, from this exact source <http://git.immerda.ch/?p=amnesia.git;a=blob;f=wiki/src/doc/advanced_topics/cold_boot_attacks.mdwn;hb=d249db72228b498407d85fb762b49ec155871ded>.
-->

# Basics #
Please understand the basics first, read the [Pre Install Advice] first!

# Network Time Synchronization #
Don't wonder... To prevent against time zone leaks, the system clock inside Whonix was set to UTC. This means it may be a few hours before or ahead of your host system clock. Do not change!

On the host. If you were a user of TorBOX 0.2.1 or below and removed NTP, restore it now.

        sudo apt-get install ntpd

Virtual Box has a feature to spoof the initial virtual hardware clock offset by setting the clock X milliseconds in feature or past.
Syntax.

	VBoxManage modifyvm <name> --biossystemtimeoffset -<milliseconds>
	VBoxManage modifyvm <name> --biossystemtimeoffset +<milliseconds>

It's prudent to add a random delay within the following range.

	VBoxManage modifyvm <name> --biossystemtimeoffset -60000
	VBoxManage modifyvm <name> --biossystemtimeoffset +60000

Pick one example per VM and use random values within the range. (On the host.)

	VBoxManage modifyvm "Whonix-Gateway" --biossystemtimeoffset -35017
	VBoxManage modifyvm "Whonix-Gateway" --biossystemtimeoffset +27931

	VBoxManage modifyvm "Whonix-Workstation" --biossystemtimeoffset -35017
	VBoxManage modifyvm "Whonix-Workstation" --biossystemtimeoffset +27931

Clock skew apart this small biossystemtimeoffset ^5^ is always bad for privacy ^1^.

When you suspend/safe the state of a VM, clock will stop and continue after resume, thus lag behind. You shouldn't suspend/safe the state of Whonix-Gateway. Rather power the Gateway off, if you no longer need it. ^2^ You can suspend/safe the state of Whonix-Workstation, but then the clock will lag behind. To fix it run inside Whonix-Workstation Start Menu -> Applications -> System -> Whonix Timesync.

The host system clock synchronization mechanism still uses unauthenticated NTP from a single source. This is not optimal, but there is no real solution to this problem. ^4^ The ISP and/or the time server could either non-intentionally or intentionally (as an attack) introduce a clock skew or the host clock could simply malfunction.

If the host clock is too much off, more than one hour in past or more than 3 hour in future, Tor can't connect to the Tor network. ^6^ The easiest fix in this situation is to manually fix the clock on the host, to power off Whonix-Gateway and to power on Whonix-Gateway again.

Another side effect of the host clock being too much off is, that downloading operating system updates on the host and cryptographic verification, such as verifying SSL certificates on the host browser may no longer be possible, until you manually fix the clock.

Before you think, your ISP is tampering with NTP, ensure first, that not simply the host clock is defect due to an empty battery.

If you should really ever catch your ISP tampering with NTP, you should probable disable it and manually update the host clock out of band, i.e. using a watch or atomic clock. In case it isn't a large scale attack, but a targeted attack, you most likely have already bigger problems to worry about than NTP. (See Warning page chapter [Confirmation attacks](https://sourceforge.net/p/whonix/wiki/Warning/#confirmation-attacks).)

You have also another option. You could disable NTP on your host and always manually adjust the clock out of band, i.e. using a watch or atomic clock. This might make your clearnet traffic more fingerprintable ^7^, since it introduces a device issuing clearnet traffic (at least operating system updates, I hope), but not using NTP. I don't know how many people deactivated/broken/uninstalled/never installed NTP. Neither I know, how many people are using alternative time synchronization methods such as authenticated NTP, tails_htp, tlsdate or similar. Search engine research however suggests, that very few people care and do so.

Summary:

* Needs to be done only after importing the Virtual Machine: Modify --biossystemtimeoffset for all Virtual Machines.
* Run Secure Network Time Synchronization after suspend/safe/resume or do not use suspend/safe/resume at all.
* Tor can't connect if the host clock is too much off. In this case manually fix the host clock, power off Whonix-Gateway and power on Whonix-Gateway again.
* Keep an eye on the host clock, ensure that it's always somewhat accurate.

<font size="-3">
Even though it's a difficult topic, you are advised to read Technical Design chapter [Whonix's Secure And Distributed Time Synchronization Mechanism](https://sourceforge.net/p/whonix/wiki/TimeSync/).
</font>

<font size="-3">
,,
Footnotes.
Additional information, reasoning, design for interested users, developers and auditors.
^1^ Can lead to linkability, thus would be [pseudonymous rather than anonymous](https://sourceforge.net/p/whonix/wiki/DoNot/#do-not-confuse-anonymity-with-pseudonymity). ^4^
^2^ Otherwise Tor can get confused if time is more than 1 hour in past or more than 3 hour in future and will only reconnect to the Tor network, if clock is manually fixed or powered off and powered on again. ^3^
^3^ Powering on a VM will initially synchronize the clock with the host clock until Whonix Timesync adjusts it.
^4^ See Design: [Whonix's Secure And Distributed Time Synchronization Mechanism](https://sourceforge.net/p/whonix/wiki/TimeSync/).
^5^ biossystemtimeoffset is being used, to unlink the initial clock synchronization of the VM by the Virtualizer from the host clock.
^6^ Because Tor can't verify the Tor consensus.
^7^ See [Fingerprint] page to find out what fingerprinting means in this case.
</font>

# Host Security #
## Recommendation to use Whonix with Physical Isolation ##
Whonix using Physical Isolation, setup using two different computers AND virtualization. This is the most secure Tor configuration to date. Unfortunately, it is difficult to setup. See [PhysicalIsolation].

## Hardening ##
General hardening recommendations apply.

* Minimize attack surface
* securely configure services
    * e.g. for ssh: use fail2ban, allow only key authentication),

Proactive Defenses

* [compile time hardening](http://wiki.debian.org/Hardening)
* [MAC](https://en.wikipedia.org/wiki/Mandatory_access_control)
* [IPS](https://en.wikipedia.org/wiki/Intrusion_prevention_system))

Retroactive Defenses

* The usefulness of this approach is limited. It doesn't prevent security breaches. It can only help making future breaches less likely.
* [rkhunter](https://en.wikipedia.org/wiki/Rkhunter)
* IDS (Intrusion Detection System)
* [Snort](https://en.wikipedia.org/wiki/Snort_%28software%29)
* [TIGER](http://packages.debian.org/wheezy/tiger)
* [sxid](http://packages.debian.org/wheezy/sxid)
* antivirus, antimalware

These are only pointers for you to search the web about these topics and these are probably beyond the scope of this guide.

## One VM ##
**One VM is deprecated.** It was tested and developed for 0.1.3. The concept worked. It's deprecated now, because it has no maintainer.

Alternatively, you could also use one VM instead of two, where Tor runs on the host. It has some security and other kinds of advantages/disadvantages listed in the article. See [OneVM].

## Separate user account for Virtual Box ##
Security wise it makes sense to create a separate user account just for using Virtual Box, which is no in the admin/sudo group.

## DMZ
If you are using a shared network, as in a cable modem/router or ADSL/router setup, that is shared with others, you should consider configuring a [DMZ](https://en.wikipedia.org/wiki/DMZ_%28computing%29) for your Whonix-Gateway.

This DMZ would restrict the Whonix-Gateway from accessing and from being accessible by other nodes on the network, eg printers, phones, computers, laptops, even if root access was somehow achieved on it.

Should an incursion occur, it would prevent the adversary from exploring other systems and possibly compromising them. It won't  however do anything to protect your anonymity, because they could just ping some remote server and discover your real IP address. Or should other systems be compromised, it would be more difficult to compromise Whonix-Gateway.

## Host Firewall
### Filtering Ports
#### Introduction
From time to time someone asks, which ports incoming/outgoing Whonix-Gateway requires. The answer is.

* incoming: none
* outgoing: all

#### Incoming
Whonix-Gateway itself does not open any ports. Closing ports on the host is still advised. That was already covered in the [Pre Install Advice](https://sourceforge.net/p/whonix/wiki/Pre%20Install%20Advice/#portscan-firewall).

#### Outgoing
**Recommend against.** Port based filtering of outgoing traffic isn't applicable (as in useful) in case of Whonix-Gateway.

Filtering outgoing ports is difficult, since Tor entry guards (or bridges) listen on a variety of different ports. Limiting ports Tor uses for outgoing traffic is possible, although recommend against, since it reduces anonymity (fewer entry guards (or bridges) are available to you). If you want to so so anyway...

On Whonix-Gateway.

    sudo nano /etc/tor/torrc

Add.

    ReachableDirAddresses *:80
    ReachableORAddresses *:443
    FascistFirewall 1
    ## maybe: FirewallPorts PORTS
    ## See Tor manual: https://www.torproject.org/docs/tor-manual.html.en

Reload Tor.

    sudo service Tor reload

This has also been discussed [in the forum](https://sourceforge.net/p/whonix/discussion/general/thread/3a0b673a/).

# Hardware Security #
It's recommend to use "clean" computers made of parts manufactured by reputable companies and to pay in cash so as to not have hardware IDs leak our identity.

Whonix doesn't do anything against hardware backdoors.

# Physical Attacks #
## Introduction ##
Physical attacks require an adversary the be physically preset, i.e. the be able to touch your computer.

## Full Disk Encryption ##
To protect against theft or robbery, power off your machine at times when this is more likely (traveling) and use FDE (Full Disk Encryption) on the host.

## Side channel attacks ##
Whonix does **not** defeat [hardware keylogger](https://en.wikipedia.org/wiki/Hardware_keylogger), miniature cameras, [TEMPEST](https://en.wikipedia.org/wiki/Tempest_%28codename%29).

Needless to say, that also FDE does not protect against these threats.

## Screen lock ##
Always lock the screen of the host (or better shut down) if you leave the system unattended.

## BIOS password ##
Can't hurt to have BIOS password for BIOS setup and boot. After you are done installing, allow only booting from HDD.

## Cold Boot Attacks ##
Due to how modern computing works, basically everything that you have done during a session is stored in the RAM. If an attacker has physical access to your computer when you are running Whonix, it may enable her to recover everything that have been achieved during the session - even if you are using Full Disk Encryptoion. From typed texts to saved files, including passwords and encryption keys. The more recent the activity, the more likely it is that it is still in the RAM.

Furthermore, it has been shown that the data present in the RAM might be recoverable for seconds or even minutes after the computer is powered off using a cold boot attack.

In both cases the RAM contents can be analyzed in a computer forensics laboratory which might turn into a major disaster depending on what they find.

As far as the authors know, cold boot attacks are not standard procedure within law enforcements and similar organizations anywhere in the world yet, but it might still be good to be prepared and stay on the safe side.

Wipe RAM on shutdown (e.g. using a kexec script) - or do not leave the computer unattended immediately after shutdown. Unfortunately there is not yet an upstream script, to implement wiping the RAM on shutdown. We can not provide a solution for this attack, this is solved nowhere but [partially](https://tails.boum.org/bugs/sdmem_does_not_clear_all_memory/) in Tails and Liberte Linux (not checked), waiting for upstream solution, see [Dev] Wipe RAM panic script. It's up to you to implement a panic button which will wipe the RAM, please [Contribute](http://sourceforge.net/p/whonix/wiki/Contribute/). The least you can do is [Vote](http://sourceforge.net/p/whonix/wiki/Contribute/#vote-ideas) at upstream for the feature.

**Hypothetical...** So, what should you do when you hear an attacker knocking at your door? You could just press the hypothetical panic button on the host. It would start to wipe the contents of the RAM by filling it out with random junk, thus erasing everything that was stored there before, including the encryption key of the encrypted storage devices you might use and the traces of your session. Then you would wait, possibly trying to buy valuable time by barricading your door.

## Evil Maid Attack ##
See [Evil Maid Attack](https://www.schneier.com/blog/archives/2009/10/evil_maid_attac.html).

If you have a TPM chip, see [Anti Evil Maid](http://theinvisiblethings.blogspot.se/2011/09/anti-evil-maid.html).

## Problematic Interfaces ##
Some interfaces such as ExpressCard, PCMCIA, FireWire or Thunderbol may depending on the host operating system settings allow an attacker with physical access to read the RAM. You are advised to securely configure those interfaces, to disable them or to remove them.

# Operating System #
## About Debian ##
### Harden Debian ###
* [Debian Security Information](http://www.debian.org/security/)
* [Securing Debian Manual Chapter 6 - Automatic hardening of Debian systems](http://www.debian.org/doc/manuals/securing-debian-howto/ch-automatic-harden.en.html)
* [Securing Debian Manual](http://www.debian.org/doc/manuals/securing-debian-howto/ch-automatic-harden.en.html)
* [Hardening Walkthrough](http://wiki.debian.org/HardeningWalkthrough)
* Feel free to research even more.

Most hardening steps can not be easily added by default to Whonix. Mostly the user has to understand them and to be aware of them, require knowledge and effort, otherwise one thing or another will break. This is still under investigation and open for suggestions. Having a secure operating system will always be an important topic.

## Harden Software Repositories ##
Many operating systems provide multiple repositories. Since *Whonix's example implementation* is based on Debian, you should read [Ubuntu Repositories (similar in Debian)](https://help.ubuntu.com/community/Repositories/) and [Debian Policy Manual Chapter 2 - The Debian Archive](http://www.debian.org/doc/debian-policy/ch-archive.html) as introduction.

In conclusion, the main repository gets most attention and security updates. It would make sense to tweak */etc/apt/sources.list* and to only use software from the main repository and to only install security fixes, no other updates.

Whonix currently doesn't do that by default and it's an open question for research if that really improves security.

[dpkg-origins](https://github.com/fab1an/unix-admin-tools/blob/master/dpkg-origins) can create a list of all packages and their repository.

## About grsecurity ##
Linux kernel is not a secure OS, Linus himself made it pretty clear that he doesn't think highly of the "security community". His threat model and a Tor User threat model don't have much in common. Good that Linux is open source and if we disagree with a policy or politics we can just patch or fork it... Grsecurity/PaX is the most comprehensive kernel patch providing much needed security hardening both for the kernel itself and for making userland protections more effective.

Sadly no distribution of binary grsec kernel exists. ^1^ That means either a packager/maintainer of Whonix needs to compile them EVERY TIME there is a security update to the kernel (which is pretty frequently) or the Whonix users themselves need to compile and update their kernels. This is undesirable because kernel compilation is not set and forget, you need a bit of knowledge, it takes a while, especially in a resource restricted VM and you need to keep updated about new releases via mailing lists or similar because your software updater doesn't automatically handle custom kernels (even emerge in hardened gentoo doesn't). All this would most likely only result in users running old, outdated kernel versions.

Further for Whonix-Gateway and the Identity/Location TCB grsecurity only addresses a subset of security risks: It can mitigate *some* kernel vulnerabilities (and we only really care about the networking stack which is pretty secure judging from its track record). **Maybe** ***some*** (memory corruption) vulnerabilities in apt-get and Tor that aren't already mitigated by the existing userland hardening done by Ubuntu. It can't protect against backdoors or security issues related to design, policy or yet unknown classes of exploits. We feel that these relatively small advantages outweigh the issues introduced by using a custom compiled kernel. We hope a binary distro will step forward and start using grsecurity. In that case we'll most likely switch Whonix-Gateway to that distro as soon as possible.

For Whonix-Workstation the benefits are even more doubtful. To be effective grsecurity needs to lock down some functions that are needed by Xorg, JIT compilers... but we need those to be working. To solve this we'd have to write a restrictive RBAC policy which is far from trivial. We think accepting that Whonix-Workstation will be exploitable and acting accordingly (using snapshots and rolling back to clean state) is the right approach for a desktop system.

If you disagree with this assessment or have any suggestions how to improve the current situation please let us know on [Dev]!

Experts only: There is also Hardened Gentoo based Whonix-Gateway. Outdated, needs maintainer. See [HardenedGentooTG]

<font size="-3">
,,
^1^ There's Alpine Linux but they don't package Tor yet: [Package Request: Tor
](http://bugs.alpinelinux.org/issues/1067).
</font>

# Virtualization Platform #
## About VirtualBox ##
VirtualBox is developed by Oracle, a company not exactly know for being very "open". That includes how they announce security issues in their products as well as how they are perceived by the security community and how they will communicate with each other.

VirtualBox is primarily a simple, "user friendly", desktop solution and most certainly not designed with our threat model in mind. I haven't heard of anyone seriously auditing the code and I'd like to recommend a different VM solution at least as an alternative. There's KVM and Xen, open source but not cross-platform. It seems they are still lacking in terms of a reliable "internal networking" feature which Whonix heavily depends on. (If you know more, please edit this paragraph).

Anyone looking into Whonix solely because of security should really consider using Whonix with [PhysicalIsolation].

Related Virtual Box Links:

* [Custom Ticket Search](https://www.virtualbox.org/query?summary=~&col=id&col=summary&col=status&col=owner&col=type&col=priority&col=component&order=priority)
* [New Ticket](https://www.virtualbox.org/newticket)

## Qubes OS ##
It shouldn't be very hard to get Whonix to run on top of Qubes OS, which would be more secure than Virtual Box. See blog post:
[Running Whonix on top of Qubes OS, anyone interested?](https://sourceforge.net/p/whonix/featureblog/2013/02/running-whonix-on-top-of-qubes-os-anyone-interested-unpacking-ova-images/).

## Secure Label ##
[Secure labeling with VBoxSDL](http://www.virtualbox.org/manual/ch09.html#idp12297856) has not yet been added to Whonix. I couldn't get it to work. If you know more, please share your knowledge.

We must not end up with non-standard desktop resolution, as per [Whonix's Protocol-Leak-Protection and Fingerprinting-Protection](https://sourceforge.net/p/whonix/wiki/Whonix%27s%20Protocol-Leak-Protection%20and%20Fingerprinting-Protection/).

# Whonix-Workstation Security #
## Hardening ##
Whonix isn't a perfectly hardened system. Additional hardening would be very welcome. At the same time, hardening by default is very difficult. That's why this is outside the scope of the Whonix Anonymous Operating System project, unless the project gets serious amounts of help with it. Hardening is left to the upstream operating system. See [Operating System](https://sourceforge.net/p/whonix/wiki/Security/#operating-system) for details.

Use [AppArmor](https://en.wikipedia.org/wiki/AppArmor) ([in Debian](http://wiki.debian.org/AppArmor)):

* [AppArmor Profile for TBB](https://trac.torproject.org/projects/tor/wiki/doc/AppArmorForTBB)

## More than one Tor Browser in Whonix ##
As the [Warning] page stated, [Whonix doesn't magically separate your different contextual identities](https://sourceforge.net/p/whonix/wiki/Warning/#whonix-doesnt-magically-separate-your-different-contextual-identities) and since Tor Browser and Tor Button do not yet solve this, for further separation of identities you could use [Multiple Whonix-Workstations](https://sourceforge.net/p/whonix/wiki/Multiple%20Whonix-Workstations/), which would be more secure. 

Alternatively, less secure than Multiple Whonix-Workstations, you could start multiple instances of Tor Browser and run them through different SocksPorts. The instructions in the [ManualTBupdate] article need minimal changes.

Instead of

    #!/bin/bash
    ## Whonix Tor Browser start script

    ~/tor-browser_en-US/App/Firefox/firefox --profile ~/tor-browser_en-US/Data/profile

    ## End of Whonix Tor Browser start script

Use

    #!/bin/bash
    ## Whonix Tor Browser start script

    ## Adjust the path!
    ~/tor-browser_2/App/Firefox/firefox --profile ~/tor-browser_2/Data/profile -no-remote

    ## End of Whonix Tor Browser start script

Only *-no-remote* was added to the start script. Otherwise Tor Browser would connect the the already running Tor Browser and this isn't what you want. And don't forget to adjust the path to the other Tor Browser.

You also have to use a different SocksPort in *user.js*. (See [Whonix Proxy Settings / user.js](https://sourceforge.net/p/whonix/wiki/TorBrowser/#whonix-proxy-settings-userjs) explanation.) Change

    user_pref("extensions.torbutton.socks_port", 9100);

For example to 

    user_pref("extensions.torbutton.socks_port", 9159);

(See [Stream Isolation] page for explanation why you should use different SocksPorts.)

## Using multiple Whonix-Workstations ##
See [Using multiple Whonix-Workstations](https://sourceforge.net/p/whonix/wiki/Multiple%20Whonix-Workstations/).

## Second, Optional, Extra Firewall ##
There is a Second, Optional, Extra Firewall for Whonix-Workstation, which is disabled by default. You find it inside Whonix-Workstation in */usr/local/bin/whonix_firewall*. [on github](https://github.com/adrelanos/Whonix/blob/stable/whonix_workstation/usr/local/bin/whonix_firewall)

Read the script comments and decide if you want to use it.

# Whonix-Gateway Security #
## Static Virtual Box IP ##

Instead of using DHCP to obtain the internal IP for Whonix-Workstation eth0 NAT adapter, you could also use a static IP instead. Perhaps this could (minimally?) improve security, since you can remove one more package: the DHCP package.

Open */etc/network/interfaces* [on github](https://github.com/adrelanos/Whonix/blob/stable/whonix_gateway/etc/network/interfaces), read the comments, comment out DHCP and comment in Static Virtual Box IP.

# Chaining Anonymizing Gateways #
Experts only!

All Whonix-Workstation traffic is by default forced through Whonix-Gateway. Alternatively, you could also build a chain of Anonymizing Gateways. Examples:

Pre-Tor-VPN.

    Whonix-Workstation -> VPN-Gateway    -> Whonix-Gateway -> destination server
    user               -> VPN            -> Tor            -> destination server

Post-Tor-VPN.

    Whonix-Workstation -> Whonix-Gateway -> VPN-Gateway    -> destination server
    user               -> Tor            -> VPN            -> destination server

Pre- and Post-Tor-VPN.

    Whonix-Workstation -> VPN-Gateway    -> Whonix-Gateway -> VPN-Gateway -> destination server
    user               -> VPN            -> Tor            -> VPN         -> destination server

It's not limited to VPN-Gateways. You could also replace the VPN with a Proxy-Gateway.

Pre-Tor-Proxy.

    Whonix-Workstation -> Proxy-Gateway  -> Whonix-Gateway -> destination server
    user               -> Proxy          -> Tor            -> destination server

Or with a Post-Tor-Proxy, or with a Pre/Post-Tor-SSH. Or replace the proxy with JonDo or perhaps i2p. Virtually any combinations are possible.

Whether that makes sense or not is controversially discussed and depends on your personal threat model, see [Tor plus VPN or Proxy](https://trac.torproject.org/projects/tor/wiki/doc/TorPlusVPN).

Legend:

* destination server: could be for example a website

Recommend basic knowledge:

* [Tunnel_Proxy_or_SSH_or_VPN_through_Tor]
* [Tunnel_Tor_through_proxy_or_VPN_or_SSH]
* [Stream Isolation]

Maybe useful as well: [Inspiration].

You must know understand and edit /etc/network/interfaces on Whonix-Gateway and/or on Whonix-Workstation (and if not using physical isolation, the virtual internal network name in Virtual Box settings).

It will be difficult, because there are no other Anonymizing Gateways (VPN/JonDo/i2p/Proxy/SSH/VPN) available for download, besides Whonix-Gateway which uses Tor to anonymize traffic, which you already know about. You have to look for instructions (there are some for a pfSense based VPN-Gateway you find using a search engines, but untested for leaks by adrelanos, which does not imply there are leaks) and/or build such a Anonymizing-Gateway yourself.

# Time Synchronization #
This is still a topic for research.

Deactivate NTP on the host. Bonus points for requesting NTP as everyone, but discarding it (for a more natural network fingerprint).

Check host clock out of band (use a watch or atomic clock), see [TimeSync] for more information. (Fingerprinting issues?)

# Useful External Links #

* http://www.aboutdebian.com/security.htm
* http://www.cyberciti.biz/faq/debian-ubuntu-linux-software-integrity-checking-with-aide/
* http://serverfault.com/questions/11659/what-steps-do-you-take-to-secure-a-debian-server
* http://seifried.org/lasg/
* https://wiki.ubuntu.com/BasicSecurity
* https://wiki.ubuntu.com/BasicSecurity/DidIJustGetOwned
* https://help.ubuntu.com/community/Antivirus

# Other important stuff #
Last, but definitely not least.

* Read [Stream Isolation].
* Read [(encrypted) (authenticated) Connection Between Whonix-Gateway and Whonix-Workstation](https://sourceforge.net/p/whonix/wiki/Connection%20Between%20Whonix-Gateway%20and%20Whonix-Workstation/).
* Read [Entropy].
* Restrict TransPort: Explained under [Whonix-Workstation is firewalled](https://sourceforge.net/p/whonix/wiki/Install%20Software/#whonix-workstation-is-firewalled).
* MAC Address: If you are interested in the discussion about anonymizing MAC addresses, you could read the development discussion and draw conclusions from it, see [MAC].
* Of course you should read all [Documentation] pages. (Although some stuff will not be of concern for you. For example, if you are not interested in TorChat, Remailers or Mixmaster, you obviously don't have to thoroughly study these pages.
* Design: Still reading? Great! Please check the Technical [Design], it contains further recommendations on what is less then ideal and how it could possibly be improved.

# License #
    Whonix Advanced Security Guide wiki page Copyright (C) Amnesia <amnesia at boum dot org>
    Whonix Advanced Security Guide wiki page Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
    
    This program comes with ABSOLUTELY NO WARRANTY; for details see the wiki source code.
    This is free software, and you are welcome to redistribute it
    under certain conditions; see the wiki source code for details.

# Footer #
[[include ref=WikiFooter]]