[[include ref=WikiHeader]]

[TOC]

= XChat / IRC =

== Introduction ==

[http://xchat.org/ XChat] in Whonix has been hardened according to [https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO/XChat TorifyHOWTO/XChat]. All servers, beside the secure (SSL) version of OFTC have been removed. You are encouraged to add the secure version of your IRC server. (Preferably a hidden service, SSL as a fallback or at best, both.) See also [https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO/XChat TorifyHOWTO/XChat].

On OFTC is the official #Tor. Note, that no Whonix developers hang out there! Upstream Tor developers do not support Whonix. For contacting Whonix developers, see [https://sourceforge.net/p/whonix/wiki/Contact/ Contacting Whonix developers / Feedback / Questions].

== How to start XChat ==

Start menu -&gt; Applications -&gt; Internet -&gt; XChat IRC

== Reset your XChat idenity ==

If you want to reset your XChat identity, run ''xchat-reset''. WARNING: this will kill XChat, delete all your settings, scripts and logs and creates a fresh XChat identity.

<pre>xchat-reset</pre>
== SASL ==

=== Whonix 0.5.6 (released) ===

Some networks, some hidden IRC servers, such as freenode, require SASL to connect to them.

All XChat plugins have been deactivated (hardening) and moved to /usr/lib/xchat/plugins.disabled. If you really need a plugin, such as perl for SASL, you can use the example below.

<pre>sudo mv /usr/lib/xchat/plugins.disabled/perl.so /usr/lib/xchat/plugins/</pre>
Setting up SASL is outside the scope of this document, have a look into [https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO/XChat TorifyHOWTO/XChat].

=== Whonix 0.6.2 and above (in development) ===

All XChat plugins have been deactivated (hardening) and deactivated using dpkg-divert. To re-enable them, use one of the following commands depending on which plugin you need.

<pre>sudo dpkg-divert --rename --remove /usr/lib/xchat/plugins/python.so
sudo dpkg-divert --rename --remove /usr/lib/xchat/plugins/tcl.so
sudo dpkg-divert --rename --remove /usr/lib/xchat/plugins/perl.so</pre>
= IRC General =

The [https://en.wikipedia.org/wiki/Ident Ident Protocol] is automatically blocked because Whonix-Workstation is firewalled.

The [https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO/IrcSilc TorifyHOWTO/IrcSilc] contains general IRC safety techniques and other tips.

= Footer =

[[include ref=WikiFooter]]

