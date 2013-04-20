[[include ref=WikiHeader]]

[TOC]

<!--
Copyright:

   Whonix Chat wiki page Copyright (C) Amnesia <amnesia at boum dot org>
   Whonix Chat wiki page Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
   
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
This Chat page is a fork of the Tails Pidgin page, from this exact source <http://git.immerda.ch/?p=amnesia.git;a=blob;f=wiki/src/doc/anonymous_internet/pidgin.mdwn;hb=96c45f5ed786f3d24c51e1a2ef8ecedf5f2644d8>.
-->

# General Safety Advice #
Recommend knowledge: [Modes of Anonymity](https://sourceforge.net/p/whonix/wiki/DoNot/#do-not-mix-modes-of-anonymity).

Most of instant messenger protocols are unsafe from a privacy point of view. This is not a Whonix specific problem. It is a general problem with instant messengers.

Pidgin (see chapter below) supports most protocols.

[Tor Exit Node eavesdropping](https://sourceforge.net/p/whonix/wiki/Warning/#tor-exit-nodes-can-eavesdrop-on-communications) can happen if no encryption to the server is enabled. Some protocols have encryption disabled by default, some do not support encryption at all. See also [Overview about Pidgin protocols and their encryption features](https://tails.boum.org/todo/Pidgin_Protocol_Review/). If encryption to the server is enabled, the Tor Exit Node can no longer eavesdrop. One problem solved, another problem remains unsolved.

The server could still gather interesting information.

* Account names
* Buddy list (list of contacts)
* Log login dates and times
* Timestamp of messages
* Who communicates with whom
    * If the recipient knows the sender and the recipient uses a non-anonymous account or was ever logged in without Tor, this can be used as a hint who the sender is.
* Content of messages - Can be prevented using end-to-end encryption. This is covered in the OTR encryption chapter below.

A server-based protocol designed with openness, security and privacy in mind is Jabber.

Systems which do not require a server by design, i.e. serverless instant messengers are better from privacy point of view. Such systems are TorChat (below) and RetroShare (below).

For IRC inside Whonix-Workstation, the [Ident Protocol](https://en.wikipedia.org/wiki/Ident) is automatically blocked because Whonix-Workstation is firewalled.

The [TorifyHOWTO/IrcSilc](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO/IrcSilc) contains general IRC safety techniques and other tips.

# TorChat #
## General ##
Whonix developer adrelanos is very curious about [TorChat](https://github.com/prof7bit/TorChat). The concept of having a serverless and fully encrypted instant messenger based on Tor hidden services is marvelous.

Unfortunately, adrelanos can't recommend TorChat for Whonix. This is because the TorChat developer does currently not respond to other people, see [TorChat issues](https://github.com/prof7bit/TorChat/issues). Adrelanos believes communication and support is crucial for anonymity related projects.

TorChat ships it's own copy of Tor, sets up a hidden service and the messenger on the host. Whonix runs Tor and applications on different machines. Tor on Whonix-Gateway and applications on Whonix-Workstation. There is not yet a way to run [TorChat with a pre-configured hidden service](https://github.com/prof7bit/TorChat/issues/24).

## HowTo ##
### Installation ###
Requires Whonix 0.5.5 or above.

**EXPERIMENTAL** Experimental as in it is difficult to install. Only use it in case you trust TorChat. There shouldn't be any anonymity leaks and it should be as safe as other hidden services in general and in Whonix.

Learn about [Hidden Services](https://sourceforge.net/p/whonix/wiki/Hidden%20Services/) in Whonix first and learn how to set up the hidden webserver. This will ease following this guide.

On Whonix-Gateway.

Open torrc.

    sudo nano /etc/tor/torrc

Search for

    #HiddenServiceDir /var/lib/tor/torchat_service/
    #HiddenServicePort 11009 192.168.0.11:11009

and comment in by removing the # in front of it.

    HiddenServiceDir /var/lib/tor/torchat_service/
    HiddenServicePort 11009 192.168.0.11:11009

Save.

Reload Tor.

    sudo service tor reload

Get your onion address.

    ## You need root to do that
    sudo su

    ## Find out your .onion hostname.
    nano /var/lib/tor/torchat_service/hostname

Backup your key, if you want to ever restore it one another machine, a newer Whonix-Workstation or after hdd failure. If you don't care to get a new TorChat ID, you can skip this step.

    /var/lib/tor/torchat_service/private_key

On Whonix-Workstation.

    sudo apt-get install torchat

Open the torchat.ini which is in the hidden folder /home/user/.torchat/torchat.ini.

Look for the following line.

    own_hostname = <your onion hostname without the .onion ending>

Replace it with your onion hostname. For example if your onion hostname is *idnxcnkne4qt76tg.onion* replace it enter *idnxcnkne4qt76tg*, so it looks like.

    own_hostname = idnxcnkne4qt76tg

Save.

### Starting ###
**NOTE** It can take a while until a Tor hidden service becomes reachable for the first time. Wait at least a few minutes before you believe it doesn't work.

Start menu -> Applications -> Internet -> TorChat Instant Messenger

### Uninstall ###
If you want to remove it. On Whonix-Workstation.

    sudo apt-get remove torchat

And undo the changes in in /etc/tor/torrc on Whonix-Gateway.

    nano /etc/tor/torrc

Reload Tor.

    sudo service tor reload

### Debugging ###
In case it won't work for you.

Test if Tor is reachable on 192.168.0.10:9119.

    /usr/bin/wget 192.168.0.10:9119

If it says.

    --2013-02-13 13:49:47--  http://192.168.0.10:9119/
    Connecting to 192.168.0.10:9119... connected.
    HTTP request sent, awaiting response... 501 Tor is not an HTTP Proxy
    2013-02-13 13:49:47 ERROR 501: Tor is not an HTTP Proxy.

It means, it's fine and the port is reachable.

Run torchat in a Terminal.

    torchat

The following output is an example, how it looks when everything is fine.

    ~ $ torchat
    (0) [config,470,main] python version 2.7.3 (default, Jan  2 2013, 16:53:07) [GCC 4.7.2]
    (0) [config,477,main] script directory is /usr/share/torchat
    (0) [config,478,main] data directory is /home/user/.torchat
    ./tor.sh: 6: ./tor.sh: tor: not found
    (0) [tc_client,2083,startPortableTor] very strange: portable tor started but hostname could not be read
    (0) [tc_client,2084,startPortableTor] will use section [tor] and not [tor_portable]

If you are using [Multiple Whonix-Workstations](https://sourceforge.net/p/whonix/wiki/Multiple%20Whonix-Workstations/), where the Workstation has another IP than *192.168.0.11* you must edit the following line in torchat.ini.

    listen_interface = 192.168.0.11

Did the hidden webserver example from the [Hidden Services] page work for you? Try that first.

You also could try using the TorChat source package, which is still documented on the [Deprecated] page.

### Technical Design ###
<font size="-3">
The [DummyTor] package prevents Tor over Tor.
</font>

### Credits ###
Thanks to scarp for helping with the TorChat instructions!

# RetroShare #
In fact [RetroShare](http://retroshare.sourceforge.net) is not an [anonymizing network](https://en.wikipedia.org/wiki/Anonymizer), it is a [friend-to-friend](https://en.wikipedia.org/wiki/Friend-to-friend) (F2F) network, or optionally a [darknet](https://en.wikipedia.org/wiki/Darknet_(file_sharing)). RetroShare has a very different audience and threat model.

RetroShare is serverless, messages are encrypted end-to-end and actively developed. That is what makes this messenger interesting.

Although google search results and many people may claim otherwise, it is possible to run RetroShare through Tor, due to transparent proxying. **Still experimental. Feel free to experiment and please share your results. Can two people, using RetroShare inside Whonix-Workstation, who only added each other, connect to each other?**

Running RetroShare through Tor enables you, to do things, which are normally potentially dangerous, such as adding random people (from a forum), while staying anonymous. (For example, to join a RetroShare forum.) This is **not** a recommendation, just stating a possibility.

After adding tons of random "friends" from a public forum, I could connect to a very few people over TCP. ^1^ Approximately only 5% were online. Although I can probable see only a very small portion of the network, the content of the network looks pretty interesting.

RetroShare reports Right click -> DHT Details: 
NET WARNING No DHT; Behind NAT UNKNOWN NAT STATE MANUAL FORWARD

<font size="-3">
,,
^1^ Chance of working better (**untested**):
[Tunneling UDP over Tor](https://sourceforge.net/p/whonix/wiki/TunnelUDPoverTor/). ^2^
^2^ Note, that [Other Anonymizing Networks over Tor UDP Tunnel](https://sourceforge.net/p/whonix/wiki/Applications/#other-anonymizing-networks-over-tor-udp-tunnel) applies.
</font>

# Pidgin #
For instant messaging Whonix you can install the [Pidgin Instant Messenger](http://pidgin.im/). It is a multi-protocol client, so you could run MSN, ICQ, IRC, AIM, Jabber and many other protocols at the same time, even with several instances of the same protocol.

For more detailed documentation refer to the [official Pidgin user guide](http://developer.pidgin.im/wiki/Using%20Pidgin).

You can install it using Start menu -> Applications -> System -> Terminal.

    sudo apt-get update
    sudo apt-get install pidgin

# OTR encryption #
Of course the issue of end-to-end encryption arises again. As we mentioned earlier, we have [Off-the-record messaging](http://www.cypherpunks.ca/otr) (commonly called OTR) for instant messaging, and Pidgin and many other instant messengers have support for that. There are several resources on how it works and how to use it on their web site. Basically all you need to do is choose "Start private conversation" in the OTR menu and a key will be generated automatically if you do not have one already. After that OTR will establish a private conversation if the other end's instant messenger supports it.

OTR and other Pidgin plugins are enabled in the "Tools menu -&gt; Plug-ins" section. Simply check the appropriate box for enabling any plugin you want, and possibly you might also want to configure it by pressing the "Configure Plug-in" button. When this is done for the OTR plugin a window that can be used to manage your keys will open. The use of OTR is recommended as many instant messaging protocols normally sends your messages in plaintext. Force your friends to migrate to clients with support for OTR!

**NOTE**: `/me` is **not** encrypted when used in a OTR private conversation!

Read also those [various other ressources about OTR](http://www.cypherpunks.ca/otr/index.php#docs).

You can install it using Start menu -> Applications -> System -> Terminal.

    sudo apt-get update
    sudo apt-get install pidgin-otr

# IRC Client XChat #
See [XChat].

# License #
    Whonix Chat wiki page Copyright (C) Amnesia <amnesia at boum dot org>
    Whonix Chat wiki page Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
    
    This program comes with ABSOLUTELY NO WARRANTY; for details see the wiki source code.
    This is free software, and you are welcome to redistribute it
    under certain conditions; see the wiki source code for details.

# Footer #
[[include ref=WikiFooter]]