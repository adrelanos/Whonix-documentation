[[include ref=WikiHeader]]

[TOC]

# Grow Virtual Harddisk #

In case you need more disk space on your virtual harddisk... Good news is, you are still a Virtual Box user. Whonix is nothing special. It's just another vm image. Any suggestions you find about Virtual Box will also work for Whonix.

Somewhat difficult, there is no easy upstream solution, such as a gui and because you have no *vdi* disk. You have a vmdk disk. ^1^ There is also no better (free, Open Source) virtualizer with this feature. However, you do not need to be a genious. If you build Whonix from source this is a easier. ^2^ In case you are using the download version, it's a bit more difficult.

Unfortunately *vboxmanage modifyhd <uuid|filename> --resize <size in mb>* does not support vmdk images yet. (Perhaps that changes or has changed at your time of reading.)

(1) On the host: Make a clone of all states of your existing virtual machine in case something goes wrong.

(2) On the host: Delete all existing snapshots.

(3) On the host: Find the folder of your virtual hdd.

    vboxmange list hdds

(4) On the host: Switch that folder.

(5) On the host: Convert from *vmdk* to *vdi*.

    VBoxManage clonehd "Whonix-Workstation-disk1.vmdk" --format vdi "Whonix-Workstation-disk1.vdi"

(6) See the syntax.

    VBoxManage modifyhd

(7) On the host: Grow the disk.

    VBoxManage modifyhd "Whonix-Workstation-disk1.vdi" --resize 100000

(8) On the host: Go to Virtual Box VM settings, mass storage, remove the old .vmdk, add the new .vdi.

(9) Boot up and look if it's still working.

(10) Until now we have only grew the physical size, we haven't changed the filesystem. Shut down again.

(11) Inside VM: You have to boot from a boot cd (Ubuntu Precise *DVD* did work) and use some tool such as gparted to grow the filesystem. Start a terminal.

    gksudo gparted

(12) Inside VM: Grow filesystem. Apply and shut down.

(13) Done.

<font size="-3">
^1^ Because *vmdk* is the standard for *ova* images (exported virtual appliances).
^2^ Search the file whonix_createvm for *VMNAME="Whonix-Workstation"* and *VMSIZE="50G"*. Increase *VMSIZE="50G"* for example to *VMSIZE="100G"*.
</font>

# Footer #
[[include ref=WikiFooter]]