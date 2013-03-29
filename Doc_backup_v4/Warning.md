[[include ref=WikiHeader]]

[TOC]

<!--
Copyright:

   Whonix Warning wiki page Copyright (C) Amnesia <amnesia at boum dot org>
   Whonix Warning wiki page Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
   
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
This wiki page is a fork of the Tails Warning page, from this exact source <http://git.immerda.ch/?p=amnesia.git;a=blob_plain;f=wiki/src/doc/about/warning.mdwn;hb=a12ede51f51195374f6f76c33750cb0fd673efef>.
-->

# Introduction 
Even though we're doing our best to offer you good tools to protect your privacy while using a computer, **there is no magic or perfect solution to such a complex problem**. Understanding well the limits of such tools is a crucial step in, first, deciding whether Whonix is the right tool for you, and second, helping you making a good use of it.

# License #
    Whonix Warning wiki page Copyright (C) Amnesia <amnesia at boum dot org>
    Whonix Warning wiki page Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
    
    This program comes with ABSOLUTELY NO WARRANTY; for details see the wiki source code.
    This is free software, and you are welcome to redistribute it
    under certain conditions; see the wiki source code for details.

<a id="exit_node"></a>

Tor exit nodes can eavesdrop on communications
==============================================

**Tor is about hiding your location, not about encrypting your communication.**

Instead of taking a direct route from source to destination, communications using the Tor network take a random pathway through several Tor relays that cover your tracks. So no observer at any single point can tell where the data came from or where it's going.

