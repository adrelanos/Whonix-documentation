[[include ref=WikiHeader]]

[TOC]

# List of installed Packages

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/Whonix-Gateway_packages

# Files
## Essential
### Anonymizer
An application to anonymize network traffic, called anonymizer, is required. The application to anonymize network traffic has to be obtained from a safe download source. Increase file maximum, if required by the anonymizer.

Whonix-Example-Implementation:

* Whonix is based on Tor.
* Tor configuration file: https://github.com/adrelanos/Whonix/blob/master/whonix_gateway/etc/tor/torrc
* Whonix uses Tor from Debian repositories.
* Tor's own repository is out commented by default in https://github.com/adrelanos/Whonix/blob/master/whonix_gateway/etc/apt/sources.list.d/torproject.list so the user would simply have to comment it in, get Tor's signing key and could start using Tor's own repository.
* Increase file maximum, if required by the anonymizer: https://github.com/adrelanos/Whonix/blob/master/whonix_gateway/etc/sysctl.d/whonix.conf

### Network Configuration
The Gateway needs two network interfaces. An external interface to communicate with clearnet for Tor and an internal interface to communicate with the Workstation.

Disable IPv6, if not supported by the anonymity network.

Disable IP forwarding, if it is not required due to the firewall rules (such as in case of Tor, which offers a TransPort and a DNSPort).

Configure the system resolver to use the anonymity network to resolve DNS. - This is **not** required to anonymize traffic of the Workstation. The system resolver of the Gateway should not get used by any applications anyway, because they are explicitly configured to use the anonymity network. Useful as defence in depth. DNS and other traffic from the Workstation gets forced by the firewall to use the anonymity network. The Gateways's own traffic gets anonymized with the purpose of **hiding the existence of the Gateway from the ISP**, because most users are expected, that they don't want to announce the existence of a Gateway, because that may indicate that they run hidden services or other less popular applications over Tor. The Gateway could alternatively fetch it's own operating system updates over clearnet, but since package selection is unique and implies, that a Gateway is in use and downloads are only authenticated and not encrypted, it's better to download the updates over the anonymity network. If an anonymity network with changing exit nodes (and therefore exit ISPs) such as Tor is getting used, this also makes it much harder for an adversary to interfere with the update process. The last sentence gets elaborated on the Design-Shared page in chapter "about package manager".

Prevent DHCP from updating the system resolver.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/whonix_gateway/etc/network/interfaces
* Disable IPv6, Disable IP forwarding. https://github.com/adrelanos/Whonix/blob/master/whonix_gateway/etc/sysctl.d/whonix.conf
* Prevent DHCP from updating the system resolver. https://github.com/adrelanos/Whonix/blob/master/whonix_gateway/etc/dhcp/dhclient-enter-hooks.d/nodnsupdate
* Configure system resolver to use the anonymity network to resolve DNS. https://github.com/adrelanos/Whonix/blob/master/whonix_gateway/etc/resolv.conf

### Firewall
Add a firewall, which only allows traffic the anonymizer to connect to the internet.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/whonix_gateway/usr/local/bin/whonix_firewall

## Debugging
### Firewall Removal
**Optional**

Include a command to easily remove all firewall rules, which can not be run by accident without editing the file with root rights.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/whonix_gateway/usr/local/bin/dev_clearnet

### Leaktest script
**Optional**

Have a script to try to produce a leak and check if there are any leaks.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/whonix_gateway/usr/local/bin/leaktest
* [LeakTests]

### Clearnet User
**Optional**

To have a user account "clearnet" on the Gateway may be helpful for debugging, an "unsafe" browser (which can be used to register public hotspots).

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/whonix_gateway/usr/local/share/whonix/chroot-scripts/70_clearnetuser

## Usability
### Tor Controller
**Optional**

Whonix-Example-Implementation:

* Arm is installed by default and documented on the [TorController] page.
* Tor Controller startup script. Starting Tor controller without password by using "sudo arm": https://github.com/adrelanos/Whonix/tree/master/whonix_gateway/usr/local/bin/arm

### Help file
**Optional**

When the user types a short and easy command, the most important and most asked commands should be listed.

Whonix-Example-Implementation:

* User can type "whonix".
* https://github.com/adrelanos/Whonix/blob/master/whonix_gateway/usr/local/bin/whonix

### Marker file
**Optional**

Add a marker file so scripts you write can find out, whether they are running on the Gateway or inside the Workstation. There are probable different implementations possible to reach that goal.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/whonix_gateway/usr/local/share/whonix/whonix_gateway

# Design-Shared
Changes from [Design-Shared] also have to be added to the Gateway.

# Footer #
[[include ref=WikiFooter]]