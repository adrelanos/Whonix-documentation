[[include ref=WikiHeader]]

[TOC]

# Whonix's Protocol-Leak-Protection and Fingerprinting-Protection #
## Introduction ##
Whonix can not do the impossible and magically prevent all kinds of [protocol leaks](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO#Protocolleaks). However, it does offer best possible protection. It is a multi level protection always trying to prevent the worst.

## Most dangerous leaks are protected ##
Most dangerous leaks are protected. The following ones are in the most dangerous categorical, because they would lead remotely and directly to the users real identity.

* Your real external non-Tor IP address is covered due to the whole Whonix design, isolated proxy usage and [the Whonix firewall](https://sourceforge.net/p/whonix/wiki/Install%20Software/#whonix-workstation-is-firewalled). ^1^
* The same as above goes for DNS^1^ requests, they are safe. ^2^ 

## Many Whonix default applications are already configured, not to leak ##
* Configured to use their own SocksPort ([Stream Isolation]), thus preventing Identity correlation through circuit sharing.
* Browser fingerprinting: *Whonix Example Implementation* includes Tor Browser. Browser fingerprinting is as good/as worse, as you were using the normal Tor Browser Bundle.
* GPG: is configured not to leak your operating system version (no-emit-version) and other stuff ([on github](https://github.com/adrelanos/Whonix/blob/stable/whonix_workstation/home/user/.gnupg/gpg.conf)).
* XChat: uses secure defaults as per [TorifyHOWTO/XChat](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO/XChat) ([on github](https://github.com/adrelanos/Whonix/tree/stable/whonix_workstation/usr/local/share/whonix/xchat2)). Identity can be reset using *xchat-reset* ([on github](https://github.com/adrelanos/Whonix/blob/stable/whonix_workstation/usr/local/bin/xchat-reset)) as documented on the [XChat] page.
* ssh: <font size="-3">Without Whonix, syntax for ssh is user@hostname [...], but if the user forgets to specific user before @hostname, the operating system user name will be used and if that is something identifiable, anonymity is broken.</font> Since Whonix set the user name to *user*, in worst case, only the username *user* can be leaked, which is harmless. He could just have copied the syntax from the manpage. <font size="-3">In another, similar project, Tails, the username is set to amnesia, which is also not something the user entered and therefore safe.</font>

Many protocol leaks are documented, see [Applications] and [TorifyHOWTO](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO).

## Important identifies ##
These are also important identifies, because they can be used for fingerprinting, narrow down the list of suspects (for example, the time zone) or even lead to directly to deanonymization (for example, if username were set to John Doe).

* Desktop resolution is 1024x768 for all Whonix users. (Virtual) refresh rate is set to 60. ^a^ ^c^
* Color depth is the default 24 bit for all Whonix users. ^b^ ^c^ 
* All Whonix users have the same list of fonts installed. ^d^ ^e^ ^f^
* Internal (virtual LAN) IP address is the same for all Whonix users.^3^ 
* Time
    * Whonix-Workstation, Whonix-Gateway and the host time are all different from each other.
    * Time zone (local time) is set to UTC. ^15^
    * Hardware clock is set to UTC.
    * See [Whonix's Secure And Distributed Time Synchronization Mechanism](https://sourceforge.net/p/whonix/wiki/TimeSync/) for more information.
* User name is set to user.
* Hostname is to to host.
* Long host name (FQDN) is set to host.localdomain.
* Operating system (apt-get) updates are routed through their own circuit ([Stream Isolation]) to prevent accidentally leakage of your software packages and versions (if any custom software installed) which then could be correlated with other anonymous activity. See also [Software updaters](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO#Softwareupdaters) and [Software installation Whonix-Workstation](https://sourceforge.net/p/whonix/wiki/Install%20Software/).
* [MAC address](https://en.wikipedia.org/wiki/MAC_address) is the same for all Whonix users.
    * Whonix-Workstation's MAC address is shared among all Whonix users. That is useful, in case an application leaks the MAC address or in case Whonix-Workstation got compromised. ^11^
    * Whonix-Workstation can also see Whonix-Gateway's MAC address.
    * Whonix-Gateways MAC address is also shared among all Whonix users. **This may have side effects, were are still discussing, see [Dev].**
    * There are cases, were some stupid applications gather your MAC address and send it to a remote server (proprietary license checks use the MAC for hardware fingerprinting). That's not an issue for Whonix, since all Whonix users share the same MAC address on Whonix-Workstation.
* Worst case scenario: contents of your RAM (error reporting; RAM dump if infected with malware; [Transparent Proxy Leaks](https://trac.torproject.org/projects/tor/wiki/doc/TransparentProxyLeaks)) would "only" contain the RAM of your Whonix-Workstation. All your non-anonymous stuff on your Host would stay safe.

## Metadata ##
See [Metadata](https://sourceforge.net/p/whonix/wiki/Metadata/).

## Less important identifies ##
These identifies are less important, because an adversary can only collect them, either if the user installed malicious software (for example, some copyright enforcement and anticheat tools collect them) or only if the the adversary got remote access, i.e. the adversary has compromised a user or in some cases the root account.

Implemented:

* Hardware serial numbers which any applications could collect are hidden due to the Virtual Machine.^4^ 
* CPU model and capabilities are hidden by Virtual Box "Synthetic CPU" option.
    * Unfortunately, the clock speed of your host CPU is visible to all code (applications or malware) inside Whonix-Workstation.^5^ 
* RAM is set to 768 MB.
* Sensor information (cpu temperature, hdd temperature, [S.M.A.R.T.](https://en.wikipedia.org/wiki/S.M.A.R.T.)) are hidden. ^6^ Fortunately Virtual Box does hide them from the guest Virtual Machine by not implementing them. 
* Battery information is unfortunately not hidden by Virtual Box. ^7^
* BIOS DMI information is hidden by Virtual Box. ^8^
* Virtual BIOS DMI information and Virtual HDD and CD serial numbers are implemented by Virtual Box.
    * Even less important: Beginning with Whonix 0.4.4, we try to share those values among all Whonix users as well. See the whonix_createvm script if you are interested. ^8^ ^9^
* VM UUID, as in explained in [VBoxManage modifyhd](http://www.virtualbox.org/manual/ch08.html#vboxmanage-modifyvdi) is shared among the same Whonix versions. (Implemented in 0.4.4 and above.) ^14^
* [SLIC table](https://msdn.microsoft.com/en-us/library/windows/hardware/hh673514.aspx) is empty by default inside Virtual Box. ^10^
* HDD UUID is the same for all Whonix users. ^12^ 
* CD-ROM UUID is the same for all Whonix users. ^13^
* All Whonix users have by default the same set of software packages installed. - If you install software packages yourself, you give up that advantage. See also [Software updaters](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO#Softwareupdaters) and [Software installation Whonix-Workstation](https://sourceforge.net/p/whonix/wiki/Security/#software-installation-on-whonix-workstation).
* Disk uuids of the real hardware is of course hidden through Virtual Box.
* The disk uuids of the virtual partitions have been set at build time and are shared among the same Whonix versions. (Introduced in Whonix 0.4.5.) */etc/fstab* is shared among all Whonix users.

* Related Virtual Box tickets:
    * [document all virtual hardware serial numbers implemented by Virtual Box](https://www.virtualbox.org/ticket/10976)
    * [document which information from the host are visible to VMs](https://www.virtualbox.org/ticket/10975)

## Footnotes ##
<font size="-3">
,,
^a^ You can check the desktop resolution and refresh rate by running in console:
</font>

    xrandr

<font size="-3">
^b^ You can check color depth by running in console:
</font>

    xdpyinfo | grep "of root"
 
<font size="-3">
^c^ Note that you can not rely on https://ip-check.info or similar websites for checking desktop resolution and color depth, because Tor Button changes this values to improve your anonymity. See Tor Button specification and Tor trac for details.
^d^ You can check installed fonts using:
</font>

    fc-list

<font size="-3">
^e^ As long you or any additional software packages do not install further packages. 
^f^ Robert Ransom suggested, if possible, to share the same list of fonts as Tails. Since Tor Browser does not leak, which fonts are installed anymore ^g^, Whonix developer adrelanos fails to see the advantage of this. Follow-up inquiry ignored.
^g^ Only 3 common fonts (monospace, serif, times new roman) for all Tor Browser / TBB users can be detected.
</font>

<font size="-3">
,,
^1^ This does not cover application vulnerabilities and exploits, which escalate from the virtual machine to the host see [Attacks](https://sourceforge.net/p/whonix/wiki/Comparison%20with%20Others/#attacks). However, by design, the Whonix-Workstation does not know it's own external non-Tor IP address. 
^2^ */etc/resolv.conf* in Whonix-Workstation is configured to use the Whonix-Gateway as DNS resolver, which is routed through Tor.
</font>

    nano /etc/resolv.conf

<font size="-3">
^3^ You can check your internal (virtual LAN) IP address using:
</font>

    sudo ifconfig

<font size="-3">
^4^ You can check visible hardware yourself with
</font>

    sudo lshw

<font size="-3">
and
</font>

    sudo lspci

<font size="-3">
If you have USB devices attached use:
</font>

    sudo apt-get install usbutils
    sudo lsusb

<font size="-3">
^5^ This is due to the design of virtualization platforms (VirtualBox, VMware, etc.). Most virtualization platforms leak cpu model, capabilities and clock speed. VirtualBox (4.1+ if not earlier) can mask at least the model and capabilities of the CPU with the "Synthetic CPU" option. This option is activated by default on Whonix 0.2.1 and above. Check
</font>

    cat /proc/cpuinfo

<font size="-3">
If that is a still problem for you another workaround could be to use an emulator, such as [bochs](http://bochs.sourceforge.net/) or qemu. Unfortunately such emulators are slow and there might be other limitations. (Does Bochs support internal networking?)
^6^ You can check sensor information using:
</font>

    sudo apt-get install hddtemp
    sudo hddtemp /dev/sda

<font size="-3">
and
</font>

    sudo apt-get install lm-sensors
    sudo sensors-detect

<font size="-3">
^7^ You can check battery information that using:
</font>

    acpi -V

<font size="-3">
^8^ You can check BIOS DMI information using:
</font>

    sudo dmidecode

<font size="-3">
^9^ You can disk ids using:
</font>

    sudo ls -la /dev/disk/by-id/

<font size="-3">
^10^ You can check the SILC table using:
</font>

    sudo nano /sys/firmware/acpi/tables/SLIC

<font size="-3">
inside Virtual Box and on your host. On your host there may or may be not be a SLIC table. If there is none, it can't leak into Virtual Box. If there is one, you'll see, that it's not mirrored in Virtual Box, which is fine.
^11^ You can check Whonix-Workstations MAC address using
</font>

    sudo ifconfig | grep HWaddr

<font size="-3">
which is set to *08:00:27:07:0b:08*. At build time it was set to *080027070B08* (just different format, without :) in whonix_createvm.
^12^ You can check the HDD UUID using:
</font>

    sudo hdparm -i /dev/sda

<font size="-3">
^13^ You can check the CD-ROM UUID using:
</font>

    udisks --show-info /dev/cdrom

<font size="-3">
^14^ You can check the VM UUID using:
</font>

    sudo dmidecode

<font size="-3">
The UUID line should look like *UUID: 9852BF98-B83C-49DB-A8DE-182C42C7226B*. It was set at build time by [whonix_createvm](https://github.com/adrelanos/Whonix/blob/stable/whonix_createvm).
^15^ You can check your time zone using:
</font>

        cat /etc/timezone

# Footer #
[[include ref=WikiFooter]]