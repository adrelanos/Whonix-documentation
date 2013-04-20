[[include ref=WikiHeader]]

[TOC]

# Download and Verification #
The recommend way to verify the Debian Signing key is to use the [web of trust](https://sourceforge.net/p/whonix/wiki/OpenPGP/), which is more secure, but not available to everyone.

This chapter documents an alternative and supplementary way to verify the Debian Signing key using an existing installation such as Ubuntu, which is already trusted, for example because you bought it from a reseller or got it from a friend who verified it.

**Should work for Debian and any Debian derivative.**

(1) Go to the [Debian Download Page](http://cdimage.debian.org/cdimage/wheezy_di_rc1/). Example, the [Debian Wheezy DVD i386 folder](http://cdimage.debian.org/cdimage/wheezy_di_rc1/i386/iso-dvd/).

(2) Download.

* SHA512SUMS
* SHA512SUMS.sign 
* DVD-1.iso

(3) Install the debian-keyring package, which contains the signing key. This is because the the [Debian Verify](http://www.debian.org/CD/verify) instructions are not accessible over SSL, neither the debian-keyring package can be downloaded over SSL. Downloading the debian-keyring package from the repository, lets apt-get verify it's integrity.

    sudo apt-get install debian-keyring

(4) Open a terminal and get into the folder where you downloaded SHA512SUMS and SHA512SUMS.sign (and DVD-1.iso).

(5) Verify the SHA512SUMS file.

    gpg --no-default-keyring --keyring /usr/share/keyrings/debian-role-keys.gpg --verify SHA512SUMS.sign

(6) Must show.

    gpg: Good signature

Otherwise something is wrong.

This might be followed by a warning saying:

    gpg: WARNING: This key is not certified with a trusted signature!
    gpg:          There is no indication that the signature belongs to the owner.

This doesn't alter the validity of the signature according to the key you downloaded. This warning rather has to do with the trust that you put in key.

(7) Done.

# Install
** UNFINISHED! **

From usability perspective, [you should always have a network connection when installing Debian](http://raphaelhertzog.com/2011/06/13/why-you-should-always-have-a-network-connection-when-installing-debian/).

From security perspective, [you should not plug to the Internet until ready](http://www.debian.org/doc/manuals/securing-debian-howto/ch3.en.html#s3.3).

You may have noticed, the default desktop environment for Whonix's Virtual Machines is KDE. (You could change that.) It doesn't matter, which desktop environment you are going to use for Debian. The default desktop environment of Debian is GNOME. If you are already accustomed to Whonix (KDE), you could also use KDE for your Debian host as well (not a must).

    Debian boot menu -> Advanced Options -> Alternative Desktop Environments ->
    Feel free to choose:
    - KDE
    - XDE
    - XFCE

It's also possible to install another desktop environment after installing or to switch from one to another.

If you are wondering what the "default", "notebook" or "standard" packages are about, see [tasksel](http://wiki.debian.org/tasksel).

Check open ports.

    su
    netstat -anltp | grep "LISTEN"

Must should be none, i.e no reply.

Remove services, which open ports. ^1^

    su
    apt-get remove dovecot-core openbsd-inetd bind9 samba cups apache2 postgres* 
    apt-get remove exim4 exim4-daemon-light rpcbind openssh-server apache2.2-bin
    apt-get autoremove

Check open ports again.

    su
    netstat -anltp | grep "LISTEN"

Must should be none, i.e no reply.

https://github.com/adrelanos/Whonix/blob/stable/host/whonix_firewall


<font size="-3">
,,
^1^ For documentation purposes I made a Debian installation and installed as much services with taskel as possible, while having a network connection. (Simulating user misunderstanding.) A Debian default installation with default setting does not install all those packages.
</font>

# Security

[Quote](http://www.debian.org/doc/manuals/securing-debian-howto/ch12.en.html):

> *Is Debian more secure than X?*
>
> *A system is only as secure as its administrator is capable of making it. Debian's default installation of services aims to be secure, but may not be as paranoid as some other operating systems which install all services disabled by default.*

I am not sure if they are referring to running services after installing them or having no services running (open ports) after a default installation with default settings. Debian doesn't do the latter, which is a pity.

Don't participate in popularity contest.

Some useful links. Parts of it are outdated (old Debian versions). Some stuff doesn't apply to Whonix host's.

* [Securing Debian Manual](http://www.debian.org/doc/manuals/securing-debian-howto)
* [Securing Debian Manual
Chapter 12 - Frequently asked Questions (FAQ)](http://www.debian.org/doc/manuals/securing-debian-howto/ch12.en.html)
* [Towards a moderately paranoid Debian laptop setup (not only useful for laptops)](http://www.hermann-uwe.de/blog/towards-a-moderately-paranoid-debian-laptop-setup--part-1-base-system)

# Footer #
[[include ref=WikiFooter]]