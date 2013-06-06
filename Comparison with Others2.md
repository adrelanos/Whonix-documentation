[[include ref=WikiHeader]]

[TOC]

# Comparison of Whonix, Tails, Tor Browser Bundle and Qubes OS TorVM
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
^3^ Medium: Tails has a firewall to block non-Tor traffic, but an [audit](https://tails.boum.org/todo/applications_audit/) at protocol level is still required. Quoted from the [Tails Security Page](https://tails.boum.org/security/index.en.html): *"Until an [audit](https://tails.boum.org/todo/applications_audit/) of the bundled network applications is done, information leakages at the protocol level should be considered as ? at the very least ? possible."*
^4^ Hard: It's left to the user to prevent non-Tor traffic, DNS leaks and protocol level leaks.
^5^ Text, screenshot or video instructions [available](https://sourceforge.net/p/whonix/wiki/Download/#install-whonix).
^6^ This and the whole documentation will be improved in next Whonix version.
^7^ Examples what not to do: [DoNot](https://sourceforge.net/p/whonix/wiki/DoNot/).
</font>

## Features
**Comparing Whonix 0.4.5 with Tails 0.16.**

| | Whonix | Tails | Tor Browser Bundle | Qubes OS TorVM
------------- |  ------------- | ------------- | ------------- | -------------
Default Desktop | KDE | GNOME | ? | ?
Multi language support | No | Yes | Yes | ?
Fits on a DVD. | No | Yes | ? | ?
VPN support | Can be manually installed. ^1^ | No ^2^ | ? | ?
IRC client pre-configured for privacy | Yes (XChat) | Yes (Pidgin) | Not an operating system. | No
Flash Support | Can be manually installed. ^3^ | No ^4^
Mixmaster over Tor | Yes ^5^ | No | Not an operating system. | No.
TorChat | Can be manually installed. ^6^ | Not supported. ^7^ | Not applicable. | ?
FTP Support | Partial ^8^ | No? ^9^ | Not an operating system. | ?
Download Manager | Can be manually installed. ^10^ | Can be manually installed. ^11^ | ? | ?
Webmail can be uses in browser | Yes | Yes | Yes | Yes
E-Mail Client | Can be manually installed. ^14^ | ? ^15^ | ? | ?
Hidden service support | Can be manually installed. ^16^ | Can be manually installed. ^17^ | ? | ?
Hidden Server configuration GUI | No | No ^13^ | ? | ?
Support for free wifi hotspots | ^18^ | Yes ^19^ | Yes ^20^ | ?
Works on 32 bit PCs | Yes | Yes | Yes | ?
Works on 64 bit PCs | Yes | Yes | Yes | Yes
32 bit builds | Yes | Yes | Yes | ?
64 bit builds | No ^21^ | No | Yes | ?
64 bit builds can be created from source code | Yes ^22^ | ? | ? | ?
Host Kernel | When using VMs, can be any supporting Virtual Box.; When using Physical Isolation: Not applicable. |  When using VMs, can be any supporting Virtualizer.; When not using VMs: Not applicable. | ? | ?
i486 Kernel for compatibility | Yes | Yes | Not an operating system. Up to the user. | ?
686-pae Kernel | Yes | Yes | Not an operating system. Up to the user. | ?
64 bit Kernel | Could be manually installed. | No. | Not an operating system. Up to the user. | ?
Kernel Autodetection at Boot Time | No | Yes | Not a distribution. Not applicable. | ?
Video/Streaming Software | Can be manually installed. | Can be manually installed. | Not an operating system. | Can be manually installed.

<font size="-3">
,,
^1^ Included, although there is no nice gui, it's available as Optional Configuration, see [VPN/tunnel support](https://sourceforge.net/p/whonix/wiki/Features/#vpn-tunnel-support).
^2^ Tails Status: https://tails.boum.org/todo/vpn_support/
^3^ Done, see [Browser Plugins](https://sourceforge.net/p/whonix/wiki/BrowserPlugins/).
^4^ Tails Status: https://tails.boum.org/todo/Flash_support/
^5^ Installed by default, see [Mixmaster].
^6^ Can be manually installed, see [Chat].
^7^ Tails: Not supported. [Tails wishlist](https://tails.boum.org/todo/Torchat_installed_by_default/)
^8^ [wget ftp support broken](https://trac.torproject.org/projects/tor/ticket/1259#comment:16).; Filezilla (not pre-installed) works.
^9^ Tails Status: https://tails.boum.org/todo/fix_Internet_FTP_support/
^10^ Users can install one of their choice, preferably using SocksPort, TransPort works as well. *wget -c* (pre-configured to use SocksPort) is also working.
^11^ Users can manually install the download manager of their choice in Tails. It just needs to be configured to use the proper SOCKS proxy.
^12^ Placeholder.
^13^ [Tails server: Self-hosted services behind Tails-powered Tor hidden services](https://tails.boum.org/todo/server_edition/)
^14^ Optional configuration, see [Mozilla Thunderbird with TorBirdy](https://sourceforge.net/p/whonix/wiki/E-Mail/#mozilla-thunderbird-with-torbirdy).
^15^ Tails Status: [Return of Icedove](https://tails.boum.org/todo/Return_of_Icedove__63__/)
^16^ Hidden services can be used without IP/DNS leaks, see [Hidden Service Support](https://sourceforge.net/p/whonix/wiki/Hidden%20Services/). There is no nice graphical user interface to setup a hidden service, works well nonetheless.
^17^ Can be used using ordinary mechanisms with torrc.; Tails Status: [persistence preset - tor](https://tails.boum.org/todo/persistence_preset_-_tor/)
^18^ When using VMs: Can be easily done on the host.; When using Physical Isolation: As in Whonix 0.5.6 there is no unsafe browser. A separate third machine with clearnet access could be used.
^19^ Tails has a unsafe browser for such tasks.
^20^ Mechanism of the host operating system can be used.
^21^ TODO: Still lacks 64 bit guest builds. 64 bit builds would offer more ALSR entropy, would safe some memory ([page fusion?](https://www.virtualbox.org/manual/ch04.html#guestadd-pagefusion)) and provide more performance.
^22^ Building them from source is already supported, see [Build Configuration](http://sourceforge.net/p/whonix/wiki/Dev_SourceCodeIntro/#debugging).
</font>

# Footer #
[[include ref=WikiFooter]]