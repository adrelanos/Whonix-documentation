[[include ref=WikiHeader]]

[TOC]

# Freenet #
## Introduction ##
There are different ways to connect to the Freenet network.

## Using a gateway (inproxy) inside your Whonix-Workstation ##
A [freenet gateway](http://www.student.nada.kth.se/~md98-osa/gateway.html). Still working? How to use?

## Freenet inside the Whonix-Workstation (Freenet over Tor) ##
In "classical sense" (directly and only over Tor) this is impossible. This is tested, freenet installs normally, but even with lowest security settings, connection will never be established. The problem is, that Tor does not support UDP. (There has been a [discussion](http://comments.gmane.org/gmane.network.freenet.support/8211) about this topic. Although it's from 2008, it doesn't look like, the situation has changed or will change.)

Workaround (tested): [Tunneling UDP over Tor](https://sourceforge.net/p/whonix/wiki/TunnelUDPoverTor/). Note, that [Other Anonymizing Networks over Tor UDP Tunnel](https://sourceforge.net/p/whonix/wiki/Applications/#other-anonymizing-networks-over-tor-udp-tunnel) applies.

Another workaround: Buy, administrate and connect the SSH server anonymously though your Whonix-Workstation. Install freenet on the remote location and connect from your Whonix-Workstation (SSL or SSH tunnel). See the freenet wiki for more information.

# Footer #
[[include ref=WikiFooter]]