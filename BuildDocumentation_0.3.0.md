[Whonix Homepage](https://sourceforge.net/p/whonix/wiki/Home/)

[TOC]

**NOT FINISHED!**

    # Copyright:
    # adrelanos (aka proper)
    # adrelanos (at) riseup (dot) net
    #
    # License:
    # GPL v3 or any later
    #
    # Any changes you pull into this source will be also licensed
    # under GPL v3 or any later. Additionally you grant adrelanos the right to
    # re-license your work under a different license. If that is not acceptable,
    # you can either fork this source under GPL v3 or any later or contact
    # adrelanos. Contact adrelanos, if you require this source code under
    # different license.
    #
    # Authors:
    # adrelanos (aka proper)
    # Big contributions from anonymous.
    # Leaktest and other stuff contributed by smarm.

This page documents how the binary distribution images are built. If you have any questions or need help let us know on [Dev].

Following these instructions will build version Whonix 0.3.0 based on Tor 0.2.3 and Ubuntu Precise.

Knowledge assumed: Virtualization and networking basic principles; operation of your platform; Linux knowledge: how to install Ubuntu and basic command line knowledge.

Only one prerequisites: you need a working internet connection.

For discussion related to the development and build process of Whonix images go [Dev].

# Build Anonymity #
While downloading the required tools for building Whonix your internet service provider could if he want notice that you want to build Whonix. This is esspecially interesting, if you want to redistribute Whonix, but still want to stay anonymous. The full story can be read in the chapter [Build Anonymity](https://sourceforge.net/p/whonix/wiki/Security/#build-anonymity).

# Build Security #
* Build on a dedicated build system, install security updates...
* All install media and all downloaded/used code must be verified (including all software on the host).
* Hashes, fingerprints  in the scripts and the wiki is not to be trusted. Verify everything.
* Read [Trust]

# Host preparation #
We recommend you use a dedicated OS installation just for hosting the Whonix VMs. (See [Security])

You need to use Ubuntu. The build scripts could be adapted to run on other *NIX systems as well but currently they assume apt-get to be available. You need about 15 GB of free space.

Install the latest security updates, install Virtual Box (and qemu-kvm which is required to mount the Virtual Box .vdi images). Reboot to apply kernel updates.

    sudo apt-get update && sudo apt-get dist-upgrade
    sudo apt-get install virtualbox qemu genisoimage
    sudo reboot

If you are going to use Virtual Box inside Virtual Box, be sure to change your host key. Virtual Box -> Preferences -> Input -> Host Key. The "outside" and the "inside" Host Key must differ, otherwise you can not leave the VM "inside" anymore. The "outside" Virtual Box hostkey may NOT be **ctrl**.^1^

,, ^1^ Because the one is used by VBoxSDL "inside".

Building on Windows is no longer supported. Redistributed Whonix builds should be build on Linux. If you want to port the Whonix build scripts to Windows, please contact us. Running Whonix on a Windows host with Virtual Box installed should is still possible.

## Using an apt cache to speed up downloading ##
**OPTIONAL**

Does only work with Whonix-Gateway. 
,, Does not work for Whonix-Workstation because it never gets direct access to the host by design. We could think about installing apt-cacher-ng on Whonix-Gateway, if there are any security implications.

If you want to build multiple times (for debugging etc.), it might make sense to install a local apt proxy on your build machine. That safes download time and traffic. 

,,Thanks to [source](https://linuxexpresso.wordpress.com/2011/02/13/howto-apt-cacher-ng-on-ubuntu/).

On the host:

    sudo apt-get install apt-cacher-ng

.

    sudo nano /etc/apt/apt.conf

.

    # /etc/apt/apt.conf
    Acquire::http { Proxy "http://127.0.0.1:3142"; };


.

    sudo apt-get update

In whonix_gateway source code: 
Go to /home/user/whonix/whonix_gateway/usr/local/bin/whonix_internal_install_script script and comment in the line *Acquire::http { Proxy "http://192.168.0.2:3142"; };*, i.e. remove the # (hash) in front of it.

# Source Code Intro #
**If you prefer to read and understand the source code just by reading scripts you may skip this optional chapter.** This chapter is dedicated to give an introduction into the Whonix source code. It can be quite difficult to get started with hacking existing big complex projects.

Both Virtual Machines will be started two times while building Whonix. The first time the operating system will be installed and the second time either the whonix_internal_install_script runs.

**whonix_gateway** All files within that folder will be copied into Whonix-Gateway. 
**whonix_workstation** All files within that folder will be copied into Whonix-Workstation. 
**whonix_shared** All files within that folder will be copied into Whonix-Gateway and Whonix-Workstation. 
Copying is done with whonix_craetevm and implemented in int_copy_gateway, int_copy_workstation and int_copy_shared.

**int_xxx** scripts are internally used by whonix_xxx scripts.

**whonix_build** is a script, which simply runs all other scripts. Actually it's "optional". It has very little functionality beside running all other scripts. You are free to run all scripts one by one. That is useful for learning and for debugging purposes. In case you want to fix a bug or in case you want to upgrade the distribution or in case you want to switch the operating system or whatever you are better off running the steps manually. You can use the Build script as a reference for which steps have to be run in which order.

**whonix_getiso** downloads and verifies the operating system iso image.

**whonix_modifyiso** mounts the downloaded iso image as read only, copies it, modifies the copied iso image by adding preseeding (unattended installation), unmounts the iso and finally creates preseed.iso, which contains the operating system installer disc modified not to require any user interaction while installing. This process already sets up lots of important privacy settings and other stuff, such as UTC timezone, hostname ubuntu, US language, username user and so on. (See [Security] and the modifyiso script itself for a list of all changes and why.) Preseed.iso is configured to power off itself when it's done installing so the whonix_build script can continue.

**whonix_createvm** creates Virtual Box machines with all settings required for secure networking, devices, security settings. Which those settings are in details can be again read in Security And Hardening or the script itself. whonix_createvm is also responsible for starting virtual machines while building. It also features to mount the virtual hdd images for debugging reasons. The whonix_internal_install_script will be copied into the VMs by whonix_createvm.

**whonix_internal_install_script** A Whonix-Gateway specific version is stored under /home/user/whonix/whonix_gateway/usr/local/bin/whonix_internal_install_script and a Whonix-Workstation specific version is stored under /home/user/whonix/whonix_gateway/usr/local/bin/whonix_internal_install_script. This script gets copied into the Virtual Machines by whonix_createvm. whonix_internal_install_script gets automatically started, only once at build time, by rc.local. They will transform the installed operating system into the Whonix-Gateway or into the Whonix-Workstation. They update the system, install security relevant software, install useful applications for an anonymous general purpose operating system, set up all relevant privacy and anonymity required settings, desktop manager etc.

**rc.local** (/home/user/whonix/rc.local) gets copied to into the VMs to /etc/rc.local and keeps care of automatically starting whonix_internal_install_script. ^2^ The final version of rc.local, which the user will see, will be reverted by 'whonix_createvm -tX-copyinto-post' and can be found under /home/user/whonix/whonix_shared/etc/rc.local.

Thus, given the nature of the build step orientated scripts, you can easily work on the the different aspects of Whonix. For example, once you have created a clean virtual machine with the operating system only, you can make a clone or snapshot, run either the whonix_Gateway or the whonix_Workstation script as often as you need to test your changes and if something goes wrong, go back to the clone or snapshot. You don't have to build everything from scratch again. ^3^

,, ^3^ For example, we could add the whonix_Gateway or whonix_Workstation script to the preseed.iso and let it run after installing. If something would go wrong, you would have to reinstall the whole operating system every time again. That's why we use separate steps.

# Get the Whonix source code #

    git clone https://github.com/adrelanos/Whonix

# Create the Images #
## Preparations ##
(1) Make the build script executable: 

    chmod +x ~/whonix/whonix_*

(2) Make sure there aren't any VMs in Virtual Box already called "Whonix-Gateway" or "Whonix-Workstation" (TODO: automate that)

(3) Check if /home/user/whonix/usr/share/version for version number.

## VM Creation ##
,, -all not supported yet.

(1) Open a shell and type:

    sudo ~/whonix/whonix_build -tg

(2) Check if all went ok.

(3) Power on whonix_Gateway

(4) Open a shell and type:

    sudo ~/whonix/whonix_build -tw

The scripts can fail for many reasons, please report back any issues!

# Debugging #
**OPTIONAL** (Only in case something goes wrong or you want to audit or develop Whonix.)

## SSH into Whonix-Gateway ##

On Whonix-Gateway: Open /usr/local/bin/whonix_firewall

    sudo nano /usr/local/bin/whonix_firewall

Comment in the incoming SSH connection firewall rule.

    iptables -A INPUT -i "$EXT_IF" -p tcp --dport 22 -j ACCEPT

Restart firewall.

    /usr/local/bin/whonix_firewall

Inside Whonix-Workstation: 

    # Run once.
    sudo apt-get install opensshd-server

On the host: 
Add port forwarding from host into Virtual Machine.

    # Run once.
    VBoxManage modifyvm "Whonix-Gateway" --natpf1 "ssh",tcp,127.0.0.1,2222,,22

On the host: 
Open a ssh session.

    ssh user@127.0.0.1 -p 2222

    # Requires setting a root password beforehand.
    ssh root@127.0.0.1 -p 2222

On the host: 
Or mount Whonix-Gateway as a folder.

    sshfs user@127.0.0.1:/ -p 2222 /home/user/whonix_binary/whonix-Gateway_sshfs

    # Requires setting a root password beforehand.
    sshfs root@127.0.0.1:/ -p 2222 /home/user/whonix_binary/whonix-Gateway_sshfs

## Mount and inspect images and Whonixinstalllogs ##

    sudo ./whonix_createvm -tg-mount

    cd "/home/user/whonix_binary/whonix-Gateway_image"
    leafpad "/home/user/whonix_binary/whonix-Gateway_image/home/user/whonixinstalllog"
    cd ~

    sudo ./whonix_createvm -tg-unmount

.

    sudo ./whonix_createvm -tw-mount

    cd "/home/user/whonix_binary/whonix-Workstation_image"
    leafpad "/home/user/whonix_binary/whonix-Workstation_image/home/user/whonixinstalllog"
    cd ~

    sudo ./whonix_createvm -tw-unmount

# How to use the ova images #
Reboot both VMs. Please read the [Readme]!

# Final Steps (Only Required For Redistribution) #
* [LeakTests]!
* [Test] the images before release! TODO: Needs big revision with all Whonix features.
* Update the [Changelog].
* Create hash sums for verification.

    sha512sum Whonix-Gateway.ova
    sha512sum Whonix-Workstation.ova

* Upload the images.
* Post hash sums to build documentation.
* Post download links to build documentation.
* At least a few testers should test before posting a news. Testers may be found by posting a news.
* Finally announce: Post a news.

# Changelog Whonix 0.3.0 #
**UNFINISHED**

* Whonix-Gateway and Whonix-Workstation
    * Added Secure Distributed Network Time Synchronization. Thanks to the Tails developers for their fine, free and Open Source tails_htp!
    * Added timesync gui.
    * Deactivated Virtual Box time synchronization.
    * Deactivating Virtual Box guest additions time synchronization if they are installed.
    * Creating a snapshots by default
    * Rebranding, the project is now called Whonix.
    * Added BitCoin address for donations.
    * Added adrelanos's gpg key.
    * Improved GPG verification mechanism.
    * torcheck renamed to Whonixcheck
    * Greatly improved Whonixcheck, now checks Whonix version, SocksPort, TransPort, stream isolation, Tor Browser version, operating system version and network time synchronization.
    * Improved uwt, uwt -t server_type -i ip -p port <command> <options>....
* Whonix-Gateway
    * No no longer uses transparet proxying. Aos-Workstation can still use transparent proxying. Aos-Gateway now uses uwt for apt-get, gpg, ssh, (tails_)htpdate
    * Improved help file: Whonix.
    * Added unsafe user account, which can connect without Tor. Not used, unless user logs in as unsafe user.
    * Optional feature for /usr/local/bin/whonix_firewall, when commented out (disabled by default), root user can connect without Tor.
    * Now using stream isolation and uwt.
* Whonix-Workstation
    * Running every day Whonixcheck cron job hopefully fixes.
    * Partially fixed gnome-terminal black on black bug. Uses ugly colors and users are hopefully motivated to change the colors.
    * new commands:
        * xchat-reset (Deletes XChat configuration files and recreates the Whonix original ones, which are tweaked for privacy.)
        * hiddenserver-install (Installs and configures lighttpd)
* Source Code
    * Now hosted on github, https://github.com/adrelanos/whonix/ and therefore safe against malicious edits by random people.
    * All files are now inside their own files and no longer in single big scripts.
    * Deprecated onevm (no maintainer).
    * Deprecated uninstall and uninstall-vm (would require rewrite, was less tested, no users, we don't install the operating system manually anymore).
    * Error handling for everything.
    * Uwt wrappers share now most code.
    * Many fixes, more robustness, step based build system.

# Footer #
[[include ref=WikiFooter]]