[[include ref=WikiHeader]]

[TOC]

# Network Manager
It would be desirable to have a graphical network manager installed in Whonix-Workstation. There are a few main use cases. Changing Whonix-Workstation's internal IP address for [Multiple Whonix-Workstations](https://sourceforge.net/p/whonix/wiki/Multiple%20Whonix-Workstations/), setting up a post-Tor-VPN using a graphical user interface and other kinds of advanced network configurations over Tor which are simpler to set up using a grapical user interface.

At the moment networking still managed by the ordinary ifupdown way in /etc/network/interfaces.

If you want to install the KDE Network Manager.

    sudo apt-get install network-manager-kde

Then it can be started from the Start Menu.

    Start menu -> System Settings -> Network Settings

You won't see Whonix's internal network interface right away. You could make it visible in Network Manger, by editing /etc/NetworkManager/NetworkManager.conf and setting managed to true.

    [main]
    plugins=ifupdown,keyfile

    [ifupdown]
    managed=true

That would be quite useful, if changing settings where possible. However, the NetworkManager.conf man page says, write support for ifupdown managed devices isn't planed.

The Fedora wiki has a nice page about [Network Manager](https://fedoraproject.org/wiki/Tools/NetworkManager) which is useful for a distro packager perspective.

Quote:
> "*NM is slowly changing from a desktop network connection configurator to a universal network configuration software that could be used as a part of the base system.*"

Once NM can do everything ifupdown can do (i.e. suitable for all tasks also from command line), ifupdown in Whonix could get completely replaced with NM.

Since IPv6 support in NM is said to be not in a production state yet, I am hesitate to switch to NM. Tor recently added support for IPv6 bridges and full IPv6 support could come in future. If Tor fixes IPv6 support first, there would eventually still (again) need for ifupdown. Therefore I think at the moment it's best to let NM mature.

For running NM on Whonix-Gateway it would be required to check if the pre-up hook to start the firewall works flawless. Having a pre-up hook which fails closed like ifupdown currently provides is desirable, because when there is a tiny syntax error in the firewall, the network won't come up and nothing leaks. Alternatively, an init.d script could be developed, it would have to be researched, if it can provide the same fail closed protections.

Since many people are interested in post-Tor-VPNs (user -> Tor -> VPN), it is open for debate if network-manager-kde should be pre-installed on Whonix-Workstation. Would the user be confused because it won't show the (virtual) wired internal network interface? Would it be less/more confusing the the (virtual) wired internal network interface where shown but impossible to edit? Shouldn't it be pre-installed for these confusion reasons and be recommend to be installed manually for users interested in post-Tor-VPNs?

As a footnote, it's also possible to use Gnome applications in Whonix (KDE based), such as [Gnome Network Manager chapter on TestVPN page](https://sourceforge.net/p/whonix/wiki/TestVPN/#gnome-network-manager).

[Quote](https://bugzilla.gnome.org/show_bug.cgi?id=689339#c4):

> "*Please also understand that currently networkmanager is not a security tool at
all. VPN plugins are regarded as connectivity plugins, not security plugins.*"

Missing auto-reconnect feature:
https://bugzilla.gnome.org/show_bug.cgi?id=349151

So perhaps using NM to set up VPNs for security isn't a good idea.

Doesn't look like NM has a fail closed mechanism:
[VPN-Firewall]

# Footer #
[[include ref=WikiFooter]]