[[include ref=WikiHeader]]

[TOC]

# Open bugs and enhancements

## misc
### SECURITY Whonix Internal Updater OPEN NEEDS_DISCUSSION

* (adrelanos) Updating Whonix from user perspective is still a mess.
     * (adrelanos) They need to somehow backup their data, download huge images, delete the old images, import new images, get operating system updates, releases are infrequent...
     * (adrelanos) If the torbrowser script breaks or they update they signing keys, manual instructions have to be provided as a hotfix, which involves terminal commands.

* (adrelanos) The updater should contain two branches, stable and development.
* (adrelanos) By the way, projects such as Whonix hosted on sourceforge.net are allowed to host an apt repository as long it's hosted in the file release system. (For example [sonar](http://sonar-pkg.sourceforge.net/) has one.)
* (adrelanos) How? a) Either Whonix must come closer to Debian, i.e. convert all Whonix configuration files into .deb packages and then host a repository on sourceforge. After installing Debian in a virtual machine users could even add the Whonix repository and run "apt-get install whonix-gateway" and get all the files they require. Disadvantage: porting Whonix to other operating systems becomes much more difficult.
* (adrelanos) b) A wrapper around git. The [Whonix News File](https://sourceforge.net/p/whonix/wiki/Dev_news/) could include the latest recommend versions (testing and experimental). The git wrapper would checkout that version and overwrite all configuration files, which are changes in Whonix source. Difficulty: what if configuration files get deleted/moved or packages get removed? The developers would have to carefully add the required commands to it.
* (adrelanos) [dpkg-maintscript-helper](http://man.cx/dpkg-maintscript-helper) may be useful for deleting or renaming configuration files if we decide to go the .deb way.
* (adrelanos) We made great progress packaging whonix as deb packages.

### SECURITY Deterministic builds OPEN NEEDS_RESEARCH NEEDS_DISCUSSION
#### Ticket moved to github bugtracker
* https://github.com/Whonix/Whonix/issues/29

#### Old Notes
* (adrelanos) We should check if [Gitian](https://gitian.org/) can be used with Whonix. Deterministic builds (Gitian) should ensure, that the binaries are created from the source we claim. Others should be easily able to check that.
* (adrelanos) Since the scripts download and install the newest operating system security updates, this would cause different hashs. If we are going for this one, we'd need somehow to keep care of this.
* (anonymous) building and diffing (before ever booting them up, or you'll see some more log and chache files) two T-G images on two different systems but on the same day (so we don't get different apt-get updates) yields following results:
    * /var/cache/ldconfig/aux-cache look harmless, cache files naturally differ
    * /etc/console-setup/cached.kmap.gz look harmless, cache files naturally differ
    * /boot/grub/locale/en_AU.mo en_CA.mo en_GB.mo sometimes there, sometimes not, looks harmless
    * /etc/apt/trustdb.gpg must be harmless (a single byte at the beginning differs)
    * /boot/initrd.img-3.2.0-25-generic needs to be unpacked and compared again:
        * mkdir /tmp/unpackinitrd
        * cd /tmp/unpackinitrd
        * cp /mntpoint/boot/initrd.img-3.2.0-25-generic .
        * gzip -dc < initrd.img-3.2.0-25-generic | cpio -i
        * results: it's console-setup/cached.kmap.gz (again)
    * /var/lib/initramfs-tools/3.2.0-25-generic sha1 of the initrd
    * /lib/modules/3.2.0-25-generic/modules.dep because of vesafb.ko? seems related to building on virtualbox vs on bare metal?
    * /etc/shadow different hash of the changeme password, random seed? Doesn't matter you should change it immediately anyway.
* (anonymous) I guess we **could** disable all update repositories in sources.list while building and get a more easily verifiable deterministic build system but because Tor is so slow binary builds should really come with all updates available preinstalled. Again, ubuntu archive contains all the files to check manually. It's more work but certainly possible. Contrast that with the real difficulty of verifying compiled code vs its source... I forgot: Imagine there's a vulnerability in wget or apt-get, we should better patch that really quickly before using the vulnerable code to build our "secure" Whonix. (In case of apt-get we are pretty SOL in any case).
* (adrelanos) Since Whonix is now based on Debian Wheezy and the images are build using grml-deboostrap... I still have no idea if I build Whonix on day A and someone else builds it on day B, to verify it's build from the same source. grml-deboostrap with naturally download and install the most recent versions while the build from day A lags behind. Old Debian packages can be downloaded from [http://snapshot.debian.org/](http://snapshot.debian.org/).
     * (adrelanos) For example let say sha256sum /usr/bin/nano
 20ad0bc144d5f1d1f93e2f0afbc4b43b2fce3a2acf9ade751d6cf5d9bba34b4f  /usr/bin/nano

-   (adrelanos) [http://ftp.de.debian.org/debian/pool/main/n/nano/nano\_2.2.6-1.dsc](http://ftp.de.debian.org/debian/pool/main/n/nano/nano_2.2.6-1.dsc) contains sha256 sums

	be68e133b5e81df41873d32c517b3e5950770c00fc5f4dd23810cd635abce67a 1572388 nano_2.2.6.orig.tar.gz
	4b341f6747f81e07e256baf11d1127b15d51012164dd1b05f0cd5fee87d9e1f1 30095 nano_2.2.6-1.debian.tar.gz

* (adrelanos) How can I verify [http://ftp.de.debian.org/debian/pool/main/n/nano/nano\_2.2.6-1.dsc](http://ftp.de.debian.org/debian/pool/main/n/nano/nano_2.2.6-1.dsc) against the Debian archive key?
-   (adrelanos) [http://ftp.de.debian.org/debian/pool/main/n/nano/nano\_2.2.6-1.dsc](http://ftp.de.debian.org/debian/pool/main/n/nano/nano_2.2.6-1.dsc) itself is only gpg signed with weak SHA1.
* (adrelanos) Does Debian somewhere publish the sha256 of /usr/bin/nano?
* (adrelanos) unrelated, may be useful: http://lists.debian.org/debian-derivatives/2013/02/msg00034.html and http://security.stackexchange.com/questions/34413/integrity-check-against-package-repository

### SECURITY VirtualBox replacement: Xen, KVM, libvirt OPEN NEEDS_RESEARCH

* (anonymous) Ubuntu/Linux has been "rock solid" for me, except for the occasional kernel panic caused by VirtualBox. And where there are bugs, there are security bugs. Xen is definitely capable: [http://wiki.xen.org/wiki/Host\_Configuration/Networking](http://wiki.xen.org/wiki/Host_Configuration/Networking) and we could borrow from Qubes-OS (which probably is the most similar project to Whonix in terms of threat model and design). I'd put KVM as the second choice, we are already far too reliant on the Linux kernel (i.e. single points of failure) and it doesn't help with reducing the TCB. But both are stop gap till something like Genode.org becomes usable.
* (adrelanos) I agree, in long term we have to move away from Virtual Box. [The VirtualBox Kernel Driver Is Tainted Crap](http://www.phoronix.com/scan.php?page=news_item&px=OTk5Mw) says everything about their skills. After all the years they still require re-compilation of modules if the kernel has been updated. Imagine there was a kernel update and Virtual Box can no longer be started, iirc that happened in past. Although they have a good feature set and user interface.
* (anonymous) Actually recompiling is necessary because it's out of tree. It's out of tree because the kernel driver is crap.
* (adrelanos) If we switch to Xen or KVM we loose support for hosting Whonix on top of Windows. That would cost a lot users.
     * (anonymous) users who don't really need Whonix, or they wouldn't even think about hosting on a proprietary system that phones home with hardware and serial numbers. The "switch" can be optional or additional too.
     * (adrelanos) Every Windows user is at least a user compared to no user. As I often said, last time under "better Marketing", more users leads to more reviews, more press, more developers, more progress etc. We easily disposed Windows as build platform, let's not easily dispose it as host platform. People start mostly with Windows and somtimes switch to Linux when they get to know it over time. Most Tor users are probable Windows users but everyone is required for a good anonymity set.

* (adrelanos) The [createvm](https://github.com/adrelanos/Whonix/blob/master/Whonix_createvm) script contains within the functions general\_setup, gateway\_specific and workstation\_specific the commands, which Whonix depends on. Some are unusual and might be unique to Virtual Box, such as synthcpu and GetHostTimeDisabled (no ultimately complete list).
* (adrelanos) Not really what this ticket stands for, but... Rudimentary [Support for Whonix in VMware](https://sourceforge.net/p/whonix/wiki/VMware/) has been documented.

#### Xen

* (adrelanos) We have to research, if Xen is really suited for Whonix. How long will Ubuntu/Debian support Xen? In past I read that it is "somewhat difficult to integrate Xen into a distro". It were stupid if we move to xen and then everyone dropping xen.
* (anonymous) Xen is "industry standard" see xen.org for who is using it... It won't get dropped, there's room for more than one. [http://wiki.xen.org/wiki/Category:Ubuntu](http://wiki.xen.org/wiki/Category:Ubuntu)
* (adrelanos) virt-manager is the only graphical user interface I've found for Xen. A desktop operating system over VNC is a real blocker. It works but is tiresome and any kind of multimedia does not work well either. Do we agree, that we need a replacement for VNC? We can try out SDL and see how 2D and 3D performance is. There is also [Xen VGA Passthrough](http://wiki.xen.org/wiki/Xen_VGA_Passthrough) for full 3D, but I am not sure if it were secure.
* (adrelanos) See Qubes OS.

#### Qubes OS OPEN

* (anonymous) Give Qubes-OS a try, it's probably the nicest adaption of Xen for Desktop usage. They also get pretty good graphics (and overall) performance.
* (adrelanos) [Qubes OS](http://qubes-os.org/) looks good indeed: [http://theinvisiblethings.blogspot.com/2011/09/playing-with-qubes-networking-for-fun.html](http://theinvisiblethings.blogspot.com/2011/09/playing-with-qubes-networking-for-fun.html) Hardware support is not so good that the moment.
* (adrelanos) Another project, TorVM for Qubes (qubes-tor): [https://github.com/abeluck/qubes-addons/blob/master/qubes-tor/README.md](https://github.com/abeluck/qubes-addons/blob/master/qubes-tor/README.md) [https://lists.torproject.org/pipermail/tor-talk/2012-October/025960.html](https://lists.torproject.org/pipermail/tor-talk/2012-October/025960.html) [https://groups.google.com/forum/?fromgroups=\#!topic/qubes-devel/C1D5\_tbl4jM](https://groups.google.com/forum/?fromgroups=#!topic/qubes-devel/C1D5_tbl4jM)
* (adrelanos) Now that Qubes OS supports [HVM](http://wiki.qubes-os.org/trac/wiki/HvmCreate) (although no Qubes Tools), it could become easier to use Whonix images inside Qubes OS.
* (adrelanos) To unpack the Whonix .ova images.

	tar -xvf Whonix-Gateway.ova
	Whonix-Gateway.ovf
	Whonix-Gateway-disk1.vmdk

* (adrelanos) Open questions... How to convert the .vmdk to Qubes OS (Xen) compatible images?
     * (adrelanos) Converts, but not tested if they work in Qubes OS. ([source of information](http://unixfoo.blogspot.com/2008/12/vmware-to-xen-conversion.html))

.
 # qemu-img info Whonix-Gateway-disk1.vmdk
	 qemu-img convert Whonix-Gateway-disk1.vmdk -O raw Whonix-Gateway.img
 # qemu-img info Whonix-Gateway.img

* (adrelanos) Can .img images be used inside Qubes OS or do they use some other format? I expect them to work.
* (adrelanos) How to create the VM description file with internal network?

#### KVM OPEN
* (adrelanos) KVM is good because it's in the kernel.
     * (anonymous) KVM is also bad because it's in the kernel. see qubes-os docs for why they chose Xen over it.
     * (adrelanos) So it will be Xen...

* (adrelanos) Which user interfaces exist?
* (adrelanos) We should make a list off all features we need from KVM  backend and from user interface (virt-manager). List the missing pieces. Track/create (if not already) the approprieate bug reports and feature requests.
-   (espes) Note 'KVM' can refer to just the kernel tech or qemu-kvm, which was a fork of qemu using the kernel driver but has recently been merged into mainline qemu.

#### Qemu see status
* (adrelanos) STATUS: Unless someone researches it, not going to happen. If someone finds out, documents, it will be gladly added. Default Virtualizer will stay Virtual Box. Might accept alternative Qemu builds if someone is willing to maintain those builds. Open for development discussion. An anonymous user [reported](https://sourceforge.net/p/whonix/discussion/general/thread/c0090dde/) in the forum, that it's working.
-   (espes) Slow (but fast enough?, self-contained, portable) without optional KVM backend.
     * (adrelanos) Needs Testing. Maybe fast enough on fast systems?

-   (espes) Probably more secure than VirtualBox (no rotten kernel module)

* (adrelanos) [KQEMU is dead.](http://wiki.qemu.org/KQemu/Doc) They now focus on KVM.
* (adrelanos) How is public scrutiny compared with Virtual Box? Do they have any enterprise or any other kind of customers?
-   (espes) Probably less secure than a hardened bare-metal hypervisor (Xen, ESX, etc)
* (adrelanos) Deployability? How difficult is it for users to download and install everything?
* (adrelanos) Usability? How difficult is it for users to start, stop (, clone, delete, import, snapshot) the VMs? Graphical user interface?
* (adrelanos) Implementation: the Whonix build process initially create .img images, which seem to be useable by Qemu. There seems easy to support Qemu. Only the start command telling how much ram, which image to use etc. I think the most difficult part could become configuring the internal network between WG and WW.
* (adrelanos) General advice when trying to develop this: Try first to get an internal network without using Whonix, afterwards(!) apply the things you learned to Whonix.
* (adrelanos) Term for search engines: qemu internal network
* (adrelanos) Might be related: [https://blog.cryptomilk.org/2007/07/12/qemu-kvm-internal-network-setup/](https://blog.cryptomilk.org/2007/07/12/qemu-kvm-internal-network-setup/)

#### libvirt IMPOSSIBLE
* (adrelanos) Should check if the Virtual Box specific commands can be replaced with [http://libvirt.org/](http://libvirt.org/). It is a wrapper for all virtualizer specific commands and offers one unified api. (Ubuntu Bug needs simple workaround: [http://stackoverflow.com/questions/2778638/libvirt-and-virtualbox-getting-started](http://stackoverflow.com/questions/2778638/libvirt-and-virtualbox-getting-started)) In theory all virtualization platforms could be supported at once. At least for building from source choosing the virtualizers would be as simple as changing one option. That would make Whonix fairly virtualizer independent and very generic.
* (adrelanos) Libvirt is out of question. [libvirt-users Does libvirt abstract each and any vm specific command?](https://www.redhat.com/archives/libvirt-users/2012-August/msg00150.html) Libvirt does not (yet) abstract some commands Whonix depends on.

### SOURCE CODE PACKAGING get tails\_htp into Debian NEEDS_CODE
* (adrelanos) [Whonix's Secure And Distributed Time Synchronization Mechanism](http://sourceforge.net/p/whonix/wiki/TimeSync/) depends on tails_htp. Let's get it into Debian.
-   create an upstream github repository -   done
-   add patch, perhaps option to deactivates Virtual Box guest additions time sync (the few lines of code are already in Whonix)
-   add patch, to run htpdate every hour at a random minute for continued time synchronization
-   add patch, to use /usr/bin/curl instead of curl to circumvent uwt wrapper, because htpdate uses socks settings.
-   make sure it could work in plain Debian without Tor, with Tor, in Tails and in Whonix
-   talk about it with the Tails developers
-   give the Tails developers git write access
-   create a .deb
-   get the .deb into Debian
* (adrelanos) Created a repository: [https://github.com/adrelanos/sdwdate](https://github.com/adrelanos/sdwdate)

### OPTIONALFEATURE Portable VirtualBox (like portableapps.com) LOOKING for contributor
* (adrelanos) Whonix can be equally as easy to use like the Tor Browser Bundle. There are adjusted versions for portability, such as vbox.me. Also when you google it, you find a lot of stuff about portable virtualbox. It would allow us to configure a package of Virtual Box portable, including T-G and T-W. The user would only have to start both and were done.
* (adrelanos) Can we trust [vbox.me/](http://www.vbox.me/)? (Did not look into it yet.)
* (adrelanos) UPDATE: [coderman implicated](https://lists.torproject.org/pipermail/tor-talk/2012-March/023575.html) that we should make the final package as easy and secure as possible. Secure in meaning of, there should be no buttons were the user can potentially harm himself. (Such as adding a NAT/bridged network adapter to the T-W.)
* (adrelanos) Another option would be the Virtual Box core combined with PhpVirtualBox. Drawback: we also would have to deploy a webserver which PhpVirtualBox needs to function. Advantage: hacking PhpVirtualBox (disabling dangerous buttons) should be easier.
* (adrelanos) Or we can control VirtualBox through the command line interface only. A (compiled) windows batch file or linux shell script could be sufficient to start the T-G.ova and the T-W.ova, thus hiding most virtual box controls.

### SECURITY Research: IP discovery through Tor Proxy LOOKING FOR CONTRIBUTOR
* (adrelanos) See torproject.org trac ticket #5928: task: Research: IP discovery through Tor behind isolated network for details.
* (adrelanos) Since May 2012, the Whonix project has neither the developers, time nor skill to do the research. Waiting for contributor.

## Host Operating System
### SECURITY Whonix Host Operating System NEEDS_DISCUSSION
* (adrelanos) See also forum discussion: https://sourceforge.net/p/whonix/discussion/general/thread/1e64cfee/

### FEATURE Whonix (USB) installer TODO NEEDS_CODE
* (adrelanos) The [Pre Install Advice](https://sourceforge.net/p/whonix/wiki/Pre%20Install%20Advice/#host-security) recommends to use a dedicated host operating system on external media just for running Whonix. Even when not using Physical Isolation, this improves security a lot. Users should be more encouraged to do it.
* (adrelanos) The Whonix installer could install a host operating system to a USB disk and download the Virtual Machine images.
* (adrelanos) The host operating system on the USB disk should be fully encrypted.
* (adrelanos) I am not aware of any tools running on existing Windows/Linux/Mac, offering to install Debian on an encrypted USB hdd.

### OPTIONAL FEATURE Whonix host additions OPEN NEEDS_CODE
* (adrelanos) Vidalia 0.3.x to control Whonix-Gateway, ssh shell into Whonix-Gateway, sshfs into Whonix-Gateway, Wipe RAM panic script would be some useful additions, which Whonix could provide for the host operating system.
* (adrelanos) Backup of hidden service keys on Whonix-Gateway is also difficult.
* (adrelanos) Host firewall progress: https://github.com/adrelanos/Whonix/tree/untested_adre/host

### SECURITY MAC address in public networks OPEN NEEDS_DISCUSSION
* (adrelanos) We need to add instructions how to change mac addresses on bare metal, since it can't be done with VirtualBox. UPDATE, not exact, see below.
* (adrelanos) [Tails MAC address](https://tails.boum.org/contribute/design/MAC_address/); [Tails macchanger](https://tails.boum.org/todo/macchanger/)
* (adrelanos) When using Whonix's bare metal Tor-Gateway in public networks, it might not be wise to use a fixed MAC, because Tor-Gateways's MAC address is public knowledge. That reveals the fact, the user is a Whonix user. Affects [anonymous wifi adapter](https://trac.torproject.org/projects/tor/wiki/doc/TorBOX/BareMetalHints#anonymouswifiadapter). Update: Also affected [anonymous 3G modem](https://trac.torproject.org/projects/tor/wiki/doc/TorBOX/BareMetalHints#anonymous3Gmodem).
* (adrelanos) And a google search told me, that our current MAC addresses are unique to Whonix. No other results for them. We should pick two popular network cards.
* (anonymous) MAC addresses don't work like that, they are supposed to be unique, there are no "popular" addresses out there. What we need to do in the case of public networks is randomize on reboots.
* (adrelanos) Randomize without asking on reboot is not good, like Tails pointed out, that can warn admins. We have to educate Whonix users about this issue and they have to make that decision.
* (adrelanos) The default MAC address for non-public networks should include a popular vendor, followed by the "unique" part.
* (anonymous) Well, if we use a non-unique MAC this isn't really so much of an issue because you still have some deniability. If using standard VBox Whonix on public networks we need to tell users to change the MAC on the host!
* (adrelanos) Yes, a NIC from a popular vendor is just a minor thing. That's only a minimal improvement, in case some stupid application collects your MAC (for licensing stuff) and sends it somewhere.
* (adrelanos) The issue in public networks is more complicated. The first part of the MAC has to be a popular vendor and the second part to be random. (by [Tails design](https://tails.boum.org/todo/macchanger/#index1h1)) If they are twice in the same public network, they (depending on their threat model) shouldn't change their MAC. Changing the MAC inside the VM is of no help within public networks. MAC has to be changed on the host, that's the MAC the public network gets to see. Bare metal = host. They won't need special instructions.
* (adrelanos) Started documenting, [Whonix in public networks / MAC Address](https://trac.torproject.org/projects/tor/wiki/doc/TorBOX/SecurityAndHardening#WhonixinpublicnetworksMACAddress). UPDATE: may be revised. Sufficient for Whonix 0.2.0.
* (anonymous) Even according to Tails doc Whonix can do automatic randomization; it's not a live distro and therefore not suited for public PCs, the worry about non existing vendor IDs is therefore a lesser too. What we need, for 0.2, is a script that will configure Ubuntu/Debian to disable auto starting of interfaces at boot and another script that can be run automatically, if so desired, to change the MAC address of all attached NICs. I think Backtrack is configured that way.
* (adrelanos) This is a hard one. And the macchanger scripts would have to be applied on host (hard, startup scripts are operating system and even distro specific) or for bare metal, on T-G. Neither Whonix nor Tails are ready for this kind of adversary in public networks. We outlined that in hardening and may add a link to the readme as well. Imho for now we can't do much more than documenting. When not used in public networks, we don't have to tamper with the host's MAC (and should not, in order not to break working setups).
* (anonymous) this does not apply to t-g on bare metal, we control everything. Also currently we assume that Whonix is built and run on debian/ubuntu and scripts for this can be made cross distro and cross version compatible. I think there should be an optional function in the tor-gateway script for this
* (adrelanos) I am okay with a optional function, but I wouldn't know how to implement it.
* (anonymous) t-g on "bare metal" (no matter whether it's a VM itself or not) always needs a changed mac address, we should use the same as for the VM (and a 3rd for host if t-g runs in vbox?) Apparently it can be added in /etc/network/interfaces as "hwaddress ether 00:00...."). That should be default for bare metal. To prevent automatically bringing up new network interfaces I think all that's needed is to uncomment "auto eth0", then manually bring up with "sudo ifup eth0". Then in addition we should provide a script to randomize, optionally on boot: add "pre-up macchanger -e eth0" to the interfaces file. TODO: documentation, -baremetal flag for t-g.sh.
* (adrelanos) "t-g on "bare metal" (no matter whether it's a VM itself or not) always needs a changed mac address" - Why?
* (anonymous) As I understand it if one uses bridged mode on the t-g and connects via Ethernet the t-w will be able to see both MAC adresses, the virtual VBox one and the physical of the host. Though I did not tested that.
     * (adrelanos) T-W should be only able to see eth1's MAC (internal network: Whonix). T-W should not be able to see eth0's MAC (NAT or bridged). If that were the case, out setup were broken. Why should T-W see eth0's MAC? Everything T-W does will either be filtered or redirected into a Socks-, Dns- or TransPort. If that were the case, this were worth a bug report against Tor client. We should see if your assumption is actually true before implementing it (for that reason).
     * (anonymous) Not so fast. We got a bare Metal Whonix with a t-g in vbox and a t-w in vbox. The virtual eth0 of the t-w in bridged mode directly connects to virtual eth1 on the t-g (bridged mode) That's how it's supposed work. But in reality t-g connects to the physical NIC on the client host which is connected to the physical NIC on the gateway host, which is connected to the virtual eth1 on t-g. Who says t-w has no way of finding out the MAC of either physical NIC? I very much doubt that, there are all these broadcast and arp things going on. Now if we use NAT for both VMs what do they see? Only a virtual NIC of the Vbox NAT device, what's the MAC of that, can it be changed? Looks like 10.0.3.2 is the virtual gateway with 52:54:00:12:35:02 which isn't unique. good. So, should we switch to NAT now? But maybe I'm wrong and t-w can't read physical MAC addresses?
     * (anonymous) Do you have a bare metal set up to test this on? I'm pretty sure if using bridged networking the t-w can actually directly connect 
to both systems the t-g and its host (as if it was directly connected to two different NICs). Consequently if that's true, the host allowed forwarding and t-w was misconfiguration or rooted one could circumvent tor.
     * (adrelanos) No, I don't have a test environment yet, hopefully soon.
     * (adrelanos) Okay, that all sounds quite scary. I haven't yet completely wrapped by head around it. Anything switching away from bridged networking sounds fine.
     * (anonymous) note: that the host could potentially forward and bypass traffic doesn't depend on bridged being used or not. The t-g host needs to be secure in every case. bridged mode really only has implications on MAC fingerprinting.

* (adrelanos) eth1's MAC on T-G (internal network) should really be changed to "0800272fcf44", but fixed. Then T-G VBox were equal T-G bare metal.
* (adrelanos) And while we are at it, anything against using uppercase for the MAC's? VBox converts to uppercase anyway.
     * (anonymous) Linux tools default to lower case, if I copy and paste that's what you get :)
     * (adrelanos) Shouldn't we convert to uppercase anyway?
     * (anonymous) If you want to, it's just cosmetic
     * (adrelanos) Not solely cosmetic, it prevents confusion if anyone cares to check. This part closed. Whole thread not.
     * (anonymous) if you say so :P Add to documentation and then let's file it for now? This isn't high priority to automate.
     * (adrelanos) Well, no, I am of course not happy with the outcome of the whole thread / problem with MACs. What is done, is the part of discussion about using uppercase for the MACs in build documentation. You said it's solely cosmetic and and didn't disagree with uppercase. I'd prefer uppercase to prevent confusion ("build documentation said low but in fact in is big, is that alright?")

* (adrelanos) Any suggestions for a fix for Whonix 0.2.0? Any suggestions for a long term fix?
     * (anonymous) "add to documentation" = I think we should just **document the changes needed to /etc/network/interfaces and leave it to the user to do it manually**. **Long term, T-G should probably auto-detect if it's run directly on bare metal or in bridged mode and always spoof the MAC address, disable eth0 networking on boot and offer a script to randomize.** ... **Further we need to take care of USB wifi/mobile network sticks.**

* (anonymous) basic documentation is done. not much more I can do without a baremetal/Pi test set up.

### SECURITY Wipe RAM panic script OPEN NEEDS_RESEARCH NEEDS_CODE
* (adrelanos) We recommend Linux for the host anyway. We also should provide and recommend a panic button. Upon pressing the panic button, the content of the RAM has to be securely wiped. (To ensure that any full disk encryption keys from RAM are lost and cold boot attacks are impossible.) Tails and Liberte Linux implemented it.
* (adrelanos) How I wish it to work: you start the script shortcut on the host, ram and master keys get deleted, system crashes, clean shutdown takes too long. Resources: [arch forum](https://bbs.archlinux.org/viewtopic.php?id=136283); google: site:www.saout.de/pipermail/dm-crypt/ cold boot attack ; [tails](https://tails.boum.org/contribute/design/memory_erasure/)
* (anonymous) Tails and Liberté use kexec, they've researched it and I think we should follow. Both could be faster but they are the most thorough, erasing even most of the kernel memory. If the hardware supports it: [http://www1.informatik.uni-erlangen.de/tresor](http://www1.informatik.uni-erlangen.de/tresor) -   The idea is nice. It's only a kernel patch. If it doesn't get supported upstream it's a bit difficult to make use of as kernel is updated.
* (anonymous) Tails and liberte do it differently and a quick glance over their sources didn't make it obvious to me how to make a simple stand-alone implementation. I could need help here.
* (adrelanos) Difficult to understand and implement for me, as it needs a custom initramfs and I haven't learned that yet. And we should recommend to implement it on the host, not so much point implementing it in VM. Tails implemented quite nice features, they always wipe at normal shutdown and also have panic key (bootmedium removed). The latter may not be possible for use (may be installed on internal hdd), therefore we should provide a panic button/script. Also here it would be better, if that feature were supported upstream "apt-get install wiperam" or something like that. Maybe it would help if there were a real project, someone else proving a project for this - haven't found one yet beside a lot forum discussion.
* (anonymous) check gentoo and arch wiki for how to do things manually in linux. Ubuntu/Debian automate a lot of tasks but when you are trying to do custom things they often get in your way and make it more complicated. We should ask Tails if they are interested in upstreaming their work or releasing it as a standalone .deb. After all this isn't just useful for Tails and other Tor projects but everyone who uses FDE.
* (adrelanos) [Tails-dev Ram Wipe Script Upstream, any progress?](https://mailman.boum.org/pipermail/tails-dev/2012-June/001258.html) Bad news. "No progress so far. It's still in my low-priority personal todo list." ... "But anyway, given the current state of relative brokenness of this feature, I'd rather see it \*fixed\* first, else it does not make sense to seriously talk about packaging."
* (adrelanos) It's a part of host security. Nothing we have to solve. Adding some hints to hardening.
* (anonymous) this is important, let's fix this. Since there's been zero progress, we need to make more noise...
* (adrelanos) I don't feel I am skilled enough to implement it myself. This issue has not been fixed by the whole security community. I wouldn't know how we could. It's not related to Whonix, it's interesting for a much wider community using FDE. Dunno why such great things like wipe ram script and TRESOR are not already in upstream. Making noise... Well, good idea, we can post a feature request to Ubuntu Brainstorm, ask askubuntu, ask serverfault, Update: superuser.com. One at a time. Let's prepare a message. Update: Please edit the message at will. If it's done I'll post it, post a link here and delete the draft.
* (adrelanos) Update posted first one: [http://askubuntu.com/questions/153245/how-to-wipe-ram-on-shutdown-prevent-cold-boot-attacks](http://askubuntu.com/questions/153245/how-to-wipe-ram-on-shutdown-prevent-cold-boot-attacks)
* (adrelanos) There has been an answer. Looks somewhat too small/easy. Btw: there is no registration required.
* (anonymous) It doesn't free any kernel memory as booting into a new small kernel via kexec which is what Tails/Liberte is doing. Still, much better than not doing anything.
* (adrelanos) I think this one will be a hard one, if no one from Tails or Liberte Linux implements it. Most people in the forum discussion have not really seen the cold boot attack demonstration and don't know how long contents of the RAM can really be extracted. Therefore most people argue that this feature is nonsense. And if the undecided ones google, they find old discussions prior the cold boot attack demonstrations and think it's pointless. We really gotta ask a good questions to attract interest.
* (adrelanos) Moved to non critical tasks due to lack of discussion and since it's not really the core of Whonix. Encryption is host security, we recommend it but are not an encryption project. Don't worry, after 0.2 we can continue making noise by posting it somewhere else.
* (adrelanos) Waiting for result on [http://security.stackexchange.com/questions/18975/wipe-ram-on-shut-down-to-prevent-cold-boot-attack](http://security.stackexchange.com/questions/18975/wipe-ram-on-shut-down-to-prevent-cold-boot-attack) and finally maybe posting on Ubuntu brainstorm.
-   (adrelanos) [http://brainstorm.ubuntu.com/idea/30076/](http://brainstorm.ubuntu.com/idea/30076/)
# ARCHIVE
Closed discussions are archived. Feel free to reopen, copy back here then.

* [The older archive.](https://trac.torproject.org/projects/tor/wiki/doc/TorBOX/Dev/ArchivedDiscussion).  
* The newer archive: [Dev_old_1].

# Footer
[[include ref=WikiFooter]]