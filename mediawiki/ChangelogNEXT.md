[[include ref=WikiHeader]]

[TOC]

= adretemp68 =

Whonix-Gateway and Whonix-Workstation

* much work on an auto updater and packaging Whonix for Debian
* added KDE Lowfat Settings
* improved many script output messages
* whonixcheck: code simplification; more robust progress_bar in corner cases.
* htpdate: 180 seconds for curl timeout as per https://mailman.boum.org/pipermail/tails-dev/2013-February/002635.html
* An anonymous user suggested, that MAC addresses used by Whonix starting with vendor prefix 080027 are too uncommon.; Used https://github.com/EtiennePerot/macchiato/tree/master/oui/wireless_laptop.sh (Integrated wireless interfaces in laptop computers) to find more popular MAC vendor ids.; Changed MAC addresses ('''still needs testing if it really worked'''):
** Whonix-Gateway eth0 '00:26:82:47:5c:e1' (Gemtek Technology Co., Ltd. - HP Laptop)
** Whonix-Gateway eth1 '00:13:02:9c:f1:91' (Intel Corporate - Fujitsu Amilo Pi 1556 Notebook, Intel Corporation PRO/Wireless 3945ABG Network Adapter)
** Whonix-Workstation eth0 '00:21:00:4d:8f:08' (GemTek Technology Co., Ltd. - HP Pavilion TX2510EA)
* Added Time Sanity Check init script.
* /etc/apt/preferences.d/50_banned-packages
* Let htpdate wait for bootclockrandomization.
* whonixcheck and timesync: Warn if bootclockrandomization and/or timesanitycheck failed.
* Time Sanity Check before and after htpdate
* configuration folder /etc/whonix.d for .d-style configuration files
* added khelpcenter4 package
* added faketime package
* added timeprivacy script
* new man pages:
** uwt
** timesync
** time_privacy
** scurl
* /etc/kde4/kdm/kdmrc: Working around a rare bug, where kdm did not start because of a timeout by using higher timeout. http://forums.debian.net/viewtopic.php?f=6&amp;t=45648
* new generic uwt/timeprivacy wrapper
* deleted old uwt wrappers
* using new generic uwt master wrapper /usr/bin/uwtwrapper instead of many copies of the same script
* fixed the bug where the uwt wrappers gave wrong arguments to curl and therefore broke applications dependent on curl, such as apt-file, update-flashplugin
* added libgl1-mesa-dri to prevent error (EE) AIGLX error: dlopen of /usr/lib/i386-linux-gnu/dri/swrast_dri.so failed (/usr/lib/i386-linux-gnu/dri/swrast_dri.so: cannot open shared object file: No such file or directory) in /var/log/Xorg.0.log
* Removed xdg-utils, since we do not need them to create desktop icons and start menu entries.
* Check total RAM. If more than 512 MB -&gt; start KDE. If less (like 128 MB) -&gt; do not start KDE. This should be be quite convenient, because users with low RAM could reduce (Whonix-Gateway) RAM to 128 MB and even if they sometimes wanted to configure/check something, they could assign 512 RAM and automagically boot into the graphical KDE desktop. There are also many settings in /etc/whonix.d/ to configure this feature, so if you want you can also add much RAM and still don't boot a desktop environment, use different display managers and so on.
* whonixcheck: now reading /etc/whonix.d/ configuration folder
* whonixcheck: added option WHONIXCHECK_NO_EXIT_ON_TRANS_PORT_DETECTION_FAILURE
* whonixcheck, timesync: bugfix: will now kill the process, if the cancel button in zenity is pressed
* added apparmor-profiles (but didn't enable enforce mode or added any useful profiles)
* added apparmor-utils (but didn't enable enforce mode or added any useful profiles)
* added /etc/default/grub
* higher console resolution 1024x768 (without X)
* enable &quot;apparmor=1 security=apparmor&quot; by default (but didn't enable enforce mode or added any useful profiles)
* more verbose output while booting, since on slow machines it may look like there is no progress otherwise
* reduced timeout from 300 to 180 to be on par with Tails
* added /usr/bin/whonix_repository which can be used to easily disable Whonix's APT repository

Whonix-Gateway

* first time connection wizard
* graphical Whonix-Gateway (got a KDE desktop now), wallpaper with most important information
* /etc/whonix_firewall.d/ for .d-style configuration files
* added option for Flash Proxy to firewall config in /etc/whonix_firewall.d/
* /etc/apt/sources.list.d/torproject.list: Activated torproject.org Debian Wheezy repository, so obfs3 can be downloaded.
* added support for obfs3 out of the box
* new man pages:
** leaktest
** armwrapper
** whonix
** whonixsetup
* /usr/local/bin/whonix_firewall: comment for using Custom Open Ports on external interface
* added SocksPorts separate for KDE and GNOME wide applications
* /usr/bin/whonix_firewall: Port 9150 is no longer a custom port. It is now SOCKS_PORT_TBB_DEFAULT, supposed to be used by stock TBB running unmodified inside Whonix-Workstation.
* /etc/tor/torrc: added 127.0.0.1:9150 for consistency
* increased Whonix-Gateway RAM from 128 MB to 768 MB, because Whonix-Gateway becomes graphical
* arm wrapper to start arm without a password now passing command line arguments to arm
* arm wrapper also announces its existence when run because &quot;set -x&quot; is now set to avoid confusion
* Removed custom socks port 9151, because this is TBB's default Tor Control Port. Therefore we shouldn't train users to use it as custom socks port to avoid confusion.

Whonix-Workstation

* Added Boot Clock Randomization. This is useful before timesync succeeded, naturally timesync runs before timesync succeded, to make sure that the host clock and Whonix-Workstation clock differ.; Open for arguments if that should be added to Whonix-Gateway as well. See TimeSync design.
* added kmix
* added graphical alternatives manager, galternatives
* torbrowser: Deactivate tor-launcher, a Vidalia replacement as browser extension, to prevent running Tor over Tor. https://trac.torproject.org/projects/tor/ticket/6009 https://gitweb.torproject.org/tor-launcher.git TOR_SKIP_LAUNCH=1
* XChat: No longer moving XChat plugins into a new folder. Using dpkg-divert instead to deactivate them. User documentation explains how to re-enable them.
* new man pages:
** xchat-reset
** torbrowser
** leaktest
** whonix
** whonix_firewall
* added proxy settings for KDE wide application
* torbrowser new --lang &quot;language&quot; command line option, see man torbrowser
* torbrowser: new option for advanced users --nokilltb

Source Code

* whonix_gateway/usr/local/bin/leaktest: using true instead of echo, since we set -x anyway
* whonix_gateway/usr/local/bin/leaktest: added comment in/out for &quot;FascistFirewall 1&quot;.
* improved error handling
* code refactoring
* help-steps/pre: fewer useless debug output
* Gateway and Workstation: /etc/X0.hosts Add xhost exception, as required for zenity, since cron starts as root and whonixcheck (zenity) starts as user.
* better documented package lists
* shared: added debsums to package selection. Added a sanity check using debsums to the chroot-script 30_internal-checks.
* chroot-scripts-pre.d
* chroot-scripts-post.d
* postinst.d
* added skip_scripts variable
* No longer setting KDEDIRS in whonix_workstation/etc/environment. Using whonix_shared/etc/X11/Xsession.d/50whonix instead.
* WHONIX_TARGET_ARCH can now be set in build configuration
* Whonix-Gateway and Whonix-Workstation: Deleted /etc/sudoers.d/whonix and created multiple small files instead.
* new file release/list_source_files
* new build-step 32_verify_copied_files: checks if everything from the whonix_gateway/whonix_workstation and whonix_shared actually was correctly copied using diff.
* Added Tor Project Archive (0x886DDD89) key, which signs the deb.torproject.org repositories and archives as chroot script. It later gets updated by torproject keyring package.
* no longer required to mess with /etc/rc.local and /etc/environment so the user can easly edit without any conflicts with Whonix configuration files (moved to /etc/profile.d/ instead)
* Whonix-Gateway, new chroot script, whonix_shared/usr/local/share/whonix/chroot-scripts-post.d/70_tor: downloading tor related software from Torprojects repository in case it contains newer software. At time of writing obfsproxy in Torprojects repository already contained obfs3 while Debian repository had only obfs2.
* whonix_shared/etc/apt/sources.list: changed from wheezy to stable, because wheezy became stable.
* gateway and workstation, package selection: Removed virtuoso-minimal, which was installed as workaround in 0787deb78d24678d87ef704ed206dd0b6b4d7e3e as dependency for nepomuk (nepomuk comes with kde-workspace). Since nepomuk now gets disabled, virtuoso is no longer required.
* deleted defunct chroot-script whonix_shared/usr/local/share/whonix/chroot-scripts/40_variables, it never worked, variables set by it were ignored by following chroot-scripts. Those variables get set in /home/user/Whonix/help-steps/variables.
* Disable uwt while building Whonix, because it is not functional while building Whonix from source code. Instead of doing this in every build and chroot script, do it in a central place, the help-steps/variables script.
* mass rename whonix_(gateway|workstation|shared)/usr/local/... to whonix_(gateway|workstation|shared)/usr/... ; mass rename /usr/local/... to /usr/...
* Removed line for changing partition uuid from build-steps/35_run-chroot-scripts-img, because it didn't really belong there and made it its own step build-steps/34_change_partition_uuid.
* We no longer place uwt wrappers into /usr/local/bin/<uwt-wrapped-application>. Therefore we now use dpkg-divert /usr/bin/<uwt-wrapped-application> to /usr/bin/<uwt-wrapped-application> and symlink /usr/bin/<uwt-wrapped-application> to /usr/bin/uwtwrapper.
* whonix_shared/usr/bin/scurl: better way to forward extra arguments, using <math>{1+"</math>@&quot;} instead of $*
* whonix_shared/usr/share/whonix/chroot-scripts-pre.d/70_banned_packages: Removed code 'echo &quot;package-name hold&quot; | dpkg --set-selections', because its no longer necessary, we're now using /etc/apt/preferences.d/ instead.
* build-steps/10_prepare-build-machine: added ruby-ronn to build dependencies (required for creating man pages)
* whonixcheck, timesync: better handling of short and long options; -help -&gt; --help -autostart -&gt; --autostart -cron -&gt; --cron
* whonixcheck: now using whonix-keys.d folder
* whonixcheck, timesync: output and startup functions are now the same on Whonix-Gateway and Whonix-Workstation, since Whonix-Gateway is now graphical as well
* DummyTor now gets created along with the other packages in debian/control
* added two new help-steps prevent-daemons-from-starting and unprevent-daemons-from-starting, because the (un)chroot are ignored for bare-metal and preventing daemons from starting is still recommend for bare-metal.
* whonix_shared/usr/share/whonix/apt.conf: changed ip from 192.168.0.11 to 127.0.0.1 to make it independent from host network configuration
* got ride of whonix_shared/usr/share/whonix/apt.conf, using apt-get command line rather
* build-steps: using http_proxy variable for setting up apt-cacher-ng as proxy for grml-debootstrap
* build-steps/2600_export-vbox-vm: added --manifest (hashes which can be used to determine if the appliance components arrived intact)
* build-steps/2600_export-vbox-vm: also added --manifest, --product, --vendor, --vendorurl, --version (Not yet using: --producturl)
* Using config-package-dev to solve conflicts when Whonix deb packages overwrite files owned by other packages.
* build-steps/2000_install-common-packages: prevent mounting /etc/resolv.conf from the host inside the chroot, /etc/resolv.conf from whonix source folder can get installed.;
* deleted whonix_workstation/etc/polipo/config (not installed, not in use)
* build-steps/1100_prepare-build-machine: - no longer installing dependencies for creating virtual machines for bare metal builds - no longer installing dependencies for bare metal builds for virtual machine builds - removed debootstrap as build dependency, because grml-debootstrap Depends on it and therefore automatically fetches it - removed git as build dependency, git is only required to download the source code but anyone who has the source code, doesn't need git (if not planing to contribute) - replaced qemu with qemu-utils, because that includes the required tools - code refactoring -
* build-steps/1300_create-debian-img: removed unneeded --keep_src_list option from grml-debootstrap#
* build-steps/2500_create-vbox-vm: removed hardware modifications, very little gain, while it breaks enabling uefi
* run update-grub while building Whonix and fix /boot/grub/grub.cfg due to a known bug in grub
* new WHONIX_DEB_DEBUG variable
* install from local APT repository, no longer required to copy packages manually into the image
* update-rc.d $display_manager remove as dpkg post invoke hook, otherwise as soon as a display manager (kdm by default) get upgraded, its postinst script will revert Whonix's post chroot script and Whonix's feature, which deactivated the /etc/init.d/ autostart mechanism, what would break Whonix's feature to decide to start a display manager depending on free RAM and other configurable settings
* build-steps/1100_prepare-build-machine: speed up apt-get update
* help-steps/variables: removed deprecated SNAPSHOT_DESCRIPTION variable
* adding Whonix APT repository signing key with apt-key while building Whonix

= adretemp40 =

Whonix-Workstation

* longer installing polipo by default. It's not required for anything.
* torbrowser: Added a meaningful error message, if the Tor Browser folder does not exist and recommend to run the updater in that case.

Whonix-Gateway and Whonix-Workstation

* Added /etc/hostname with content &quot;host&quot;. Even though grml-debootstrap already creates /etc/hostname with content &quot;host build-steps/35_run-chroot-scripts-img: added support for bare metal users.

Source Code

* torbrowser: merged tb_start function into tb_start_new_tab.

= 0.6.1 =

Whonix-Gateway and Whonix-Workstation

* timesync: added autostart status notification
* Added /etc/apt.conf.d/20oldconfig: never ask if a configuration file should get updated by dpkg. Always keep the locally installed one.
* Running whonixcheck after a random amount of time (minimum 60 seconds + a random number between 0 and 500) to make the network fingerprint less predictable.

Whonix-Gateway

* torrc, firewall: added port 9050

Whonix-Workstation

* workstation: Disable Apper's mechanism to automatically check for updates, to work around upstream bugs: - https://bugs.freedesktop.org/show_bug.cgi?id=62575 and https://bugs.freedesktop.org/show_bug.cgi?id=62576
* timesync: When timesync is run by cron.hourly (/usr/local/bin/htpdate_hourly), and there is nothing important to tell, say nothing. Otherwise there would be such a popup every hour.
* timesync: When timesync is automatically started and nothing important has to be reported, use kdialog --passivepopup, because that is non-intrusive and will automatically fade out. When timesync is manually started, always use zenity.
* timesync: No need for flashing a progress meter, if htpdate already succeeded.
* whonix_workstation/home/user/.bashrc: Do not &quot;cat /etc/motd&quot; on Whonix-Workstation login shell, only in virtual console. (Konsole)
* Workstation: Graphical notify-send notification that start of whonixcheck gets delayed.
* Workstation package selection: added libnotify-bin for whonixcheck.
* whonixcheck: Removed transitional popup, that whonixcheck is no longer autostarted at every boot of Whonix-Workstation.
* torbrowser: Downloading Tor Browser and signature from http://idnxcnkne4qt76tg.onion/dist/torbrowser/linux instead from https://www.torproject.org/dist/torbrowser for better security when run inside Whonix.
* torbrowser: Added --max-time 300 to signature download to defeat a endless data or slow retrieval attack.
* torbrowser: downloading signature file before Tor Browser itself. - Would be a pity to download Tor Browser (takes long) only to recognize, that the signature download (takes very little time) fails.
* whonix_workstation/usr/local/share/whonix/kde/share/applications/whonix-whonixcheck.desktop: improved icon description.
* torbrowser: Removed tb_create_user_js, since no longer required to change Tor Browser's proxy settings. (Now using rinetd.)
* torbrowser: Always starting Tor Browser with cd ~/tor-browser_&quot;<math>TB_LANG"/ ~/tor-browser_"</math>TB_LANG&quot;/App/Firefox/firefox --profile Data/profile instead of cd ~/tor-browser_&quot;<math>TB_LANG"/ ~/tor-browser_"</math>TB_LANG&quot;/start-tor-browser and therefore not starting Vidalia/Tor when the user manually downloaded or updated TBB.
* Workstation: Added rinetd. It prevents Tor over Tor by just installing Tor or by using the complete Tor Browser Bundle, which starts Vidalia and Tor.; This is because, it listens on port 9050 and 9150 and therefore lets a default Tor or TBB fail to start.; Fowards port 127.0.0.1:9050 (Workstation) to 192.168.0.10:9050 (Gateway). Fowards port 127.0.0.1:9150 (Workstation) to 192.168.0.10:9150 (Gateway).

Source Code

* whonix_shared/usr/local/share/whonix/chroot-scripts/50_adduser-user: Not re-creating user &quot;user&quot;, and therefore perhaps changing an existing password. That should support re-running the script and bare metal better.
* gateway firewall: renamed variable, GATEWAY_ALLOW_INCOMMING_SSH -&gt; GATEWAY_ALLOW_INCOMING_SSH; typo fixes
* renamed: whonix_shared/etc/profile.d/whonixcheck.sh -&gt; whonix_shared/etc/profile.d/20_whonixcheck.sh
* whonix_shared/usr/local/bin/delay: added small help file. It's required to prevent getting the logins sparred.
* whonix_shared/usr/local/bin/whonixcheck-scripts/15_kill-old-instances fixed
* whonixcheck: load help_output module earlier so it also works for the check_autostart module whonix_shared/usr/local/bin/whonixcheck-scripts/25_autostart: disable debugging
* build-steps/30_copy-into-img: Remove symlink /etc/localtime before copying to prevent &quot;cp: <code>/usr/share/zoneinfo/UTC' and</code>/etc/localtime' are the same file&quot; error.
* whonixcheck: better way to autostart
* timesync: added option for -autostart
* chown --recursive user:user -&gt; chown --recursive &quot;<math>USERNAME":"</math>USERNAME&quot;
* build-steps/15_prepare-build-machine: using &quot;$USERNAME&quot; instead of user
* chown --recursive user:user -&gt; chown --recursive &quot;<math>USERNAME":"</math>USERNAME&quot;
* more consistency: /home/&quot;<math>USERNAME" -> "</math>HOMEVAR&quot;
* build-steps/15_prepare-build-machine: added creation of user &quot;user&quot;.
* build-steps/20_create-debian-img: arch as variable $ARCH; comments for alternative architectures for custom builds
* help-steps/variables: added &quot;export DEBIAN_FRONTEND=noninteractive &quot;
* Added new build step 15_prepare-build-machine to ease building from source.
* whonixcheck: removed redundant variable COUNTER
* torbrowser: using general trap; reduced code duplication by sourcing the tbbversion function
* whonixcheck: split the script, which had grown too big over time into many smaller scripts
* timesync: using whonixcheck error handler, reduced code duplication
* timesync: split timesync script into many smaller scripts and reduced code duplication comments
* help-steps/variables: Variable WHONIX_SOURCE_FOLDER supports now being used by different user than &quot;user&quot;.
* whonix_build: Removed &quot;chmod +x &quot;$WHONIX_SOURCE_FOLDER&quot;/build-steps/20_create-debian-img&quot; - no longer required, no longer using the executable bit to decide which steps to run. This is now done using command line switches and variables.
* Fix: build script when not using as user &quot;user&quot; - deactivate trap before running the id command.
* release/whonix_release: Added --armor to gpg --detach-sign. .asc files look better (look like plain text) than .sig (look like binary).
* release/whonix_news: No longer required to update the version manually.; It's now read from whonix_shared/usr/local/share/whonix/version.;
* release/upload_whonix_news: added automatic signing and verification to upload script.; deleted release/whonix_news.asc, since no longer required.
* upload_download_readme: Added automatic sign, verify to upload script.; release/README.asc deleted, since no longer required. release/whonix_release: comments
* release/upload_download_readme: Read version from /whonix_shared/usr/local/share/whonix/version. No longer required to manually edit version.
* whonixcheck: more modular, own function for get_local_whonix_version.
* whonixcheck: No longer hardcoding architecture variable ARCH. Now using uname.
* torbrowser: made the script more modular
* Not trying to creating any users (and thus changing their passwords), if these user accounts already exist. This should support (physical isolation) users better, who changed these passwords already. gateway torrc: using bridge for obfs bridge comment instead of Bridge - both work (tested), but since regular bridges are also already written in lowercase, it's more consistant. (bridges.torproject.org also uses &quot;bridges&quot; in lowercase.)

= 0.6.0 =

Whonix-Gateway and Whonix-Workstation

* Run update-command-not-found while building to prevent prompting the user &quot;Please run update-command-not-found.&quot;.
* Prevent form installing: popularity-contest (privacy); geoclue (privacy); resolvconf (can mess up /etc/resolv.conf); ufw (can mess up firewall); and also for custom builds: canonical-census, unity-lens-shopping, unity-scope-video-remote, unity-scope-musicstores, geoclue-ubuntu-geoip; using dpkg hold; users who wish can overwrite those default banned packages which shouldn't be necessary for anyone but experts

Whonix-Gateway

* torrc: Added comment for mumble server hidden service.

Whonix-Workstation

* Disable xchat plugins no longer with xchat-reset, only disable while building so the user is free to re-enable them.
* Removed redundant hiddenserver-install. No longer required. Whonix documentation explains how to install it a hidden server.

Source Code

* Now easier to understand. More modular. New step based layout.
* Got ride of unclear whonix_internal_install_script. Chroot-Scripts are now in whonix_.../usr/local/share/whonix/chroot-scripts/.
* whonix_build -all -tg -tw -fast -tg-fast -fw-fast -clean -clean-tg -clean-tw
* Running whonix_build_clean &quot;<math>MACHINE" before whonix_build_clean "</math>MACHINE&quot;, i.e. when running whonix_build -all/tg(-fast)/tw(-fast) won't break anymore if running whonix_build -clean(-tg/-tw) has been forgotten beforehand.
* Moved workstation specific icons to workstation folder.; Moved icons to /usr/local/share/whonix/icons/.; Moved gpg public keys to /usr/local/share/whonix/gpg-pubkeys/.
* chmod -x whonix_workstation/home/user/.bashrc
* Removed whonix_workstation/usr/local/share/whonix/chroot-scripts/70_audio, redundant on Debian/KDE, audio will work out of the box.
* torbrowser: No longer adding additional extensions.torbutton.banned_ports, it was always redundant.
* added /etc/apt/apt.conf.d/99timeout to handle apt-get timeouts better
* workstation: added failsafe mechanism to Whonix second, optional, extra firewall
* workstation: Creating the dummytor package while building Whonix.
* Gateway: No longer required to set +i on /etc/resolv.conf. Removed. DHCP is configured to prevent overwriting it and resolvconf is a banned package.
* gateway: added /etc/dhcp/dhclient-enter-hooks.d/nodnsupdate to prevent showing an error message while booting

= Footer =

[[include ref=WikiFooter]]

