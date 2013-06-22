[[include ref=WikiHeader]]

[TOC]

= OLD =

'''OneVM is deprecated. It was tested and developed for 0.1.3. The concept worked. It's deprecated now, because it has no maintainer.'''

= Introduction =

Whonix needs at least two systems, one running Tor, the other running clients that are routed through Tor. This ensures the highest possible security and isolation. We can implement this using different strategies: Two VMs (Gateway VM and Workstation VM) or bare metal. A different approach is to use a host running Tor and only a single client VM. This site will guide you through all required steps to set up a One VM Whonix. If anything remains unclear please refer to the more verbose How To.

Advantages:

* One VM less required.
* One operating system less required.
* Less system resources required.

Disadvantages:

* Much more difficult to develop, deploy and test for the many different host operating systems.
* Difficult to develop a download version. Could be only an installer, which had to comply with the differences in different host operating systems.
* Guest VM can see MAC address of host?

= Host preparation =

Install Ubuntu 12.04.

You should choose &quot;user&quot; as your username (you can also add such a user if you already installed Ubuntu). Otherwise you need to edit the script (see PREREQUISITES/ASSUMPTIONS #4). You can ignore the ASSUMPTION #2, the -onevm option will configure a virtual internal interface called vnet0.

Get the shell script and run it on the host

<pre>sudo Whonix-Gateway -onevm</pre>
Download or build the Whonix-Workstation image. # VirtualBox settings for Whonix-Workstation #

Go to Devices &gt; Network Adapter. Make sure all network adapters except Adapter 1 are disabled. Set Adapter one according to following options: (IMPORTANT!)

Attached to: Bridged Adapter Name: vnet0 Click OK.

= Guest VM configuration =

Follow instructions for Whonix-Workstation in [BuildDocumentation].

Run as root (sudo -i) directly on the workstation (since you need to set up networking ssh can't be used):

<pre>ifdown -a

echo &quot;
auto eth0
iface eth0 inet static
# increment last octet (the ...0.2) on additional workstations
address 172.16.0.2
   netmask 255.255.255.0
   network 172.16.0.0
   broadcast 172.16.0.255
   gateway 172.16.0.1&quot; | tee -a /etc/network/interfaces

chattr -i /etc/resolv.conf
echo &quot;nameserver 172.16.0.1&quot; | tee /etc/resolv.conf
chattr +i /etc/resolv.conf
ifup -a</pre>
Source: http://www.howtoforge.com/how-to-set-up-a-tor-middlebox-routing-all-virtualbox-virtual-machine-traffic-over-the-tor-network

= Footer =

[[include ref=WikiFooter]]

