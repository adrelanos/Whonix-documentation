[[include ref=WikiHeader]]

[TOC]

# Change the User Interface Language #
## Introduction ##
Because Whonix is nothing special and based on Debian GNU/Linux and KDE, you are free to change the system language. The technical steps are the same. You could also refer to Debian or KDE upstream documentation. If you are happy with the default English, you do not have to do anything.

## Tor Browser ##
### Method 1 ###
**Whonix-Workstation ONLY!**

(1) Start Tor Browser.

(2) Find out which ESR Firefox version Tor Browser is using.

    Tor Browser -> Help -> About Tor Browser

Should be something like *10.0.11*.

(3) Install a language pack.

Go to [http://download-origin.cdn.mozilla.net/pub/mozilla.org/firefox/releases/**10.0.11**esr/linux-i686/xpi/](http://download-origin.cdn.mozilla.net/pub/mozilla.org/firefox/releases/10.0.11esr/linux-i686/xpi/). You may need to change the **bold** part of that link depending on which ESR Firefox version Tor Browser is using!

(4) Restart Tor Browser.

(5) Done.

### Method 2 ###
**Whonix-Workstation ONLY!**

**Please TEST and leave feedback.**

(1) Update the package lists.

    sudo apt-get update

(2) Search for available language packs.

    apt-cache search iceweasel-l10n-

(3) Install a language pack.

    ## Example, replace the -ar with your language!
    sudo apt-get install iceweasel-l10n-ar

(4) Change setting in Tor Browser.

    sudo find /usr/lib/iceweasel/extensions -maxdepth 1 -name 'langpack*.xpi' -exec ln -s '{}' /home/user/tor-browser_en-US/Data/profile/extensions/ ';'

## System ##
### All Languages ###
**Whonix-Workstation ONLY!**

(1) Open konsole

    Start menu -> Applications -> System -> Terminal.

(2) Update the package lists.

    sudo apt-get update

(3) Search for available language packs.

    apt-cache search kde-i18n 

Or [search the Debian package archive](http://packages.debian.org/search?keywords=kde-l10n&searchon=names&suite=stable&section=all).

(4) Install a language pack.

    ## Example, replace the -ar with your language!
    sudo apt-get install kde-l10n-ar

(5) Change setting in KDE.

    Start menu -> Applications -> System -> System Settings -> Locale -> Languages -> Change Language

### Korean ###
User contributed instructions originally posted in [Whonix Forum - Korean language support](https://sourceforge.net/p/whonix/discussion/general/thread/fff34595/) by Anonymous. You can also use that thread for support questions.

(1) Open konsole

    Start menu -> Applications -> System -> Terminal.

(2) Update the package list.

    sudo apt-get update

(3) View available language packs.

    apt-cache search kde-i18n

(4) Install Korean language pack.

    sudo apt-get install kde-l10n-ko

(5) Install Korean fonts.

    sudo apt-get install ttf-unfonts-core ttf-unfont-extra

(6) Open system settings and set eungulim as kde's font.

(7) Open konsole and

    sudo dpkg-reconfigure locales

(8) Set "*ko KR.UTF-8 UTF-8*" as Default locale.

(9) Install nabi.

    apt-get install nabi

(10) Restart your Whonix-Workstation and start nabi.

(11) Done. You can write and read Korean now.

# Footer #
[[include ref=WikiFooter]]