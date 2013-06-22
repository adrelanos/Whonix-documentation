[[include ref=WikiHeader]]

[TOC]

= Easy =

You can install any additional software packages inside Whonix-Workstation using ''apt-get'', since it's based on Debian.

The Whonix developer adrelanos is really paranoid about security. That's why Whonix was created. One of the main reasons for creating Whonix was to greatly reduce the risk through any (additional) software package not exclusively designed for use with Tor.

Whonix is currently the safest method to run Tor-unsafe applications such as Adobe Flash (see [BrowserPlugins]).

Nevertheless adrelanos can not stop documenting every eventuality in very detail.

This is '''not''' a recommendation against installing additional software.

On the [https://sourceforge.net/p/whonix/wiki/Software/ Software] page you'll find:

* Applications for different tasks, which are already installed on Whonix by default.
* Software recommendations for different tasks.
* Safety advice.
* Installation instructions.

= More Security =

== Introduction ==

Installing additional software...

Advantages:

* Obviously you can install your favorite software packages. Almost any application with a few exceptions listed under [https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO#Howtotorifyspecificprograms impossible to torify].
* You are protected from IP and DNS leaks. (Read above for details.)
* You have some, but no perfect [https://sourceforge.net/p/whonix/wiki/Whonix%27s%20Protocol-Leak-Protection%20and%20Fingerprinting-Protection/ Protocol-Leak Protection and Fingerprinting-Protection].

Disadvantages:

* You should still try to prevent any other [https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO#Protocolleaks protocol leaks] using the [[[https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO|TorifyHOWTO]] (but most of those most are mitigated by using Whonix).
* When you are updating using apt-get, you'll leak which software packages and versions you have installed, see [https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO#Softwareupdaters Software updaters]. This information can not be directly linked to any other activity, such as web browsing, because the Whonix apt-get uwt wrapper forces apt-get to go through it's own circuit. There are still risks for [https://sourceforge.net/p/whonix/wiki/Stream%20Isolation/ correlation] to the same pseudonym. <sup>1</sup> <sup>2</sup>

You should update using the guidelines below &quot;How to safely update using apt-get?&quot;.

Extra care is needed when adding extra custom repositories, especially PPA's (Personal Package Archives). Single developers may be pressured and/or turn malicious more easily than the main repositories.

<font size="-3"> ,, <sup>1</sup> For example, if you announced somewhere, that you a X user and have a specific set of x, y, and z installed, this information may be available to an adversary. If you run apt-get (which goes through it's own circuit) though any exit nodes, mirrors or ISP's controlled by the adversary, it's possible to guess for the adversary, that it's the same pseudonym, which is running it. In that case the adversary gets your list of installed packages, can run stale mirror attack (only if you are using a custom build using Ubuntu, see About Ubuntu), or can try other attacks against apt-get. <sup>2</sup> Another example, if you run a hidden service with a specific set of server software, let's say apache, mediawiki, phpbb, x, y, z... Similar as <sup>1</sup>... </font>

Read [https://sourceforge.net/p/whonix/wiki/Whonix%27s%20Protocol-Leak-Protection%20and%20Fingerprinting-Protection/ Whonix's Protocol-Leak-Protection and Fingerprinting-Protection] first! (Many leaks, such as DNS and IP related leaks do not apply to Whonix; etc.)

The [https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO TorifyHOWTO] contains documentation about [https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO#Protocolleaks protocol leaks] and how to mitigate them.

Also see [https://trac.torproject.org/projects/tor/wiki/doc/TransparentProxyLeaks Transparent Proxy Leaks]. (Mostly Microsoft Windows related.)

== How to install or update with most caution? ==

# Stop all your activities. <sup>2</sup>
# Change your circuit.<sup>1</sup>
# Update using apt-get after a random delay.
# Change your circuit again.<sup>1</sup>
# Continue your activities later with a random delay.

<font size="-3"> ,, <sup>1</sup> One way to do it using Arm (see [https://sourceforge.net/p/whonix/wiki/TorController/ Tor Controller]): Go to your Whonix-Gateway and start &quot;arm&quot;. Press ''m'' for menu, go down to ''New Identity'' and press enter. <sup>2</sup> Maybe not, if you run a hidden service. </font>

= Whonix-Workstation is firewalled =

'''This is just an informational chapter if you are interested in server or other advanced or otherwise uncommon applications.'''

This means:

* does not support incoming connections
** however, if you make an outgoing connections, the following incoming connections are accepted (web browsing, irc, etc. works)
** so called server ports
** or also called open ports
** Ident Protocol / web server listening port is not reachable, unless you explicitly configure it
* you can [https://sourceforge.net/p/whonix/wiki/OptionalConfigurations/#hosting-hidden-services Host hidden services]
* the firewall can be found on the Whonix-Gateway /usr/local/bin/whonix_firewall ([https://github.com/adrelanos/Whonix/blob/stable/whonix_gateway/usr/local/bin/whonix_firewall on github])
* Standard DNS requests on UDP port 53 will be redirected to Tor's DnsPort. If you change the DNS server in /etc/resolv.conf in Whonix-Workstation, this will probable have no effect, since the firewall on Whonix-Gateway will redirect all those requests to Tor's DnsPort. (However, if you tunneling/encrypting DNS request, as per [https://sourceforge.net/p/whonix/wiki/OptionalConfigurations/#secondary-dns-resolver Secondary DNS resolver] (DNSCrypt, httpsdnsd) it will work.)

Also note:

* Tor does not support UDP. This is not an Whonix issue. <sup>1</sup>
* Tor does not support IPv6. This is not an Whonix issue. <sup>1</sup>

<font size="-3"> ,, <sup>1</sup> Perhaps [https://sourceforge.net/p/whonix/wiki/OptionalConfigurations/#onioncat OnionCat with Whonix] can be a suitable workaround. </font>

Whonix's firewall on the Whonix-Gateway is very restrictive. You can make it even more restrictive by activating #OptionalFeatureNr.3# within the firewall script. It's possible to limit, which outgoing ports will be redirected to Tor's TransPort. Depending on what you want to archive, it could be useful to remove all SocksPorts.

= Footer =

[[include ref=WikiFooter]]

