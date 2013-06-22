[TOC]

= Deprecated =

Source code archived on github for historical reasons. Signed (by adrelanos) tag 0.1.3 available. https://github.com/adrelanos/Whonix https://github.com/adrelanos/Whonix/zipball/0.1.3

0.1.3 does not work anymore, because Tor 0.2.3 was released and changes to torrc are required.

= Obsolete =

This page documents how the [Download binary distribution images] are built.

Following these instructions will always build the latest available version. The scripts used to build a certain version of a Tor-Gateway or Tor-Workstation image can be found in the VM at /usr/share/doc/torbox and through the wiki history. If you only want to build images for your own use you can type any password you want right away during installation instead of first using &quot;changeme&quot; (but you must choose the username &quot;user&quot;), same goes for the keyboard layout.

If you have any questions or need help let us know [/Dev#Questions here].

Knowledge assumed: Virtualization and networking basic principles; operation of your platform; Linux knowledge: how to install Ubuntu and basic command line knowledge.

Only two prerequisites: you need to have VirtualBox installed and you need a working internet connection.

For discussion related to the development and build process of TorBOX images go [/Dev/ClientVM here].

= Build Security =

* Build on a dedicated build system, install security updates...
* All install media and all downloaded/used code must be verified (including all software on the host)
* Hashes or fingerprints listed on the wiki are not to be trusted, same goes for the scripts, verify them (and make use of the history feature)

= Host preparation =

We recommend you use a dedicated OS installation just for hosting the TorBOX VMs (See [/SecurityAndHardening TorBOX/SecurityAndHardening])

Install the latest security updates, install VirtualBox and reboot to apply kernel updates.

'''Read and apply if necessary [/Readme#NetworkTimeSyncing &quot;Network Time Syncing&quot;]!

''' If you use Debian/Ubuntu: {{{ sudo apt-get update &amp;&amp; sudo apt-get dist-upgrade sudo apt-get install virtualbox sudo reboot }}}

'''If you use Windows as the host'''

Download all security updates, install an antivirus... usual security recommendations apply.

Download and verify required software: * [https://www.virtualbox.org/ VirtualBoX] * SSH and SCP, we recommend [http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html PuTTY and PSCP]

= Create Tor-Gateway.ova =

== Installation ==

Download and verify [http://www.ubuntu.com/download/server/download ubuntu-11.10-server-i386.iso] <sup>1</sup>

,,<sup>1</sup> Other Linux flavors will also work such as Debian stable, Debian testing, etc. This is untested and will require slight changes to the shell script (see comments in the script).

Following settings are used (if nothing is specified choose default settings/selections)

<pre>VM Settings:
Name: Tor-Gateway
Ubuntu, 2 GB Disk, 128 MB RAM
Leave Adapter 1 as NAT
Add port forwarding for ssh: within the &quot;Adapter 1&quot; tab click &quot;Advanced&quot;, then Port Forwarding. Insert a new rule as follows: 
Name: SSH; Protocol: TCP; Host IP: 127.0.0.1; Host Port: 2222; Guest IP: leave blank; Guest Port: 22 
Enable Adapter 2, set to &quot;Internal Network&quot;
Disable &quot;System-&gt;Enable absolute pointing device&quot;, then disable &quot;USB-&gt; Enable USB Controller&quot;
Close Settings window and start the VM:
In the boot menu press F4 and select &quot;Install a minimal system&quot;
Language English
United States
keyboard layout English (US) (don't autodetect)
Primary network interface: eth0
Hostname: ubuntu
Timezone:UTC
Partitioning: Guided - use entire disk (Not LVM!)
Username: user
Password: changeme
encrypt home folder: No
No automatic updates 
tasksel: select nothing</pre>
== Configuration ==

Log in and install the latest security updates and reboot to apply kernel upgrades. (run on the guest)

<pre>sudo apt-get update &amp;&amp; sudo apt-get --yes dist-upgrade
sudo reboot</pre>
It is recommended that you install a ssh server at this point so you can copy and paste commands from host: (run on the guest)

<pre>sudo apt-get install openssh-server</pre>
Transfer [/Dev/TGScript tor-gateway.sh] to /home/user (run on the host)

<pre>scp -P 2222 tor-gateway.sh user@127.0.0.1:/home/user/</pre>
(Instead of using scp you can also log in via ssh, open nano and copy and paste the script, save as tor-gateway.sh; exit)

Now you can log in from the host with (run on the host)

<pre>ssh -p 2222 user@127.0.0.1</pre>
Import GPG key for the Torproject repository: Do not simply trust the [https://www.torproject.org/docs/signing-keys.html.en fingerprint] you found here. [https://www.torproject.org/docs/debian.html.en#ubuntu Verify] that it is correct! (run on the guest)

<pre>gpg --keyserver x-hkp://pool.sks-keyservers.net --recv-keys 886DDD89
gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | sudo apt-key add -</pre>
Before executing read through the script to check for errors (or malicious edits)!

<pre>nano tor-gateway.sh</pre>
Run tor-gateway.sh directly on a terminal, not through ssh! (run on the guest)

<pre>chmod +x tor-gateway*.sh
sudo ./tor-gateway.sh -vm</pre>
If you install on bare metal omit the &quot;-vm&quot;.

Wait till it says &quot;Tor-Gateway configuration successful.&quot; If the script fails you probably forgot to attach the second adapter or to import the gpg key or your internet connection is down. After fixing that simply run the script again. If it still fails please let us know on [/Dev TorBOX/Dev]!

== Final Steps ==

* remove port forwarding
* Poweroff. In Network-&gt;Adapter 2: rename the network to &quot;torbox&quot;

Skip the following if you build for your own use and not for redistribution. (run on the guest) * sudo mv ./tor-gateway.sh /usr/share/doc/torbox * set password to &quot;changeme&quot; if a different one was used before (use the command passwd) * rm .bash_history (you need to log out and back in first for this to have any effect) * Export the VM, save as Tor-Gateway.ova * [/TestAndTroubleshoot Test] the image before release!

= Create Tor-Workstation.ova =

== Installation ==

Download and verify ubuntu-11.10-server-i386.iso

Following settings are used (if nothing is specified choose default settings)

<pre>VM Settings: 
Name: Tor-Workstation
Ubuntu, 8 GB Disk, 512 MB RAM
In Settings-&gt;Network Leave Adapter 1 as NAT (faster apt-get downloads during set up)
Enter following MAC address: 080027070b08
Add port forwarding for ssh: within the &quot;Adapter 1&quot; tab click &quot;Advanced&quot;, then Port     Forwarding. Insert a new rule as follows: 
Name: SSH; Protocol: TCP; Host IP: 127.0.0.1; Host Port: 4444; Guest IP: leave blank; Guest Port: 22
In the boot menu press F4 and select &quot;Install a minimal system&quot;
Language English
United States
Keyboard layout English (US)
Hostname: ubuntu
Timezone: UTC
Partitioning: Guided - use entire disk (Not LVM!)
Username: user
Password: changeme
encrypt home folder: No
No automatic updates 
tasksel: select nothing</pre>
== Configuration ==

Log in and install the latest security updates and reboot to apply kernel upgrades. (run on the guest)

<pre>sudo apt-get update &amp;&amp; sudo apt-get --yes dist-upgrade
sudo reboot</pre>
It is recommended that you install a ssh server at this point so you can copy and paste commands from host: (run on the guest)

<pre>sudo apt-get install openssh-server</pre>
Transfer [/Dev/TWScript tor-workstation.sh] to /home/user (run on the host)

<pre>scp -P 4444 tor-workstation.sh user@127.0.0.1:/home/user/</pre>
(Instead of using scp you can also log in via ssh, open nano and copy and paste the script, save as tor-workstation.sh and exit)

Now you can log in from the host with (run on the host)

<pre>ssh -p 4444 user@127.0.0.1</pre>
Before executing read through the script to check for errors (or malicious edits)!

<pre>nano tor-workstation.sh</pre>
Make the script executable and run it (You need to run it directly on a terminal, not through ssh!) (run on the guest)

<pre>chmod +x tor-workstation.sh
sudo ./tor-workstation.sh</pre>
== Final Steps ==

* remove port forwarding
* Poweroff. Set Adapter 1 to internal, rename the network to &quot;torbox&quot;

Skip the following if you build for your own use and not for redistribution. (run on the guest) * mv ./tor-workstation.sh /usr/share/doc/torbox #This script * set password to &quot;changeme&quot; if a different one was used before (use the command passwd) * rm .bash_history (you need to log out and back in first for this to have any effect) * Export the VM, save as Tor-Workstation.ova * [/TestAndTroubleshoot Test] the image before release!

= How to use the ova images =

Reboot both VMs. Please read the [/Readme Readme]!

= Testing and Troubleshooting =

[/TestAndTroubleshoot TorBOX/TestAndTroubleshoot]

= Footer =

[[include ref=WikiFooter]]

