[[include ref=WikiHeader]]

[TOC]

= Tor Hidden Services - EASY =

== Introduction ==

Be sure to read and understand [https://www.torproject.org/docs/hidden-services.html.en Tor: Hidden Service Protocol] (general information) and [https://www.torproject.org/docs/tor-hidden-service.html.en Configuring Hidden Services for Tor] (standard setup, no isolated proxy) first. Note that hidden services are always only reachable using Tor or tunnel services, such as tor2web, ([https://trac.torproject.org/projects/tor/wiki/doc/tor2web be careful]).

You do not need [https://en.wikipedia.org/wiki/Secure_Sockets_Layer SSL], because [http://www.quora.com/Is-there-an-SSL-equivalent-for-Tor-Hidden-Services connections to Tor hidden services are end-to-end encrypted by default]. <sup>1</sup> This is handy, as you do not have to bother with self singed certificates or certificate authorities.

An adversary can see whether the service (and presumably Tor) is up and running or not.

<font size="-3"> ,, <sup>1</sup> To be exact, only tor-to-tor, see [https://sourceforge.net/p/whonix/wiki/Threat%20Model/#notes-about-end-to-end-security-of-hidden-services Notes about End-to-end security of Hidden Services]. </font>

== Whonix specific ==

You can provide any server service, which relies on TCP. Beware of application level leaks, see [https://sourceforge.net/p/whonix/wiki/Whonix%27s%20Protocol-Leak-Protection%20and%20Fingerprinting-Protection/ Whonix's Protocol-Leak-Protection and Fingerprinting-Protection].

Even if someone hacks your hidden server software (lighttpd, thttpd, apache, etc.), the attacker can not steal your hidden service key or bypass Tor, see [https://sourceforge.net/p/whonix/wiki/Comparison%20with%20Others/#attacks Attack on Whonix]. The key is stored on the Whonix-Gateway. Once you cleaned your Whonix-Workstation, no one can impersonate your hidden service anymore.

== Hosting ANY Hidden Services ==

You can provide '''any''' server service, which relies on TCP. <font size="-3">UDP is not supported by the Tor network.</font>

Below is an ''example'' for a Hidden Webserver. <font size="-3">On the [Voip] page is an example for a Hidden Voip Mumble Server.</font>

== Hidden Webserver ==

=== Setup ===

On your Whonix-Gateway:

Open torrc.

<pre>sudo nano /etc/tor/torrc</pre>
Look for #OptionalFeatureNr.2#. Read the comments, which explain where to find your .onion URL and to backup your hidden service keys. Comment in the following two lines.

<pre>HiddenServiceDir /var/lib/tor/hidden_service/
HiddenServicePort 80 192.168.0.11:80</pre>
Keep care... &quot;HiddenServicePort 80 192.168.0.11:12345&quot; has to be changed to &quot;HiddenServicePort 80 192.168.0.11:80&quot;.

Restart Tor.

<pre>sudo service tor reload</pre>
Reminder: To get your hidden service url.

<pre>## requires root: sudo su
nano /var/lib/tor/hidden_service/hostname</pre>
Reminder: Backup your hidden service key, in case you want to be able to restore it, on another machine, on a newer Whonix-Gateway, after hdd failure, etc.

<pre>## requires root: sudo su
nano /var/lib/tor/hidden_service/private_key</pre>
On your Whonix-Workstation:

Run the following commands to install lighttpd.

<pre>sudo apt-get update
sudo apt-get install lighttpd</pre>
Done.

=== Debugging ===

Check permissions.

<pre>ls -la /var/lib/tor/hidden_service/</pre>
In case you manually restored your hidden_service keys as root, Tor will fail to start. The folder must be owned by debian-tor.

<pre>sudo chown debian-tor:debian-tor /var/lib/tor/hidden_service/</pre>
Note: Tor Browser will allow connections to ''127.0.0.1:80'' but not to ''192.168.0.11:80''.

In Whonix-Workstation try.

<pre>## Circumventing Whonix uwt wget stream isolation wrapper.
/usr/bin/wget 127.0.0.1:80</pre>
Check.

<pre>nano index.html</pre>
In Whonix-Workstation try.

<pre>## Circumventing Whonix uwt wget stream isolation wrapper.
/usr/bin/wget 192.168.0.11:80</pre>
Check.

<pre>nano index.html</pre>
== Tips settings up any hidden service ==

Please test the example Hidden Webserver above first. It helps understanding this in general and will ease debugging.

Quoted from the [https://www.torproject.org/docs/tor-manual.html.en Tor manual]:

<pre>HiddenServiceDir DIRECTORY

Store data files for a hidden service in DIRECTORY. Every hidden service must have a separate
directory. You may use this option multiple times to specify multiple services. DIRECTORY
must be an existing directory.</pre>
Quoted from the [https://www.torproject.org/docs/tor-manual.html.en Tor manual]:

<pre>HiddenServicePort VIRTPORT [TARGET]

Configure a virtual port VIRTPORT for a hidden service. You may use this option multiple
times; each time applies to the service using the most recent hiddenservicedir. By default,
this option maps the virtual port to the same port on 127.0.0.1 over TCP. You may override
the target port, address, or both by specifying a target of addr, port, or addr:port. You
may also have multiple lines with the same VIRTPORT: when a user connects to that VIRTPORT,
one of the TARGETs from those lines will be chosen at random.</pre>
Read the [Security Guide].

= Tor Hidden Services - ADVANCED =

== Notes about End-to-end security of Hidden Services ==

Hidden services are not really &quot;end-to-end&quot; encrypted, they encrypted only Tor to End. (or &quot;Tor to Tor&quot;) The communication between the browser or server and Tor is sent in clear text. This doesn't really constitute a security issue, as localhost (or Workstation to Gateway on an isolated network), is supposed to be secure. But it has some security implications:

With hidden services alone, without TLS enabled, the adversary only needs to compromise Whonix-Gateway to get knowledge of the content of the connection and the clients identity/location. To compromise the content of the connection, the adversary only needs to compromise either the gateway or the workstation.

With hidden services, and TLS enabled, an adversary needs to compromise Whonix-Workstation to gain knowledge of the content of the connection. The adversary would have to compromise Whonix-Gateway as well, to gain knowledge of the client's identity/location.

It is possible to use hidden services and TLS at the same time, i.e. https://****************.onion. There are only a very few hidden services reachable over TLS. For example https://pad.riseup.net/ can be reached over https://ttbmov2dezfs2fln.onion/. But since this only offers benefits to users of Whonix (and other Tor gateway implementations), there is no demand. It would provide some nice defense in depth as it eliminates a single point of failure.

It would open the question, how would the certificate be verified?

That's simple for private sites, where server and clients know each other. They simply verify it over preshared secure channel, for example, a meeting.

And public hidden services? It is unlikely, that certificate authorities will give out certificates for .onion sites. Startssl.com declined, because .onion is no .gTLD, see [https://trac.torproject.org/projects/tor/ticket/6116 Bug #6116: apply for .onion gTLD at IANA]. Although you could try asking other certificate authorities, if they offer SSL certificates for people who can prove that they own a .onion domain. You can prove, that you have control over the domain by editing its contents on their request.

But CAs should not be relied on anyway. See chapter [https://sourceforge.net/p/whonix/wiki/Security/#ssl SSL].

Hidden Services with Whonix are still safer than running Tor and the server software on the same host, see [https://sourceforge.net/p/whonix/wiki/Security/#hidden-services Hidden Services] for more information.

= Footer =

[[include ref=WikiFooter]]

