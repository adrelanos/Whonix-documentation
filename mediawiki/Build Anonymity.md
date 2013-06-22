[[include ref=WikiHeader]]

[TOC]

= Build Anonymity =

This does only apply, if you are going to build Whonix from source, and/or if you are going to redistribute Whonix and/or if you are going to use Physical Isolation. This is not a Whonix specific problem. Most projects do not even have a chapter about build anonymity. While building Whonix, software has to be downloaded. It's a unique selection of software and there is no way to make it non-unique. Therefore your '''i'''nternet'''s'''ervice'''p'''rovider (ISP) could guess, that you are building Whonix. This should not be of any concern in a free country (free by your own definition), if the content of your traffic is not being observed or logged.

Especially, but not exclusively, in case you want to redistribute Whonix, you might be interested to hide the fact, you are building Whonix (i.e. you want to stay anonymous).

To prevent any kind of personally identifiable or even fingerprintable information leaking from the build system into the Whonix images, it is recommended to build inside of an already torified Virtual Machine. <sup>1</sup> You can build Whonix inside an existing Whonix-Workstation, but it can also be built on a headless server.

It's also recommend to build in an already torified Virtual Machine, because that prevents leaks from the build system, which could help an attacker (with root access to the Whonix-Workstation), to gather identifiable information about that build system, that could ultimately lead back to your identity.

Beginning with Whonix 0.4.0, we use grml-debootstrap and chroot for virtual machine image creation. The grml-debootstrap source code tells, that it copies /etc/network/interfaces and /etc/resolv.conf into the chroot. grml-debootstrap also mounts a lot devices (/dev, /proc etc.) inside the chroot and later Whonix's chroot also mounts some devices. That's why it's recommend to build inside an already torified virtual machine.

Building from source code naturally also leaves local traces on the disk, such as the source code itself and build dependencies. If that is of concern to you, it can be more easily disposed, when it's contained in a Virtual Machine.

It would also possible to build directly on the host and torify all connections the scripts make, but we don't know what other grml-debootstrap/chroot related leaks there might be.

We know it's not the best solution to build inside a VM.

<font size="-3"> ,, <sup>1</sup> Yes, this creates a bootstrap, chicken or egg problem. To solve it you can either download already existing Whonix binary builds or if you prefer to build form source, build a minimal torified machine yourself first while running any network traffic over Tor. Any help required with that? [Contact] us. See also [Whonix Manual Installation]. </font>

== Virtual Box inside Virtual Box ==

Virtual Box inside Virtual Box is no longer required since 0.4.4. If you want to use it anyway, for example for testing the Virtual Machines inside Virtual Box, here are some suggestions.

Using ''vboxmanage &quot;Whonix-Workstation&quot; modifyvm --acpi on'' and ''vboxmanage &quot;Whonix-Workstation&quot; modifyvm --ioapic on'' for all VM's, i.e. for the build_Whonix-Workstation and the ones you build, speeds up the VM inside the VM a lot. That is already the default for Whonix Virtual Machines since version 0.2.0.

If you are going to use Virtual Box inside Virtual Box, be sure to change your host key. Virtual Box -&gt; Preferences -&gt; Input -&gt; Host Key. The &quot;outside&quot; and the &quot;inside&quot; Host Key must differ, otherwise you can not leave the VM &quot;inside&quot; anymore.

= Footer =

[[include ref=WikiFooter]]

