[[include ref=WikiHeader]]

[TOC]

# Comparison of Whonix, Tails, Tor Browser Bundle and Qubes OS TorVM
## Introduction
Quick comparison of Whonix and Tails key virtues. If ever anything in this table is incorrect/outdated feel free to contact Whonix developers, we'll correct as fast as possible.

**Last update**

Comparing:

* Whonix 0.4.5
* Tails 0.1.6.
* Qubes OS TorVM 0.1.beta1

## Different views
One has always to be very careful, when talking about others. Especially, when talking about advantages and disadvantages. Different opinions are accepted and listed here.

* [Tails-dev: please look at Comparison of Whonix, Tails and TBB](https://mailman.boum.org/pipermail/tails-dev/2012-September/001704.html)
* [Tails-dev: please look at Comparison of Whonix, Tails and TBB #2](https://mailman.boum.org/pipermail/tails-dev/2013-February/002563.html)
* [qubes-devel: please look at Comparison of Whonix, Tails, TBB and Qubes OS TorVM](https://groups.google.com/forum/?fromgroups#!topic/qubes-devel/GT8LyE-la-o)

## General
| | Whonix | Tails | Tor Browser Bundle | Qubes OS TorVM
------------- |  ------------- | ------------- | ------------- | -------------
Focus on anonymity, privacy and security | Yes | Yes | Yes | Yes
Type | general purpose os available as VM images and physical isolation | LiveCD/DVD/USB | portable browser | general purpose os, VM plugin for Qubes OS, 
Supported hardware | any ^1^ | x86 compatible and/or and Virtual Machines | Windows, Linux, Mac and Virtual Machines | any capable of running Qubes OS
Based on | Tor, Debian ^2^ and a Virtualizer ^3^ \[Virtual Box\] when not using Physical Isolation | Tor, Debian | Tor, Firefox | Tor, Qubes OS, Fedora
Gateway and torify any operating system (advanced users) | Yes ^4^ | Not a Gateway. | Not a Gateway. | Probable (?) yes, when using [HVM](http://wiki.qubes-os.org/trac/wiki/HvmCreate)
Live CD | No | Yes | No | No
Live USB | No | Yes | No | No
USB bootable | Yes ^5^ | Yes | Yes ^5^ | Yes ^5^
Requires Virtual Box | If not using Physical Isolation, yes. ^3^ | No | No | No
Requires Qubes OS | No | No | No | Yes
System requirements | higher | lower | lowest | highest
Can run in VM | Yes | Yes | Yes | Yes
Persistence | Full | Optional for Live USB | Yes ^6^ | Full (?)
Number of developers | one with lots of anonymous contributions | multiple | multiple | One (?)
Maturity | project since 2012 | established, respected project for many years | established, respected project for many years | project since 2012 (?)
Open Source | Yes | Yes | Yes | Yes
Anonymous developers | Yes | Yes | No | (?)

<font size="-3">
,,
^1^ *Whonix Framework* workstation: self made builds can run on any real or virtual hardware. Intel VT-x or AMD-V will greatly speed up Virtual Machines. *Whonix Framework* gateway: anonymizer (Tor) must support that platform. 
^2^ Whonix-Workstation: also [OtherOperatingSystems](https://sourceforge.net/p/whonix/wiki/OtherOperatingSystems/) are supported.; Whonix-Gateway: In long term we are also agnostic about any other secure distributions. The concept is agnostic, you could use another operating system as base, but it requires effort.
^3^ Default downloads are for Virtual Box. (Subject for change in future.) [PhysicalIsolation] is an security optional feature for advancend users. Experimental optional support for [VMware]. You can build your own images for other virtualizers, but it requires effort.
^4^ See [OtherOperatingSystems](https://sourceforge.net/p/whonix/wiki/OtherOperatingSystems/).
^5^ You can install your host operating system on USB. 
^6^ You can download files and keep them, save bookmarks and passwords depending on your settings.
</font>

## Security
### General
| | Whonix | Tails | Tor Browser Bundle | Qubes OS TorVM
------------- |  ------------- | ------------- | ------------- | -------------
Amnesic | No ^7^ | Yes | No ^12^ | No
Protection against IP/location discovery through root exploits ([Malware](https://en.wikipedia.org/wiki/Malware) with root rights) on the Workstation ^18^. | Yes ^a^ | No ^2^ | No ^2^ | Yes
IP/DNS protocol leak protection | Full ^1^ | Depends ^5^ | Depends ^5^ | Full
Takes advantage of Entry Guards | Yes | No | Yes | Yes (?)
Operating System Updates | persist once updated | are lost after reboot | persist once updated | persist once updated (?)
Hides hardware serials from malicious software | Yes ^16^ | No ^17^ | No ^17^ | (?)
Collects hardware serials | No | No | No | No
Includes Tor Browser | Yes | No | Yes | No
Stream isolation to prevent identity correlation through circuit sharing | Yes | Yes ^13^ | See ^14^ ^15^ | Manually (?)
Stream isolates Tor Browser | No ^14^ | No ^14^ | No ^14^ | No ^14^
Encryption | Should be applied on host. | Yes, for persistent USB. | Should be applied on host. | Should be applied on host. | No (?)
Cold Boot Attack Protection ^8^ | No, planed. | Yes | No | No (?)
Secure Distributed Network Time Synchronization | Yes | Yes | No | No
Hides your time zone (set to UTC) | Yes | Yes | Yes | Yes
Hides your operating system account name | Yes, set to user. | Yes, set to amnesia. | No | Yes
Hides your MAC address from websites | Invalid ^19^ | Invalid ^19^ | Invalid ^19^ | Invalid ^19^
Secures your MAC address from local LAN (sometimes ISP) ^20^ | No, planed, see. ^21^ | No, planed. ^22^ | No | (?)
Hides your MAC address from applications | Yes ^24^ | No | No | (?)
Secure gpg.conf | Yes | Yes | Not an operating system. | No
Privacy enhanced IRC client configuration. | Yes | Yes | Not an IRC client. | No

<font size="-3">
,,
^a^ Whonix has Protection against IP/location discovery through root exploits ([Malware](https://en.wikipedia.org/wiki/Malware) with root rights) inside Whonix-Workstation. But you really should not test it. In case Whonix-Workstation gets rooted, the adversary can not find out the users real IP/location. This is because Whonix-Workstation can only connect through the Whonix-Gateway. How difficult is it to compromise Whonix? See [Attack on Whonix](https://sourceforge.net/p/whonix/wiki/Comparison%20with%20Others/#attacks) and [Design]. More skill is required.
^1^ Such kinds of leaks are impossible ^a^ in Whonix, since the Whonix-Workstation is unaware of it's external IP.
^2^ In case Tails or TBB gets rooted, the adversary can simply bypass the firewall and get the user's real IP.
^5^ See first example of [Whonix security in real world](https://sourceforge.net/p/whonix/wiki/Security%20in%20Real%20World/). When applications in Tails are configured wrong, due to a bug in Tails or the application, IP can leak. Quoted from the [Tails Security Page](https://tails.boum.org/security/index.en.html): *"Until an [audit](https://tails.boum.org/todo/applications_audit/) of the bundled network applications is done, information leakages at the protocol level should be considered as − at the very least − possible."*
^7^ There are no special measures to limit what is written to disk. This includes (non exclusive list) user created files, backup files, temporary files, swap, chat history, browser history and so on. Whonix acts like an ordinary installed operating system. It can also not be prevented, that the host memory [swaps](https://en.wikipedia.org/wiki/Swap) to the host disk. There is a [Recommendation to use multiple VM Snapshots](https://sourceforge.net/p/whonix/wiki/Security%20Guide/#recommendation-to-use-multiple-vm-snapshots) and it is is [recommend](https://sourceforge.net/p/whonix/wiki/Advanced%20Security%20Guide/#full-disk-encryption) to apply Full Disk Encryption on the host.
^8^ See [Cold boot attack](https://en.wikipedia.org/wiki/Cold_boot_attack). 
^12^ Although it does not try to store to disk, swap can still leak. 
^13^ [Tails separate Tor streams](https://tails.boum.org/todo/separate_Tor_streams/)
^14^ [Tor Browser should set SOCKS username for a request based on referer](https://trac.torproject.org/projects/tor/ticket/3455)
^15^ Tor Browser comes with it's own Tor instance. It's just a browser, not a live system or operating system. 
^16^ See [Whonix's Protocol-Leak-Protection and Fingerprinting-Protection](https://sourceforge.net/p/whonix/wiki/Whonix%27s%20Protocol-Leak-Protection%20and%20Fingerprinting-Protection/) for details.
^17^ By default there get of course not send to anyone. This is only at risk in case the machine gets compromised by malware. See also, [Are hardware serial numbers hidden in TAILS?](https://tails.boum.org/forum/Are_hardware_serial_numbers_hidden_in_TAILS__63__/).
^18^ The Workstation is the place where the browser, IRC client and so on is running. The Gateway is the place where Tor and the firewall is running.
^19^ It is in the nature of the MAC addresses, that destination servers can not see them. Therefore yes, always hidden from destination servers.
^20^ Most ISPs do not see the MAC addresses of their clients. Some ISPs are based on LANs, in that case they can see the MAC address. Also hotspots can see the MAC address.
^21^ Please read [Whonix in public networks / MAC Address](https://sourceforge.net/p/whonix/wiki/Whonix%20in%20public%20networks%20-%20MAC%20Address/).
^22^ [Tails Todo: machanger](https://tails.boum.org/todo/macchanger/)
^23^ Placeholder.
^24^ The virtual MAC address of Whonix-Workstation and Whonix-Gateway ^25^ is shared among all Whonix users. If any (malicious) applications would spill it ^26^, it would only be known that it's from a Whonix user.
^25^ The virtual MAC address for Whonix-Gateway's internal network interface (eth1) is shared among all Whonix users, because Whonix-Workstation can see it. However, Whonix-Workstation can not see Whonix-Gateway's external network cards (eth0) MAC address.
^26^ Which they usually won't do. Sometimes anti cheat or copyright protection tools do it.
</font>

### Fingerprint
| | Whonix | Tails | Tor Browser Bundle | Qubes OS TorVM
------------- |  ------------- | ------------- | ------------- | -------------
Network/Web Fingerprint | [Whonix Fingerprint Page](https://sourceforge.net/p/whonix/wiki/Fingerprint/) | [Tails Fingerprint Page](https://tails.boum.org/doc/about/fingerprint/index.en.html) | TBB traffic is tunneled through Tor. Host traffic passes clearnet. | -
Network fingerprint: ISP can trivially guess project type ^27^ | No. | No. | No. | (?)
Network fingerprint: ISP can guess a non-persistent Tor directory is being used | No. | Yes, because [not yet](https://tails.boum.org/todo/persistence_preset_-_tor/) supporting persistent entry guards. | No. | (?)
clearnet traffic | All Whonix-Gateway and Whonix-Workstation traffic is tunneled through Tor. Host traffic (operating system updates, eventually host browser etc.) uses clearnet. | None, unless other users sharing the same internet connection are not using Tails. | TBB traffic is tunneled through Tor. Host traffic (operating system updates, eventually untorified second browser etc.) uses clearnet. | Yes, Gateway is not torified.
Network fingerprint: ISP can guess which anonymity software is being used because of ratio of Tor and clearnet traffic | Unknown. ^33^ | Can guess a Tor Live CD is being used, unless Unsafe Browser is in use or other people sharing same internet connections not using Tails. | ? | (?)
Network fingerprint: ISP can guess which anonymity software is being used because of [tordate](https://tails.boum.org/contribute/design/Time_syncing/) ^34^ | No, does not include tordate. | Yes, if clock is too much off when booting. ^34^ | No, not an operating system. | No, does not include tordate.
web fingerprint ^28^ | Same as TBB. ^29^ | Tails specific. ^30^ | TBB. ^31^ | Does not include Tor Browser.

<font size="-3">
^27^ Find out if Whonix, Tails or TBB is running.
^28^ Fingerprint for the websites that you are visiting
^29^ Uses the original Tor Browser from torproject.org with the only difference, that Tor runs on Whonix-Gateway instead the locally shipped Tor.
^30^ See [evaluate web fingerprint](https://tails.boum.org/todo/evaluate_web_fingerprint/).
^31^ Is the original Tor Browser Bundle from torproject.org.
^32^ Live CD without persistent USB storage for the Tor data directory.^^ 
^33^ Whonix users might tend to have more traffic than TBB users, due to operating system updates of Whonix-Workstation and Whonix-Gateway through Tor. Unknown if this is specific enough to guess a transparent or isolating proxy is being used or if enough other Tor users run big enough amounts of traffic through Tor. Research before Whonix was created has shown that big amounts of filesharing traffic were run through Tor. Classical filesharing tends to have more upload than Whonix, but it's also unknown how many people disabled upload or moved to methods which do not involve much upload, such as file hosters.
^34^ Quoted from the [Tails Design about Time syncing](https://tails.boum.org/contribute/design/Time_syncing/#index5h1): "*Our initial time guess based on the Tor consensus is probably easier to fingerprint, though: a fresh Tor is started, and restarted again right after the consensus has been downloaded.*"
</font>

### Flash / Browser Plugin security
**Note**: Whonix developer adrelanos recommend due to anonymity, privacy and security issues against using Adobe Flash when anonymity is the goal. As far I know, Tails and Tor developers recommend against it as well.

Flash Tracking Technique | Whonix-Workstation | Tor on host |
------------- |  ------------- | ------------- |
Proxy bypass IP leak | Protected. | Insecure, leads to deanonymization.
Protocol IP leak | Protected. | Insecure, leads to deanonymization.
Flash Cookies | Reduce anonymity to pseudonymity. Recommend to delete Flash Cookies. | Can link your clearnet Flash activity to your Flash activity over Tor, which leads to deanonymization (or at least a good guess) if the skew is big and rare. Also useful for fingerprinting, which is bad. ^1^
Number of installed fonts. | The number of fonts inside Whonix-Workstation and your clearnet/host operating system will differ, which is good. | Same fonts are reported for your clearnet and your Tor Flash activity, which is bad. ^1^
Exact flash player version. | Shared among all up to date Debian users. Not very useful for fingerprinting. Probable different from your clearnet/host operating system, which is good. | Same version is reported for your clearnet and for your Flash activity over Tor, which is bad. ^1^
GNU/Linux Kernel version. | Shared among all up to date Debian users. Not very useful for fingerprinting. | Same version is reported for your clearnet and for your Flash activity over Tor. ^1^
Language. | Set to en_US for all Whonix users. | Your local language setting. Useful for fingerprinting and anonymity set reduction, which is bad. ^1^
Exact date and time. | Differs from your clearnet/host operating system, which is good. (See [Whonix's Secure And Distributed Time Synchronization Mechanism](https://sourceforge.net/p/whonix/wiki/TimeSync/) for details.) | Same time/clockskew is reported for your clearnet and your Tor Flash activity, which is bad. ^1^
Exact screen resolution and DPI. | Shared among all Whonix users. (See [Whonix's Protocol-Leak-Protection and Fingerprinting-Protection](https://sourceforge.net/p/whonix/wiki/Whonix%27s%20Protocol-Leak-Protection%20and%20Fingerprinting-Protection/) for details.) Even if you changed it, the screen resolution and DPI it will differ from your clearnet/host operating system. | Same screen resolution and DPI is reported for your clearnet and Tor use, which is bad. ^1^
Full path to your flash plugin. | Shared among all Debian users. | Depends on your clearnet/host operating system. In worst case it could contain your operating system user name, which is even worse if that is your real name. Same path to your flash plugin is reported for your clearnet and Tor use, which is bad. ^1^
Anything else. <font size="-3">(You can check that yourself offsite on <https://ip-check.info>.)</font> | Assume reduction from anonymity to pseudonymity. | Even more possibilties for fingerprinting and linking, which is bad. ^1^
Conclusion | IP/location/identity will still be hidden inside Whonix-Workstation. Assume it to be [pseudonymous rather than anonymous](https://sourceforge.net/p/whonix/wiki/DoNot/#do-not-confuse-anonymity-with-pseudonymity). | Flash over Tor (on the host, without something like Whonix) is totally unsafe. In case you also ever use(ed) Flash over clearnet, linkability is possible. Assume the Flash fingerprint to be that strong, that your clearnet and your Tor Flash activity can be linked together, which leads to deanonymization.

^1^ Which is bad, because it could be used for fingerprinting, linking and also deanonymization (or at least a good guess) if the fingerprint is detailed enough.

For more information about Flash and Browser Plugins in Whonix, see also [Browser Plugins](https://sourceforge.net/p/whonix/wiki/BrowserPlugins/).

## Attacks
### Circumventing Proxy Obedience Design
Knowledge assumed:

* [Comparison of different Whonix variants](https://sourceforge.net/p/whonix/wiki/Comparison%20of%20different%20Whonix%20variants/).
* Unsafe Browser: Tails and Liberte Linux contain a so called Unsafe Browser. The Unsafe Browser does not use Tor. Connects in the clear. It is useful to register on hotspots or to view content in the clear without Tor.
* Exploit against physically isolated Whonix-Gateway: difficult against a bare metal physical isolated Whonix-Gateway. This is because Whonix-Workstation can only access Tor running on Whonix-Gateway. We minimized attack surface, hardening etc. See the whole Security and Hardening page for details.
* TBB stands for Tor Browser Bundle.
* In the following table,
	* "fail" is defined as "IP/location of user is compromised.".
	* "safe" is defined as "IP/location of user is hidden behind Tor.".
* The numbers (1) to (10) are used to numerate various attacks. Those attacks are described in more details below.

Whonix protects against IP/location discovery through root exploits ([Malware](https://en.wikipedia.org/wiki/Malware) with root rights) on the Workstation^1^. This does not mean, risk to get infected with malware. Do not! It would still make all data inside Whonix-Workstation available to the attacker. Like said at other places as well, Whonix is not a perfect system. It can not be. Whonix is not unbreakable. What Whonix does, it higher the effort for an attacker to find out the user's real IP address, thus de-anonymizing the user. The following table shall visualize the various defense layers provided by Whonix.

<font size="-3">
,,
^1^ The Workstation is the place where the browser, IRC client and so on is running. The Gateway is the place where Tor and the firewall is running.
</font>

attack | Whonix Standard Download version host+vm+vm | Whonix Physical Isolation | Tails | Tails in a VM | TBB | TBB in a VM | Qubes OS TorVM
------------- |  ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | -------------
(1) Proxy Bypass IP leak | safe ^5^ | safe ^5^ | safe ^5^ | safe ^5^ | fail | fail | safe
(2) Protocol IP leak | safe ^4^ | safe ^4^ | fail | safe ^6^ | fail | safe ^6^ | safe
(3) exploit + Unsafe Browser | safe | safe | fail | fail | fail | fail | safe
(4) exploit + root exploit + Unsafe Browser | safe | safe | fail | fail | fail | fail | safe
(5) root exploit + Unsafe Browser | safe | safe | fail | fail | fail | fail | safe
(6) exploit + vm exploit + Unsafe Browser | fail | safe | fail | fail | fail | fail | fail
(7) exploit + vm exploit + exploit against physically isolated Whonix-Gateway | fail | fail | fail | fail | fail | fail | fail | fail
(8) vm exploit | fail | safe | safe | fail | safe | fail | fail
(9) vm exploit + exploit against physically isolated Whonix-Gateway | fail | fail | safe | fail | safe | fail | fail
(10) exploit against Tor process | fail | fail | fail | fail | fail | fail | fail
(11) attack against the Tor network | fail | fail | fail | fail | fail | fail | fail

(1) An application doesn't honor proxy settings. Example: [Tor Browser Bundle: Firefox security bug (proxy-bypass)](https://blog.torproject.org/blog/firefox-security-bug-proxy-bypass-current-tbbs).

(2) For example proxy bypass bugs, where the application spills the users real IP. See [Whonix security in real world](https://sourceforge.net/p/whonix/wiki/Security%20in%20Real%20World/), for examples where Whonix circumvented them. It gets circumvented by Whonix because Whonix-Workstation does not know the users real IP address.

(3) Example: user visits a website over Tor with a torified Browser. The website uses known or zero day vulnerability to gain remote code execution on the users machine. Remote cod execution is used to install malware on the users machine. The used vulnerability allows the adversary to get "only" user rights, not root. The adversary could remotely start the Unsafe Browser and therefore find out the users real IP address. This attack gets circumvented by Whonix, because any applications inside Whonix, including malware, can only connect through Tor.

(4) Example: user visits a website over Tor with a torified Browser. The website uses known or zero day vulnerability to gain remote code execution on the users machine. Remote cod execution is used to install malware on the users machine. The used vulnerability allows the adversary to get "only" user rights, not root. The adversary gains root through escalate privileges using a second vulnerability. This allows the adversary to tamper with iptables rules, to make non-Tor connections and so on. This attack gets circumvented by Whonix, because Whonix's Firewall runs on another (virtual) machine. This attack gets circumvented by Whonix, because any root applications inside Whonix, including malware with root rights, can only connect through Tor.

(5) Example: user visits a website over Tor with a torified Browser. The website uses known or zero day vulnerability to gain remote code execution on the users machine. Remote cod execution is used to install malware on the users machine. The used vulnerability allows the adversary to get root rights. This allows the adversary to tamper with iptables rules, to make non-Tor connections and so on. This attack gets circumvented by Whonix, because Whonix's Firewall runs on another (virtual) machine. This attack gets circumvented by Whonix, because any root applications inside Whonix, including malware with root rights, can only connect through Tor.

(6)  Example: user visits a website over Tor with a torified Browser. The website uses known or zero day vulnerability to gain remote code execution on the users machine. Remote cod execution is used to install malware on the users machine. A second exploit is being used to break out of the Virtual Machine. Whonix Standard Download version host+vm+vm is broken against this attack. Whonix Physical Isolation defeats this attack, because the Whonix-Workstation's host does not know it's real IP address, only Whonix-Gateway, running on an other physical machine knows it.

(7) Same as attack (5). But the adversary uses an extra vulnerability to break into Whonix-Gateway. Whonix is broken against this attack.

(8) Example: user visits a website over Tor with a torified Browser. The website uses known or zero day vulnerability to gain remote code execution on the host. Whonix Standard Download version host+vm+vm: fail, same as attack (5). Physical Isolation defeats this attack, same as attack (5).

(9) Example: user visits a website over Tor with a torified Browser. The website uses known or zero day vulnerability to gain remote code execution on the host. The adversary uses an extra vulnerability to break Whonix-Gateway. Whonix is broken against this attack.

(10) Example: user visits a website over Tor with a torified Browser. Tor processes the traffic. The adversary uses a vulnerability to gain remote code execution. The machine were Tor is running always ^2^ knows the users real IP address. Whonix is broken against this attack.

(11) Example: end to end correlation attack, but there are much more attacks where Tor is known to be broken against. Any successful attack against Tor on a Tor based anonymity operating system will naturally deanonymize the user. ^2^ ^3^

<font size="-3">
,,
^1^ Placeholder. 
^2^ Unless you are using Multiple Gateways. (Optional Whonix feature in progress.) 
^3^ Whonix defeats some attacks against Tor (and components such as Tor Browser), for example, see [Whonix's Secure And Distributed Time Synchronization Mechanism](https://sourceforge.net/p/whonix/wiki/TimeSync/) and [Whonix's Protocol-Leak-Protection and Fingerprinting-Protection](https://sourceforge.net/p/whonix/wiki/Whonix%27s%20Protocol-Leak-Protection%20and%20Fingerprinting-Protection/) and the rest of the Security and Hardening page.
^4^ Workstation doesn't know it's own external IP address.
^5^ Prevented by firewall.
^6^ VM replaces the IP with an internal LAN IP, which is safe.
</font>

### Network Time related

Knowledge assumed:

* [Tails Design: Time synching](https://tails.boum.org/contribute/design/Time_syncing/)
* [Whonix Design: TimeSync](https://sourceforge.net/p/whonix/wiki/TimeSync/)
* In the following table,
    * "(VM host) update/crypto block" is defined as: Can prevent (VM host) operating system updates and cryptographic verification such as for SSL verification in (VM host) browser.
    * "u/c-block" is defined as: update/crypto block
    * "Tor blocked" is defined as: Can prevent connections to the Tor network until clock gets manually fixed.
    * "big clock skew" is defined as: more than 1 hour in past or more than 3 hour in future. ^13^
    * "small clock skew" is defined as: less then 1 hour in past or less than 3 hour in future. ^13^

_ | Whonix Standard Download version host+vm+vm | Whonix Physical Isolation | Tails | Tails in a VM | TBB | TBB in a VM | Qubes OS TorVM
------------- |  ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | -------------
Info: VM host time synchronization mechanism | NTP | Gateway: There is no VM host.; Workstation host: NTP | There is no VM host. Same as operating system synchronization mechanism | NTP | There is no VM host. | NTP | NTP
Info: operating system synchronization mechanism | tails_htp | tails_htp | tordate and tails_htp | tordate and tails_htp | NTP | NTP | (?)
if clock is too much off | Tor blocked | Tor blocked | tordate will fix it. | tordate will fix it. | Tor blocked | Tor blocked | Tor blocked
VM host time differs from operating system time | Yes, ^2^ | Yes, ^2^ | There is no VM host. | Yes. ^11^ | No. ^5^  | Maybe. ^6^ | No
unsafe browser time differs from torified browser time. ^1^ | Yes. ^2^ | Yes. ^3^ | No. ^10^ | No. ^10^ | No. ^5^ | Maybe. ^6^ | No
big clock skew attack against NTP ^8^: VM host effects | u/c-block | VM host u/c-block | There is no VM host. | VM host u/c-block | There is no VM host. | VM host u/c-block | u/c-block
big clock skew attack against NTP ^8^: operating system effects | Tor blocked | Tor blocked | ^7^; tordate will fix it. | ^7^; tordate will fix it. | Tor blocked; u/c block | Tor blocked; u/c block | Tor blocked
Fingerprintable reaction ^12^ when big clock skew attack was used | No, fails the same way TBB fails. | No, fails the same way TBB fails. | Probable yes, see Fingerprint section above. | Probable yes, see Fingerprint section above. | TBB | TBB | No
small clock skew attack against NTP ^8^, VM host effects: | VM host u/c block | VM host u/c block | There is no VM host. | VM host u/c block | VM host u/c block | VM host u/c block | VM host u/c block
small clock skew attack against NTP ^8^, operating system effects: | Whonix VMs: tails_htp will fix it. | tails_htp will fix it. | VM: tails_htp will fix it. | tails_htp will fix it. | If users visits a page which is under observation by the adversary, the adversary knows who is connecting. ^9^ | If users visits a page which is under observation by the adversary, the adversary knows who is connecting. ^9^ | If users visits a page which is under observation by the adversary, the adversary knows who is connecting. ^9^

<font size="-3">
,,
^1^ This is important because otherwise non-anonymous activity could be linked to anonymous activity if the clock skew is too big and/or too unique.
^2^ Because unsafe browser runs on the VM host (NTP) and torified browser runs inside Whonix-Workstation. (tails_htp)
^3^ Whonix-Workstation (tails_htp) and Whonix-Gateway (separate tails_htp) time differ.
^4^ VM host time gets synchronized with NTP and VM time gets synchronized with tails_htp.
^5^ Untorified host browser uses the same clock as TBB.
^6^ Host and VM clock both get synchronized with NTP, but it could still make a difference, because they are synchronized independently.
^7^ Assumed an installed regular operating system using NTP was used earlier and the adversary introduced a clock skew.
^8^ Introduced by ISP level adversary attack.
^9^ Due to unique clock skew.
^10^ Unsafe browser and torified browser share the same clock. (tails_htp)
^11^ VM Host time gets synchronized with NTP and operating system time gets synchronized with tails_htp.
^12^ Such as running tordate.
^13^ [source of information](https://lists.torproject.org/pipermail/tor-talk/2012-February/023264.html)
</font>

## Usability
| | Whonix | Tails | Tor on the host | Qubes OS TorVM
------------- |  ------------- | ------------- | ------------- | -------------
Difficulty to install additional software while IP remains hidden ^1^ | easy ^2^ | medium ^3^ | hard ^4^ | easy
Difficulty to initially install the anonymity software | medium ^5^ | easy | easy | easy (?)
Required knowledge to prevent the user shooting it's own feet ^7^ | hard | hard | hard | hard
Pre-installed applications | Not many. ^6^ | Nice selection. | None. | Not many. (?)
Host clock too much off | No connection to the Tor network until clock gets manually fixed. | Uses [tordate](https://tails.boum.org/contribute/design/Time_syncing/) to fix it. | No connection to the Tor network until clock gets manually fixed. | No connection to the Tor network until clock gets manually fixed.

<font size="-3">
,,
^1^ To do it safely.
^2^ Easy: In Whonix one could also install an [Tor-unsafe](https://blog.torproject.org/blog/bittorrent-over-tor-isnt-good-idea) BitTorrent client. In worst case it would be pseudonymous (IP still hidden) rather than anonymous.
^3^ Medium: Tails has a firewall to block non-Tor traffic, but an [audit](https://tails.boum.org/todo/applications_audit/) at protocol level is still required. Quoted from the [Tails Security Page](https://tails.boum.org/security/index.en.html): *"Until an [audit](https://tails.boum.org/todo/applications_audit/) of the bundled network applications is done, information leakages at the protocol level should be considered as − at the very least − possible."*
^4^ Hard: It's left to the user to prevent non-Tor traffic, DNS leaks and protocol level leaks.
^5^ Text, screenshot or video instructions [available](https://sourceforge.net/p/whonix/wiki/Download/#install-whonix).
^6^ This and the whole documentation will be improved in next Whonix version.
^7^ Examples what not to do: [DoNot](https://sourceforge.net/p/whonix/wiki/DoNot/).
</font>

## Many other differences
Please also read [Why don't you merge with Tails and join efforts?](https://sourceforge.net/p/whonix/wiki/FAQ/#why-dont-you-merge-with-tails-and-join-efforts).

## Conclusion
Conclusion: different threat model, different implementation, different use cases, although some overlap. Different political and design decisions.

## Part 2
[Comparison Of Tor, Proxies, CGI proxies, Proxy Chains and VPN Services](https://sourceforge.net/p/whonix/wiki/ComparisonOfTorProxiesCGIproxiesProxyChainsAndVPNServices/)

# Footer #
[[include ref=WikiFooter]]