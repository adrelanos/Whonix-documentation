[[include ref=WikiHeader]]

[TOC]

# Whonixcheck #
*whonixcheck* ([on github](https://github.com/adrelanos/Whonix/blob/stable/whonix_shared/usr/local/bin/whonixcheck)) is a a bash script, checking many important things. Supports to be run in console and also has a grapical progress meter and graphical info popup for the results. It's stored in */usr/local/bin/whonixcheck*. Whonix will also work without that script. Nothing is compiled, it's just a script and anyone can read the source code.

Screenshots:

 * gui: http://whonix.sourceforge.net/screenshots/whonixcheck_gui.png
 * progress: http://whonix.sourceforge.net/screenshots/whonixcheck_progress.png
 * cli: http://whonix.sourceforge.net/screenshots/whonixcheck_cli.png

Whonixcheck checks:

* Status of Network Time Synchronization
    * see above
    * Only the status of the logfiles is read, there is no actual network traffic, that is done before.
 * Tor connection
    * downloads https://check.torproject.org with curl through extra SocksPort
    * downloads https://check.torproject.org with wget through TransPort
 * Tor Browser version
    * downloads https://check.torproject.org/RecommendedTBBVersions with curl through extra SocksPort
 * operating system updates
    * Run *apt-get update* through apt-get SocksPort and inform about the system being up to date or requiring updates.
 * Whonix version and Whonix news
    * Downloads http://whonix.sourceforge.net/whonix_news.asc with curl through extra whonix news SocksPort.
    * Is supposed to reflect most important news for people not even following Whonix Important Blog. In theory, if an IP leak in Whonix where found or exit nodes activly exploiting apt-get traffic, this would be used to briefly inform users about the danger.
    * [Whonix News Format](https://sourceforge.net/p/whonix/wiki/Dev_news/)
    * Whonix version and news file must be signed by Whonix developer adrelanos.
    * Adrelanos gpg key got copied to /usr/share/whonix/adrelanos.asc at build time.
    * Warns if the file can not be gpg verified with adrelanos gpg key. In that case version and news is ignored.
    * Also see [Trust].
    * An adversary with (temporary) control over the sourceforge.net server could replace that file with any other message ever signed by adrelanos. There is no defense against this attack, but a defense wouldn't be useful anyway. ^1^

The whonixcheck script was inspired by (and uses for a part of the checks) check.torproject.org. In past when people were still recommended to use proxy settings to torify webbrowsers, it was an important check. While manual torification of webbrowsers is nowadays recommend against, the Tor Browser Bundle, which is securely pre-configured, still visits check.tpo and checks if everything is okay. Check.tpo also checks if the Tor Browser Bundle version is up to date (technically Tor Button downloads version information and checks locally).

While check.tpo just checks the browser, Whonix is more than a browser. It's a complete operating system. Therefore when the browser starts, it's already too late. It has to be checked earlier, because the user might not start the browser. That's why whonixcheck will be automatically started after boot/login.

The Whonix design ensures, that never the users real IP can be detected. Why check it anyway? Sometimes check.tpo reports false positives and fails to detect Tor exit nodes. The user should be informed about that possibility. That reduces support requests and bad press. It's still ok to investigate if the Tor exit node could not be detected, but it's very sure that the outcome will be, that it's a Tor exit node IP.

*/etc/cron.daily/* should run it once every day, even if the system is not restarted (TODO) but that feature appears to be broken and needs fixing. The motivation behind that is also to inform long running systems.

The *ca-certificates* Debian package is installed on Whonix. Curl will verify the SSL certificate and aborts if the certificate is not valid.

Attack surface for this script includes at least curl, apt-get, gpg, grep, sed, bash, uwt, torsocks, zenity, pgrep, htpdate logs. Adrelanos believes, that benefits outweigh the risks not running those checks. The user is free to *sudo chmod -x /usr/local/bin/whonixcheck* and adrelanos remains as always open for reviews and suggestions.

Also see chapter [SSL](https://sourceforge.net/p/whonix/wiki/SSL/).

<font size="-3">
^1^ An adversary in that position could run even more powerful attacks, such as malicious website news and documentation, malicious downloads ^2^ etc.
^2^ Adrelanos is sure, that not everyone will verify gpg signatures.
</font>

# 0.5.x changes #
In upcoming version 0.5.x the following things will change.

When whonixcheck gets manually run run by the user (technically, no command line option given) all checks will run same as in 0.4.x.

When run by on Whonix-Workstation by kde autostart (*home/user/.config/autostart/whonixcheck.desktop*) or by user cron (*/usr/local/bin/whonixcheck_daily*) it will run with the -autostart option.

When run with the -autostart option, whonixcheck will not perform any checks if it was recently (up to 24 hours) run already.

In other words, whonixcheck will only automatically perform checks if twenty four hours passed. When Whonix wasn't in use for a while, for example for a two days break, it will run right after boot.

Whonixcheck will also run rawdog to download Whonix Important Blog and Whonix Feature Blog using rawdog though Whonix News SocksPort.

# Footer #
[[include ref=WikiFooter]]