[[include ref=WikiHeader]]

[TOC]

= Stream Isolation =

== Introduction ==

If you do not explicitly take action against this and install custom applications, you risk, that different activities, let's say Web (Chromium or similar) or IRC (mIRC or similar) go through the Tor same circuit and exit node. Even though, you would still be anonymous, i.e. the Tor exit node would still not know your real IP/location, they can easily correlate those activities issued by different applications to the same pseudonym.

The following graphic illustrates, the difference of using Tor SocksPort's compared to using Tor's TransPort. Using dedicated SocksPort's per application results in taking different routes through the Tor network per application. Not necessarily all nodes (first, second, third) get replaced by Tor. Sometimes just the first, sometimes just the second, sometimes just the third, and sometimes multiple nodes change.

[[Image:http://whonix.sourceforge.net/pictures/stream_isolation.1.0.jpg|frame|none|alt=|caption Stream Isolation Graphic]]

Whonix 0.2.1 and above implement protection against ''identity correlation through circuit sharing'', however, for better privacy, you are still advised understand a bit of the technical background. Since Tor version 0.2.3, different Socks,- Dns-, or TransPorts go through different circuits, therefore preventing ''identity correlation''. Whonix configures most applications, that come preinstalled with Whonix, to use different SocksPort, thus no ''identity correlation'' is at risk. Whonix uses either socks proxy settings to direct various applications to different SocksPorts or uwt (more information below).

Any other traffic (i.e. custom installed applications, misc applications, such as ''nslookup'', go through Tor's Dns-, and/or TransPort (can be optionally disabled, see below).

Applications in Whonix 0.2.1 and above configured to prevent ''identity correlation through circuit sharing'':

<table>
<thead>
<tr class="header">
<th align="left"></th>
<th align="left">pre-installed</th>
<th align="left">pre-configured</th>
<th align="left">type</th>
<th align="left">port</th>
<th align="left">instructions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Tor Browser</td>
<td align="left">yes</td>
<td align="left">yes</td>
<td align="left">socks proxy settings</td>
<td align="left">9100</td>
<td align="left">[TorBrowser]</td>
</tr>
<tr class="even">
<td align="left">XChat</td>
<td align="left">yes</td>
<td align="left">yes</td>
<td align="left">socks proxy settings</td>
<td align="left">-</td>
<td align="left">[Chat]</td>
</tr>
<tr class="odd">
<td align="left">Thunderbird with TorBirdy</td>
<td align="left">no</td>
<td align="left">yes</td>
<td align="left">socks proxy settings</td>
<td align="left">-</td>
<td align="left">[https://sourceforge.net/p/whonix/wiki/E-Mail Mozilla Thunderbird with TorBirdy]</td>
</tr>
<tr class="even">
<td align="left">Instant Messenger</td>
<td align="left">no</td>
<td align="left">no</td>
<td align="left">socks proxy settings</td>
<td align="left">port prepared, IP 192.168.0.10, port 9103</td>
<td align="left">[Chat]</td>
</tr>
<tr class="odd">
<td align="left">apt-get</td>
<td align="left">yes</td>
<td align="left">yes</td>
<td align="left">uwt wrapper</td>
<td align="left">-</td>
<td align="left">-</td>
</tr>
<tr class="even">
<td align="left">gpg</td>
<td align="left">yes</td>
<td align="left">yes</td>
<td align="left">uwt wrapper</td>
<td align="left">-</td>
<td align="left">-</td>
</tr>
<tr class="odd">
<td align="left">ssh</td>
<td align="left">yes</td>
<td align="left">yes</td>
<td align="left">uwt wrapper</td>
<td align="left">-</td>
<td align="left">-</td>
</tr>
<tr class="even">
<td align="left">git</td>
<td align="left">no</td>
<td align="left">yes</td>
<td align="left">uwt wrapper</td>
<td align="left">-</td>
<td align="left">-</td>
</tr>
<tr class="odd">
<td align="left">[https://sourceforge.net/p/whonix/wiki/Dev_timesync/ htpdate]</td>
<td align="left">yes</td>
<td align="left">yes</td>
<td align="left">socks proxy settings</td>
<td align="left">-</td>
<td align="left">-</td>
</tr>
<tr class="even">
<td align="left">wget</td>
<td align="left">yes</td>
<td align="left">yes</td>
<td align="left">uwt wrapper</td>
<td align="left">-</td>
<td align="left">-</td>
</tr>
<tr class="odd">
<td align="left">curl</td>
<td align="left">yes</td>
<td align="left">yes</td>
<td align="left">uwt wrapper</td>
<td align="left">-</td>
<td align="left">-</td>
</tr>
<tr class="even">
<td align="left">whonixcheck</td>
<td align="left">yes</td>
<td align="left">yes</td>
<td align="left">socks proxy settings</td>
<td align="left">-</td>
<td align="left">-</td>
</tr>
<tr class="odd">
<td align="left">BitCoin</td>
<td align="left">no</td>
<td align="left">no</td>
<td align="left">socks proxy settings</td>
<td align="left">port prepared, IP 192.168.0.10, port 9111</td>
<td align="left">[Money]</td>
</tr>
<tr class="even">
<td align="left">privoxy</td>
<td align="left">no</td>
<td align="left">no</td>
<td align="left">socks proxy settings</td>
<td align="left">port prepared, IP 192.168.0.10, port 9112</td>
<td align="left">-</td>
</tr>
<tr class="odd">
<td align="left">privoxy</td>
<td align="left">no</td>
<td align="left">no</td>
<td align="left">socks proxy settings</td>
<td align="left">port prepared, IP 192.168.0.10, port 9113</td>
<td align="left">-</td>
</tr>
<tr class="even">
<td align="left">torbrowser update script</td>
<td align="left">yes</td>
<td align="left">yes</td>
<td align="left">socks proxy settings</td>
<td align="left">-</td>
<td align="left">[TorBrowser]</td>
</tr>
<tr class="odd">
<td align="left">apt-cacher-ng</td>
<td align="left">no</td>
<td align="left">no</td>
<td align="left">uwt wrapper</td>
<td align="left">-</td>
<td align="left">helper script with comments prepared, see ''/usr/local/bin/apt-cacher-ng_uwt''</td>
</tr>
<tr class="even">
<td align="left">TorChat</td>
<td align="left">no</td>
<td align="left">yes</td>
<td align="left">settings, socks proxy settings, connects only to hidden services</td>
<td align="left">-</td>
<td align="left">[Chat]</td>
</tr>
<tr class="odd">
<td align="left">mixmaster</td>
<td align="left">yes</td>
<td align="left">yes</td>
<td align="left">settings (connects only to hidden services)</td>
<td align="left">-</td>
<td align="left">[Mixmaster]</td>
</tr>
<tr class="even">
<td align="left">mixmaster-update</td>
<td align="left">yes</td>
<td align="left">yes</td>
<td align="left">uwt wrapper</td>
<td align="left">-</td>
<td align="left">[Mixmaster]</td>
</tr>
</tbody>
</table>

Whonix 0.6.2 and above: KDE application wide proxy settings (no KDE applications with network activity pre-installed, pre-configured socks proxy settings, port 9122)

Whonix 0.6.2 and above: GNOME application wide proxy settings (no GNOME applications with network activity pre-installed, [https://sourceforge.net/p/whonix/wiki/Dev_GNOME/ not pre-configured], port prepared, port 9123)

The required socks proxy settings were setup by the Whonix build scripts. uwt wrappers and are located on Whonix-Gateway and on Whonix-Workstation under ''/usr/local/bin/''. [https://trac.torproject.org/projects/tor/wiki/doc/torsocks uwt] is a wrapper around torsocks, which is also already installed to /usr/local/bin/uwt.

* Example, each time you run a uwt wrapped application, i.e. simply type ''apt-get'' in console, the uwt wrapper /usr/local/bin/apt-get will run. It adds uwt before apt-get. For curiosity check ''nano /usr/local/bin/apt-get''. The uwt wrapper then runs ''/usr/local/bin/uwt /usr/bin/apt-get''. That is also the case for all other uwt wrapped applications.
* If you ever want or must run a uwt wrapped application without uwt, do not run for example ''apt-get'' in console, do run ''/usr/bin/apt-get''. Use cases could be if you connect to localhost. If you know what you are doing, you should also be able to deactivate any uwt wrappers you dislike with ''chmod -x /usr/bin/apt-get''.
* When running ''/usr/bin/apt-get'' directly it goes through Tor's DnsPort and through Tor's TransPort and not through it's own SocksPort.
* uwt looks if the command contains the words ''localhost'' or ''127.0.0.1'', if that is the case, uwt will not be used. The command will be run without uwt. Thus, if a localhost connection is falsely detected it will leak, but only leak through Tor's DnsPort and through Tor's TransPort, which should be ok.

Isolate by destination address: Let's assume SSH goes over port 22 and you want to connect to different SSH servers and do not want an observer to be able to correlate that activity to the same pseudonym. If the SSH servers run on different IP's isolate by destination address might help.

Isolate by destination port: This doesn't seem to be useful for anything in Whonix, applications using different protocols (and therefore different ports) are already isolated through using different SOCKSPorts.

Isolate by destination port doesn't really achieve anything for web browsing: [https://lists.torproject.org/pipermail/tor-talk/2012-May/024403.html tor-talk Tor's stream isolation features defaults].

For more information about stream isolation refer to the Tor manual.

* [https://www.torproject.org/docs/tor-manual.html.en Tor stable manual]
* [https://www.torproject.org/docs/tor-manual-dev.html.en Tor alpha manual]

=== Tor Browser ===

Different tabs and websites in Tor Browser are not isolated until Tor upstream feature &quot;[https://trac.torproject.org/projects/tor/ticket/3455 Tor Browser should set SOCKS username for a request based on referer]&quot; gets implemented. A limited workarounds are described below.

=== Custom Software ===

If you install custom software on Whonix-Workstation, and want to prevent ''identity correlation through circuit sharing'' (which you should do), you have to manually configure them. This is not a Whonix specific problem. <sup>1</sup> <sup>2</sup> <sup>3</sup>

Read also [https://sourceforge.net/p/whonix/wiki/Install%20Software/ Software installation on Whonix-Workstation].

=== Hidden Services ===

[https://lists.torproject.org/pipermail/tor-talk/2012-September/025432.html Hidden services are automatically separated from each other.]

=== Footnotes ===

<font size="-3"> ,, <sup>1</sup> If you used to use only one SocksPort with the [https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO common torification methods], the [https://lists.torproject.org/pipermail/tor-talk/2012-March/023535.html same thing happened]. <sup>2</sup> Also the current (March 2012) [https://www.torproject.org/projects/torbrowser.html.en Tor Browser Bundle] is affected, all Firefox Tabs can be correlated to the same identity until the circuit is automatically changed by Tor. <sup>3</sup> [https://tails.boum.org/ Tails], which is officially listed on torproject.org was [https://lists.torproject.org/pipermail/tor-talk/2012-March/023535.html also affected]. Tails done [https://tails.boum.org/todo/separate_Tor_streams/ Todo] item. </font>

== How to mitigate identity correlation ==

=== Basic Protection ===

Most applications which come with Whonix 0.2.1 and above are already configured to prevent ''identity correlation through circuit sharing'', you really should read the introduction above.

The only traffic going through TransPort by default is [whonixcheck] when testing the TransPort. If that is of concern to you, it can be disabled in whonixcheck. Just comment out the &quot;''check_tor &quot;TransPort&quot;''&quot; in ''/usr/local/bin/whonixcheck'' in that case.

All custom installed application's TCP traffic is routed through Tor's TransPort and all their DNS requests through Tor's DnsPort. This means different activities or &quot;identities&quot; in different applications (say browser, IRC, email) end up being routed through the same circuit, thus ''identity correlation'' is at risk.

To protect against this, you have to set up per-application SOCKS ports in Whonix-Gateway.

On Whonix-Gateway in ''/etc/tor/torrc'' ([https://github.com/adrelanos/Whonix/blob/stable/whonix_gateway/etc/tor/torrc on github]) are already a lot custom socks ports prepared for custom installed applications:

* Without IsolateDestAddr and without IsolateDestPort: SocksPort 192.168.0.10:9152 to 9159
* With IsolateDestAddr, but without IsolateDestPort: SocksPort 192.168.0.10:9160 to 9169
* Without IsolateDestAddr, but with IsolateDestPort: SocksPort: 192.168.0.10:9170 to 9179
* With IsolateDestAddr and with IsolateDestPort: SocksPort: 192.168.0.10:9180 to 9189
* If they those are not enough, you can add your own ones.

You can point your applications, where you want to prevent ''identity correlation though circuit sharing'', to those SocksPorts. Each custom installed application has to be torified, for directions how to do that use the [https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO Torify HOWTO].

Additional comments regarding the Torify HOWTO:

* Warnings about protocol related warnings you must honor. You are still better off with Whonix, as it offers best possible [https://sourceforge.net/p/whonix/wiki/Whonix%27s%20Protocol-Leak-Protection%20and%20Fingerprinting-Protection/ Protocol-Leak-Protection and Fingerprinting-Protection].
* Whonix's setup provides protection against IP leaks through [https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO#Protocolleaks protocol leaks].
* If you do not correctly torify, no connections will be possible.
* If you redirect more than one application to the same SocksPort, ''identity correlation'' is at risk.
* DNS related [https://trac.torproject.org/projects/tor/wiki/doc/TorFAQ#IkeepseeingthesewarningsaboutSOCKSandDNSandinformationleaks.ShouldIworry warnings] still apply, though to a lesser extent - an attack could only make correlations but still couldn't figure out your IP. You can prevent that, be out commenting (# in front) DnsPort in /etc/tor/torrc on the Whonix-Gateway and by removing the DNS redirection firewall rule from /usr/local/bin/whonix_firewall. ([https://github.com/adrelanos/Whonix/blob/stable/whonix_gateway/usr/local/bin/whonix_firewall on github])
** Do not use a [https://trac.torproject.org/projects/tor/wiki/doc/SupportPrograms#DNS local DNS resolver], as all DNS requests would be executed by the same circuit.
* Other leaks, such as applications not honoring the proxy settings / wrapper, ICMP or UDP leaks do not apply to Whonix.

=== Better Protection ===

For best protection against ''identity correlation'':

Read the advice above and on Whonix-Gateway:

Deactivate KDE / GNOME - application wide proxy settings...

* Whonix 0.6.2 and above: Because those proxy settings are not application specific, but rather force all KDE / GNOME applications through the same SocksPort (no KDE / GNOME applications which use the internet preinstalled by default), deactivating those KDE / GNOME - wide proxy settings gives better control about stream isolation.

To deactivate TransPort and DnsPort...

* Set ''WORKSTATION_TRANSPARENT_TCP=0'' in ''/usr/local/bin/whonix_firewall'' ([https://github.com/adrelanos/Whonix/blob/stable/whonix_gateway/usr/local/bin/whonix_firewall on github])
* Set ''WORKSTATION_TRANSPARENT_DNS=0'' in in ''/usr/local/bin/whonix_firewall''
* Reload whonix_firewall (''sudo /usr/local/bin/whonix_firewall'') or simply reboot.

Although not strictly required, you could additionally, comment out:

* TransPort in ''/etc/tor/torrc''
* DnsPort in ''/etc/tor/torrc''
* And restart Tor. (''sudo service tor restart'')

This will disable transparent proxying. All applications not configured to use a SocksPort or forced to use a SocksPort (use uwt) will not be able to establish connections. This is the only way to ensure, that different SocksPorts are used and that also DNS is remotely resolved through that SocksPort.

=== Total protection ===

Total protection is only possible, if you honor the advice above and only use one application per session and always revert to a fresh snapshot or use [http://sourceforge.net/p/whonix/wiki/TorBrowser/#more-than-one-tor-browser-in-whonix more than one Whonix-Workstation]. [Multiple Whonix-Workstations] (using different internal IP's) are automatically separated by Tor (IsolateClientAddr is Tor's default).

=== Limited workarounds for Tor Browser ===

==== Second Tor Browser with its own SocksPort ====

A good option would be to install a second browser and configure it to use its own SocksPort, see [http://sourceforge.net/p/whonix/wiki/TorBrowser/#more-than-one-tor-browser-in-whonix More than one Tor Browser in Whonix].

==== IsolateDestAddr and IsolateDestPort for Tor Browser (Recommend against!) ====

'''(Recommend against!)'''

As a workaround you could enable IsolateDestAddr and IsolateDestPort for the Tor Browser.

This comes at great performance costs, especially for websites with lots of 3rd party content. It will not isolate connections to different websites on a shared server and it will create new circuits for every IP address you connect to (e.g. it will isolate subdomains if they use different IPs). It will also let you stand out more from other Tor Browser users, because almost no one is using it that way. Generally, for these reasons you should not enable this feature. Instead close the browser and get a &quot;new identity&quot; through arm on the gateway if you want to separate activities inside Tor Browser.

On Whonix-Gateway open ''/etc/tor/torrc''.

<pre>sudo nano /etc/tor/torrc</pre>
Comment out.

<pre>#SocksPort 192.168.0.10:9100</pre>
Comment in.

<pre>SocksPort 192.168.0.10:9100 IsolateDestAddr IsolateDestPort</pre>
== Development ==

Tests.

Applications which internally use curl.

<pre>sudo update-command-not-found

sudo update-flashplugin-nonfree --install --verbose</pre>
Applications which is uwt wrapped itself and internally uses ssh.

<pre>git push origin master</pre>
== Sources ==

<font size=-3>

* [https://gitweb.torproject.org/torspec.git/blob/HEAD:/proposals/171-separate-streams.txt Separate streams across circuits by connection metadata]
* [https://lists.torproject.org/pipermail/tor-talk/2012-March/023496.html tor-talk Operating system updates / software installation behind Tor Transparent Proxy]
* [https://lists.torproject.org/pipermail/tor-talk/2012-March/023536.html tor-talk Awareness for identity correlation through circuit sharing is almost zero.]
* [https://lists.torproject.org/pipermail/tor-talk/2012-May/024401.html tor-talk Tor's stream isolation features defaults Question]
* [https://lists.torproject.org/pipermail/tor-talk/2012-May/024403.html tor-talk Tor's stream isolation features defaults Answer]
* [https://mailman.boum.org/pipermail/tails-dev/2012-August/001422.html Tails-dev separate Tor streams]
* [https://tails.boum.org/todo/separate_Tor_streams/ Tails separate Tor streams]
* [https://mailman.boum.org/pipermail/tails-dev/2012-August/001532.html Tails-dev Please review Tails stream isolation plans]
* [https://tails.boum.org/contribute/design/stream_isolation/ Tails Design: Tor stream isolation]

</font>

= Footer =

<font size=-3> Stream Isolation Graphic has been contributed by: Cuan Knaggs – graphic and web design [http://revolver.za.net/ revlover] print media – web design – web development – cms – e-commerce </font>

[[include ref=WikiFooter]]

