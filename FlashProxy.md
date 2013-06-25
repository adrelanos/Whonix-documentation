[[include ref=WikiHeader]]

[TOC]

# Flash Proxy

Credits: anonym on tails-dev wrote some things about Flash Proxy. These have been adapted for Whonix.

* Each flashproxy client requires a listening port on the open Internet. That's something we've never had in Whonix before, neither by default or through some options (our firewall even blocks it). That enables fingerprintability when scanning the ports of a Whonix host.

* Listening on a port like that also increases the attack surface dramatically; before this, no random host could try to attack Whonix by connecting to it -- the Whonix host had to (some how) connect to them first. So, yeah, these two things are quite contradictory.

* The above point also raises some practical issues: in order to listen on an Internet-exposed port, the user must either use IPv6 (which isn't served by all ISPs, and is unsupported/disabled by default in many routers in use) or, in the case of IPv4, set up port-forwarding (since most people are behind NAT). This limits the usefulness of flashproxy.

* The flashproxy client requires a direct connection to gmail.com, which I feel a bit uncomfortable with for a number of reasons. Currently Whonix only "speaks Tor" outwards, i.e. it communicates directly only with the Tor network or Tor bridges (exceptions: unsafe user on Whonix-Gateawy (e.g. for physical isolation users and captive portal login).

# Footer #
[[include ref=WikiFooter]]