[[include ref=WikiHeader]]

[TOC]

## Comparison of different Whonix variants ##
### Related to Virtualization or Hardware ###

Name| Number of systems | Security | Usability | Status
------------- |  ------------- | ------------- | ------------- |
[OneVM] | host+VM=2 | Better security than Tor Browser Bundle, Tor Live CDs. | Installation instructions depend on host operating system.; More difficult to install. | Deprecated. Looking for maintainer.
Standard [Download] version | host+VM+VM=3 | Same as OneVM. | Easily redistributable and installable. | Fully supported. Main development focus.
[PhysicalIsolation] with bare metal Gateway | host+VM+host=3 | Stronger than Standard Download version. | Difficult to install, advanced users only. | Fully supported.
[PhysicalIsolation] with virtualized Gateway | host+VM+host+VM=4 | Higher attack surface. | Easier to deploy. Four operating systems must be kept updated. | Limited supported.
[PhysicalIsolation] without any virtualization | host+host=2 | Basically same as standard Physical Isolation.; Smaller attack surface because not using Virtual Machines.; No protection against hardware fingerprinting.; | Difficult to install, advanced users only. | There are currently no instructions on how to build a Whonix-Workstation while not using a Virtual Machine. If you are interested please get in contact.

Virtual machines can provide following security related features:

* Network isolation (connections can easily be forced through tor)
* Hardware isolation (hide unique hardware serials)
* Roll back feature
* Cheap and simple multi-level security through running multiple clones/VMs

Live CDs offer:

* Non-persistence in case of software compromises
* Anti-Forensics and deniability (no encryption keys to disclose, if it's powered down and RAM is wiped/faded everything is "gone")
* But: difficult to roll out security updates

### Related to Operating System ###
Multiple options for operating system.

* Debian Wheezy GNU/Linux (Default-Download-Version, recommend!).
* See also [OtherOperatingSystems], especially [Security Comparison: Whonix-Download-Workstation vs. Whonix-Custom-Workstation](https://sourceforge.net/p/whonix/wiki/OtherOperatingSystems/#security-comparison-whonix-download-workstation-vs-whonix-custom-workstation)
* Any other, see *Whonix Framework*.
* There is [Hardened Gentoo based Whonix-Gateway](https://sourceforge.net/p/whonix/wiki/HardenedGentooTG/). (outdated, experts only, needs maintainer!) 

### Security Comparison: Whonix-Download-Workstation vs. Whonix-Custom-Workstation ###
See [Security Comparison: Whonix-Download-Workstation vs. Whonix-Custom-Workstation](https://sourceforge.net/p/whonix/wiki/OtherOperatingSystems/#security-comparison-whonix-download-workstation-vs-whonix-custom-workstation).

Unless otherwise stated, the documentation and design is about the Default-Download-Version.

# Footer #
[[include ref=WikiFooter]]