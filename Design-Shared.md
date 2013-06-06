[[include ref=WikiHeader]]

[TOC]

# Last updated git #
4a70f4868d683a08b73c6236b36684220d704d97

# Get Build Dependencies
Install a tool to create Virtual Machine images (such as grml-debootstrap) and tools for mouting and apply other useful build configurations.

Whonix-Example-Implementation:

* Configure apt-get and dpkg, to ask no questions while installing the build dependencies.
* Update the build machine's operating system.
* Configure apt-cacher-ng to speed up downloading when building multiple times (for debugging).
* Install tools used in the build process.
    * https://github.com/adrelanos/Whonix/blob/master/build-steps/15_prepare-build-machine

# Get Base Operating System
Use a tool to create a Virtual Machine base installation, which contains a secure operating system and which is bootable.

Whonix-Example-Implementation:

* Used Debian for reasons explained on the [OperatingSystem] design page.
* Whonix uses grml-debootstrap to build .img Virtual Machine images. The .img images are still virtualizer agnostic, can be run in a variety of virtualizers such as Qemu or Qubes OS. They can (and will in Whonix-Example-Implementation case) be converted to other formats to support other virtualizers (such as the .img format, which Virtual Box uses in case of Whonix).
    * https://github.com/adrelanos/Whonix/blob/master/build-steps/20_create-debian-img
    * https://github.com/adrelanos/Whonix/blob/master/Whonix-Gateway_packages
    * https://github.com/adrelanos/Whonix/blob/master/Whonix-Workstation_packages
    * https://github.com/adrelanos/Whonix/blob/master/grml_config

Other Implementations:

