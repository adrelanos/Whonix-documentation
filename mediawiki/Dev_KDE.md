[[include ref=WikiHeader]]

[TOC]

= Changes to the Debian/KDE defaults =

<table>
<thead>
<tr class="header">
<th align="left">Application</th>
<th align="left">Changed Setting</th>
<th align="left">Reason</th>
<th align="left">Status</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Dolphin</td>
<td align="left">Always show Menu Bar</td>
<td align="left">Easier to find the button to show hidden files.</td>
<td align="left">Done.</td>
</tr>
<tr class="even">
<td align="left">Dolphin</td>
<td align="left">Double click instead single click.</td>
<td align="left">Usability</td>
<td align="left">Done.</td>
</tr>
<tr class="odd">
<td align="left">Desktop</td>
<td align="left">Change Theme</td>
<td align="left">Prevent confusion of host desktop and Whonix-Workstation desktop.; No legally required, but looking different than the Debian/KDE default theme.</td>
<td align="left">TODO, how?</td>
</tr>
<tr class="even">
<td align="left">Desktop</td>
<td align="left">Mouse Theme</td>
<td align="left">Same as above.</td>
<td align="left">TODO, how?</td>
</tr>
<tr class="odd">
<td align="left">Desktop</td>
<td align="left">Change Wallpaper</td>
<td align="left">Same as above.</td>
<td align="left">Done.</td>
</tr>
<tr class="even">
<td align="left">plasma-desktop</td>
<td align="left">folderview instead of desktop view</td>
<td align="left">Displaying desktop icons for the most important applications.</td>
<td align="left">Done.</td>
</tr>
<tr class="odd">
<td align="left">KGpg</td>
<td align="left">Disabled tip of the day.</td>
<td align="left">-</td>
<td align="left">Done.</td>
</tr>
<tr class="even">
<td align="left">KGpg</td>
<td align="left">Disabled first run wizard and configure.</td>
<td align="left">-</td>
<td align="left">Done.</td>
</tr>
<tr class="odd">
<td align="left">Konsole</td>
<td align="left">Unlimited scroll back</td>
<td align="left">-</td>
<td align="left">Done.</td>
</tr>
<tr class="even">
<td align="left">KDE?</td>
<td align="left">Autologin</td>
<td align="left">-</td>
<td align="left">Done.</td>
</tr>
<tr class="odd">
<td align="left">plasma-desktop</td>
<td align="left">Digital Clock, set to UTC, show date, show seconds</td>
<td align="left">Without showing UTC it's even more confusing why the clock &quot;wrong&quot;.; Show seconds to demonstrate the timesync script is working.</td>
<td align="left">[https://bugs.kde.org/show_bug.cgi?id=314224 Upstream BUG]</td>
</tr>
<tr class="even">
<td align="left">plasma-desktop</td>
<td align="left">KGpg unhidden in tray</td>
<td align="left">Usability. Otherwise it looks like it doesn't start. It would start, but only hidden in tray.</td>
<td align="left">FAIL. TODO, how?</td>
</tr>
<tr class="odd">
<td align="left">plasma-desktop</td>
<td align="left">start menu favorites</td>
<td align="left">Usability. Highlighting most important applications.</td>
<td align="left">Done.</td>
</tr>
</tbody>
</table>

= Added Desktop Icons =

<table>
<thead>
<tr class="header">
<th align="left">Application</th>
<th align="left">Changed Setting</th>
<th align="left">Reason</th>
<th align="left">Status</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">plasma-desktop</td>
<td align="left">Synaptic (install software)</td>
<td align="left">-</td>
<td align="left">Done.</td>
</tr>
<tr class="even">
<td align="left">plasma-desktop</td>
<td align="left">Tor Browser Updater Icon</td>
<td align="left">-</td>
<td align="left">Done.</td>
</tr>
<tr class="odd">
<td align="left">plasma-desktop</td>
<td align="left">Tor Browser</td>
<td align="left">-</td>
<td align="left">Done.</td>
</tr>
<tr class="even">
<td align="left">plasma-desktop</td>
<td align="left">Documentation</td>
<td align="left">Encouraging reading documentation.</td>
<td align="left">Done.</td>
</tr>
<tr class="odd">
<td align="left">plasma-desktop</td>
<td align="left">Tor Browser Recommend</td>
<td align="left">Encouraging users to read Whonix Feature Blog or at least Whonix Important Blog.</td>
<td align="left">Done.</td>
</tr>
<tr class="even">
<td align="left">plasma-desktop</td>
<td align="left">XChat</td>
<td align="left">-</td>
<td align="left">Done.</td>
</tr>
<tr class="odd">
<td align="left">plasma-desktop</td>
<td align="left">Whonixcheck</td>
<td align="left">-</td>
<td align="left">Done.</td>
</tr>
<tr class="even">
<td align="left">plasma-desktop</td>
<td align="left">Timesync</td>
<td align="left">-</td>
<td align="left">Done.</td>
</tr>
<tr class="odd">
<td align="left">plasma-desktop</td>
<td align="left">Whonix Readme</td>
<td align="left">-</td>
<td align="left">Done.</td>
</tr>
<tr class="even">
<td align="left">plasma-desktop</td>
<td align="left">konsole</td>
<td align="left">-</td>
<td align="left">Done.</td>
</tr>
<tr class="odd">
<td align="left">plasma-desktop</td>
<td align="left">User Help Forum</td>
<td align="left">Support. Building a community.</td>
<td align="left">Done.</td>
</tr>
<tr class="even">
<td align="left">plasma-desktop</td>
<td align="left">Developer Mailing List</td>
<td align="left">Attracting developers.</td>
<td align="left">Done.</td>
</tr>
<tr class="odd">
<td align="left">plasma-desktop</td>
<td align="left">Contribute</td>
<td align="left">Encouraging contributions.</td>
<td align="left">Done.</td>
</tr>
<tr class="even">
<td align="left">plasma-desktop</td>
<td align="left">Donate</td>
<td align="left">Encouraging donations.</td>
<td align="left">Done.</td>
</tr>
<tr class="odd">
<td align="left">plasma-desktop</td>
<td align="left">Feature Blog</td>
<td align="left">-</td>
<td align="left">Done.</td>
</tr>
<tr class="even">
<td align="left">plasma-desktop</td>
<td align="left">Important Blog</td>
<td align="left">-</td>
<td align="left">Done.</td>
</tr>
</tbody>
</table>

= KDE Lowfat Settings =

Will appear in Whonix 0.6.0 and above.

[http://lists.kde.org/?l=kde&m=136497689725852&w=2 KDE Mailing list: How to learn about all those configuration file values?]

== kdedrc ==

https://github.com/adrelanos/Whonix/blob/kdelowfat/whonix_workstation/usr/local/share/whonix/kde/share/config/kdedrc

<pre>## What does it do: Disable KDE Bluetooth integration
## Source: http://userbase.kde.org/Bluedevil
## Whonix: Not required in Whonix 
[Module-bluedevil]
autoload=false</pre>
kcmshell4 --list | grep mount, gives me device_automounter_kcm, with a description: &quot;Configure automatic handling of removable storage media&quot;.<br />kcmshell4 device_automounter_kcm give me... well you can try it.

Of course that's the Removable Device Automounter, as listed in the services configuration (kcmkded).

Without this module running the new removable device should still show up in device-notifier, but the configured automount actions won't occur.<br />This one will strongly depend on whether the user is willing to jump thru manual hoops to mount a newly plugged removable storage device, or would prefer that kde handled it even at the expense of a bit of kde startup speed and memory for the automounting service. Of course people like me don't like kde mounting stuff behind their back anyway, so turning it off is an easy choice here, but a lot of users want the system to handle it... if they even know anything about mounting to begin with.

http://lists.kde.org/?l=kde&amp;m=136497689725852&amp;w=2

<pre>[Module-device_automounter]
autoload=true</pre>
http://lists.kde.org/?l=kde&amp;m=136497689725852&amp;w=2

<pre>[Module-dnssdwatcher]
autoload=false

## What does it do: This module notifies the user when /home or one of
## the other directories which you can configure it to monitor are
## running out of space. 
## Source: http://packages.debian.org/unstable/main/freespacenotifier
## Whonix: We should probable leave it enabled.
[Module-freespacenotifier]
autoload=true

[Module-kwrited]
autoload=false

[Module-nepomuksearchmodule]
autoload=false</pre>
http://lists.kde.org/?l=kde&amp;m=136497689725852&amp;w=2 I /think/ this is Network Status in kcmkded. But as I don't run network-manager or the like at all, instead using initscripts for my network management, I have absolutely no experience with this.

<pre>[Module-networkmanagement]
autoload=false

[Module-obexftpdaemon]
autoload=false</pre>
http://lists.kde.org/?l=kde&amp;m=136497689725852&amp;w=2 kcmkded says display management change monitor. Probably useful for laptop users that often plug external monitors or who frequently change resolution, not so much for folks who always run the same monitor config and resolution.

<pre>[Module-randrmonitor]
autoload=false</pre>
http://lists.kde.org/?l=kde&amp;m=136497689725852&amp;w=2 Remote URL change notifier. For those with network folders this is probably useful. Otherwise, not so much.

<pre>[Module-remotedirnotify]
autoload=false</pre>
== kdeglobals ==

https://github.com/adrelanos/Whonix/blob/kdelowfat/whonix_workstation/usr/local/share/whonix/kde/share/config/kdeglobals

<pre>## What does it do: sets the widget style to plastic
[General]
widgetStyle=plastique

## What does it do: set the graphiceffecstlevel parameter to 0
[KDE-Global GUI Settings]
GraphicEffectsLevel=0</pre>
== knotifyrc ==

https://github.com/adrelanos/Whonix/blob/kdelowfat/whonix_workstation/usr/local/share/whonix/kde/share/config/knotifyrc

<pre>## What does it do: Disables sound in knotify notifications
## Source: http://www.linuxquestions.org/questions/linux-desktop-74/kde-system-notifications-not-working-kde-3-5-8-debian-testing-branch-631616/ | https://bugs.kde.org/show_bug.cgi?format=multiple&amp;amp;id=95062 | http://linux.error-exception.org/article/1254821/KNotify+crashes+often | https://bbs.archlinux.org/viewtopic.php?id=132307
[Sounds]
No sound=true</pre>
== krunnerrc ==

https://github.com/adrelanos/Whonix/blob/kdelowfat/whonix_workstation/usr/local/share/whonix/kde/share/config/krunnerrc

<pre>## What does it do: To start the kde session fresh, it makes the applications
## that was open (with tabs and contents), to start again without any kind of
## data. It wipes the applications that were open from the desktop.
## Source: http://techbase.kde.org/KDE_System_Administration/Startup and
## http://www.backtrack-linux.org/forums/archive/index.php/t-8210.html
## Note: in this case this is what krunnerrc does, not this specific module.
## Couldn't find a more specific information. 

[Plugins]

## Deactivate for better performance and privacy.

PowerDevilEnabled=false
nepomuksearchEnabled=false
bookmarksEnabled=false
webshortcutsEnabled=false
recentdocumentsEnabled=false

## Let's leave the default (enable).

placesEnabled=true
calculatorEnabled=true
desktopsessionsEnabled=true
installerEnabled=true
killEnabled=true
locationsEnabled=true
shellEnabled=true
org.kde.windowedwidgetsEnabled=true
windowsEnabled=true
plasma-desktopEnabled=true

## Unsure.
servicesEnabled=true
solidEnabled=false</pre>
== ksmserverrc ==

https://github.com/adrelanos/Whonix/blob/kdelowfat/whonix_workstation/usr/local/share/whonix/kde/share/config/ksmserverrc

<pre>## What does it do: To start the kde session fresh, it makes the applications
## that was open (with tabs and contents), to start again without any kind of data.
## It wipes the applications that were open from the desktop.
## Source: http://techbase.kde.org/KDE_System_Administration/Startup and
## http://www.backtrack-linux.org/forums/archive/index.php/t-8210.html
[General]
loginMode=default</pre>
== kwinrc ==

https://github.com/adrelanos/Whonix/blob/kdelowfat/whonix_workstation/usr/local/share/whonix/kde/share/config/kwinrc

<pre>## What does it do: Disables kde window compositing.
## Source: http://techbase.kde.org/KDE_System_Administration/Startup and
## http://www.kubuntuforums.net/archive/index.php/t-59569.html
[Compositing]
Enabled=false

## What does it do: Sets the window decoration to 'kwin3_plastik' .
## Source: http://techbase.kde.org/KDE_System_Administration/Startup
## http://www.kubuntuforums.net/archive/index.php/t-59569.html
[Style]
PluginLib=kwin3_plastik</pre>
== nepomukserverrc ==

https://github.com/adrelanos/Whonix/blob/kdelowfat/whonix_workstation/usr/local/share/whonix/kde/share/config/nepomukserverrc

<pre>## What does it do: Makes the daemon which hosts all Nepomuk service including
## the main Nepomuk data repository not to start at logging time.
## Source: http://techbase.kde.org/index.php?title=Development/Tutorials/Metadata/Nepomuk/NepomukServer
[Basic Settings]
Start Nepomuk=false

## What does it do: It prevents the use of 'Strigi', a module of nepomuk that
## can be used for a full file indexing framework (is the desktop file indexer)
## Source: http://techbase.kde.org/Projects/Nepomuk/ComponentOverview/en#Strigi
[Service-nepomukstrigiservice]
autostart=false

## What does it do: Sets the maximum memory at 10.
[main Settings]
Maximum memory=10</pre>
= Footer =

[[include ref=WikiFooter]]

