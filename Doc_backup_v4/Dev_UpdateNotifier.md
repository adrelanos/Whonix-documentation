[[include ref=WikiHeader]]

[TOC]

# Implemented #
## apper (kde) package ##
**After 0.4.5!**

whonixcheck runs *apt-get update*. Checks if there are updates with */usr/lib/update-notifier/apt-check*. If there are updates, it opens *apper --updates*, if installed. (Otherwise notifies about updates only in whonixcheck result.)

Apper is user friendly since there is only one big update button and does also honor proxy settings in */etc/apt/apt.conf* which are required for Tor stream isolation.

Automatic update check has been disabled in */etc/apt/apt.conf.d/10periodic* because the execution time would be too predictable. Whonixcheck runs at startup (non-predictable) and every day at a random time.

# Rejects ideas #
## update-notifier (gnome) package ##
Overall ui is very good. Asks a confusing question to update "safely" and not removing packages. After updating "safely" it still reports updates. Open question: how to translate update-notifer? Would be all gnome language packages needed?

Would have to configure it with something like "gconftool-2 --config-source xml:readwrite:/etc/gconf/gconf.xml.mandatory". Would have to 

	cp /etc/xdg/autostart/update-notifier.desktop /etc/xdg/autostart/update.desktop

And remove shownotin kde from /etc/xdg/autostart/update.desktop.

## update-notifier-kde package ##
Is a bit confusing. It shows how many udpates are available, but it has only one button "later".

# Footer #
[[include ref=WikiFooter]]