[[include ref=WikiHeader]]

[TOC]

= Tunnel Proxy/SSH/VPN through Tor =

== Required Knowledge ==

=== Introduction ===

'''user -&gt; Tor -&gt; Proxy/SSH/VPN'''

Read first: [https://trac.torproject.org/projects/tor/wiki/doc/TorPlusVPN Tor Plus VPN or proxy] and [https://sourceforge.net/p/whonix/wiki/Authorship/#whonix-vpn-disclaimer Whonix VPN disclaimer].

You can tunnel through Tor first and add an additional proxy, SSH or VPN hop at the very end of that chain as your &quot;exit node&quot;. The services you connect to, will not know, that you are using Tor <sup>1</sup>. This can be useful to '''evade Tor bans''', for example, to visit websites or IRC networks who blacklisted Tor. Beware of the risks, this adds a &quot;permanent exit node&quot;, read [https://trac.torproject.org/projects/tor/wiki/doc/TorPlusVPN Tor Plus VPN or proxy].

To do that, go to your Whonix-Workstation and add the proxy, SSH or VPN normally, just like you would do, if you wouldn't use the Whonix-Gateway. Adding your proxy, SSH or VPN inside Whonix-Workstation will, thanks to Whonix-Gateway, result in them getting tunneled over Tor.

[https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO Protocol leaks] still apply, thought to a lesser extend. Leaks would ''only'' leak through Tor and you have best possible [https://sourceforge.net/p/whonix/wiki/Whonix%27s%20Protocol-Leak-Protection%20and%20Fingerprinting-Protection/ Protocol-Leak-Protection and Fingerprinting-Protection].

<font size="-3"> ,, <sup>1</sup> Unless it's a &quot;transparent proxy&quot; in sense of sending http forwarded for, covered in the [https://trac.torproject.org/projects/tor/wiki/doc/TorPlusVPN Tor Plus VPN or proxy] article. </font>

=== uwt and Tor Browser ===

There are two special cases in Whonix. Applications using uwt and Tor Browser. These are pre-configured to use Socks Proxy settings. (<font size="-3">(...and not just TransPort, which is a security feature: Stream Isolation.)</font>

You may have to disable the affected uwt wrapper, in case there is one, for the application you want to tunnel. See [https://sourceforge.net/p/whonix/wiki/Stream%20Isolation/ Stream Isolation] to learn what uwt and uwt wrappers are. For example to deactivate the uwt wrapper for wget, you could use.

<pre>sudo chmod -x /usr/local/bin/apt-get</pre>
If you want to do it with Tor Browser, you must [https://sourceforge.net/p/whonix/wiki/TorBrowser/#remove-proxy-settings Remove Proxy Settings].

=== Malware ===

Also note, that once Whonix-Workstation gets rooted by malware, the VPN/SSH/proxy can be easily circumvented by the attacker and you are left to the protections by Whonix and Tor.

=== Leaks ===

If setting up socksifier, proxy settings, transparent proxy with local redirection, SSH tunnel or a VPN in a leak free manner were easy, this means while ensuring nothing will bypass the VPN, SSH or proxy, there would have been no reason to develop Whonix in the first place.

The methods described on this page are all tested and should all more or less work. Should there be any misconfiguration or leak bug, you are left to the protections by Whonix and Tor. This means, the leak will still go through Whonix-Gateway and therefore forced through Tor. The methods on this page are not as safe as a Whonix-Gateway. There were development discussions and [https://sourceforge.net/p/whonix/wiki/Inspiration/ some progress], about chaining multiple Gateways, VPNBOX, JonDoBOX, i2pBOX, FreenetBOX and ProxyBOX, but nothing was finished to to lack of community interest, support and developers.

=== Web Browser ===

I don't know how anonymous it is to use (proxy/VPN/SSH -&gt;) Tor -&gt; Proxy/VPN/SSH -&gt; Tor Browser -&gt; website. How many people show up with a proxy, VPN or SSH IP using Tor Browser? This setup is so special that I believe only very few people are doing it. For this reason, I recommend against.

On the other hand, due to browser fingerprinting, I can't really recommend to use another browser than Tor Browser either.

== Tunnel proxy through Tor ==

'''user -&gt; Tor -&gt; proxy'''

Note, that the connection, between the Tor exit node and the proxy, is in most cases, not encrypted.

=== Proxy Settings Method ===

After understanding the ''Required Knowledge'' chapter above, using proxy settings in Whonix there is no difference from using proxy settings in an ordinary why, other than that it's running inside Whonix-Workstation.

If proxy settings are honored by application or in worst case leak through Tor alone (thanks to Whonix), is another question and not in Whonix's power, see [https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO TorifyHOWTO].

=== Proxyfier Method ===

==== General ====

After understanding the ''Required Knowledge'' chapter above, using a Proxyfier in Whonix there is no difference from using a Proxyfier in an ordinary way, other than that it's running inside Whonix-Workstation.

If the Proxifier is leak free or in worst case leaks through Tor alone (thanks to Whonix), is another question and not in Whonix's power, see [https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO TorifyHOWTO].

==== uwt ====

uwt uses torsocks. While the name implies it's Tor specific, it's not. You can point it to any socks proxy. Examples.

<pre>## For Tor stream isolation #1
uwt -t 5 -i 192.168.0.10 -p 9153 /usr/bin/wget -c https://check.torproject.org

## For Tor stream isolation #2
uwt -t 5 -i 192.168.0.10 -p 9154 /usr/bin/wget -c https://check.torproject.org

## Proxy
uwt -t 5 -i x.x.x.x -p xxxx /usr/bin/wget -c https://check.torproject.org</pre>
<font size="-3"Using the full path, i.e. /usr/bin/wget will circumvent the wget uwt wrapper.</font>

For testing, if you didn't disable the wget uwt wrapper, the following command will most likely get another IP, because still using Stream Isolation.

<pre>## Using Tor's TransPort
## (/usr/local/bin/wget uwt wrapper)
wget https://check.torproject.org</pre>
==== proxychains ====

'''WARNING''':

* I don't know how well proxychains works. For example [https://trac.torproject.org/projects/tor/wiki/doc/torsocks#WorkaroundforIPv6leakbug torsocks has a IPv6 leak bug]. I don't know if proxychains forces everything through the proxies. Whonix only ensures, should their be leaks, they go only through Tor.
* There are at least three different versions of proxychains. The old/original/unmaintained version on sourceforge.net and two forks on github. I don't know about that status of any of them and haven't heard of anyone looking if they do really work as expected. The two authors argue with each other and I wasn't motivated to understand the conflict and to determine which version is better. However, any leaks not going through the proxy(chain) will go through Tor.

Instructions:

Install proxychains.

<pre>sudo apt-get install proxychains</pre>
Note the uwt and Tor Browser notice in ''Required Knowledge'' above first. After you have done so it's quite simple.

Open proxychains configuration file.

<pre>kdesudo leafpad /etc/proxychains.conf</pre>
Go to the bottom of the settings file. Comment out &quot;''socks4 127.0.0.1 9050''&quot; and add for example &quot;''socks5 192.168.0.10 9152''&quot; (for Tor stream isolation) or &quot;''socks5 ip port''&quot; with an IP and port of your choice to set the proxy settings.

<pre>[ProxyList]
## add proxy here ...
## meanwhile
## defaults set to &quot;tor&quot;
#socks4 127.0.0.1 9050
socks5 192.168.0.10 9152
# socks5 x.x.x.x xxxx</pre>
Advanced. Recommendation: Why not use Tor stream isolation for the proxychains connection?

<pre>[ProxyList]
## add proxy here ...
## meanwhile
## defaults set to &quot;tor&quot;
#socks4 127.0.0.1 9050
socks5 192.168.0.10 9152
socks5 x.x.x.x xxxx</pre>
Safe the configuration file. Test afterwards. For example:

<pre>proxychains /usr/bin/wget https://check.torproject.org</pre>
Will do.

For testing, if you didn't disable the wget uwt wrapper, the following command will most likely get another IP. (Stream Isolation)

<pre>## Using Tor's TransPort
## (/usr/local/bin/wget uwt wrapper)
wget https://check.torproject.org</pre>
=== Transparent Proxying ===

==== Introduction ====

To make clear, what this is about. Whonix-Gateway is already servering as a Transparent Proxy <font size="-3">(anonymizing middlebox)</font>, which means, that all applications not explicitly configured <font size=-3>(by uwt socksifier or proxy settings)</font> to use a SocksPort, can connect through Tor without any settings. The Transparent Proxying chapter on the ''Tunnel Proxy/SSH/VPN through Tor'' page is about configuring Whonix-Workstation also to act as a Transparent Proxy <font size="-3">(local redirection)</font>. Use case: a user wants to ensure all traffic goes through Tor (by using Whonix-Gateway) and want to additionally ensure, all traffic goes through a proxy choosen by the user behind Tor, i.e. user -&gt; Tor -&gt; proxy.

<font size="-3">[https://trac.torproject.org/projects/tor/wiki/doc/TorBOX/OptionalConfigurations?version=129#TransparentProxying torproject.org wiki version 129] contains an old example using privoxy, JonDo and httpsdnsd. The new example uses redsocks and is simpler.</font>

You always have to keep in mind, which kind of data and which kind of proxy you are using. There are CGIproxies, http(s) proxies and socks4/4a/5 proxies.

In case you redirect the network layer directly with iptables, you need a TransPort. Unfortunately very few applications, do offer a TransPort. For example, Tor supports a TransPort. In most other cases, you need to translate the different kinds of data.

Due to the nature of Transparent Proxying, we need to redirect with iptables and end up with a &quot;Trans data stream&quot;. Because most proxies are either http or socks we need to translate this. Below we discuss a few tools which help here, not all are required, depending on what you want to do.

Required reading:

* [https://trac.torproject.org/projects/tor/wiki/doc/proxy proxy]
* [https://trac.torproject.org/projects/tor/wiki/doc/TorPlusVPN Tor Plus VPN or proxy]

===== Tools =====

Tor is a socks proxy and also has a TransPort. Unfortunately, Tor can not be directly used as a http proxy. You must also keep in mind, that Tor does not support UDP, although it offers a DnsPort..

[http://darkk.net.ru/redsocks/ redsocks] can also accept &quot;Trans data streams&quot; and can forward them to http'''s''', socks4 and socks5 proxies. If you were to use a http proxy (no https, without connect-method, see proxy article), you could access only http sites, no https sites. Rather redsocks can convert UDP DNS queries to TCP DNS queries.

===== DNS resolution =====

The complication (and also advantage/feature) with transparent proxying is, that the internet application (browser, etc.) is not aware of the proxy. Therefore the internet application will attempt to do the DNS resolution itself using the system, not using the proxy. The DNS requests also must be considered. Since Tor does not support UDP, we have to transmit DNS queries via TCP.

It is impossible to resolve DNS directly on the proxy, when using the proxy as a transparent proxy, see [https://sourceforge.net/p/whonix/wiki/Inspiration/#transparent-proxying-method Transparent Proxying Method] for explanation. You need an extra DNS server, which answers over TCP.

You have several options to resolve DNS.

Either leave the setup as it is, Tor's DnsPort and therefore the Tor exit nodes will still do the DNS requests. (See DNS rule #1.) This is probable not what you want, since you wanted to cloak your identity with an additional proxy after Tor.

Alternatively you can use a public DNS resolver. The instructions for [https://sourceforge.net/p/whonix/wiki/OptionalConfigurations/#dnscrypt-by-opendns DNSCrypt by OpenDNS]<sup>4</sup> should work out of the box (tested). (See DNS rule #2.) (See footnotes <sup>1</sup>, <sup>2</sup> and <sup>3</sup> if you are looking for other alternatives.)

Read the [https://sourceforge.net/p/whonix/wiki/Secondary%20DNS%20Resolver/ DNS related warnings].

<font size="-3"> ,, <sup>1</sup> Also [https://sourceforge.net/p/whonix/wiki/OptionalConfigurations/#httpsdnsd-by-jondos httpsdnsd by JonDos]<sup>4</sup> might work, but you'd need to make some changes (use httpsdnsd as a system wide, Whonix-Workstation wide, DNS resolver, not just for a specific user account). <sup>2</sup> Or perhaps also [http://www.mulliner.org/collin/ttdnsd.php ttdnsd] with Google could work. All [https://en.wikipedia.org/wiki/Comparison_of_DNS_server_software DNS resolvers] should work, as long TCP is supported and as long you are querying a TCP enabled DNS server. <sup>3</sup> You can't simply add another public DNS resolver (i.e. OpenDNS or Google) to /etc/resolv.conf in Whonix-Workstation (i.e. Tor -&gt; public DNS resolver), it would have no effect, as explained under [https://sourceforge.net/p/whonix/wiki/Install%20Software/#whonix-workstation-is-firewalled Whonix-Workstation is firewalled]. <sup>4</sup> DNSCrypt and httpsdnsd add the advantage, that neither the proxy nor the Tor exit node can sniff or manipulate your DNS requests, since they are encrypted and authenticated. </font>

==== HowTo ====

Everything on Whonix-Workstation.

Get a working proxy and test if it works reliable.

Install redsocks.

<pre>## Untested, easier. Please try and leave feedback.
sudo apt-get install redsocks

## Or compile form git.
#git clone https://github.com/darkk/redsocks.git
## Build latest stable. 0.4 at time of writing. See
## https://github.com/darkk/redsocks/tags for
## most recent tag.
#git tag -v &lt;version&gt;
#compile...</pre>
Config redsocks. TODO: share config. Shouldn't be hard to do oneself. See [https://github.com/darkk/redsocks/blob/master/debian/redsocks.conf default config]. If you do, please share.

Add user redsocks.

<pre>sudo adduser redsocks</pre>
Start redsocks.

<pre>sudo -u redsocks ./redsocks</pre>
Create a fw.sh and use this firewall rules.

<pre>#!/bin/bash
## These iptables rules redirect the traffic for all users,
## including root, with the exception of the user redsocks,
## through the proxy.

## TODO: these iptables rules need review.

## Choose either DNS rule #1 or DNS rule #2.

## For debugging/testing use this command in console.
## tail -f /var/log/syslog

## Flush old rules.
iptables -F
iptables -t nat -F
iptables -X

## Allow unlimited traffic on the loopback interface.
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT
iptables -A OUTPUT --dst 127.0.0.1 -j ACCEPT

## Established incoming connections are accepted.
iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT

## Established outgoing connections are accepted.
iptables -A OUTPUT -m state --state RELATED,ESTABLISHED -j ACCEPT

## DNS rule #1.
## Allow DNS directly through Whonix-Gateway.
#iptables -A OUTPUT --dst 192.168.0.10 -p udp --dport 53 -j ACCEPT

## DNS rule #2.
## For DNSCrypt set /etc/resolv.conf to
## nameserver 127.0.0.1
##
## sudo dnscrypt-proxy --tcp-only --user=user
##
## DNSCrypt listening on port 53
iptables -t nat -A OUTPUT --dst 127.0.0.1 -p udp --dport 53 -j ACCEPT
iptables -t nat -A OUTPUT --dst 127.0.0.1 -p tcp --dport 53 -j ACCEPT

## redsocks must be allowed to establish direct connections.
iptables -A OUTPUT -j ACCEPT -m owner --uid-owner redsocks
iptables -t nat -A OUTPUT -j ACCEPT -m owner --uid-owner redsocks

## Redirect remaining traffic to redsocks.
iptables -t nat -A OUTPUT -p tcp -j REDIRECT --to-port 12345

## TODO: UDP rule untested.
#iptables -t nat -A OUTPUT -p udp -j REDIRECT --to-port 10053

## Log blocked traffic for debugging.
iptables -A OUTPUT -j LOG --log-level 4 --log-prefix &quot;iptables: &quot;

## Reject all other traffic.
iptables -A OUTPUT -j REJECT</pre>
Make the firewall script executable.

<pre>sudo chmod +x fw.sh</pre>
Apply the firewall rules.

<pre>sudo ./fw.sh</pre>
== Tunnel SSH through Tor ==

'''user -&gt; Tor -&gt; SSH'''

This chapter is not about connecting to a SSH server as a client (see Whonix in general and the Torify HOWTO). It is about adding an extra SSH tunnel after Tor.

Note, that even though SSH supports socks5, SSH is still not able to forward UDP on its own. Have a look the the [http://zarb.org/~gc/html/udp-in-ssh-tunneling.html source] of that information. To summarize: to tunnel UDP over SSH client and shell admin need a special setup, which is for most shells, not going to happen.

A SSH tunnel will provide a local socks5 proxy. Create the SSH tunnel in the Whonix-Workstation. From there you'll end up with a local socks5 proxy. You can use this socks5 proxy following the proxy instructions above. Once the SSH tunnel is established, there are not many differences, besides the difference already clarified above about UDP and that the warning about missing encryption to the proxy does not apply to SSH tunnels, since SSH is encrypted. The SSH process needs to be allowed to access the internet directly, if you use transparent proxying, run the SSH process under an account, which is privileged to access the internet directly.

Another untested method may be [https://github.com/apenwarr/sshuttle sshuttle].

== Tunnel VPN through Tor ==

'''user -&gt; Tor -&gt; VPN'''

=== Notes ===

==== UDP ====

Note, that you have to choose TCP transport, because Tor does not support UDP.

==== Using TransPort instead of SocksPort is required for Tor -&gt; VPN ====

For applications configured to use SocksPort, instead of TransPort, which is the default setting for most Whonix default applications, such as [https://sourceforge.net/p/whonix/wiki/TorBrowser/ Tor Browser]...

SocksPort is configured for [https://sourceforge.net/p/whonix/wiki/Stream%20Isolation/ Stream Isolation]. As [https://trac.torproject.org/projects/tor/wiki/doc/TorPlusVPN Tor Plus VPN or proxy] explains, you have to keep in mind, a VPN behind Tor adds a permanent exit node.

Rather, all applications, which are configured to use SocksPort, will not be tunneled through the VPN. They will be &quot;only&quot; tunneled through Tor. This is because, the VPN will not touch connections to ''192.168.0.10'', which is the Whonix-Gateway. For example, if you wish to tunnel Tor Browser through Tor -&gt; VPN, you have to remove all proxy settings from Tor Browser, see [https://sourceforge.net/p/whonix/wiki/TorBrowser/#whonix-proxy-settings-userjs Tor Browser Whonix Proxy Settings / user.js]. Check.torproject.org will tell you then &quot;''You are not using Tor.''&quot; and you'll see your VPN's IP. In fact your VPN was tunneled through Tor first. (Because Whonix-Workstation can not make any non-Tor connections by design, everything is tunneled over Tor.) When you stop your VPN for test reasons (''sudo /etc/init.d/openvpn stop''), it will show &quot;''You are using Tor.''&quot; again.

==== Use a Fail Closed Mechanism ====

This is not a Whonix specific problem. It is a general problem with VPNs. Most users are simply not aware of it. VPN's generally fail open. VPN servers and VPN software can occasionally break down without announcement. This means, if the VPN is unreachable, connections breaks down for whatever reasons and so on, in most cases, you can continue to connect to the internet without the VPN.

Whonix-Workstation will seamlessly continue to make &quot;direct&quot; connections through Tor once the VPN breaks down. If you are using the VPN only to connect to websites which ban Tor, you may not care so much. On the other hand, if you believe a VPN improves your security, it would be rational to make sure, the VPN is always used instead only most of the time.

If you want to enforce, that the VPN gets always used, see [VPN-Firewall].

==== VPN and stream isolation ====

While you are using a VPN behind Tor, you probable also may not be able to make use of the stream isolation feature <sup>1</sup>, which is planed Tor Browser. This is because Tor Browser would not talk to Tor directly anymore. Tor Browser would connect to the VPN instead.

<font size="-3"> <sup>1</sup> [https://trac.torproject.org/projects/tor/ticket/3455 Bug #3455: Tor Browser should set SOCKS username for a request based on referer] </font>

==== Identity correlation ====

By design, a VPN routes all your applications (those without any proxy settings, as explained above) through the VPN. You may not want this, as explained above ([Stream Isolation]). To circumvent that, you should use this Whonix-Workstation only for the particular application you want to route through the VPN. You are advised to read [https://sourceforge.net/p/whonix/wiki/Multiple%20Whonix-Workstations/ Multiple Whonix-Workstations].

=== How ===

Just use general instructions on doing so and of course do it inside Whonix-Workstation. Don't forget to read all the notes above. Since everything is routed through Tor, the VPN can be easily tunneled through Tor.

See also [https://sourceforge.net/p/whonix/wiki/TestVPN/ Free example VPNs working with Whonix for testing purposes].

= Footer =

[[include ref=WikiFooter]]