![A Tor connection usually goes through 3 relays with the last one establishing the actual connection to the final destination](http://whonix.sourceforge.net/pictures/htw2-tails.png)

The last relay on this circuit, called the exit node, is the one that establishes the actual connection to the destination server. As Tor does not, and by design cannot, encrypt the traffic between an exit node and the destination server, **any exit node is in a position to capture any traffic passing through it**.

For example, in 2007, a security researcher intercepted thousands of private e-mail messages sent by foreign embassies and human rights groups around the world by spying on the connections coming out of an exit node he was running. See [Wired: Rogue Nodes Turn Tor Anonymizer Into Eavesdropper's Paradise.](http://www.wired.com/politics/security/news/2007/09/embassy_hacks) ([w](http://www.webcitation.org/6EUyHbBEU)).

**To protect yourself from such attacks you should use end-to-end encryption.**

**Whonix includes many tools to help you using strong encryption** while browsing, sending email or chatting in [Documentation].

<font size="-3">Source: [Tor FAQ: Can exit nodes eavesdrop on communications?](https://trac.torproject.org/projects/tor/wiki/TheOnionRouter/TorFAQ#CanexitnodeseavesdroponcommunicationsIsntthatbad) ([w](http://www.webcitation.org/6EUyAPZe4))</font>

Whonix makes it clear that you are using Tor
============================================

Tor tries to prevent attackers from learning what destination websites you connect to. 

**Unless** you are using the Optional Configuration [Hide the fact, that you are using Tor/Whonix from your ISP](https://sourceforge.net/p/whonix/wiki/Hide%20Tor%20and%20Whonix%20from%20your%20ISP/) **Your ISP or your local network administrator** can easily check that you're connecting to a Tor relay, and not a normal web server for example.

**Unless** you are using the Optional Configuration [Tunnel Tor through proxy, VPN or SSH](https://sourceforge.net/p/whonix/wiki/Tunnel_Tor_through_proxy_or_VPN_or_SSH/) **The destination server your are contacting through Tor** can know whether your communication comes out from a Tor exit node by consulting the publicly available list of exit nodes that might contact it. For example using the [Tor Bulk Exit List tool](https://check.torproject.org/cgi-bin/TorBulkExitList.py) of the Tor Project.

**So unless you are using Optional Configurations to prevent this, using Whonix doesn't make you look like any random Internet user.** The anonymity provided by Tor and Whonix works by trying to make all of their users look the same so it's not possible to identify who is who amongst them.

Ultimately the best protection is a social approach: the more Tor users there are near you and the more [diverse](https://www.torproject.org/about/torusers.html.en) their interests, the less dangerous it will be that you are one of them. Convince other people to use Tor, too!

<font size="-3">
Attribution:
Two sentences in the "Whonix makes it clear that you are using Tor" chapter, have been forked from the [Tor](https://www.torproject.org/download/download-easy.html.en) ([w](http://www.webcitation.org/6EUyWNl4n))website, which was licensed under a [Creative Commons Attribution 3.0 United States License](https://creativecommons.org/licenses/by/3.0/us/) ([w](http://www.webcitation.org/6EUyX0A2y)) at this point.
</font>

Whonix might make it clear you are using Whonix
===============================================
Even though Whonix developers designed Whonix not to reveal the fact to your ISP, that you are a Whonix user there might still be an unknown method to find out you are.

In case you care about that, see also the Optional Configuration [Hide the fact, that you are using Tor/Whonix from your ISP](https://sourceforge.net/p/whonix/wiki/Hide%20Tor%20and%20Whonix%20from%20your%20ISP/).

<a id="man-in-the-middle"></a>

Man-in-the-middle attacks
=========================

A man-in-the-middle attack (MitM) is a form of active eavesdropping in which the attacker makes independent connections with the victims and relays messages between them, making them believe that they are talking directly to each other over a private connection, when in fact the entire conversation is controlled by the attacker.

![Illustration of a man-in-the-middle attack](http://whonix.sourceforge.net/pictures/man_in_the_middle.jpg)

While using Tor, man-in-the-middle attacks can still happen between the exit node and the destination server. The exit node itself can also act as a man-in-the-middle. <font size="-3>For an example of such an attack see [MW-Blog: TOR exit-node doing MITM attacks](http://www.teamfurry.com/wordpress/2007/11/20/tor-exit-node-doing-mitm-attacks) ([w](http://www.webcitation.org/6EUybaLf8)).</font>

**Again, to protect yourself from such attacks you should use end-to-end encryption** and while doing so taking extra care at verifying the server authenticity.

Usually, this is automatically done through [SSL](https://en.wikipedia.org/wiki/Transport_Layer_Security) certificates checked by your browser against a given set of recognized [certificate authorities](https://en.wikipedia.org/wiki/Certificate_authority). If you get a security exception message such as this one you might be victim of a man-in-the-middle attack and should not bypass it unless you have another trusted way of checking the certificate's fingerprint with the people running the service.

![This Connection is Untrusted](http://whonix.sourceforge.net/pictures/ssl_warning.png)

[How do I tell if my connection to a website is secure?](https://support.mozilla.org/en-US/kb/how-do-i-tell-if-my-connection-is-secure) ([w](http://www.webcitation.org/6EUzXi9P5))

But on top of that the certificate authorities model of trust on Internet is susceptible to various methods of compromise.

For example, on March 15, 2011, Comodo, one of the major SSL certificates company, reported that a user account with an affiliate registration authority had been compromised. It was then used to create a new user account that issued nine certificate signing requests for
seven domains: mail.google.com, login.live.com, www.google.com, login.yahoo.com (three certificates), login.skype.com, addons.mozilla.org, and global trustee. <font size="-3">Source: [Comodo: The Recent RA Compromise](http://blogs.comodo.com/it-security/data-security/the-recent-ra-compromise/) ([w](http://www.webcitation.org/6EUyeEwBE)).</font>

Later in 2011, DigiNotar, a Dutch SSL certificate company, incorrectly issued certificates to a malicious party or parties. Later on, it came to light that they were apparently compromised months before or perhaps even in May of 2009 if not earlier. Rogues certificates were issued for domains such as google.com, mozilla.org, torproject.org, login.yahoo.com and many more. <font size="-3">Source: [The Tor Project: The DigiNotar Debacle, and what you should do about it](https://blog.torproject.org/blog/diginotar-debacle-and-what-you-should-do-about-it) ([w](http://www.webcitation.org/6EUyf0rpk)).</font>

**This still leaves open the possibility of a man-in-the-middle attack even when your browser is trusting an HTTPS connection.**

There are alternatives to SSL, worth checking out if they may be useful for you. Unfortunately can not be used as a drop in replacement. Tools providing connection security include [Monkeysphere](http://web.monkeysphere.info/), [Convergence](https://en.wikipedia.org/wiki/Convergence_%28SSL%29), [Perspectives Project](http://perspectives-project.org/) and Tor hidden services. <font size="-3">(Hidden services are automatically encrypted end-to-end, see [Hidden Services] for details.)</font>

On one hand, by providing anonymity, Tor makes it more difficult to perform a man-in-the-middle attack targeted at **one specific person** with the blessing of a rogue SSL certificate. But on the other end, Tor makes it easier for people or organizations running exit nodes to perform large scale MitM attempts, or attacks targeted at **a specific server**, and especially those among its users who happen to use Tor.

In all cases, you are advised to use additional message encryption for encrypting your mails, chats and so on. Tools such as encrypted messengers (Covered on [Chat] page.), GPG [(wikipedia)](https://en.wikipedia.org/wiki/GNU_Privacy_Guard), [KGpg](https://sourceforge.net/p/whonix/wiki/Software/#encrypt-decrypt-sign-and-verify-text-using-openpgp-gnupg-frontend) and [Mozilla Thunderbird with TorBirdy](https://sourceforge.net/p/whonix/wiki/E-Mail/) and enigmail (gpg add-on) may be useful.

<font size="-3">Quoted from [wikipedia Man-in-the-middle_attack](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) ([w](http://www.webcitation.org/6EUyk0IKX)) and [Tor Project: Detecting Certificate Authority compromises and web browser collusion](https://blog.torproject.org/blog/detecting-certificate-authority-compromises-and-web-browser-collusion) ([w](http://www.webcitation.org/6EUykcmES)).</font>

Confirmation attacks
====================

Quoted from [Tor Project: "One cell is enough to break Tor's anonymity](https://blog.torproject.org/blog/one-cell-enough) ([w](http://www.webcitation.org/6EUyo9u9N)).

"*The Tor design doesn't try to protect against an attacker who can see or measure both traffic going into the Tor network and also traffic coming out of the Tor network. That's because if you can see both flows, some simple statistics let you decide whether they match up.*

*That could also be the case if your ISP (or your local network administrator) and the ISP of the destination server (or the destination server itself) cooperate to attack you.*

*Tor tries to protect against traffic analysis, where an attacker tries to learn whom to investigate, but Tor can't protect against traffic confirmation (also known as end-to-end correlation), where an attacker tries to confirm an hypothesis by monitoring the right locations in the network and then doing the math.*"

Whonix doesn't encrypt your documents by default
===============================================

The documents that you might save inside Whonix will not be encrypted by default. The [Advanced Security Guide] recommends [to fully encrypt the host](https://sourceforge.net/p/whonix/wiki/Advanced%20Security%20Guide/#full-disk-encryption).

It is likely that the files you may create will keep tracks that they were created using Whonix. (Under research.)

Whonix is not amnesic
=====================
Other than Tails, Whonix is not an Amnesic Live CD. If you install Whonix on your computer this will leave local traces on the harddrive, that you installed Whonix on that device. Any files you create will still exist after powering off or rebooting unless you securely wiped all signs of their previous existence.

There are no special measures to limit what is written to disk. This includes (non exclusive list) user created files, backup files, temporary files, swap, chat history, browser history and so on. Whonix acts like an ordinary installed operating system. It can also not be prevented, that the host memory [swaps](https://en.wikipedia.org/wiki/Swap) to the host disk. There is a [Recommendation to use multiple VM Snapshots](https://sourceforge.net/p/whonix/wiki/Security%20Guide/#recommendation-to-use-multiple-vm-snapshots) and it is is [recommend](https://sourceforge.net/p/whonix/wiki/Advanced%20Security%20Guide/#full-disk-encryption) to apply Full Disk Encryption on the host.
 
Whonix doesn't clear the metadata of your documents
===================================================

Numerous files format store hidden data or metadata inside of the files. Text processors or PDF files could store the name of the author, the date and time of creation of the file, and sometimes even parts of the editing history of the fileâ€¦ those hidden data depend on the file format and the software used. 

Images file formats, like TIFF of JPEG, probably take the prize in this field. Those files, created by digital cameras or mobile phones, contain a metadata format called EXIF which can include the date, time and sometimes the GPS coordinates of the picture, the brand and serial number of the device which took it as well as a thumbnail of the original image. Image processing software tend to keep those data intact. Internet is full of cropped or blurred images for which the EXIF thumbnail still contains the full original picture.

**Whonix doesn't clear the metadata of your files for you**. Yet. Still it's in Whonix' design goal to help you do that. For example, Whonix already comes with [MAT](https://sourceforge.net/p/whonix/wiki/Metadata/), which is an Metadata Anonymisation Toolkit.

Whonix doesn't encrypt the Subject: and other headers of your encrypted e-mail messages
=======================================================================================
Please note, that the Subject: as well as the rest of the header lines of your OpenPGP encrypted e-mail messages are not encrypted. This is not a bug of Whonix or the [OpenPGP](http://www.mozilla-enigmail.org/forum viewtopic.php?f=3&t=328) ([w](http://www.webcitation.org/6EUyt6L0f)) protocol; it's for backwards compatibility with the original SMTP protocol. Unfortunately no RFC standard exists yet for Subject encryption.

If you are looking for an e-mail client supporting OpenPGP encryption (enigmail), [Mozilla Thunderbird with TorBirdy](https://sourceforge.net/p/whonix/wiki/E-Mail/) is recommend.

Tor doesn't protect you from a global adversary
===============================================
A global passive adversary would be a person or an entity able to monitor at the same time the traffic between all the computers in a network. By studying, for example, the timing and volume patterns of the different communications across the network, it would be statistically possible to identify Tor circuits and thus matching Tor users and destination servers.

It is part of Tor's initial trade-off not to address such a threat in order to create a low-latency communication service usable for web browsing, Internet chat or SSH connections.

For more expert information see [Tor Project: The Second-Generation Onion Router](https://svn.torproject.org/svn/projects/design-paper/tor-design.pdf), ([w](http://www.webcitation.org/6EUyv297d)) part 3. Design goals and assumptions.

<a id="identities"></a>

Whonix doesn't magically separate your different contextual identities
=====================================================================
It is usually not advisable to use the same Whonix-Workstation to perform two tasks or endorse two contextual identities that you really want to keep separate from another. For example hiding your location to check your email and publishing anonymously a document.

First, because Tor tends to reuse the same circuits, for example amongst a same browsing session. Since the exit node of a circuit knows both the destination server (and possibly the content of the communication if not encrypted) and the address of the previous relay it received the communication from, it makes it easier to correlate the several browsing requests as part of a same circuit and possibly made by a same user. If you are facing a global adversary as described above, it might then also be in position to do this correlation.

Second, in case of a security hole or a misuse in using Whonix or one of its application, information about that Whonix-Workstation could be leaked. That could reveal that the same person was behind the various actions made inside that Whonix-Workstation.

**The solution to both threats is either following the [Recommendation to use multiple VM Snapshots](https://sourceforge.net/p/whonix/wiki/Security%20Guide/#recommendation-to-use-multiple-vm-snapshots) and/or to [use multiple Whonix-Workstations](https://sourceforge.net/p/whonix/wiki/Multiple%20Whonix-Workstations/)** every time you're using a new identity, if you really want to isolate them better.

[arm's](https://sourceforge.net/p/whonix/wiki/TorController/) "New Identity" button forces Tor to use new circuits but only for new connections: existing connections might stay open. Plus, apart from the Tor circuits, other kind of information can reveal your past activities, for example the cookies stored by your browser. So this feature of arm is not a solution to really separate contextual identities.

Whonix doesn't make your crappy passwords stronger
=================================================
Tor allows you to be anonymous online; Whonix ensures that the whole operating system is forced through Tor (and many other extra Security features, see [Design]). But again, **neither of both are magic spells for computer security**.

If you use weak passwords, they can be guessed by brute-force attacks with or without Whonix in the same way. To know if your passwords are weak and learn good practices to create better password, you can read [Wikipedia: Weak Passwords](https://en.wikipedia.org/wiki/Password_strength#Examples_of_weak_passwords) ([w](http://www.webcitation.org/6EUz4uxz8)).

Whonix doesn't secure your host
===============================
Whonix can only be as secure as the host is. Of course you can as probable many people do simply use Whonix on top of your every day operating system. You will be much safer if you follow the [Recommendation to use a dedicated host operating system](https://sourceforge.net/p/whonix/wiki/Pre%20Install%20Advice/#recommendation-to-use-a-dedicated-host-operating-system).

# Only Whonix-Workstation is designed for anonymous activity #
Easy:
All anonymous activity should only happen inside Whonix-Workstation. Nowhere else.

Explanation:
The host operating system (the operating system running Virtual Box, the system you used before ever downloading Whonix) will NOT be torified. Do never do any anonymous tasks on your host.

The Whonix-Gateway's only purpose is running Tor and the firewall. In most cases there is no need to modify things on the Gateway. Minor modifications such as setting up bridges are documented.

# Whonix doesn't improve security/anonymity outside of Whonix #
Obviously, Whonix can't stop people form looking over your shoulder or stop (mobile) providers from pinpointing your location if you gave it to a website for (mobile) phone verification. 

# Whonix doesn't prevent you from shooting your own feet #
If you login into your personal Facebook account, which is bound to you real name, you are obviously not anonymous and other things.

This will be substantiated on the later page [Non technical steps staying anonymous](https://sourceforge.net/p/whonix/wiki/DoNot/).

# Whonix doesn't defeat Stylometry #
Whonix does not obfuscate you writing style.

This will be substantiated on the later page [Anonymous Surfing, Posting and Blogging](https://sourceforge.net/p/whonix/wiki/Surfing_Posting_Blogging/).

# Whonix does not (yet)... #
Whonix is currently alpha quality software and missing features, some of them security related. Some of the following will probably never get "fixed" or implemented because they are impossible to do in a software only project.

Whonix in its current form does not:

* Encrypt your stuff.
* Wipe RAM on shut down. See [Idea #30076: Enhancy Privacy/Security, Wipe RAM on shut down, reboot and trigger](http://brainstorm.ubuntu.com/idea/30076/).
* Wipe video RAM on shut down. See [Tails -erase video memory on shutdown ](https://tails.boum.org/todo/erase_video_memory_on_shutdown/).
* Make weak passwords stronger.
* Protect against local adversaries, who for example can mount cold boot and evil maid attacks.
* Protect you if you don't read our [Documentation] or do stupid things or change default settings without knowing what you are doing.
* Automatically apply security updates. This was a conscious decision because automated updates also come with their own set of security problems. However, you will be notified about updates on Whonix-Workstation by whonixcheck.
* Protect against global network adversaries.
* Protect against hardware or software backdoors.
* Automatically protect against MAC address fingerprinting on public networks.
* Protect against the more skilled software attack, unless you use  [PhysicalIsolation].
* By default, protect you if Tor is somehow broken. You can improve that to some extend and with caveats by chaining Tor with SSH, proxies or VPNs.
* By default, hide the fact that you are using Tor, though there is an optional feature, [Hide the fact you are using Tor/Whonix](https://sourceforge.net/p/whonix/wiki/Hide%20Tor%20and%20Whonix%20from%20your%20ISP/).
* Use all the possible hardening options like full PIE and grsecurity. It doesn't use AppArmor profiles for everything.
* Obfuscate your writing style, defeat Stylometry.
* Have deterministic builds, see [Dev]. Also Tor itself does not have deterministic builds yet, see [Bug 3688](https://trac.torproject.org/projects/tor/ticket/3688).
* This list might be incomplete. Please read the rest of the [Documentation] (and perhaps [Design] as well) to if you want an overview about security, what's in and what not.

If you want to help us improve the security of Whonix, please join the discussions on [Dev] or on the developer mailing list.

Whonix is a work in progress
===========================
Whonix, as well as all the software it includes, are on continuous development and might contain programming errors or security holes. [Stay tuned](https://sourceforge.net/p/whonix/wiki/Download/#stay-tuned) to Whonix development. Do not rely on it for strong anonymity.

Whonix 0.4.5 is currently alpha quality software.

The basic functionality is ready. You can use Whonix to browse the web and [host hidden services](https://sourceforge.net/p/whonix/wiki/Hidden%20Services/), use email, IRC, ssh, etc. Development is still ongoing and more features are being added to Whonix. If you want join the development process or want to see what issues are still open visit [Whonix/Dev](https://sourceforge.net/p/whonix/wiki/Dev).

From [Whonix 0.4.5 release announcement](https://lists.torproject.org/pipermail/tor-talk/2012-October/025921.html) ([w](http://www.webcitation.org/6EUzBC5nH)):

      Whonix uses the best of both worlds, the Isolating Proxy concept [2]
    and the Transparent Proxy concept. At the moment there are no known
    anonymity leaks or proxy bypass problems. The principal design is less
    vulnerable for any kind of leaks. At time of writing (October 2012) I
    have been working on the theoretical concept and practical
    implementation for 9 months, the basics have been developed by (at
    least) three people, adrelanos, smarm and anonymous. [1] [2]

      Although Whonix has been developed with greatest care, a negative,
    being leak free or being free form mistakes in the extended project
    description [1], can not be proven. This is Whonix's first release
    announcement. I hope skilled people look into the concept and
    implementation and fail to find anonymity related bugs.

See also [Whonix security in real world](https://sourceforge.net/p/whonix/wiki/Security%20in%20Real%20World/), [Security Reviews and Feedback](https://sourceforge.net/p/whonix/wiki/Security%20Reviews%20and%20Feedback/) and [Security Overview](https://sourceforge.net/p/whonix/wiki/Technical%20Introduction/#security-overview).

# Footer #
[[include ref=WikiFooter]]