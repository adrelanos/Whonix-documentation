[[include ref=WikiHeader]]

[TOC]

# Tunnel Proxy/SSH/VPN through Tor #
## Required Knowledge ##
### Introduction ###
**user -> Tor -> Proxy/SSH/VPN**

Read first: [Tor Plus VPN or proxy](https://trac.torproject.org/projects/tor/wiki/doc/TorPlusVPN) and [Whonix VPN disclaimer](https://sourceforge.net/p/whonix/wiki/Authorship/#whonix-vpn-disclaimer).

You can tunnel through Tor first and add an additional proxy, SSH or VPN hop at the very end of that chain as your "exit node". The services you connect to, will not know, that you are using Tor ^1^. This can be useful to **evade Tor bans**, for example, to visit websites or IRC networks who blacklisted Tor. Beware of the risks, this adds a "permanent exit node", read [Tor Plus VPN or proxy](https://trac.torproject.org/projects/tor/wiki/doc/TorPlusVPN).

To do that, go to your Whonix-Workstation and add the proxy, SSH or VPN normally, just like you would do, if you wouldn't use the Whonix-Gateway. Adding your proxy, SSH or VPN inside Whonix-Workstation will, thanks to Whonix-Gateway, result in them getting tunneled over Tor.

[Protocol leaks](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO) still apply, thought to a lesser extend. Leaks would *only* leak through Tor and you have best possible [Protocol-Leak-Protection and Fingerprinting-Protection](https://sourceforge.net/p/whonix/wiki/Whonix%27s%20Protocol-Leak-Protection%20and%20Fingerprinting-Protection/).

<font size="-3">
,,
^1^ Unless it's a "transparent proxy" in sense of sending http forwarded for, covered in the [Tor Plus VPN or proxy](https://trac.torproject.org/projects/tor/wiki/doc/TorPlusVPN) article.
</font>

### uwt and Tor Browser ###
There are two special cases in Whonix. Applications using uwt and Tor Browser. These are pre-configured to use Socks Proxy settings. (<font size="-3">(...and not just TransPort, which is a security feature: Stream Isolation.)</font>

You may have to disable the affected uwt wrapper, in case there is one, for the application you want to tunnel. See [Stream Isolation](https://sourceforge.net/p/whonix/wiki/Stream%20Isolation/) to learn what uwt and uwt wrappers are. For example to deactivate the uwt wrapper for wget, you could use.

    sudo chmod -x /usr/local/bin/apt-get

If you want to do it with Tor Browser, you must [Remove Proxy Settings](https://sourceforge.net/p/whonix/wiki/TorBrowser/#remove-proxy-settings).

### Malware ###
Also note, that once Whonix-Workstation gets rooted by malware, the VPN/SSH/proxy can be easily circumvented by the attacker and you are left to the protections by Whonix and Tor.

### Leaks ###
If setting up socksifier, proxy settings, transparent proxy with local redirection, SSH tunnel or a VPN in a leak free manner were easy, this means while ensuring nothing will bypass the VPN, SSH or proxy, there would have been no reason to develop Whonix in the first place.

The methods described on this page are all tested and should all more or less work. Should there be any misconfiguration or leak bug, you are left to the protections by Whonix and Tor. This means, the leak will still go through Whonix-Gateway and therefore Tor. The methods on this page are not as safe as a Whonix-Gateway. There were development discussions and [some progress](https://sourceforge.net/p/whonix/wiki/Inspiration/), about chaining multiple Gateways, VPNBOX, JonDoBOX, i2pBOX, FreenetBOX and ProxyBOX, but nothing was finished to to lack of community interest, support and developers.

### Web Browser ###
I don't know how anonymous it is to use (VPN ->) Tor -> VPN -> Tor Browser -> website. How many people show up with a VPN IP using Tor Browser? This setup is so special that I believe only very few people are doing it. For this reason, I recommend against.

On the other hand, due to browser fingerprinting, I can't really recommend to use another browser than Tor Browser either.

## Tunnel proxy through Tor ##
**user -> Tor -> proxy**

Note, that the connection, between the Tor exit node and the proxy, is in most cases, not encrypted.

### Proxy Settings Method ###
After understanding the *Required Knowledge* chapter above, using proxy settings in Whonix there is no difference from using proxy settings in an ordinary why, other than that it's running inside Whonix-Workstation.

If proxy settings are honored by application or in worst case leak through Tor alone (thanks to Whonix), is another question and not in Whonix's power, see [TorifyHOWTO](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO).

### Proxyfier Method ###
#### General ####
After understanding the *Required Knowledge* chapter above, using a Proxyfier in Whonix there is no difference from using a Proxyfier in an ordinary way, other than that it's running inside Whonix-Workstation.

If the Proxifier is leak free or in worst case leaks through Tor alone (thanks to Whonix), is another question and not in Whonix's power, see [TorifyHOWTO](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO).

#### uwt ####
uwt uses torsocks. While the name implies it's Tor specific, it's not. You can point it to any socks proxy. Examples.

    ## For Tor stream isolation #1
    uwt -t 5 -i 192.168.0.10 -p 9153 /usr/bin/wget -c https://check.torproject.org

    ## For Tor stream isolation #2
    uwt -t 5 -i 192.168.0.10 -p 9154 /usr/bin/wget -c https://check.torproject.org

    ## Proxy
    uwt -t 5 -i x.x.x.x -p xxxx /usr/bin/wget -c https://check.torproject.org

<font size="-3"Using the full path, i.e. /usr/bin/wget will circumvent the wget uwt wrapper.</font>

For testing, if you didn't disable the wget uwt wrapper, the following command will most likely get another IP, because still using Stream Isolation.

    ## Using Tor's TransPort
    ## (/usr/local/bin/wget uwt wrapper)
    wget https://check.torproject.org

#### proxychains ####
**WARNING**:

* I don't know how well proxychains works. For example [torsocks has a IPv6 leak bug](https://trac.torproject.org/projects/tor/wiki/doc/torsocks#WorkaroundforIPv6leakbug). I don't know if proxychains forces everything through the proxies. Whonix only ensures, should their be leaks, they go only through Tor.
* There are at least three different versions of proxychains. The old/original/unmaintained version on sourceforge.net and two forks on github. I don't know about that status of any of them and haven't heard of anyone looking if they do really work as expected. The two authors argue with each other and I wasn't motivated to understand the conflict and to determine which version is better. However, any leaks not going through the proxy(chain) will go through Tor.

Instructions:

Install proxychains.

    sudo apt-get install proxychains

Note the uwt and Tor Browser notice in *Required Knowledge* above first. After you have done so it's quite simple.

Open proxychains configuration file.

    kdesudo leafpad /etc/proxychains.conf

Go to the bottom of the settings file. Comment out "*socks4 127.0.0.1 9050*" and add for example "*socks5 192.168.0.10 9152*" (for Tor stream isolation) or "*socks5 ip port*" with an IP and port of your choice to set the proxy settings. 

    [ProxyList]
    ## add proxy here ...
    ## meanwhile
    ## defaults set to "tor"
    #socks4 127.0.0.1 9050
    socks5 192.168.0.10 9152
    # socks5 x.x.x.x xxxx

Advanced. Recommendation: Why not use Tor stream isolation for the proxychains connection?

    [ProxyList]
    ## add proxy here ...
    ## meanwhile
    ## defaults set to "tor"
    #socks4 127.0.0.1 9050
    socks5 192.168.0.10 9152
    socks5 x.x.x.x xxxx

Safe the configuration file. Test afterwards. For example:

    proxychains /usr/bin/wget https://check.torproject.org

Will do.

For testing, if you didn't disable the wget uwt wrapper, the following command will most likely get another IP. (Stream Isolation)

    ## Using Tor's TransPort
    ## (/usr/local/bin/wget uwt wrapper)
    wget https://check.torproject.org

### Transparent Proxying ###
#### Introduction ####
To make clear, what this is about. Whonix-Gateway is already servering as a Transparent Proxy <font size="-3">(anonymizing middlebox)</font>, which means, that all applications not explicitly configured <font size=-3>(by uwt socksifier or proxy settings)</font> to use a SocksPort, can connect through Tor without any settings. The Transparent Proxying chapter on the *Tunnel Proxy/SSH/VPN through Tor* page is about configuring Whonix-Workstation also to act as a Transparent Proxy <font size="-3">(local redirection)</font>. Use case: a user wants to ensure all traffic goes through Tor (by using Whonix-Gateway) and want to additionally ensure, all traffic goes through a proxy choosen by the user behind Tor, i.e. user -> Tor -> proxy.

<font size="-3">[torproject.org wiki version 129](https://trac.torproject.org/projects/tor/wiki/doc/TorBOX/OptionalConfigurations?version=129#TransparentProxying) contains an old example using privoxy, JonDo and httpsdnsd. The new example uses redsocks and is simpler.</font>

You always have to keep in mind, which kind of data and which kind of proxy you are using. There are CGIproxies, http(s) proxies and socks4/4a/5 proxies.

In case you redirect the network layer directly with iptables, you need a TransPort. Unfortunately very few applications, do offer a TransPort. For example, Tor supports a TransPort. In most other cases, you need to translate the different kinds of data.

Due to the nature of Transparent Proxying, we need to redirect with iptables and end up with a "Trans data stream". Because most proxies are either http or socks we need to translate this. Below we discuss a few tools which help here, not all are required, depending on what you want to do.

Required reading: 

* [proxy](https://trac.torproject.org/projects/tor/wiki/doc/proxy)
* [Tor Plus VPN or proxy](https://trac.torproject.org/projects/tor/wiki/doc/TorPlusVPN)

##### Tools #####
Tor is a socks proxy and also has a TransPort. Unfortunately, Tor can not be directly used as a http proxy. You must also keep in mind, that Tor does not support UDP, although it offers a DnsPort..

[redsocks](http://darkk.net.ru/redsocks/) can also accept "Trans data streams" and can forward them to http**s**, socks4 and socks5 proxies. If you were to use a http proxy (no https, without connect-method, see proxy article), you could access only http sites, no https sites. Rather redsocks can convert UDP DNS queries to TCP DNS queries.

##### DNS resolution #####
The complication (and also advantage/feature) with transparent proxying is, that the internet application (browser, etc.) is not aware of the proxy. Therefore the internet application will attempt to do the DNS resolution itself using the system, not using the proxy. The DNS requests also must be considered. Since Tor does not support UDP, we have to transmit DNS queries via TCP.

It is impossible to resolve DNS directly on the proxy, when using the proxy as a transparent proxy, see [Transparent Proxying Method](https://sourceforge.net/p/whonix/wiki/Inspiration/#transparent-proxying-method) for explanation. You need an extra DNS server, which answers over TCP.

You have several options to resolve DNS.

Either leave the setup as it is, Tor's DnsPort and therefore the Tor exit nodes will still do the DNS requests. (See DNS rule #1.) This is probable not what you want, since you wanted to cloak your identity with an additional proxy after Tor.

Alternatively you can use a public DNS resolver. The instructions for [DNSCrypt by OpenDNS](https://sourceforge.net/p/whonix/wiki/OptionalConfigurations/#dnscrypt-by-opendns)^4^ should work out of the box (tested). (See DNS rule #2.) (See footnotes ^1^, ^2^ and ^3^ if you are looking for other alternatives.)

Read the [DNS related warnings](https://sourceforge.net/p/whonix/wiki/Secondary%20DNS%20Resolver/).

<font size="-3">
,,
^1^ Also [httpsdnsd by JonDos](https://sourceforge.net/p/whonix/wiki/OptionalConfigurations/#httpsdnsd-by-jondos)^4^ might work, but you'd need to make some changes (use httpsdnsd as a system wide, Whonix-Workstation wide, DNS resolver, not just for a specific user account).
^2^ Or perhaps also [ttdnsd](http://www.mulliner.org/collin/ttdnsd.php) with Google could work. All [DNS resolvers](https://en.wikipedia.org/wiki/Comparison_of_DNS_server_software) should work, as long TCP is supported and as long you are querying a TCP enabled DNS server.
^3^ You can't simply add another public DNS resolver (i.e. OpenDNS or Google) to /etc/resolv.conf in Whonix-Workstation (i.e. Tor -> public DNS resolver), it would have no effect, as explained under [Whonix-Workstation is firewalled](https://sourceforge.net/p/whonix/wiki/Install%20Software/#whonix-workstation-is-firewalled).
^4^ DNSCrypt and httpsdnsd add the advantage, that neither the proxy nor the Tor exit node can sniff or manipulate your DNS requests, since they are encrypted and authenticated.
</font>

#### HowTo ####
Everything on Whonix-Workstation.

Get a working proxy and test if it works reliable.

Install redsocks.

    ## Untested, easier. Please try and leave feedback.
    sudo apt-get install redsocks

    ## Or compile form git.
    #git clone https://github.com/darkk/redsocks.git
    ## Build latest stable. 0.4 at time of writing. See
    ## https://github.com/darkk/redsocks/tags for
    ## most recent tag.
    #git tag -v <version>
    #compile...

Config redsocks. TODO: share config. Shouldn't be hard to do oneself. See [default config](https://github.com/darkk/redsocks/blob/master/debian/redsocks.conf). If you do, please share.

Add user redsocks.

    sudo adduser redsocks

Start redsocks.

    sudo -u redsocks ./redsocks


Create a fw.sh and use this firewall rules.

    #!/bin/bash
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
    iptables -A OUTPUT -j LOG --log-level 4 --log-prefix "iptables: "

    ## Reject all other traffic.
    iptables -A OUTPUT -j REJECT

Make the firewall script executable.

    sudo chmod +x fw.sh

Apply the firewall rules.

    sudo ./fw.sh

## Tunnel SSH through Tor ##
**user -> Tor -> SSH**

This chapter is not about connecting to a SSH server as a client (see Whonix in general and the Torify HOWTO). It is about adding an extra SSH tunnel after Tor.

Note, that even though SSH supports socks5, SSH is still not able to forward UDP on its own. Have a look the the [source](http://zarb.org/~gc/html/udp-in-ssh-tunneling.html) of that information. To summarize: to tunnel UDP over SSH client and shell admin need a special setup, which is for most shells, not going to happen.

A SSH tunnel will provide a local socks5 proxy. Create the SSH tunnel in the Whonix-Workstation. From there you'll end up with a local socks5 proxy. You can use this socks5 proxy following the proxy instructions above. Once the SSH tunnel is established, there are not many differences, besides the difference already clarified above about UDP and that the warning about missing encryption to the proxy does not apply to SSH tunnels, since SSH is encrypted. The SSH process needs to be allowed to access the internet directly, if you use transparent proxying, run the SSH process under an account, which is privileged to access the internet directly.

Another untested method may be [sshuttle](https://github.com/apenwarr/sshuttle).

## Tunnel VPN through Tor ##
**user -> Tor -> VPN**

### Notes ###
#### UDP ####
Note, that you have to choose TCP transport, because Tor does not support UDP.

#### Using TransPort instead of SocksPort is required for Tor -> VPN ####
For applications configured to use SocksPort, instead of TransPort, which is the default setting for most Whonix default applications, such as [Tor Browser](https://sourceforge.net/p/whonix/wiki/TorBrowser/)...

SocksPort is configured for [Stream Isolation](https://sourceforge.net/p/whonix/wiki/Stream%20Isolation/). As [Tor Plus VPN or proxy](https://trac.torproject.org/projects/tor/wiki/doc/TorPlusVPN) explains, you have to keep in mind, a VPN behind Tor adds a permanent exit node.

Rather, all applications, which are configured to use SocksPort, will not be tunneled through the VPN. They will be "only" tunneled through Tor. This is because, the VPN will not touch connections to *192.168.0.10*, which is the Whonix-Gateway. For example, if you wish to tunnel Tor Browser through Tor -> VPN, you have to remove all proxy settings from Tor Browser, see [Tor Browser Whonix Proxy Settings / user.js](https://sourceforge.net/p/whonix/wiki/TorBrowser/#whonix-proxy-settings-userjs). Check.torproject.org will tell you then "*You are not using Tor.*" and you'll see your VPN's IP. In fact your VPN was tunneled through Tor first. (Because Whonix-Workstation can not make any non-Tor connections by design, everything is tunneled over Tor.) When you stop your VPN for test reasons (*sudo /etc/init.d/openvpn stop*), it will show "*You are using Tor.*" again.

#### VPN breakdown ####
VPN servers and VPN software can occasionally break down without announcement. Whonix-Workstation will seamlessly continue to make "direct" connections through Tor once the VPN breaks down. This is not a Whonix specific problem. It is a general problem with VPNs. Most users are simply not aware of it. This happens also with the common setup, where the VPN simply runs on a host. If you want to enforce, that the VPN is always tunneled through Tor, have to use a modified routing table. It is currently in development and help is welcome, see [VPN](https://sourceforge.net/p/whonix/wiki/VPN/).

#### VPN and stream isolation ####
While you are using a VPN behind Tor, you probable also may not be able to make use of the stream isolation feature ^1^, which is planed Tor Browser. This is because Tor Browser would not talk to Tor directly anymore. Tor Browser would connect to the VPN instead.

<font size="-3">
^1^ [Bug #3455: Tor Browser should set SOCKS username for a request based on referer](https://trac.torproject.org/projects/tor/ticket/3455)
</font>

#### Identity correlation ####
By design, a VPN routes all your applications (those without any proxy settings, as explained above) through the VPN. You may not want this, as explained above ([Stream Isolation]). To circumvent that, you should use this Whonix-Workstation only for the particular application you want to route through the VPN. You are advised to read [Multiple Whonix-Workstations](https://sourceforge.net/p/whonix/wiki/Multiple%20Whonix-Workstations/).

### How ###
Just use general instructions on doing so and of course do it inside Whonix-Workstation. Don't forget to read all the notes above. Since everything is routed through Tor, the VPN can be easily tunneled through Tor.

See also [A Free example VPN working with Whonix for testing purposes](https://sourceforge.net/p/whonix/wiki/TestVPN/).

# Footer #
[[include ref=WikiFooter]]