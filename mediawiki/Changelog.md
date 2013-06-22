[[include ref=WikiHeader]]

= Next =

If you are curious what will come in next Whonix version, see [ChangelogNEXT].

= Whonix 0.5.6 Changelog =

Whonix-Gateway

* Fixed a time zone bug, which prevented Tor to connect in some cases.

= Whonix 0.5.5 Changelog =

Whonix-Gateway and Whonix-Workstation

* Fixed htpdate_hourly.
* whonixcheck: improved messages.
* whonixcheck: better method for Tor Browser local and remote version phrasing.
* uwt: Fixed a bug: &quot;''libtorsocks(18790): Could not open socks configuration file (/tmp/tmp.pKSaitLYTN) errno (13), assuming sensible defaults for Tor.''&quot;
* Deactivate automatic update check in /etc/apt/apt.conf.d/10periodic. It is handled by whonixcheck. This makes fingerprinting Whonix users harder.
* whonix_createvm: Disable clipboard sharing at build time. Only matters if guest additions are installed which is recommend against. Just in case.
* whonix_release: Removed sha sums. New versions will no longer contain sha sums. A more secure method, gpg signatures are provided.
* Enabled auto login on tty1 for Whonix-Gateway and Whonix-Workstation.
* Added haveged, which is an entropy gathering daemon.
* adrelanos.asc: changed e-mail address from proper at secure-mail dot biz to adrelanos at riseup dot net. Key otherwise unchanged. Fingerprint remains the same. There is no need to update. Just mail to the my current riseup e-mail address.
* Installing command-not-found.<br />
* Removed redundant mdadm and lvm2 from package selection. Physical Isolation and other advanced users most likely know if they need those packages.

Whonix-Workstation

