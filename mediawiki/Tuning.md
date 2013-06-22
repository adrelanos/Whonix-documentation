[[include ref=WikiHeader]]

[TOC]

= Tuning =

== Introduction ==

'''Everything absolutely optional. Mostly largely untested!'''

At the top of the ''Tuning chapter'' are the easier tuning steps. The farther you go down, the more skill will be required.

== Increase Virtual Machine RAM ==

If [https://sourceforge.net/p/whonix/wiki/Whonix%27s%20Protocol-Leak-Protection%20and%20Fingerprinting-Protection/#less-important-identifies less important identifiers] are not important to you, and this is most likely is very unimportant, you could use Virtual Box settings and increase the RAM for you Virtual Machine(s). Whonix-Workstation will profit most, if you run into low RAM. Also Whonix-Gateway could profit if you are creating big numbers of circuits and keep Tor busy. You can check how much RAM is free using ''free -m'' in Terminal.

== More CPU cores ==

On systems with multi-core processors, if [https://sourceforge.net/p/whonix/wiki/Whonix%27s%20Protocol-Leak-Protection%20and%20Fingerprinting-Protection/#less-important-identifies less important identifiers] are not important to you, and this is most likely is unimportant, you could increase the number of cores available to the Virtual Machine(s) in Virtual Box settings.

== Removing packages ==

For example you could experiment with uninstalling Nepomuk and virtuoso.

== Replacing desktop environment ==

You could even uninstall KDE and use your own desktop environment or only cli.

== Synthetic CPU ==

If [https://sourceforge.net/p/whonix/wiki/Whonix%27s%20Protocol-Leak-Protection%20and%20Fingerprinting-Protection/#less-important-identifies less important identifiers] are not important to you, you could try if deactivating the Synthetic CPU increases performance for you.

<pre>sudo -u $USERNAME VBoxManage modifyvm &quot;Whonix-Workstation&quot; --synthcpu off
sudo -u $USERNAME VBoxManage modifyvm &quot;Whonix-Gateway&quot; --synthcpu off</pre>
== Nested paging and VPIDs ==

You could increase performance by using Nested paging and/or VPIDs. It is unknown, if that may decease security or stability. See Virtual Box manual: [http://www.virtualbox.org/manual/ch10.html#nestedpaging Nested paging and VPIDs] for more information.

<pre>vboxmanage modifyvm Whonix-Workstation --largepages on
vboxmanage modifyvm Whonix-Gateway --largepages on

vboxmanage modifyvm Whonix-Workstation --vtxvpid on
vboxmanage modifyvm Whonix-Gateway --vtxvpid on</pre>
== Guest Additions ==

Not recommend for security reasons, but would improve performance, see [https://sourceforge.net/p/whonix/wiki/VirtualBox%20Guest%20Additions/ VirtualBox Guest Additions].

== Hardware-accelerated graphics ==

Requires Guest Additions, therefore not recommend, see above. Can increase performance.

See Virtual Box manual: [https://www.virtualbox.org/manual/ch04.html#guestadd-3d Hardware-accelerated graphics].

== Memory ballooning, Page Fusion, Memory overcommitment ==

Requires Guest Additions, therefore not recommend, see above. Can increase performance.

See Virtual Box manual: [https://www.virtualbox.org/manual/ch04.html#idp18673360 Memory overcommitment].

== 64 bit architecture ==

Several methods. The last method is probable the most useful one.

Maybe it would enhance security and/or performance by using an amd64 kernel. I don't know how much sense that makes when the rest of the system is still 32 bit.

<pre>sudo apt-get install linux-image-amd64</pre>
You could try to [http://wiki.debian.org/Multiarch/HOWTO Debian Multiarch HOWTO].

Or better create amd64 [https://sourceforge.net/p/whonix/wiki/BuildDocumentation/ builds yourself from source]. Just open the file ''int_whonix_image'' and look for ''--arch i386'' and replace ''i386'' with ''amd64''. I believe that is all you need to build amd64 builds, but it is untested.

== Optimized builds ==

Since the the concept behind Whonix isn't tied to anything, you could create your own implementation. Perhaps using Gentoo with optimized build flags for your system. See [https://sourceforge.net/p/whonix/wiki/Technical%20Introduction/#whonix-framework Whonix Framework], [OneVM] and [HardenedGentooTG].

== PCI passthrough ==

Might greatly improve graphics performance.; Might have security implications.

Essentially this feature allows to directly use physical PCI devices on the host by the guest even if host doesn't have drivers for this particular device. See Virtual Box Manual: [http://www.virtualbox.org/manual/ch09.html#pcipassthrough PCI passthrough].

= Footer =

[[include ref=WikiFooter]]

