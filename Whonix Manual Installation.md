[[include ref=WikiHeader]]

[TOC]

# Manually Installing Whonix #
This is just a draft, unfinished, just some ideas. For special setups and advanced users only. Only in case the [Download] version, [OtherOperatingSystems], [PhysicalIsolation] or [BuildDocumentation] instructions are not suitable, for example if you like to use another distribution as base for Whonix-Gateway. [Build Anonymity] has not been considered.

This assumes Whonix 0.6.0 or above. It would work with 0.5.6 as well (see wiki history), but in 0.6.0 it's easier because the build scripts layout has been improved.

[Dev_SourceCodeIntro] contains a source code introduction.

Look into Whonix source code. It's mostly an installing and copy and paste task.

Look into the source file ./build-steps/45_create-vbox-vm. See function general_setup to see which commands are used to create both Virtual Machines, apply hardware_modifications on both machines, and also apply gateway_specific or workstation_specific accordingly.

After installing the operating system...

* Packages listed in /home/user/Whonix/Whonix-Gateway_packages have to be installed on Whonix-Gateway.
* Packages listed in /home/user/Whonix/Whonix-Workstation_packages have to be installed on Whonix-Workstation.

All files within whonix_gateway folder are configuration files supposed to be installed on Whonix-Gateway. For example /home/user/Whonix/whonix_gateway/etc/tor/torrc is supposed to be installed on Whonix-Gateway under /etc/tor/torrc.

All files within whonix_workstation folder are configuration files supposed to be installed on Whonix-Workstation. For example /home/user/Whonix/whonix_workstation/usr/local/bin/xchat-reset is supposed to be copied to /usr/local/bin/xchat-reset on Whonix-Workstation.

whonix_shared are configuration files supposed to be installed on Whonix-Gateway and Whonix-Workstation. For example /home/user/Whonix/whonix_shared/etc/sudoers.d/whonix is supposed to be copied to /etc/sudoers.d/whonix on Whonix-Gateway and Whonix-Workstation.

You don't have to bother with most other files in Whonix source folder. ^1^ Just read README and LICENSE.

Chroot Scripts...

All commands scripts in the folder https://github.com/adrelanos/Whonix/blob/development/whonix_gateway/usr/local/share/whonix/chroot-scripts/ have to be run on Whonix-Gateway.

All commands scripts in the folder https://github.com/adrelanos/Whonix/blob/development/whonix_workstation/usr/local/share/whonix/chroot-scripts/ have to be run on Whonix-Workstation.

All commands scripts in the folder https://github.com/adrelanos/Whonix/blob/development/whonix_shared/usr/local/share/whonix/chroot-scripts/ have to be run on Whonix-Workstation and Whonix-Gateway.

You can also read the scripts and only run the commands you find sensible manually one by one.

<font size="-3">
,,
^1^ Those are used for image creation and Virtual Machine creation.
</font>

# Footer #
[[include ref=WikiFooter]]