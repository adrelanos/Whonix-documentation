[[include ref=WikiHeader]]

[TOC]

= Introduction =

This chapter is dedicated to give an introduction into the Whonix source code. '''''If you prefer to read and understand the source code just by reading scripts you may skip this optional chapter.''''' It can be quite difficult to get started with hacking existing big complex projects.

'''''Files and folders overview''''':

* '''whonix_gateway''' All files within that folder will be copied into Whonix-Gateway.
* '''whonix_workstation''' All files within that folder will be copied into Whonix-Workstation.
* '''whonix_shared''' All files within that folder will be copied into Whonix-Gateway and Whonix-Workstation.

'''Chroot Scripts'''

* /whonix_gateway/usr/local/share/whonix/chroot-scripts are run inside Whonix-Gateway
* /whonix_workstation/usr/local/share/whonix/chroot-scripts are run inside Whonix-Workstation
* /whonix_shared/usr/local/share/whonix/chroot-scripts are run inside Whonix-Gateway and Whonix-Workstation

'''build-steps'''

This is a high level overview. Whonix-Example-Implementation can currently be build in nine steps. (There is also a whonix_build script, which automates these eight steps for your convenience.)

* 15_prepare-build-machine
* 20_create-debian-img
* 25_backup-img
* 30_copy-into-img
* 32_verify_copied_files
* 35_run-chroot-scripts-img
* 40_convert-img-to-vdi
* 45_create-vbox-vm
* 50_export-vbox-vm

'''debug-steps'''

Some stuff to help developers with testing and debugging.

* delete-vbox-vm
* download-source
* interactive-img

'''help-steps'''

Boring methods, which are required by the build-steps above.

* mount-img
* mount-vdi
* chroot-img
* unchroot-img
* unmount-img
* unmount-img-force
* unmount-vdi
* unmount-vdi-force
* pre gets sourced by all other scripts.
* variables gets sourced by all other scripts.

'''whonix_build'''

Is a script, which simply runs all other build-steps. Actually it's &quot;optional&quot;. It has very little functionality beside running all other steps. You are free to run all steps one by one. That is useful for learning and for debugging purposes. In case you want to fix a bug or in case you want to upgrade the distribution or in case you want to switch the operating system or whatever you are better off running the steps manually. Run it with -help to see available switches. It has also -fast, -tg-fast and -tw-fast switch, which skips the slow 20_create-debian-img step.

'''''Overview''''':

(1.) 15_prepare-build-machine: installs build dependencies and applies a few other required settings for building from source.

