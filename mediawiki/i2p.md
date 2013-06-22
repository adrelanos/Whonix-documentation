[[include ref=WikiHeader]]

[TOC]

= i2p anonymizing network =

== Introduction ==

TODO: write introduction into i2p.

You can either use inproxies inside Whonix-Workstation to browse eepsites or install i2p inside Whonix-Workstation.

The inproxy method is more suited for a causal use of i2p, where you just want to anonymously view an eepsite and don't care about eavesdroppers as long you are anonymous.

Instaling i2p inside Whonix-Workstation is safer, all i2p traffic gets tunneled through Tor, fully featured but a tiny bit more difficult than installing i2p the ordinary way, i.e. using i2p in the clear, not over Tor.

* [http://www.i2p2.de/debian.html Debian I2P Packages]

== Inproxies inside Whonix-Workstation ==

There are several i2p inproxies, those are similar to [https://trac.torproject.org/projects/tor/wiki/doc/tor2web tor2web]. Simply use [https://sourceforge.net/p/whonix/wiki/TorBrowser/ Tor Browser], which comes with Whonix by default.

Note, that you will loose the end-to-end encryption to the eepsites, which i2p would provide, if you would install it directly inside Whonix-Workstation, or if you would use it the ordinary way. Depending on if the inproxy uses http (unencrypted), http'''s''' (or is reachable through a hidden service), also [https://sourceforge.net/p/whonix/wiki/Warning/#tor-exit-nodes-can-eavesdrop-on-communications Exit Nodes Eavesdropping] applies. In any case, the i2p inproxy admin can see, all your traffic into the i2p network and there is no way to prevent that.

List of i2p inproxies:

* awxcnx i2p eepsite inproxy
** [https://www.awxcnx.de/tor-i2p-proxy2-en.htm clearnet SSL version]
** [http://a5ec6f6zcxtudtch.onion/tor-i2p-proxy2-en.htm Tor hidden service version]
** [http://awxcnx.i2p/tor-i2p-proxy2-en.htm I2P eepsite version]
* awxcnx i2p IRC inproxy (See [Chat] for general chat safety advice.)
** [https://www.awxcnx.de/i2p-irc-en.htm clearnet SSL version]
** [http://a5ec6f6zcxtudtch.onion/i2p-irc-en.htm Tor hidden service version]
** [http://awxcnx.i2p/i2p-irc-en.htm I2P eepsite version]
* [http://6dyi4t72u7y6g763.onion/ 6dyi4t72u7y6g763.onion]
* or simply add '.to' after '.i2p'. For example, instant of ''http://forum.i2p'' you can use ''http://forum.i2p.to''.

== Installing i2p inside Whonix-Workstation (i2p over Tor) ==

It is possible to run i2p inside the Whonix-Workstation. Advantages:

* Anonymity is provided by Tor.
* I2p webinterface works normal inside Tor Browser. No need to install a graphical user interface on the Whonix-Gateway.
* Eepsites (.i2p) can be reached directly from Tor Browser.
* I2p's end-to-end encryption will be used like usual.

Disadvantages:

* Adds load to Tor.
* Adds load to i2p.
* It's slower than i2p directly on Whonix-Gateway or the ordinary usage.
* Incoming connections are not possible, because [https://sourceforge.net/p/whonix/wiki/Install%20Software/#whonix-workstation-is-firewalled Whonix-Workstation is firewalled]. <sup>1</sup>
* No contribution (leaching) to the i2p network. <sup>2</sup>

<font size="-3"> ,, <sup>1</sup> If you know to use a hidden service, please add this information. <sup>2</sup> Sounds worse than it is. Only very little people are expected to use i2p over Tor. I2p offers those options itself. It's not like a leeching mod. </font>

Recommend settings:

* Tor Browser
** Use a [https://sourceforge.net/p/whonix/wiki/TorBrowser/#more-than-one-tor-browser-in-whonix second instance of the Tor Browser], [https://sourceforge.net/p/whonix/wiki/Security%20Guide/#recommendation-to-use-multiple-vm-snapshots multiple VM Snapshots] or [https://sourceforge.net/p/whonix/wiki/Multiple%20Whonix-Workstations/ multiple Whonix-Workstations]
** Add http proxy IP: 127.0.0.1 port: 4444 in Tor Browser's Tor Button.
* Network
** IP configuration: hidden mode (do not publish IP) <sup>1</sup>
** UDP-Port: completely disable <sup>2</sup>
** TCP: disable inbound (Firewalled) <sup>3</sup>
* Tunnels
** length (all tunnels): inbound and outbound: 0 <sup>4</sup>

<font size="-3"> ,, <sup>1</sup> There is no need to publish the exit node's IP address. It wouldn't work. Tor does not support incoming connections (server ports) unless hidden services are used. i2p very unlikely to support Tor hidden services, since they have their own network design. <sup>2</sup> UDP is unsupported by Tor. <sup>3</sup> Only outgoing TCP supported by Tor. <sup>4</sup> It's faster and less connection interrupts. Anonymity is already provided by Tor. No need to leech from Tor/i2p. </font>

== Installing i2p on Whonix-Gateway (i2pBOX) ==

Was just a development idea with some progress. Moved to [Inspiration].

= Footer =

[[include ref=WikiFooter]]

