[[include ref=WikiHeader]]

[TOC]

= Access Whonix-Gateway Port From Host =

'''This is very esoteric and you probable don't need it!''' '''Advanced users only!'''

== Example: Make port 9050 accessible from the host. ==

On the host...

In the Whonix-Gateway VM network settings. Set up Port Forwarding: within the &quot;Adapter 1&quot; tab click &quot;Advanced&quot;, then Port Forwarding. Insert a new rule as follows.

<pre>Name: 9050
Protocol: TCP
Host IP: 127.0.0.1
Host Port: 9050
Guest IP: leave blank
Guest Port: 9050</pre>
Or the same as command line.

<pre>VBoxManage modifyvm &quot;Whonix-Gateway&quot; --natpf1 &quot;9050&quot;,tcp,127.0.0.1,9050,,9050</pre>
Inside Whonix-Gateway...

Add to /etc/tor/torrc.

<pre>## 10.0.2.15 is usually obtained form Virtual Box's DHCP server.
## Hope this always works, otherwise you have to edit /etc/network/interfaces
## and use a static virtual LAN IP.
SocksPort 10.0.2.15:9050

## The next line is not strictly required, neat for debugging.
SocksPort 127.0.0.1:9050</pre>
Reload Tor.

<pre>sudo service tor reload</pre>
We need to /usr/local/bin/whonix_firewall. Look for.

<pre>## Allow incoming SSH connections on the external interface.
## DISABELD BY DEFAULT. Only for testing/debugging.
if [ &quot;$GATEWAY_ALLOW_INCOMING_SSH&quot; = &quot;1&quot; ]; then
   iptables -A INPUT -i &quot;$EXT_IF&quot; -p tcp --dport 22 -j ACCEPT
fi</pre>
And below that, add.

<pre>iptables -A INPUT -i &quot;$EXT_IF&quot; -p tcp --dport 9050 -j ACCEPT</pre>
== Debugging ==

Inside Whonix-Gateway...

Switch to clearnet user.

<pre>su clearnet
## default password: changeme</pre>
Test if the port you want to make available on the host is available from inside Whonix-Workstation. (If that's not the case, something is fundamentally wrong and you need to fix this first.)

<pre>## Circumventing uwt curl wrapper.
/usr/bin/curl 127.0.0.1:9050

## Circumventing uwt curl wrapper.
/usr/bin/curl 10.0.2.15:9050</pre>
It should answer &quot;Tor is not a http proxy&quot;.

== Testing ==

On the host...

<pre>/usr/bin/curl 127.0.0.1:9050</pre>
It should answer &quot;Tor is not a http proxy&quot;. If you see that, that indicates that Tor is, which runs inside Whonix-Gateway is accessible on the host as well.

== Forwarding that port to LAN ==

On the host...

This is untested, but should work, otherwise get in contact.

You can use something like rinetd to redirect that port 127.0.0.1:9050 to a different network interface. Otherwise you could experiment with the Whonix-Gateway VM network settings.

= Footer =

[[include ref=WikiFooter]]

