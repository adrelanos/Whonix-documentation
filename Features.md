[[include ref=WikiHeader]]

[TOC]

# Whonix Features #
Whonix is an Anonymous Operating System. It hides your IP/location and uses Tor to anonymize your data traffic. This means that neither the contacted server, nor any eavesdropper on your connections, nor the operators of the Tor network themselves can realize which webservice you use.

Basically all programs can used together with Whonix.

* For web browsing, Tor Browser is included.
* Messengers, like Pidgin, with the Jabber protocol and the OTR plugin.
* Privacy friendly e-mail client: Mozilla Thunderbird with TorBirdy
* scp for secure data transfer from and to a server.
* Unobserved administration of servers via SSH
* Web servers: Apache, ngnix, IRC servers, etc. via Hidden Services
* Other programs...

It is possible, with the help of Whonix, to use applications via Tor, which are not capable of proxy support by themselves.

Everything is explained in [Documentation].

# Feature List #
    Adobe Flash anonymously
    Browse The Web Anonymously
    Anonymous IRC
    Anonymous Publishing
    Anonymous E-Mail with Mozilla Thunderbird and TorBirdy
    Add a proxy behind Tor (Tor -> proxy)
    Based on Debian GNU/Linux.
    Based on the Tor anonymity network.
    Based on Virtual Box.
    Can torify almost any application.
    Can torify any operating system
    Can torify Windows.
    Chat anonymously.
    Circumvent Censorship.
    DNSSEC over Tor ¹
    Encrypted DNS ¹
    Encrypted Communication
    Full IP/DNS protocol leak protection.
    Hide the fact that you are using Tor ¹
    Hide the fact you are using Whonix
    Hide installed software from ISP
    Isolating Proxy
    Java anonymously
    Javascript anonymously
    Location/IP hidden servers
    Mixmaster over Tor
    Prevents anyone from learning your IP.
    Prevents anyone from learning your physical location.
    Private obfuscated bridges supported.
    Protects your privacy.
    Protocol-Leak-Protection and Fingerprinting-Protection
    Secure And Distributed Time Synchronization Mechanism
    Security by Isolation
    Send Anonymous E-mails without registration
    Stream isolation to prevent identity correlation through circuit sharing
    Virtual Machine Images
    VPN/Tunnel Support
    Whonix is produced independently from the Tor (r) anonymity software and carries no guarantee from The Tor Project about quality, suitability or anything else.
    Transparent Proxy
    Tunnel Freenet through Tor
    Tunnel i2p through Tor
    Tunnel JonDonym through Tor
    Tunnel Proxy through Tor
    Tunnel Retroshare through Tor
    Tunnel SSH through Tor
    Tunnel UDP over Tor ¹
    Tunnel VPN through Tor
    Tor enforcement
    TorChat ¹
    Free Software, Libre Software, Open Source
    ¹ via Optional Configuration

