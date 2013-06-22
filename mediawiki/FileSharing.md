[[include ref=WikiHeader]]

[TOC]

= File Sharing =

== Please don't! ==

Even though p2p over Whonix is anonymous it is still discouraged. It's slow. Tor is not really designed for it and file sharing through Tor puts excessive load on nodes because it opens hundreds of new circuits. Don't be a lame, the exit node admins get the trouble and may shut their node, at our all cost.

Source: [https://blog.torproject.org/blog/bittorrent-over-tor-isnt-good-idea The Tor Project Blog: Bittorrent over Tor isn't a good idea.]

== Alternative ==

In many locations and in many places a VPN is safe enough for sharing software, which is not supposed to be shared. You are discouraged to violate laws.

== Limited Damage Control ==

If you decided to be lame and using Tor for file sharing, please add a VPN behind Tor, i.e. Tor -&gt; VPN -&gt; filesharing network. This will at least protect the Tor exit nodes from abuse complaints and may result in faster download speed as well. (Because of [https://sourceforge.net/p/whonix/wiki/TunnelUDPoverTor/ Tunnel UDP over Tor]) See [https://sourceforge.net/p/whonix/wiki/Tunnel_Proxy_or_SSH_or_VPN_through_Tor/ Tunnel Proxy/SSH/VPN through Tor (Tor -&gt; Proxy/SSH/VPN)].

You already decided to leech from the Tor network. Please also consider leeching from the file sharing network. 1. Disable uploading/sharing: this reduces load form the Tor network and may also result in faster download speeds. 2. Or lower upload rate to the absolute minimum required. 3. Remove the files/torrent file form your shared folder after finishing downloading: this ensures the file gets no longer shared.

== Updates ==

Quote [https://lists.torproject.org/pipermail/tor-talk/2011-December/022376.html Jacob Appelbaum]:

<blockquote>''[...] I'm not clear that it will harm the network if Tails includes a BitTorrent client. I think that the harm comes when someone runs a few seeding boxes through Tor and doesn't bother to add any capacity to the network at all. [...]''
</blockquote>
Quote [https://lists.torproject.org/pipermail/tor-talk/2011-December/022369.html Andrew Lewman says]:

<blockquote>''[...] There are completely legitimate uses of bittorrent over Tor. I've talked to people who want to get their ISO of Fedora or Ubuntu from outside their country, so they bt over tor to do so. [...] I'm fully aware that the tor codebase punishes me for doing large downloads over Tor, so be it. [...]''
</blockquote>
Quote: [https://blog.torproject.org/blog/bittorrent-over-tor-isnt-good-idea Roger Dingledine]:

<blockquote>''[...] We've been saying for years not to run Bittorrent over Tor, because the Tor network [https://blog.torproject.org/blog/why-tor-is-slow can't handle the load]; [...]''
</blockquote>
[http://sourceforge.net/mailarchive/forum.php?thread_name=41dcd1d6b4a3635860722f7c74bf5f51%40mail.cs.umu.se&forum_name=libtorrent-discuss libtorrent - socks proxy obedience]

= Footer =

[[include ref=WikiFooter]]

