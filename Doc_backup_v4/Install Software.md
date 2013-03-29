[[include ref=WikiHeader]]

[TOC]

# Easy #
You can install any additional software packages inside Whonix-Workstation using *apt-get*, since it's based on Debian.

The Whonix developer adrelanos is really paranoid about security. That's why Whonix was created. One of the main reasons for creating Whonix was to greatly reduce the risk through any (additional) software package not exclusively designed for use with Tor.

Whonix is currently the safest method to run Tor-unsafe applications such as Adobe Flash (see [BrowserPlugins]).

Nevertheless adrelanos can not stop documenting every eventuality in very detail.

This is **not** a recommendation against installing additional software.

On the [Software](https://sourceforge.net/p/whonix/wiki/Software/) page you'll find:

* Applications for different tasks, which are already installed on Whonix by default.
* Software recommendations for different tasks.
* Safety advice.
* Installation instructions.

# More Security #
## Introduction ##
Installing additional software...

Advantages:

* Obviously you can install your favorite software packages. Almost any application with a few exceptions listed under [impossible to torify](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO#Howtotorifyspecificprograms).
* You are protected from IP and DNS leaks. (Read above for details.)
* You have some, but no perfect [Protocol-Leak Protection and Fingerprinting-Protection](https://sourceforge.net/p/whonix/wiki/Whonix%27s%20Protocol-Leak-Protection%20and%20Fingerprinting-Protection/). 

Disadvantages: 

* You should still try to prevent any other [protocol leaks](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO#Protocolleaks) using the [TorifyHOWTO]([https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO) (but most of those most are mitigated by using Whonix).
* When you are updating using apt-get, you'll leak which software packages and versions you have installed, see [Software updaters](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO#Softwareupdaters). This information can not be directly linked to any other activity, such as web browsing, because the Whonix apt-get uwt wrapper forces apt-get to go through it's own circuit. There are still risks for [correlation](https://sourceforge.net/p/whonix/wiki/Stream%20Isolation/) to the same pseudonym. ^1^ ^2^

You should update using the guidelines below "How to safely update using apt-get?".

Extra care is needed when adding extra custom repositories, especially PPA's (Personal Package Archives). Single developers may be pressured and/or turn malicious more easily than the main repositories.

<font size="-3">
,,
^1^ For example, if you announced somewhere, that you a X user and have a specific set of x, y, and z installed, this information may be available to an adversary. If you run apt-get (which goes through it's own circuit) though any exit nodes, mirrors or ISP's controlled by the adversary, it's possible to guess for the adversary, that it's the same pseudonym, which is running it. In that case the adversary gets your list of installed packages, can run stale mirror attack (only if you are using a custom build using Ubuntu, see About Ubuntu), or can try other attacks against apt-get. 
^2^ Another example, if you run a hidden service with a specific set of server software, let's say apache, mediawiki, phpbb, x, y, z... Similar as ^1^...
</font>

Read [Whonix's Protocol-Leak-Protection and Fingerprinting-Protection](https://sourceforge.net/p/whonix/wiki/Whonix%27s%20Protocol-Leak-Protection%20and%20Fingerprinting-Protection/) first! (Many leaks, such as DNS and IP related leaks do not apply to Whonix; etc.)

The [TorifyHOWTO](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO) contains documentation about [protocol leaks](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO#Protocolleaks) and how to mitigate them.

Also see [Transparent Proxy Leaks](https://trac.torproject.org/projects/tor/wiki/doc/TransparentProxyLeaks). (Mostly Microsoft Windows related.)

## How to install or update with most caution? ##
1. Stop all your activities. ^2^ 
2. Change your circuit.^1^ 
3. Update using apt-get after a random delay. 
4. Change your circuit again.^1^ 
5. Continue your activities later with a random delay. 

<font size="-3">
,,
^1^ One way to do it using Arm (see [Tor Controller](https://sourceforge.net/p/whonix/wiki/TorController/)): Go to your Whonix-Gateway and start "arm". Press *m* for menu, go down to *New Identity* and press enter. 
^2^ Maybe not, if you run a hidden service.
</font>

# Whonix-Workstation is firewalled #
**This is just an informational chapter if you are interested in server or other advanced or otherwise uncommon applications.**

This means:

* does not support incoming connections
    * however, if you make an outgoing connections, the following incoming connections are accepted (web browsing, irc, etc. works)
    * so called server ports
    * or also called open ports
    * Ident Protocol / web server listening port is not reachable, unless you explicitly configure it
* you can [Host hidden services](https://sourceforge.net/p/whonix/wiki/OptionalConfigurations/#hosting-hidden-services)
* the firewall can be found on the Whonix-Gateway /usr/local/bin/whonix_firewall ([on github](https://github.com/adrelanos/Whonix/blob/stable/whonix_gateway/usr/local/bin/whonix_firewall))
* Standard DNS requests on UDP port 53 will be redirected to Tor's DnsPort. If you change the DNS server in /etc/resolv.conf in Whonix-Workstation, this will probable have no effect, since the firewall on Whonix-Gateway will redirect all those requests to Tor's DnsPort. (However, if you tunneling/encrypting DNS request, as per [Secondary DNS resolver](https://sourceforge.net/p/whonix/wiki/OptionalConfigurations/#secondary-dns-resolver) (DNSCrypt, httpsdnsd) it will work.)

Also note:

* Tor does not support UDP. This is not an Whonix issue. ^1^
* Tor does not support IPv6. This is not an Whonix issue. ^1^

<font size="-3">
,,
^1^ Perhaps [OnionCat with Whonix](https://sourceforge.net/p/whonix/wiki/OptionalConfigurations/#onioncat) can be a suitable workaround.
</font>

Whonix's firewall on the Whonix-Gateway is very restrictive. You can make it even more restrictive by activating #OptionalFeatureNr.3# within the firewall script. It's possible to limit, which outgoing ports will be redirected to Tor's TransPort. Depending on what you want to archive, it could be useful to remove all SocksPorts.

# Footer #
[[include ref=WikiFooter]]