[[include ref=WikiHeader]]

[TOC]

= Security Overview =

All methods:

* Risk of transferring [Metadata] or other sensitive information into Whonix-Workstation.
* Whonix is about isolation. If you import data from the host or other media into Whonix-Workstation you weaken isolation and must be very careful.

Shared Folder:

* Using filesharing built into Virtual Box (Shared Folder) isn't very secure.
* It requires installing [https://sourceforge.net/p/whonix/wiki/VirtualBox%20Guest%20Additions/ Virtual Box Guest Additions] and therefore weakens security.

SSH:

* Works with ssh, scp, sshfs. Instructions below.

ISO Images, Host -&gt; Whonix-Gateway/Workstation:

* Safest method of getting files into Whonix-Workstation.

USB devices plugged into Virtual Box:

* Hardware serials of the USB controller and/or USB device could leak into Whonix-Workstation.
* Requires closed source Virtual Box extensions.

Mounting Virtual Machine images:

* No idea if and if yes, what could leak into the Virtual Machine image.
* See also [https://sourceforge.net/p/whonix/wiki/Build%20Anonymity/ Build Anonymity].

= Transfer files from the Host into Whonix-Gateway or Whonix-Workstation through ISO images =

On the host...

Install genisoimage:

<pre>sudo apt-get install genisoimage</pre>
To create an iso &quot;files.iso&quot; containing the content of &quot;folder&quot;:

<pre>mkisofs -o files.iso /path/to/folder</pre>
Use the Virtual Box graphical user interface to mount your newly created iso a virtual VM CD/DVD drive.

Inside Whonix-Workstation...

Create the folder /media/cdrom.

<pre>sudo mkdir -p /media/cdrom</pre>
Now attach the iso to the VM. Mount it with

<pre>sudo mount /dev/sr0 /media/cdrom</pre>
Get into that folder.

<pre>cd /media/cdrom</pre>
See your files.

<pre>dir</pre>
This is intentionally one-way as the Whonix-Workstation is inherently untrusted and should remain isolated to prevent side-channel attacks and covert channel leaks.

= Adding USB device to Virtual Box =

This is recommend against for security reasons.

Does '''not''' require Virtual Box Guest Additions.

Please read the chapter [https://sourceforge.net/p/whonix/wiki/About/#whonix-is-based-on-debian-virtualbox-and-tor Whonix is based on Debian, VirtualBox and Tor].

Means, you can change your search terms from &quot;How to get USB in Whonix-Workstation?&quot; to &quot;How to get USB in Virtual Box?&quot;.

Anyway, Virtual Box does not support USB out of the box. There are closed source additional extensions for usb support. You can download them from the [https://www.virtualbox.org/wiki/Downloads Virtual Box download page].

Install them on the host.

I don't know if reboot is required. Then you can plug USB devices into Virtual Machines through the device menu in Virtual Box.

Note, that automount of USB devices is disabled in Whonix by default. Try, Start menu -&gt; System Settings -&gt; Removable Media or manually mount. [https://sourceforge.net/p/whonix/discussion/general/thread/3b4b67c2/ Please share your results.]

= Shared Folder =

See [https://sourceforge.net/p/whonix/wiki/VirtualBox%20Guest%20Additions/ Virtual Box Guest Additions] chapter.

= SSH into Whonix-Gateway =

'''Developers / experts only! Only for debugging!'''

On Whonix-Gateway: Open /usr/local/bin/whonix_firewall

<pre>sudo nano /usr/local/bin/whonix_firewall</pre>
Set GATEWAY_ALLOW_INCOMMING_SSH to 1.

<pre>GATEWAY_ALLOW_INCOMMING_SSH=1</pre>
Restart firewall.

<pre>sudo /usr/local/bin/whonix_firewall</pre>
Inside Whonix-Gateway:

<pre>## Run once.
sudo apt-get install openssh-server</pre>
On the host: Add port forwarding from host into Virtual Machine.

<pre>## Open a terminal.
## Run once.
## This forwards connection from the host to 127.0.0.1:2200 to
## the SSH server running inside Whonix-Gateway on port 22.
VBoxManage modifyvm &quot;Whonix-Gateway&quot; --natpf1 &quot;ssh&quot;,tcp,127.0.0.1,2200,,22

## If you ever want to undo this...
#VBoxManage modifyvm &quot;Whonix-Gateway&quot; --natpf1 delete &quot;ssh&quot;</pre>
On the host: Open a ssh session.

<pre>## as user
ssh user@127.0.0.1 -p 2200
## or as root
ssh root@127.0.0.1 -p 2200</pre>
On the host: Or mount Whonix-Gateway as a folder.

<pre>## as user
sshfs user@127.0.0.1:/ -p 2200 /home/user/whonix_binary/whonix-Gateway_sshfs
## or as root
sshfs root@127.0.0.1:/ -p 2200 /home/user/whonix_binary/whonix-Gateway_sshfs</pre>
= SSH into Whonix-Workstation =

'''Developers / experts only! Only for debugging!'''

You can not directly SSH into Whonix-Workstation, because Whonix-Workstation has only an internal network interface and no NAT interface. Adding one would defeat the purpose of Whonix. (See [Security Guide] for details why.)

Required: You mastered the steps &quot;SSH into Whonix-Gateway&quot; above.

Connection will look like this: host -&gt; ssh -&gt; Whonix-Gateway -&gt; ssh -&gt; Whonix-Workstation.

On Whonix-Workstation:

<pre>sudo apt-get install openssh-server</pre>
On the Whonix-Gateway:

<pre>## or user@
/usr/bin/ssh root@192.168.0.11</pre>
Then SSH from the host into Whonix-Gateway (host -&gt; Whonix-Gateway). From there, SSH into Whonix-Workstation (Whonix-Gateway -&gt; Whonix-Workstation). You can also do that with one command (called SSH hopping).

<pre>## or root@
ssh -t user@127.0.0.1 -p 2200 &quot;ssh user@192.168.0.11&quot;</pre>
You can also mount the filesystem of Whonix-Workstation with two commands. SSH hopping is also possible for sshfs (a website [http://www.larkinweb.co.uk/computing/mounting_file_systems_over_two_ssh_hops.html told] ([http://www.webcitation.org/6FDYtApEP w]) me).

<pre>## or root@

## SSH into Whonix-Workstation and map to localhost:2222.
ssh -f user@127.0.0.1 -p 2200 -L 2222:192.168.0.11:22 -N

## Mount Whonix-Workstation folder on the host.
sshfs -p 2222 user@localhost:/remote/path /mnt/localpath</pre>
= Mount and inspect images =

== Introduction ==

'''Developers / experts only! Only for debugging!'''

Required knowledge:

* You don't have to use this method. Standard ''vdi'' (or ''img'') images are used. Feel free to mount them using any other way you like.
* Mount and inspect images has been researched for only for Linux hosts. Not saying it's impossible on Windows, but it's not documented.
* You must understand [Dev_SourceCodeIntro] / Overview, i.e. understand for what ''img'' and for what ''vdi'' images are used.
* You need some dependencies, see chapter [https://sourceforge.net/p/whonix/wiki/BuildDocumentation_0.4.0/#building-on-linux Building on Linux].
* You need the Whonix source code, see chapter [https://sourceforge.net/p/whonix/wiki/BuildDocumentation_0.4.0/#get-the-whonix-source-code Get the Whonix source code].
* [https://sourceforge.net/p/whonix/wiki/BuildDocumentation_0.4.0/#verify-the-whonix-source-code-with-gpg Verify the Whonix source code with gpg] is not required, but recommend.

== VDI ==

=== Mount Whonix-Gateway ''vdi'' images. ===

Using the git stable branch.

<pre>sudo ./whonix_createvm -tg-mountvdi

cd &quot;/home/user/whonix_binary/whonix-Gateway_image&quot;
## inspect
cd ~

sudo ./whonix_createvm -tg-unmountvdi</pre>
Using the development stable branch.

<pre>sudo ./help-steps/mount-vdi -tg

cd &quot;/home/user/whonix_binary/whonix-Gateway_image&quot;
## inspect
cd ~

sudo ./help-steps/unmount-vdi -tg</pre>
=== Mount Whonix-Workstation ''vdi'' images. ===

Using the git stable branch.

<pre>sudo ./whonix_createvm -tw-mountvdi

cd &quot;/home/user/whonix_binary/whonix-Workstation_image&quot;
## inspect
cd ~

sudo ./whonix_createvm -tw-unmountvdi</pre>
Using the development stable branch.

<pre>sudo ./help-steps/mount-vdi -tw

cd &quot;/home/user/whonix_binary/whonix-Gateway_image&quot;
## inspect
cd ~

sudo ./help-steps/unmount-vdi -tw</pre>
== IMG ==

=== Mount Whonix-Gateway ''img'' images. ===

Using the git stable branch.

<pre>sudo ./whonix_createvm -tg-mountimg

cd &quot;/home/user/whonix_binary/whonix-Gateway_image&quot;
## inspect
cd ~

sudo ./whonix_createvm -tg-unmountimg</pre>
Using the development stable branch.

<pre>sudo ./help-steps/mount-img -tg

cd &quot;/home/user/whonix_binary/whonix-Gateway_image&quot;
## inspect
cd ~

sudo ./help-steps/unmount-img -tg</pre>
=== Mount Whonix-Workstation ''img'' images. ===

Using the git stable branch.

<pre>sudo ./whonix_createvm -tw-mountimg

cd &quot;/home/user/whonix_binary/whonix-Workstation_image&quot;
## inspect
cd ~

sudo ./whonix_createvm -tw-unmountimg</pre>
Using the development stable branch.

<pre>sudo ./help-steps/mount-img -tw

cd &quot;/home/user/whonix_binary/whonix-Gateway_image&quot;
## inspect
cd ~

sudo ./help-steps/unmount-img -tw</pre>
== VMDK ==

Not yet documented. Please share.

== Related ==

* [https://sourceforge.net/p/whonix/wiki/Dev_SourceCodeIntro/#converting-vmdk-images-to-img-images Converting .vmdk images to .img images]
* [https://sourceforge.net/p/whonix/wiki/Dev_SourceCodeIntro/#unpacking-ova-images Unpacking .ova images]

= Footer =

[[include ref=WikiFooter]]

