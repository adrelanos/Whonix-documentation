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
plasma-desktop |  Digital Clock, set to UTC, show date, show seconds | Without showing UTC it's even more confusing why it's "wrong".; Show seconds to demonstrate the timesync script is working. | [Upstream BUG](https://bugs.kde.org/show_bug.cgi?id=314224)
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
**UNDER DEVELOPMENT! Candidate for next Whonix version.***

https://github.com/adrelanos/Whonix/blob/kdelowfat/whonix_workstation/usr/local/share/whonix/kde/share/config/kdedrc

    [Module-bluedevil]
    autoload=false

    [Module-device_automounter]
    autoload=false

    [Module-dnssdwatcher]
    autoload=false

    [Module-freespacenotifier]
    autoload=false

    [Module-kwrited]
    autoload=false

    [Module-nepomuksearchmodule]
    autoload=false

    [Module-networkmanagement]
    autoload=false

    [Module-obexftpdaemon]
    autoload=false

    [Module-randrmonitor]
    autoload=false

    [Module-remotedirnotify]
    autoload=false

https://github.com/adrelanos/Whonix/blob/kdelowfat/whonix_workstation/usr/local/share/whonix/kde/share/config/kdeglobals

    [General]
    widgetStyle=plastique

    [KDE-Global GUI Settings]
    GraphicEffectsLevel=0

https://github.com/adrelanos/Whonix/blob/kdelowfat/whonix_workstation/usr/local/share/whonix/kde/share/config/knotifyrc

    [Sounds]
    No sound=true

https://github.com/adrelanos/Whonix/blob/kdelowfat/whonix_workstation/usr/local/share/whonix/kde/share/config/krunnerrc

    [Plugins]
    PowerDevilEnabled=false
    bookmarksEnabled=false
    calculatorEnabled=false
    desktopsessionsEnabled=false
    installerEnabled=false
    killEnabled=false
    locationsEnabled=false
    nepomuksearchEnabled=false
    org.kde.windowedwidgetsEnabled=false
    placesEnabled=false
    plasma-desktopEnabled=false
    recentdocumentsEnabled=false
    servicesEnabled=true
    shellEnabled=true
    solidEnabled=false
    webshortcutsEnabled=false
    windowsEnabled=false

https://github.com/adrelanos/Whonix/blob/kdelowfat/whonix_workstation/usr/local/share/whonix/kde/share/config/ksmserverrc

    [General]
    loginMode=default

https://github.com/adrelanos/Whonix/blob/kdelowfat/whonix_workstation/usr/local/share/whonix/kde/share/config/kwinrc

    [Compositing]
    Enabled=false

    [Style]
    PluginLib=kwin3_plastik

https://github.com/adrelanos/Whonix/blob/kdelowfat/whonix_workstation/usr/local/share/whonix/kde/share/config/nepomukserverrc

    [Basic Settings]
    Start Nepomuk=false

    [Service-nepomukstrigiservice]
    autostart=false

    [main Settings]
    Maximum memory=10

# Footer #
[[include ref=WikiFooter]]