[[include ref=WikiHeader]]

[TOC]

# Stream Isolation #
## Introduction ##
If you do not explicitly take action against this and install custom applications, you risk, that different activities, let's say Web (Chromium or similar) or IRC (mIRC or similar) go through the Tor same circuit and exit node. Even though, you would still be anonymous, i.e. the Tor exit node would still not know your real IP/location, they can easily correlate those activities issued by different applications to the same pseudonym.

The following graphic illustrates, the difference of using Tor SocksPort's compared to using Tor's TransPort. Using dedicated SocksPort's per application results in taking different routes through the Tor network per application. Not necessarily all nodes (first, second, third) get replaced by Tor. Sometimes just the first, sometimes just the second, sometimes just the third, and sometimes multiple nodes change.

![Stream Isolation Graphic](http://whonix.sourceforge.net/pictures/stream_isolation.1.0.jpg)

Whonix 0.2.1 and above implement protection against *identity correlation through circuit sharing*, however, for better privacy, you are still advised understand a bit of the technical background. Since Tor version 0.2.3, different Socks,- Dns-, or TransPorts go through different circuits, therefore preventing *identity correlation*. Whonix configures most applications, that come preinstalled with Whonix, to use different SocksPort, thus no *identity correlation* is at risk. Whonix uses either socks proxy settings to direct various applications to different SocksPorts or uwt (more information below).

Any other traffic (i.e. custom installed applications, misc applications, such as *nslookup*, go through Tor's Dns-, and/or TransPort (can be optionally disabled, see below).

Applications in Whonix 0.2.1 and above configured to prevent *identity correlation through circuit sharing*:


| | pre-installed | pre-configured | type | port | instructions
------------- |  ------------- | ------------- | ------------- | ------------- | -------------
Tor Browser | yes  | yes | socks proxy settings | 9100 | [TorBrowser]
XChat | yes | yes | socks proxy settings | - | [Chat]
Thunderbird with TorBirdy | no | yes | socks proxy settings | - | [Mozilla Thunderbird with TorBirdy](https://sourceforge.net/p/whonix/wiki/E-Mail)
Instant Messenger | no | no | socks proxy settings | port prepared, IP 192.168.0.10, port 9103 | [Chat]
apt-get | yes | yes | uwt wrapper | - | -
gpg | yes | yes | uwt wrapper | - | -
ssh | yes | yes | uwt wrapper | - | -
git | no | yes | uwt wrapper | - | -
[htpdate](https://sourceforge.net/p/whonix/wiki/Dev_timesync/) | yes | yes | socks proxy settings | - | -
wget | yes | yes | uwt wrapper | - | -
curl | yes | yes | uwt wrapper | - | -
whonixcheck | yes | yes | socks proxy  settings | - | -
BitCoin | no | no | socks proxy settings | port prepared, IP 192.168.0.10, port 9111 | [Money]
privoxy | no | no | socks proxy settings | port prepared, IP 192.168.0.10, port 9112 | -
privoxy | no | no | socks proxy settings | port prepared, IP 192.168.0.10, port 9113 | -
torbrowser update script | yes | yes | socks proxy settings | - | [TorBrowser]
apt-cacher-ng | no | no | uwt wrapper | - | helper script with comments prepared, see */usr/local/bin/apt-cacher-ng_uwt*
TorChat | no | yes | settings, socks proxy settings, connects only to hidden services | - | [Chat]
mixmaster | yes | yes | settings (connects only to hidden services) | - | [Mixmaster]
mixmaster-update | yes | yes | uwt wrapper | - | [Mixmaster]

Whonix 0.6.2 and above: KDE application wide proxy settings (no KDE applications with network activity pre-installed, pre-configured socks proxy settings, port 9122)

Whonix 0.6.2 and above: GNOME application wide proxy settings (no GNOME applications with network activity pre-installed, [not pre-configured](https://sourceforge.net/p/whonix/wiki/Dev_GNOME/), port prepared, port 9123)

The required socks proxy settings were setup by the Whonix build scripts. uwt wrappers and are located on Whonix-Gateway and on Whonix-Workstation under */usr/local/bin/*. [uwt](https://trac.torproject.org/projects/tor/wiki/doc/torsocks) is a wrapper around torsocks, which is also already installed to /usr/local/bin/uwt.

* Example, each time you run a uwt wrapped application, i.e. simply type *apt-get* in console, the uwt wrapper /usr/local/bin/apt-get will run. It adds uwt before apt-get. For curiosity check *nano /usr/local/bin/apt-get*. The uwt wrapper then runs */usr/local/bin/uwt /usr/bin/apt-get*. That is also the case for all other uwt wrapped applications.
* If you ever want or must run a uwt wrapped application without uwt, do not run for example *apt-get* in console, do run */usr/bin/apt-get*. Use cases could be if you connect to localhost. If you know what you are doing, you should also be able to deactivate any uwt wrappers you dislike with *chmod -x /usr/bin/apt-get*.
* When running */usr/bin/apt-get* directly it goes through Tor's DnsPort and through Tor's TransPort and not through it's own SocksPort.
* uwt looks if the command contains the words *localhost* or *127.0.0.1*, if that is the case, uwt will not be used. The command will be run without uwt. Thus, if a localhost connection is falsely detected it will leak, but only leak through Tor's DnsPort and through Tor's TransPort, which should be ok.

Isolate by destination address:
Let's assume SSH goes over port 22 and you want to connect to different SSH servers and do not want an observer to be able to correlate that activity to the same pseudonym. If the SSH servers run on different IP's isolate by destination address might help.

Isolate by destination port:
This doesn't seem to be useful for anything in Whonix, applications using different protocols (and therefore different ports) are already isolated through using different SOCKSPorts.

Isolate by destination port doesn't really achieve anything for web browsing: [tor-talk Tor's stream isolation features defaults](https://lists.torproject.org/pipermail/tor-talk/2012-May/024403.html).

For more information about stream isolation refer to the Tor manual.

 * [Tor stable manual](https://www.torproject.org/docs/tor-manual.html.en)
 * [Tor alpha manual](https://www.torproject.org/docs/tor-manual-dev.html.en)

### Tor Browser ###
Different tabs and websites in Tor Browser are not isolated until Tor upstream feature "[Tor Browser should set SOCKS username for a request based on referer](https://trac.torproject.org/projects/tor/ticket/3455)" gets implemented. A limited workarounds are described below.

### Custom Software ###
If you install custom software on Whonix-Workstation, and want to prevent *identity correlation through circuit sharing* (which you should do), you have to manually configure them. This is not a Whonix specific problem. ^1^ ^2^ ^3^ 

Read also [Software installation on Whonix-Workstation](https://sourceforge.net/p/whonix/wiki/Install%20Software/).

### Hidden Services ###
[Hidden services are automatically separated from each other.](https://lists.torproject.org/pipermail/tor-talk/2012-September/025432.html)

### Footnotes ###
<font size="-3">
,,
^1^ If you used to use only one SocksPort with the [common torification methods](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO), the [same thing happened](https://lists.torproject.org/pipermail/tor-talk/2012-March/023535.html).
^2^ Also the current (March 2012) [Tor Browser Bundle](https://www.torproject.org/projects/torbrowser.html.en) is affected, all Firefox Tabs can be correlated to the same identity until the circuit is automatically changed by Tor. 
^3^ [Tails](https://tails.boum.org/), which is officially listed on torproject.org was [also affected](https://lists.torproject.org/pipermail/tor-talk/2012-March/023535.html). Tails done [Todo](https://tails.boum.org/todo/separate_Tor_streams/) item.
</font>

## How to mitigate identity correlation ##
### Basic Protection ###
Most applications which come with Whonix 0.2.1 and above are already configured to prevent *identity correlation through circuit sharing*, you really should read the introduction above.

The only traffic going through TransPort by default is [whonixcheck] when testing the TransPort. If that is of concern to you, it can be disabled in whonixcheck. Just comment out the "*check_tor "TransPort"*" in */usr/local/bin/whonixcheck* in that case.

All custom installed application's TCP traffic is routed through Tor's TransPort and all their DNS requests through Tor's DnsPort. This means different activities or "identities" in different applications (say browser, IRC, email) end up being routed through the same circuit, thus *identity correlation* is at risk.

To protect against this, you have to set up per-application SOCKS ports in Whonix-Gateway.

On Whonix-Gateway in */etc/tor/torrc* ([on github](https://github.com/adrelanos/Whonix/blob/stable/whonix_gateway/etc/tor/torrc)) are already a lot custom socks ports prepared for custom installed applications:

* Without IsolateDestAddr and without IsolateDestPort: SocksPort 192.168.0.10:9152 to 9159
* With IsolateDestAddr, but without IsolateDestPort: SocksPort 192.168.0.10:9160 to 9169
* Without IsolateDestAddr, but with IsolateDestPort: SocksPort: 192.168.0.10:9170 to 9179
* With IsolateDestAddr and with IsolateDestPort: SocksPort: 192.168.0.10:9180 to 9189
* If they those are not enough, you can add your own ones.

You can point your applications, where you want to prevent *identity correlation though circuit sharing*, to those SocksPorts. Each custom installed application has to be torified, for directions how to do that use the [Torify HOWTO](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO).

Additional comments regarding the Torify HOWTO:

* Warnings about protocol related warnings you must honor. You are still better off with Whonix, as it offers best possible [Protocol-Leak-Protection and Fingerprinting-Protection](https://sourceforge.net/p/whonix/wiki/Whonix%27s%20Protocol-Leak-Protection%20and%20Fingerprinting-Protection/).
* Whonix's setup provides protection against IP leaks through [protocol leaks](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO#Protocolleaks).
* If you do not correctly torify, no connections will be possible.
* If you redirect more than one application to the same SocksPort, *identity correlation* is at risk.
* DNS related [warnings](https://trac.torproject.org/projects/tor/wiki/doc/TorFAQ#IkeepseeingthesewarningsaboutSOCKSandDNSandinformationleaks.ShouldIworry) still apply, though to a lesser extent - an attack could only make correlations but still couldn't figure out your IP. You can prevent that, be out commenting (# in front) DnsPort in /etc/tor/torrc on the Whonix-Gateway and by removing the DNS redirection firewall rule from /usr/local/bin/whonix_firewall. ([on github](https://github.com/adrelanos/Whonix/blob/stable/whonix_gateway/usr/local/bin/whonix_firewall))
    * Do not use a [local DNS resolver](https://trac.torproject.org/projects/tor/wiki/doc/SupportPrograms#DNS), as all DNS requests would be executed by the same circuit.
* Other leaks, such as applications not honoring the proxy settings / wrapper, ICMP or UDP leaks do not apply to Whonix.

### Better Protection ###
For best protection against *identity correlation*:

Read the advice above and on Whonix-Gateway:

Deactivate KDE / GNOME - application wide proxy settings...

* Whonix 0.6.2 and above: Because those proxy settings are not application specific, but rather force all KDE / GNOME applications through the same SocksPort (no KDE / GNOME applications which use the internet preinstalled by default), deactivating those KDE / GNOME - wide proxy settings gives better control about stream isolation.

To deactivate TransPort and DnsPort...

* Set *WORKSTATION_TRANSPARENT_TCP=0* in */usr/local/bin/whonix_firewall* ([on github](https://github.com/adrelanos/Whonix/blob/stable/whonix_gateway/usr/local/bin/whonix_firewall))
* Set *WORKSTATION_TRANSPARENT_DNS=0* in in */usr/local/bin/whonix_firewall*
* Reload whonix_firewall (*sudo /usr/local/bin/whonix_firewall*) or simply reboot.

Although not strictly required, you could additionally, comment out:

* TransPort in */etc/tor/torrc*
* DnsPort in */etc/tor/torrc*
* And restart Tor. (*sudo service tor restart*)

This will disable transparent proxying. All applications not configured to use a SocksPort or forced to use a SocksPort (use uwt) will not be able to establish connections. This is the only way to ensure, that different SocksPorts are used and that also DNS is remotely resolved through that SocksPort.

### Total protection ###
Total protection is only possible, if you honor the advice above and only use one application per session and always revert to a fresh snapshot or use [more than one Whonix-Workstation](http://sourceforge.net/p/whonix/wiki/TorBrowser/#more-than-one-tor-browser-in-whonix). [Multiple Whonix-Workstations] (using different internal IP's) are automatically separated by Tor (IsolateClientAddr is Tor's default).

### Limited workarounds for Tor Browser ###
#### Second Tor Browser with its own SocksPort ####
A good option would be to install a second browser and configure it to use its own SocksPort, see [More than one Tor Browser in Whonix](http://sourceforge.net/p/whonix/wiki/TorBrowser/#more-than-one-tor-browser-in-whonix).

#### IsolateDestAddr and IsolateDestPort for Tor Browser (Recommend against!) ####
**(Recommend against!)**

As a workaround you could enable IsolateDestAddr and IsolateDestPort for the Tor Browser. 

This comes at great performance costs, especially for websites with lots of 3rd party content. It will not isolate connections to different websites on a shared server and it will create new circuits for every IP address you connect to (e.g. it will isolate subdomains if they use different IPs). It will also let you stand out more from other Tor Browser users, because almost no one is using it that way. Generally, for these reasons you should not enable this feature. Instead close the browser and get a "new identity" through arm on the gateway if you want to separate activities inside Tor Browser.

On Whonix-Gateway open */etc/tor/torrc*.

    sudo nano /etc/tor/torrc

Comment out.

    #SocksPort 192.168.0.10:9100

Comment in.

    SocksPort 192.168.0.10:9100 IsolateDestAddr IsolateDestPort

## Development ##
Tests.

Applications which internally use curl.

    sudo update-command-not-found

    sudo update-flashplugin-nonfree --install --verbose

Applications which is uwt wrapped itself and internally uses ssh.

    git push origin master

## Sources ##
<font size=-3>

* [Separate streams across circuits by connection metadata](https://gitweb.torproject.org/torspec.git/blob/HEAD:/proposals/171-separate-streams.txt)
* [tor-talk Operating system updates / software installation behind Tor Transparent Proxy](https://lists.torproject.org/pipermail/tor-talk/2012-March/023496.html)
* [tor-talk Awareness for identity correlation through circuit sharing is almost zero.](https://lists.torproject.org/pipermail/tor-talk/2012-March/023536.html)
* [tor-talk Tor's stream isolation features defaults Question](https://lists.torproject.org/pipermail/tor-talk/2012-May/024401.html)
* [tor-talk Tor's stream isolation features defaults Answer](https://lists.torproject.org/pipermail/tor-talk/2012-May/024403.html)
* [Tails-dev separate Tor streams](https://mailman.boum.org/pipermail/tails-dev/2012-August/001422.html)
* [Tails separate Tor streams](https://tails.boum.org/todo/separate_Tor_streams/)
* [Tails-dev Please review Tails stream isolation plans](https://mailman.boum.org/pipermail/tails-dev/2012-August/001532.html)
* [Tails Design: Tor stream isolation](https://tails.boum.org/contribute/design/stream_isolation/)

</font>

# Footer #
<font size=-3>
Stream Isolation Graphic has been contributed by:
Cuan Knaggs – graphic and web design
[revlover](http://revolver.za.net/)
print media – web design – web development – cms – e-commerce
</font>

[[include ref=WikiFooter]]