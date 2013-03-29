<!--
Copyright:

   Whonix Anonymity wiki page Copyright (C) Amnesia <amnesia at boum dot org>
   Whonix Anonymity wiki page Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
   
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
The Whonix Fingerprint wiki page is forked from the Tails Fingerprint page, from this exact source <http://git.immerda.ch/?p=amnesia.git;a=blob;f=wiki/src/doc/about/fingerprint.mdwn;h=24d279245503ec0014b941c82266b6127fe0a1dc;hb=b10ce9f3622437faa7fe2b0b52c83a4fe018fc4a>.
-->

[[include ref=WikiHeader]]

[TOC]

# Fingerprint #
In this context we use the term *fingerprint* to refer to the specificities in the way Whonix behaves on Internet. Those specificities could be used to determine whether a particular user is using Whonix or not.

As explained on our [Warning] page, when using Whonix it is possible to know that you are using Tor. But Whonix tries to make it as difficult as possible to distinguish Whonix users from other Tor users, especially Tor Browser Bundle (TBB) users. If it is possible to determine whether your are a Whonix user or a TBB user, this provides more information about you and in consequence reduces your anonymity.

This section explains some issues regarding the fingerprint of Whonix and how this could be used to identify you as a Whonix user.

For the websites that you are visiting
======================================

The websites that you are visiting can retrieve a lot of information about your browser. That information can include its name and version, window size, list of available extensions, timezone, available fonts, etc.

To make it difficult to distinguish Whonix users from TBB users, Whonix includes TBB and therefore should provide the same information as the TBB in order to have similar fingerprints.

For your ISP or local network administrator
===========================================

This is difficult (impossible?) to say with 100% certainty, since part of this is still a general Tor (not Whonix!) research question. It's also impossible to prove a negative.

Whonix is itself exclusively generating Tor activity on the network. Both, all traffic from Whonix-Workstation (TBB, updates, timesync, etc.) and Whonix-Gateway (updates, timesync) goes through Tor. Getting online activity is the task of the host, so the host ^2^ is most likely using DHCP to obtain a local IP address. Usually TBB users also have network activity outside of Tor, either from another web browser or other applications. So the proportion or amount of Tor activity could be used to determine whether a user is using Whonix or the TBB. If you are sharing your Internet connection with other users that are not using Whonix or if you also use a browser on the host ^1^, it is probably harder for your ISP to determine whether a single user is generating only Tor traffic and so maybe using Whonix.

Whonix uses the entry guards mechanism of Tor. with the [entry guard mechanism](https://www.torproject.org/docs/faq#EntryGuards), a Tor user always uses the same few relays as first hops, which is a security feature. [Whonix uses an unmodified version of Tor](https://sourceforge.net/p/whonix/wiki/FAQ/#does-whonix-modify-tor), but a [configured torrc](https://github.com/adrelanos/Whonix/blob/master/whonix_gateway/etc/tor/torrc) for the [Stream Isolation] security feature.

When starting, Whonix synchronizes the system clock to make sure it differs from the host clock and is not too much off ([TimeSync]). [whonixcheck] issues some network traffic to check for updates and news, all goes through different circuits, which might be specific to Whonix. (Unchecked theory, it is unknown if an ISP can guess "oh, this Tor user opens many different Tor circuits. On the other hand, Tor seems to open only X entry guards and keep them for a while, thus not opening as many entry guards as streams.)

There is also the general Tor research question "Website traffic fingerprinting" ^3^. (Not a Whonix specific issue!) No one ever researched yet, if that also applies to other traffic (apt-get).

In conclusion, if your ISP or local network administrator can determine someone is using the official Tor Browser Bundle from The Tor Project, Whonix, a custom transparent Tor proxy or similar project, depends on how well Tor actually works. Since Whonix is itself exclusively generating Tor activity on the network and relies on Tor to obfuscate that traffic, it really depends on Tor and these are open research questions.

^1^ Which would come with the risk of the user confusing one browser for another.
^2^ In case of Default/Download version, it's the host's task to get online. In case of [PhysicalIsolation] it's the Gateway's task to get online.
^3^ See [Tor Browser Design](https://www.torproject.org/projects/torbrowser/design/) for Website traffic fingerprinting.

For your Entry Guard or Bridge
==============================
**TODO**: To be written.

Comparison
==========
[Comparison with Others](https://sourceforge.net/p/whonix/wiki/Comparison%20with%20Others/)

# License #
    Whonix Fingerprint wiki page Copyright (C) Amnesia <amnesia at boum dot org>
    Whonix Fingerprint wiki page Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
    
    This program comes with ABSOLUTELY NO WARRANTY; for details see the wiki source code.
    This is free software, and you are welcome to redistribute it
    under certain conditions; see the wiki source code for details.

# Footer #
[[include ref=WikiFooter]]