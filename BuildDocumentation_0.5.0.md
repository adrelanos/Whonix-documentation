[[include ref=WikiHeader]]

[TOC]

# Introduction #
**This page reflects 0.5.6, the released and stable Whonix version! If you want to develop Whonix, rather get the latest, because the source code layout was heavily simplified.**

This page documents how the binary distribution images are built. If you have any questions or need help let us know on [Dev].

Following these instructions will build version Whonix 0.5.x based on Tor and Debian Wheezy.

Knowledge assumed: Virtualization and networking basic principles; operation of your platform; Linux knowledge: how to install Debian and basic command line knowledge.

Only one prerequisites: you need a working internet connection.

For discussion related to the development and build process of Whonix images go [Dev].

# Warning #
*/dev/mapper/loop0p1* (and */dev/nbd0*) (used for mounting the images) is hard coded inside Whonix build scripts. Beware if you are using such devices. It may conflict with TrueCrypt. (And possibly other tools relying on */dev/mapper/loop0p1* (and */dev/nbd0*).)

To avoid damage to your host system, it may be wise to build Whonix inside a Virtual Machine.

# Build Anonymity #
While downloading the required tools for building Whonix your internet service provider could if he want notice that you want to build Whonix. This is especially interesting, if you want to redistribute Whonix, but still want to stay anonymous. The full story can be read in the chapter [Build Anonymity](https://sourceforge.net/p/whonix/wiki/Build%20Anonymity/).

# Build Security #
Especially, but not exclusively, if you want to distribute Whonix images, you should improve the security of your build environment.

* Build on a dedicated build system, install security updates... ([Security Guide])
* All install media and all downloaded/used code must be verified (including all software on the host).
* Hashes, fingerprints  in the scripts and the wiki is not to be trusted. Verify everything.
* Read [Trust].

# Host preparation #
## Building on Linux ##
It is recommend to set your terminal (for example Konsole) to unlimited scrollback, so you can watch the full creation log.

You need to use **Debian**. (How to obtain Debian safely: [Debian ISO gpg verification](https://sourceforge.net/p/whonix/wiki/Debian/))

The build scripts could be adapted to run on other *NIX systems as well but currently they assume apt-get and grml-debootstrap to be available. You need about 15 GB of free space.

Become root.

    su

Update package lists and upgrade.

    apt-get update && sudo apt-get dist-upgrade

Install build dependencies.

    apt-get install virtualbox qemu apt-cacher-ng grml-debootstrap parted kpartx debootstrap mksh dialog git sudo equivs rsync

Add user to sudo group.

    addgroup user sudo

Reboot.

    reboot

## Building on Windows ##
Building Whonix directly on Windows is no longer supported. Redistributed Whonix builds should be build on Linux. If you want to port the Whonix build scripts to Windows, please [Contact] us. Running Whonix on a Windows host with Virtual Box installed and building Whonix inside a Virtual Machine with a Linux guest on a Windows host is still possible.

## Using an apt cache to speed up downloading ##
If you want to build multiple times (for debugging etc.), it makes sense to install a local apt proxy on your build machine. ^1^ That safes download time and traffic. ^2^ If you build Whonix on Whonix, apt-cacher-ng will go through Tor's TransPort.

<font size="-3">
,,
^1^ Thanks to [source](https://linuxexpresso.wordpress.com/2011/02/13/howto-apt-cacher-ng-on-ubuntu/).
^2^ It would be possible to download without an apt-cacher. But why? If you want to ignore it, ignore this chapter and change the mirror settings in grml configuration file.
</font>

If you build inside Whonix-Workstation, disable the apt-get uwt wrapper.

    sudo chmod -x /usr/local/bin/apt-get

Open */etc/apt/apt.conf*.

    sudo nano /etc/apt/apt.conf

Add the following.

    ## /etc/apt/apt.conf
    Acquire::http { Proxy "http://127.0.0.1:3142"; };

Restart apt-cacher-ng. Should not be required, but it was for me.

    sudo service apt-cacher-ng restart

Safe and test if it's working.

    sudo apt-get update

Should there ever be a problem with apt-cacher-ng (package verification failure) (rare cases), use this.

    #sudo apt-get update
    #sudo apt-get autoremove
    #sudo apt-get dist-upgrade
    #sudo apt-get clean
    #sudo apt-get autoclean

# Source Code Intro #
## Introduction ##
This chapter is dedicated to give an introduction into the Whonix source code. **If you prefer to read and understand the source code just by reading scripts you may skip this optional chapter.** When you like to mess with the source code, it would probable help a lot if you at least knew what **.img**, **.vdi**, **.vmdk** and **.ova** are being used for.

Moved to [Dev_SourceCodeIntro_0.5.0].

# Build as user "user" #
Log in as "*user*".

<font size="-3">
This is because the build script is far from perfect. The username "*user*" and */home/user/Whonix* is hardcoded and expected as source folder. Bug: [no longer hardcode user folder](https://trac.torproject.org/projects/tor/wiki/doc/TorBOX/Dev#SOURCECODEnolongerhardcodeuserfolder)
</font>

## gpg keys ##
gpg keys for required for build Whonix are stored inside */home/user/Whonix/whonix_shared/usr/local/share/whonix/*. These include.

* adrelanos.asc - Whonix maintainer key - used for [whonixcheck] news verification
* erinn.asc - [obtained from torproject.org](https://www.torproject.org/docs/signing-keys.html.en) - Used to verify downloads of Tor Browser by *whonix_workstation/usr/local/bin/torbrowser*.
* sebastian.asc - same as erinn.asc.

To find out what the keys are good for, simply grep the source code.

    cd /home/user/Whonix
    grep -r adrelanos.asc *
    grep -r erinn.asc *
    grep -r sebastian.asc *

If you are in luck, you never have to update the keys yourself and the Whonix maintainer will keep it updated. Otherwise and also as a good precaution you can verify these keys manually. Follow the instructions form torproject.org to obtain the key. Then simply check if the keys match or update the old key with the new one.

## Rebuilding Debian packages ##
Should not be necessary. The package is already ready.

Currently only the [DummyTor] package. Documenting for the sake of completeness.

    cd /home/user/Whonix/whonix_workstation/usr/local/share/whonix/dummytor/
    rm tor_1.0_all.deb
    ./dummytor
    cd /home/user/Whonix/

# Get the Whonix source code #

    git clone https://github.com/adrelanos/Whonix

# Verify the Whonix source code with gpg #
This is recommend but not required. See [Trust].

(1) [Learn about Whonix signing key.](https://sourceforge.net/p/whonix/wiki/TrustingWhonixSigningKey/).

(2) Get a list of available git tags.

    git tag

(3) Verify the tag you want to build.

    ## Replace with tag you want to build.
    git tag -v 0.5.6

(4) Output should look like the following.

    object 13870efc29018065267788f9f23026e6ff489684
    type commit
    tag 0.5.6
    tagger adrelanos <adrelanos at riseup dot net> 1348681401 -0400

    0.5.6
    gpg: Signature made Wed Sep 26 17:43:26 2012 UTC using RSA key ID 713AAEEF
    gpg: Good signature from "adrelanos <adrelanos at riseup dot net"

The warning.

    gpg: WARNING: This key is not certified with a trusted signature!
    gpg:          There is no indication that the signature belongs to the owner.


(1.1) Get into the correct [git branch](https://sourceforge.net/p/whonix/wiki/Dev_git/).

    ## 0.5.6
    git checkout 0.5.6

    ## For stable hotfixes.
    #git checkout stable

    ## In case you want to use the development branch.
    #git checkout devel

    ## In case you want to use the bleeding edge and help with development.
    #git checkout untested_adre

Is explained on the [Whonix signing key](https://sourceforge.net/p/whonix/wiki/TrustingWhonixSigningKey/) page and can be ignored.

# Create the Images #
## Preparations ##
(1) Git checkout, which version you want to build.

    git checkout 0.5.6

(2) Make sure there aren't any VMs in Virtual Box already called "Whonix-Gateway" or "Whonix-Workstation" (TODO: automate that)

(3) Check if /home/user/Whonix/usr/share/version for version number.

## VM Creation ##
(1) Open a shell and type:

    sudo ~/Whonix/whonix_build -all

(2) Check if all went ok.

The scripts can fail for many reasons, please report back any issues!

# Debugging #
**OPTIONAL** (Only in case something goes wrong or you want to audit or develop Whonix.)

* [SSH into Whonix-Gateway](https://sourceforge.net/p/whonix/wiki/File%20Transfer/#ssh-into-whonix-gateway)
* [Mount and inspect images](https://sourceforge.net/p/whonix/wiki/File%20Transfer/#mount-and-inspect-images)

* Rebuild the .ova images, while skipping the -tX-createimg step.

The "*sudo ./whonix_createvm -tX-createimg*" step takes far most of the build creation time. As long as no packages have been added or removed, you can repeat all other steps from a backup, which has been automatically created for you, by using.

    sudo ./whonix_build -fast

* Interactively chroot Whonix-Gateway.

Open a bash shell inside the Whonix-Gateway **.img** image.

    sudo ./whonix_createvm -tg-interactive

* Interactively chroot Whonix-Workstation.

Open a bash shell inside the Whonix-Workstation **.img** image.

    sudo ./whonix_createvm -tw-interactive

# How to use the ova images #
Reboot both VMs. Please read the [Documentation]!

# Final Steps (Only Required For Redistribution) #
## apt.conf ##
What is */usr/local/share/whonix/apt.conf* good for?

This apt.conf is only used inside chroot and currently only in effect for "*./whonix_createvm -tg-source*" and "*./whonix_createvm -tg-source*".

It points to *http://192.168.0.2:3142*, which is expected to be a Whonix-Workstation with apt-cacher-ng running. It's useful for running "*apt-get install*" and "*apt-get source*" inside chroot, because downloads are cached, which speeds up the build process when building several times in a row. (Debugging with only minor changes.)

In case you don't want to use it or to use another proxy, edit */home/user/Whonix/whonix_shared/usr/local/share/whonix/apt.conf* (comment out with a # or change proxy settings). Don't forget ./whonix_createvm -tX-copyinto-pre after modifying the file.

## other ##
See [Release Folder](https://github.com/adrelanos/Whonix/tree/development/release) in Whonix source code.

* Don't forget to update Whonix version number.
* [LeakTests]!
* [Test] the images before release! TODO: Needs big revision with all Whonix features.
* See if [Documentation] still makes sense.
* Update the [Changelog].
* See https://github.com/adrelanos/Whonix/blob/master/release/whonix_release

* Source Code

Whonix-Gateway

    sudo ./whonix_createvm -tg-source

Whonix-Workstation

    sudo ./whonix_createvm -tw-source

Pack. Upload.

* Upload the images.
* At least a few testers should test before posting a news. Testers may be found by posting a news.
* Check, if [ManualTBupdate] is still up to date.
* Update [Download].
* Update [PhysicalIsolation].
* Update [BuildDocumentation].
* Update [Features].
* Update [sf.net project page](http://sourceforge.net/projects/whonix/).
* Update sf.net default download.
* New documentation from [Next].
* Finally announce: Post a news.

    * In Whonix Important and Feature Blog.

    * http://lists.debian.org/debian-derivatives/
        * debian-derivatives@lists.debian.org

    * https://lists.torproject.org/pipermail/tor-talk/
        * tor-talk@lists.torproject.org

    * https://lists.sourceforge.net/lists/listinfo/whonix-devel
        * whonix-devel@lists.sourceforge.net

    * full-disclosure@lists.grok.org.uk

    * https://mailman.stanford.edu/mailman/listinfo/liberationtech
        * liberationtech@lists.stanford.edu

# Footer #
[[include ref=WikiFooter]