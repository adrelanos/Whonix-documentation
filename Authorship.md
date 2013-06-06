[[include ref=WikiHeader]]

[TOC]

# DISCLAIMER #
## General ##
__**DISCLAIMER:**__ The authors accept NO responsibility for any leaks, faults, detection, incarceration, torture, etc; as  a result of your use of Whonix.  NO WARRANTY expressed or implied.

We have done our best to create this project, but we are not programmers, network experts, tor expert, lawyer, etc; Just a Tor user who have done extensive research on Google. Be careful, use your brain, trust no one but yourself.

## Whonix VPN disclaimer ##
You only have to read this chapter, when you are going to combine Whonix with a VPN.

Whonix is in no way affiliated with any VPN provider.

The mentioned VPN providers on other wiki pages have been chosen, because we found them, it was easy to register, no personal information were required and because it was free. Whonix developers do not review or rate VPN providers, that is beyond the Whonix project. You are welcome to post instructions for other free VPN services, which will be treated equally. In no way any provider is labeled as a good/bad choice.

Depending on what they were used for, they also fulfilled certain criteria, which are mentioned in the specific article. For example: TCP connection supported; not blocking UDP ports; OpenVPN supported, many other free providers offered only access through proprietary, closed source and/or windows-only clients.

Most websites recommend for choosing a good VPN: 
1. Do not use free VPNs, as they observe you, log everything and sell you. 
2. Leave no money trail, pay anonymously. (Bitcoin etc.) ([Anonymous Money page](https://sourceforge.net/p/whonix/wiki/Money/))
3. Research their reputation, background, history, location. 
4. Check their privacy policy and terms of service. 
5. They shouldn't ask for any identifying information. (name, postal address, e-mail etc.) 
6. The providers homepage is reachable over http**s** with a valid SSL certificate. 
7. You can use GPG to mail them. ([gpg mail encryption chapter](https://sourceforge.net/p/whonix/wiki/Software/#encrypt-decrypt-sign-and-verify-text-using-openpgp-gnupg-frontend))
8. They offer to use their service with a VPN software, which secure and [Free Software](https://en.wikipedia.org/wiki/Free_software), such as OpenVPN.

Use at your own risk.

# Code Contributors #
**Current Maintainers**

At the moment only adrelanos develops and maintains Whonix. Help is welcome!

* adrelanos (adrelanos at riseup dot net): anonymous author; see disclaimer; initially researched extensively and compiled all information floating around the web into a guide; Later created the Whonix build scripts, binary images, extended documentation.

**Past Code Contributors **

* smarm: made many things in TorBOX guide much clearer; English languages fixes; created leaktest scripts; Thank you! (smarm [at] hushmail dot com)
* cypherpunks/anonymous: Everyone can contribute! Feb 2012: added a shell script to automate set up TorBOX, changed guide to use VirtualBox instead of VMware, rewritten the iptables firewall and added a hardening section.

# Arts Contriutors #
* original TorBOX logo

Made by CJ.

* Whonix Stream Isolation Graphic

Cuan Knaggs – graphic and web design
[revlover](http://revolver.za.net)
print media – web design – web development – cms – e-commerce

# Contributors #
In random order.

**[Joshua](https://sourceforge.net/u/jbwhonixxxx/profile/)**

* Forum Moderator
* contributed a phone number, so the Whonix Google+ and Youtube account could be set up
* documentation feedback
* testing Whonix images

**scarp**

* comments on Whonix source code and changes
* review Whonix build documentation
* testing Whonix building from source code
* helped with Whonix TorChat integration
* reviewing public relation

**anonymous**

* documentation feedback

# Credits, Inspiration, Alternatives, Sources #
## credits ##
**In random order.**

**Without those projects and the people behind who created and maintain those, Whonix in it's current form wouldn't have been possible.**

* [GNU](https://www.gnu.org/)
* [Ubuntu GNU/Linux](http://www.ubuntu.com/)
* Debian GNU/Linux
* [Tails](http://tails.boum.org/)
* Some documentation pages forked from [Tails](http://tails.boum.org/) by adrelanos for Whonix. See [TailsDocFork](https://sourceforge.net/p/whonix/wiki/TailsDocFork/) for a list, which documentation pages have been forked.
* The Tor Project
* help-bash Mailing List

** For general thoughts on anonymity networks and threat models. **

* Liberte Linux
* JonDo
* i2p 

Misc things.

* bitboy for bitcoin logo https://bitcointalk.org/index.php?topic=1631.0
* leo bogert for Simple Bitcoin Donate Button http://leo.bogert.de/2012/02/22/simple-bitcoin-donate-button/

## sources ##
Sources I (adrelanos) learned from:

In random order.

* [http://www.debiantutorials.com/installing-and-configuring-pptp-vpn-server-on-lenny/ Debian Tutorials: Installing and configuring PPTP VPN server on lenny]
* [http://www.debiantutorials.com/loading-iptables-rules-on-startup/ Debian Tutorials: Loading iptables rules on startup]
* [http://www.howtogeek.com/51237/setting-up-a-vpn-pptp-server-on-debian/ How-To Geek: How to Setup a VPN (PPTP) Server on Debian Linux]
* [https://trac.torproject.org/projects/tor/wiki/doc/TransparentProxy Tor Project: Transparently Routing Traffic Through Tor]
* [http://www.mail-archive.com/tor-talk@lists.torproject.org/msg03291.html “Re: (tor-talk) Aurora only build”]
* [https://en.wikibooks.org/wiki/How_to_Protect_your_Internet_Anonymity_and_Privacy/TOR_Hidden_Service_for_Anonymous_Websites wikibooks.org How to Protect your Internet Anonymity and Privacy/TOR Hidden Service for Anonymous Websites]
* http://blog.bodhizazen.net/linux/how-to-transparent-proxy/
* http://www.webupd8.org/2012/02/encrypt-dns-traffic-in-linux-with.html
* https://anonymous-proxy-servers.net/forum/viewtopic.php?f=10&t=6680
* https://anonymous-proxy-servers.net/en/help/transocks.html
* http://www.kubuntuforums.net/showthread.php?58706-Making-folderview-as-default-for-all-new-users
* http://www.debianadmin.com/how-to-auto-login-and-startx-without-a-display-manager-in-debian.html
* KDE Mailing List
* http://packages.linuxmint.com/pool/main/m/mint-configuration-kde/mint-configuration-kde_5.0.9.tar.gz
* http://www.askubuntu.com/questions/252734/apt-get-mass-install-packages-from-a-file
* http://www.cyberciti.biz/faq/dhclient-etcresolvconf-hooks/
* http://stackoverflow.com/questions/59895/can-a-bash-script-tell-what-directory-its-stored-in
* http://unix.stackexchange.com/questions/12068/how-to-measure-time-of-program-execution-and-store-that-inside-a-variable
* http://stackoverflow.com/questions/8426058/bash-get-the-parent-directory-of-current-directory
* http://stackoverflow.com/questions/13426908/dialog-in-bash-is-not-grabbing-variables-correctly
* http://mywiki.wooledge.org/

## Similar Projects ##
Here is a list of projects with similar goals to Whonix. The list is here for reference. Those projects may have interesting thoughts, mistakes, security enhancements, features and so on. The useful stuff can be potentially ported to Whonix. Some projects inspired the development of Whonix (missing features, implementation reference etc.).

 * [A few reasons listed in this link not to use some of those projects applies here as well.](https://trac.torproject.org/projects/tor/wiki/doc/JanusVM)
 * [Torouter](https://trac.torproject.org/projects/tor/wiki/doc/Torouter); alpha
 * [Tor and the DreamPlug](https://trac.torproject.org/projects/tor/wiki/doc/TorDreamPlug); similar networking/firewall
 * [Tor and OpenWRT](https://trac.torproject.org/projects/tor/wiki/doc/OpenWRT); similar networking/firewall
 * [Transparent Proxy](https://trac.torproject.org/projects/tor/wiki/doc/TransparentProxy); it offers: 1. Transparently anonymizing traffic for a specific user; 2. Local Redirection Through Tor; 3. Anonymizing Middlebox; 4. Local Redirection and Anonymizing Middlebox; closest one to Whonix is Anonymizing Middlebox; Whonix is an Isolating Proxy
 * [Transocksifying Tor](https://trac.torproject.org/projects/tor/wiki/doc/TransocksifyingTor); now outdated; back when Tor didn't natively support TransPort; uses a different firewall with DNAT
 * [PELD](https://tails.boum.org/contribute/design/); specification and implementation (in the form of Tails
 * [A Tor Virtual Machine Design and Implementation](https://svn.torproject.org/svn/torvm/trunk/doc/design.html); design document
 * [JanusVM](https://trac.torproject.org/projects/tor/wiki/doc/JanusVM); insecure
 * [TorVM](http://www.janusvm.com/tor_vm/); from the same authors like JanusVM; [other link](https://svn.torproject.org/svn/torvm/); insecure
 * [TorVPN](https://trac.torproject.org/projects/tor/wiki/doc/TorVPN); the abandoned predecessor of TorBOX (now Whonix); not finished
 * [another TorVM](http://tor.hermetix.org/torvm/index.html.en); from unknown authors; site wants to look similar to official Tor site; fishy
 * [Easy and secure anonymous internet usage](http://ra.fnord.at/2011/05/easy-and-secure-anonymous-internet-usage) by ra; anonymous author; [https://github.com/ra--/Tor-gateway/wiki now with source code]
 * [Tails](http://tails.boum.org); Live CD/USB distribution preconfigured to use Tor safely.; listed on https://www.torproject.org; with [Tor enforcement](http://tails.boum.org/contribute/design/Tor_enforcement/)
 * old instructions from [board.gulli.com](http://board.gulli.com/thread/993224-tutorial-alle-tcp-ip-verbindung-eines-vmware-guests-automatisch-ueber-tor-leiten); in German language; more complicated; back when Tor didn't natively support TransPort
 * [Tor relay in virtualized OpenBSD with KVM](http://blog.minibofh.org/2011/01/03/tor-relay-in-virtualized-openbsd-with-kvm); no review yet
 * [VM basierende Anonymisierung](http://wiki.ubuntuusers.de/VM_basierende_Anonymisierung); German; not very sophisticated
 * [Tor Hidden Service Server in a box -- Tor Hidden Service VM](http://www.cs.washington.edu/homes/aczeskis/random/tor-hidden-service-vm.html); no review
 * ["My Hidden Blog" - Hosting Tutorial](http://lotjbov3gzzf23hc.onion/hostingtutorial/); based on [Tor Hidden Service Server in a box -- Tor Hidden Service VM](http://www.cs.washington.edu/homes/aczeskis/random/tor-hidden-service-vm.html); no review
 * [Liberté Linux](http://www.dee.su/); Live CD based on hardened Gentoo; No isolation between client applications and Tor, infrequent security releases.
 * [Qubes](http://theinvisiblethings.blogspot.com/2011/09/playing-with-qubes-networking-for-fun.html); focuses on security through isolation based on virtualization. This blog post provides some hints how to integrate Tor but the actual implementation is left to the user.
 * [Hidden Service Setup Guide for Newbies (Version .2)](https://lists.torproject.org/pipermail/tor-talk/2009-September/019541.html); howto; you don't have to download the pdf, you find the guide on google and in google cache (google the pdf link)
 * [VMWare Through Tor](https://trac.torproject.org/projects/tor/wiki/doc/VMWareThroughTor) Getting Tor to proxy connections from inside the VMWare Browser Appliance.
 * TorVM for Qubes (qubes-tor)
    * [TorVM for Qubes (qubes-tor)](https://github.com/abeluck/qubes-addons/blob/master/qubes-tor/README.md)
    * [tor-talk Review request: TorVM implementation in Qubes OS](https://lists.torproject.org/pipermail/tor-talk/2012-October/025960.html)
    * [qubes-devel TorVM implementation](https://groups.google.com/forum/?fromgroups=#!topic/qubes-devel/C1D5_tbl4jM)

Thank you!

# History #
[History] of Whonix.

# License #
See license file in Whonix source code.

# Footer #
[[include ref=WikiFooter]]