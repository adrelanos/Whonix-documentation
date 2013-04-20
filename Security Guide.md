[[include ref=WikiHeader]]

[TOC]

# Basics #
* [Warnings!](https://sourceforge.net/p/whonix/wiki/Warning/)
* [Non technical steps staying anonymous](https://sourceforge.net/p/whonix/wiki/DoNot/)
* [Pre Install Advice](https://sourceforge.net/p/whonix/wiki/Pre%20Install%20Advice/)
* [Post Install Advice](https://sourceforge.net/p/whonix/wiki/Post%20Install%20Advice/)
* and reading [Documentation] in general

# Operating System #
## Recommendation to install latest security updates on all systems ##
(1) Important! Everything must stay current.

Check at least at a daily base. Keep your host operating system updated. Update Whonix-Gateway and Whonix-Workstation.

    sudo apt-get update && sudo apt-get dist-upgrade

(2) If you see something like the following.

    Configuration file `/etc/network/interfaces'
     ==> Modified (by you or by a script) since installation.
     ==> Package distributor has shipped an updated version.
       What would you like to do about it ?  Your options are:
        Y or I  : install the package maintainer's version
        N or O  : keep your currently-installed version
          D     : show the differences between the versions
          Z     : background this process to examine the situation
     The default action is to keep your current version.
    *** interfaces (Y/I/N/O/D/Z) [default=N] ? N

You should keep the currently-installed version! Otherwise anonymity/privacy/security settings deployed with Whonix might get lost. If you are an advanced user and know better, you can of course manually check the difference and merge them.

(3) Never install unsigned packages!

If Apper complains because of unsigned packages, this is most likely a bug in Apper. In this case update manually using apt-get as described above.

If apt-get complains that a package can not be verified, don't proceed! Ruining "*apt-get update*" again should fix it. If not, something is broken or it's a man-in-the-middle attack.

# Whonix-Gateway Security #
## General ##
You should never use Whonix-Gateway for anything other than running Tor on it!

In case the Whonix-Gateway is compromised the identity (public IP), all destinations and all clear-text (and hidden service) communication over Tor is available to the attacker.

If you feel you need to install any extra packages on the Gateway please consult the developers first to ask if that is really necessary/wise.

## Warning: Bridged Networking ##
You shouldn't change the Whonix-Gateway's first or second network interface to bridged network. This is untested. It should not be necessary. If you feel it is necessary, please get in contact.

<font size="-3">
If you are interested, here is a [discussion thread](https://sourceforge.net/p/whonix/discussion/general/thread/1e6a8675/), and [another one](https://sourceforge.net/p/whonix/discussion/general/thread/3a0b673a/), with arguments whether NAT or bridged network is more secure.
</font>

# Host Security #
## Basics ##
Please read the [Pre Install Device about Host Security](https://sourceforge.net/p/whonix/wiki/Pre%20Install%20Advice/#host-security).

## Risks through hardware components ##
Assumption: 
an adversary managed to break out of Whonix-Workstation's Virtual Machine using an exploit.

Hardware components, either built in or extra components, such as CPU or hdd temperature sensors, microphones and cameras introduce risks.

Whonix with Physical Isolation is affected. 

* Users IP address is still safe, but the temperature sensors can be used for anonymity set reduction. Different CPU or hdd models will have a different sensor information, depending on climate and weather. If you can, you are advised to remove or to obfuscate the sensors result.
* Camera and microphones can be covertly activated by the adversary. At least remove them (external ones) or disable them in BIOS if possible. Better cover them or ideally remove them.

Whonix Standard / Download version (host+VM+VM) is affected, although it does not matter: 

* Same as above applies. If the assumption is true, the adversary can already find out the users real IP address.

<font size="-3">Thanks to Robert Ransom for pointing Whonix developer adrelanos to this issue.</font>

## Anonymous 3G modem ##
Normally your dial up or broadband provider knows your name, postal address and non-anonymous payment method. This is bad. Suppose Tor or Whonix are compromised. An adversary just has to pressure your provider and can very easily find our your identity. This is not the case here.

* plugged or integrated into Whonix-Gateway
* Buy the 3G modem anonymously \[in a store, second hand, on street, no personal data\].
* Be sure to have never used it for non-anonymous use before.
    * This is because, in many countries the telecommunication company log the phone serial number (IMEI), the SIM serial number and the phone number for each network login.
* Also be sure to buy the SIM-card anonymously.
* Prepaid is better.
* Buy cash codes in different stores anonymously.
* Be sure, to never have used this anonymous SIM-card with a non-anonymous phone or 3G model.
    * This is because, in many countries the telecommunication company log the phone serial number (IMEI), the SIM serial number and the phone number for each network login.
    * Optionally, always get a fresh, distant, random, non-circle spot. (security vs. comfort)
    * Check of cameras and witnesses.
* 3G users often get only a shared IP. Due to scarcity of IPv4 IP's, thousands of users share the same external IP (IPv4). Some providers do not log yet users (NAT) ports. Consequently they can not identify them, when they are given an IP and timestamp. Nice to have, but don't rely on it! (Some providers assign additional IPv6 IP's to their users, which are unique. Tor does not use IPv6 yet.)

## Anonymous WiFi adapter ##
Normally your dial up or broadband provider knows your name, postal address and non-anonymous payment method. This is bad. Suppose Tor or Whonix are compromised. An adversary just has to pressure your provider and can very easily find our your identity. This is not the case here.

* Plugged or integrated into Whonix-Gateway.
* Buy the wifi adapter anonymously \[In a store, second hand, on street, no personal data\].
* Be sure to have never used it for non-anonymous use before.
    * This is because a few providers or hotspot providers log the mac address and the username (for paid hotspots) for each dial up.
* Use only free hotspots or pay them anonymously (if that's possible, otherwise abstain from paid hotspots).
    * Optionally, always get a fresh, distant, random, non-circle spot. (security vs. comfort)
    * Check of cameras and witnesses. 

## Hardening ##
Whonix does not yet improve host security. You are advised to use a secure host operating system.

# Virtualization Platform #
## Harden Virtualbox ##
For an overview on security risks of VMs in general: [How secure are Virtual Machines really?](http://security.stackexchange.com/questions/3056/how-secure-are-virtual-machines-really-false-sense-of-security)

The less features, the smaller the [attack surface](http://en.wikipedia.org/wiki/Attack_surface). Here are some suggestions for features which you can remove and not impact core functionality:

* Disable Audio
* Do not enable Shared Folders
* Do not enable video acceleration
* Do not enable Serial Port
* Do not install Virtual Box Guest Additions
    * They weaken security in general.
    * Additionally they give the Virtual Machine access the the host's (built-in) microphone. Many notebooks have a built-in microphone. In case you install Guest Additions anyway, better cover it up or remove your microphone.
* Remove Floppy drive
* Remove CD/DVD drive
* Do not attach USB devices
* Do not enable Remote Display server
* Do not enable IO APIC, EFI? (questionable)
* Enable PAE/NX? (NX is a security feature)

For the best security you should consider using multiple physical systems, see [PhysicalIsolation].

# Whonix-Workstation Security #
## Introduction ##
If this VM is compromised all data it has access to, all credentials, browser data, passwords... the user has entered can be compromised. The IP is never leaked but these information can still result in identity disclosure.

Best practice is to create snapshots of the VM and "roll back" after risky activity and whenever the user suspect the integrity of the system could have been compromised, see *Recommendation to use multiple VM Snapshot* below.

*Whonix Example Implementation* is currently based on Debian.

<font size="-3">
For Technical Design notes, see [OperatingSystem].
For Information on how to use other operating systems,see  [OtherOperatingSystems].
</font>

## Recommendation to use multiple VM Snapshots ##
Apart from offering protection against hardware serial leaks VMs got another great advantage: the ability to quickly discard and restore a system.

It is recommended that you keep a master copy of Whonix-Workstation, keep it updated, make regular "clean" snapshots but do not edit any settings or install additional software or use it directly for any activity. Instead make a clone or use snapshotting (but never mix up clean and unclean states!) for activities that require anonymity.

## Adding NAT adapter to Whonix-Workstation / Updates without Tor ##
Obviously the anonymity will get compromised if you add another NAT network adapter to the Whonix-Workstation. It is quite clear not to do that. If you were infected, it could leak then. Therefore it's recommend to do updates over Tor. It's slow and there are no leaks.

## Adding Host-Only Networking adapter to Whonix-Workstation / SSH into Whonix-Workstation ##
One might wish to access the Whonix-Workstation through SSH. Therefore one could add a second network adapter with [Host-Only Networking](http://www.virtualbox.org/manual/ch06.html#network_hostonly). Dangerous! Don't add another network adapter! Also potentially dangerous if any other VMs are running besides Whonix-Workstation! This would expose the mac address of your host to Whonix-Workstation.

The warning of VMware Host Only networking may also apply to Whonix:

*"If you install the proper routing or proxy software on your host computer, you can establish a connection between the host virtual Ethernet adapter and a physical network adapter on the host computer. This allows you, for example, to connect the virtual machine to a Token Ring or other non-Ethernet network.*

*On a Windows 2000, Windows XP or Windows Server 2003 host computer, you can use host-only networking in combination with the Internet connection sharing feature in Windows to allow a virtual machine to use the host's dial-up networking adapter or other connection to the Internet. See your Windows documentation for details on configuring Internet connection sharing."*

* (1) If you want to SSH or VNC your Whonix-Workstation your safest bet could be to do it from another Whonix-Workstation. If they are within the same virtual LAN, they can see each other.
* (2) Or you could run those services using [hidden services](https://sourceforge.net/p/whonix/wiki/Security/#hidden-services) and to access them though another Whonix-Workstation...
* (3) ...or from the host using the ordinary torification methods.
* (4) Alternatively you could from the host SSH into Whonix-Gateway (see [File Transfer]) and from there SSH into Whonix-Workstation. (If you are interested in that approach and need more information, try searching for "Chaining SSH" or "SSH hopping".)

In any case (3) and (4) you would weaken isolation between host and Whonix-Workstation.

# Installing additional software #
See [Install Software](https://sourceforge.net/p/whonix/wiki/Install%20Software/).

# Updating with extra care #
See [Install Software](https://sourceforge.net/p/whonix/wiki/Install%20Software/).

# Other Anonymizing Networks over Tor UDP Tunnel #
If you are [Tunneling UDP over Tor](https://sourceforge.net/p/whonix/wiki/OptionalConfigurations/#tunnel-udp-over-tor) to connect to [Other Anonymizing Networks](https://sourceforge.net/p/whonix/wiki/OtherAnonymizingNetworks/) you must read this chapter, otherwise you can skip this one.

Read first: [Tor Plus VPN or Proxy](https://trac.torproject.org/projects/tor/wiki/doc/TorPlusVPN) and [Whonix VPN disclaimer](https://sourceforge.net/p/whonix/wiki/Authorship/#whonix-vpn-disclaimer).

You should be aware, that because you need to install additional tunnel software (OpenVPN, etc.), once exploits are found, an attacker could target them.

However, when you are using a secure tunnel software (for example, OpenVPN, not PPTP), the Tor exit node may not read your communication with the VPN provider. It can only recognize, a encrypted VPN connection to the VPN provider.

The VPN provider can find out, depending on the other anonymizing network design, that you are connecting to that network. The VPN provider won't know you, but can find out, that someone is connecting over Tor.

The encryption of the tunnel software is not relevant, because the other anonymizing network most likely will make use of encryption itself. Subsequently neither the Tor exit node nor the VPN provider will know the content of your other anonymizing network connection. The usefulness of the information, the Tor exit node and the VPN provider can gather, is minimal.

"Normally Tor switches frequently its path through the network. When you choose a permanent destination X, you give away this advantage, which may have serious repercussions for your anonymity." as mentioned applies.

It's recommend to use a dedicated virtual machine for this activity, see [dedicated Whonix-Workstation](https://sourceforge.net/p/whonix/wiki/Security/#using-multiple-whonix-workstations).

# Advanced Security Guide #
For even more Security, see [Advanced Security Guide](https://sourceforge.net/p/whonix/wiki/Advanced%20Security%20Guide/).

# Footer #
[[include ref=WikiFooter]]