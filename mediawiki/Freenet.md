[[include ref=WikiHeader]]

[TOC]

= Freenet =

== Introduction ==

There are different ways to connect to the Freenet network.

== Using a gateway (inproxy) inside your Whonix-Workstation ==

A [http://www.student.nada.kth.se/~md98-osa/gateway.html freenet gateway]. Still working? How to use?

== Freenet inside the Whonix-Workstation (Freenet over Tor) ==

In &quot;classical sense&quot; (directly and only over Tor) this is impossible. This is tested, freenet installs normally, but even with lowest security settings, connection will never be established. The problem is, that Tor does not support UDP. (There has been a [http://comments.gmane.org/gmane.network.freenet.support/8211 discussion] about this topic. Although it's from 2008, it doesn't look like, the situation has changed or will change.)

Workaround (tested): [https://sourceforge.net/p/whonix/wiki/TunnelUDPoverTor/ Tunneling UDP over Tor]. Note, that [https://sourceforge.net/p/whonix/wiki/Security%20Guide/#other-anonymizing-networks-over-tor-udp-tunnel Other Anonymizing Networks over Tor UDP Tunnel] applies.

Another workaround: Buy, administrate and connect the SSH server anonymously though your Whonix-Workstation. Install freenet on the remote location and connect from your Whonix-Workstation (SSL or SSH tunnel). See the freenet wiki for more information.

= Footer =

[[include ref=WikiFooter]]

