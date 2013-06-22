[[include ref=WikiHeader]]

[TOC]

= Most simple, least secure =

Inoffical Video, using Whonix-Gateway to torify Ubuntu.

Html5 Video. Works without Flash inside Tor Browser. Showing the Easiest, but least secure option, see [https://www.youtube.com/embed/id_l4fKqA4Q Youtube Link].

= More secure =

Tested with Debian and Ubuntu.

Download [http://www.ubuntu.com/download Ubuntu] (or use a different install CD or iso file) and verify using [https://help.ubuntu.com/community/VerifyIsoHowto VerifyIsoHowto].

Create a new VM and choose following settings: Under Network set Adapter 1 to &quot;Internal Network&quot;, rename &quot;intnet&quot; to &quot;Whonix&quot;.

You can use the Live environment or install Ubuntu. When the installer asks questions, generally choose the default, most common or other non-identifying options. Language: English; keymap: choose yours (potentially risk...); Country (leave it as it is): United States; User Name: leave blank; Host Name (leave it as it is): ubuntu; Time Zone (change it): UTC (it's at the very bottom); Username (account name): user. This ensures that all Whonix users have the same settings. Additionally this is more safe, when an application leaks such data, such as SSH, if you simply ssh some.host.name, it will tell your current account name, and it would be very bad if this where you real name or anything which would identify you.

Reboot into the freshly installed system and open a terminal:

Remove Ubuntu's “phone home” program(s). In a terminal type:

<pre># If installed, will not hurt if not installed.
sudo apt-get -y remove canonical-census unity-lens-shopping unity-scope-video-remote unity-scope-musicstores</pre>
Dhcp auto-configuration like software such as network manager have to be removed, since we are using static networking.

<pre>sudo apt-get remove isc-dhcp-client isc-dhcp-common network-manager network-manager-gnome resolvconf</pre>
Setup a fixed IP for the virtual LAN network card and to use the same subnet like the Whonix-Gateway for the Internal Network. If you use a Linux desktop with network manager you can use the GUI for this step. Otherwise: open a Terminal and type

<pre>sudo nano /etc/network/interfaces</pre>
You only need to configure eth0:

<pre># This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

# The loopback network interface, leave as it is
auto lo
iface lo inet loopback

auto eth0
#iface eth0 inet dhcp
iface eth0 inet static
# increment last octet on additional workstations
       address 192.168.0.12
       netmask 255.255.255.0
       #network 192.168.0.0
       #broadcast 192.168.0.255
       gateway 192.168.0.10</pre>
Open /etc/resolv.conf.

<pre>sudo nano /etc/resolv.conf</pre>
and delete everything, then add

<pre>nameserver 192.168.0.10</pre>
If you forgot to set the time to UTC you can do so at any time by type the following into the terminal:

<pre>sudo dpkg-reconfigure tzdata</pre>
Now would be a good time to create a snapshot of the VM.

Update package lists.

<pre>sudo apt-get update</pre>
Get latest updates.

<pre>sudo apt-get dist-upgrade</pre>
Now would be a another good time to create a snapshot of the VM.

= Guest additions for Ubuntu =

Optional. '''Warning: Not recommend!''' Weakens security as per [Security Guide].

You can try first, if [https://sourceforge.net/p/whonix/wiki/VirtualBox%20Guest%20Additions/ VirtualBox Guest Additions] work on Ubuntu, because they are a bit shorter and easier.

Otherwise...

On the host:

<pre>sudo apt-get install virtualbox-guest-additions-iso</pre>
Inside Whonix-Workstation:

Execute the following commands. They can take a very long time, due to the Ubuntu upstream bug [https://bugs.launchpad.net/ubuntu/+source/dpkg/+bug/947664 Unpacking linux-headers unbelievably slow in Lubuntu Precise (Beta 1)] (affects Ubuntu precise final as well).

<pre>sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install dkms build-essential linux-headers-generic linux-headers-generic-pae</pre>
Insert the guest additions iso by clicking on the VM -&gt; devices -&gt; install guest additions.

<pre>sudo mkdir -p /mnt/sr0
sudo mount /dev/sr0 /mnt/sr0
sudo sh /mnt/sr0/VBoxLinuxAdditions.run</pre>
Or start autorun.sh (not with a console, strange bug!).

Force remove CD eject.

Reboot. Done.

= Advanced =

== About Ubuntu ==

While Ubuntu is one of the more secure (See [https://wiki.ubuntu.com/Security/Features Overview]) Linux distributions it's by no means a secure operating system. It is designed first and foremost to bring Linux to end users. It doesn't protect against some of the threat models that some Tor users will have.

Here's an (incomplete) list of things the more paranoid user will have to consider:

''apt-get'' as currently used in Ubuntu does not protect against a ''stale mirror attack'' ([https://bugs.launchpad.net/launchpad/+bug/716535 Bug #716535: Please support Valid-Until in release files for security.ubuntu.com]) where an adversary provides validly signed but outdated metadata to prevent users from downloading and installing the latest critical security updates. When fetching updates over tor this problem is of a lesser extent because no single malicious exit node will realistically prevent users from downloading updates more than once in a row. Malicious mirror is possible but Whonix-Workstation uses the main US mirror, any irregularities will be uncovered pretty soon. More of concern is the clear text update of the host operating system. Here it's a good idea to manually check how old the repository metadata is yourself:

<pre>find /var/lib/apt/lists/* -type f | xargs cat | grep &quot;Date: &quot;</pre>
From time to time vulnerabilities that allow installation of untrusted code are discovered in apt. New security features are often implemented in Debian first.

The Ubuntu server kernel comes with everything and the kitchen sink. At any given day the kernel will be vulnerable in one way or the other. It's by far the most patched piece of code in the default Ubuntu Server installation, obviously runs at full kernel privileges and naturally can't be protected with mandatory access control. Whonix-Gateway exposes the kernel to attacks through its firewall, TCP/IP stack and whatever kernel calls Tor does or could be compelled to do.

[http://www.trapkit.de/tools/checksec.html checksec.sh] --kernel reports good kernel protection: GCC stack protector support, Enforce read-only kernel data, Restrict /dev/mem and /dev/kmem access are all enabled!

Userland protection for Tor is great.<sup>1</sup> Unlike TBB bundles the tor version distributed via the .deb comes with RELRO, canaries etc. and can fully make use of ASLR since it's compiled as PIE. Of course with Grsec the entropy would be higher.

<font size="-3"> <sup>1</sup> This would only apply if you created a Custom-Whonix-Gateway. </font>

= Footer =

[[include ref=WikiFooter]]

