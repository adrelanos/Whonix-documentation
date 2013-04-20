[[include ref=WikiHeader]]

[TOC]

# VirtualBox Guest Additions #
## Warning ##
**Warning: Not recommend!**

 * **Weakens security in general as per [Security Guide] (Harden Virtualbox).**
 * Also see article, [The VirtualBox Kernel Driver Is Tainted Crap](http://www.phoronix.com/scan.php?page=news_item&px=OTk5Mw) ([w](...)).
 * **Additionally they give the Virtual Machine access the the host's (built-in) microphone. Many notebooks have a built-in microphone. In case you install Guest Additions anyway, better cover it up or remove your microphone.**
 * **Disable clipboard sharing!** It is already disabled by default since Whonix 0.5.5. Enable it only temporarily in case you really need it. Go to Virtual Box machine settings -> General -> Advanced -> Shared Clipboard -> Disable -> ok.

## Installing VirtualBox Guest Additions ##
### New Instructions for Debian Wheezy ###
Very simple.

[Searching](http://packages.debian.org/search?searchon=names&keywords=virtualbox) for Debian packages containing Virtual Box was a wise thing. In past it was sometimes a real pain to install the guest additions. The search brought up, that honorable people created a debian package with the tools. Simply do:

    sudo apt-get update && sudo apt-get dist-upgrade

Followed by.

    ## If you only want Shared Folder, for improved security,
    ## you can try using only the next line, but not the line after next.
    sudo apt-get install --no-install-recommends virtualbox-guest-dkms virtualbox-guest-utils

    ## If you want all features, such as dynamic resolution
    ## and mouse integration.
    sudo apt-get install virtualbox-guest-x11

Reboot. And you're done.

Alternatively, if this fails, you could also refer to the upstream documentation, [Virtual Box: Chapter 4. Guest Additions](https://www.virtualbox.org/manual/ch04.html).

### Old instructions for Ubuntu Precise ###
Moved to [Guest additions for Ubuntu Precise](https://sourceforge.net/p/whonix/wiki/Ubuntu/#guest-additions-for-ubuntu).

## Shared Folder ##
And if you want to use the shared folder read ahead... Go to VirtualBox -> machine -> change -> shared folder -> choose a folder -> use folder name **shared**. Choose mount automatically and create permanently. Press ok. Use the following commands to mount to folder.

    sudo mkdir -p /mnt/shared
    sudo chmod 777 /mnt/shared
    sudo mount -t vboxsf -o uid=1000,gid=1000 shared /mnt/shared

<font size="-3">
If you run into a **Protocol Error** try using a different name, do not use *share*, use something else, anything, for example, **shared**.
</font>

### Permanently mount Shared Folder ###
After reboot, you have to repeat the mount command. If you want to mount the folder automatically, have a look at the [source](https://help.ubuntu.com/community/VirtualBox/SharedFolders) of that information or simply add **before** *exit 0* in your /etc/rc.local:

    sudo mount -t vboxsf -o uid=1000,gid=1000 shared /mnt/shared

## Temporary disable Guest Additions ##
**This solution is incomplete!** In case you want to temporarily disable Virtual Box guest additions, you can try this. A safer solution would be to uninstall them.

Find out which Virtual box kernel modules are load.

    cat /proc/modules | grep vbox

Create a new config file for module blacklisting.

    sudo nano /etc/modprobe.d/vbox.conf

And add:

    blacklist vboxvideo
    blacklist vboxsf
    blacklist vboxguest

Safe and reboot. Done.

# Footer #
[[include ref=WikiFooter]]