(2.) 20_create-debian-img: [http://grml.org/grml-debootstrap/ grml-debootstrap] creates virtual machine images in '''.img''' image format. It keeps care of creating the image, the partition table, grub boot manager, minimal system debootstrap and apt-get installing all Whonix packages. This step requires most time in the build process.

(3.) 25_backup-img: A backup _copy of the .img gets created.

(4.) 30_copy-into-img: Files get copied into image.

(5.) 32_verify_copied_files: Verify that all files from Whonix source code have been copied into the image by using diff. This is just a sanity test.

(6.) 35_run-chroot-scripts-img: Chroot Scripts are applied.

(7.) 40_convert-img-to-vdi: The '''.img''' image gets converted to a '''.vdi''' image. Actually not converted, a new file will be created and the old '''.img''' remains available until cleanup is run or manually deleted or grml-debootstrap runs again.

The '''.img''' format is more &quot;generic&quot;. Virtual Box does not support raw ('''.img''') images, but '''.vdi''' and '''.vmdk''' (and others).

(8.) 45_create-vbox-vm: A virtual machine (Virtual Box) will be created and the '''.vdi''' image will be attached.

(9.) 50_export-vbox-vm: The virtual machines get exported to a '''.ova''' images. (Technically the '''.ova''' format seams to require '''.vmdk''' files. Therefore Virtual Box automatically creates it. So anyone using or extracting the '''.ova''' image will see, that it it includes a '''.vmdk''' image.)

'''''Modularity:'''''

Steps (2.), (6.), (7.), (8.) and (9.) could be easily replaced to add support for additional virtualizers, operating systems and so on. The numbers before the script names (20_..., 25_..., 30..., ...) are honored by whonix_build (using [http://manpages.ubuntu.com/manpages/raring/man8/run-parts.8.html run-parts]), which runs these steps in lexical order. Therefore you can easily add steps to the beginning or the end or even wretch steps in between.

'''''Summary:'''''

Thus, given the nature of the build step orientated scripts, you can easily work on the the different aspects of Whonix. For example, once you have created a clean virtual machine with the operating system only, you can make a copy, run either the gateway or the workstation copy routine or Chroot Scripts as often as you need to test your changes and if something goes wrong, go back to backup. You don't have to build everything from scratch again. <sup>3</sup>

'''''Another Introduction:'''''

It's really not that difficult after all. If you like, you could read [Whonix Manual Installation], which is a similar topic, which covers part of this in other words.

<font size="-3"> ,, <sup>3</sup> If something would go wrong, you would have to reinstall the whole operating system every time again. That's why we use separate steps. </font>

= gpg keys =

gpg public keys required for building Whonix are stored inside ''/home/user/Whonix/whonix_[...]/usr/local/share/whonix/gpg-pubkeys''. These include.

* adrelanos.asc - Whonix maintainer key - used for [whonixcheck] news verification
* erinn.asc - [https://www.torproject.org/docs/signing-keys.html.en obtained from torproject.org] - Used to verify downloads of Tor Browser by ''whonix_workstation/usr/local/bin/torbrowser''.
* sebastian.asc - same as erinn.asc.
* torprojectarchive.asc - Torproject's archive key https://www.torproject.org/docs/debian.html.en

To find out what the keys are good for, simply grep the source code.

<pre>cd /home/user/Whonix
grep -r adrelanos.asc *
grep -r erinn.asc *
grep -r sebastian.asc *
grep -r torprojectarchive.asc *</pre>
If you are in luck, you never have to update the keys yourself and the Whonix maintainer will keep them updated. Otherwise and also as a good precaution you can verify these keys manually. Follow the instructions form torproject.org to obtain the key. Then simply check if the keys match or update the old key with the new one.

Torproject's archive key expires '''2014-08-29'''.

<pre>gpg --fingerprint A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89
pub   2048R/886DDD89 2009-09-04 [expires: 2016-08-28]
      Key fingerprint = A3C4 F0F9 79CA A22C DBA8  F512 EE8C BC9E 886D DD89
uid                  deb.torproject.org archive signing key
sub   2048R/219EC810 2009-09-04 [expires: 2014-08-29]</pre>
= Debugging =

Stuff you may find helpful for debugging.

== Build Configuration ==

=== Skipping Build Steps ===

Rebuild the .ova images, while skipping the slow ''15_prepare-build-machine'' and ''20_create-debian-img'' steps. (Of course, this assumes, that these steps where run at least once previously.)

The &quot;''sudo ./build-steps/20_create-debian-img -tX''&quot; step takes far most of the build creation time. As long as no packages have been added or removed, you can repeat all other steps from a backup, which has been automatically created for you, by using.

<pre>sudo ./whonix_build -fast

## Or alternatively, if you only want to rebuild one machine.
#sudo ./whonix_build -tg-fast
#sudo ./whonix_build -tw-fast</pre>
=== Skipping Chroot Scripts ===

Some chroot-scripts, especially the 70_update_command_not_found and 70_torbrowser take very long, while they are non-critical. You can either run update-command-not-found and the Tor Browser Updater after Whonix has been build and booted, or if you don't wish to use them at all, just don't use it at all. Therefore you can conveniently disable them, to safe some time, which is useful for debug builds.

<pre>## NOTE: these variables must be set and exported as ROOT!
##       (Because the build script runs as root.)

export skip_scripts=&quot;70_update_command_not_found 70_torbrowser&quot;</pre>
This works for the following folders.

* [https://github.com/adrelanos/Whonix/blob/master/whonix_gateway/usr/local/share/whonix/chroot-scripts/ /whonix_gateway/usr/local/share/whonix/chroot-scripts/]
* [https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/usr/local/share/whonix/chroot-scripts/ /whonix_workstation/usr/local/share/whonix/chroot-scripts/]
* [https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/chroot-scripts/ /whonix_shared/usr/local/share/whonix/chroot-scripts/]

=== Target Architecture ===

Affects ''build-steps/20_create-debian-img''.

<pre>## NOTE: these variables must be set and exported as ROOT!
##       (Because the build script runs as root.)

## NOTE: Its impossible to create 64 bit builds on 32 bit hosts.
##       (This is a limitation of (grml-)debootstrap.)

## i386 is the default target architecture,
## if WHONIX_TARGET_ARCH variable is not set or empty.
#export WHONIX_TARGET_ARCH=&quot;i386&quot;

## Interesting target architecture for custom builds: 64 bit
## Despite it's name, works on AMD and Intel.
#export WHONIX_TARGET_ARCH=&quot;amd64&quot;

## Also interesting target architectures for custom builds: Kernel of FreeBSD
## Will not work out of the box for Whonix-Gateway, because Whonix Firewall
## is based on iptables (Linux) and the FreeBSD does not support iptables,
## its firewall is pf. The Whonix iptables rules would have to be rewritten in pf.
#export WHONIX_TARGET_ARCH=&quot;kfreebsd-amd64&quot;
#export WHONIX_TARGET_ARCH=&quot;kfreebsd-i386&quot;</pre>
= SSH =

* [https://sourceforge.net/p/whonix/wiki/File%20Transfer/#ssh-into-whonix-gateway SSH into Whonix-Gateway]
* [https://sourceforge.net/p/whonix/wiki/File%20Transfer/#ssh-into-whonix-workstation SSH into Whonix-Workstation]

= Mount and inspect images =

[https://sourceforge.net/p/whonix/wiki/File%20Transfer/#mount-and-inspect-images Mount and inspect images]

== Interactive Chroot ==

* Interactively chroot Whonix-Gateway.

Open a bash shell inside the Whonix-Gateway '''.img''' image.

<pre>sudo ./debug-steps/interactive-chroot-img -tg</pre>
* Interactively chroot Whonix-Workstation.

Open a bash shell inside the Whonix-Workstation '''.img''' image.

<pre>sudo ./debug-steps/interactive-chroot-img -tw</pre>
* Check Whonix version number.

Important before building builds for redistribution.

<pre>cat /home/user/Whonix/whonix_shared/usr/local/share/whonix/version</pre>
= Less Important Goodies =

== Unpacking '''.ova''' images ==

If you want for some reason to unpack an '''.ova''', for example to get the '''.vdmk''' image, you can use tar.

<pre>tar -xvf Whonix-Gateway.ova
Whonix-Gateway.ovf
Whonix-Gateway-disk1.vmdk</pre>
== Converting '''.vmdk''' images to '''.img''' images ==

<pre>#qemu-img info Whonix-Gateway-disk1.vmdk

qemu-img convert Whonix-Gateway-disk1.vmdk -O raw Whonix-Gateway.img

#qemu-img info Whonix-Gateway.img</pre>
= Porting =

This are some random notes about porting Whonix update debs to rpm.

What would have to be done:

* create rpm package
* add init scripts (currently done by debhelper)
* add man pages (currently done by debhelper and ronn, see debian/rules)

= Footer =

[[include ref=WikiFooter]]

