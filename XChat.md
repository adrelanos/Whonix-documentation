[[include ref=WikiHeader]]

[TOC]

# XChat / IRC #
## Introduction ##
[XChat](http://xchat.org/) in Whonix has been hardened according to [TorifyHOWTO/XChat](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO/XChat). All servers, beside the secure (SSL) version of OFTC have been removed. You are encouraged to add the secure version of your IRC server. (Preferably a hidden service, SSL as a fallback or at best, both.) See also [TorifyHOWTO/XChat](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO/XChat).

On OFTC is the official #Tor. Note, that no Whonix developers hang out there! Upstream Tor developers do not support Whonix. For contacting Whonix developers, see [Contacting Whonix developers / Feedback / Questions](https://sourceforge.net/p/whonix/wiki/Contact/).

## How to start XChat ##
Start menu -> Applications -> Internet -> XChat IRC

## Reset your XChat idenity ##
If you want to reset your XChat identity, run *xchat-reset*. WARNING: this will kill XChat, delete all your settings, scripts and logs and creates a fresh XChat identity.

    xchat-reset

## SASL ##
Some networks, some hidden IRC servers, such as freenode, require SASL to connect to them.

All XChat plugins have been deactivated (hardening) and moved to /usr/lib/xchat/plugins.disabled. If you really need a plugin, such as perl for SASL, you can use the example below.

    sudo mv /usr/lib/xchat/plugins.disabled/perl.so /usr/lib/xchat/plugins/

Setting up SASL is outside the scope of this document, have a look into [TorifyHOWTO/XChat](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO/XChat).

# IRC General #
The [Ident Protocol](https://en.wikipedia.org/wiki/Ident) is automatically blocked because Whonix-Workstation is firewalled.

The [TorifyHOWTO/IrcSilc](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO/IrcSilc) contains general IRC safety techniques and other tips.

# Footer #
[[include ref=WikiFooter]]