[[include ref=WikiHeader]]

[TOC]

= Control Port Filter Proxy =

== Introduction ==

Tor's control port has at least one, in context of Whonix, dangerous feature. Its &quot;GETINFO address&quot; and the answer to this request will be the real external IP of the Tor client. By the way, this Tor control port feature makes also a [https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO/BridgeFirewall Bridge Firewall] impossible. Therefore before Whonix 0.6.2, Whonix-Workstation had no access to Tor's control port. This was because, Whonix-Workstation is not supposed to have an way of finding out its own external IP address.

Before Whonix 0.6.2, this also broke Tor Button's New Identity feature, which essentially sends &quot;SIGNAL NEWNYM&quot; to Tor's control port. While Tor Button's New Identity is still the only feature that was not available when using Tor Browser in Whonix, Tor Button in future will get more and more dependent on Tor's control port.

TBB (since version 3 alpha) [https://trac.torproject.org/projects/tor/ticket/6546#comment:33 by default performs its own control port verification]. It simply checks, that the socks port Tor reports, is the same one as Tor Browser is configured to use. If it fails, and it would fail in Whonix 0.5.6, Tor Button would look like disabled and show a failure message.

In future, Tor Button will likely also use something like [https://trac.torproject.org/projects/tor/ticket/3652 &quot;GETINFO clockskew&quot;].

Therefore all requirements, Whonix-Workstation having no way of finding its own external IP address, joining Tor Browser's fingerprint for Whonix users, having no access for Whonix-Workstation to Tor's control port with Tor Buttons new requirement to have access to Tor's control port contradicted itself.

Control Port Filter Proxy has been implemented as a solution. It gives Whonix-Workstation access to a limited selection of Tor's control port commands, using white listing (not blacklisting). For example, it allows &quot;SIGNAL NEWNYM&quot; to make Tor Buttons New Identity feature available for users who use Tor Browser in Whonix-Workstation.

Tor Button would get confused by the many SocksPorts Whonix-Gateway has open (for stream isolation). Therefore when Control Port Filter Proxy gets asked 'GETINFO net/listeners/socks', it lies, and answers '250-net/listeners/socks=&quot;127.0.0.1:9150&quot;'. This makes Tor Button happy and therefore it shows a &quot;Congratulations!&quot; (success) welcome page on its default homepage about:tor and not the failure page, which would confuse users.

For eventual further Tor control port access requirements by Tor Button, the configuration file of accepted commands has to be extended. If Tor Button would ever ask for anything which violates Whonix's design (Whonix-Workstation has no way of finding out its own external IP address in particular), such as &quot;GETINFO address&quot;, for example if Tor Button wanted to ensure, that the user isn't using its own external IP address, a new lie would have to be added to the Control Port Filter Proxy script. In case many more lies are required, lies should go into the config file as well, for now, hard coding is sufficient.

== Whonix-Workstation ==

Tor Browser points to Tor control port 127.0.0.1:9151 by default (no changes by Whonix).

Whonix sets appropriate environment variables in /etc/profile.d/ for control port (9151), control port ip (127.0.0.1) and control port password &quot;password&quot;. The latter is not really in use, its just to make Tor Button happy, because it doesn't default to some password. Tor Button sends it, but its ignored by Control Port Filter Proxy.

rinetd redirects 127.0.0.1:9151 to Whonix-Gateway 192.168.0.10:9052.

== Whonix-Gateway ==

Control Port Filter proxy listens on 127.0.0.1 port 9052, filters (white list) incoming control port messages and forwards them to the real Tor Control Port listening in 127.0.0.1:9051. Control Port Filter Proxy itself uses cookies authentication to authenticate Tor's control port. The latter is not important, since Whonix-Gateway's only purpose is running Tor, its not a multi user operating system, and if it were compromised, cookie authentication wouldn't be of help anymore either.

== Debugging Inspiration ==

<pre>sudo cp whonix_gateway/etc/init.d/controlportfiltd /etc/init.d/
sudo cp whonix_gateway/usr/bin/controlportfilt /usr/bin/
sudo cp whonix_gateway/usr/lib/whonix/cpf-tcpserver /usr/lib/whonix/
sudo cp whonix_workstation/etc/profile.d/20_controlportfilt.sh /etc/profile.d/
sudo cp whonix_shared/usr/bin/tor-ctrl /usr/bin/
sudo cp whonix_gateway/etc/controlportfilt.d/30_controlportfilt_defaul /etc/controlportfilt.d/

sudo service controlportfiltd restart

tail -f /var/log/controlportfilt</pre>
= Footer =

[[include ref=WikiFooter]]