* easier to install [https://sourceforge.net/p/whonix/wiki/Chat/#torchat TorChat]
* pre-installed [Mixmaster], a tool to send e-mail without registering e-mail accounts
* easier to install TorBirdy
* pre-installed rawdog, an rss reader to read Whonix News Blogs
* autologin for kde user
* added [DummyTor] package
* whonixcheck: runs once a day.
* Leaktest script fixed.
* Added icons for whonix online readme, torbrowser, whonixcheck and timesync.
* installing kde-baseapps-bin package. It's required for KDE applications proxy settings. (Only for stream isolation, manually installed applications.)
* MAT, the [Metadata] Anonymisation Toolkit, now fully installed and therefore easier to use
* added GnuPG frontend: KGpg
* install accessibility tools
* install process manager: ksysguard
* Whonix-Workstation KDE settings:
** double click instead of single click
** kgpg settings hide user id and keyservers
** KGpg settings: Decided not to set hkp://2eghzlv2wwcq7u7y.onion as keyserver, because it was offline.
** Dolphin show menu bar
** Konsole unlimited scrollbag
** plasma-widget-folderview, which allows to show the content of the ~/Desktop folder on the desktop.
** kde desktop set to folderview by default to show desktop icons.
** set default wallpaper to /usr/share/wallpapers/stripes.png
** New icons and desktop shortcuts.
** Whonix specifc start menu default icons.
* new /home/user/.bashrc - adds displaying /etc/motd (contains password and help) and bash completion.
* removed leafpad and kate. added kwrite as editor.
* whonixcheck: show &quot;apt-get update &amp;&amp; apt-get dist-upgrade&quot; again even if apper is available because apper has bugs. (unsigned package warning)
* torbrowser:
** wrapper script supports now -new-tab link.com, for example: torbrowser -new-tab https://www.startpage.com
** the script may no longer be run as root.
** can now be run as any user, not just as &quot;user&quot;, but this is untested. Only tested for user &quot;user&quot;.
** new -lang switch for language help.
** better error message if network is down and curl fails.
** more help if network is down or script is broken.
** added Tor Browser Updater icon
** added graphical progress meter.
** graphical user interface
** removed gpg key download code and move it to deprecated_code. Downloading the keys at Tor Browser update time from the keyservers was a relict from TorBOX times, where a build script created TorBOX. It was due to trust and space reasons to include only the gpg fingerprint and the gpg keyserver commands to download the key. Anyone using Whonix binary builds or source code without audit already trusts Whonix. Deploying the gpg public keys for Tor Browser download instead of downloading them from them keyservers adds no additional trust problem. Auditors can instead of comparing the gpg fingerprint, download they keys and compare them with the ones shipped with Whonix. Not relying on the keyservers will make the Tor Browser update script much more robust.
** better and less scaring error message if torbrowser script bug is ever caught.
** Creating tor-browser_&quot;$TB_LANG&quot;/Docs/version. Tor Browser changelog has been forgotten to update by upstream. https://sourceforge.net/p/whonix/discussion/general/thread/6122990d/ To play it safe and having a chance of finding out the installed version, we create a file ourselves to remember it.
** Fixed profile not found bug, in case Tor Browser wasn't fully loaded by hard coding to wait 30 seconds before trying to open extra tabs
* whonixcheck, torbrowser, htpdate: Notice Endless data attacks and Slow retrieval attacks by adding --max-time 300 to curl.

Whonix-Gateway

* package selection: installing tor-geooipdb. arm needs it to show countries.
* 0.4.5 undocumented: added settings to whonix_firewall, these were and are documented on the applications page
* whonixcheck
** now runs automatically at least every 24 hour on Whonix-Gateway as well.
** On Whonix-Gateway. Will now display the results when automatically run to all logged in users using the wall command.
** Also download whonix version and news file on the gateway for users using custom workstations.
* Fixed whonix_gateway/usr/local/bin/leaktest.
* Usability: arm can now be run without password.
* whonixcheck:

Source Code

* You can now just drop files inside the whonix_gateway, whoniy_workstation or whonix_shared folders and don't need to add every single file inside int_copy_*.
* Faster debugging.
** new switch: whonix_createvm -t&quot;$MACHINE&quot;-copyimg required for building form source code...
** This eases debugging. Before we created the img using grml-debootstrap and directly copied into it and directly run the chroot script inside it. Creating a clean modification required to re-create the whole img using grml-debootstrap which always took a long time, even though using apt-cacher-ng. From now, only a copy of the img is modified. Using whonix_createvm -tg-copyimg (or -tw-copyimg) will copy the original img created by grml-debootstrap from /home/user/whonix_binary/&quot;<math>VMNAME".img  to /home/"</math>USERNAME&quot;/whonix_binary/&quot;<math>VMNAME"_copy.img. Only/home/"</math>USERNAME&quot;/whonix_binary/&quot;$VMNAME&quot;_copy.img gets modified from now.;
** whonix_build: added -fast switch, which skips the -createimg step
* whonix_createvm:
** only set Workstation hardware clock to UTC.
** No longer setting Gateway hardware clock to UTC.
*** This is because Tor leaks it to entry guards (and bridges?).
*** torproject.org #7277: timestamp leaked in TLS client hello https://trac.torproject.org/projects/tor/ticket/7277
*** torproject.org #4852: Clients send NETINFO with time https://trac.torproject.org/projects/tor/ticket/4852
** Whonix-Gateway is therefore less fingerprintable.
* removed comment, pae is now documented in the faq
* added release folder, whonix_release file are still just notes, not a automatic script.
* new switches for mounting and unmounting images are tX-(un)mountimg and tX-(un)mountvdi
* start-tor-browser: comment fix. Added export in front of the TOR_TRANSPROXY, TOR_SOCKS_HOST, TOR_SOCKS_PORT variables. Fixes https://github.com/adrelanos/tbb-scripts/issues/1 Thanks to scruloose for reporting!
* torbrowser: found zenity workaround, therefore removed kdialog.
* whonixcheck: found zenity workaround, therefore removed kdialog.
* whonixcheck: removed old wget/uwt comments.
* htpdate: changed curl to /usr/bin/curl to circumvent uwt wrapper.
* /usr/local/bin/htpdate_hourly more comments for debugging.
* apt-get-update: small fix. Now returning return code of apt-get update.
* whonixcheck: better error handling if apt-get-update fails.
* added backup of documentation
* License file: Added sources of icons and their licenses. Reformatting.
* torbrowser: Removed old comments.
* torbrowser: i686 to &quot;$ARCH&quot;
* torbrowser: en-US to &quot;$LANG&quot;
* torbrowser: Check if TB_LANG exists and is not empty. If it's empty, set to default en-US. Otherwise leave it untouched.
* torbrowser: Improved comments.
* torbrowser: Easier readable version phrasing.
* torbrowser: #for commented out commands; ## for comments
* torbrowser: code refactoring. Removed redundancy of downloading the update information twice. Improved comments and echos.
* torbrowser: No longer deleting Tor/Vidalia from the downloaded TBB package. No longer trying to safe space. The wasted space is minimal, while this could have unforeseen consequences.
* torbrowser: gpg fingerprints are now inside variables. Fingerprints and how to verify them is now noted in echos.
* torbrowser: use more variables for download links. Now just one comment has to be removed to download from .onion instead.
* torbrowser: removed old out commented code for deleting stuff.
* torbrowser: simpler startup script creation method and fixed a quote bug.
* torbrowser: using rm --force to suppress error messages.
* torbrowser: deleting TorBrowser_installation_FAILED in case it was created earlier.
* torbrowser: ed editor startup script modification method comment removed.
* torbrowser: many changes. Added a graphical user interface
* torbrowser: comments; echos.
* torbrowser: new startup script creation method and fixes a quote bug.
* torbrowser: using rm --force to suppress error messages.
* torbrowser: deleting TorBrowser_installation_FAILED in case it was created earlier.
* whonixcheck: better method for Tor Browser local and remote version phrasing, same as in the the torbrowser script.
* whonixcheck: moved news file location from sf project web to sf file release system due to traffic limits for sf project web.
* moved /home/user/.local/share/applications to /etc/skel/.local/share/applications
* torbrowser: no progress bar, if -force-install is used.
* torbrowser: updated extensions.torbutton.banned_ports
* torbrowser: Workaround for the &quot;The proxy server is refusing connections&quot; bug introduced in latest Tor Browser. https://trac.torproject.org/projects/tor/ticket/8336
* torbrowser: Removed redundant misc settings from user.js... user_pref(&quot;extensions.torbutton.prompt_torbrowser&quot;, false); user_pref(&quot;general.autoScroll&quot;, true);
* added /etc/dpkg/origins/whonix to honor Debian policy
* package selection: added debian-keyring (40 MB) as comment. Currently not required. Just to keep it in mind and for discussion.
* many code simplifications and code refactoring
* added /etc/environment for Tor Browser
* Whonix-Workstation_packages: marked non essential packages, which are safe to remove and which could make a complete operating system with ## LITE; shuffle; revised comments.
* Workstation package selection: added and unfortunately commented out software-center due to too many bugs which make it unusable http://bugs.debian.org/cgi-bin/pkgreport.cgi?pkg=software-center
* Whonix-Gateway_packages, Whonix-Workstation_packages: added sysvinit-utils and bsdutils. Dependencies for whonixcheck.
* LICENSE
** Moved picture licenses to Whonix-documentation repository.;
** &quot;Except in this file or in files where otherwise noted, content in this the Whonix source package is licensed under Whonix source code license.&quot;
** improved formatting
** added links to webcitation.org
* removed doc backup, created extra repository https://github.com/adrelanos/Whonix-documentation
* Renamed start-torbrowser to start-tor-browser. The Whonix specific name start-torbrowser was too confusing.
* /etc/inittab: using getty instead of login. getty does not break whonix | more.
* gateway/workstation packages: explicitly installing util-linux because it contains getty.
* Copying temporary apt.conf into Whonix-G/W instead of only into Whonix-G.
* Using apt-cacher-ng for downloading source code.
* added damngpl
* Append &quot;127.0.0.1 host.localdomain host&quot; to /etc/hosts as per [https://mailman.boum.org/pipermail/tails-dev/2013-January/002457.html Let's share username, /etc/hostname and /etc/host among all anonymity distributions]
* new debug build option: -tX-interactive
* deleted adrelanos.asc from the untested_adre branch. It continues to life in the master branch.
* Whonix-Workstation_packages: removed dhcp3-client since not required
* moved whonix_workstation/etc/apt/apt.conf to whonix_workstation/etc/apt/apt.conf.d/99whonix
* whonix_shared/etc/apt/sources.list: added security non-free
* whonixcheck: If it was run by cron and there is nothing to tell, say nothing.; comments; echos; output
* int_copy_workstation: chattr -i on resolv.conf removed because it was redundant
* renamed whonix_shared/etc/apt/apt.conf.d/10periodic to whonix_shared/etc/apt/apt.conf.d/20noperiodic
* 20noperiodic takes precedence over 10periodic
** no longer required to backup /etc/apt/apt.conf.d/10periodic
** no longer required to replace /etc/apt/apt.conf.d/10periodic
* whonixcheck; timesync: overwrite all instances of let with || true because let throws an error when the result is 0
* whonix_createvm: added -tw-bare-metal-pre and -tw-bare-metal-post
* gateway: new, out commented by default, /etc/apt/sources.list.d/torproject.list
* package selection: explicitly installing bash-completion, less, more

= Whonix 0.4.5-fix2 =

[0.4.5-fix] for testers.

This is just a hotfix for torbrowser and whonixcheck. The Tor Browser locally installed version check was broken, because The Tor Project forgot to update the changelog and because the keyserver was offline. The torbrowser and the whonixcheck scripts now use a more robust method. ([https://sourceforge.net/p/whonix/discussion/general/thread/6122990d/ Bug report and discussion])

* fixes torbrowser udpate script
* fixes whonixcheck
* fixes timesync command

= Whonix 0.4.5-fix1 =

Testers release with same goals as Whonix 0.4.5-fix2, but didn't work.

= Whonix 0.4.5 Changelog =

* Whonix-Gateway and Whonix-Workstation
** added gnupg-curl package
** shared partition uuid
** new apt-cacher-ng_uwt helper script
** whonixcheck: stream isolation fix when not using Tor, which should really only happen if the user manually added a VPN or transproxy.
** whonixcheck: improved possible reasons help message if Tor is not detected (VPN, transproxy, false positive).
** whonixcheck: now uses mktemp
** whonixcheck: Suggestions for &quot;Your Internet connection appears to be down.&quot;.
** whonixcheck: using curl instead of wget for download
** whonixcheck: enforcing tlsv1
** whonixcheck: uwt no longer required in whonixcheck
** package selection: added curl and bc for whonixcheck
** timesync and whonixcheck: check_htpdate now checks if htpdate pid file exists.
** timesync can now also be run when zenity is installed but X window system not started
** timesync now fails faster if done file exists but no success file
** Hacked the htpdate init script to work with Wheezy and fixed disabling of virtual box additions time sync (if installed).
** timesync: Waiting longer for htpdate result.
** fixed help messages in whonixcheck and timesync
** motd fix
* Whonix-Gateway
** pre-installing obfsproxy
** Renamed user unsafe to clearnet.
** torrc: Shuffle settings in torrc. Moved more important things, which might be subject to change are to the top.
** torrc: Added table of contents as comment.
** Expanded nslookup help in gateway help file whonix.
* Whonix-Workstation
** Experimental set workstation image size to 50 GB, only space which really is in use should be filled up.
** running whonixcheck daily at random time on workstation
** Keyserver choice comment in gpg.conf.
** Installing image viewer gwenview.
** Installing virtuoso-minimal as dependency for nepomuk (nepomuk came with kde-workspace). Perhaps not best solution.
** Deleting /usr/share/applications/kde4/knetattach.desktop.
* Source Code
** Mounting .img images instead of .vdi images. This makes it easier to add support other virtualizers.
** ./whonix_createvm -createvm renamed to ./whonix_createvm -createvboxvm
** switch -convertfromraw renamed to -converttovdi
** switch -tX-delete renamed to -tX-vboxdelete
** switch -tX-delete renamed to -tX-vboxdelete
** /usr/share/whonix moved to /usr/local/share/whonix
** moved whonix_internal_install_script(s) to (tg/ws)/usr/share/whonix/
** whonix news format moved to https://sourceforge.net/p/whonix/wiki/Dev_news/

= Whonix 0.4.4 Changelog =

* Whonix-Gateway and Whonix-Workstation
** Switched to Debian Wheezy.
** Added Secure Distributed Network Time Synchronization. Thanks to the Tails developers for their fine, free and Open Source tails_htp!
** Added timesync gui.
** Deactivated Virtual Box time synchronization.
** Deactivating Virtual Box guest additions time synchronization if they are installed.
** Creating a snapshots by default
** Rebranding, the project is now called Whonix.
** Spoofing virtual hardware information.
** Added BitCoin address for donations.
** Added adrelanos's gpg key. key for integrated Whonix Version and News notification (whonixcheck).
** Improved GPG verification mechanism.
** torcheck renamed to whonixcheck
** Greatly improved whonixcheck, now checks Whonix version, SocksPort, TransPort, stream isolation, Tor Browser version, operating system version and network time synchronization.
** Improved uwt, uwt -t server_type -i ip -p port ....
** Deactivated whonix_config_uuids_fstab. Regression.
** Deactivated autologin.
** gpg.conf improvements
** Installed ca-certificates Debian package.
** Boots faster because of &quot;VBoxManage storagectl --sataportcount 4&quot;.
** No longer removing friendly-recovery.
** Added selectively IsolateDestAddr and IsolateDestPort.
** Expanded and revised whole documentation.
** Gateway and Workstation IPs changed to avoid confusion.
* Whonix-Gateway
** No no longer uses transparet proxying. Whonix-Workstation can still use transparent proxying. Whonix-Gateway now uses uwt for apt-get, gpg, ssh, (tails_)htpdate
** Improved help file: Whonix.
** Added unsafe user account, which can connect without Tor. Not used, unless user logs in as unsafe user.
** Optional feature for /usr/local/bin/whonix_firewall, when activated (disabled by default), root user can connect without Tor.
** Now using stream isolation and uwt.
** Revised helpfile whonix.
** Installing Tor from Debian repositories.
** Allow starting Tor Controller arm without password.
** Now longer opening port 22 on external interface by default. We no longer install over ssh.
* Whonix-Workstation
** KDE is the new desktop environment. KDM the desktop manager. It's a minimal KDE with very few KDE applications.
** Removed Openbox.
** Running every day Whonixcheck
** Greatly improved Whonixcheck, cron job hopefully fixed.
** Installed MAT (Metadata Anonymization Toolkit).
** new commands:
*** xchat-reset (Deletes XChat configuration files and recreates the Whonix original ones, which are tweaked for privacy.)
*** hiddenserver-install (Installs and configures lighttpd)
** Increased RAM for Whonix-Workstation to 768 MB.
** Two shortcuts for Tor Browser. One with default homepage check.torproject.org and one with check.torproject.org and Whonix readme
** New help file whonix.
** Changed Whonix readme url.
** Tor Browser Start and Update script:
** Better error handling.
** Better gpg verification.
** Uses now checks Whonix version, SocksPort, TransPort, stream isolation, Tor Browser version, completely (from the rest of the system) separate streams for GPG and wget.
** Running every day Whonixcheck cron job hopefully fixed.
** Partially fixed gnome-terminal black on black bug. Uses ugly colors and users are hopefully motivated to change the colors.
** new commands:
*** xchat-reset (Deletes XChat configuration files and recreates the Whonix original ones, which are tweaked for privacy.)
*** hiddenserver-install (Installs and configures lighttpd)
* Source Code
** Now building with grml-debootstrap and chroot instead of building inside Virtual Box.<br />
** Now hosted on github, https://github.com/adrelanos/whonix/ and therefore safe against malicious edits by random people.
** All files are now inside their own files and no longer in single big scripts.
** Much more comments.
** Deprecated onevm (no maintainer).
** Deprecated uninstall and uninstall-vm (would require rewrite, was less tested, no users, we don't install the operating system version manually anymore).
** Error handling for everything.
** Uwt
*** wrappers share now most code.
*** New option: -force-install-uwt-dev-passthrough.
*** No longer requires sudo.
*** Added uwt patch from anonym. Thanks! Other unrelated fixes. Updated uwt wrappers for latest uwt.
*** Now using mktemp for torsocks temporary configuration file. Thanks to intrigeri for suggesting it.
*** Some fixes as per https://mailman.boum.org/pipermail/tails-dev/2012-September/001575.html
** torsocks patch deactivated, since no longer required for Debian Wheezy.
** Many fixes, more robustness, step based build system.
** Reduce cpu and network time synchronization.
** Improved uwt, uwt -t server_type -i ip -p port ....
** Whonix-Gateway
** Lowest and cpu disk priority while building.
** import_tpo_archive_key import torproject.org gpg key no longer used. No longer required since switch to Debian Wheezy. Now using Debian repos.
** Added developers-only clearnet traffic passthrough script.
** Bare metal:
*** (untested/unfinished) sudo ./whonix_createvm -tg-bare-metal-pre
*** (untested/unfinished) sudo ./whonix_createvm -tg-bare-metal-pre
** Firewall has now uses uwt for apt-get, gpg, ssh, (tails_)htpdate
** Improved help file: Whonix.
** Optional feature for /usr/local/bin/whonix_firewall, when commented out (disabled by default), root user can connect without Tor.
** Now using stream isolation and uwt.
** Firewall has now an error handler.

= Whonix 0.2.1 Changelog =

<pre>***2012-07-16 0.2.1***
* Download Version
 * Changes
  * You need to make a clean install for both Whonix-Gateway and Whonix-Workstation, incremental update from 0.1 is not supported!
  * Updated to Ubuntu 12.04.
  * Solves &quot;Identity correlation through circuit sharing&quot; by separating streams through different SocksPorts.
  * Integrated leaktest script.
  * Improved Whonix network fingerprint.
   * All TCP and DNS traffic originating from Whonix-Workstation and Whonix-Gateway gets routed through Tor. In the past, Whonix-Gateway send in the clear and an adversary could have found out, that you are using Whonix.
  * Improved hardware fingerprinting resistance.
   * Whonix-Workstation disc uuids are now the same among all Whonix users.
   * MAC addresses are now the same among all Whonix users.
   * CPU model and capabilities are now hidden. (VirtualBox --synthcpu on)
  * Improved support for (obfuscated) bridges.
  * Whonix-Gateway greeting help file.
  * Optionally downloading the alpha version of Tor is easy.
  * Optionally downloading obfsproxy from the Tor alpha repository is easy.
  * Tor Controller**arm** now preinstalled on Whonix-Gateway.
  * Firewall updates.
   * Whonix-Gateway and Whonix-Workstation have now a IPv6 firewall for defense in     depth.
   * Whonix-Workstation has now also an**optional** firewall for defense in depth.
  * Critical issue were an old Tor consensus and entry guards from our build machine was fixed, because we no longer start services while installing them.
  * Powersaving, which is default in Ubuntu, has been disabled for the virtual machines. Screen no longer blacks out.
  * Whonix-Workstation GPG no longer spills operating system and version information, added other privacy and security improving options to gpg.conf as well.
  * torcheck bash script, combined graphical and console version, starts on boot and every 24 hour. It checks Tor Browser version, Tor Socks- and TransPort IPs and if stream isolation is functional.
 * Open issues
  * CPU with PAE required, since Ubuntu Precise no longer ships a non-PAE kernel. We consider switching to Debian once Wheezy is out.
  * torcheck does not work on Whonix-Gateway.
  * Gnome Terminal is black on black. Please change colors manually.
  * More open issues on Whonix/Dev.

* New shell script features
 * Build documentation has been greatly revised and fully automated builds are now supported.
 * The Virtual Machines are now created by command line, ensuring that no step can be forgotten.
 * You need to make a clean install for both Whonix-Gateway and Whonix-Workstation, incremental update from 0.1 is not supported!
 * More comments, which explain almost everything.
 * Huge stylistic improvements.
 * The scripts are now modular. (Consist of functions.)
 * It's now easier to maintain, understand, bugfix and add new features.
 * Scripts can now be run over SSH.
 * Automatic GPG key download for required software and verification.
 * obfsproxy supported out of the box after minor update (commenting in feature).
 * Install torsocks and uwt.
 * Building Whonix inside Whonix (VirtualBox inside VirtualBox) is supported.
 * Deleting all logs to prevent leaking information about your system.
 * Fixed a leak, where the host's DNS settings could leak into the Whonix-Gateway.
 * Whonix-Gateway script
  * new switches
   * -install
   * -uninstall
  * Reverting changes, in case the script fails.
  * Optional features are clearly marked.
   * Hidden Services.
   * Even more restrictive firewall rules.
   * More Socks Ports.
   * Best possible protection against Identity correlation through circuit sharing. (Removes Trans and DnsPort)
   * Leak Testing.
 * Whonix-Workstation script
  * -install
  * -xchat resets XChat.
  * -update-torbrowser updates TorBrowser.
  * -hiddenserver
  * -uwt
  * -update
  * -uninstall</pre>
= older =

<pre>Changelog: 
2012-03-25 0.1.3
* improve fingerprint resistance
* introduce stream isolation features (will be automatically enabled when Tor 0.2.3 becomes stable)
* significantly reduce image sizes
* upgrade TB to current latest stable (2.2.35-9)
2012-03-07 0.1.2
* Internal release, script clean up.
2012-03-03 0.1.1-alpha
* Different default selection of client applications
2012-02-29 0.1-alpha
* Initial Release</pre>
= Footer =

[[include ref=WikiFooter]]

