[[include ref=WikiHeader]]

[TOC]

# Connection between Whonix-Gateway and Whonix-Workstation #
## Introduction ##
**This chapter is only important, if you do not use the Default/Download (host + VM + VM) version.** You should read it if you are using Physical Isolation or for any kind of custom, non-stock configurations.

### Basics ###
By Whonix default, it is assumed, that Whonix-Gateway and Whonix-Workstation are connected by (virtual) LAN cable. Wireless technologies are recommend against, because a malware compromised Whonix-Workstation could jump to other wireless access point and subsequently connect without Tor. Using a (virtual) cable enforces, that Whonix-Workstation can only connect through Whonix-Gateway. For the same reason connections to Whonix-Gateway over internet are recommend against as well.

By Whonix default, connections between Whonix-Workstation and Whonix-Gateway are not authenticated/encrypted. This is because of the assumption above. The connection between Whonix-Workstation and Whonix-Gateway is assumed to be secure. ^1^ Adding authentication/encryption by default would also greatly increase complexity of Whonix, which is what we want to avoid in the first place for reasons explained in earlier chapters.

In case you want to run multiple Whonix-Workstations at the same time inside the same (virtual) isolated LAN, you should add authentication:

* Inside virtual LANs:
    * Authentication is enough.
    * No encryption is required.
        * When no machines can be impersonanted, no MITM is possible inside the virtual LAN.
* Inside real LANs:
    * You only need encryption if in your threat model includes the possibility for a MITM.

In case you want to connect to Whonix-Gateway over insecure networks (internet):

* You should add encryption and authentication.
    * Encryption is required, because otherwise a MITM could eavesdrop.
    * Authentication ensures, you're connecting to the right machine.
        * Most encryption solutions, such as OpenVPN or ssh also provide authentication.

<font size="-3">
,,
^1^ Secure means, you assume that no one on your (virtual) LAN is going to MITM.
</font>

### Motivation for secure connections between Whonix-Gateway and Whonix-Workstation ###
**Only applies to non-stock configurations**: if you run multiple Whonix-Workstations at the same time or if you want to connect to Whonix-Workstation over insecure networks (internet):

A compromised Whonix-Workstation can impersonate Whonix-Gateway or any other Whonix-Workstation inside the same (virtual) LAN, perform active MITM attacks or passively eavesdrop.

### OpenVPN vs SSH ###
Adding encryption can be done using OpenVPN or SSH. Using SSH and not OpenVPN, has the advantage, that you an later, still easily tunnel a VPN through Tor. If you don't plan to do this, using OpenVPN is probable easier. The disadvantage of using SSH is, that it's complicated to setup for this use case. You are probable better off using OpenVPN.

## Authenticated connections between Whonix-Gateway and Whonix-Workstation ##
### ARP spoofing defense ###
This is only been quickly researched. After reading the [wikipedia article about ARP spoofing](https://en.wikipedia.org/wiki/ARP_spoofing), it looks like *Static ARP entries* could be used for authenticated connections between Whonix-Gateway and Whonix-Workstation.

### Using additional (isolated) network interfaces ###
(This chapter is actually not authentication, solves the threat nonetheless.)

A workaround, when using Virtual Box and running everything on the same host:

* One can also enable Virtual Network Adapter 3 and 4 and use uniquely named internal networks, for up to 3 Whonix-Workstations, which are isolated against each other.

A workaround, for Whonix with Physical Isolation, where all machines in the same trusted place: 

* That Whonix-Gateway already requires two network interfaces is a though requirement. (External and internal interface.) You could theoretically also add additional interfaces for additional internal LAN interfaces.

## Encrypted and authenticated connections between Whonix-Gateway and Whonix-Workstation ##
### Using SSH (not tested/recommend) ###
You must not allow [ssh login](http://serverfault.com/questions/56566/ssh-tunneling-only-access).

Each Whonix-Workstation probable needs its own SSH account, with public key authentication and the SSH private key distributed to each T-W. Whonix-Gateway and all Whonix-Workstations need the correct SSH commands. Whonix-Gateway has to autostart SSH and to continuously listening for connections. And Whonix-Workstation has to autostart SSH as well and continuously reconnect (in case Whonix-Workstation started before Whonix-Gateway or Whonix-Gateway restarted) (perhaps using autossh or something similar). All Whonix-Workstations need to use the tunnel IP, to connect to the Whonix-Gateway. And the Whonix-Gateway should reject unencrypted gateway requests, and only accept forwarding to Tor over the SSH tunnel. And also answer only over the SSH tunnel. All Whonix-Workstations must use the SSH tunnel as gateway (redirect network level to socks using tranSOCKS_ev or similar). Perhaps also changes in the Whonix-Gateway firewall are required. Taking all the into account, it looks like, it's not impossible to use SSH for this task, but it's quite complicated.

You are probable better off using OpenVPN.

### Using OpenVPN ###
**DRAFT! UNFINISHED!**

Right now only supports two modes/security domains:

* Whonix-Workstations with the secret key (=trusted) and
* other workstation with no key/vpn configured.

NOTE:

* Transparent proxying doesn't seem to work at all, therefore you need to configure all applications to use socks ports.

On the gateway:

	sudo -i
	apt-get -y install openvpn

	# create a new symmetric key
	sudo -u user openvpn --genkey --secret /home/user/static.key

	# copy key to workstation (Firewall needs to be disabled and openssh-server installed on Whonix-Workstation for this to work)
	sudo -u user scp /home/user/static.key user@192.168.0.10:/home/user/static.key

	mv /home/user/static.key /etc/openvpn/static.key
	chown root:root /etc/openvpn/static.key
	chmod 700 /etc/openvpn/static.key

	# create server configuration
	echo "
	user nobody
	group nogroup
	daemon
	dev tun
	ifconfig 10.8.0.1 10.8.0.2
	secret /etc/openvpn/static.key" > /etc/openvpn/server.conf

	service openvpn restart

	# Edit torrc
	# TODO: only selectively change listening addresses. TransPort and optionally other SocksPorts have to remain available,
	#       if unauthenticated workstations are to be used.
	# NOTE: we are using a hardcoded default IP here, if you are using non standard settings this will have to be edited.
	ed -s /etc/tor/torrc <<< $',s/192.168.0.10/10.8.0.1/g
w'

	# Edit /usr/local/bin/whonix_firewall
	# TODO: Put this automatically where it actually belongs
	echo '
	# Allow openvpn in on port 1194
	iptables -A INPUT -i $INT_IF -p udp --dport 1194 -j ACCEPT' >> /usr/local/bin/whonix_firewall
	# TODO: replace hardcoded "eth1" with a wildcard
	ed -s /usr/local/bin/whonix_firewall<<< $',s/INT_TIF=eth1/INT_TIF=tun0/g
w'

	/usr/local/bin/whonix_firewall

On the Workstation(s):

TODO: Disable/tweak the new firewall

	sudo -i
	
	mv /home/user/static.key /etc/openvpn/static.key
	chown root:root /etc/openvpn/static.key
	chmod 700 /etc/openvpn/static.key
	
	# should be in the default installation
	apt-get --yes install --no-install-recommends torsocks
	
	echo "
	user nobody
	group nogroup
	daemon
	remote 192.168.0.10
	dev tun
	ifconfig 10.8.0.2 10.8.0.1
	secret /etc/openvpn/static.key" > /etc/openvpn/server.conf

	# Edit resolv.conf
	chattr -i /etc/resolv.conf
	echo "nameserver 10.8.0.1" > /etc/resolv.conf
	chattr +i /etc/resolv.conf

# Footer #
[[include ref=WikiFooter]]