[[include ref=WikiHeader]]

[TOC]

# Proxy Settings
Setting GNOME 3 application wide proxy for improved [Stream Isolation] so far failed. Some notes.

    ## install tools
    apt-get install gconf2

    ## sources:
    ## https://developer.gnome.org/ProxyConfiguration/

    ## gsettings as root
    ## thanks to http://stackoverflow.com/questions/10374520/gsettings-with-cron
    ## not sure if using gsettings as root means system wide here
    sessionfile=`find "${HOME}/.dbus/session-bus/" -type f`
    export `grep "DBUS_SESSION_BUS_ADDRESS" "${sessionfile}" | sed '/^#/d'`

    ## list proxy settings
    gsettings list-recursively org.gnome.system.proxy

    ## set socks proxy settings
    gsettings set org.gnome.system.proxy.socks host "192.168.0.10"
    gsettings set org.gnome.system.proxy.socks port "9159"

# Footer #
[[include ref=WikiFooter]]