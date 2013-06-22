[[include ref=WikiHeader]]

[TOC]

<!--
Copyright:

   Whonix About wiki page Copyright (C) Amnesia <amnesia at boum dot org>
   Whonix About wiki page Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
   
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
This wiki page is a fork of the Tails About page, from this exact source <http://git.immerda.ch/?p=amnesia.git;a=blob;f=wiki/src/about.mdwn;hb=9ff23c529b206f6f3d637257f8f1f2aa434f3d27>.
-->

= Introduction =

Whonix is an operating system that aims at preserving your privacy and anonymity. It helps you to use all kinds applications anonymously.

It is a complete operating-system designed to be used from your host operating system or a USB hard drive independently of the computer's original operating system. It is Free Software and based on [http://www.debian.org/ Debian GNU/Linux], Virtual Box and Tor.

Whonix comes with several built-in applications pre-configured with security in mind: web browser, irc client, word processing, etc.

= Anonymity online through Tor =

Whonix relies on the Tor anonymity network to protect your privacy online: all connections are forced through Tor, and direct (non-anonymous) connections are blocked.

Tor is free software and an open network that helps you defend against a form of network surveillance that threatens personal freedom and privacy, confidential business activities and relationships, and state security known as traffic analysis.

Tor protects you by bouncing your communications around a distributed network of relays run by volunteers all around the world: it prevents somebody watching your Internet connection from learning what sites you visit, and it prevents the sites you visit from learning your physical location.

To learn more about Tor, see the official [https://www.torproject.org/ Tor website]:

* [https://www.torproject.org/about/overview.html.en#whyweneedtor Tor overview: Why we need Tor]
* [https://www.torproject.org/about/overview.html.en#thesolution Tor overview: How does Tor work]
* [https://www.torproject.org/about/torusers.html.en Who uses Tor?]

= Whonix is based on Debian, VirtualBox and Tor =

Remember, Whonix is based on Debian, KDE, VirtualBox, Tor and Tor Browser. It is nothing very special. To oversimplify it: Whonix is just a collection of configuration files. <sup>1</sup>

No stripped down versions are used. For example, anything <sup>2</sup> you can do with Debian GNU/Linux, you can do with Whonix as well. Most Debian GNU/Linux problems and questions with Whonix you may have can probable be solved the same way as for &quot;vanilla&quot; Debian. Q: &quot;How do I install xrandr on Debian GNU/Linux?&quot; A: &quot;The same way you would with regular Debian GNU/Linux. Try ''apt-get install xrandr''. Nothing special. Same goes for Tor etc. Whonix doesn't break anything, it doesn't stop you from using obfuscated [https://sourceforge.net/p/whonix/wiki/Bridges/ bridges] or any other fancy stuff etc.

Tip: since Ubuntu is based on Debian, most things working on Ubuntu will also work on Debian. Most online help for Ubuntu also works for Debian.

<font size="-3"> ,, <sup>1</sup> Plus some shell extra shell scripts, a perl script (tails_htp) and a package selection. Whonix just puts everything together. <sup>2</sup> Actually only &quot;almost&quot; everything. Any limitations (beside bugs) will be Tor's responsibility. For example, UDP is not supported by Tor yet, therefore this won't work. </font>

= Cryptography =

<a id="cryptography"></a>

Whonix contains some State-of-the-art cryptographic tools, a selection of tools to protect your data using strong encryption:

* Automatically encrypt with HTTPS all your communications to a number of major websites using [https://www.eff.org/https-everywhere HTTPS Everywhere], a Firefox extension developed by the [https://www.eff.org Electronic Frontier Foundation].
* [https://en.wikipedia.org/wiki/GNU_Privacy_Guard GNU Privacy Guard]

= Summary of what Whonix is =

== What is Whonix? ==

* Whonix is an Anonymous Operating System, that spoofs your own IP/location.
* Tor multiply encrypts the data sent over the Tor network. Neither your access provider nor Tor operators (except for the exit node) can see your plaintext data.
* Tor does regularly change the outgoing IP address.
* Whonix is an Anti-Censorship-Application that allows access to otherwise blocked Internet sites. Advanced users may configure their Whonix as a forwarding server in order to allow others access to the Tor network.
* Whonix is open source and free.
* Tor Browser in Whonix filters and anonymizes HTTP headers.
* For anonymous e-mails please see [E-Mail], i.e. use Mozilla Thunderbird with TorBirdy, because it provides special, additional data filtering in the email client itself.
* Whonix is available on all major systems (Windows, Mac OS X, Linux).

== What is Whonix not? ==

* Whonix does NOT make your PC's or router's IP address invisible. Your IP address is assigned to you by your ISP, and it is inalterable by third parties. You need the IP so that the Tor client may successfully connect to the Tor network on the Internet. When using Whonix, you are surfing through Tor servers on the Internet that all have their own separate IP address. The websites accessed by you will only see this respective outgoing address and not yours.
* Whonix does NOT accelerate Internet access. In fact by routing everything through the Tor network it becomes slower.
* Whonix is NOT The Tor Project. Tor is developed by The Tor Project.
* Whonix does not NOT use random &quot;anonymous&quot; proxies (e.g. those on lists of open proxies) to create an anonymous connection. This would be a totally unsafe method that does not lead to anonymization.
* Whonix is NO One-Click-Anonymization-Tool - something like that can and will not really ever exist! Prudence and knowledge remain maxim for Internet security.

= What's next? =

To continue discovering Whonix, you can now read:

* the [Warning] page to understand better the security limitations of Whonix and Tor,
* more details about the [Features] of Whonix,
* our [Documentation] explaining in details how to use Whonix,
* some hints on why should you [Trust] or not Trust Whonix,
* our [Security Guide] and [Design] document about Whonix specification, threat model and implementation.

= Acknowledgements, Credits, Related projects, Authorship =

See [Authorship].

= License =

<pre>Whonix About wiki page Copyright (C) Amnesia &lt;amnesia at boum dot org&gt;
Whonix About wiki page Portions Copyright (C) 2012 adrelanos &lt;adrelanos at riseup dot net&gt;

This program comes with ABSOLUTELY NO WARRANTY; for details see the wiki source code.
This is free software, and you are welcome to redistribute it
under certain conditions; see the wiki source code for details.</pre>
Thanks to [https://anonymous-proxy-servers.net/ JonDos] ([https://anonymous-proxy-servers.net/forum/viewtopic.php?p=31220&sid=ac8a6ca16eb768b3322be30b20375c97#p31220 Permission]). The &quot;Summary of what Whonix is&quot; chapter of the Whonix About wiki page contains content from the JonDonym documentation [https://anonymous-proxy-servers.net/en/help/about.html Features] page.

= Footer =

[[include ref=WikiFooter]]

