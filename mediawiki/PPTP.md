[[include ref=WikiHeader]]

For what this is useful: PPTP is used because it's very easy to configure and well supported by all kind of devices. Compared to a proper set up with a hardware gateway between the internet and the devices you want to torify it's less secure but doesn't require any kind of hardware or network layout changes.

**This article has not been checked since latest Whonix release. May require update. **

[TOC]

''''''Description''''''

VPN ([http://en.wikipedia.org/wiki/Vpn Virtual private network]) is a method for users to connect to another network and access resources that can be seen from that network.

In this case, VPN is used to allow other users on your local LAN to connect and use your TorBox to connect to Tor with minimal configuration. Unlike Tor-VM where all network connections are forced through Tor or rejected workstations connected over PPTP are NOT automatically protected against network level leaks and application layer exploits.

We use [http://en.wikipedia.org/wiki/Pptp PPTP] here due to its wide install base (every installation of Windows since Windows 95 includes a client) and ease of installation. Be aware of the [http://en.wikipedia.org/wiki/Pptp#Security_of_the_PPTP_protocol enormous security issues with PPTP].

'''Warning''', PPTP should '''NOT''' be used with TorBox over the Internet, only for local trusted sources. See below for an OpenVPN implementation that allows use of Tor with minimal client configuration and should be secure enough to allow Internet connections (coming soon).

''''''VPN: Bypassing Censorship &amp; Enabling Free Speech''''''

Ref: ([http://en.flossmanuals.net/bypassing-censorship/ch025_what-is-vpn/ How to Bypass Internet Censorship @ Flossmanuals.net])

<pre>Because VPN services [http://en.wikipedia.org/wiki/IP_tunnel tunnel] all Internet traffic, they can be used for e-mail, instant messaging,</pre>
Voice over IP (VoIP) and any other Internet service in addition to Web browsing, making everything that travels through the tunnel unreadable to anyone along the way.

<pre>If the tunnel ends outside the area where the Internet is being restricted, this can be an effective method of circumvention,</pre>
since the filtering entity/server sees only encrypted data, and has no way of knowing what data is passing through the tunnel. It has the additional effect of making all your different kinds of traffic look similar to an eavesdropper.

We use VPN here for its “tunnel” capabilities, so that others that you allow access, can take advantage of Tor via TorBox with a single connection.

= Install PPTPd =

(Whonix-Gateway)

From your Whonix-Gateway:

<pre>apt-get install pptpd</pre>
This will install and start the <code>pptpd</code> daemon on your Whonix-Gateway. Verify its running:

<pre>ps aux | grep pptpd</pre>
Should show something similar to:

<pre>root      8357  0.0  0.5  10512   696 ?        Ss   17:26   0:00 /usr/sbin/pptpd</pre>
Stop it for the time being, while we configure it.

<pre>/etc/init.d/pptpd stop</pre>
= Configure PPTP =

(Whonix-Gateway)

Configure PPTP settings:

<pre>nano /etc/pptpd.conf</pre>
Setup your <code>localip</code> and <code>remoteip</code> settings:

<pre>localip 192.168.0.1 #your eth1 address
remoteip 192.168.0.200-250 #a range of unassigned IP's</pre>
See the [http://poptop.sourceforge.net/dox/pptpd.conf.txt official documentation here].

'''Discussion:'''

This can be potentially confusing, as the documentation in the configuration files are not the best. When you setup a PPTP connection, your Whonix-Gateway will setup a virtual adapter (e.g. ppp0) which will output traffic sent from your client computer (those that connect to your server from your local LAN) to the Whonix-Gateway and allow it to be routed through Tor. So if we want to use this virtual adapter just like a real adapter (e.g. eth0), we need to give it an IP address. That's what the <code>localip</code> option is.

<code>remoteip</code> is a bit simpler. It's the IP address (or addresses) that are assigned to the client's computer when they connect. They get their own virtual adapter, which needs its own IP address.

See the [http://poptop.sourceforge.net/dox/qna.html#19 FAQ here for information]. For a simple overview of the VPN process see [https://help.ubuntu.com/community/VPNClient#Extra_credit:''how''VPN_works VPNClient @ Ubuntu Community Documentation].

'''localip''', for simplicity should be the IP of your eth1, as Tor is already configured to listen here and we don't actually do any routing creating an IP address conflict. '''remoteip''', should be several IP's on your internal network (you should have as many IP's as potential clients, for example the “192.168.0.200-250” range above defines IP's for 50 clients)

(Advanced: <code>localip</code> and <code>remoteip</code> can be set to other networks, other subnets, etc. With our approach it doesn't matter what their IP's are, simply that they exist. It is in fact encouraged that such clients be assigned to a “quarantine” network. Since we don't have routing enabled, other subnets would prevent your client's from seeing each other and your already established “safe” LAN; where your Whonix-Workstation lives. But! The <code>torrc</code> would need to be updated to listen on said addresses as well. Subneting in this fashion is beyond the scope of this document.)

= Configure PPTP Options =

(Whonix-Gateway)

<pre>nano /etc/ppp/pptpd-options</pre>
Verify the following settings are configured as shown:

<pre>refuse-pap
refuse-chap
refuse-mschap
require-mschap-v2
require-mppe-128
ms-dns &lt;eth1 address&gt;</pre>
'''Discussion:''' [http://poptop.sourceforge.net/dox/options.pptpd.txt See official documentation here].

'''refuse-pap''': [http://en.wikipedia.org/wiki/Password_authentication_protocol PAP style authentication], insecure, so we don't want to use it if we can help it. '''refuse-chap''': [http://en.wikipedia.org/wiki/Challenge-Handshake_Authentication_Protocol CHAP authentication], insecure. '''refuse-mschap''': [http://en.wikipedia.org/wiki/MSCHAP MS-CHAP], insecure '''require-mschap-v2''': [http://en.wikipedia.org/wiki/MSCHAPv2 MS-CHAPv2], make sure that any connecting client must use this. It's as secure a we can get for a supported authentication method for PPTP. '''require-mppe-128''': [http://en.wikipedia.org/wiki/MPPE Microsoft Point-to-Point Encryption], as secure encryption as we can get over PPTP, 128 bit is the maximum supported. '''ms-dns''': Use this address as the DNS server for connecting (Windows) clients.

= Configure IPtables rules for client connect and disconnect =

(Whonix-Gateway)

The <code>ip-up</code> script is called on each connection by a PPTP client, so we can put special firewall rules here to help with Torifying the traffic through this interface.

<pre>nano /etc/ppp/ip-up</pre>
Add to the end:

<pre>#Firewall rules to add to route PPTP through TOR
#Tor's TransPort
TRANS_PORT#&quot;9040&quot;

iptables -t nat -A PREROUTING -i $PPP_IFACE -p udp --dport 53 -j REDIRECT --to-ports 53
iptables -t nat -A PREROUTING -i $PPP_IFACE -p tcp --syn -j REDIRECT --to-ports $TRANS_PORT</pre>
The variable “$PPP_IFACE” is defined in the script (see the documentation at the beginning of the ip-up script) and resolves to the name of the interface established after a PPTP connection (e.g. ppp0).

Similarly the <code>ip-down</code> script is called when tearing down the connection. To prevent your iptables from getting polluted with redundant rules, we remove the previously configured rules here:

<pre>nano /etc/ppp/ip-down</pre>
Add to the end:

<pre>#Firewall rules to add to route PPTP through TOR
#Tor's TransPort
TRANS_PORT#&quot;9040&quot;

iptables -t nat -D PREROUTING -i $PPP_IFACE -p udp --dport 53 -j REDIRECT --to-ports 53
iptables -t nat -D PREROUTING -i $PPP_IFACE -p tcp --syn -j REDIRECT --to-ports $TRANS_PORT</pre>
Notice the addition of the '''-D''' instead of '''-A''' to the rule definitions. This tells <code>iptables</code> to Delete a rule with those parameters rather than Add one.

([http://manpages.ubuntu.com/manpages/karmic/man8/iptables.8.html See IPTables documentation])

= Testing =

(Whonix-Gateway)

Start up your PPTP server:

<pre>/etc/init.d/pptpd start</pre>
(Client)

From a client on your network (preferably one outside of your Tor network, e.g. not your Whonix-Workstation) connect to your VPN server.

Instructions for a variety of clients:

[http://pptpclient.sourceforge.net/documentation.phtml Linux (many flavors, direct from the pptp-client site)] [http://support.microsoft.com/kb/314076 How to configure a connection to a virtual private network (VPN) in Windows XP] [https://help.ubuntu.com/community/VPNClient VPNClient @ Ubuntu Community Documentation] [http://www.pcworld.com/article/210562/how_to_set_up_vpn_in_windows_7.html Windows 7 VPN step by step guide]

Now verify the connection on the gateway, after successfully connecting: (Whonix-Gateway)

<pre>ifconfig</pre>
Should show something like:

<pre>ppp0      Link encap:Point-to-Point Protocol
    inet addr:192.168.0.1  P-t-P:192.168.0.200  Mask:255.255.255.255
    UP POINTOPOINT RUNNING NOARP MULTICAST  MTU:1496  Metric:1
    RX packets:91 errors:0 dropped:0 overruns:0 frame:0
    TX packets:71 errors:0 dropped:0 overruns:0 carrier:0
    collisions:0 txqueuelen:3
    RX bytes:10080 (10.0 KB)  TX bytes:3622 (3.6 KB)</pre>
.

<pre>iptables -vnL -t nat</pre>
Should show:

<pre>Chain PREROUTING (policy ACCEPT 103 packets, 14589 bytes)
pkts bytes target     prot opt in     out     source                   destination                                          
    0     0 REDIRECT   udp  --  ppp0  *       0.0.0.0/0            0.0.0.0/0 udp dpt:53     redir ports 53
   22  1320 REDIRECT   tcp  --  ppp0  *       0.0.0.0/0            0.0.0.0/0 tcp     flags:0x17/0x02 redir ports 9040</pre>
(You may have more information displayed here depending on configuration, but the lines above should at least appear in your PREROUTING chain)

(Client)

On the client you should then be able to connect via Tor.

* Browse to <code>check.torproject.org</code> and verify the “congratulations” message

Next disconnect from the VPN. On the server you should see several changes: (Whonix-Gateway)

* <code>ifconfig</code> should no longer show any ppp interfaces
* <code>iptables -vnL -t nat</code> should show no rules that involve any ppp interfaces

You can in fact test several client connections in this way. Each should get a new IP address (192.168.0.201, 192.168.0.202, etc), create a new virtual adapter (ppp1, ppp2, etc) and route through Tor via the Iptables commands (as above).

You can also attempt [LeakTests Leak Testing] to verify that no packets are leaking through your VPN connection.

= Footer =

[[include ref=WikiFooter]]

