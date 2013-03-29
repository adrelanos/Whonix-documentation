[Whonix Homepage](https://sourceforge.net/p/whonix/wiki/Home/)

[TOC]

    # Version: Whonix 0.2.1

    # Copyright: adrelanos (aka proper)
    #
    # License: GPL v3 or any later
    #
    # Any changes you pull changes into this source will be also licensed
    # under GPL v3 or any later. Additionally you grant proper the right to
    # re-license your work under a different license. If that is not acceptable,
    # you can either fork this source under GPL v3 or any later or contact proper.
    # Contact proper, if you require this source code under different license.

This page documents how the [Download binary distribution images] are built. If you have any questions or need help let us know on [Dev#Questions /Whonix/Dev#Question].

The scripts used to build a certain version of a Whonix-Gateway or Whonix-Workstation image can be found in the VM at /usr/share/doc/torbox (in TorBox 0.2 at /usr/local/bin/tor-*) and through the wiki history.

Following these instructions will build version Whonix 0.2.1 based on Tor 0.2.3 and Ubuntu Precise.

Knowledge assumed: Virtualization and networking basic principles; operation of your platform; Linux knowledge: how to install Ubuntu and basic command line knowledge.

Only one prerequisites: you need a working internet connection.

For discussion related to the development and build process of Whonix images go [Dev/ Whonix/Dev/].

# Build Anonymity #
While downloading the required tools for building Whonix your internet service provider could if he want notice that you want to build Whonix. This is esspecially interesting, if you want to redistribute Whonix, but still want to stay anonymous. The full story can be read in the chapter [SecurityAndHardening#BuildAnonymity Build Anonymity].

# Build Security #
* Build on a dedicated build system, install security updates...
* All install media and all downloaded/used code must be verified (including all software on the host).
* Hashes or fingerprints listed on the wiki are not to be trusted, same goes for the scripts, verify them (and make use of the history feature).
* Read [Trust Whonix/Trust]

# Host preparation #
**Read and apply if necessary [Readme#NetworkTimeSyncing "Network Time Syncing"]!

We recommend you use a dedicated OS installation just for hosting the Whonix VMs (See [SecurityAndHardening Whonix/SecurityAndHardening])

You need to use Ubuntu. The build scripts could be adapted to run on other*NIX systems as well but currently they assume apt-get to be available. You need about 15 GB of free space.

Install the latest security updates, install VirtualBox (and qemu-kvm which is required to mount the Virtual Box .vdi images). Reboot to apply kernel updates.

    sudo apt-get update && sudo apt-get dist-upgrade
    sudo apt-get install virtualbox qemu genisoimage
    sudo reboot

If you are going to use Virtual Box inside Virtual Box, be sure to change your host key. Virtual Box -> Preferences -> Input -> Host Key. The "outside" and the "inside" Host Key must differ, otherwise you can not leave the VM "inside" anymore. The "outside" Virtual Box hostkey may NOT be**ctrl**.^1^ 
,, ^1^ Because the one is used by VBoxSDL "inside".

Building on Windows is no longer supported. Redistributed Whonix builds should be build on Linux. If you want to port the Whonix build scripts to Windows, please contact us. Running Whonix on a Windows host with Virtual Box installed should still be possible.

## Using an apt cacher to speed up downloading ##
**OPTIONAL**

Does only work with Whonix-Gateway.
,, Does not work for Whonix-Workstation because it never gets direct access to the host by design. We could think about installing apt-cacher-ng on Whonix-Gateway, if there are any security implications.

Go to Whonix_Gateway script and comment in the line**Acquire::http { Proxy "http://192.168.0.2:3142"; };**, i.e. remove the # (hash) in front of it.

If you want to build multiple times (for debugging etc.), it might make sense to install a local apt proxy on your build machine. That safes download time and traffic. ,,Thanks to [https://linuxexpresso.wordpress.com/2011/02/13/howto-apt-cacher-ng-on-ubuntu/ source].

    sudo apt-get install apt-cacher-ng


    sudo nano /etc/apt/apt.conf


    Acquire::http { Proxy "http://127.0.0.1:3142"; };


    sudo apt-get update


# Source Code Intro #
**If you prefer to read and understand the source code just by reading scripts you may skip this optional chapter.** This chapter is dedicated to give an introduction into the Whonix source code. It can be quite difficult to get started with hacking existing big complex projects.

**Whonix_Build** is a script, which simply runs all other scripts. Actually it's "optional". It has very little functionality beside running all other scripts. You are free to run all scripts one by one. That is useful for learning and for debugging purposes. In case you want to fix a bug or in case you want to upgrade the distribution or in case you want to switch the operating system or whatever you are better off running the steps manually. You can use the Build script as a reference for which steps have to be run in which order.

Ironically currently most scripts are used to create a virtual machine image, which contains the operating system and the either the Whonix_Gateway or the Whonix_Workstation script. Scripts needed for creation the virtual machine image are Whonix_GetISO, Whonix_ModifyISO, Whonix_CreateVM and Whonix_Image. GetISO downloads and verifies the operating system iso image.

ModifyISO mounts the downloaded iso image as read only, copies it, modifies the copied iso image by adding preseeding (unattended installation), unmounts the iso and finally creates preseed.iso, which contains the operating system installer disc modified not to require any user interaction while installing. This process already sets up lots of important privacy settings and other stuff, such as UTC timezone, hostname ubuntu, US language, username user and so on. (See [SecurityAndHardening Whonix/SecurityAndHardening] and the ModifyISO script itself for a list of all changes and why.) Preseed.iso is configured to power off itself when it's done installing so the Whonix_Build script can continue.

Whonix_CreateVM creates VirtualBox machines with all settings required for secure networking, devices, security settings. Which those settings are in details can be again read in Security And Hardening or the script itself. CreateVM is also responsible for starting virtual machines while building. That happens two times, the first time the operating system will be installed and the second time either the Whonix_Gateway or the Whonix_Workstation script will be installed.

Whonix_Image allow to mount the virtual hdd images. This is required because we have to somehow get the Whonix_Gateway or the Whonix_Workstation script into the virtual hdds, so we can install them. With Whonix 0.1.3 we used ssh, but that was suboptimal. ^1^**Image** also allows to copy the Whonix_Gateway or the Whonix_Workstation script to /usr/local/bin/ inside the virtual hdd images. It also adds autostarting them only once as soon as the virtual machine gets started next time. This is done by adding the script to /etc/rc.local. rc.local will look if the installer log exists and if that is so, the script will not be run again. rc.local will also power off the VM if the Whonix_Gateway or Whonix_Workstation script finished. ^2^

,, ^1^ It required manually installing an ssh server just for getting the script into the virtual hdds. Ok, that could also be done with preseed. But it involves weakening the isolation of the VM from the host. The MAC address of the host could be seen my the VM. 
,, ^2^ /etc/rc.local will be reverted by the Whonix_Gateway or the Whonix_Workstation script.

Whonix_Gateway or the Whonix_Workstation will transform the installed operating system into the Whonix-Gateway or into the Whonix-Workstation. They update the system, install security relevant software, install useful applications for an anonymous general purpose operating system, set up all relevant privacy and anonymity required settings, desktop manager etc.

Thus, given the nature of the build step orientated scripts, you can easily work on the the different aspects of Whonix. For example, once you have created a clean virtual machine with the operating system only, you can make a clone or snapshot, run either the Whonix_Gateway or the Whonix_Workstation script as often as you need to test your changes and if something goes wrong, go back to the clone or snapshot. You don't have to build everything from scratch again. ^3^

,, ^3^ For example, we could add the Whonix_Gateway or Whonix_Workstation script to the preseed.iso and let it run after installing. If something would go wrong, you would have to reinstall the whole operating system every time again. That's why we use separate steps.

The**torcheck** script will only be copied into Whonix-Workstation and is supposed to be run in Whonix-Workstation only. Checks network connection, Tor Browser version, SocksPort and TransPort IP and stream isolation.

# Get the Whonix source code #
Get all our scripts (currently 8) and save them in one folder, it's best to create a new folder called Whonix_src in your home directory. It is important that they are all named correctly!

Check the source code for error or malicious edits. Make use of the history feature of torproject.org's wiki.

"Whonix_Build" script 
https://trac.torproject.org/projects/tor/wiki/doc/Whonix/Dev/Build

"Whonix_GetISO" script 
https://trac.torproject.org/projects/tor/wiki/doc/Whonix/Dev/GetISO

"Whonix_ModifyISO" script 
https://trac.torproject.org/projects/tor/wiki/doc/Whonix/Dev/ModifyISO

"Whonix_CreateVM" script 
https://trac.torproject.org/projects/tor/wiki/doc/Whonix/Dev/CreateVM

"Whonix_Image" script 
https://trac.torproject.org/projects/tor/wiki/doc/Whonix/Dev/Image

"Whonix-Gateway" script 
https://trac.torproject.org/projects/tor/wiki/doc/Whonix/Dev/TGScript

"Whonix-Workstation" script 
https://trac.torproject.org/projects/tor/wiki/doc/Whonix/Dev/TWScript

"torcheck" script 
https://trac.torproject.org/projects/tor/wiki/doc/Whonix/Dev/torcheck

# Create the Images #
## Preparations ##
Make the build script executable: 

    chmod +x ~/Whonix_source/Whonix_*

Make sure there aren't any VMs in VirtualBox already called "Whonix-Gateway" or "Whonix-Workstation" (TODO: automate that)

## VM Creation ##
,, -all not supported yet.

(1). Open a shell and type:

    sudo ~/Whonix_source/Whonix_Build -tg

(2). Check if all went ok.

(3). Power on Whonix_Gateway

(4). Open a shell and type:

    sudo ~/Whonix_source/Whonix_Build -tw

The scripts can fail for many reasons, please report back any issues!

# How to use the ova images #
Reboot both VMs. Please read the [Readme Readme]!

# Final Steps (Only Required For Redistribution) #
* [LeakTests Leak Testing]!
* [TestAndTroubleshoot Test] the images before release! TODO: Needs big revision with all Whonix features.
* Update the [Changelog Changelog].
* Create hash sums for verification.

    sha512sum Whonix-Gateway.ova
    sha512sum Whonix-Workstation.ova

* Upload the images.
* Post hash sums to build documentation.
* Post download links to build documentation.
* At least a few testers should test before posting a news. Testers may be found by posting a news.
* Finally announce: Post a news.

# Footer #
[[include ref=WikiFooter]]