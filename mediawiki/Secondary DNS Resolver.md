[[include ref=WikiHeader]]

[TOC]

= Secondary DNS Resolver =

== Introduction ==

By Whonix default, Tor is used for DNS resolution. If you suspect a Tor exit node to tamper with DNS, you can get a second opinion from another non-Tor DNS server. This may also be useful, in special cases if you want to resolve types of DNS over Tor, which are unsupported by Tor itself, such as MX <font size="-3">(required for some [Mixmaster] servers over Tor)</font> or DNSSEC.

It's recommend against to use non-Tor DNS resolvers for an extended amount of time. Although it's technically possible to completely replace DNS resolution (not using Tor for DNS resolution anymore), it's recommend against. That would add too much power to a single DNS server. Using a permanent DNS server is recommend against just as using a permanent Tor exit node is recommend against.

Note, that even if you correctly set up all settings, it might happen that this won't work. Sometimes Tor or the DNS server causes a timeout. This gets even worse, when you additionally tunnel the DNS request through an additional proxy (for example: Tor -&gt; JonDonym -&gt; DNS server).

Read first: [https://sourceforge.net/p/whonix/wiki/Stream%20Isolation/ Stream Isolation].

Required knowledge: Difference between encryption and authentication.

In the chapters below are examples how to use authenticated DNS ([https://en.wikipedia.org/wiki/Domain_Name_System_Security_Extensions DNSSEC]) or encrypted DNS (DNSCrypt or httpsdnsd). I haven't found any public DNS resolvers supporting both, encryption and authentication.

Note that most applications, such as [https://sourceforge.net/p/whonix/wiki/TorBrowser/ Tor Browser], will '''not''' ''automatically'' profit from setting up an alternative DNS resolver. This is because applications in Whonix are configured to use SocksPort instead of Trans- or DnsPort, see [https://sourceforge.net/p/whonix/wiki/Stream%20Isolation/ Stream Isolation] for details. Another reason is, that most applications do not yet make use of authenticated DNS (DNSSEC). However, you could use encrypted DNS when deconfiguring SocksPort and when using system resolver (TransPort).

== Authenticated DNS over Tor ==

=== DNSSEC over Tor ===

==== Example with CZ.NIC Labs DNS resolver ====

<font size="-3"> [https://labs.nic.cz/page/993/dnssec-validation-over-tor--linux-/ source for this chapter: CZ NIC LABS] </font>

The ''CZ.NIC Labs DNS resolver'' has been chosen as an example. Feel free to use and other DNS resolver at your own choice.

===== Installation =====

Install [https://unbound.net/ unbound] and [http://www.dest-unreach.org/socat/ socat].

<pre>sudo apt-get install unbound socat</pre>
Open ''/etc/unbound/unbound.conf''.

<pre>sudo nano /etc/unbound/unbound.conf</pre>
''Add'' the following lines.

<pre>#tcp-upstream goes under &quot;server:&quot; section
    tcp-upstream: yes

#put forward-zone somewhere at the end of file
forward-zone:
    name: &quot;.&quot;
    forward-addr: 0.0.0.0@5353</pre>
===== Starting =====

Open a terminal and start socat.

<pre>socat TCP4-LISTEN:5353,bind=localhost,reuseaddr,fork SOCKS4A:192.168.0.10:217.31.204.130:53,socksport=9150</pre>
Open another terminal tab and restart unbound.

<pre>sudo service unbound restart</pre>
===== Using =====

Test with dig.

<pre>dig +dnssec nic.cz @localhost</pre>
Please refer to upstream documentation on how to interpret the DNSSEC test results.

== Encrypted DNS over Tor ==

=== Introduction ===

This is different from DNSSEC.

=== DNSCrypt by OpenDNS ===

Although the official [https://www.opendns.com/technology/dnscrypt/ DNSCrypt website] states, that a Linux version does not exit, this [http://www.webupd8.org/2012/02/encrypt-dns-traffic-in-linux-with.html blog post] suggests there is one.

This has nothing to do with [https://en.wikipedia.org/wiki/Domain_Name_System_Security_Extensions DNSSEC], the differences of DNSSEC and DNSCrypt are well explained on the [https://www.opendns.com/technology/dnscrypt/ DNSCrypt website].

These instructions completely replace Tor's DNS resolver with opendns's dnscrypt for all users and the whole system. Not recommend for a longer amount of time, see warning above. Some hints are included how to do it only for a specific user account.

(1). Download the [https://github.com/opendns/dnscrypt-proxy/downloads dnscrypt source code] and unpack. You have to compile it. Get into the dnscrypt directory ''cd dnscrypt-proxy-...''. Configure ''./configure'', make ''make''.

(2). Start dnscrypt-proxy. <sup>1</sup> <sup>2</sup> <sup>3</sup> <sup>4</sup> <sup>5</sup> <sup>6</sup>

<pre>sudo dnscrypt-proxy --tcp-only</pre>
<font size="-3"> ,, <sup>1</sup> ''--tcp-only'' is required since Tor does not support UDP. The UDP DNS request will immediately get truncated reply and a RFC-compliant resolver should repeat same query via TCP in this case. This is the case for Ubuntu's default DNS resolver. You can get some more information on UDP/TCP/DNS on the unrelated [http://darkk.net.ru/redsocks/ redsocks] website. <sup>2</sup> To start it later in background (after debugging) add ''--daemonize''. <sup>3</sup> ''--help'' to see all options. <sup>4</sup> Start up takes a few seconds &quot;INFO Generating a new key pair&quot;, this is normal, wait. Until it's done, DNS will not work. <sup>5</sup> ''--user=username'' can and should be used to start the dnscrypt-proxy under a specific user account. <sup>6</sup> Since this instructions completely replace Tor's DNS resolver with opendns's dnscrypt for all users and the whole system, you could add ''--local-port=5800'' to let dnscrypt-proxy listen on port 5800. You would be able to add iptables rules to redirect only the DNS requests of a specific user account to opendns's dnscrypt, you can get some hints how to do that in the ''httpsdnsd by JonDos'' chapter below, which would be a very similar setup. </font>

(3). Edit your resolv.conf ''nano /etc/resolv.conf'', comment out everything and add ''nameserver 127.0.0.1''.

(4). Check if it's working, there are several [https://www.opendns.com/support/article/64 test pages] on opendns.com.

(5). To shut it down you can use ''sudo killall dnscrypt-proxy'' and don't forget to revert the changes in /etc/resolv.conf.

=== httpsdnsd by JonDos ===

==== Introduction ====

Source: [https://anonymous-proxy-servers.net/en/help/transocks.html anonymous-proxy-servers.net] and also use it as a more verbose tutorial, but keep in mind that their tutorial is JonDonym specific, while this tutorial is Tor specific.

Everything inside your Whonix-Workstation.

==== Installation ====

Install dependencies.

<pre>sudo apt-get install libnet-ssleay-perl libnet-server-perl libnet-dns-perl libxml-simple-perl liblog-log4perl-perl</pre>
Download httpsdnsd. (See source above in case download link changed.)

<pre>wget https://anonymous-proxy-servers.net/downloads/httpsdnsd.tar.bz2</pre>
Unpack.

<pre>.    </pre>
Go into the httpsdnsd folder.

<pre>cd httpsdnsd</pre>
Install httpsdnsd. <sup>1</sup>

<font size="-3"> ,, <sup>1</sup> (It contains also a uninstall.sh, if you want to uninstall it later.) </font>

<pre>sudo install.sh</pre>
Add a new user for httpsdnsd.

<pre>sudo adduser --system --disabled-password --group httpsdns_daemon</pre>
Editing /etc/resolv.conf is not required. (You still could out comment everything against DNS leaks.)

Create a firewall script.

<pre>nano dns-fw.sh</pre>
Insert these firewall rules.

<pre># Flush old rules
iptables -F
iptables -t nat -F
iptables -X

# Redirect DNS traffic to httpdnsd.
iptables -t nat -A OUTPUT -p udp -m owner --uid-owner anonuser --dport 53 -j REDIRECT --to-ports 4053

# Accept connections to the httpdnsd.
iptables -t filter -A OUTPUT -p udp -m owner --uid-owner anonuser --dport 4053 -j ACCEPT

# Reject all other traffic for anonuser.
iptables -t filter -A OUTPUT ! -o lo -m owner --uid-owner anonuser -j REJECT</pre>
Install Privoxy. <sup>1</sup>

<font size="-3"> ,, <sup>1</sup> [https://trac.torproject.org/projects/tor/wiki/doc/TorBOX/OptionalConfigurations?version=95#httpsdnsdbyJonDos torproject.org Wiki Version 95] of this site contains a working example using Polipo. Changed later to Privoxy, because Privoxy can be useful for other tasks as well. (Incoming: TransPort, http proxy; forwarding: http and socks.) </font>

<pre>sudo apt-get install privoxy</pre>
Open the privoxy configuration file.

<pre>nano /etc/privoxy/config</pre>
Add the following to your privoxy configuration file.

<pre># Theoretically you can tunnel through any
# http or socks proxy. Local or remote proxy.
# Inside Whonix-Workstation, due to design,
# everything will be tunneled through Tor first.

# Using Tor's socks5 proxy, running on Whonix-Gateway. 
# Change the port, see above...
forward-socks5 / 192.168.0.10:9112 .

# Another example using a http proxy.
# (In this case, JonDo running on localhost.)
# forward / 127.0.0.1:4001</pre>
Restart privoxy to enable the changes.

<pre>sudo /etc/init.d/privoxy restart</pre>
Privoxy is now listening on 127.0.0.1:8118. <sup>2</sup>

<font size="-3"> ,, <sup>2</sup> For debugging you can enter this IP/port into Tor Browser as http proxy and try if you can still reach check.torproject.org. Deactivate after testing. </font>

==== Starting ====

Run httpsdnsd. <sup>1</sup> <sup>2</sup> <sup>3</sup> <sup>4</sup>

<font size="-3"> ,, <sup>1</sup> For debugging, kill httpsdnsd and drop the ''--runasdaemon''. <sup>2</sup> Run ''httpsdnsd --help'' or ''man httpsdnsd'' for help. <sup>3</sup> Httpsdnsd will by default listen on localhost port 4053 for DNS queries. <sup>4</sup> ''--https_proxy_port=8118'' will redirect traffic to port 8118, where Privoxy is listening. This is necessary because Tor offers a socks proxy and httpsdnsd requires a http proxy. Privoxy translates from http to socks. </font>

<pre>sudo httpsdnsd --https_proxy_port=8118 --runasdaemon</pre>
Activate the firewall. Shouldn't show any errors.

<pre>sudo ./dns-fw.sh</pre>
==== Using ====

Open a console and switch to anonuser.

<pre>su anonuser</pre>
Resolve DNS.

<pre>nslookup check.torproject.org</pre>
= Footer =

[[include ref=WikiFooter]]

