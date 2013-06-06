[[include ref=WikiHeader]]

[TOC]

# Tuning #
## Introduction ##
**Everything absolutely optional. Mostly largely untested!**

At the top of the *Tuning chapter* are the easier tuning steps. The farther you go down, the more skill will be required.

## Increase Virtual Machine RAM ##
If [less important identifiers](https://sourceforge.net/p/whonix/wiki/Whonix%27s%20Protocol-Leak-Protection%20and%20Fingerprinting-Protection/#less-important-identifies) are not important to you, and this is most likely is very unimportant, you could use Virtual Box settings and increase the RAM for you Virtual Machine(s). Whonix-Workstation will profit most, if you run into low RAM. Also Whonix-Gateway could profit if you are creating big numbers of circuits and keep Tor busy. You can check how much RAM is free using *free -m* in Terminal.

## More CPU cores ##
On systems with multi-core processors, if [less important identifiers](https://sourceforge.net/p/whonix/wiki/Whonix%27s%20Protocol-Leak-Protection%20and%20Fingerprinting-Protection/#less-important-identifies) are not important to you, and this is most likely is unimportant, you could increase the number of cores available to the Virtual Machine(s) in Virtual Box settings.

## Removing packages ##
For example you could experiment with uninstalling Nepomuk and virtuoso.

## Replacing desktop environment ##
You could even uninstall KDE and use your own desktop environment or only cli.

## Synthetic CPU ##
If [less important identifiers](https://sourceforge.net/p/whonix/wiki/Whonix%27s%20Protocol-Leak-Protection%20and%20Fingerprinting-Protection/#less-important-identifies) are not important to you, you could try if deactivating the Synthetic CPU increases performance for you.

    sudo -u $USERNAME VBoxManage modifyvm "Whonix-Workstation" --synthcpu off
    sudo -u $USERNAME VBoxManage modifyvm "Whonix-Gateway" --synthcpu off

## Nested paging and VPIDs ##
You could increase performance by using Nested paging and/or VPIDs. It is unknown, if that may decease security or stability. See Virtual Box manual: [Nested paging and VPIDs](http://www.virtualbox.org/manual/ch10.html#nestedpaging) for more information.

    vboxmanage modifyvm Whonix-Workstation --largepages on
    vboxmanage modifyvm Whonix-Gateway --largepages on

    vboxmanage modifyvm Whonix-Workstation --vtxvpid on
    vboxmanage modifyvm Whonix-Gateway --vtxvpid on

## Guest Additions ##
Not recommend for security reasons, but would improve performance, see [VirtualBox Guest Additions](https://sourceforge.net/p/whonix/wiki/VirtualBox%20Guest%20Additions/).

## Hardware-accelerated graphics ##
Requires Guest Additions, therefore not recommend, see above. Can increase performance.

See Virtual Box manual: [Hardware-accelerated graphics](https://www.virtualbox.org/manual/ch04.html#guestadd-3d).

## Memory ballooning, Page Fusion, Memory overcommitment ##
Requires Guest Additions, therefore not recommend, see above. Can increase performance.

See Virtual Box manual: [Memory overcommitment](https://www.virtualbox.org/manual/ch04.html#idp18673360).

## 64 bit architecture ##
Several methods. The last method is probable the most useful one.

Maybe it would enhance security and/or performance by using an amd64 kernel. I don't know how much sense that makes when the rest of the system is still 32 bit.

    sudo apt-get install linux-image-amd64

You could try to [Debian Multiarch HOWTO](http://wiki.debian.org/Multiarch/HOWTO).

Or better create amd64 [builds yourself from source](https://sourceforge.net/p/whonix/wiki/BuildDocumentation/). Just open the file *int_whonix_image* and look for *--arch i386* and replace *i386* with *amd64*. I believe that is all you need to build amd64 builds, but it is untested.

## Optimized builds ##
Since the the concept behind Whonix isn't tied to anything, you could create your own implementation. Perhaps using Gentoo with optimized build flags for your system. See [Whonix Framework](https://sourceforge.net/p/whonix/wiki/Technical%20Introduction/#whonix-framework), [OneVM] and [HardenedGentooTG].

## PCI passthrough
Might greatly improve graphics performance.; Might have security implications.

Essentially this feature allows to directly use physical PCI devices on the host by the guest even if host doesn't have drivers for this particular device. See Virtual Box Manual: [PCI passthrough](http://www.virtualbox.org/manual/ch09.html#pcipassthrough).

# Footer #
[[include ref=WikiFooter]]