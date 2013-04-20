[[include ref=WikiHeader]]

[TOC]

<!--
Copyright:

   Whonix Bridges wiki page Copyright (C) Amnesia <amnesia at boum dot org>
   Whonix Bridges wiki page Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
   
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
This wiki page is a fork of the Tails Tor Bridge Mode page, from this exact source <http://git.immerda.ch/?p=amnesia.git;a=blob;f=wiki/src/doc/first_steps/startup_options/bridge_mode.mdwn;hb=b4c1868fc9d59b6a1cb6d0e956ece5c92059c653>.
-->

What bridges are and when to use them
=====================================

When using Tor with Whonix in its default configuration, anyone who can observe the traffic of your Internet connection (for example your Internet Service Provider and perhaps your government and law enforcement agencies) can know that you are using Tor.

This may be an issue if you are in a country where the following
applies:

1. **Using Tor is blocked by censorship:** since all connections to the Internet are forced to go through Tor, this would render Whonix useless for everything except for working offline on documents, etc.

2. **Using Tor is dangerous or considered suspicious:** in this case starting Whonix in its default configuration might get you into serious trouble.

Tor bridges, also called Tor bridge relays, are alternative entry points to the Tor network that are not all listed publicly. Using a bridge makes it harder, but not impossible, for your Internet Service Provider to know that you are using Tor.

If you are in one of the situations described above you might want to use Tor bridges in Whonix. Please also read The Tor Project's [dedicated page about bridges](https://www.torproject.org/docs/bridges) to get a general idea about what bridges are.

In order to use bridges, you must know in advance the address of at least one bridge. The Tor Project distributes bridge addresses in several ways, for example from their [website](https://bridges.torproject.org/) and via email.

*Bridges are less reliable and tend to have lower performance than other entry points. If you life in a uncensored are, they are not necessarily more secure than entry guards.* <font size="-3">*Source: [bridge vs non-bridge users anonymity](https://trac.torproject.org/projects/tor/wiki/doc/TorFAQ#bridgevsnon-bridgeusersanonymity).*</font>

How to use bridges in Whonix
============================

## Using obfuscated obfs2, (private) and/or ordinary bridges

Must be manually set up. Whonix does not yet include a *bridge mode* that guides you through the process of setting up bridges before connecting to Tor.

Note that you must have at hand at least one bridge address before starting Whonix. For example, you can write it down on a piece of paper.

(Private) obfs2 bridges can currently be configured on Whonix-Gateway the same way, they would be configured when not using Whonix, i.e. just like on a server without graphical user interface. Have a look at */etc/tor/torrc*. ([on github](https://github.com/adrelanos/Whonix/blob/stable/whonix_gateway/etc/tor/torrc))

    sudo nano /etc/tor/torrc

## Using (private) obfuscated obfs3 bridges

obfs3 bridges should work in Whonix-Gateway as well, but you would have to manually add torproject.org's Debian repository and to download a newer version of obfsproxy.

## Flash Proxy bridges

Should work in Whonix-Gateway as well, but require some fiddling. See [Forum topic](https://sourceforge.net/p/whonix/discussion/general/thread/729ba238/).

If using Tor is dangerous in your country
=========================================

The Tor Project's [documentation on bridges](https://www.torproject.org/docs/bridges) mainly focuses on censorship circumvention, this means when the usage of Tor is blocked by censorship. If using Tor is dangerous or considered suspicious in your country, then there are some extra rules that you should follow in order to prevent you from being identified as a Tor user.

*Bridges are important tools that work in many cases but* **they are not an absolute protection** *against the technical progress that an adversary could do to identify Tor users.*

1. When starting Whonix for the first time, start it while the host internet connection is deactivated, which is most secure. Otherwise the Whonix-Gateway would automatically connect to the public Tor network. Alternatively, Start Virtual Box -> Right Click in Whonix-Gateway -> Settings -> Network -> Adapter 1 -> Deactivate the box *"Enable Network Adapter"*. (less secure)

2. Only use [*obfuscated bridges*](https://www.torproject.org/docs/bridges#PluggableTransports) since they are harder to identify than other bridges.

3. The less publicly known the bridges are, the better. Unfortunately, since some bridge addresses can be obtained by anyone from the Tor website or by email, it is also possible for an adversary to get the same bridge information by the same means. The Tor Project has some protection against that, but they are far from being perfect.

So the best is if you can find a trusted friend or an organization in a different country who runs a **"private" obfuscated bridge** for you. In this case "private" means that the bridge is configured with the option `PublishServerDescriptor 0`. Without this option The Tor Project can learn about the bridge and may distribute its address to others and so it could end up in the hands of your adversary.

See also [Hide the fact, that you are using Tor/Whonix](https://sourceforge.net/p/whonix/wiki/Hide%20Tor%20and%20Whonix%20from%20your%20ISP/)!

# License #
    Whonix Bridges wiki page Copyright (C) Amnesia <amnesia at boum dot org>
    Whonix Bridges wiki page Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
    
    This program comes with ABSOLUTELY NO WARRANTY; for details see the wiki source code.
    This is free software, and you are welcome to redistribute it
    under certain conditions; see the wiki source code for details.

# Footer #
[[include ref=WikiFooter]]