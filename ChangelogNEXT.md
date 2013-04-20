[[include ref=WikiHeader]]

[TOC]

# adretemp40
Whonix-Workstation:

* longer installing polipo by default. It's not required for anything.
* torbrowser: Added a meaningful error message, if the Tor Browser folder does not exist and recommend to run the updater in that case.

Whonix-Gateway and Whonix-Workstation

* Added /etc/hostname with content "host". Even though grml-debootstrap already creates /etc/hostname with content "host build-steps/35_run-chroot-scripts-img: added support for bare metal users.

Source Code

* torbrowser: merged tb_start function into tb_start_new_tab.

# 0.6.1
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
* whonix_workstation/home/user/.bashrc: Do not "cat /etc/motd" on Whonix-Workstation login shell, only in virtual console. (Konsole)
* Workstation: Graphical notify-send notification that start of whonixcheck gets delayed.
* Workstation package selection: added libnotify-bin for whonixcheck.
* whonixcheck: Removed transitional popup, that whonixcheck is no longer autostarted at every boot of Whonix-Workstation.
* torbrowser: Downloading Tor Browser and signature from http://idnxcnkne4qt76tg.onion/dist/torbrowser/linux instead from https://www.torproject.org/dist/torbrowser for better security when run inside Whonix.
* torbrowser: Added --max-time 300 to signature download to defeat a endless data or slow retrieval attack.
* torbrowser: downloading signature file before Tor Browser itself. - Would be a pity to download Tor Browser (takes long) only to recognize, that the signature download (takes very little time) fails.
* whonix_workstation/usr/local/share/whonix/kde/share/applications/whonix-whonixcheck.desktop: improved icon description.
* torbrowser: Removed tb_create_user_js, since no longer required to change Tor Browser's proxy settings. (Now using rinetd.)
* torbrowser: Always starting Tor Browser with cd ~/tor-browser_"$TB_LANG"/ ~/tor-browser_"$TB_LANG"/App/Firefox/firefox --profile Data/profile instead of cd ~/tor-browser_"$TB_LANG"/ ~/tor-browser_"$TB_LANG"/start-tor-browser and therefore not starting Vidalia/Tor when the user manually downloaded or updated TBB.
* Workstation: Added rinetd. It prevents Tor over Tor by just installing Tor or by using the complete Tor Browser Bundle, which starts Vidalia and Tor.; This is because, it listens on port 9050 and 9150 and therefore lets a default Tor or TBB fail to start.; Fowards port 127.0.0.1:9050 (Workstation) to 192.168.0.10:9050 (Gateway). Fowards port 127.0.0.1:9150 (Workstation) to 192.168.0.10:9150 (Gateway).

Source Code

