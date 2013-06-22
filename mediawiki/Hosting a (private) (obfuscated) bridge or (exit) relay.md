[[include ref=WikiHeader]]

[TOC]

= Hosting a (private) (obfuscated) bridge or (exit) relay =

== Introduction ==

You can still volunteer to Tor and host a bridge, private bridge, obfuscated bridge, private obfuscated bridge, middle node or exit relay when you are using Whonix. Either inside the Whonix-Gateway or directly on the host.

== Inside the Whonix-Gateway ==

This chapter hasn't been tested for a long time. Get in contact if you are interested in this configuration.

Simply follow all the usual instructions given on torproject.org inside the Whonix-Gateway just as you would, if Tor wouldn't run inside a virtual machine. The only additional thing to do is to set up a port forwarding from the host to the virtual machine. That is simple. It's a Virtual Box feature. You can also do this with the Virtual Box graphical user interface. Go to Whonix-Gateway -&gt; Settings -&gt; Network Interface -&gt; Port Forwarding.

What's left are the firewall rules. On the Whonix-Gateway ''sudo nano /usr/local/bin/whonix_firewall'' ([https://github.com/adrelanos/Whonix/blob/stable/whonix_gateway/usr/local/bin/whonix_firewall on github]) and look out for

<pre>GATEWAY_ALLOW_INCOMMING_SSH=0</pre>
And change that to

<pre>GATEWAY_ALLOW_INCOMMING_SSH=1</pre>
Scroll down to

<pre>if [ &quot;$GATEWAY_ALLOW_INCOMMING_SSH&quot; = &quot;1&quot; ]; then
    iptables -A INPUT -i &quot;$EXT_IF&quot; -p tcp --dport 22 -j ACCEPT
fi</pre>
and add

<pre># Tor
iptables -A INPUT -i $EXT_IF -p tcp --dport YOURPORT -j ACCEPT</pre>
= Footer =

[[include ref=WikiFooter]]

