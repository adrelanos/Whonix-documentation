# Introduction #
Whonix's [DesignDocument] initially used [A Tor Virtual Machine Design and Implementation](https://svn.torproject.org/svn/torvm/trunk/doc/design.html) from Martin Peck, Kyle Williams and The Tor Project, Inc. as base.

It has been copied to the wiki and transformed with the aim to let it look as much as possible like the original. No changes are allowed to [DesignDocumentBase] beside correcter formatting.

All changes go to Whonix's own [DesignDocument].

[[include ref=WikiHeader]]

[TOC]

# original source #
Has been copied on Feb 22, 2012 from https://svn.torproject.org/svn/torvm/trunk/doc/design.html to [DesignDocumentBase].

# original design document - A Tor Virtual Machine Design and Implementation #
**Martin Peck**
<coderman at gmail dot com>

**Kyle Williams**
<kyle.kwilliams at gmail dot com>

Copyright © 2008-2009 The Tor Project, Inc.

February 27, 2009

# 1. Introduction #

This document describes a transparent Tor™ proxy design and implementation for Windows® and other operating systems using a virtual machine platform. An overview of the transparent proxy approach is provided in addition to design goals and implementation detail.

## 1.1. Privacy and Anonymity ##

Privacy is the ability to selectively disclose information about yourself and who you share it with. Tor is a privacy enhancing technology designed to provide low latency anonymity on the Internet against an adversary who can generate, modify, or delete traffic, run malicious Tor nodes, and perform other attacks against participants in the network.

Using the nymity slider as reference Tor aims to provide Unlinkable Anonymity for its users. A poor implementation of Tor may expose the user to set reduction attacks eroding privacy to Linkable Anonymity. A more effective attack could further degrade user privacy to Persistent Pseudonymity via a unique identifier, for example. And worst case side channel attacks that reveal origin IP address can void all of the privacy intent of the Tor software. These side channel or catastrophic attacks completely defeat the privacy goals of Tor and indicate a failure of the implementation.

## 1.2. Transparent Proxy Overview ##

