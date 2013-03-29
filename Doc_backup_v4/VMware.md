[[include ref=WikiHeader]]

[TOC]

# Status of VMware support in Whonix #
**Current state of Whonix inside VMware: rarely tested, it works, highly experimental, recommend against, rather recommend to use Virtual Box, VMware is closed source.**

**Whonix needs a contributor to support Whonix in VMware!**

# Supported VMware Products #
**VMware Workstation** was tested. It's currently in a *it works* state, but *rarely tested*.

**VMware Server** or other products are *untested*, but perhaps also in a *it works* state.

**VMware Player** is unsupported, because I don't see an option for for internal networking. ^1^

<font size="-3">
,,
^1^ Perhaps [OneVM] could work with VMware, but that would require even more contributions.
</font>

# About VMware #
Maybe I am a spoilt by Free Software. VMware is not very open, but in my opinion openness is important for security. I haven't found out how to submit a bug report. It looks like only buying customers may submit bug reports and there is only community support for products, which are free in price. There is also no list with open bugs. Without a list of known bugs, I am unable to determine if VMware is suitable for Whonix, i.e. does not compromise the user's anonymity. For this reasons it's also demotivating to contribute and report bugs.

# VMware upstream bug reports #
* [VMware bug report: failed to import .ova image](http://communities.vmware.com/thread/423920)
* [VMware bug report: .ova image internal network becomes bridged network](http://communities.vmware.com/thread/423924)
* [Virtual Box bug report Ticket #11160: .ova image created with Virtual Box, failed to import in VMware](https://www.virtualbox.org/ticket/11160)

# HowTo #
Do not forget to read the [Documentation].

You can either import the [Download] version of manually build from source. Import Whonix-Gateway.ova and Whonix-Workstation.ova. Due to a VMware upstream bug, you may have to press *retry* when importing the .ova images.

Due to a VMware upstream bug the network settings have to be adjusted.

* Whonix-Gateway set *network adapter* **2** to custom, */dev/vmnet8* (or on Windows probable: *vmnet8*).
* Whonix-Workstation set *network adapter* **1** to *custom*, */dev/vmnet8* (or on Windows probable: *vmnet8*).

# Harden VMware #
* Remove printer
* Disable 3D acceleration
* Remove CD/DVD drive
* Remove floppy drive
* Remove USB controller (at least disable automatically connect new devices)
* Remove sound card
* Do not install VMware Tools or open-vm-tools (comfort vs. security)

# Security #
* Connect the virtual network adapter to custom.  This is important! No host-only, no NAT, no bridging! I used VMnet9 virtual network, as it wasn't used by anything else.

One might wish to access the Whonix-Workstation through SSH. Therefore he could add a second network adapter with [Host-Only Networking](http://www.vmware.com/support/ws55/doc/ws_net_configurations_hostonly.html). Beware

    If you install the proper routing or proxy software on your host computer, you can establish
    a connection between the host virtual Ethernet adapter and a physical network adapter on the
    host computer. This allows you, for example, to connect the virtual machine to a Token Ring
    or other non-Ethernet network.

    On a Windows 2000, Windows XP or Windows Server 2003 host computer, you can use host-only
    networking in combination with the Internet connection sharing feature in Windows to allow a
    virtual machine to use the host's dial-up networking adapter or other connection to the
    Internet. See your Windows documentation for details on configuring Internet connection
    sharing. 

See also [Security Guide].

# Further Security #
If this article gets updated, the following should be noted:

[Changing or keeping a UUID for a moved virtual machine](http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=1541)

**"The UUID is based on the physical computer's identifier and the path to the virtual machine's configuration file."**

# Footer #
[[include ref=WikiFooter]]