* whonix_shared/usr/local/share/whonix/chroot-scripts/50_adduser-user: Not re-creating user "user", and therefore perhaps changing an existing password. That should support re-running the script and bare metal better.
* gateway firewall: renamed variable, GATEWAY_ALLOW_INCOMMING_SSH -> GATEWAY_ALLOW_INCOMING_SSH; typo fixes
* renamed:    whonix_shared/etc/profile.d/whonixcheck.sh -> whonix_shared/etc/profile.d/20_whonixcheck.sh
* whonix_shared/usr/local/bin/delay: added small help file. It's required to prevent getting the logins sparred.
* whonix_shared/usr/local/bin/whonixcheck-scripts/15_kill-old-instances fixed
* whonixcheck: load help_output module earlier so it also works for the check_autostart module
whonix_shared/usr/local/bin/whonixcheck-scripts/25_autostart: disable debugging
* build-steps/30_copy-into-img: Remove symlink /etc/localtime before copying to prevent "cp: `/usr/share/zoneinfo/UTC' and `/etc/localtime' are the same file" error.
* whonixcheck: better way to autostart
* timesync: added option for -autostart
* chown --recursive user:user -> chown --recursive "$USERNAME":"$USERNAME"
* build-steps/15_prepare-build-machine: using "$USERNAME" instead of user
* chown --recursive user:user -> chown --recursive "$USERNAME":"$USERNAME"
* more consistency: /home/"$USERNAME" -> "$HOMEVAR"
* build-steps/15_prepare-build-machine: added creation of user "user".
* build-steps/20_create-debian-img: arch as variable $ARCH; comments for alternative architectures for custom builds
* help-steps/variables: added "export DEBIAN_FRONTEND=noninteractive "
* Added new build step 15_prepare-build-machine to ease building from source.
* whonixcheck: removed redundant variable COUNTER
* torbrowser: using general trap; reduced code duplication by sourcing the tbbversion function
* whonixcheck: split the script, which had grown too big over time into many smaller scripts
* timesync: using whonixcheck error handler, reduced code duplication
* timesync: split timesync script into many smaller scripts and reduced code duplication
comments
* help-steps/variables: Variable WHONIX_SOURCE_FOLDER supports now being used by different user than "user".
* whonix_build: Removed "chmod +x "$WHONIX_SOURCE_FOLDER"/build-steps/20_create-debian-img" - no longer required, no longer using the executable bit to decide which steps to run. This is now done using command line switches and variables.
* Fix: build script when not using as user "user" - deactivate trap before running the id command.
* release/whonix_release: Added --armor to gpg --detach-sign. .asc files look better (look like plain text) than .sig (look like binary).
* release/whonix_news: No longer required to update the version manually.; It's now read from whonix_shared/usr/local/share/whonix/version.;
* release/upload_whonix_news: added automatic signing and verification to upload script.; deleted release/whonix_news.asc, since no longer required.
* upload_download_readme: Added automatic sign, verify to upload script.; release/README.asc deleted, since no longer required. release/whonix_release: comments
* release/upload_download_readme: Read version from /whonix_shared/usr/local/share/whonix/version. No longer required to manually edit version.
* whonixcheck: more modular, own function for get_local_whonix_version.
* whonixcheck: No longer hardcoding architecture variable ARCH. Now using uname.
* torbrowser: made the script more modular
* Not trying to creating any users (and thus changing their passwords), if these user accounts already exist. This should support (physical isolation) users better, who changed these passwords already.
gateway torrc: using bridge for obfs bridge comment instead of Bridge - both work (tested), but since regular bridges are also already written in lowercase, it's more consistant. (bridges.torproject.org also uses "bridges" in lowercase.)

# 0.6.0

Whonix-Gateway and Whonix-Workstation

* Run update-command-not-found while building to prevent prompting the user "Please run update-command-not-found.".
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
* Running whonix_build_clean "$MACHINE" before whonix_build_clean "$MACHINE", i.e. when running whonix_build -all/tg(-fast)/tw(-fast) won't break anymore if running whonix_build -clean(-tg/-tw) has been forgotten beforehand.
* Moved workstation specific icons to workstation folder.; Moved icons to /usr/local/share/whonix/icons/.; Moved gpg public keys to /usr/local/share/whonix/gpg-pubkeys/.
* chmod -x whonix_workstation/home/user/.bashrc
* Removed whonix_workstation/usr/local/share/whonix/chroot-scripts/70_audio, redundant on Debian/KDE, audio will work out of the box.
* torbrowser: No longer adding additional extensions.torbutton.banned_ports, it was always redundant.
* added /etc/apt/apt.conf.d/99timeout to handle apt-get timeouts better
* workstation: added failsafe mechanism to Whonix second, optional, extra firewall
* workstation: Creating the dummytor package while building Whonix.
* Gateway: No longer required to set +i on /etc/resolv.conf. Removed. DHCP is configured to prevent overwriting it and resolvconf is a banned package.
* gateway: added /etc/dhcp/dhclient-enter-hooks.d/nodnsupdate to prevent showing an error message while booting

# Footer #
[[include ref=WikiFooter]]