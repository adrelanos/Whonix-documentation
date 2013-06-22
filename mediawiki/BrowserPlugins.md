[[include ref=WikiHeader]]

[TOC]

= Introduction =

We explain the risks of browser plugins (flash etc.), discuss some alternatives and finally explain how to use browser plugins anyway in the best possible secure manner.

= Tor Browser =

For information about Tor Browser in general, see [https://sourceforge.net/p/whonix/wiki/TorBrowser/ Tor Browser].

= Warning not to use them =

Quoted the Whonix [Features] page: &quot;''Java / JavaScript / flash / browser plugins / [https://en.wikipedia.org/wiki/Malware Malware] / misconfigured applications cannot leak your real external IP.''&quot; <font size="-3">&quot;''This is still not recommended as they may decrease anonymity (e.g. flash cookies) and often have security vulnerabilities. Most popular plugins are closed source. See [https://sourceforge.net/p/whonix/wiki/Security%20in%20Real%20World/ Whonix Security in real world].''&quot;</font>

Although it's not recommend, we don't want to withhold the knowledge from you how to use browser plugins.

IP leaks are not easily <sup>2</sup> possible.

The concern against browser plugins can be broken down to: 1. Linkability: browser plugins use can be probably <sup>3</sup> correlated to the same [https://sourceforge.net/p/whonix/wiki/DoNot/#do-not-confuse-anonymity-with-pseudonymity pseudonym]. 2. Fingerprinting: browser plugins can probable leak lots of information about your (virtual) operating system (=Whonix-Workstation) 3. Security: some plugins have a history for remote exploits. More precise: the risk for your virtual operating system to get infected by trojan horses etc. is higher.

But anyway, of course you should look for alternatives first (see below), but if you must use browser plugins, an isolating/transparent proxy like Whonix is probable your best bet. <sup>3</sup>

= Avoiding browser plugins =

Avoiding browser plugins and flash is better than using them.

Note, that there are alternatives to browser plugins. Most of the workarounds aren't a 100% complete, perfect drop in replacement, but perhaps it works sufficient for you (for example, if you only need youtube). Alternatives are html5, gnash, flash video replacer, flash video download or using a flash video download and convert online service. There are also applications worth checking, such as youtuberipper, ClipGrab, minitube, Totem with totem-plugins-extra, etc. Discussing the flash alternatives in details is beyond the scope of Whonix.

Also the Tails folks prepared a good list of Flash alternatives, see [https://tails.boum.org/todo/Flash_support Tails Flash support].

If you still want to use browser plugins or flash, read below.

= How to use Flash - EASY =

If you want to use plugins anyway (read warning above), you can install new software <sup>a</sup> in Whonix-Workstation. Your best bet may be using the Tor Browser.

Your IP/location will still be hidden. Consider the plugin usage ''[https://sourceforge.net/p/whonix/wiki/DoNot/#do-not-confuse-anonymity-with-pseudonymity pseudonymous rather than anonymous]''. This is the EASY chapter, which does not include all security considerations. For those, read the whole page.

If you are using any plugins such as Flash, it will be probable known to the exit node, exit node's ISP and website, that you are a Whonix user. <sup>4</sup> <sup>5</sup> <sup>6</sup>

<ol style="list-style-type: decimal;">
<li><p>Install Flash.</p>
== Due to a bug in Whonix wget uwt wrapper, ==

== we have to disable it while installing Adobe Flash. ==

==  ==

== This issue will most likely be gone, if ==

== &quot;add stream isolation support to torsocks&quot; ==

== gets implemented. ==

== https://trac.torproject.org/projects/tor/ticket/8053 ==

<p>sudo chmod -x /usr/local/bin/wget sudo apt-get install flashplugin-nonfree sudo chmod +x /usr/local/bin/wget</p></li>
<li><p>Additionally, it might make sense to install Firefox (Tor Browser) Add-On [https://addons.mozilla.org/en-US/firefox/addon/betterprivacy/ BetterPrivacy], which can be setup to delete Flash Cookies.</p></li>
<li><p>Activate browser plugins in Tor Browser.</p></li></ol>

To activate browser plugins in Tor Browser <sup>b</sup> right click on Tor Button -&gt; Preferences... -&gt; Security Settings -&gt; uncheck: Disable Plugins during Tor usage. You have to restart Tor Browser.

<ol start="4" style="list-style-type: decimal;">
<li>Updating Flash</li></ol>

Each time there is a new version of flash, you should update.

<pre>## Due to a bug in Whonix wget uwt wrapper,
## we have to disable it while installing Adobe Flash.
##
## This issue will most likely be gone, if
## &quot;add stream isolation support to torsocks&quot;
## gets implemented.
## https://trac.torproject.org/projects/tor/ticket/8053
sudo chmod -x /usr/local/bin/wget 
sudo update-flashplugin-nonfree --install --verbose
sudo chmod +x /usr/local/bin/wget </pre>
= How to use other browser plugins =

Note, that Tor Browser developers added a patch <sup>c</sup>, which blocks all plugins except flash. To use other plugins, read the more advanced guide below.

<sup>b</sup> Note, that Tor Button in Tor Browser disables all plugins by the default settings. That decision is made by the Tor Browser developers, not by the Whonix developers. (Of course, the Whonix developers second their decision.) <sup>c</sup> https://gitweb.torproject.org/torbrowser.git/blob/maint-2.2:/src/current-patches/firefox/0005-Block-all-plugins-except-flash.patch

= How to use browser plugins - Advanced =

If you don't like to use Tor Browser, you could install the mainstream Firefox, Chromium, Flash etc. For a discussion whether this is good or bad for anonymity, see the &quot;More Security&quot; section below.

Firefox.

<pre>## In Debian, Firefox is called Iceweasel.
sudo apt-get install iceweasel</pre>
Or Chromium.

<pre>sudo apt-get install chromium-browser chromium-browser-l10n</pre>
= How to use browser plugins - More Security =

== Read the EASY chapter above first ==

Read the EASY chapter above first

== Deactivate unneeded browser plugins ==

It's recommend to activate only plugins, you really use. On most browsers their is a pseudo URL 'about:plugins' to check which are activated. Go to Tor Browser -&gt; Tools -&gt; Plugins and deactivate all plugins, which you don't need, or even better, uninstall them.

== Separate Tor Browser or Separate Whonix-Workstation dedicated to browser plugins ==

For best security use [https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO/WebBrowsers#TorBrowserbehindatransparentorisolatingproxy More than one Tor Browser behind an transparent or isolating proxy] or even better, [https://sourceforge.net/p/whonix/wiki/Security%20Guide/#recommendation-to-use-multiple-vm-snapshots multiple VM snapshots] or [https://sourceforge.net/p/whonix/wiki/Multiple%20Whonix-Workstations/ multiple Whonix-Workstations].

== SocksPort vs TransPort ==

Using the easy instructions above will cause Tor Browser to go through SocksPort and browser plugins such as Flash to go through TransPort. It may or or not make sense to either force both through a SocksPort (difficult) or to force both through the TransPort, see footnotes <sup>4</sup> <sup>5</sup> <sup>6</sup>.

== Download Flash directly from Adobe ==

For [http://lists.debian.org/debian-security/2012/12/msg00025.html better security] or if Flash from the Debian repository does not work for you, Flash can be downloaded directly form Adobe.

<ol style="list-style-type: decimal;">
<li><p>Go to https://get.adobe.com/flashplayer/otherversions/</p></li>
<li><p>choose Linux (32-bit)</p></li>
<li><p>choose 11.2 for other Linux (.tar.gz) 32-bit</p></li>
<li><p>click on the Download now button</p></li>
<li><p>you will see</p>
<p>An external application is needed to handle:</p>
<p>https://fpdownload.macromedia.com/get/flashplayer/pdc/11.2.202.270/install_flash_player_11_linux.i386.tar.gz</p>
<p>[...]</p></li></ol>

Verify, that you'll download from http'''s'''.

<ol start="6" style="list-style-type: decimal;">
<li><p>Download.</p></li>
<li><p>Unpack.</p></li>
<li><p>Follow the Installation instructions in the readme.txt.</p></li></ol>

== General Whonix Install Advice ==

<sup>a</sup> Read [https://sourceforge.net/p/whonix/wiki/Install%20Software/ Software Installation on Whonix-Workstation]

= Footnotes =

<sup>2</sup> Read [https://sourceforge.net/p/whonix/wiki/Comparison%20with%20Others/#attacks Attack on Whonix] and/or [Design] for details on how much effort would be needed.

<sup>3</sup> For an overview about Flash Tracking Techniques and why Whonix users are much better off than users who run Tor and proxifiers and/or custom firewall rules, see chapter [https://sourceforge.net/p/whonix/wiki/Comparison%20with%20Others/#flash-browser-plugin-security Flash / Browser Plugin Security],

<sup>4</sup> Most &quot;plugins over Tor&quot; users probable use Mozilla Firefox and Flash on Microsoft Windows with a socksifier. They can be easily browser fingerprinted and probable even linked, see [https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO/WebBrowsers TorifyHOWTO/WebBrowsers] and [https://www.torproject.org/torbutton/torbutton-faq.html.en#oldtorbutton Tor Button FAQ].

<sup>5</sup> That is because very few people use Tor Browser with plugins, which are routed through Tor. Also because Tor Browser was at Whonix build time manually configured to use a Tor's SocksPort (for stream isolation), while user-installed plugins will will be automatically routed Tor's TransPort. The SocksPort and the TransPort will go through different circuits and most times through different exit nodes. That probable differs from the rest of the &quot;Plugins over Tor&quot; users group. For demonstration, see [https://sourceforge.net/projects/whonix/screenshots/flash_leak_test.png Whonix Flash Leak Test Screenshot SocksPort and TransPort], you'll see, that the Tor Browser and Flash have different Tor exit IP's. It's questionable if that particular difference could and should be fixed and if situation had improved afterwards. <sup>6</sup>

<sup>6</sup> It is currently not easily possible to use Tor Browser through Tor's TransPort, see Tor Browser upstream bugs: [https://trac.torproject.org/projects/tor/ticket/6566 broken &quot;Transparent Torification (Requires custom transproxy or Tor router)&quot;] and [https://trac.torproject.org/projects/tor/ticket/6254 Support Tor Router/Transtor mode in Tor Browser]. In ''/etc/environment'' you could comment out

<pre>#TOR_SOCKS_HOST=&quot;192.168.0.10&quot;
#TOR_SOCKS_PORT=&quot;9100&quot;</pre>
And comment in.

<pre>TOR_TRANSPROXY=1</pre>
And reboot.

Or add

<pre>export TOR_TRANSPROXY=1</pre>
to the top of the startup script ''start-tor-browser''. Then both, Tor Browser and plugins would go through Tor's TransPort. This has been tested by adrelanos, see screenshot [http://whonix.sourceforge.net/screenshots/flash_leak_test_both_transport.png Flash leak test both TransPort]. The question would be, if that would actually improve the situation talked about in footnotes <sup>4</sup> and <sup>5</sup>. There are probable only a very few using Tor Browser and plugins through the same circuit. (In footnote <sup>4</sup> it was mentioned, that they are still using Mozilla Firefox, even though that's even more discouraged.)

= Deprecated =

'''You can skip this chapter. It's no longer of use, because if you use BetterPrivacy as recommend above, you won't need this.'''

'''Restrict Flash Settings'''

Flash applications can set cookies, so-called Local Shared Objects (LSO), independently of the browser's settings. These cookies are able to save data up to 100 Kb. Usually, they save settings but they may be used to track surfers as well.

In order to manage the settings of your Adobe Flash Player, Macromedia offers a [http://www.macromedia.com/support/documentation/en/flashplayer/help/settings_manager.html Flash application] on its website. There you may e.g. configure the rules concerning the data storage and the rights for using camera and microphone. The settings are spread over several flash applications. Deactivate all funcions that allow sharing and saving of data. The storage of LSOs may be deactivated on the [http://www.macromedia.com/support/documentation/en/flashplayer/help/settings_manager03.html Global Storage Settings panel].

<font size="-3"> Hint: Only in case you previously deactivated JavaScript: You must have Javascript enabled for adobe.com and macromedia.com temporary to run the Flash application. </font>

[[Image:http://whonix.sourceforge.net/screenshots/flash1.png|frame|none|alt=|caption flash1]]

Furthermore, the cookies already saved have to be deleted. This functionality may be found on the [http://www.macromedia.com/support/documentation/en/flashplayer/help/settings_manager07.html Website Storage Settings panel].

[[Image:http://whonix.sourceforge.net/screenshots/flash2.png|frame|none|alt=|caption flash2]]

<font size="-3"> Personal side note: you see how ridiculous that plugin is, if the usage of the Flash settings manager depends on their website being reachable. </font>

= License =

Thanks to [https://anonymous-proxy-servers.net/ JonDos] ([https://anonymous-proxy-servers.net/forum/viewtopic.php?p=31220&sid=ac8a6ca16eb768b3322be30b20375c97#p31220 Permission]). The &quot;Restrict Flash Settings&quot; chapter of the Whonix BrowserPlugins wiki page contains content from the JonDonym documentation [https://anonymous-proxy-servers.net/en/help/flash-applets.html How to anonymize Flash videos and applets] page.

= Footer =

[[include ref=WikiFooter]]

