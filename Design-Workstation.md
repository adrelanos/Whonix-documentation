[[include ref=WikiHeader]]

[TOC]

# List of installed Packages

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/Whonix-Workstation_packages

# Files
## Essential
### Network Configuration
Configure the system resolver to use the Gateway to resolve DNS. (There can be no DNS leaks, because the Gateway firewall prevents that.) It shouldn't get used often, only for applications which are not configured to use stream isolation (SocksPort). Just as a general catch all for user installed applications to improve usability.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/etc/resolv.conf
* https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/etc/network/interfaces

### DummyTor
Since the anonymizer software runs on the Gateway, users could still accidental install the anonymizer software on the Workstation. This would lead into connecting to the anonymity network over the anonymity network itself. In best case it just doesn't work or is very slow and in worst case it leads to unknown consequences. Prevent that.

Whonix-Example-Implementation:

* Banning the Tor package from Whonix-Workstation to prevent Tor over Tor. https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/usr/local/share/whonix/chroot-scripts/70_dummytor
* Install an empty Tor package which does no more than simulating, that Tor is already installed and thus preventing the package manager from installing Tor, see also [DummyTor].
* DummyTor package description file: https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/usr/local/share/whonix/dummytor/tor
* rinetd (see below) also prevents Tor from opening the default listener on port 9050. Therefore the Tor service will fail to start.

### KDE / GNOME - application wide proxy settings
Whether KDE / GNOME will be used or not, in addition to stream isolation wrappers and other preconfigured applications for stream isolation, in addition it's useful to also configure KDE / GNOME - wide proxy settings. In case the user installs KDE or GNOME applications, which connect to the internet, which honor proxy settings, those won't go through Tor's TransPort, but through a dedicated SocksPort for further improved stream isolation. These settings are not system-wide, but KDE-wide / GNOME-wide.

Whonix-Example-Implementation:

