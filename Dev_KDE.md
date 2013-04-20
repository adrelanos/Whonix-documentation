[[include ref=WikiHeader]]

[TOC]

# Changes to the Debian/KDE defaults #

| Application | Changed Setting | Reason | Status
------------- |  ------------- | ------------- | -------------
Dolphin | Always show Menu Bar | Easier to find the button to show hidden files. | Done.
Dolphin | Double click instead single click. | Usability | Done.
Desktop | Change Theme | Prevent confusion of host desktop and Whonix-Workstation desktop.; No legally required, but looking different than the Debian/KDE default theme. | TODO, how?
Desktop | Mouse Theme | Same as above. | TODO, how?
Desktop | Change Wallpaper | Same as above. | Done.
plasma-desktop | folderview instead of desktop view | Displaying desktop icons for the most important applications. | Done.
KGpg | Disabled tip of the day. | - | Done.
KGpg | Disabled first run wizard and configure. | - | Done.
Konsole | Unlimited scroll back | - | Done.
KDE? | Autologin | - | Done.
plasma-desktop |  Digital Clock, set to UTC, show date, show seconds | Without showing UTC it's even more confusing why the clock "wrong".; Show seconds to demonstrate the timesync script is working. | [Upstream BUG](https://bugs.kde.org/show_bug.cgi?id=314224)
plasma-desktop | KGpg unhidden in tray | Usability. Otherwise it looks like it doesn't start. It would start, but only hidden in tray. | FAIL. TODO, how?
plasma-desktop | start menu favorites | Usability. Highlighting most important applications. | Done.

# Added Desktop Icons #
| Application | Changed Setting | Reason | Status
------------- |  ------------- | ------------- | -------------
plasma-desktop | Synaptic (install software) | - | Done.
plasma-desktop | Tor Browser Updater Icon | - | Done.
plasma-desktop | Tor Browser | - | Done.
plasma-desktop | Documentation | Encouraging reading documentation. | Done.
plasma-desktop | Tor Browser Recommend | Encouraging users to read Whonix Feature Blog or at least Whonix Important Blog. | Done.
plasma-desktop | XChat | - | Done.
plasma-desktop | Whonixcheck | - | Done.
plasma-desktop | Timesync | - | Done.
plasma-desktop | Whonix Readme | - | Done.
plasma-desktop | konsole | - | Done.
plasma-desktop | User Help Forum | Support. Building a community. | Done.
plasma-desktop | Developer Mailing List | Attracting developers. | Done.
plasma-desktop | Contribute | Encouraging contributions. | Done.
plasma-desktop | Donate | Encouraging donations. | Done.
plasma-desktop | Feature Blog | - | Done.
plasma-desktop | Important Blog | - | Done.

# KDE Lowfat Settings
Will appear in Whonix 0.6.0 and above.

