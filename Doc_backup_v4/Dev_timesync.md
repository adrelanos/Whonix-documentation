[[include ref=WikiHeader]]

[TOC]

# Introduction #

[tails_htp](https://tails.boum.org/contribute/design/Time_syncing/) has already been copied into Whonix. This file documents the steps done to copy it and implementation differences.

See also [Whonix's Secure And Distributed Time Synchronization Mechanism](https://sourceforge.net/p/whonix/wiki/Security/#whonixs-secure-and-distributed-time-synchronization-mechanism).

# Overview #

| | Tails | Whonix
| ------------- |  ------------- | -------------
| adduser htp | /chroot_local-hooks/06-adduser_htp | Done in [whonix_internal_install_script](https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/usr/local/bin/whonix_internal_install_script) (s).
| init script |/etc/init.d/htpdate | [/etc/init.d/htpdate](https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/init.d/htpdate) ^1^
| tails_htpdate configuration file | /etc/default/htpdate | [/etc/default/htpdate](https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/default/htpdate) ^6^
| tails_htpdate binary | /usr/local/sbin/htpdate	| [/usr/local/sbin/htpdate](https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/sbin/htpdate) ^7^
| anachron script |Not used in Tails. | [/etc/cron.hourly/htpdate](https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/cron.hourly/htpdate) ^2^
| anachron helper delay script |Not used in Tails. | [/usr/local/bin/htpdate_hourly](https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/bin/htpdate_hourly) ^3^
| timesync gui |Not used in Tails. | [/usr/local/bin/timesync](https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/bin/timesync) ^4^
| /etc/init.d/htpdate sudoers exception | Not used in Tails. | [/etc/sudoers](https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/appendto_sudoers) ^5^

Whonix changes:

* ^1^ Deactivates Virtual Box guest additions time sync; socks proxy IP and port adapted for Whonix.
* ^2^ Minimal script which simply runs */usr/local/bin/htpdate_hourly*. The delay isn't done in this script, since this would make anachron wait until it's done.
* ^3^ Runs htpdate every hour at a random minute.
* ^4^ Optional graphical user interface.
* ^5^ Allows running *sudo /etc/init.d/htpdate* without a password.
* ^6^ See bottom of this page.
* ^7^ Uses */usr/bin/curl* instead of *curl* to circumvent uwt wrapper, because htpdate uses socks settings.

# How tails_htp was initially imported into Whonix #

    # Get the Tails signing key:
    # https://tails.boum.org/doc/about/openpgp_keys/index.en.html
    #
    # https://tails.boum.org/contribute/git/
    git clone git://git.immerda.ch/amnesia.git
    cd amnesia
    git tag -v 0.12

    # Alternatively it's also possible to download Tail's CD and to unpack it.
    # sudo unsquashfs -x -dest /home/user/b filesystem.squashfs

.

    # /amnesia/config/chroot_local-packageslists/tails-common.list contains a list of all Tails dependencies.
    # Seach for "needed by htpdate". You'll see tails_htp depends on the following packages.
    libdatetime-perl libdatetime-format-dateparse-perl libgetopt-long-descriptive-perl libtry-tiny-perl

.

    # adduser htp
    /home/user/amnesia/config/chroot_local-hooks/06-adduser_htp
    # Has been added to whonix_internal_install_script(s).

    # We need tails_htpdate, the actual binary.
    cp /home/user/amnesia/config/chroot_local-includes/usr/local/sbin/htpdate /home/user/whonix/whonix_shared/usr/bin/htpdate

.

    # Init script.
    mkdir -p /home/user/whonix/whonix_shared/etc/init.d/
    cp /home/user/amnesia/config/chroot_local-includes/etc/init.d/htpdate /home/user/whonix/whonix_shared/etc/init.d/htpdate
    # got added by whonix_internal_install_script: update-rc.d htpdate defaults

.

    # Copy server pool for tails_htp.
    cp /home/user/amnesia/config/chroot_local-includes/etc/default/htpdate /home/user/whonix/whonix_shared/etc/default/htpdate

.

    # The server pool /etc/default/htpdate contains a line:
    # config/chroot_local-includes/usr/local/bin/getTorbuttonUserAgent
    #
    # Will not be used in Whonix, since there is also no Ubuntu package with Tor Button.
    # Open Tor Browser about:config and search for "useragent_override", copy the value.
    # Manually add to /home/user/whonix/whonix_shared/etc/default/htpdate
    # Replace
    HTTP_USER_AGENT="$(/usr/local/bin/getTorbuttonUserAgent)"
    # with
    #HTTP_USER_AGENT="$(/usr/local/bin/getTorbuttonUserAgent)"
    HTTP_USER_AGENT="Mozilla/5.0 (Windows NT 6.1; rv:10.0) Gecko/20100101 Firefox/10.0"

# Long Term Plan #
Rename tails_htp to sdwdate and get it into Debian.

Repository created:

* https://github.com/adrelanos/sdwdate

**Help welcome!**

# Footer #
[[include ref=WikiFooter]]