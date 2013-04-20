[[include ref=WikiHeader]]

[TOC]

# Using multiple Whonix-Workstations #
## Introduction ##
For tasks where you want to use additional software you should use a second (or third) VM, you can make a clone. Consider this more of a pseudonymous than an anonymous environment and act accordingly. 

Multiple Whonix-Workstation VM's isolate different torified clients from each other. For example, an exploit in the browser can not read your IRC identity in another VM. However, keep in mind, if Tor inside the Whonix-Gateway or your host internet connection goes offline, all Whonix-Workstations will go offline, and if you were simultaneously using something, an attacker could guess, that you are the same person (i.e. two Tor users in one IRC channel go offline at the same moment).

The most safe thing to do is using only one Whonix-Workstation for one activity at the same time.

Leaving multiple Whonix-Workstations running at the same time introduces also new risks. One compromised Whonix-Workstation can perform various attacks. It's impossible to defeat all those attacks. Depending on the adversary's skills and assumptions and your activity in other Whonix-Workstations, he could correlate various running Whonix-Workstations to the same pseudonym.

* An adversary could stress either/and CPU, HDD, RAM, network connection and other Whonix-Workstations and perhaps also the host would suffer. 
* There is no defense against DOSing other Whonix-Workstations or the Whonix-Gateway.
* The adversary could try to exploit other Whonix-Workstations or the Whonix-Gateway. This risk can be reduced by hardening. Whonix-Workstation provides an optional (disabled by default, because it can get into the way for other tasks) firewall (under "/usr/local/bin/whonix_firewall") to isolate different Whonix-Workstations from each other.
* A defense against impersonating (i.e. MITM or malicious gateway) other Whonix-Workstations or the Whonix-Gateway can be implemented using authentication, this is outlined below.

## How to use more than one Whonix-Workstation - EASY ##
The following instructions only apply for Download/Default-Whonix-Workstations or if you build yourself from source code. If you want to use other operating systems, such as Windows, other Linux, BSD etc. please see the [OtherOperatingSystems] article instead.

To setup a second or any additional Whonix-Workstation only two minor details are required. It needs it's own MAC address and it's own internal LAN IP address.

(1). Additional Whonix-Workstation and separate MAC address.

Clone a clean Whonix-Workstation. This will assign a new MAC address to the newly created Whonix-Workstation.

<font size="-3">Or in case you imported an extra Whonix-Workstation, go to Virtual Box -> Settings -> Network -> Adapter 1 -> Advanced -> Mac Address -> Create a new MAC address (press the green round arrow icon) -> Ok.</font>

(2). Open /etc/network/interfaces.

	sudo nano /etc/network/interfaces

(3). And change the last octet. E.g. 192.168.0.**11** or 192.168.0.**12**.

(4). Reboot or restart network using

	sudo service networking restart

(4). Done.

## How to use more than one Whonix-Workstation - More Security ##
(1) Quite useful: If you want to run multiple Whonix-Workstations at the same time, you should also read:

* [Connections between Whonix-Gateway and Whonix-Workstation](https://sourceforge.net/p/whonix/wiki/Connection%20Between%20Whonix-Gateway%20and%20Whonix-Workstation/)

(2) Really special: Knowledge assumed to understand the following lines:

* [Whonix's Protocol-Leak-Protection and Fingerprinting-Protection](https://sourceforge.net/p/whonix/wiki/Whonix%27s%20Protocol-Leak-Protection%20and%20Fingerprinting-Protection/).

There are some less important identifiers, which will differ on any additional Whonix-Workstation.

* VM uuid. (See [VirtualBox: Clone VM without Re-activation of Windows 7](http://www.windowstablettv.com/windows-tips/190-virtualbox-clone-windows-activation/). (Different motivation and goals, but technically the same.))
* The virtual MAC address. Since it is only a virtual MAC address, it is as well a less important identifier.
* The internal LAN IP address.

Since these are less important identifiers, you probable don't have to mess with them trying to make them uniform with the Default-Whonix-Workstation. You could make these less important identifies uniform (untested), but then you will most likely not be able to run multiple Whonix-Workstations at the same time. Since this is really, really a minor detail without practical or even theoretical consequences, you probable don't have to care about it.

# Footer #
[[include ref=WikiFooter]]