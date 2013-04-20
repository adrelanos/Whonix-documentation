[[include ref=WikiHeader]]

[TOC]

# Whonix-Gateway #
Whonix-Gateway MUST NOT be ever used for anything other than running Tor on it.

If this machine is compromised the identity (public IP), all destinations and all clear-text (and hidden service) communication over Tor is available to the attacker.

Our first goal in securing the Whonix-Gateway is minimizing it's attack surface. By installing a "minimal system", the only attack surface to an remote attack is Tor itself, apt-get and tails_htp. You can verify this with netstat.

Security features that do not prevent exploitation but only restrict what exploits can do, such as chrooting or sandboxing, do not make much sense: A compromise of Tor already results in a compromise of everything the user cares about.

Compile time hardening (see [Bug #5024: compile time hardening of TBB (RELRO, canary, PIE)](https://trac.torproject.org/projects/tor/ticket/5024)) should be done by the Tor package maintainer and is beyond the scope of Whonix.

Debian is a good compromise of security and usability. More secure and hardened Linux or BSD based options do exist but they require too much work and/or maintenance to be considered for Whonix. The [OperatingSystem] design page elaborates on that topic.

Having said this, you are welcome to use your own distro. The Whonix design is distro agnostic. You just won't be able to thoughtlessly copy and paste commands or to use the source without modifications.

There was also a Hardened Gentoo based Whonix-Gateway (unfinished, experts only! Needs maintainer). See [HardenedGentooTG].

# Footer #
[[include ref=WikiFooter]]