# Advantages of Whonix #
* All applications, including those, which do not support proxy settings, will automatically be routed through Tor.^1^ ^2^ ^3^ ^4^
* Installation of any software package possible.^12^
* Safe hosting of [Hidden services](https://sourceforge.net/p/whonix/wiki/Hidden%20Services/) possible. ^13^
* Protection against side channel attacks, no IP or DNS leaks possible. ^16^
* Advantage over Live CD's: Tor's data directory is still available after reboot, due to persistent storage. Tor requires persistent storage to save it's [Entry Guards](https://www.torproject.org/docs/faq.html.en#EntryGuards).
* Java / JavaScript^15^ / flash / [Browser Plugins](https://sourceforge.net/p/whonix/wiki/BrowserPlugins/)^9^ / misconfigured applications cannot leak your real external IP. See [Whonix security in real world](https://sourceforge.net/p/whonix/wiki/Security%20in%20Real%20World/).
* Protection against IP/location discovery through root exploits ([Malware](https://en.wikipedia.org/wiki/Malware) with root rights) inside Whonix-Workstation. But you really should not test it, read footnote ^a^ and follow links mentioned in footnote ^a^.
* Uses only [Free Software](https://en.wikipedia.org/wiki/Free_software).
* Building Whonix from source is easy, see [BuildDocumentation].
* [Tor](https://www.torproject.org)+[Vidalia](https://www.torproject.org/projects/vidalia.html.en)^10^ and [Tor Browser](https://www.torproject.org/projects/torbrowser.html.en) are not running inside the same machine. That means that for example an exploit in the browser can't affect the integrity of the Tor process.
* It is possible to use Whonix in conjunction with VPNs, ssh and other proxies. But see [Tor plus VPN/proxies Warning](https://trac.torproject.org/projects/tor/wiki/doc/TorPlusVPN). Everything possible, as first chain or last chain, or both.
* Loads of [Features].
* Loads of [Optional Configurations](http://sourceforge.net/p/whonix/wiki/OptionalConfigurations/) (additional features / Add-Ons) available.
* Best possible [Protocol-Leak-Protection and Fingerprinting-Protection](https://sourceforge.net/p/whonix/wiki/Whonix%27s%20Protocol-Leak-Protection%20and%20Fingerprinting-Protection/).
* Private obfuscated [Bridges] can be added to */etc/tor/torrc*.
* Whonix-Gateway can also torify Windows, see [OtherOperatingSystems].

# Disadvantages of Whonix #
* More difficult to set up compared to the regular Tor Browser Bundle.
* Needs virtual machines or spare hardware.
* Updating OS and applications behind the Tor proxy is slow.
* Higher maintenance required.^14^
* Tor Button's New Identity button is not supported with Whonix, see [Tor Browser](https://sourceforge.net/p/whonix/wiki/TorBrowser/#new-identity-button) for a workaround.

# Footnotes #
<font size="-3">
,, 
^a^ In case Whonix-Workstation gets rooted, the adversary can not find out the users real IP/location. This is because Whonix-Workstation can only connect through the Whonix-Gateway. How difficult is it to compromise Whonix? See [Attack on Whonix](https://sourceforge.net/p/whonix/wiki/Comparison%20with%20Others/#attacks) and [Design].  More skill is required. 
^1^ For application warnings, see [Documentation].
^2^ IPv6 is not yet supported by Tor. Limited workaround: ^6^
^3^ UDP ^5^ [is not supported by Tor](https://trac.torproject.org/projects/tor/ticket/7830), thus will not work in Whonix as well. Limited workaround: ^6^; ^7^
^4^ Services that need to listen on publicly reachable ports (open/forwarded ports) are also not supported. However you may run [Hidden services](https://sourceforge.net/p/whonix/wiki/Hidden%20Services/) which are reachable via Tor or tor2web ([be careful]([https://trac.torproject.org/projects/tor/wiki/doc/tor2web)).
^5^ ICMP, ping, VOIP calls^11^ over UDP, etc...
^6^ [OnionCat](https://sourceforge.net/p/whonix/wiki/OnionCat/)
^7^ [Tunnel UDP over Tor](https://sourceforge.net/p/whonix/wiki/TunnelUDPoverTor/) 
^8^ Placeholder.
^9^ This is still not recommended as they may decrease anonymity (e.g. flash cookies) and often have security vulnerabilities. Most popular plugins are closed source. See [Browser Plugins](https://sourceforge.net/p/whonix/wiki/BrowserPlugins/) for more information. 
^10^ [Vidalia](http://sourceforge.net/p/whonix/wiki/OptionalConfigurations/#vidalia-for-whonix) is optional; [Arm](https://sourceforge.net/p/whonix/wiki/TorController/) is installed as alternative 
^11^ Skype over TCP does work, but it's not recommend, because it's proprietary, closed source and there is no control over the encryption keys. Skype authority can compromise you out any moment. A secure encryption/authentication design looks different. For example GPG and OTR are secure, because the user has control over the keys, not the server. See [Skype FAQ entry](https://sourceforge.net/p/whonix/wiki/FAQ/#does-this-mean-that-for-example-is-my-ip-and-location-safe-when-using-skype) for details.
^12^ Must be able to run on Debian GNU/Linux or you can use [OtherOperatingSystems]. See also [Software installation on Whonix-Workstation](https://sourceforge.net/p/whonix/wiki/Install%20Software/) for details. 
^13^ Even if someone hacks your hidden server software (lighttpd, thttpd, apache, etc.), he can not steal your hidden service key. The key is stored on the Whonix-Gateway. Once you cleaned your Whonix-Workstation, no one can impersonate your hidden service anymore. 
^14^ You need to maintain three instead of one OS. You need to remember several passwords and update at least three systems. 
^15^ There is no difference compared to using JavaScript directly within the [Tor Browser Bundle](https://www.torproject.org/projects/torbrowser.html.en). Of course JavaScript within TBB inside Whonix will also not leak your IP. Browser fingerprinting still applies. For more information see [Web-browser](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO/WebBrowsers)! 
^16^ Whonix protects against IP and DNS leaks. Other possible leaks (such as username; time zone; etc.) and how to mitigate them see [Documentation]. Additionally [Whonix's Protocol-Leak-Protection and Fingerprinting-Protection](https://sourceforge.net/p/whonix/wiki/Whonix%27s%20Protocol-Leak-Protection%20and%20Fingerprinting-Protection/) mitigates many possible fingerprinting attacks by using common, non-identifying defaults. (username set to user; timezone set to UTC; etc.) 
^17^ The Workstation is the place where the browser, IRC client and so on is running. The Gateway is the place where Tor and the firewall is running.
</font>

# VPN / Tunnel support #
All kinds of tunnels is possible and tested. Route something through Tor; or route through something before connecting to Tor; or both.

* [Tunnel Support](https://sourceforge.net/p/whonix/wiki/Features/#vpn-tunnel-support)

    * [Tunnel Tor through proxy, VPN or SSH (user -> proxy/VPN/SSH -> Tor)](https://sourceforge.net/p/whonix/wiki/Tunnel_Tor_through_proxy_or_VPN_or_SSH/)
        * [Tunnel Tor through proxy (user -> proxy -> Tor)](https://sourceforge.net/p/whonix/wiki/Tunnel_Tor_through_proxy_or_VPN_or_SSH/)
        * [Tunnel Tor through SSH (user -> SSH -> Tor)](https://sourceforge.net/p/whonix/wiki/Tunnel_Tor_through_proxy_or_VPN_or_SSH/)
        * [Tunnel Tor through VPN (user -> VPN -> Tor)](https://sourceforge.net/p/whonix/wiki/Tunnel_Tor_through_proxy_or_VPN_or_SSH/)

    * [Tunnel Proxy/SSH/VPN through Tor (user -> Tor -> Proxy/SSH/VPN)](https://sourceforge.net/p/whonix/wiki/Tunnel_Proxy_or_SSH_or_VPN_through_Tor/)
        * [Tunnel proxy through Tor (user -> Tor -> proxy)](https://sourceforge.net/p/whonix/wiki/Tunnel_Proxy_or_SSH_or_VPN_through_Tor/)
        * [Tunnel SSH through Tor (user -> Tor -> SSH)](https://sourceforge.net/p/whonix/wiki/Tunnel_Proxy_or_SSH_or_VPN_through_Tor/)
        * [Tunnel VPN through Tor (user -> Tor -> VPN)](https://sourceforge.net/p/whonix/wiki/Tunnel_Proxy_or_SSH_or_VPN_through_Tor/)

    * And if you combine both methods...
        * user -> Proxy/SSH/VPN > Tor -> Proxy/SSH/VPN
        * is possible as well.

    * [Free Example VPNs working with Whonix for testing purposes](https://sourceforge.net/p/whonix/wiki/TestVPN/)

<font size="-3">
Replacing Tor with something is possible as well, although only for some combinations and networks. It's partially done but don't hold your breath for seeing those features finished, see [OtherAnonymizingNetworks](https://sourceforge.net/p/whonix/wiki/OtherAnonymizingNetworks/).
</font>

# License #
<font size="-3">Thanks to [JonDos](https://anonymous-proxy-servers.net/) ([Permission](https://anonymous-proxy-servers.net/forum/viewtopic.php?p=31220&sid=ac8a6ca16eb768b3322be30b20375c97#p31220)). The "Whonix Features" chapter of the Whonix Features wiki page contains content from the JonDonym documentation [Features](https://anonymous-proxy-servers.net/en/help/about.html) page.</font>

# Footer #
[[include ref=WikiFooter]]