* KDE: https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/usr/local/share/whonix/kde/share/config/kioslaverc
* GNOME: Not yet implemented. [TODO](https://sourceforge.net/p/whonix/wiki/Dev_GNOME/)

## Extra
### second, optional, extra firewall
Optional.

Optional second, optional, extra firewall for advanced users as damage protection in case the Whonix-Gateway gets ever compromised (Tor exploit).

Whonix-Example-Implementation:

* Please read the script comments.
* Firewall script: https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/usr/local/bin/whonix_firewall
* Configuration file: https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/etc/whonix_firewall.d/10_default

## Usability
### Swap
Let the kernel only swap if it is absolutely necessary.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/etc/sysctl.d/whonix.conf

### Environment Variables
Optional.

It's useful to have an environment variable announcing "I am a Workstation", so applications such as TorButton and TorBirdy can act accordingly. (I.e. not starting Tor/Vidalia on the Workstation; not using 127.0.0.1 as proxy, but therefore the Gateway.)

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/etc/profile.d/20_whonix.sh
* https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/etc/profile.d/20_torbrowser.sh

### apt.conf
Optional.

Whonix-Example-Implementation:

* Doesn't do anything by default. Just some comments. https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/etc/apt/apt.conf.d/90whonix
* (apt is forced though Tor by apt-get uwt wrapper (Design-Shared) and by the firewall running on the Gateway.

### http to socks converter
Optional.

Some applications don't support socks, but http. It's useful to have a http to socks converter.

Whonix-Example-Implementation:

* None required to be installed by default.
* If someone likes to use polipo, the config file from torproject.org is shipped. (Only adapted to use the Whonix-Gateway. https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/etc/polipo/config

### Sending e-mails without registration
Optional.

Install a tool, which can send e-mails without registration.

Whonix-Example-Implementation:

* Using Mixmaster. (Of course over Tor.)
* Implementation notes: https://sourceforge.net/p/whonix/wiki/Dev_Mixmaster/
* https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/home/user/.Mix/mix.cfg
* Documented on [Remailer] and [Mixmaster] page.

### GnuPG Configuration
Optional.

Using more secure defaults for GnuPG.

Whonix-Example-Implementation:

* Using more secure defaults. https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/home/user/.gnupg/gpg.conf

### Project News Notification
Optional.

Whonix-Example-Implementation:

* Using rawdog, a privacy friendly rss reader to download Whonix News Blogs.
* Privacy friendly as in, once it downloaded the blog's content, there will be no incoming/outgoing traffic. The page can be viewed offline and contains no tracking scripts.
* Non-ideal configuration. In rawdog config is a https link with a sourceforge rss feed, which unfortunately redirects to a non-https page, which rawdog follows. Thus, news isn't fetched over https and a man-in-the-middle could spread malicious news.

* rawdog Configuration folder: https://github.com/adrelanos/Whonix/tree/master/whonix_workstation/home/user/.rawdog/
* Documented on page [rss] and [Download (Stay Tuned)](https://sourceforge.net/p/whonix/wiki/Download/#stay-tuned) page.
* rawdog gets run by whonixcheck. (See [Design-Shared].)
* The user is asked to prefer to start Tor Browser using the Tor Browser Recommend shortcut on the Desktop: https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/usr/local/share/whonix/kde/share/applications/whonix-tbrecommend.desktop

### TorChat Configuration
Optional.

Using TorChat on a already torified Workstation while preventing Tor over Tor isn't trivial. Therefore it's useful to ship required configuration files, preconfigured as much as possible by default to ease installation of TorChat.

Whonix-Example-Implementation:

* TorChat does **not** get installed by default.
* Due to popular request, Whonix makes it as easy as possible to use TorChat with Whonix.
* https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/home/user/.torchat/torchat.ini
* Documented on [Chat] page.
* Banning the Tor package from Whonix-Workstation to prevent Tor over Tor. https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/usr/local/share/whonix/chroot-scripts/70_dummytor

### IRC Client
Optional.

Secure IRC Client configuration and script for getting a new IRC identity.

Whonix-Example-Implementation:

* Whonix comes with XChat configured for privacy.
* https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/usr/local/bin/xchat-reset
* Documented on [XChat] page.
* Configuration files. https://github.com/adrelanos/Whonix/tree/master/whonix_workstation/usr/local/share/whonix/xchat2
* Deactivating plugins. https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/usr/local/share/whonix/chroot-scripts/70_xchat

### Web Browser
Secure Web Browser, which doesn't suffer from likability and browser fingerprinting.

Whonix-Example-Implementation:

* Whonix comes with Tor Browser, which is maintained by The Tor Project.
* Reasons for TorBrowser can be found on the [TorBrowser] page.
* Documented on [TorBrowser] page.
* torbrowser update script: https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/usr/local/bin/torbrowser
* Patched torbrowser startup script to make Tor Browser work without the bundled Tor and Vidalia: https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/usr/local/share/whonix/start-tor-browser The torbrowser update script https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/usr/local/bin/torbrowser keeps care to replace the upstream start-tor-browser file.
* Install Tor Browser while building Whonix: https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/usr/local/share/whonix/chroot-scripts/70_torbrowser
* Environment variables: https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/etc/profile.d/20_torbrowser.sh
* Gpg keys to verify the downloaded Tor Browser:
    * https://github.com/adrelanos/Whonix/tree/master/whonix_workstation/usr/local/share/whonix/gpg-pubkeys
    * https://sourceforge.net/p/whonix/wiki/Dev_SourceCodeIntro/#gpg-keys

### rinetd
Optional.

Whonix-Example-Implementation:

* rinetd is configured to listen on local ports 9050 and 9150.
    * rinetd forwards port 127.0.0.1:9050 (Workstation) to 192.168.0.10:9050 (Gateway).
    * Forwards port 127.0.0.1:9150 (Workstation) to 192.168.0.10:9150 (Gateway).
    * https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/etc/rinetd.conf
    * This prevents Tor over Tor by just installing Tor or by using the complete Tor Browser Bundle, which starts Vidalia and Tor. This is because, it listens on port 9050 and 9150 and therefore lets a default Tor or TBB fail to start.
    * Should the Tor Browser update script ever break,
        * Whonix users can download (and verify) the stock Tor Browser Bundle (TBB) from torproject.org,
        * unpack to /home/user/tor-browser_en-US and
        * start it from the desktop menu shortcut or from the start menu.
        * As long as The Tor Project will still ship Vidalia with TBB: Starting with the stock startup script /home/user/tor-browser_en-US/start-tor-browser will fail closed. Vidalia will report, that Tor won't connect, because port 9150 is already blocked by rinetd. This will be fixed as soon as The Tor Project merges a proposed patch https://trac.torproject.org/projects/tor/ticket/5611 for the start-tor-browser startup script, which adds an optional environment variable, once set, only starts Tor Browser and not the bundled Tor/Vidalia.
        * As soon as The Tor Project moved to tor-launcher and drops Vidalia: Starting stock TBB inside Whonix should work out of the box, because https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/etc/profile.d/20_torbrowser.sh sets the required environment variables to deactivate tor-launcher.

### Marker file
Optional.

Add a marker file so scripts you write can find out, whether they are running on the Gateway or inside the Workstation. There are probable different implementations possible to reach that goal.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/usr/local/share/whonix/whonix_workstation

### Terminal Help
Optional.

Add a welcome and help message also to virtual terminals. (Those which can get started in graphical environments such as KDE and Konsole.)

Whonix-Example-Implementation:

* Default Debian .bashrc at the top and Whonix specific additions at the bottom: https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/home/user/.bashrc
* Whonix-Workstation terminal help file: https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/usr/local/bin/whonix

## Debugging
### Leaktest script
Optional.

Have a script to try to produce a leak and check if there are any leaks.

Whonix-Example-Implementation:

* https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/usr/local/bin/leaktest
* https://github.com/adrelanos/Whonix/tree/master/whonix_workstation/usr/local/share/whonix/leaktest
* [LeakTests]

# Design-Shared
Changes from [Design-Shared] also have to be added to the Gateway.

# Footer #
[[include ref=WikiFooter]]