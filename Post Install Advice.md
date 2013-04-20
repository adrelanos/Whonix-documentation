[[include ref=WikiHeader]]

[TOC]

# Post Install Advice #
## On Whonix-Gateway and Whonix-Workstation ##
### Change Passwords ###
**The default user is:** ***user***

**The default password is:** ***changeme***

Immediately change it!

Login as root:

    sudo su

Change root and user password:

    passwd
    passwd user

and follow the instructions.

### Security Updates ###
Regularly check for **security updates** and apply them with:

    sudo apt-get update && sudo apt-get dist-upgrade

## Network Time Syncing ##
Don't wonder... To prevent against time zone leaks, the system clock inside Whonix was set to UTC. This means it may be a few hours before or ahead of your host system clock. Do not change!

Don't use the suspend/safe/resume feature of Virtual Box, unless you understood the [Network Time Synchronization](https://sourceforge.net/p/whonix/wiki/Advanced%20Security%20Guide/#network-time-synchronization) chapter from the Advanced Security Guide.

If your host clock is more than 1 hour in past or more than 3 hour in future, Tor can't connect. In this case fix your host clock manually (right click on clock). (Check for empty battery.) Then power off Whonix-Gateway and power Whonix-Gateway on again, Tor should be able to connect again. If your host clock is even more off, you could get into trouble updating your host operating system so have an eye on it that it's somewhat accurate.

This chapter is supposed to be as simple and short as possible to provide basic protection. You can archive more security if you understand the [Network Time Synchronization](https://sourceforge.net/p/whonix/wiki/Advanced%20Security%20Guide/#network-time-synchronization) chapter from the Advanced Security Guide.

## Security Guide ##
You can further improve the security, see the [Security Guide](https://sourceforge.net/p/whonix/wiki/Security%20Guide/).

# Footer #
[[include ref=WikiFooter]]