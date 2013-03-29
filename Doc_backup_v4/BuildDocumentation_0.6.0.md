[[include ref=WikiHeader]]

[TOC]

# Introduction #
This page documents how to build Whonix Virtual Box images. If you have any questions or need help, get in [Contact].

Knowledge assumed: Virtualization basic principles; operation of your platform; Linux knowledge: how to install Debian and basic command line knowledge.

Only one prerequisites: you need a working internet connection.

For discussion related to the development and build process of Whonix images get in [Contact].

How to use the resulting images, is documented in the [Documentation].

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
It is recommend to set your terminal (for example Konsole) to unlimited scrollback, so you can watch the full build log.

You need to build on **Debian**. <font size ="-3">(How to obtain Debian safely: [Debian ISO gpg verification](https://sourceforge.net/p/whonix/wiki/Debian/))</font>

The build scripts could be adapted to run on other *NIX systems as well but currently they assume apt-get and grml-debootstrap to be available. You need about 15 GB of free space.

<font size ="-3">
(Build dependencies and configurations get automatically applied by *[build-steps/15_prepare-build-machine](https://github.com/adrelanos/Whonix/blob/development/build-steps/15_prepare-build-machine)*, so you don't have to worry about that.)
</font>

# Introduction into Whonix Source Code #
This chapter is dedicated to give an introduction into the Whonix source code. **If you prefer to read and understand the source code just by reading scripts you may skip this optional chapter.** When you like to mess with the source code, it would probable help a lot if you at least knew what **.img**, **.vdi**, **.vmdk** and **.ova** are being used for. See [Dev_SourceCodeIntro].

# Get the Whonix Source Code #
Install git.

    sudo apt-get install git

Get the Whonix source code.

    git clone https://github.com/adrelanos/Whonix

# Get adrelanos's PGP Public Key #
This chapter is recommend for better security, but not strictly required. <font size=-3>(See [Trust].)</font>

(1) Get into Whonix source folder.

    cd Whonix

(2) Import the key.

    gpg --import adrelanos.asc

(4) Verify.

    gpg --fingerprint 9B157153925C303A42253AFB9C131AD3713AAEEF

Should show.

    pub   4096R/713AAEEF 2012-03-02
          Key fingerprint = 9B15 7153 925C 303A 4225  3AFB 9C13 1AD3 713A AEEF
    uid                  adrelanos <adrelanos at riseup dot net>
    sub   4096R/794279C4 2012-03-02

For even better security, [learn about Whonix signing key](https://sourceforge.net/p/whonix/wiki/TrustingWhonixSigningKey/).

# Verify the Whonix Souce Code #
This chapter is recommend for better security, but not strictly required. <font size=-3>(See [Trust].)</font>

(1) Get a list of available git tags.

    git tag

(2) Verify the tag you want to build.

    ## Replace with tag you want to build.
    git tag -v 0.6.0

(3) Output should look like the following.

    object 13870efc29018065267788f9f23026e6ff489684
    type commit
    tag 0.6.0
    tagger adrelanos <adrelanos at riseup dot net> 1348681401 -0400

    0.6.0
    gpg: Signature made Wed Sep 26 17:43:26 2012 UTC using RSA key ID 713AAEEF
    gpg: Good signature from "adrelanos <adrelanos at riseup dot net"

The warning.

    gpg: WARNING: This key is not certified with a trusted signature!
    gpg:          There is no indication that the signature belongs to the owner.

Is explained on the [Whonix signing key](https://sourceforge.net/p/whonix/wiki/TrustingWhonixSigningKey/) page and can be ignored.

# Create the Images #
## Preparations ##
(1) Git checkout, which version or [git branch](https://sourceforge.net/p/whonix/wiki/Dev_git/) you want to build

    ## 0.6.0
    #git checkout 0.6.0

    ## For stable including hotfixes.
    ## (If there is no git tag yet.)
    #git checkout stable

    ## In case you want to use the development branch.
    #git checkout development

(2) Make sure there aren't any VMs in Virtual Box already called "Whonix-Gateway" or "Whonix-Workstation" - any VMs with such a name get deleted!

## VM Creation ##
(1) Open a shell and type:

    sudo ~/Whonix/whonix_build -all

(2) Check if all went ok.

The scripts can fail for many reasons, please report back any issues!

# Debugging #
**OPTIONAL** (Only in case something goes wrong or if you want to audit or develop Whonix.)

See [Debugging](https://sourceforge.net/p/whonix/wiki/Dev_SourceCodeIntro/#debugging).

# Final Steps #
**Only Required For Redistribution.** See [Dev_Redistribution].

# Footer #
[[include ref=WikiFooter]]