[KDE Mailing list: How to learn about all those configuration file values?](http://lists.kde.org/?l=kde&m=136497689725852&w=2)

## kdedrc
https://github.com/adrelanos/Whonix/blob/kdelowfat/whonix_workstation/usr/local/share/whonix/kde/share/config/kdedrc

    ## What does it do: Disable KDE Bluetooth integration
    ## Source: http://userbase.kde.org/Bluedevil
    ## Whonix: Not required in Whonix 
    [Module-bluedevil]
    autoload=false

kcmshell4 --list | grep mount, gives me device_automounter_kcm, with a 
description: "Configure automatic handling of removable storage media".   
kcmshell4 device_automounter_kcm give me... well you can try it.  

Of course that's the Removable Device Automounter, as listed in the 
services configuration (kcmkded).

Without this module running the new removable device should still show up 
in device-notifier, but the configured automount actions won't occur.  
This one will strongly depend on whether the user is willing to jump thru 
manual hoops to mount a newly plugged removable storage device, or would 
prefer that kde handled it even at the expense of a bit of kde startup 
speed and memory for the automounting service.  Of course people like me 
don't like kde mounting stuff behind their back anyway, so turning it off 
is an easy choice here, but a lot of users want the system to handle 
it... if they even know anything about mounting to begin with.

http://lists.kde.org/?l=kde&m=136497689725852&w=2

    [Module-device_automounter]
    autoload=true

http://lists.kde.org/?l=kde&m=136497689725852&w=2

    [Module-dnssdwatcher]
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
    autoload=false

http://lists.kde.org/?l=kde&m=136497689725852&w=2 I /think/ this is Network Status in kcmkded.  But as I don't run network-manager or the like at all, instead using initscripts for my network management, I have absolutely no experience with this. 

    [Module-networkmanagement]
    autoload=false

    [Module-obexftpdaemon]
    autoload=false

http://lists.kde.org/?l=kde&m=136497689725852&w=2 kcmkded says display management change monitor.  Probably useful for laptop users that often plug external monitors or who frequently change resolution, not so much for folks who always run the same monitor config 
and resolution.

    [Module-randrmonitor]
    autoload=false

http://lists.kde.org/?l=kde&m=136497689725852&w=2 Remote URL change notifier.  For those with network folders this is 
probably useful.  Otherwise, not so much.

    [Module-remotedirnotify]
    autoload=false

## kdeglobals

https://github.com/adrelanos/Whonix/blob/kdelowfat/whonix_workstation/usr/local/share/whonix/kde/share/config/kdeglobals

    ## What does it do: sets the widget style to plastic
    [General]
    widgetStyle=plastique

    ## What does it do: set the graphiceffecstlevel parameter to 0
    [KDE-Global GUI Settings]
    GraphicEffectsLevel=0

## knotifyrc

https://github.com/adrelanos/Whonix/blob/kdelowfat/whonix_workstation/usr/local/share/whonix/kde/share/config/knotifyrc

    ## What does it do: Disables sound in knotify notifications
    ## Source: http://www.linuxquestions.org/questions/linux-desktop-74/kde-system-notifications-not-working-kde-3-5-8-debian-testing-branch-631616/ | https://bugs.kde.org/show_bug.cgi?format=multiple&amp;id=95062 | http://linux.error-exception.org/article/1254821/KNotify+crashes+often | https://bbs.archlinux.org/viewtopic.php?id=132307
    [Sounds]
    No sound=true

## krunnerrc

https://github.com/adrelanos/Whonix/blob/kdelowfat/whonix_workstation/usr/local/share/whonix/kde/share/config/krunnerrc

    ## What does it do: To start the kde session fresh, it makes the applications
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
    solidEnabled=false

## ksmserverrc

https://github.com/adrelanos/Whonix/blob/kdelowfat/whonix_workstation/usr/local/share/whonix/kde/share/config/ksmserverrc

    ## What does it do: To start the kde session fresh, it makes the applications
    ## that was open (with tabs and contents), to start again without any kind of data.
    ## It wipes the applications that were open from the desktop.
    ## Source: http://techbase.kde.org/KDE_System_Administration/Startup and
    ## http://www.backtrack-linux.org/forums/archive/index.php/t-8210.html
    [General]
    loginMode=default

## kwinrc

https://github.com/adrelanos/Whonix/blob/kdelowfat/whonix_workstation/usr/local/share/whonix/kde/share/config/kwinrc

    ## What does it do: Disables kde window compositing.
    ## Source: http://techbase.kde.org/KDE_System_Administration/Startup and
    ## http://www.kubuntuforums.net/archive/index.php/t-59569.html
    [Compositing]
    Enabled=false

    ## What does it do: Sets the window decoration to 'kwin3_plastik' .
    ## Source: http://techbase.kde.org/KDE_System_Administration/Startup
    ## http://www.kubuntuforums.net/archive/index.php/t-59569.html
    [Style]
    PluginLib=kwin3_plastik

## nepomukserverrc

https://github.com/adrelanos/Whonix/blob/kdelowfat/whonix_workstation/usr/local/share/whonix/kde/share/config/nepomukserverrc

    ## What does it do: Makes the daemon which hosts all Nepomuk service including
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
    Maximum memory=10

# Footer #
[[include ref=WikiFooter]]