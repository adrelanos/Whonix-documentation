[[include ref=WikiHeader]]

[TOC]

= Grow Virtual Harddisk =

In case you need more disk space on your virtual harddisk... Good news is, you are still a Virtual Box user. Whonix is nothing special. It's just another vm image. Any suggestions you find about Virtual Box will also work for Whonix.

Somewhat difficult, there is no easy upstream solution, such as a gui and because you have no ''vdi'' disk. You have a vmdk disk. <sup>1</sup> There is also no better (free, Open Source) virtualizer with this feature. However, you do not need to be a genious. If you build Whonix from source this is a easier. <sup>2</sup> In case you are using the download version, it's a bit more difficult.

Unfortunately ''vboxmanage modifyhd <uuid|filename> --resize <size in mb>'' does not support vmdk images yet. (Perhaps that changes or has changed at your time of reading.)

<ol style="list-style-type: decimal;">
<li><p>On the host: Make a clone of all states of your existing virtual machine in case something goes wrong.</p></li>
<li><p>On the host: Delete all existing snapshots.</p></li>
<li><p>On the host: Find the folder of your virtual hdd.</p>
<p>vboxmange list hdds</p></li>
<li><p>On the host: Switch that folder.</p></li>
<li><p>On the host: Convert from ''vmdk'' to ''vdi''.</p>
<p>VBoxManage clonehd &quot;Whonix-Workstation-disk1.vmdk&quot; --format vdi &quot;Whonix-Workstation-disk1.vdi&quot;</p></li>
<li><p>See the syntax.</p>
<p>VBoxManage modifyhd</p></li>
<li><p>On the host: Grow the disk.</p>
<p>VBoxManage modifyhd &quot;Whonix-Workstation-disk1.vdi&quot; --resize 100000</p></li>
<li><p>On the host: Go to Virtual Box VM settings, mass storage, remove the old .vmdk, add the new .vdi.</p></li>
<li><p>Boot up and look if it's still working.</p></li>
<li><p>Until now we have only grew the physical size, we haven't changed the filesystem. Shut down again.</p></li>
<li><p>Inside VM: You have to boot from a boot cd (Ubuntu Precise ''DVD'' did work) and use some tool such as gparted to grow the filesystem. Start a terminal.</p>
<p>gksudo gparted</p></li>
<li><p>Inside VM: Grow filesystem. Apply and shut down.</p></li>
<li><p>Done.</p></li></ol>

<font size="-3"> <sup>1</sup> Because ''vmdk'' is the standard for ''ova'' images (exported virtual appliances). <sup>2</sup> Search the file whonix_createvm for ''VMNAME=&quot;Whonix-Workstation&quot;'' and ''VMSIZE=&quot;50G&quot;''. Increase ''VMSIZE=&quot;50G&quot;'' for example to ''VMSIZE=&quot;100G&quot;''. </font>

= Footer =

[[include ref=WikiFooter]]

