[[include ref=WikiHeader]]

[TOC]

# Introduction #
We explain the risks of browser plugins (flash etc.), discuss some alternatives and finally explain how to use browser plugins anyway in the best possible secure manner.

# Tor Browser #
For information about Tor Browser in general, see [Tor Browser](https://sourceforge.net/p/whonix/wiki/TorBrowser/).

# Warning not to use them #
Quoted the Whonix [Features] page:
"*Java / JavaScript / flash / browser plugins / [Malware](https://en.wikipedia.org/wiki/Malware) / misconfigured applications cannot leak your real external IP.*" <font size="-3">"*This is still not recommended as they may decrease anonymity (e.g. flash cookies) and often have security vulnerabilities. Most popular plugins are closed source. See [Whonix Security in real world](https://sourceforge.net/p/whonix/wiki/Security%20in%20Real%20World/).*"</font>

Although it's not recommend, we don't want to withhold the knowledge from you how to use browser plugins.

IP leaks are not easily ^2^ possible.

The concern against browser plugins can be broken down to: 
1. Linkability: browser plugins use can be probably ^3^ correlated to the same [pseudonym](https://sourceforge.net/p/whonix/wiki/DoNot/#do-not-confuse-anonymity-with-pseudonymity). 
2. Fingerprinting: browser plugins can probable leak lots of information about your (virtual) operating system (=Whonix-Workstation) 
3. Security: some plugins have a history for remote exploits. More precise: the risk for your virtual operating system to get infected by trojan horses etc. is higher.

But anyway, of course you should look for alternatives first (see below), but if you must use browser plugins, an isolating/transparent proxy like Whonix is probable your best bet. ^3^

# Avoiding browser plugins #
Avoiding browser plugins and flash is better than using them.

Note, that there are alternatives to browser plugins. Most of the workarounds aren't a 100% complete, perfect drop in replacement, but perhaps it works sufficient for you (for example, if you only need youtube). Alternatives are html5, gnash, flash video replacer, flash video download or using a flash video download and convert online service. There are also applications worth checking, such as youtuberipper, ClipGrab, minitube, Totem with totem-plugins-extra, etc. Discussing the flash alternatives in details is beyond the scope of Whonix.

Also the Tails folks prepared a good list of Flash alternatives, see [Tails Flash support](https://tails.boum.org/todo/Flash_support).

If you still want to use browser plugins or flash, read below.

# How to use Flash - EASY #
If you want to use plugins anyway (read warning above), you can install new software ^a^ in Whonix-Workstation. Your best bet may be using the Tor Browser.

Your IP/location will still be hidden. Consider the plugin usage *[pseudonymous rather than anonymous](https://sourceforge.net/p/whonix/wiki/DoNot/#do-not-confuse-anonymity-with-pseudonymity)*. This is the EASY chapter, which does not include all security considerations. For those, read the whole page.

If you are using any plugins such as Flash, it will be probable known to the exit node, exit node's ISP and website, that you are a Whonix user. ^4^ ^5^ ^6^

(1) Install Flash.

    ## Due to a bug in Whonix wget uwt wrapper,
    ## we have to disable it while installing Adobe Flash.
    ##
    ## This issue will most likely be gone, if
    ## "add stream isolation support to torsocks"
    ## gets implemented.
    ## https://trac.torproject.org/projects/tor/ticket/8053
    sudo chmod -x /usr/local/bin/wget
    sudo apt-get install flashplugin-nonfree
    sudo chmod +x /usr/local/bin/wget

(2) Additionally, it might make sense to install Firefox (Tor Browser) Add-On [BetterPrivacy](https://addons.mozilla.org/en-US/firefox/addon/betterprivacy/), which can be setup to delete Flash Cookies.

(3) Activate browser plugins in Tor Browser.

To activate browser plugins in Tor Browser ^b^ right click on Tor Button -> Preferences... -> Security Settings -> uncheck: Disable Plugins during Tor usage. You have to restart Tor Browser.

(4) Updating Flash

Each time there is a new version of flash, you should update.

    ## Due to a bug in Whonix wget uwt wrapper,
    ## we have to disable it while installing Adobe Flash.
    ##
    ## This issue will most likely be gone, if
    ## "add stream isolation support to torsocks"
    ## gets implemented.
    ## https://trac.torproject.org/projects/tor/ticket/8053
    sudo chmod -x /usr/local/bin/wget 
    sudo update-flashplugin-nonfree --install --verbose
    sudo chmod +x /usr/local/bin/wget 

# How to use other browser plugins #
Note, that Tor Browser developers added a patch ^c^, which blocks all plugins except flash. To use other plugins, read the more advanced guide below.

^b^ Note, that Tor Button in Tor Browser disables all plugins by the default settings. That decision is made by the Tor Browser developers, not by the Whonix developers. (Of course, the Whonix developers second their decision.)
^c^ https://gitweb.torproject.org/torbrowser.git/blob/maint-2.2:/src/current-patches/firefox/0005-Block-all-plugins-except-flash.patch

# How to use browser plugins - Advanced #
If you don't like to use Tor Browser, you could install the mainstream Firefox, Chromium, Flash etc. For a discussion whether this is good or bad for anonymity, see the "More Security" section below.

Firefox.

    ## In Debian, Firefox is called Iceweasel.
    sudo apt-get install iceweasel

Or Chromium.

    sudo apt-get install chromium-browser chromium-browser-l10n

# How to use browser plugins - More Security #
## Read the EASY chapter above first ##
Read the EASY chapter above first

## Deactivate unneeded browser plugins ##
It's recommend to activate only plugins, you really use. On most browsers their is a pseudo URL 'about:plugins' to check which are activated. Go to Tor Browser -> Tools -> Plugins and deactivate all plugins, which you don't need, or even better, uninstall them.

## Separate Tor Browser or Separate Whonix-Workstation dedicated to browser plugins ##
For best security use [More than one Tor Browser behind an transparent or isolating proxy](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO/WebBrowsers#TorBrowserbehindatransparentorisolatingproxy) or even better, [multiple VM snapshots](https://sourceforge.net/p/whonix/wiki/Security%20Guide/#recommendation-to-use-multiple-vm-snapshots) or [multiple Whonix-Workstations](https://sourceforge.net/p/whonix/wiki/Multiple%20Whonix-Workstations/).

## SocksPort vs TransPort ##
Using the easy instructions above will cause Tor Browser to go through SocksPort and browser plugins such as Flash to go through TransPort. It may or or not make sense to either force both through a SocksPort (difficult) or to force both through the TransPort, see footnotes ^4^ ^5^ ^6^.

## Download Flash directly from Adobe ##
For [better security](http://lists.debian.org/debian-security/2012/12/msg00025.html) or if Flash from the Debian repository does not work for you, Flash can be downloaded directly form Adobe.

(1) Go to https://get.adobe.com/flashplayer/otherversions/

(2) choose Linux (32-bit)

(3) choose 11.2 for other Linux (.tar.gz) 32-bit

(4) click on the Download now button

(5) you will see

    An external application is needed to handle:

    https://fpdownload.macromedia.com/get/flashplayer/pdc/11.2.202.270/install_flash_player_11_linux.i386.tar.gz

    [...]

Verify, that you'll download from http**s**.

(6) Download.

(7) Unpack.

(8) Follow the Installation instructions in the readme.txt.

## General Whonix Install Advice #
^a^ Read [Software Installation on Whonix-Workstation](https://sourceforge.net/p/whonix/wiki/Install%20Software/)

# Footnotes #
^2^ Read [Attack on Whonix](https://sourceforge.net/p/whonix/wiki/Comparison%20with%20Others/#attacks) and/or [Design] for details on how much effort would be needed. 

^3^ For an overview about Flash Tracking Techniques and why Whonix users are much better off than users who run Tor and proxifiers and/or custom firewall rules, see chapter [Flash / Browser Plugin Security](https://sourceforge.net/p/whonix/wiki/Comparison%20with%20Others/#flash-browser-plugin-security),

^4^ Most "plugins over Tor" users probable use Mozilla Firefox and Flash on Microsoft Windows with a socksifier. They can be easily browser fingerprinted and probable even linked, see [TorifyHOWTO/WebBrowsers](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO/WebBrowsers) and [Tor Button FAQ](https://www.torproject.org/torbutton/torbutton-faq.html.en#oldtorbutton).

^5^ That is because very few people use Tor Browser with plugins, which are routed through Tor. Also because Tor Browser was at Whonix build time manually configured to use a Tor's SocksPort (for stream isolation), while user-installed plugins will will be automatically routed Tor's TransPort. The SocksPort and the TransPort will go through different circuits and most times through different exit nodes. That probable differs from the rest of the "Plugins over Tor" users group. For demonstration, see [Whonix Flash Leak Test Screenshot SocksPort and TransPort](https://sourceforge.net/projects/whonix/screenshots/flash_leak_test.png), you'll see, that the Tor Browser and Flash have different Tor exit IP's. It's questionable if that particular difference could and should be fixed and if situation had improved afterwards. ^6^

^6^ It is currently not easily possible to use Tor Browser through Tor's TransPort, see Tor Browser upstream bugs: [broken "Transparent Torification (Requires custom transproxy or Tor router)"](https://trac.torproject.org/projects/tor/ticket/6566) and [Support Tor Router/Transtor mode in Tor Browser](https://trac.torproject.org/projects/tor/ticket/6254). In */etc/environment* you could comment out

    #TOR_SOCKS_HOST="192.168.0.10"
    #TOR_SOCKS_PORT="9100"

And comment in.

    TOR_TRANSPROXY=1

And reboot.

Or add 

    export TOR_TRANSPROXY=1

to the top of the startup script *start-tor-browser*. Then both, Tor Browser and plugins would go through Tor's TransPort. This has been tested by adrelanos, see screenshot [Flash leak test both TransPort](http://whonix.sourceforge.net/screenshots/flash_leak_test_both_transport.png). The question would be, if that would actually improve the situation talked about in footnotes ^4^ and ^5^. There are probable only a very few using Tor Browser and plugins through the same circuit. (In footnote ^4^ it was mentioned, that they are still using Mozilla Firefox, even though that's even more discouraged.)

# Deprecated #
**You can skip this chapter. It's no longer of use, because if you use BetterPrivacy as recommend above, you won't need this.**

**Restrict Flash Settings**

Flash applications can set cookies, so-called Local Shared Objects (LSO), independently of the browser's settings. These cookies are able to save data up to 100 Kb. Usually, they save settings but they may be used to track surfers as well.

In order to manage the settings of your Adobe Flash Player, Macromedia offers a [Flash application](http://www.macromedia.com/support/documentation/en/flashplayer/help/settings_manager.html) on its website. There you may e.g. configure the rules concerning the data storage and the rights for using camera and microphone. The settings are spread over several flash applications. Deactivate all funcions that allow sharing and saving of data. The storage of LSOs may be deactivated on the [Global Storage Settings panel](http://www.macromedia.com/support/documentation/en/flashplayer/help/settings_manager03.html).

<font size="-3">
Hint: Only in case you previously deactivated JavaScript: You must have Javascript enabled for adobe.com and macromedia.com temporary to run the Flash application.
</font>

![flash1](http://whonix.sourceforge.net/screenshots/flash1.png)

Furthermore, the cookies already saved have to be deleted. This functionality may be found on the [Website Storage Settings panel](http://www.macromedia.com/support/documentation/en/flashplayer/help/settings_manager07.html).

![flash2](http://whonix.sourceforge.net/screenshots/flash2.png)

<font size="-3">
Personal side note: you see how ridiculous that plugin is, if the usage of the Flash settings manager depends on their website being reachable.
</font>

# License #
Thanks to [JonDos](https://anonymous-proxy-servers.net/) ([Permission](https://anonymous-proxy-servers.net/forum/viewtopic.php?p=31220&sid=ac8a6ca16eb768b3322be30b20375c97#p31220)). The "Restrict Flash Settings" chapter of the Whonix BrowserPlugins wiki page contains content from the JonDonym documentation [How to anonymize Flash videos and applets](https://anonymous-proxy-servers.net/en/help/flash-applets.html) page.

# Footer #
[[include ref=WikiFooter]]