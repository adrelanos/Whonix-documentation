[[include ref=WikiHeader]]

[TOC]

# Secondary DNS Resolver #
## Introduction ##
By Whonix default, Tor is used for DNS resolution. If you suspect a Tor exit node to tamper with DNS, you can get a second opinion from another non-Tor DNS server. This may also be useful, in special cases  if you want to resolve types of DNS over Tor, which are unsupported by Tor itself, such as MX <font size="-3">(required for some [Mixmaster] servers over Tor)</font> or DNSSEC.

It's recommend against to use non-Tor DNS resolvers for an extended amount of time. Although it's technically possible to completely replace DNS resolution (not using Tor for DNS resolution anymore), it's recommend against. That would add too much power to a single DNS server. Using a permanent DNS server is recommend against just as using a permanent Tor exit node is recommend against.

Note, that even if you correctly set up all settings, it might happen that this won't work. Sometimes Tor or the DNS server causes a timeout. This gets even worse, when you additionally tunnel the DNS request through an additional proxy (for example: Tor -> JonDonym -> DNS server).

Read first: [Stream Isolation](https://sourceforge.net/p/whonix/wiki/Stream%20Isolation/).

Required knowledge: Difference between encryption and authentication.

In the chapters below are examples how to use authenticated DNS ([DNSSEC](https://en.wikipedia.org/wiki/Domain_Name_System_Security_Extensions)) or encrypted DNS (DNSCrypt or httpsdnsd). I haven't found any public DNS resolvers supporting both, encryption and authentication.

Note that most applications, such as [Tor Browser](https://sourceforge.net/p/whonix/wiki/TorBrowser/), will **not** *automatically* profit from setting up an alternative DNS resolver. This is because applications in Whonix are configured to use SocksPort instead of Trans- or DnsPort, see [Stream Isolation](https://sourceforge.net/p/whonix/wiki/Stream%20Isolation/) for details. Another reason is, that most applications do not yet make use of authenticated DNS (DNSSEC). However, you could use encrypted DNS when deconfiguring SocksPort and when using system resolver (TransPort).

## Authenticated DNS over Tor ##
### DNSSEC over Tor ###
#### Example with CZ.NIC Labs DNS resolver ####
<font size="-3">
[source for this chapter: CZ NIC LABS](https://labs.nic.cz/page/993/dnssec-validation-over-tor--linux-/)
</font>

The *CZ.NIC Labs DNS resolver* has been chosen as an example. Feel free to use and other DNS resolver at your own choice.

##### Installation #####
Install [unbound](https://unbound.net/) and [socat](http://www.dest-unreach.org/socat/).

    sudo apt-get install unbound socat

Open */etc/unbound/unbound.conf*.

    sudo nano /etc/unbound/unbound.conf

*Add* the following lines.

    #tcp-upstream goes under "server:" section
        tcp-upstream: yes

    #put forward-zone somewhere at the end of file
    forward-zone:
        name: "."
        forward-addr: 0.0.0.0@5353

##### Starting #####
Open a terminal and start socat.

    socat TCP4-LISTEN:5353,bind=localhost,reuseaddr,fork SOCKS4A:192.168.0.10:217.31.204.130:53,socksport=9150

Open another terminal tab and restart unbound.

    sudo service unbound restart

##### Using #####
Test with dig.

    dig +dnssec nic.cz @localhost

Please refer to upstream documentation on how to interpret the DNSSEC test results.

## Encrypted DNS over Tor ##
### Introduction ###
This is different from DNSSEC.

### DNSCrypt by OpenDNS ###
Although the official [DNSCrypt website](https://www.opendns.com/technology/dnscrypt/) states, that a Linux version does not exit, this [blog post](http://www.webupd8.org/2012/02/encrypt-dns-traffic-in-linux-with.html) suggests there is one.

This has nothing to do with [DNSSEC](https://en.wikipedia.org/wiki/Domain_Name_System_Security_Extensions), the differences of DNSSEC and DNSCrypt are well explained on the [DNSCrypt website](https://www.opendns.com/technology/dnscrypt/).

These instructions completely replace Tor's DNS resolver with opendns's dnscrypt for all users and the whole system. Not recommend for a longer amount of time, see warning above. Some hints are included how to do it only for a specific user account.

(1). Download the [dnscrypt source code](https://github.com/opendns/dnscrypt-proxy/downloads) and unpack. You have to compile it. Get into the dnscrypt directory *cd dnscrypt-proxy-...*. Configure *./configure*, make *make*.

(2). Start dnscrypt-proxy. ^1^ ^2^ ^3^ ^4^ ^5^ ^6^

    sudo dnscrypt-proxy --tcp-only

<font size="-3">
,,
^1^ *--tcp-only* is required since Tor does not support UDP. The UDP DNS request will immediately get truncated reply and a RFC-compliant resolver should repeat same query via TCP in this case. This is the case for Ubuntu's default DNS resolver. You can get some more information on UDP/TCP/DNS on the unrelated [redsocks](http://darkk.net.ru/redsocks/) website.
^2^ To start it later in background (after debugging) add *--daemonize*.
^3^ *--help* to see all options.
^4^ Start up takes a few seconds "INFO Generating a new key pair", this is normal, wait. Until it's done, DNS will not work.
^5^ *--user=username* can and should be used to start the dnscrypt-proxy under a specific user account.
^6^ Since this instructions completely replace Tor's DNS resolver with opendns's dnscrypt for all users and the whole system, you could add *--local-port=5800* to let dnscrypt-proxy listen on port 5800. You would be able to add iptables rules to redirect only the DNS requests of a specific user account to opendns's dnscrypt, you can get some hints how to do that in the *httpsdnsd by JonDos* chapter below, which would be a very similar setup.
</font>

(3). Edit your resolv.conf *nano /etc/resolv.conf*, comment out everything and add *nameserver 127.0.0.1*.

(4). Check if it's working, there are several [test pages](https://www.opendns.com/support/article/64) on opendns.com.

(5). To shut it down you can use *sudo killall dnscrypt-proxy* and don't forget to revert the changes in /etc/resolv.conf.

### httpsdnsd by JonDos ###
#### Introduction ####
Source: [anonymous-proxy-servers.net](https://anonymous-proxy-servers.net/en/help/transocks.html) and also use it as a more verbose tutorial, but keep in mind that their tutorial is JonDonym specific, while this tutorial is Tor specific.

Everything inside your Whonix-Workstation.

#### Installation ####
Install dependencies.

    sudo apt-get install libnet-ssleay-perl libnet-server-perl libnet-dns-perl libxml-simple-perl liblog-log4perl-perl

Download httpsdnsd. (See source above in case download link changed.)

    wget https://anonymous-proxy-servers.net/downloads/httpsdnsd.tar.bz2

Unpack.

    .    

Go into the httpsdnsd folder.

    cd httpsdnsd

Install httpsdnsd. ^1^

<font size="-3">
,, ^1^ (It contains also a uninstall.sh, if you want to uninstall it later.)
</font>

    sudo install.sh

Add a new user for httpsdnsd.

    sudo adduser --system --disabled-password --group httpsdns_daemon

Editing /etc/resolv.conf is not required. (You still could out comment everything against DNS leaks.)

Create a firewall script.

    nano dns-fw.sh

Insert these firewall rules.

    # Flush old rules
    iptables -F
    iptables -t nat -F
    iptables -X

    # Redirect DNS traffic to httpdnsd.
    iptables -t nat -A OUTPUT -p udp -m owner --uid-owner anonuser --dport 53 -j REDIRECT --to-ports 4053

    # Accept connections to the httpdnsd.
    iptables -t filter -A OUTPUT -p udp -m owner --uid-owner anonuser --dport 4053 -j ACCEPT

    # Reject all other traffic for anonuser.
    iptables -t filter -A OUTPUT ! -o lo -m owner --uid-owner anonuser -j REJECT

Install Privoxy. ^1^ 

<font size="-3">
,,
^1^ [torproject.org Wiki Version 95](https://trac.torproject.org/projects/tor/wiki/doc/TorBOX/OptionalConfigurations?version=95#httpsdnsdbyJonDos) of this site contains a working example using Polipo. Changed later to Privoxy, because Privoxy can be useful for other tasks as well. (Incoming: TransPort, http proxy; forwarding: http and socks.)
</font>

    sudo apt-get install privoxy

Open the privoxy configuration file.

    nano /etc/privoxy/config

Add the following to your privoxy configuration file.

    # Theoretically you can tunnel through any
    # http or socks proxy. Local or remote proxy.
    # Inside Whonix-Workstation, due to design,
    # everything will be tunneled through Tor first.
    
    # Using Tor's socks5 proxy, running on Whonix-Gateway. 
    # Change the port, see above...
    forward-socks5 / 192.168.0.10:9112 .

    # Another example using a http proxy.
    # (In this case, JonDo running on localhost.)
    # forward / 127.0.0.1:4001

Restart privoxy to enable the changes.

    sudo /etc/init.d/privoxy restart

Privoxy is now listening on 127.0.0.1:8118. ^2^ 

<font size="-3">
,,
^2^ For debugging you can enter this IP/port into Tor Browser as http proxy and try if you can still reach check.torproject.org. Deactivate after testing.
</font>

#### Starting ####
Run httpsdnsd. ^1^ ^2^ ^3^ ^4^

<font size="-3">
,,
^1^ For debugging, kill httpsdnsd and drop the *--runasdaemon*.
^2^ Run *httpsdnsd --help* or *man httpsdnsd* for help. 
^3^ Httpsdnsd will by default listen on localhost port 4053 for DNS queries.
^4^ *--https_proxy_port=8118* will redirect traffic to port 8118, where Privoxy is listening. This is necessary because Tor offers a socks proxy and httpsdnsd requires a http proxy. Privoxy translates from http to socks. 
</font>

    sudo httpsdnsd --https_proxy_port=8118 --runasdaemon

Activate the firewall. Shouldn't show any errors.

    sudo ./dns-fw.sh

#### Using ####
Open a console and switch to anonuser.

    su anonuser

Resolve DNS.

    nslookup check.torproject.org

# Footer #
[[include ref=WikiFooter]]