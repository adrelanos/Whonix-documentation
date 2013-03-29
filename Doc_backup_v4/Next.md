**Documentation for the NEXT Whonix version! ONLY for developers! No gurantee it really makes into the next Whonix version.**

# TOC #
[TOC]

# Tor Browser #
Available languages as in October 2012:

    ar
    de
    en-US
    es-ES
    fa
    fr
    it
    ko
    nl
    pl
    pt-PT
    ru
    vi
    zh-CN

To check if further languages are supported visit https://www.torproject.org/dist/torbrowser/linux/ or http://idnxcnkne4qt76tg.onion/dist/torbrowser/linux/.

Always use.

    export TB_LANG="<language code>"

to set the language before running the Tor Browser Updater.

For example, for Vietnamese use:

    export TB_LANG="vi"

Replace "vi" with "zh-CN" for Chinese
and so on.

# DNS on Whonix-Gateway #
Working.

Explanation http://sourceforge.net/p/whonix/discussion/general/thread/41116dda/

    sudo chattr -i /etc/resolv.conf
    sudo rm /etc/resolv.conf
    sudo service networking restart
    sudo su clearnet
    ping google.com
    # working


# Remove Proxy Settings #
Open *start-tor-browser* in the root of the Tor Browser folder and add right below *#!/bin/sh*. ^1^ ^2^ ^3^ ^4^

    unset TOR_SOCKS_HOST
    unset TOR_SOCKS_PORT

Now you could use Tor Button's settings dialog to set it to any other proxy.

Alternatively, if you want to set it to no proxy, you could additionally add below "*unset TOR_SOCKS_PORT*".

    export TOR_TRANSPROXY=1

# Footer #
[[include ref=WikiFooter]]