[[include ref=WikiHeader]]

[TOC]

= Proxy Settings =

Setting GNOME 3 application wide proxy for improved [Stream Isolation] so far failed. Some notes.

<pre>## install tools
apt-get install gconf2

## sources:
## https://developer.gnome.org/ProxyConfiguration/

## gsettings as root
## thanks to http://stackoverflow.com/questions/10374520/gsettings-with-cron
## not sure if using gsettings as root means system wide here
sessionfile=`find &quot;${HOME}/.dbus/session-bus/&quot; -type f`
export `grep &quot;DBUS_SESSION_BUS_ADDRESS&quot; &quot;${sessionfile}&quot; | sed '/^#/d'`

## list proxy settings
gsettings list-recursively org.gnome.system.proxy

## set socks proxy settings
gsettings set org.gnome.system.proxy.socks host &quot;192.168.0.10&quot;
gsettings set org.gnome.system.proxy.socks port &quot;9159&quot;</pre>
= Footer =

[[include ref=WikiFooter]]

