[[include ref=WikiHeader]]

[TOC]

= Whonix security in real world =

Some real world examples that are '''protected by using Whonix''':

* Flash and Java, although recommend against, can also not leak IP/location. See [https://sourceforge.net/p/whonix/wiki/BrowserPlugins/ Browser Plugins] for details.
* Skype, although recommend against, can also not leak IP/location. See [https://sourceforge.net/p/whonix/wiki/Voip/#skype Skype].
* BitTorrent, when using ordinary proxyfication methods, has been [https://blog.torproject.org/blog/bittorrent-over-tor-isnt-good-idea reported to protocol IP leak] ([http://www.webcitation.org/6FDaBuhHi w]). Although recommend against due to excessive traffic and therefore harming the Tor network (see [FileSharing]), can also not leak IP/location. This is because the external ISP IP address is hidden from Whonix-Workstation.
* [https://tails.boum.org/security/IP_address_leak_with_icedove/index.en.html Tails: Icedove (Thunderbird) leaks the real IP address] ([http://www.webcitation.org/6FDZcatic w]) - Whonix didn't exist at the time that bug existed. Such kinds of leaks are impossible in Whonix, since the Whonix-Workstation is unaware of it's external IP. To be fair, such kind of leaks are now much less likely in Tails, since they are no longer using transparent proxying. ([https://mailman.boum.org/pipermail/tails-dev/2012-September/001704.html source] ([http://www.webcitation.org/6FDZe0ZXS w]))
* [https://tails.boum.org/bugs/pidgin_leaks_the_real_IP/ pidgin leaks the real IP] ([http://www.webcitation.org/6FDZj1gpN w]) - Whonix didn't exist at the time that bug existed. Such kinds of leaks are not possible with Whonix, since the Whonix-Workstation is unaware of it's external IP. To be fair, it has to be noted, that this bug existed only in the development source code. They spotted the bug and fixed it before the release. ([https://mailman.boum.org/pipermail/tails-dev/2012-September/001704.html source] ([http://www.webcitation.org/6FDZe0ZXS w]))
* [https://blog.torproject.org/blog/firefox-security-bug-proxy-bypass-current-tbbs Tor Browser Bundle: Firefox security bug (proxy-bypass)] ([http://www.webcitation.org/6FDZlP2Ht w]) - This vulnerability was circumvented by Whonix. Any proxy bypass may have only emitted traffic through Tor's TransPort. All that could have been leaked is the IP address of another Tor exit node, which is harmless.
* clock skew attack ([http://www.reddit.com/r/onions/comments/10usgv/clock_skewing_a_clever_unconventional_means_of/ link]) ([http://www.webcitation.org/6FDZnhH5j w]) brief summary: The adversary gets the time of a hidden server (example: http header) and measures the skew. Then the adversary compares with Tor relays or other public reachable (web) servers. If they have the same skew, it's very likely, it's hosted on the same server. - Although recommend against to run a Tor relay/public reachable server and a hidden service on the same server (because that opens up for a lot other attacks (bandwidth, DDOS related)), Whonix 0.4.4 and above circumvent this attack. To be fair, when this attack was first described, Whonix didn't exist, but it would circumvent it now.
* [http://hal.inria.fr/inria-00574178/en/ Exploiting P2P Applications to Trace and Profile Tor Users] ([http://www.webcitation.org/6FVK6WpNu w]) - Whonix didn't exist at the time that attack was first described. This attack gets defeated by Whonix, since the Whonix-Workstation is unaware of it's external IP and because Whonix makes extensive use of [Stream Isolation].

= Footer =

[[include ref=WikiFooter]]

