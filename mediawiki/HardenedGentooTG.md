[[include ref=WikiHeader]]

[TOC]

= DRAFT! =

'''Draft! Development for Hardened Gentoo based Whonix-Gateway stalled. Debian based gateway still under active development and other operating systems are being considered.'''

= How to create a Hardened Gentoo based Whonix-Gateway =

== Overview ==

* Install Gentoo build environment (how-to is for installation in a chroot but you can also use a full gentoo installation)
* Build Whonix-Gateway kernel and userland
* Install on media/export to iso/ova (TODO)

Advantages/disadvantages compared to the default Debian/Ubuntu based T-G:

* Updating is much more complicated:
* You need to keep a build system around, keep that updated using emerge-webrsync &amp;&amp; emerge --update --newuse --deep -av world (and probably etc-update)
* you need to update the t-g system on the build system (append --update --newuse --deep to that long emerge command [/Dev/HardenedGentooTG#BuildWhonix-Gatewayenvironment below])
* you need to build new kernels manually
* then you need to copy the new files over your current installation (simple but inefficient: 'cd path/to/torgateway &amp;&amp; tar zcvf update.tgz .' extract: 'tar xvzpf update.tgz')
* emerge is not apt-get, updates often require a bit of manual configuration, review /var/log/portage/elog/summary.log
* Grsec, full pie, no RBAC (hardly necessary considering the threat model of the gateway), no disk encryption, no RAM wipe on shutdown (help would be welcome). When not using hidden services, tor log and cache files can be put into tmpfs so we don't need FDE at all. Otherwise we can still use partial disk encryption (loop file or /var). Evil maid attacks apply anyway as long as there's an unencryped /boot (and BIOS, and firmware...) and no TPM.
* Size: &lt;50 MB compressed.

= Install Gentoo build environment =

Read Upstream Documentation: [http://www.gentoo.org/doc/en/handbook/ Gentoo Handbook]!

<pre># If you use a grsec kernel on the host:

echo &quot;0&quot; &gt; /proc/sys/kernel/grsecurity/chroot_deny_chmod
echo &quot;0&quot; &gt; /proc/sys/kernel/grsecurity/chroot_caps

mkdir gentoodev
cd gentoodev
# verify fingerprints!
gpg --keyserver subkeys.pgp.net --recv-keys 96D8BF6D 2D182910 17072058

# fetch stage3 and portage snapshot
LATESTDL=`wget -q http://distfiles.gentoo.org/releases/x86/autobuilds/latest-stage3-i686.txt -O - | tail -1`
wget http://distfiles.gentoo.org/releases/x86/autobuilds/$LATESTDL{,.DIGESTS.asc,.DIGESTS}
wget http://distfiles.gentoo.org/releases/snapshots/current/portage-latest.tar.bz2{,.gpgsig,.md5sum}

gpg --verify stage3-*.tar.bz2.DIGESTS.asc
sha1sum -c stage3*.tar.bz2.DIGESTS

gpg --verify portage-latest.tar.bz2.gpgsig portage-latest.tar.bz2
md5sum -c portage-latest.tar.bz2.md5sum

tar xvjpf stage3-*.tar.bz2
tar xvjf portage-latest.tar.bz2 -C usr

# edit makeopts according to your CPU count (cores+1); add a nearby mirror (when using a gentoo install disk use #mirrorselect -i -o &gt;&gt; etc/make.conf
echo '
MAKEOPTS=&quot;-j3&quot;
USE=&quot;unicode minimal crypt ssl gpm ncurses fbcon -X -pam -cracklib -git -extensions     -glib -opengl \
-icu -readline -xcb -fts3 -png -policykit -gtk -crashreporter -startup-notification \
-dbus -introspection -libnotify -webm -gnome -qt4 -qt3support -kde -bluetooth -nls     -ipv6 \
-cups -zeroconf -encode -recode -acl -iconv -tcpd -berkdb -pcre -net -cramfs -sqlite -gdbm&quot;
FEATURES=&quot;webrsync-gpg nodoc noinfo noman&quot;
PORTAGE_GPG_DIR=&quot;/etc/portage/gpg&quot;
SYNC=&quot;&quot;
#GENTOO_MIRRORS=&quot;&quot;' &gt;&gt; etc/make.conf

cp -L /etc/resolv.conf etc/
mount -t proc none proc/
chroot . /bin/bash
env-update
source /etc/profile
export PS1=&quot;(build-chroot) $PS1&quot;

# set root passwd (just used in the development environment, probably not necessary?)
passwd

eselect profile list
# select hardened/linux/x86
eselect profile set 8

echo &quot;en_US ISO-8859-1&quot; &gt;&gt; /etc/locale.gen
locale-gen
cp /usr/share/zoneinfo/UTC /etc/localtime

# get a hardened toolchain
emerge --oneshot binutils gcc virtual/libc
source /etc/profile
export PS1=&quot;(build-chroot) $PS1&quot;

# Configure emerge-webrsync. Verify fingerprints!
emerge gnupg
mkdir -p /etc/portage/gpg
chmod 0700 /etc/portage/gpg
gpg --homedir /etc/portage/gpg --keyserver subkeys.pgp.net --recv-keys 0x239C75C4 0x96D8BF6D
gpg --homedir /etc/portage/gpg --edit-key AE5454F967B56AB09AE160640838C26E239C75C4 trust
gpg --homedir /etc/portage/gpg --edit-key DCD05B71EAB94199527F44ACDB6B8C1F96D8BF6D trust

# update portage with
emerge-webrsync</pre>
== Build a Kernel for Whonix-Gateway ==

<pre>emerge hardened-sources
cd /usr/src/linux
make menuconfig
make 
# or, if you use loadable modules:
# make &amp;&amp; make modules_install 
cd </pre>
Some hints:

* when using modules make sure that stuff needed to mount root is built in:
* SCSI disk support
* ext4
* SATA BDMA (you need to know your hardware)
* enable netfilter support (use advanced and enable pretty much everything, save to exclude: protocol specific connection trackers)
* enable grsecurity
* security level? (I've only tested workstation, server should work, maybe even High
* disable ipv6
* save to disable (always depending on hardware)
* pci express, pcmcia
* wifi, bluetooth
* amateur radio, RF
* RAID/LVM
* AGP graphics
* sound
* File systems (ext2,3, xfs, jfs, ntfs, nfs...)
* graphic drivers (DRI...)

== Build Whonix-Gateway environment ==

<pre>mkdir /torgateway

emerge gzip baselayout coreutils debianutils diffutils ed file findutils gawk grep groff kbd less iptables \
module-init-tools net-tools openrc sed shadow sysvinit sys-apps/texinfo util-linux     which e2fsprogs udev procps psmisc iputils  \
bash nano tor torsocks localepurge grub dhcpcd \
-v --root /torgateway

mkdir -p /torgateway/{sys,proc,dev,boot,root,home,var/run,var/log,var/lib/run/tor,var/log/tor}

echo &quot;tor:x:101:246:added by portage for tor:/var/lib/tor:/sbin/nologin&quot; &gt;&gt; /torgateway/etc/passwd
echo &quot;tor:x:246:&quot; &gt;&gt; /torgateway/etc/group

# Don't know if etc-update works in Whonix-Gateway? you need at least modify the script and remove any reference to &quot;portageq&quot;
cp /usr/sbin/etc-update /torgateway/usr/sbin/etc-update
cp /etc/etc-update.conf /torgateway/etc/etc-update.conf

cp /usr/src/linux/arch/x86/boot/bzImage /torgateway/boot/kernel
# I didn't use modules so that part is missing, refer to http://www.gentoo.org/doc/en/handbook/handbook-x86.xml?full=1#kernel_modules

mount -t proc none /torgateway/proc/

# enter target chroot
chroot /torgateway
source /etc/profile
export PS1=&quot;(target-chroot) $PS1&quot;

# set root password for Whonix-Gateway
passwd

chown tor:tor /var/lib/run/tor
chown tor:tor /var/log/tor

echo &quot;192.168.0.1&quot; &gt; /etc/resolv.conf

echo &quot;en_US ISO-8859-1&quot; &gt;&gt; /etc/locale.gen
locale-gen
cp /usr/share/zoneinfo/UTC /etc/localtime

# untested
mv /etc/conf.d/net /etc/conf.d/net.old
echo '# see /usr/share/doc/openrc*/net.example*
config_eth0=&quot;dhcp&quot;
config_eth1=&quot;192.168.0.1  netmask 255.255.255.0 brd 192.168.0.255&quot;
#routes_eth1=&quot;default via 192.168.0.1&quot;' &gt; /etc/conf.d/net

cd /etc/init.d
ln -s net.lo net.eth0
rc-update add net.eth0 default
ln -s net.lo net.eth1
rc-update add net.eth1 default
cd

rc-update add udev sysinit
rc-update add udev-postmount default
rc-update add gpm default
rc-update add tor default

# TODO:
# copy iptables and torrc from ubuntu-tg
/etc/init.d/iptables save
rc-update add iptables boot

ed -s /etc/locale.nopurge  &lt;&lt;&lt; $',s/NEEDSCONFIGFIRST/#NEEDSCONFIGFIRST/g</pre>
w' localepurge

== Install Whonix-Gateway to a hard disk or sd card: ==

Using Grub:

<pre>fdisk /dev/sdb
mkfs.ext4 /dev/sdb1
mkdir /mnt/target
mount /dev/sdb1 /mnt/target

# edit according to partition and disc layout! sda/sdb/hd are just examples!
# The /dev/sd* name will probably be different on your build system and on your target     system.
# in this example the host got two hard disks, you install to the second one, &quot;sdb&quot;
# this drive is attached to the gateway system and if it's the only drive it becomes &quot;sda&quot;
# same goes for grub: hd1 == sdb, hd0 == sda

echo &quot;
title TorGateway
root (hd0,0)
kernel /boot/kernel root=/dev/sda1&quot; &gt;&gt; /boot/grub/grub.conf

grep -v rootfs /proc/mounts &gt; /etc/mtab

echo &quot;/dev/sda1               /               ext4            noatime         0 1&quot; &gt; /etc/fstab

## outside the chroot (open a new terminal on the host)
cd gentoodev
rsync -a dev/ torgateway/dev/
rm -r torgateway/var/db/* torgateway/tmp/*
rsync -a torgateway/ /mnt/target/

## then, inside the target-chroot

grub
# then manually configure:
# grub&gt; root (hd1,0)
# grub&gt; setup (hd1)

# alternatively, may not work properly
#grub-install --no-floppy /dev/sdb --recheck

exit #target-chroot
exit #build-chroot</pre>
= Footer =

[[include ref=WikiFooter]]

