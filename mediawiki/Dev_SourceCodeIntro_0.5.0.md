[[include ref=WikiHeader]]

[TOC]

= Introduction =

'''This page reflects 0.5.6! If you want to develop Whonix, rather get 0.6.0. ([Dev_SourceCodeIntro]).'''

This chapter is dedicated to give an introduction into the Whonix source code. '''''If you prefer to read and understand the source code just by reading scripts you may skip this optional chapter.''''' It can be quite difficult to get started with hacking existing big complex projects.

'''''Files and folders overview''''':

* '''whonix_gateway''' All files within that folder will be copied into Whonix-Gateway.
* '''whonix_workstation''' All files within that folder will be copied into Whonix-Workstation.
* '''whonix_shared''' All files within that folder will be copied into Whonix-Gateway and Whonix-Workstation.
* Copying files into the virtual machine images is done with whonix_craetevm and implemented in int_copy_gateway, int_copy_workstation and int_copy_shared.
* '''int_xxx''' scripts are internally used by whonix_xxx scripts.

'''''Overview''''':

(1.) [http://grml.org/grml-debootstrap/ grml-debootstrap] creates virtual machine images in '''.img''' image format. It keeps care of creating the image, the partition table, grub boot manager, minimal system debootstrap and apt-get installing all Whonix packages. This step requires most time in the build process.

(2.) A backup _copy of the .img gets created.

(3.) Files get copied into image.

(4.) whonix_internal_install_script runs inside chroot.

(5.) The '''.img''' image gets converted to a '''.vdi''' image. Actually not converted, a new file will be created and the old '''.img''' remains available until cleanup is run or manually deleted or grml-debootstrap runs again.

(6.) The '''.img''' format is more &quot;generic&quot;. Virtual Box does not support raw ('''.img''') images, but '''.vdi''' and '''.vmdk''' (and others).

(6.) A virtual machine (Virtual Box) will be created and the '''.vdi''' image will be attached.

(7.) The virtual machines get exported to a '''.ova''' images. (Technically the '''.ova''' format seams to require '''.vmdk''' files. Therefore Virtual Box automatically creates it. So anyone using or extracting the '''.ova''' image will see, that it it includes a '''.vmdk''' image.)

(8.) Steps (5.), (6.), (7.) and (8.) can be easily replaced or support for additional virtualizers can be added.

(9.) That's it, basically. Now we got '''.ova''' images, which can be imported by the user.

'''''More details:'''''

'''whonix_build''' is a script, which simply runs all other build steps. Actually it's &quot;optional&quot;. It has very little functionality beside running all other steps. You are free to run all steps one by one. That is useful for learning and for debugging purposes. In case you want to fix a bug or in case you want to upgrade the distribution or in case you want to switch the operating system or whatever you are better off running the steps manually. You can use the build script as a reference for which steps have to be run in which order. It has also a -fast switch, which skips the slow -createimg step.

'''whonix_createvm''' uses grml-debootstrap to create '''.img''', creates Virtual Box machines with all settings required for secure networking, devices, security settings. Which those settings are in details can be read in the script itself. It also features mounting the virtual hdd images for debugging reasons. The whonix_internal_install_script will be copied into the virtual machine images by &quot;''./whonix_createvm -tXcopyinto''&quot;. (Where X stands for g Gateway or w Workstation.) ''./whonix_createvm -help'' will show you available options and in which order all options have to be started.

'''whonix_internal_install_script''' A Whonix-Gateway specific version is stored under /home/user/Whonix/whonix_gateway/usr/local/share/whonix_internal_install_script and a Whonix-Workstation specific version is stored under /home/user/Whonix/whonix_gateway/usr/local/share/whonix_internal_install_script. This script gets copied into the Virtual Machines image by ''sudo ./whonix_createvm -tX-copyinto''. whonix_internal_install_script gets started by ''sudo ./whonix_createvm -tX-chroot''. They will transform the installed operating system into the Whonix-Gateway or into the Whonix-Workstation. They install the Tor Browser (only on Whonix-Workstation), set up relevant privacy and anonymity required settings.

'''''Summary:'''''

Thus, given the nature of the build step orientated scripts, you can easily work on the the different aspects of Whonix. For example, once you have created a clean virtual machine with the operating system only, you can make a clone or snapshot, run either the whonix_Gateway or the whonix_Workstation script as often as you need to test your changes and if something goes wrong, go back to the clone or snapshot. You don't have to build everything from scratch again. <sup>3</sup>

'''''Another Introduction:'''''

It's really not that difficult after all. If you like, you could read [Whonix Manual Installation], which is a similar topic, which covers part of this in other words.

<font size="-3"> ,, <sup>3</sup> If something would go wrong, you would have to reinstall the whole operating system every time again. That's why we use separate steps. </font>

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
= Footer =

[[include ref=WikiFooter]]