A [transparent Tor proxy](http://wiki.noreply.org/noreply/TheOnionRouter/TransparentProxy) operates at the network and transport layers of of the OSI model instead of the usual application layer like SOCKS or HTTP. Intercepting and routing traffic in this manner avoids the risk of catastrophic side channel attacks that pose the most significant risk to privacy, particularly in a Windows environment.

Usability is also improved as manual SOCKS or HTTP proxy configuration is no longer necessary in each anonymized application. Software that does not support any kind of proxy feature can also be supported in this manner without any additional effort.

## 1.3. Virtual Machine Advantages ##

A virtual machine environment can further improve the security position by providing defense in depth against attacks which rely on using local applications to make requests to Tor that can compromise anonymity. This benefit is mainly achieved through the use of isolated network stacks in the host and guest OS. Separate stacks ensure that by default applications on one host cannot communicate with the other unless explicitly configured to do so. This is in contrast to the usual localhost idiom which assumes connections to/from 127.0.0.1 are protected from external threats.

Separate network stacks also simplify the implementation of a transparent proxy approach by using existing networking facilities to route traffic to the virtual machine as a default gateway instead of using more complicated traffic classification and redirection within the host network stack. This is important in a Windows environment where capabilities like Linux® netfilter or BSD® packet filter do not exist.

For Windows platforms offloading the TCP session intensive Tor process to a Linux guest with [edge triggered IO](http://monkey.org/~provos/libevent/) can significantly improve the performance of Tor and eliminate [socket buffer problems](http://wiki.noreply.org/noreply/TheOnionRouter/WindowsBufferProblems).

## 1.4. Application Isolation and Consistency ##

The use of multiple virtual machines to isolate application instances can protect against linkability of user communications by providing a consistent and trusted initial state for anonymous applications using a static virtual machine image to ensure that any changes made within that isolated environment are not persisted from one runtime instance to the next.

This fixed virtual machine state is critical for using otherwise dangerous software like browser plugins that can write persistent and unique identifying information to hard disk and relay this information to an attacker.

## 2. Tor VM Design ##

The transparent Tor proxy virtual machine must provide a usable and secure interface to the Tor network that preserves the unlinkable anonymity intent of Tor. A number of design criteria are necessary to achieve this goal.
2.1. Threat Model

A number of threats are expected when using the Tor network for anonymous communication over the Internet.

**Attacker Intent**
   ***Identify User Endpoint** 
    One goal of the attacker within this threat model is to obtain the Tor user origin IP address.

   ***Identify User Verinym** 
    The attacker may desire uniquely identifying user information like name and address stored on the host computer.

   ***Reduce Privacy to Persistent Pseudonym** 
    While not as useful as the identifying information above the attacker may wish to uniquely track the individuals using Tor even if their true identities remain unknown.
    
   ***Link Anonymous Communications** 
    The attacker may also attempt to correlate anonymous communications from the same user with each other. 

**Attacker Capabilities and Methods** 
   ***Proxy Bypass** 
    If the attacker can inject some kind of content to invoke a client request that bypasses application proxy settings they can achieve their goal of determining user endpoint. Social engineering attacks which entice a user to make a request that may bypass proxy settings are also included in this class of techniques.

   ***DNS Requests** 
    The attacker may also attempt to have the user application make a DNS request that does not resolve through Tor in order to expose the origin endpoint. This can often be accomplished when proxy settings are otherwise honored correctly.

   ***Combined Local and Remote Attacks** 
    Another effective attack vector is the use of local and remote resources in a coordinated attack against a client system. One example of this approach is injecting a malicious Java applet into web requests which in turn uses the sun.net.spi.nameservice.dns.DNSNameService and related parameters to request explicit DNS resolution from a DNS server on the local subnet. Many transparent proxy implementations that rely on the default route alone to direct traffic through Tor are vulnerable to this and other similar techniques.

   ***Partitioning Attacks** 
    The attacker may observe distinguishing characteristics of Tor user traffic to partition the anonymity set of some users over time into progressively smaller and smaller sets. When this set becomes a set of one individual they can [track individual activity](https://torbutton.torproject.org/dev/design/#fingerprinting) and likely achieve their goal of identifying user endpoint.

   ***Linking Attacks via Persistent State** 
    The attacker may use files or application state stored on disk to link separate instances of Tor use with each other. Note that unique identifiers or configuration associated with applications or operating system components can be used to link communications from the same user if exposed to an attacker.

   ***Fingerprinting Attacks** 
    The attacker may obtain as much information as possible about the application and environment it is running in to obtain a set of parameters unique to each pseudonym targeted.

   ***Full Remote Code Execution Attacks** 
    Vulnerabilities in applications or configuration may be exploited remotely for arbitrary execution of the attackers code. This will typically grant access to most of the files and configuration on the operating system. 

**Indefensible Attacks** 
   ***Tor Attacks** 
    Attacks which Tor cannot defend against, like a global passive adversary or traffic confirmation attacks, are obviously outside the scope of even the most robust Tor implementation.

   ***Some Remote Exploit and Arbitrary Execution Attacks** 
    Attacks which leverage an application or operating system flaw to gain full remote code execution on the host system are not defensible. This highlights the need for secure hosts when relying on Tor for anonymity. An untrusted host cannot provide a trusted Tor instance, regardless of how robust the implementation may be otherwise.

    The multiple virtual machine model provides defense in depth against these types of attacks and may constrain the scope of any compromise to the single virtual machine instance affected by the exploit. It is possible (though hard to quantify how difficult) to escalate from a compromised guest VM to secondary exploit of the host OS, again rendering all protections ineffective.

   ***Some Correlation Attacks** 
    If a Tor user interacts with the same site or service when using Tor and not using Tor it is likely trivial for an attacker to correlate the anonymous activity with the original user, and thus achieve their goal of identifying origin endpoint. Users must be aware of the absolute necessity of keeping anonymous services separate from directly accessed services and never mix the two.

    The ability to switch between anonymous and direct access to such services requires a strong separation of state, like that provided by [TorButton](http://torbutton.torproject.org/dev/design/), which is too complicated and restrictive to apply to the entire spectrum of applications and protocols that may be used over a transparent Tor proxy implementation. For this reason a "toggle" capability is explicitly not included in the design goals for this implementation. 

**Attacks Difficult to Defend Against Transparently** 

   ***Partitioning and Fingerprinting Attacks** 
    While side channel attacks can be thwarted effectively with a robust transparent Tor implementation it is more difficult to protect the content of the communications from partitioning or fingerprinting attacks. The use of TorButton and other such tools is encouraged to provide additional defense against these attacks. Application virtual machines may be difficult to implement for the full spectrum of applications in a way that defeats these attacks.

   ***The Faithless Endpoint** 
    Another difficult problem for Tor implementations is the opportunity for malicious exit nodes to observe and manipulate traffic from their router to compromise user privacy and security. [The Faithless Endpoint](https://svn.torproject.org/svn/torvm/trunk/doc/design.html) details a number of risks that users may not be aware of.

    Educating the user about these risks in an intuitive manner and providing them tools to prevent unintended exposure to malicious participants in the Tor network is a complicated effort and outside the scope of this implementation. 

# 2.2. Design Requirements #

The risks identified in the threat model above drive a number of design criteria necessary to thwart or mitigate compromise of user privacy.

**Transparent Proxy Requirements** 
   **1. Proxy All TCP and DNS Traffic** 
    All TCP and DNS traffic must be routed through the Tor VM without fail. This requires that no local subnets be exposed on the host network stack once started to prevent the combined local and remote DNS exploits described above.
    
   **2. Filter Remaining Traffic** 
    Traffic that is not TCP or DNS must be dropped at the Tor VM instance to prevent forwarding potentially sensitive multicast, ICMP, or other datagrams to the upstream router(s). Likewise certain protocols, like SMTP and NetBIOS, should be filtered as soon as they leave the host.

   **3. Fail Safely** 
    If the Tor VM is unable to proxy traffic it must not let the traffic through unaltered, but instead present an error to the user via the user interface describing the nature of the failure to communicate and possible remedies if any. 

**Virtual Machine Requirements**
   **1. Open Source** 
    While VMware® is one of the more friendly and stable VM implementations, particularly with respect to bridged networking on Windows, it lacks the transparency necessary for a robust security position and also precludes bundling into a portable Tor VM.

   **2. Bridged Network Adapter Support** 
    To support the widest range of client uses a bridged network adapter is required within the Virtual Machine implementation used by Tor VM. Many of the potential VM platforms support this mode of operation via the WinPcap driver.

   **3. Low Host OS Overhead** 
    A VM platform that provides low host memory and CPU consumption improves the usability and stability of Tor VM in addition to making it suitable for a wider range of older or less powerful hardware users may have. This is particularly important for graphical applications and other media intensive virtual machine instances.

   **4. VM Isolation and Integrity Protections** 
    The ability to run multiple VM instances for application runtime isolation and defense in depth against unknown application or guest operating system vulnerabilities is required. Kernel level VM acceleration is potentially useful, however, the expanded attack surface presented by such acceleration layers should be considered carefully. 

**Host Requirements**
   **1. IP Routing Through Tor VM** 
    All operating systems that are able to run Tor should be able to route traffic in the manner required for transparent proxy through the virtual machine. Using the combined bridge and tap adapter configuration there is no need to rely on VPN or DHCP resources for Tor VM functionality; basic IP interface configuration and IP routing facilities are all that is necessary.

   **2. Privilege Separation** 
    To obtain the most benefit of a transparent virtual machine implementation host access controls and privilege separation should be used to  constrain the capabilities of the implementation and the applications used with it. Newer Windows versions go beyond the typical owner / group based distinction into fine grained access control which may be useful.

**User Interface Requirements**
   **1. Native GUI Controller (Vidalia)** 
    Vidalia is an existing feature rich and well known controller for Tor on Windows and other operating systems that would provide much of the interface desired. This requires that an acceptably secure method of allowing control port access to the Tor instance in the VM could be implemented.

    A hashed control password generated randomly at start is used by Vidalia to authenticate to Tor. This is passed to the VM kernel but never stored on disk. This would allow control port access without connection behavior changes with the limitation that any Vidalia restart requires a restart of the VM as well. 

# 3. Tor VM Implementation #

A solution that satisfies these requirements can be implemented using a variety of GNU/Linux and Win32 software. The open source licenses associated with these tools ensure that adequate scrutiny of the code base supporting a Tor virtual machine is possible for those who choose to evaluate it.

# 3.1. Build Environment #

The following dependencies are required for building the Tor VM image and supporting VM tools.

**Linux Build Environment** 
   **OpenWRT Distribution** 
    [OpenWRT](http://openwrt.org/) provides a full cross compile toolchain and Linux image build tools including the initramfs with all the usual system and networking tools. Creating a minimal kernel image with only the functions and linkage needed reduces the compiled bootable image size and helps reduce host OS resource usage.

    The full toolchain build is configured by default for broad build platform support. Debian based Linux systems are the best supported build platforms on i386, x86-64, UltraSparc, and PowerPC architectures for the OpenWRT kernel builds. 

**Windows Platform and Build Tools**
   ** Windows XP™** 
    Windows XP is used to build the Qemu virtual machine with all necessary patches and libraries required for a portable Tor VM implementation. The build process creates a CDROM ISO image that can be used with a Windows VM or host to automate the build environment preparation and Qemu compilation.

   **Windows Vista™ and Windows Server 2008™** 
    Windows Server 2008 Core (GUI-less) is well suited for automated builds. Either platform may be used to compile the Windows Tor VM package.
    Microsoft Windows Driver Development Kit

    The Windows DDK distribution is required for building the TAP-Win32 and WinPcap kernel drivers.

   **MingW and MSYS**
    The Minimalist GNU for Windows packages are used to build Qemu and supporting software. The source packages and build scripts are packaged together with an autorun batch file for automated builds. 

## 3.2. Virtual Machine Software ##

Two virtual machine implementations were considered and tested: [coLinux](http://www.colinux.org/) and [Qemu](http://bellard.org/qemu/). Bridged networking adapter support is available in both implementations and the GPL license applied to each code base satisfies the open source requirement.

The coLinux cooperative virtual machine provides low CPU and memory consumption relative to other vm implementations by running the Linux kernel as a process in ring0 on the host. This method of virtualization exposes a greater risk to stability and security on the host OS given the direct execution and lack of memory protection between the two operating system instances.

Qemu on the other hand provides full CPU emulation for much stronger host / guest isolation and does not require any changes to the guest kernel or system level drivers on the host. For these reasons Qemu is preferred for the virtual machine implementation despite the increased CPU and memory overhead associated with full emulation.

Both solutions provide bridged network devices via the WinPcap driver and point-to-point connections using the Tap32 adapter.

## 3.3. Tor VM Patchset ##

A number of patches are necessary for the implementation of Tor VM using the tools identified in this document. These modifications are provided as a series of small patches (patch set) for greater transparency into the modifications applied with the intent of adoption by upstream maintainers for these projects where appropriate. This will help reduce the maintenance required for up to date builds of the Tor VM implementation.

**Qemu Patches** 
   ** WinPcap Bridge Support** 
    qemu-winpcap-0.9.1.patch

   ** Kernel Command Line via STDIN** 
    qemu-kernel-cmdline-from-stdin.patch

**OpenWRT Patches** 
   **Superfluous Code Reduction** 
    kamikaze-mod-basefiles.patch 
    kamikaze-mod-kernel-config.patch 
    kamikaze-build-config.patch 

   **Tor Package and Supporting Libraries** 
    kamikaze-tor-package.patch
    kamikaze-libevent-package.patch

**WinPcap Patches** 
   **Portable Driver Layer** 
    winpcap-tor-device-mods.patch

**OpenVPN TAP-Win32 Patches**
   **Portable TAP-Win32 Network Device Driver** 
    openvpn-tor-tap-win32-driver.patch

## 3.4. Tor VM Build ##

    # IMPORTANT: You will need about 2G of space for a full build.
    #
    svn export https://svn.torproject.org/svn/torvm/trunk/ torvm
    cd torvm
    echo View the README file in this directory for detailed build instructions

## 3.5. Tor Configuration ##

Torrc config file: (User, Group, PidFile, DataDirectory, Log all set according to host disk configuration and not listed here.)

    RunAsDaemon 1
    TransListenAddress 0.0.0.0
    TransPort 9095
    DNSListenAddress 0.0.0.0
    DNSPort 9093

## 3.6. Persistent Storage ##

Many protections built into Tor to protect against various types of attacks against Tor client anonymity rely on a persistent data storage facility of some kind that preserves cached network status, saved keys and configuration, and other critical capabilities. There are a number of ways to configure the virtual disk storage for the VM based on the role of the node in the network and the environment where it resides.

**Virtual Block Device** 
   **Virtual IDE Hard Disk** 
    A virtual disk image is provided with the Qemu build that contains an empty XFS file system. This file system is mounted at boot and used to store persistent Tor configuration and data, in addition to other system state, like /dev/random seed. 

   **Loop-AES Privacy Extensions** 

    .

   **GNU Privacy Guard Passphrase Authentication** 

    .

   **Loop-AES Disk Key Generation, Storage, and Authorization**

    .

## 3.7. Host Virtual Machine Integration ##

Usability is a critical part of any Tor implementation. Providing a responsive and intuitive interface for the Tor implementation and the applications routing through it is a particularly difficult problem in the context of the threats detailed above.

Any effective methods of improving usability should be considered.

**Virtual Machine and Application Management**
   **Tor VM Process Launcher**
    A portable Tor VM implementation requires a number of driver and network configuration tasks integrated into a application to manage the TAP-Win32 and WinPcap device driver installation and removal, as well as virtual machine instance configuration, activation, and monitoring. A parent process to manage these details is provided as a native win32 application without external library or installation requirements.

   **Run As Service**
    The ability to run a persistent instance of a Tor VM as a service on the host would also be useful.

   **KQemu Accelerator**
    Kernel level virtual machine acceleration is particularly useful for running graphical applications with SVGA displays and high color depth. The KQemu accelerator can provide a useful performance increase for these graphical applications. 

**Application Window Based Multi-VM Model**
   **MingW X Display**

    .

   **Lightweight X Application VMs**

    .

**Windows Application Isolation VM**
   **Read-Only Guest OS Images**

    .

   **Wine Win32 API Implementation**

    .

   **Minimal Windows Guest VM**

    .

## 3.8. Network Configuration ##

A robust transparent Tor proxy implementation requires careful configuration of the routing and filtering of traffic on both the host and guest OS instances. Unfortunately Windows does not support [/31 style point-to-point](http://rfc.net/rfc3021.html) links so a two host address /30 subnet is used.

   **Bridged Adapter Endpoint Pivot**

    .

   **Win32 Tap Adapter**

    .

   **Inter-VM Host Only VLANs**

    .

   **Linux Traffic Redirection**

    .

## 3.9. User Interface ##

    .

# 4. Legal Notice #
You may distribute or modify this document according to the terms of the [GNU Free Documentation License Version 1.2 or later](http://www.gnu.org/licenses/fdl-1.2.txt). 
"BSD® is a registered trademark of UUnet Technologies, Inc." 
"Linux® is the registered trademark of Linus Torvalds in the U.S. and other countries." 
"Tor® is a registered trademark of The Tor Project, Inc." 
"VMware® is a registered trademark of VMware, Inc. in the United States and other jurisdictions." 
"Windows® is a registered trademark of Microsoft Corporation in the United States and other countries."

# Footer #
[[include ref=WikiFooter]]