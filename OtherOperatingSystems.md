[[include ref=WikiHeader]]

[TOC]

# Introduction #
The [Whonix Framework](https://sourceforge.net/p/whonix/wiki/Technical%20Introduction/#whonix-framework) supports any operating system.

***Using a Whonix-Download-Workstation is easier and provides more Security out of the box!*** It's your responsibility to get the same security features for a Whonix-Custom-Workstation, see [Security Comparison: Whonix-Download-Workstation vs. Whonix-Custom-Workstation](https://sourceforge.net/p/whonix/wiki/OtherOperatingSystems/#security-comparison-whonix-download-workstation-vs-whonix-custom-workstation) at the bottom of the page for details.

The Whonix-Gateway already supports torification of any operating system, including Microsoft Windows and others. As an transparent or isolating proxy, see below for more information.

# Windows-Whonix-Workstation #
XP, Vista and Windows 7 are are known to work behind Whonix-Gateway. While it's possible, it's not recommend and only for advanced users. This is because, there are issues with Windows. Those are not Whonix issues. Whonix developers can not fix those issues. One issue is, that Windows is closed source. Rather, Windows is affected by [Transparent Proxy Leaks](https://trac.torproject.org/projects/tor/wiki/doc/TransparentProxyLeaks) and other issues. For more information and depending on your security requirements, read the following chapters.

## Easiest ##
Easiest, but least secure option.

(1). Download and use the default Whonix-Gateway.

Import it the same way you would do for Whonix-Default/Download-Version

(2). Create a Virtual Box VM.

Virtual Box -> Machine -> New -> Next -> Enter Name ->
Enter Operating System and Version -> Next -> define RAM ->
Next > create a new hdd (or not) -> Next ->
disk format doesn't matter, VDI works fine however -> Next ->
dynamically or fixed size is a matter of preference -> Next
hdd size and location is a matter of preference -> Next ->
Create

(3). Switch Virtual Box VM settings.

Choose the newly created VM -> Settings -> System -> Motherboard -> Hardware Clock in UTC

System -> Processor -> Enable PAE/NX if available

Network -> Adapter 1 -> attached to Internal Network (Important!)

Network -> Adapter 1 -> Name (of Internal Network) (Important!): Whonix

USB -> uncheck Enable USB controller

-> OK

(4). Start VM and Install Operating System.

You don't have to install updates while installing. You can do that right after installing, after the network has been set up.

username: user
computer name: host

(5). Configure network:

For Windows 7 (similar in Windows XP): In Control Panel > Network and Sharing Center: click on "Change adapter settings"
Right-click on local area connection > properties
In property window: double-click Internet Protocol Version 4, use the following settings:

    IP address 192.168.0.50
    Subnet netmask 255.255.255.0
    Default gateway 192.168.0.10
    Preferred DNS server 192.168.0.10

(6). Download operating system updates.

# Whonix-GNU/Linux-Workstation #
## Easiest ##
Easiest, but least secure option.

(1). Download and use the default Whonix-Gateway.

Import it the same way you would do for Whonix-Default/Download-Version

(2). Create a Virtual Box VM.

Virtual Box -> Machine -> New -> Next -> Enter Name ->
Enter Operating System and Version -> Next -> define RAM ->
Next > create a new hdd (or not) -> Next ->
disk format doesn't matter, VDI works fine however -> Next ->
dynamically or fixed size is a matter of preference -> Next
hdd size and location is a matter of preference -> Next ->
Create

(3). Switch Virtual Box VM settings.

Choose the newly created VM -> Settings -> System -> Motherboard -> Hardware Clock in UTC

System -> Processor -> Enable PAE/NX if available

Network -> Adapter 1 -> attached to Internal Network (Important!)

Network -> Adapter 1 -> Name (of Internal Network) (Important!): Whonix

USB -> uncheck Enable USB controller

-> OK

(4). Start VM and Install Operating System.

You don't have to install updates while installing. You can do that right after installing, after the network has been set up.

username: user
computer name: host

(5). Configure network:

Open a Terminal and type.

    sudo nano /etc/network/interfaces

You only need to configure eth0:

    # This file describes the network interfaces available on your system
    # and how to activate them. For more information, see interfaces(5).

    # The loopback network interface, leave as it is
    auto lo
    iface lo inet loopback

    auto eth0
    #iface eth0 inet dhcp
    iface eth0 inet static
    # increment last octet on additional workstations
           address 192.168.0.12
           netmask 255.255.255.0
           #network 192.168.0.0
           #broadcast 192.168.0.255
           gateway 192.168.0.10

Open /etc/resolv.conf.

    sudo nano /etc/resolv.conf

and delete everything, then add

    nameserver 192.168.0.10

(6). Download operating system updates.

Debian based Linux, such as Ubuntu:

    sudo apt-get update && sudo apt-get dist-upgrade

# More security #
Recommendations:

 * Verify operating system installation CD, compare with sha256 hash or even better verify the gpg signature, if available.
 * Install while the Virtual Machine has no internet connection.
 * Set your username to *user*.
 * Disable Internet Time Syncing.
 * Set your Time Zone to *UTC*.
 * Set up a static IP.
 * In case you want to run more than one Whonix-Workstation at the same time, it's recommend reading the Introduction in the [Multiple Whonix-Workstations] article.
 * Read [Security Guide], [Documentation] and [Design] (which is Whonix-Example-Implementation-Workstation (based on Debian GNU/Linux) specific) and try to apply as much from it to Windows as possible.

# Even more security #
## General ##
Recommendations:

 * Prevent [Transparent Proxy Leaks](https://trac.torproject.org/projects/tor/wiki/doc/TransparentProxyLeaks) by disabling Whonix-Gateway's Transparent Proxy feature. Instead use your Windows Whonix-Workstation behind an [Isolating Proxy](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO/IsolatingProxy). See [Stream Isolation] for more information and instructions on how to disable the Transparent Proxy feature.
 * Check your host clock out of band (use a watch or atomic clock).
 * Set your host and your Workstation clock to show seconds as well. After booting the Whonix-Windows-Workstation, add a random skew to your clock, maybe +/- 1 to 30 seconds. Optimal values are still under investigation. For reference, see [Whonix's Secure And Distributed Time Synchronization Mechanism](https://sourceforge.net/p/whonix/wiki/TimeSync/), it's Whonix-Example-Implementation-Workstation (based on Debian GNU/Linux) specific, but most information also applies to Windows. Since I am not aware of a tails_htp alternative for Windows, you have to do it manually.

## VM settings ##
**TODO**: Check and expand.

In Whonix source code look into *whonix_createvm* for the functions general_setup, workstation_specific and hardware_modifications. Find out your VM name using.

    vboxmanage list vms

You can and should drop the "sudo -u $USERNAME".

Apply all required settings. Not required (because recommended earlier or done by the gui creation process):

--name
storagectl
--memory
--pae
--hardwareuuid ^1^
sethduuid ^1^
--intnet1
--cableconnected1
--macaddress1 ^1^
--audiocontroller
--audio

^1^ You can only use those, if you are not using a Whonix-Default/Download-Workstation, otherwise they conflict.

Example:

    VBoxManage modifyvm "yourvmname" --synthcpu on

# Most security #
Use the default Whonix VMs and build them yourself from source.

# Ubuntu #
## General ##
Moved to [Ubuntu](https://sourceforge.net/p/whonix/wiki/Ubuntu/)

## About Ubuntu ##
Moved to [About Ubuntu](https://sourceforge.net/p/whonix/wiki/Ubuntu/#about-ubuntu).

## Guest additions for Ubuntu Precise ##
Moved to [Ubuntu](https://sourceforge.net/p/whonix/wiki/Ubuntu/).

# Debian #
Whonix-Default/Download-Version is already based on Debian Wheezy. In case you want to build on top of stable, sid or whatever, you may be interested to read:

* How to obtain Debian safely: [Debian ISO gpg verification](https://sourceforge.net/p/whoni/wiki/Debian/)

# Security Comparison: Whonix-Download-Workstation vs. Whonix-Custom-Workstation #
## Introduction ##
Read first: [Comparison of Whonix, Tails and TBB](https://sourceforge.net/p/whonix/wiki/Comparison%20of%20different%20Whonix%20variants/)!

Note: Whonix-BuildYourselfFromSource-Workstation is of course the same as Whonix-Download-Workstation.


## Table ##
_ | Whonix-Download-Workstation | Whonix-Custom-Workstation
------------- |  ------------- | ------------- |
Based on | Debian Wheezy GNU/Linux | Any of your choice. |
Amnesic | No | No
Protection against root exploits (Malware with root rights) on the Workstation ^18^ | Yes ^1^ ^a^ | Yes ^1^ ^a^
IP/DNS protocol leak protection	| Full ^1^ | Full ^1^
Takes advantage of Entry Guards	| Yes | Yes
Operating System Updates persist once updated | Yes | Depends if gets installed or is a Live CD.
Hides hardware serials from malicious software | Yes ^16^ | Yes ^16^
Collects (virtual) hardware serials | No | Depends on the custom operating system
Includes Tor Browser | Yes | Your responsibility to install Tor Browser.
Includes Firefox privacy patches ([reference](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO/WebBrowsers)) and Tor Button (=Tor Browser) | Yes, because it uses Tor Browser (without Tor/Vidalia). | Your responsibility to install Tor Browser.
Prevents Tor over Tor for Tor Browser | Yes | Your responsibility to prevent Tor over Tor.
Stream isolation to prevent identity correlation through circuit sharing | Yes | Your responsibility to use Stream Isolation.
Stream isolates Tor Browser | No ^14^ | No ^14^
Encryption | Should be applied on host. | Should be applied on host.
Cold Boot Attack Protection ^8^ | No | No
Secure Distributed Network Time Synchronization | Yes | Your responsibility to install it.
Hides your time zone (set to UTC) | Yes | Your responsibility to set clock to UTC.
Hides your operating system account name | Yes, set to user. | Your responsibility to set username to user.
Hides your MAC address from websites | Invalid ^19^ | Invalid ^19^
Secures your MAC address from local LAN (sometimes ISP) ^20^ | No, planed, see. ^21^ | Your responsibility. ^20^ ^21^
Hides your hosts MAC address from applications | Yes ^24^ | Yes ^24^
Secure gpg.conf | Yes | Your responsibility to use a secure gpg.conf.
Privacy enhanced IRC client configuration. | Yes | Your responsibility to configure the IRC client for enhanced privacy.

## Footnotes ##
Same footnotes as in [Comparison of Whonix, Tails and TBB / Security](https://sourceforge.net/p/whonix/wiki/Comparison%20of%20different%20Whonix%20variants/).

## Conclusion ##
The Whonix-Download-Workstation is already preconfigured with all Whonix extra security features.

A Whonix-Custom-Workstation *can be made* (Your responsibility!) as secure as a Whonix-Download-Workstation. If you simply create^1^ a Whonix-Custom-Workstation it has still *some* security advantages, <font size="-3">for example full IP/DNS protocol leak protection</font>, but *not all*, <font size="-3">for example it lacks Secure Distributed Network Time Synchronization</font>. The details are listed in the table above.

<font size="-3">
^1^ Install or use a Live CD/DVD into Whonix-Workstation.
</font>

# Footer #
[[include ref=WikiFooter]]