* Old Whonix versions up to 0.3.0 used Ubuntu as base operating system.
* Old Whonix versions up to 0.3.0 used [Preseed](https://en.wikipedia.org/wiki/Preseed), installed the operating system from DVD inside a Virtual Machine.
* This step can also be done manually, i.e. the user could be told to manually install some operating system.
* Whonix with [PhysicalIsolation].

# Backup Base Operating System
Make a backup of that image. This is not strictly required, but you will want to modify that image often and want to start fresh often.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/build-steps/25_backup-img

# Mount Image
Mount the image, so files can be copied into it.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/help-steps/mount-img

# Copy Files Into Image
Copy configuration files and chroot scripts into the Virtual Machine image to transform it into a Gateway or Workstation. 

Whonix-Example-Implementation:

* Copying script: https://github.com/adrelanos/Whonix/blob/master/build-steps/30_copy-into-img
* Verification script: https://github.com/adrelanos/Whonix/blob/master/build-steps/32_verify_copied_files
* All files from whonix_gateway will get copied into Whonix-Gateway.
* All files from whonix_workstation will get copied into Whonix-Workstation.
* All files from whonix_shared will get copied into Whonix-Gateway and Whonix-Workstation.

# Chrooting
As preparation for the next step, there must be a method to chroot the mounted image.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/help-steps/chroot-img

# Running Scripts inside Chroot
The base operating system has to be modified. Some scripts need to be executed inside the virtual machines. This is called running chroot scripts.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/build-steps/35_run-chroot-scripts-img

# Unchrooting
The process of chrooting must be undone after the chroot scripts were executed.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/help-steps/unchroot-img

# Unmounting 
The image must be unmounted after the copying files into it or after chrooting, running chroot scripts and unchrooting.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/help-steps/unmount-img

# Creating a Virtual Machine package
It's useful to deploy the Virtual Machine images through a package format, which makes it easy to import them for users.

Whonix-Example-Implementation:

* Uses Virtual Box.
* Virtual Box does not support .img images, only .vdi (and others).
    * Therefore the .img image has to be converted to .vdi.
        * https://github.com/adrelanos/Whonix/blob/master/build-steps/40_convert-img-to-vdi
    * The next step is to create a virtual machine description file.
        * After creating it, the Virtual Machine could be started.
        * https://github.com/adrelanos/Whonix/blob/master/build-steps/45_create-vbox-vm
    * An easy way to deploy Virtual Machine images is through the [Open Virtualization Format](https://en.wikipedia.org/wiki/Open_Virtualization_Format) format (.ova images)
        * https://github.com/adrelanos/Whonix/blob/master/build-steps/50_export-vbox-vm

# Files #
## Essential
### Username, FQDN, hostname
Hosts file. Use non-identifying values for FQDN and hostname, because some applications may leak it. (Mixmaster is known to leak it.) Set FQDN to "host.localdomain" and set hostname to "host". [It's best when they are shared among anonymity focused distributions.](https://mailman.boum.org/pipermail/tails-dev/2013-January/002457.html)

It's recommend to work as non-privileged user and not using one will get into usability trouble (desktop environments don't like running as root). For usability, consistency, defence in depth, name it "user". It's better to say non-saying operating system user account names and ideally share them among anonymity focused distributions since the user could accidentally leak it (ex: ssh).

Whonix-Example-Implementation:

* Set FQDN to "host.localdomain" and set hostname to "host": https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/hosts

* adding user account "user": https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/chroot-scripts/30_adduser_user
* configuring hostname "host": https://github.com/adrelanos/Whonix/blob/master/build-steps/20_create-debian-img
* Even though grml-debootstrap already creates /etc/hostname with content "host", it's useful for physical isolation users, who set up the wrong host while installing: https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/hostname
* More information about the shared user name "user": [Whonix's Protocol-Leak-Protection and Fingerprinting-Protection]

### Operating System Updates
Configure the package manager.

Configure software repositories.

Do not use the default automatic updates mechanism and use higher timeouts. It's better to disable the operating system's default automatic update mechanism, because times of automatic run are too predictable. The network fingerprint (not web fingerprint) could help an ISP guessing, that there is a network hidden operating system.

Notify about operating system updates in a safe way.

Misc settings, higher timeouts, more retries when package download or DNS resolution fails. This is useful because anonymity networks are slow and otherwise updating would occasionally fail due to network problems.

Must have a secure operating system updater (package manager), i.e. must not fall through the [TUF Threat Model](https://www.updateframework.com/wiki/Docs/Security#AttacksandWeaknesses) ([w](http://www.webcitation.org/6F7Io2ncN)). Additionally, downloading should go thought an anonymity network, with changing exit nodes. This makes an adversary less likely to interfere with the update process, because updates go through different ISPs, which makes it much more difficult to mount a man-in-the-middle attack over an extended amount of time.

The package manager shouldn't confuse the user with questions to keep the locally installed configuration file or to install the new version from the upstream package maintainer.

Whonix-Example-Implementation:

* Gateway and Workstation updates go through Tor. (Due to Firewall, Network Configuration and Stream Isolation Wrapper, details in Design-Shared/Gateway/Workstation.)
* Whonix uses Debian ftp.us.debian.org and security.debian.org repositories. 
    * https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/apt/sources.list
* Disable the operating system's default automatic update mechanism.
    * https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/apt/apt.conf.d/20noperiodic
    * https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/kde/share/config/apper
* Stop dpkg from asking questions whether new version of the Debian upstream package manager should be used. Always keep the old versions of configuration files to ensure, changes made by Whonix for privacy/anonymity won't get lost.
    * https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/apt/apt.conf.d/20oldconfig 
* Higher timeouts, more retries.
    * https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/apt/apt.conf.d/99timeout
* For the safe update notification, see check mechanism (whonixcheck) below.
* Disable Apper (packagekit) automatic download of package lists (due to upstream bugs https://bugs.freedesktop.org/show_bug.cgi?id=62575 and https://bugs.freedesktop.org/show_bug.cgi?id=62576)
    * https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/usr/local/share/whonix/kde/share/config/apper

### TimeSync
Add a secure method with distributed trust to obtain date and time, because a clock which is drift, is bad for anonymity.

Whonix-Example-Implementation:

General Information

* [TimeSync]
* [Dev_timesync]
* tails_htp configuration file: https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/default/htpdate
* When timesync is run by cron, it adds a random delay to prevent having a predictable network (not web) fingerprint. Essentially runs tails_htp every hour at a random time.

Start Hooks

* tails_htp init script: https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/init.d/htpdate
* Using cron to start it every hour: https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/cron.hourly/30_timesync
* The file https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/bin/timesync_hourly gets run by https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/cron.hourly/30_timesync cron every hour.
* Auto start Boot Clock Randomization: https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/etc/init.d/bootclockrandomization

* Auto start timesync status notification after (auto) login Whonix-Gateway: https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/profile.d/30_timesync.sh

* Workstation specific
    * Auto start timesync status notification after (auto) login Whonix-Workstation: https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/home/user/.config/autostart/timesync.desktop

Install Hooks

* Adding tails_htp daemon user account and init script: https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/chroot-scripts/70_htp
* Install Boot Clock Randomization init script: https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/chroot-scripts/70_bootclockrandomization
* Install Time Sanity Check init script: https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/chroot-scripts/70_timesanitycheck

Supporting Files

* /etc/sudoers.d/
    * Allow Network Time Synchronization (tails htpdate) without password: https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/sudoers.d/htpdate
    * Allow "sudo service bootclockrandomization status" without a password: https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/sudoers.d/bootclockrandomization
    * Allow "sudo service timesanitycheck status" and "restart" without a password: https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/sudoers.d/timesanitycheck
* Delay console output a bit when run after login. This ensures /etc/motd is shown earlier and introduces the status notifications gracefully. Better look and feel: https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/bin/delay
* Icon. https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/icons/timesync.ico

Script

* htpdate (tails_htp) itself: https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/sbin/htpdate
* Combined graphical and text user interface "timesync" main script. https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/bin/timesync
* Combined graphical and text user interface "timesync" scripts folder. https://github.com/adrelanos/Whonix/tree/master/whonix_shared/usr/local/bin/timesync-scripts and some from https://github.com/adrelanos/Whonix/tree/master/whonix_shared/usr/local/bin/whonixcheck-scripts (which are sourced becomes clear by reading the main https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/bin/timesync script)

### Banned Packages
Some packages aren't suited for an anonymous operating system. Reasons are privacy issues or messing with network settings. Ensure, that those get removed, if they got installed by the virtual machine image creation tool. This shouldn't be the case because of the hand selected package selection. Just in case upstream dependencies change or custom packages get added by users who build from source code. Ensure that those packages won't get installed by accident. Since it's documented, advanced users can overwrite these recommendations if they know better.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/chroot-scripts/70_banned_packages
* https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/apt/preferences.d/50_banned-packages

### Stream Isolation Wrapper
Stream isolate different applications to prevent identity correlation through circuit sharing. To my knowledge, only the anonymizer Tor supports this feature.

Whonix-Example-Implementation:

* See [Stream Isolation].
* [uwt](https://trac.torproject.org/projects/tor/wiki/doc/torsocks) is a wrapper arround torsocks: https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/bin/uwt
* uwt / timeprivacy master wrapper: https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/bin/uwtwrapper
* uwt configuration folder (.d-style): https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/whonix.d/
* Application wrapper symlinks to the master wrapper (If the application isn't installed, the wrapper doesn't do anything. So having one more installed than necessary, doesn't matter.): https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/chroot-scripts/70_uwt

## Extra #
### Time Privacy ###
Applications such as gpg and git embed time stamps in their output. For improved privacy it may make sense to fake this data. The user should enable it oneself, otherwise it could be very surprising and may not do what the user wants. Experimental design and implementation. Disabled by default.

Whonix-Example-Implementation:

* Disabled by default.
* timeprivacy script: https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/bin/timeprivacy
* uwt / timeprivacy master wrapper: https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/bin/uwtwrapper
* Time Privacy configuration folder (.d-style): https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/whonix.d/
* Application wrapper symlinks to the master wrapper (If the application isn't installed, the wrapper doesn't do anything. So having one more installed than necessary, doesn't matter.): https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/chroot-scripts/70_uwt

### hdd configuration / swap / Disk uuid / dbus machine-id
Since the virtual machine creation tool won't create a swap partition (which is actually good because it simplifies the setup) but the system could run out of memory, add a swap file. The is optional depending on the operating system and available RAM. Configure swap to be used as little as possible to improve speed.

Whonix-Example-Implementation:

* Swap file creation. https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/chroot-scripts/70_create_swap_file
* Activating swap in fstab. https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/fstab
* Only swap to disk if really necessary. https://github.com/adrelanos/Whonix/blob/master/whonix_gateway/etc/sysctl.d/whonix.conf
* Less Important Identifies (Defined as per [Whonix's Protocol-Leak-Protection and Fingerprinting-Protection].)
    * Share Disk UUIDs.
        * In /etc/fstab. https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/fstab
        * Also share uuid for swap file. https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/chroot-scripts/70_create-swap-file
    * Chang partition uuid. "*tune2fs /dev/mapper/loop0p1 -U 26ada0c0-1165-4098-884d-aafd2220c2c6*" https://github.com/adrelanos/Whonix/blob/master/build-steps/35_run-chroot-scripts-img
    * Change disk uuid: https://github.com/adrelanos/Whonix/blob/master/build-steps/45_create-vbox-vm
    * Share dbus machine-id: https://github.com/adrelanos/Whonix/blob/master/whonix_shared/var/lib/dbus/machine-id

### Base Files
Perhaps only required for Debian and derivatives. Whonix was asked to replace the default dpkg origin symlink.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/dpkg/origins/whonix
* https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/chroot-scripts/70_symlinks

## Usability
### check mechanism
Recommend, not strictly required. 

Whonix-Example-Implementation:

General Information

* [whonixcheck]
* Whonixcheck essentially runs whonixcheck at least once very day.
* Whonixcheck, although run on each boot and every hour by cron, itself is rate limited and stops running checks, if it was run less than one day ago. The user can always manually perform all whonixcheck checks.

Start Hooks

* The file https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/bin/whonixcheck_hourly gets run by cron.hourly https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/cron.hourly/40_whonixcheck
* Allowing messages to tty (setting "mesg y") while an application was started in background (by cron): https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/profile.d/20_mesg.sh
* Whonix-Gateway specific
    * https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/profile.d/40_whonixcheck.sh gets run on every (automatic) login.
* Whonix-Workstation specific
    * Since Whonix-Workstation is graphical, it's better to use the event by the desktop environment than using profile.d for autostart. https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/home/user/.config/autostart/whonixcheck.desktop

Supporting Files

* Allows running apt-get update as user (non-root): https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/sudoers.d/apt-get-update
* Allow wall (with -nobanner option) without password: https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/sudoers.d/wall
* Version file to let the whonixcheck find out which version of Whonix is locally installed. https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/version
* apt-get-update (which has an sudoers exception) runs apt-get update. https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/bin/apt-get-update
* When automatically run by autostart or cron, whonixcheck adds a random delay (to prevent having a predictable network (not web) fingerprint.
* gpg key of Whonix maintainer adrelanos to verify Whonix News. https://github.com/adrelanos/Whonix/tree/master/whonix_shared/usr/local/share/whonix/gpg-pubkeys
* Icon. https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/icons/whonix.ico
* xhost exception. https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/X0.hosts

Script

* The whonixcheck main script. https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/bin/whonixcheck
* The folder with the various checks. https://github.com/adrelanos/Whonix/tree/master/whonix_shared/usr/local/bin/whonixcheck-scripts

### Desktop Environment
Optional.

It's useful to have a desktop preconfigured to make it as easy as possible for users who use Linux for the first time.

Whonix-Example-Implementation:

* shared
    * Based on KDE.
    * [Dev_KDE]
    * Desktop usability improvements
        * kdm auto login: https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/kde4/kdm/kdmrc
        * https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/chroot-scripts/70_kde
        * https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/kde/share/config/dolphinrc
        * Hiding unwanted knetattach shortcut: https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/chroot-scripts/70_knetattach
        * https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/kde/share/config/konsolerc
    * Performance (kde-lowfat)
        * https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/kde/share/config/kdedrc
        * https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/kde/share/config/kdeglobals
        * https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/kde/share/config/krunnerrc
        * https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/kde/share/config/ksmserverrc
        * https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/kde/share/config/kwinrc
        * https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/kde/share/config/nepomukserverrc
    * Security
        * No sounds: https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/kde/share/config/knotifyrc
    * Supporting Files
        * Icons Files: https://github.com/adrelanos/Whonix/tree/master/whonix_shared/usr/local/share/whonix/icons
        * Desktop Icons: https://github.com/adrelanos/Whonix/tree/master/whonix_shared/usr/local/share/whonix/kde/share/applications
        * Setting KDEDIRS variable: https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/X11/Xsession.d/50whonix

* gateway specific
    * Changing default skin and wallpaper: https://github.com/adrelanos/Whonix/blob/master/whonix_gateway/usr/local/share/whonix/kde/share/apps/plasma-desktop/init/00-defaultLayout.js
    * Start menu favorites: https://github.com/adrelanos/Whonix/blob/master/whonix_gateway/usr/local/share/whonix/kde/share/config/kickoffrc
    * Desktop Icons: TODO
    * Creating desktop icons: https://github.com/adrelanos/Whonix/blob/master/whonix_gateway/usr/local/share/whonix/chroot-scripts/70_desktopicons

* workstation specific
    * Changing default skin and wallpaper: https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/usr/local/share/whonix/kde/share/apps/plasma-desktop/init/00-defaultLayout.js
    * Start menu favorites: https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/usr/local/share/whonix/kde/share/config/kickoffrc
    * Desktop Icons: https://github.com/adrelanos/Whonix/tree/master/whonix_workstation/usr/local/share/whonix/kde/share/applications
    * Creating desktop icons: https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/usr/local/share/whonix/chroot-scripts/70_desktopicons

### sudoers
Optional. For convenience. Only recommend for Virtual Machines.

Allow shutdown, reboot and poweroff without a password.
Allow starting Tor Controller arm without password. (No effect on Workstation, since arm is only Gateway.)
Allow mixmaster-update without password. (No effect on Gateway, since mixmaster is only installed on Gateway.)

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/sudoers.d/reboot
* https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/sudoers.d/arm
* https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/sudoers.d/mixmaster-update

### Console Autologin
Optional. Only recommend for virtual machines.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/inittab

### Console Default Password Hint
Optional.

The system will be shipped with a default password (which users are suggested to change in documentation). To prevent user frustration when not knowing the password it greatly reduced (from Whonix experience) support requests if the default password is displayed right above the password prompt.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/issue

### Console Welcome Message
Optional.

Contains general information about derivative, licensing, default passwords, how to open the help file.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/motd

### Deactivate display power saving in Virtual Machines
Since it's confusing and not useful and not saving any energy. (Needs to be applied on host.)

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/profile.d/20_disable_powersaving.sh

### boot manager configuration
Optional. For higher boot resolution, it's required to run update-grub after changing grub configuration files.

Whonix-Example-Implementation:

* Not yet functional.
* https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/grub.d/50_whonix
* https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/chroot-scripts/70_grub

### update command not found
Optional.

Initially update the command not found database, to prevent showing "please run update-command-not-found" in case a non-existent command gets entered in console.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/chroot-scripts/70_update_command_not_found

### Secure/SSL Command Line Downloader
Add a command line downloader, which enforces using https (SSL).

Whonix-Example-Implementation:

* A simple curl wrapper. https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/bin/scurl
* Documented under [scurl - SSL command line downloader](https://sourceforge.net/p/whonix/wiki/Software/#scurl-ssl-command-line-downloader)
* The user starts scurl, the wrapper will run the curl uwt wrapper (/usr/local/bin/curl), which stream isolates and finally calls curl.

### Slim Down
Optional. To safe space and to prevent (some) development related leaks, remove cache, temporary files, dhcp leases, package manager cache, logs, history.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/chroot-scripts/80_slimdown

### Icons
Optional.

Some pretty icons for the start menu and the desktop for custom applications, which are only useful in a Gateway/Workstation design.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/tree/master/whonix_shared/usr/local/share/whonix/icons

## Debugging
### Sanity Checks
Recommend, not strictly required.

Some simple tests to check for example, if all files have been correctly copied into the image, if the package manager is fully functional, because some virtual machine creation tools build broken images. Package integrity checks.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/build-steps/32_verify_copied_files
* https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/chroot-scripts/10_root_check
* https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/chroot-scripts/20_sanity_checks

### Misc
Optional.

Whonix-Example-Implementation:

* Chroot Script Skeleton, not strictly required, might just be useful to explain how to create chroot-scripts: https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/chroot-scripts/70_skeleton
* Create a list of all files inside Whonix source folder. https://github.com/adrelanos/Whonix/blob/master/release/list_source_files
* List of all files inside Whonix source code with comments: https://github.com/adrelanos/Whonix/blob/master/development/files_list
* Commented list of files inside Whonix source code that may require special treatment when creating a Whonix-Gateway/Workstation.deb (which is planed): https://github.com/adrelanos/Whonix/blob/master/development/files_list_short

### Variables
Recommend, not strictly required.

It's useful to configure the system, not to ask any questions which require user interaction such as when you plan to run the package manager from within chroot. This is because interaction isn't useful when automating things.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/help-steps/variables

### Package Cache
Optional.

If the package manager is used inside chroot, it makes sense to run it though a cache, so debugging steps can be done faster.

Whonix-Example-Implementation:

* apt.conf which can be used in case apt-get gets used inside chroot. https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/apt.conf

What is */usr/local/share/whonix/apt.conf* good for?

This apt.conf is only used inside chroot and currently only in effect for "*./debug-steps/download-source -tg*" and "*./debug-steps/download-source -tw*".

It points to *http://192.168.0.11:3142*, which is expected to be a Whonix-Workstation with apt-cacher-ng running. It's useful for running "*apt-get install*" and "*apt-get source*" inside chroot, because downloads are cached, which speeds up the build process when building several times in a row. (Debugging with only minor changes.)

In case you don't want to use it or to use another proxy, edit */home/user/Whonix/whonix_shared/usr/local/share/whonix/apt.conf* (comment out with a # or change proxy settings). Don't forget "*sudo ./build-steps/30_copy-into-img -tX*" after modifying the file.

* Script to run apt-cacher-ng through uwt for Stream Isolation. https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/bin/apt-cacher-ng_uwt

### Prevent daemons from starting inside chroot
Optional.

Only in case you want to install something inside chroot for debugging purposes. Otherwise they can lock the chroot folder and you won't be able to unchroot.

Whonix-Example-Implementation:

* policy-rc.d blocks daemons from starting. https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/policy-rc.d
* policy-rc.d gets copied into chroot when chrooting. https://github.com/adrelanos/Whonix/blob/master/help-steps/chroot-img
* policy-rc.d gets deleted inside chroot when leaving chroot. https://github.com/adrelanos/Whonix/blob/master/help-steps/unchroot-img

### Indicate last chroot script
Not strictly required. A chroot script, which indicates that all went well.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/chroot-scripts/90_end

### Lower priority while building
Optional. Not strictly required.

Using ionice and renice.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/help-steps/pre

### Enable debugging
Optional. Not strictly required.

When using bash, set -x to show each any any command that gets executed.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/help-steps/pre

### Error handling
Optional. Not strictly required.

It's important to ensure that there are no error while copying files into the images or while running the chroot scripts because many steps are essential. Stop and loudly complain if any unexpected error occurs.

Whonix-Example-Implementation:

* general trap: https://github.com/adrelanos/Whonix/blob/master/help-steps/pre
* using traps and exit 1 everywhere

### Delete Virtual Machine files
Optional. Not strictly required.

So they can be re-created for debugging purposes.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/debug-steps/delete-vbox-vm

### Interactive Chroot
Optional. Not strictly required.

After creating the base operating system image, after copying files into it or after applying the chroot scripts, it's useful to have a command, which allows to look around inside the image without having to boot the image. Adrelanos calls this Interactive Chroot.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/debug-steps/interactive-chroot-img

## Licensing
Only required for builds, which will be redistributed in public.

Make a list of GPLed software.

Whonix-Example-Implementation:

* Added [damngpl](http://dberkholz.com/2004/02/). https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/damngpl
* Creating a list of GPLed software. https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/chroot-scripts/70_sources
* A script to download all GPLed software, which can be run inside the virtual machine or inside chroot. https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/share/whonix/whonix_download_sources
* The source code needs a License file. https://github.com/adrelanos/Whonix/blob/master/LICENSE

# Build Automation
Optional. Not strictly required.

Since many steps are required to build a Gateway or Workstation, it's useful to automate build creation.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/whonix_build
* [BuildDocumentation]

# Release Automation
Optional. Not strictly required.

Since many steps are required to redistribute a Gateway or Workstation, it's useful to automate releases.

Whonix-Example-Implementation:

* Release maintenance folder: https://github.com/adrelanos/Whonix/blob/master/release/README
* sourceforge.net Download Readme: https://github.com/adrelanos/Whonix/blob/master/release/README
* Whonix News File: https://github.com/adrelanos/Whonix/blob/master/release/whonix_news
* Script to automate gpg signing, verification (as sanity check) and upload sourceforge.net Download Readme: https://github.com/adrelanos/Whonix/blob/master/release/upload_download_readme
* Script to automate gpg signing, verification (as sanity check) and upload Whonix News File: https://github.com/adrelanos/Whonix/blob/master/release/upload_whonix_news
* Building and uploading of Virtual Machine Images. Fully documented on https://sourceforge.net/p/whonix/wiki/Dev_Redistribution/ and https://github.com/adrelanos/Whonix/blob/master/release/whonix_release.

# Other important things
The things on this (Design-Shared) page are supposed to be added to the Gateway and the Workstation.

To build a Gateway, also things from the [Design-Gateway] page have to be added.

To build a Workstation, also things from the [Design-Workstation] page have to be added.

Justify other design decisions, what the project doesn't and what it doesn't do.
Have loads of documentation. Have a source code hacking guide and source code introduction.

Whonix-Example-Implementation:

* https://sourceforge.net/p/whonix/wiki/Design-Gateway
* https://sourceforge.net/p/whonix/wiki/Design-Workstation
* https://sourceforge.net/p/whonix/wiki/Design/
* https://sourceforge.net/p/whonix/wiki/Documentation/
* https://sourceforge.net/p/whonix/wiki/Dev_SourceCode/
* https://sourceforge.net/p/whonix/wiki/Dev_SourceCodeIntro/

# Footer #
[[include ref=WikiFooter]]