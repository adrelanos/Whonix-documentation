[[include ref=WikiHeader]]

**WARNING**: Please don't forget reading the Warnings chapter.

[TOC]

# Introduction #
## Technical Introduction ##
When setting up Whonix in the form of two Virtual Machines running on the same physical host, exploits targeting the VM implementation or the host can still break out of the torified Client VM and expose the IP of a user. Malware running on the host has full control over all VMs. To protect such attacks we need a different approach: In this context we called it Physical Isolation, because the gateway system is installed on separate hardware. This drastically reduces the [TCB](https://en.wikipedia.org/wiki/Trusted_computing_base) by more than the half.

In total we'll be installing and configuring two computers and set up an isolated point to point network between them (you could also set up a an ordinary, completely isolated, LAN behind the Whonix-Gateway). One computer acts as the client or "Whonix-Workstation", the other as a proxy or "Whonix-Gateway" which will transparently route all of the Whonix-Workstation's traffic through Tor.

The Whonix-Gateway on its own physical device can either run directly on hardware or inside a virtual machine. Both options have advantages and disadvantages. We recommend to use no additional Virtual Machine for the Whonix-Gateway.

The Whonix-Workstation should always be installed in a Virtual Machine: A VM hides hardware serial numbers. See also [Recommendation to use multiple VM Snapshots](https://sourceforge.net/p/whonix/wiki/Security%20Guide/#recommendation-to-use-multiple-vm-snapshots).

The host operating system(s) should only be used for downloading operating system updating, hosting Whonix-Gateway or Whonix-Workstation and nothing else.

Bonus points if the physical systems are exclusively used for hosting Whonix, or if storage devices are separated for Whonix and non-Whonix use cases, to avoid a Whonix hard drive getting infected by a another operating system.

## Warnings ##
**WARNING**: Instructions for Whonix 0.5.6 with Physical Isolation are still under development. Advanced Linux users can already understand them. As recently [reported](http://sourceforge.net/p/whonix/discussion/general/thread/24115e26/) in the user help forum, they are working.

**WARNING**: [Build Anonymity](https://sourceforge.net/p/whonix/wiki/Build%20Anonymity/) has not been considered for this article.

**WARNING**: This article currently lacks information about Whonix-Gateway's and Whonix-Workstation's MAC address. See also

* [Whonix's Protocol-Leak-Protection and Fingerprinting-Protection](https://sourceforge.net/p/whonix/wiki/Whonix%27s%20Protocol-Leak-Protection%20and%20Fingerprinting-Protection/)
* [Whonix in public networks / MAC Address](https://sourceforge.net/p/whonix/wiki/Pre%20Install%20Advice/#mac-address)
* [Dev] Mac address in public networks.

## Using spare hardware + Virtual Machine ##
Advantages:

* You can install a graphical host.
* Use the Whonix download version.
* You can use the graphical network manager on the host, for example to connect to WiFi.
* You can setup easily a VPN on the host. Tor will be tunneled through the VPN.

Disadvantages:

* Higher attack surface, because the Virtual Machine code get's involved.

## Using spare hardware without Virtual Machine ##
Advantages:

* More secure, because less code is involved.

Disadvantages:

* Slightly more complicated setup
* More difficult to set up VPN
* More difficult to set up 3G networking compared to using a Windows host

## Hardware ##
### General ###
We recommend that you use two dedicated computers for Whonix that are never used for activities that could lead back to your identity. Alternatively you can use an already existing and otherwise used computer for the Whonix-Gateway. To offer some isolation you should disconnect all internal and external drives and boot from a eSATA, USB or another internal drive into a clean environment.

### non-anonymous use ###
* non-anonymous box (leave it as is is, like you want)
* non-anonymous home dial up internet router (leave it as is is, like you want)

### anonymous use ###
* Whonix-Gateway
    * This really does not have to be a big desktop computer or ordinary server. There are alternatives.
    * smartphone ^1^,
    * [UMPC](https://en.wikipedia.org/wiki/Ultra-mobile_PC)
    * pad, tablet,
    * notebook, netbook,
    * [Raspberry Pi](https://en.wikipedia.org/wiki/Raspberry_Pi)  (Whonix User Help Forum: [Installing Whonix Gateway on Raspberry Pi](https://sourceforge.net/p/whonix/discussion/general/thread/30381157/)),
    * router ^2^,
    * set top box,
    * etc.
    * how to utilize such a device as a linux server is beyond the scope of this guide, there are already better resources
* anonymous 3G modem (see below) or anonymous wifi adapter (see below)
* Whonix-Workstation
    * You get the idea. Use a device which suits you.^1^

<font size="-3">
,,
^1^ Just some hints to get started. It is difficult and beyond the scope of Whonix, because you don't have an Ethernet interface. Some (after market) firmwares support USB-host. (You can plug USB devices into your phone, such as an USB ethernet card. For example some rooted android smartphones can [install](http://android.galoula.com/en/LinuxInstall/) Debian Linux.
^2^ something like OpenWRT
</font>

# Prerequisites #
* Whonix-Gateway: A device with at least two network adapters, at least one of them ethernet^1^, capable of running Linux. It will run Debian.^2^
* Whonix-Workstation: A device connected via ethernet to the Whonix-Gateway. It must only have this one NIC and no other network connectivity! Must be connected by wire.^3^ This will be the torified client system or Whonix-Workstation. It must be capable of running Debian.^4^ 
* We recommend to use a VM as the client, the same Whonix-Workstation, that most non Physical Isolation users use. ^7^
* Whonix-Gateway is already read and started, host build environment has a working internet connection to Debian mirrors.

<font size="-3">
,,
^1^ The other one may be either an [Anonymous 3G modem](https://sourceforge.net/p/whonix/wiki/Security%20Guide/#anonymous-3g-modem); [Anonymous WiFi adapter](https://sourceforge.net/p/whonix/wiki/Security%20Guide/#anonymous-wifi-adapter), another ethernet or wifi connected to your modem/router.
^2^ Theoretically you could use any OS that supports iptables or pf. If you don't want to use Debian you will have to edit the source code. This will be easy for Debian derivatives but much more difficult for *BSD for example. In any case, the choice of OS shouldn't really matter because this system isn't used for anything but running Tor. A cheap plug computer, something like Raspberry Pi or the hardware used by Torouter would be sufficient.
^3^ If you don't connect by wire, you significantly weaken isolation and security. One the Whonix-Workstation were infected, it could jump onto another network and start leaking. 
^4^ Any OS can be used. But this is not recommended! If you do anyway, read warning, especially for Windows: [Transparent Proxy Leaks](https://trac.torproject.org/projects/tor/wiki/doc/TransparentProxyLeaks).
^5^ A generic VM image can neither leak identifying hardware serial numbers nor unique software fingerprints. (e.g. trough [software updates](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO#Softwareupdaters)).
^6^ This ensures that you get the latest security features and most secure configurations. (Such as stream isolation that protects against Identity correlation through circuit sharing, XChat IRC hardening or Whonix's Protocol-Leak-Protection and Fingerprinting-Protection etc.)
^7^ From the download page or build it yourself from source code.
</font>

# Installation #
## General ##
From [BuildDocumentation] general advice about Build Security and Host preparation apply.

## How To Install Whonix-Gateway on hardware (RECOMMENDED) ##
(0). Download a Debian Wheezy 32 bit installation iso. (You could also use a Debian Wheezy 64 bit installation iso, these instructions should also work, but it's less tested.) Detailed instructions doing so are unfortunately not part of this guide. However, the [Verify Debian ISO with GPG](https://sourceforge.net/p/whonix/wiki/Debian/) page contains some help.

(1). Install Debian Wheezy and chose following settings:

    In the boot menu press F4 and select "Install a minimal system"
    Language: English
    Country: United States
    keyboard layout: English (US) (don't autodetect)
    Primary network interface: eth0 (depends on hardware layout?)
    Hostname: host
    Full name for the new user: user
    Username for your account: user
    Choose a password for the new user: <Set up a strong password>
    encrypt home directory: No
    Timezone: UTC
    Partitioning: It's a good idea to set up cryptsetup based FDE at this point.
    No proxy
    No automatic updates 
    tasksel (Choose software to install): select nothing

(2). The external interface (usually eth0) may need to be configured according to the requirements of your local network, e.g. static or simply left to use dhcp if the gateway is connected to a dhcp capable router. For wlan follow the upstream documentations: [debian wiki](http://wiki.debian.org/WiFi), [Ubuntu help](https://help.ubuntu.com/community/WifiDocs/WiFiHowTo).

(3). Make sure the internet is working.

(4). Install all security updates and reboot.

    ## Become root.
    su

    ## Refresh package lists.
    apt-get update

    ## Upgrade.
    apt-get dist-upgrade

    ## Back to normal user.
    exit

(5). Install build dependencies. ^1^

    sudo apt-get install git sudo

<font size="-3">
,,
^1^ You need git to obtain the source code. Alternatively, you could also download a git tag as tar.gz archive using a (torified) browser: https://github.com/adrelanos/Whonix/tags
</font>

(6). You must build as user "user" and that user must be a member of the "sudo" group.

    ## Become root.
    su

    ## adduser "user"
    adduser user

    ## add "user" to sudo group
    addgroup user sudo

    ## Back to normal user.
    exit

(7). On your Whonix-Gateway: It is assumed you created user account named "user".

    su user
    cd ~

(8). Get latest source code. When 0.5.6 gets released there will be a signed release tag, if you wish a signed release tag of a snapshot in meanwhile please get in contact.

    git clone https://github.com/adrelanos/Whonix

(9). Get into Whonix source folder.

    cd Whonix

(10). Verify the git tag you want to use.

    ## 0.5.6 users
    git tag -v 0.5.6

    ## 0.6.1 testers only!
    #git tag -v 0.6.1

(11). Switch to the git tag you want to use.

    ## 0.5.6 users
    git checkout 0.5.6

    ## 0.6.1 testers only!
    #git checkout 0.6.1

(12). Make sure you have all packages installed which are listed in the file *Whonix-Gateway_packages*.

    ## If you are experimenting with 64 bit Whonix-Gateway,
    ## you will have to comment out the package linux-image-486
    ## in the file Whonix-Gateway_packages.
    apt-get install $(grep -vE "^\s*#" Whonix-Gateway_packages | tr "
" " ")

(13). Before running the whonix_createvm ^2^ script make sure eth1 and eth0 refer to the correct interfaces.

    ## May be helpful.
    dmesg | grep eth

Otherwise you have to change the variables in the configuration files. To find the affected files, the following commands may be helpful. ^3^

    grep -r eth0* *
    grep -r eth1* *

<font size="-3">
,,
^2^ Do not get concerned about the "vm" within whonix_createvm. The name is historically and the functionality for building an Whonix-Gateway featuring Physical Isolation has been added later. 
^3^ Should be really only a very few files. We used variables for eth0 and eth1 wherever possible.
</font>

(14). Most configuration files work well inside Virtual Machines and on hardware. Only minor things such as deactivating powersaving, passwordless reboot, shutdown etc. are only recommend for Virtual Machines. You can easily comment them out by putting a hash # in front of them. They are marked, to find them, grep can be used.

    grep -r VMONLY* *

(15). Copy the files from the Whonix source folder to their correct place.

    ## 0.5.6 users
    sudo ./whonix_createvm -tg-bare-metal

    ## 0.6.1 testers only!
    #./build-steps/30_copy-into-img -tg-bare-metal

(16). Start whonix_internal_install_script ("chroot" scripts).

    ## 0.5.6 users
    sudo /usr/local/share/whonix/whonix_internal_install_script -install

    ## 0.6.1 testers only!
    #sudo run-parts --verbose --test "/usr/local/share/whonix/chroot-scripts"
    #sudo run-parts --verbose --exit-on-error "/usr/local/share/whonix/chroot-scripts"

    ## adretemp40 (0.6.1.1) testers only!
    #sudo ./build-steps/35_run-chroot-scripts-img -tg-bare-metal

(17). Reboot.

    sudo reboot

(18). You will autologin as new user "user". <font size="-3">(If you didn't install as user "user", your old user and home folder does of course still exist.)</font>

(19). Done.

## How To Install Whonix-Gateway in a VM (UNTESTED / NOT RECOMMEND) ##
It is advised to install a new OS just for hosting the Gateway VM, any OS that can run VirtualBox works but we recommend an Open Source system.

Download the Whonix-Gateway image. <font size="-3">(Or build it from source code.)</font>

Adapter 1 can be set up as a NAT network. Adapter 2 must either be set to NAT as well (but you will need to forward ports from the host to the guest) or much simpler: use bridged networking and set it to the second physical interface (the one that goes into the isolated network/point to point ethernet). See "NAT vs Bridging" below.

This configuration is entirely untested and not recommended unless you need to run Tor through a VPN (can't that be done without VMs?) or an unsupported 3G modem and can't afford a 3rd physical device.

When using NAT for a virtualized Gateway you need to set up port forwarding in VirtualBox. Using bridged network may be easier, but then the router may see the Whonix-Gateway MAC address which identifies as Whonix-Gateway. (Should not be of concern in home networks. Should be of concern in untrusted networks or when using a modem to connect.)

## Install Whonix-Workstation in a VM (RECOMMEND) ##
### First Steps ###
Install and update a host operating system. On the host can run any OS that is capable of running VirtualBox, but be aware of [Transparent Proxy Leaks](https://trac.torproject.org/projects/tor/wiki/doc/TransparentProxyLeaks). It is recommended against to use Windows or another other commercial proprietary system as host operating system.

Download the Whonix-Workstation image. <font size="-3">(Or build it from source code.)</font>

Note sure what we wanted to say with this sentence:
If the physical network (between Whonix-Gateway and a router) uses 192.168.0.\* you need to review and edit all shell scripts and switch the internal network to something else!

### Host Network Adapter ###
The host has to be configured to use the static IP configuration.

    ## Whonix-Workstation
    ## /etc/network/interfaces for the host,
    ## when using Physical Isolation,
    ## with Whonix-Workstation in a VM.

    auto lo
    iface lo inet loopback

    auto eth0
    iface eth0 inet static
       ## Increment last octet of address
       ## on optional additional hosts.
       address 192.168.0.11
       netmask 255.255.255.0
       gateway 192.168.0.10
       #pre-up /usr/local/bin/whonix_firewall

       ## Out commented.
       ## For what do we require the network and broadcast
       ## instances anyway?
       #network 192.168.0.0
       #broadcast 192.168.0.255

    #auto eth0
    #iface eth0 inet dhcp

    ## end of /etc/network/interfaces

If the physical network (between Whonix-Gateway and a router) uses 192.168.0.\* you need to review and edit all */etc/network/interfaces*.

### NAT vs Bridging ###
#### Two Choices ####
In the default Whonix Virtual Box image, the network adapter setting for Adapter 1 (eth0) is set to internal network and will therefore not work out of the box. There are two choices to fix this. NAT (recommend) or bridged network.

#### NAT (RECOMMEND) ####
If you use NAT you will have to edit the */etc/network/interfaces/* in Whonix-Workstation to use DHCP (easier, shown in the example below) <font size="-3">or a static IP for Virtual Box NAT</font>.

    sudo nano /etc/network/interfaces/

Replace it with.

    ## Whonix-Workstation
    ## /etc/network/interfaces in a VM
    ## when using Physical Isolation.

    auto lo
    iface lo inet loopback

    auto eth0
    iface eth0 inet dhcp

    ## end of /etc/network/interfaces

#### Bridged Network (UNTESTED / NOT RECOMMEND) ####
If you use bridged networking things will (or should, we haven't tested anything yet) just work.

Since in the bridged network case, Whonix-Workstation can see the MAC address of whatever network adapter it is connected to, you should change the MAC address of the Workstation host and of the Whonix-Gateway.

See [Whonix in public networks / MAC Address](https://sourceforge.net/p/whonix/wiki/Pre%20Install%20Advice/#mac-address).

## Install Whonix-Workstation on hardware (NOT RECOMMEND) ##
Install Whonix-Workstation on hardware without using a VM is recommend against, because hardware serials would be visible to Whonix-Workstation.

The instructions are very similar, if not the very same, to those in "How To Install Whonix-Gateway on hardware" above. You have to use Whonix-Workstation_packages instead of Whonix-Gateway_packages and -t**w**-bare-metal instead of -tg-bare-metal.

# Further required reading #
[Documentation]. The host security chapter applies to both computers!

# Extra packages for better hardware support #
Some packages for bare metal may or may not be missing. Here is an probable incomplete list of packages, which may or may not be useful for better hardware support. Some suggestions.

    xorg
    xserver-xorg-input-all
    xserver-xorg-input-wacom
    xserver-xorg-input-geode
    xserver-xorg-input-vmmouse
    xserver-xephyr

    xserver-xorg-input-*
    xserver-xorg-*

    acpi-support-base
    acpid
    acpi

    discover
    discover-modprobe
    discover-data

    hwdata

    mdetect

    apt-cache show task-desktop
    apt-cache show task-kde-desktop
    apt-cache show task-laptop

If you have EFI bios.

    grub-efi-amd64

To get a more complete list, install Debian (with KDE) on bare metal using the regular Debian installer medium.

* diff "dpkg -l" with Whonix
* diff "sudo lsmod" with Whonix
* contribute your findings

# Footer #
[[include ref=WikiFooter]]