[[include ref=WikiHeader]]

[TOC]

# Hide the fact, that you are using Tor/Whonix #
## Introduction ##
Whonix users are most likely Tor power users. They are more paranoid then normal Tor users. And adversaries might ask themselves why. Whonix users most likely [host hidden services](https://sourceforge.net/p/whonix/wiki/Hidden%20Services/) or do other fancy stuff over Tor.

Depending on how restricted your area is and how paranoid you are, you may want to hide the fact from your provider, that you are a Whonix and/or Tor user.

Hiding the fact, that you are using Whonix is relatively easy, because Whonix is itself exclusively generating Tor activity on the network. To find out how easy/difficult it is for an ISP to detect Whonix, see footnote ^4^.

Hiding the fact, that you are a Tor user is not so easy. If you download Whonix over Tor, the fact you are using Whonix will be hidden. This is because all traffic from Whonix-Workstation and Whonix-Gateway is routed over Tor. ^1^ ^3^

Hiding the fact you, that you are a Tor user is very tricky to archive. Be very careful. Here are some tips. This isn't a step by step tutorial. It's recommend to read the whole chapter.

Use either private and obfuscated bridges or a VPN/SSH proxy. On one hand, best chance to hide Tor might be to combine both ways, on the other hand, people who want to hide the fact, that they are using Tor, may also have the same desire to hide the fact, that they are using VPN or SSH.

Using private and obfuscated bridges alone doesn't provide strong guarantees of hiding your the fact you are using Tor from your ISP. [Quote](https://mailman.boum.org/pipermail/tails-dev/2013-April/002950.html) ([w](http://www.webcitation.org/6G67ltL45)) Jacob Appelbaum:

> Some pluggable transports may seek to obfuscate traffic or to morph it. However, they do not claim to hide that you are using Tor *in all cases* but rather in very specific cases. An example threat model includes a DPI device with limited time to make a classification choice - so the hiding is very specific to functionality and generally does not take into account endless data retention with retroactive policing.

Using a VPN or SSH neither doesn't provide strong guarantees of hiding your the fact you are using Tor from your ISP. VPN's and SSH's are vulnerable to an attack called Website traffic fingerprinting. See [VPN/SSH Fingerprinting](https://trac.torproject.org/projects/tor/wiki/doc/TorPlusVPN#VPNSSHFingerprinting) ([w](http://www.webcitation.org/6Gmywywoj)) for explanation.

<font size="-3">
,,
^1^ To preserve anonymity of activities the user is doing inside Whonix-Worktation, it would not be required to torify Whonix-Gateway's own traffic. ^2^
^2^ apt-get operating system updates, network time synchronization.
^3^ Since Whonix 0.2.1 also the Whonix-Gateway traffic is routed over Tor. This prevents telling the world, that the user is a Whonix user.
^4^ See [Fingerprint] page for details.
</font>

## Warnings ##
* Think about, if your ISP knowing, you're a VPN or SSH user is acceptable to you.
* Download Tor through a trusted internet service provider (in your (home) country) or through SSH or VPN (or before entering a hostile environment).
* Setup the SSH/VPN tunnel or the private obfuscated bridges first. (Depending on what you want to use, read below.)
* If you are extra paranoid, you should also download Virtual Box over Tor.
* First, think about, how do you obtain the Tor Browser Bundle and obfuscated bridges and/or VPN and/or SSH, without your ISP noticing it? It's a chicken egg problem. You most likely have to get it from a trusted source. This isn't a problem, which Whonix could solve, it's a Tor upstream question.
* Another issue for hiding your Whonix usage is installing and/or downloading Whonix.
* Download.
    * If you download Whonix form sf.net that download will go unencrypted and your internet service provider (or SSH/VPN provider) will learn, that you downloaded Whonix.
        * A workaround could be, to download Whonix by using the official torproject.org Tor Browser Bundle.
        * You have to turn off your network connection while starting Whonix for the first time, otherwise it will automatically connect to the Tor public network. **TODO: [First time connection wizard](https://sourceforge.net/p/whonix/awiki/Dev/#security-first-time-connection-wizard).** Then set up everything to hide your Tor/Whonix usage, either by using a SSH or VPN or private obfuscated bridge, which is also covered on this page.
* Building from Source.
    * You can learn everything about building Whonix, using the Tor Browser Bundle.
    * If you are building Whonix from source, the build scripts, will download a specific set of software packages with of apt-get, Tor Browser with curl, update-command-not-found, and your internet service provider could notice, that you are building Whonix from source.
    * If you understand the build scripts, you can also manually build Whonix, by applying the commands and configuration files manually.
    * See also [Build Anonymity](https://sourceforge.net/p/whonix/wiki/Build%20Anonymity/).

## Using a Proxy ##
Impossible! (The connection between you and your proxy is unencrypted. That goes for all proxies, http, https, socks4, socks4a, socks5.) Your ISP could still see, that you are connecting to the Tor network. This is only mentioned because that myth is constantly suggested and asked when this topic comes up.

## Using SSH or VPN ##
See warnings above first. By default all traffic of Whonix-Gateway is routed through Tor! You need to route all that traffc through SSH/VPN.

Tunnel all Tor related traffic first through a VPN or SSH. See [Tunnel Tor through proxy or VPN or SSH](https://sourceforge.net/p/whonix/wiki/Tunnel_Tor_through_proxy_or_VPN_or_SSH/) (ignore the proxy related stuff). This will hide the fact that you use Tor from your ISP. If the server is outside a national firewall this is also a way to circumvent Tor censorship.

If you do not trust any SSH or VPN providers, then anonymously host your own in a safe place.

## Using private and obfuscated bridges ##
See warnings above first. Set up Tor to use [private and obfuscated bridges](https://sourceforge.net/p/whonix/wiki/Bridges/). This makes it harder for ISPs and national firewalls to detect and block Tor but it does not prevent a dedicated adversary to find out that you are using Tor (research is ongoing, see obfsproxy).

# Footer #
[[include ref=WikiFooter]]