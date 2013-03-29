<!--
Copyright:

   Whonix Pre Install Advice wiki page Copyright (C) Amnesia <amnesia at boum dot org>
   Whonix Pre Install Advice wiki page Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
   
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
The Whonix Pre Install Advice wiki page is forked from the Tails Enable MAC Changer page, from this exact source <http://git.immerda.ch/?p=amnesia.git;a=blob;f=wiki/src/doc/advanced_topics/mac_changer.mdwn;hb=770c6f26f8dcd06452fef1c57dafb2878e0dee11> and on the Tails macchanger page from this exact source <http://git.immerda.ch/?p=amnesia.git;a=blob;f=wiki/src/todo/macchanger.mdwn;hb=f27853e23d7985594d54f00f30153b6acd97312e>.
-->

[[include ref=WikiHeader]]

[TOC]

# Pre Install Advice #
## General ##
I believe Whonix is with default settings safer than Tor alone.

You can make it even more secure. It depends on how much you are willing to read, see [Documentation].

## Warnings ##
Make sure you have already read the [Warning](https://sourceforge.net/p/whonix/wiki/Warning/) page.

## On your host operating system ##
### Tor Browser Bundle ###
It is recommend to always have the latest working [Tor Browser Bundle](https://www.torproject.org/projects/torbrowser.html.en) installed on your host. A great way to learn the basics about Tor.

The Tor Browser Bundle is great for testing if you live in a censored area or not, if Tor is blocked by your ISP or not. When you need (private) (obfuscated) bridges for the Tor Browser Bundle, you will need them for Whonix as well. (See [bridges](https://sourceforge.net/p/whonix/wiki/OptionalConfigurations/#using-private-obfuscated-bridges).)

If you can not get the Tor Browser Bundle to work, you will most certainly not get Whonix to work either. And if some day Tor Browser in Whonix shouldn't work anymore or updating is broken, you can still use the Tor Browser Bundle to visit the Whonix Homepage.

## Host Security ##
### Introduction ###
If the host is compromised by [Malware](https://en.wikipedia.org/wiki/Malware) so is every virtual machine with Whonix, Tor and all anonymous communication. In essence, Malware can see your desktop, everything you do, type, send, receive, etc.

Antivirus products and [personal firewalls](https://en.wikipedia.org/wiki/Personal_firewall) are **not** drop in solutions for a a secure host. Malware often stays undetected. ([Polymorphic code](https://en.wikipedia.org/wiki/Polymorphic_code) and [Rootkits](https://en.wikipedia.org/wiki/Rootkit)) pretty much render Antivirus products helpless. Personal firewalls often get circumvented.

The **only** promising approach is not to get infected by Malware in the first place. Once malicious code is on a system, it's next to impossible to contain. Not saying Antivirus scanning and firewalls are useless. They are not. Refer to them as your very last line of defense. If you ever find malware on your system, which is not a false positive, it only demonstrates, that your precautions didn't work. It are the precautions that matter (hardening, secure host operating system, using signed software, etc.), not the detection.

### Recommendation to use a dedicated host operating system ###
You are advised to use a dedicated host operating system just for hosting the Whonix Virtual Machines. Should your regular every day operating system be already compromised, then Whonix could not provide any additional protections. It's best to have one dedicated host operating system, which is only used to host Whonix.

### Recommendation to use Whonix on External Media ###
No one stops you from installing the host operating systems(s) required for Whonix on external disks such as USB, FireWire, eSATA, etc. You can improve security by installing Whonix's host operating system(s) on a dedicated disk(s). That reduces the risk that any other operating system(s) of yours infecting Whonix's host operating system. You can remove and hide the Whonix disk(s) while you're not using them.

You can use any guide on the web explaining how to install Linux on USB. There are no Whonix specific differences other than, after you finished that, you install Virtual Box and Whonix.

### Recommendation to use a dedicated host ###
If you want to go even one step further on the security ladder, you are advised to use a dedicated computer just for hosting Whonix. A machine which you only use for using Whonix. Dedicated within the meaning of using a second/extra host operating system(s), which you never use(ed) for anything else.

### Windows Hosts
You are must better off using alternative host operating systems, such as GNU/Linux. If you are using Windows...

Was Windows installed from legitimate media? Not some pirated iso found on the net that could include malware. 

You shouldn't have any pirated software, this usually involves running unverified, possibly malicious binary cracks or key generators.

Stick to renowned Open Source software, such as Firefox, Gimp, 7-zip, Libre Office, etc., which is more unlikely to contain malicious code. You should only download over https (SSL) and even better check the gpg signatures.

### GNU/Linux Hosts
Using GNU/Linux on the host and only using in-repository software is automatically gpg signed and installed from the distributor's repositories by the package manager. This is much safer than downloading stuff from the web like you have to do as a Windows user.

### Which host operating system do you recommend?
Briefly:
Debian GNU/Linux is a reasonable compromise of security and usability (popularity, documentation). For extra security tips for download, verification and installation see [Debian Tips](https://sourceforge.net/p/whonix/wiki/Debian/).

Longer:
There are of course other options. See [Why don't you use <your favorite most secure operating system\> for Whonix?](https://sourceforge.net/p/whonix/wiki/OperatingSystem/#why-dont-you-use-your-favorite-most-secure-operating-system62-for-whonix).

### LAN/Router Security ###
In case Whonix-Gateway would be ever compromised, you should know that it can theoretically access any computer in your local network. Therefore, if you're the admin of your home network, it's recommend to lock down the webinterface of your home router, i.e. installing the latest firmware with latest security patches and using a secure password.

## Whonix information ##
### MAC Address ###
#### Status of MAC Address chapter ####
This is nowhere well solved. Neither in Whonix, Tails, Liberte Linux or the Tor Browser Bundle. It's still an open research problem. This chapter will give you all existing information.

#### Introduction ####
First of all, you should know that all network cards, both wired and wireless, have a unique identifier stored in them called their MAC address.

This address is actually used to address your computer on the local network, but it will never get out on the Internet so people can not use it to trace you.

However, other computers on the network could log it, which then would provide proof that your computer have been connected to it. But if you are using an untrusted, public network, you should consider it.

#### Using your home connection ####
Changing your MAC address is not required.

#### Using a public computer (e.g. in a library, Internet-cafe) ####
The MAC address should not be changed, as it may bring undesired admin attention and/or simply forbid access to the Internet.

#### Using a personal computer (e.g. a laptop, wherever it happens) in a public network ####
The MAC address should be changed.

Rather the admin may or may not find out, that you are using Tor. That depends on your your configuration, i.e. perhaps you are using obfsproxy or you tunnel your traffic SSH/VPN and on the adversaries skills.

The MAC address and being a Tor user, might depending on your personal threat model, be a risk visiting that public network (again).

If you are going to use the same public network again, you have to decide, depending on your threat model, if you are going to use the very same MAC address or if you are going to create a new MAC address. In case you suspect, the admin has seen you and logged the MAC, you shouldn't change the MAC, since this were suspicious. If you believe that public network is so public, that no one has seen you, you might decide to use a new MAC address (popular vendor id, random/unique second part) each time you step by.

#### Random MAC address ####
Using a random MAC address is not recommend. While this might sufficiently confuse some adversaries, it won't defeat skilled adversaries. If you are using a random MAC address, it might happen that the vendor id part of the MAC address is non-existent. Even if it were existent, you might up with a vendor id, which has either never been used or never been used in decades. If you are going to spoof your MAC, you have to use a popular vendor id.

The initial second part of the MAC address may be random/unique.

Unfortunately, we can't yet provide detailed instructions on how to create such appropriate MAC addresses. Research is still ongoing.

The reason why MAC changing is not always enabled is that is might cause problems on some networks.

#### Auto-connect issue ####
Apart from the difficulty creating such an appropriate MAC address, there are also technical hurdles. All the care creating the MAC does not help, if you boot your computer and it instantly connects to the public network and spills your MAC address. For Virtual Machine users: your host operating system most likely automatically connects (updates, perhaps time sync). For Physical Isolation users: Whonix-Gateway automatically connects to Tor after start.

Also if you plug in a wifi stick, it might happen, they automatically try to connect and spill your MAC.

#### Changing MAC address ####
***TODO***: test and expand, please help!

<u>(1)</u>

**Standard-Download-Version users**

Edit */etc/network/interfaces* on the host.

**[PhysicalIsolation] users**

Edit */etc/network/interfaces* on Whonix-Gateway

<u>(2)</u>

Below "*iface eth0 inet dhcp*" Add

    hwaddress ether 00:00....

<u>(3)</u>

To automatically randomize the MAC address on boot (if you want this?) add

    pre-up macchanger -e eth0

instead.

<u>(4)</u>

To prevent automatically bringing up new network interfaces I think all that's needed is to uncomment

    auto eth0

Then manually bring up with

    sudo ifup eth0

#### Sources ####
<font size="-3">Source of information: [Tails 1](https://tails.boum.org/contribute/design/MAC_address/); [Tails 2](https://tails.boum.org/todo/macchanger/). Both worth reading! Thanks to Tails!</font>

## Known bugs ##
Check [Download](https://sourceforge.net/p/whonix/wiki/Download/) page for a list of known bugs.

## Most Security ##
If you want to learn everything Whonix considers, you should, before installing Whonxi, read all Whonix [Documentation] pages, and depending on security needs, also the [Design].

# License #
    Whonix Pre Install Advice wiki page Copyright (C) Amnesia <amnesia at boum dot org>
    Whonix Pre Install Advice wiki page Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
    
    This program comes with ABSOLUTELY NO WARRANTY; for details see the wiki source code.
    This is free software, and you are welcome to redistribute it
    under certain conditions; see the wiki source code for details.

# Footer #
[[include ref=WikiFooter]]