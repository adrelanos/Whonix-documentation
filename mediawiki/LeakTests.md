[[include ref=WikiHeader]]

[TOC]

= Introduction =

In past Whonix documentation stated &quot;in your own interest you should do the leak tests&quot;. That was from a time, where Whonix was only useful for very advanced end users, because only textual instructions existed, no scripts, no source code and the Whonix concept was brand new. It is unrealistic, that all download users do and understand the leak tests. That's why it was removed from the Readme.

You are still invited and encouraged to do the leak tests, in fact, at the moment, there are probable not many people auditing Whonix security.

Unfortunately, leak testing is as complicated as programming. You can not learn it overnight and you won't find someone online, willing to teach you for free. That's really something you have to do on your own. We continue to list and document all leak test we are aware of, but we can not educate everyone in the depths of networking.

= Knowledge assumed =

* [https://trac.torproject.org/projects/tor/wiki/doc/build/BuildSignoff#Expectedissueswithpopulartestpages Expected issues with popular test pages]
* Search for previous discussions before reporting.

= Leak Testing Websites =

There are two many websites for leak testing. (Some are offline.)

* [https://trac.torproject.org/projects/tor/wiki/doc/build/BuildSignoff#TestPagestoUse List 1]
* [https://trac.torproject.org/projects/tor/wiki/doc/Testing/Tools#Sites List 2]

None of the Leak Testing Websites was able to find out the IP of Whonix-Workstation, no matter if plugins, flash and/or java was activated.

= DNS Leak Tests =

== Online ==

* http://www.dnsleaktest.com/
* Also check out http://check2ip.com/

== Defunct host DNS ==

Rendering the DNS on your host defunct should result in your not not being be able to nslookup anymore, but Whonix-Workstation's DNS should still be functional.

== Defunct /etc/resolv.conf ==

On the Whonix-Gateway 'sudo nano /etc/resolv.conf' and out comment everything (# before every line so everything is ignored).

<pre>#nameserver 127.0.0.1</pre>
As a tests result the DNS requests in the Whonix-Workstation should still work while the DNS requests in the Whonix-Gateway no longer work.

== Using dig ==

Another very poor manish leak test: Because Tor's DNS resolver does not handle AAAA records this will not return any google hostnames if run on Whonix-Workstation and DNS requests aren't leaking. Running.

<pre>dig AAAA check.torproject.org</pre>
Should reply.

<pre>; &lt;&lt;&gt;&gt; DiG 9.8.1-P1 &lt;&lt;&gt;&gt; AAAA check.torproject.org
;; global options: +cmd
;; Got answer:
;; -&gt;&gt;HEADER&lt;&lt;- opcode: QUERY, status: NOTIMP, id: 42383
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;check.torproject.org.          IN      AAAA

;; Query time: 0 msec
;; SERVER: 192.168.0.10#53(192.168.0.10)
;; WHEN: [date]
;; MSG SIZE  rcvd: 38</pre>
Tor also does not support DNSSEC yet. Running.

<pre>dig +dnssec check.torproject.org @localhost</pre>
Should reply.

<pre>; &lt;&lt;&gt;&gt; DiG 9.8.1-P1 &lt;&lt;&gt;&gt; +dnssec check.torproject.org @localhost
;; global options: +cmd
;; connection timed out; no servers could be reached</pre>
== Using nslookup ==

Running.

<pre>nslookup -type=mx check.torproject.org</pre>
Should reply.

<pre>Server:         192.168.0.10
Address:        192.168.0.10#53

** server can't find check.torproject.org: NOTIMP</pre>
Running

<pre>nslookup -type=AAAA check.torproject.org</pre>
Should reply.

<pre>Server:         192.168.0.10
Address:        192.168.0.10#53

** server can't find check.torproject.org: NOTIMP</pre>
= Leaks through the host or VM =

Shut down the Whonix-Gateway and start the Whonix-Workstation. The Whonix-Workstation shouldn't be able to exchange data with any outside target.

= Ping Test =

First, make sure both VMs are online. Since ICMP is not supported by Tor and filtered by Whonix firewall, you should not be able to ping any servers.

= Integrated tshark leaktest =

The necessary scripts for leak testing are now integrated into the Whonix machines.

On Whonix-Gateway start looking for leaks.

<pre>## Login as user, open a shell as user or su user.
## /usr/local/bin/leaktest
sudo leaktest</pre>
On Whonix-Workstation try to produce a leak.

<pre>## Login as user, open a shell as user or su user.
## /usr/local/bin/leaktest
sudo leaktest</pre>
If you are wondering, how this works and what that does, the old article, [LeakTestsOld] is still being kept.

* Original article.
* As copy and paste tutorial.
* For better understanding with more comments.
* Perhaps useful for similar projects.
* Optional additional tests.

= Other Leak Tests =

A similar project published another leak test. Read [https://github.com/ra--/Tor-gateway/wiki/Faq How can I test if there is a leak in the setup respectively all traffic goes through Tor?]. Has not be done with Whonix yet. If you do it, please share your results.

= See Also =

* [Test]

= Footer =

[[include ref=WikiFooter]]

