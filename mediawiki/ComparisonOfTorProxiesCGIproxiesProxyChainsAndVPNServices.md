[[include ref=WikiHeader]]

[TOC]

= Comparison =

== Comparison of Tor and Proxies ==

=== Introduction ===

Proxy services are particularly famous for this kind of &quot;anonymization on demand&quot;, besides the already mentioned services. They are literally &quot;proxy PCs&quot; which switch communication between your PC and the Internet. They relay your data traffic to the target and send the answer back to your PC so that the web site cannot see your IP address.

=== Comparison ===

This is a brief overview with a comparison of features of proxies, which you can find on many free proxy sharing websites. It's not about the proxy protocol. Not a comprehensive discussion of all aspects of proxies. Some points required for understanding.

Footnotes:

<sup>1</sup> Not when being used as a transparent proxy. Only when being used as proxy settings. <sup>2</sup> Tor offers a socks5 proxy but Tor does not support UDP. <sup>3</sup> Some http and https proxies don't even hide your IP, if these are setup to send the '[https://trac.torproject.org/projects/tor/wiki/doc/TorPlusVPN#VPNSSHversusProxy http forwarded for]' header. Proxies not sending http forwarded for, are sometimes called &quot;elite&quot; or &quot;anonymous&quot; proxies. <sup>4</sup> To the destination server, for example to the webserver torproject.org. <sup>5</sup> Without user-to-proxy encryption the ISP (internet service provider) or any man in the middle, can see connection details, including destination server IP and package content. (Package content will be only hidden, when end-to-end encryption such as SSL is being used.) <sup>6</sup> Depends on proxy. <sup>7</sup> Not yet supported by the Tor network. <sup>8</sup> Socks interface only available to paying users. <sup>9</sup> eepsites only. Connections to clearnet only possible through outproxies (no SSL to destination site). <sup>a</sup> Do not support the connect method (see below). Therefore connections to SSL protected websites is impossible. <sup>b</sup> https proxy is misleading, as the connection to the proxy is not encrypted. The proxy additionally supports the connect method, which is required to access SSL protected websites and other services than http. <sup>c</sup> Tor can offer a SocksPort (socks4(a)/5), DnsPort and TransPort. Third party http 2 socks converter (privoxy) available. <sup>d</sup> For a more detailed review of that network, see [https://sourceforge.net/p/whonix/wiki/JonDonym/ JonDonym].

<table>
<thead>
<tr class="header">
<th align="left">proxy type</th>
<th align="left">comment</th>
<th align="left">http <sup>4</sup></th>
<th align="left">https <sup>4</sup></th>
<th align="left">UDP</th>
<th align="left">Remote DNS</th>
<th align="left">http forwarded for header <sup>3</sup></th>
<th align="left">user-to-proxy encryption <sup>5</sup></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">http</td>
<td align="left"><sup>a</sup></td>
<td align="left">yes</td>
<td align="left">no</td>
<td align="left">no</td>
<td align="left">yes <sup>1</sup></td>
<td align="left">depends <sup>6</sup></td>
<td align="left">no</td>
</tr>
<tr class="even">
<td align="left">https</td>
<td align="left"><sup>b</sup></td>
<td align="left">yes</td>
<td align="left">yes</td>
<td align="left">no</td>
<td align="left">yes <sup>1</sup></td>
<td align="left">depends <sup>6</sup></td>
<td align="left">no</td>
</tr>
<tr class="odd">
<td align="left">socks4</td>
<td align="left">-</td>
<td align="left">yes</td>
<td align="left">yes</td>
<td align="left">no</td>
<td align="left">no</td>
<td align="left">no</td>
<td align="left">no</td>
</tr>
<tr class="even">
<td align="left">socks4a</td>
<td align="left">-</td>
<td align="left">yes</td>
<td align="left">yes</td>
<td align="left">no</td>
<td align="left">yes</td>
<td align="left">no</td>
<td align="left">no</td>
</tr>
<tr class="odd">
<td align="left">socks5</td>
<td align="left">-</td>
<td align="left">yes</td>
<td align="left">yes</td>
<td align="left">yes</td>
<td align="left">yes</td>
<td align="left">no</td>
<td align="left">no</td>
</tr>
<tr class="even">
<td align="left">CGI</td>
<td align="left">see below</td>
<td align="left">depends <sup>6</sup></td>
<td align="left">depends <sup>6</sup></td>
<td align="left">no</td>
<td align="left">yes</td>
<td align="left">depends <sup>6</sup></td>
<td align="left">depends <sup>6</sup></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th align="left">anonymization service</th>
<th align="left">comment</th>
<th align="left">http <sup>4</sup></th>
<th align="left">https <sup>4</sup></th>
<th align="left">UDP</th>
<th align="left">Remote DNS</th>
<th align="left">http forwarded for header <sup>3</sup></th>
<th align="left">user-to-proxy encryption <sup>5</sup></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">i2p</td>
<td align="left">-</td>
<td align="left"><sup>9</sup></td>
<td align="left"><sup>9</sup></td>
<td align="left">?</td>
<td align="left">yes</td>
<td align="left">no</td>
<td align="left">yes</td>
</tr>
<tr class="even">
<td align="left">JonDo</td>
<td align="left"><sup>d</sup></td>
<td align="left">yes</td>
<td align="left">yes</td>
<td align="left">premium only <sup>8</sup></td>
<td align="left">yes</td>
<td align="left">no</td>
<td align="left">yes</td>
</tr>
<tr class="odd">
<td align="left">Tor</td>
<td align="left"><sup>c</sup></td>
<td align="left">yes</td>
<td align="left">yes</td>
<td align="left">no <sup>7</sup></td>
<td align="left">yes</td>
<td align="left">no</td>
<td align="left">yes</td>
</tr>
</tbody>
</table>

=== Conclusion ===

Other than anonymization services such as JonDo, i2p and Tor, unfortunately, proxies have a high susceptibility to misuse and user data theft: many proxies are PCs hijacked by hackers or criminals, or even exclusively offered for the purpose of user observation. <sup>3</sup> Even if they were legitimately offered, it would be a security by policy, rather than protection by design - because a single operator can decide to enable logging.

Some proxies automatically give your IP address away to the target webserver <sup>4</sup>.

Connections with proxies are almost always unencrypted <sup>1</sup>, so that an eavesdropper on your connection could observe your surfing behavior. Moreover, the proxy operator can, of course, watch exactly what you are doing. Proxies offer thus, if at all, only weak protection against destination website logging and no protection from third parties eavesdroppers. Their usage is risky.

<font size="-3"> <sup>1</sup> I am not aware of any http(s) or socks4(a)/5 proxies <sup>2</sup>, supporting encryption. <sup>2</sup> (other than anonymity networks, which use http(s) socks4(a)/5 proxies just as an interface) <sup>3</sup> I haven't found any http(s) or socks4(a)/5 proxies <sup>2</sup> as legitimate offer. Most proxies are found on (free) proxy sharing and it's dubious if they those proxies are aware of it want to be listed there or if they are only open proxies. (misconfigured machines) <sup>4</sup> (http forwarded for header) </font>

=== License ===

<font size="-3">License of &quot;Comparison of different proxy types&quot;: This was originally posted by adrelanos (proper) to the [https://trac.torproject.org/projects/tor/wiki/doc/proxy TorifyHOWTO/proxy] ([http://www.webcitation.org/6GmyeR7Y5 w]) ([https://trac.torproject.org/projects/tor/wiki/doc/LegalStuff license]) ([http://www.webcitation.org/6GmySlraB w]). Adrelanos didn't surrender any copyrights and can therefore re-use it here. It is under the same license as the rest of the page. </font>

<font size="-3">Thanks to [https://anonymous-proxy-servers.net/ JonDos] ([https://anonymous-proxy-servers.net/forum/viewtopic.php?p=31220&sid=ac8a6ca16eb768b3322be30b20375c97#p31220 Permission]). The &quot;this&quot; chapter of the &quot;&quot; contains content from the JonDonym documentation [https://anonymous-proxy-servers.net/en/help/otherServices.html Other Services] page.</font>

== Comparison of Whonix, Tails, Tor Browser Bundle and CGIproxies ==

=== Introduction ===

Point of view: using them in Mozilla Firefox on the host without using something such as Whonix or Tails.

CGIproxies are webproxy services, Internet pages with a form field in which the user can input the target address that he want's to visit anonymously. The webproxy subsequently delivers the content of the requested website and automatically patches all links to use the webproxy when clicked. For using webproxy services the browser configuration does not have to be changed.

Compared to network proxies, they have the disadvantage not to be able to replace each link correctly, in particular on web sites with JavaScript code. This makes it easier that the user IP address gets &quot;leaked&quot; to the web server, which the proxy should actually prevent. The https://ip-check.info anonymity test displays the weakness of some web proxies in the comparison table.

They could only anonymize browser traffic and not other applications, but to be fair, they don't claim more than anonymizing browser traffic.

=== Comparison ===

Required knowledge:

* [https://en.wikipedia.org/wiki/CGIProxy CGIProxy]
* Legend:
** Broken: Real IP address gets uncovered.
** *: The thereby marked service does not even reach the test site if JavaScript is activated. It parses so bad, that the browser just leaves the service silently in some cases...
** Ok: no leak found.
** ?: Not tested and therefore unknown.
** NI: Not installed by default.
** DE: Deactivated even if installed.
** RA: recommend against by maintainers.
** <sup>1</sup> encrypted connection to the CGI proxy (SSL) <sup>2</sup> or Tor exit node
** <sup>2</sup> with proper SSL certificate recognized by certificate authorities

<table>
<thead>
<tr class="header">
<th align="left">Software / Provider</th>
<th align="left">HTML/CSS/FTP</th>
<th align="left">JavaScript</th>
<th align="left">Java</th>
<th align="left">encrypted <sup>1</sup></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Whonix</td>
<td align="left">Ok</td>
<td align="left">Ok</td>
<td align="left">NI DE RA Ok</td>
<td align="left">Yes</td>
</tr>
<tr class="even">
<td align="left">Tails</td>
<td align="left">Ok</td>
<td align="left">Ok</td>
<td align="left">NI DE RA ?</td>
<td align="left">Yes</td>
</tr>
<tr class="odd">
<td align="left">Tor Browser Bundle</td>
<td align="left">Ok</td>
<td align="left">Ok</td>
<td align="left">NI DE RA (Broken)</td>
<td align="left">Yes</td>
</tr>
<tr class="even">
<td align="left">Anonymouse</td>
<td align="left">Broken</td>
<td align="left">Broken*</td>
<td align="left">Broken</td>
<td align="left">premium only</td>
</tr>
<tr class="odd">
<td align="left">Hide My Ass!</td>
<td align="left">Ok</td>
<td align="left">Broken*</td>
<td align="left">Broken</td>
<td align="left">Yes</td>
</tr>
<tr class="even">
<td align="left">WebProxy.ca</td>
<td align="left">Ok</td>
<td align="left">Broken</td>
<td align="left">Broken</td>
<td align="left">No</td>
</tr>
<tr class="odd">
<td align="left">KProxy</td>
<td align="left">Broken</td>
<td align="left">Broken*</td>
<td align="left">Broken</td>
<td align="left">Yes</td>
</tr>
<tr class="even">
<td align="left">Guardster</td>
<td align="left">Ok</td>
<td align="left">Broken (if allowed)*</td>
<td align="left">Broken</td>
<td align="left">premium only</td>
</tr>
<tr class="odd">
<td align="left">Megaproxy</td>
<td align="left">Broken</td>
<td align="left">premium only</td>
<td align="left">premium only</td>
<td align="left">Yes</td>
</tr>
<tr class="even">
<td align="left">Proxify</td>
<td align="left">premium only</td>
<td align="left">?</td>
<td align="left">?</td>
<td align="left">?</td>
</tr>
<tr class="odd">
<td align="left">Ebumna PHProxy</td>
<td align="left">Broken</td>
<td align="left">Broken*</td>
<td align="left">Broken</td>
<td align="left">No</td>
</tr>
</tbody>
</table>

=== Links to Software / Provider and Test ===

&quot;(check manually)&quot; in the following table means, enter the test link manually in the browser.

<table>
<thead>
<tr class="header">
<th align="left">Link</th>
<th align="left">ip-check.info</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">[http://whonix.sourceforge.net/ Whonix]</td>
<td align="left">[https://ip-check.info/?lang=en click] (check manually)</td>
</tr>
<tr class="even">
<td align="left">[https://tails.boum.org Tails]</td>
<td align="left">[https://ip-check.info/?lang=en click] (check manually)</td>
</tr>
<tr class="odd">
<td align="left">[https://www.torproject.org/ Tor Browser Bundle]</td>
<td align="left">[https://ip-check.info/?lang=en click] (check manually)</td>
</tr>
<tr class="even">
<td align="left">[http://anonymouse.org/ Anonymouse]</td>
<td align="left">[http://anonymouse.org/cgi-bin/anon-www.cgi/https://ip-check.info/?lang=en click]</td>
</tr>
<tr class="odd">
<td align="left">[https://hidemyass.com/ Hide My Ass!]</td>
<td align="left">[http://3.hidemyass.com/ip-4/encoded/Oi8vaXAtY2hlY2suaW5mby8_bGFuZz1lbg%3D%3D click]</td>
</tr>
<tr class="even">
<td align="left">[http://www.webproxy.ca/ WebProxy.ca]</td>
<td align="left">[http://www.webproxy.ca/ click] (check manually)</td>
</tr>
<tr class="odd">
<td align="left">[https://www.kproxy.com/ KProxy]</td>
<td align="left">[http://www.kproxy.com/ click] (check manually)</td>
</tr>
<tr class="even">
<td align="left">[http://www.guardster.com/ Guardster]</td>
<td align="left">[http://tproxy.guardster.com/proxy.php/333000024320ce282929b0d2d7cf2cd04dce484dced6cbcc4bcbd7b7cf49cc4bb74dcd0300 click]</td>
</tr>
<tr class="odd">
<td align="left">[https://www.megaproxy.com/ Megaproxy]</td>
<td align="left">[http://www.megaproxy.com/freesurf/ click] (check manually)</td>
</tr>
<tr class="even">
<td align="left">[https://proxify.com/ Proxify]</td>
<td align="left">[http://proxify.com/ click] (check manually)</td>
</tr>
<tr class="odd">
<td align="left">[http://phproxy.ebumna.net/ Ebumna PHProxy]</td>
<td align="left">[http://phproxy.ebumna.net/index.php?s=aHR0cDovL2lwLWNoZWNrLmluZm8vP2xhbmc9ZW4%3D click]</td>
</tr>
</tbody>
</table>

=== Conclusion ===

In comparison to Tor, CGIproxies are only a one hop proxies, thus they know who is connecting and where the user connects to. They could read all transmissions, even if entering SSL protected domain names. This makes them much inferior to Tor.

Due to these disadvantages, other security features, which have been discussed above in chapter comparison of Whonix, Tails and Tor Browser bundle, such as UTC timezone, fingerprinting didn't appear worthwhile to compare.

=== License ===

<font size="-3">Thanks to [https://anonymous-proxy-servers.net/ JonDos] ([https://anonymous-proxy-servers.net/forum/viewtopic.php?p=31220&sid=ac8a6ca16eb768b3322be30b20375c97#p31220 Permission]). The &quot;Whonix Comparison of Whonix, Tails, Tor Browser Bundle and CGIproxies&quot; chapter of the &quot;Whonix Comparision with Others wiki page&quot; contains content from the JonDonym documentation [https://anonymous-proxy-servers.net/en/help/otherServices.html Other Services] page.</font>

== Comparison of Tor and Proxy Chains ==

=== Aren't 10 proxies (proxychains) better than Tor with only 3 hops? - proxychains vs Tor ===

Maybe you've seen the funny picture &quot;I am behind 10 proxies, so what?&quot;. Nevermind.

10 open proxies are not as secure as Tor. Many people are not aware of that.

As outlined above, proxies are not very secure.

With Tor the first hop won't see the IP of the last hop because it can't decrypt the message for the second hop. If one hop can be trusted, the connection is secure (see the onion design).

Even if you are using &quot;elite&quot; or &quot;anonymous&quot; proxies... Or even Socks Proxies...

* All connections between you and all proxies are unencrypted.
* This has nothing to do with SSL, but for demonstration, let's assume you are connecting to an SSL protected web server.
* In human understandable form, this is a sketch how the package for the first proxy in your chain of 5 would look like:
* Hey Proxy1, can you please forward &quot;forward to Proxy3; forward to Proxy4; forward to Proxy5; forward to https://encrypted.google.com 'c8e8df895c2cae-some-garbage-here-(encrypted)-166bad027fdf15335b'&quot; to Proxy2? Thanks!
* You see, your actual transmission will be safely encrypted and can be only decrypted by the https protected webserver, but every proxy will see it's predecessor IP and all successor IP's.
* There is no way to encrypt that information, no way to make your own onion. The proxy protocols (http(s), socks4(a)/5) do not support encryption.

As you would have to trust any of them the IP of all it's successors... The second question about open proxies is, who hosts them?

* most of them are a simple misconfiguration, the owners are not aware of it and do not want the public to use them
* many of them are compromised machines (worm infected)
* some are honeypots, logging or exploiting (dns spoofing, protocol spoofing, ssl spoofing)
* few of them are are from generous people who just want your best and give you anonymity (similar to most Tor server admins)

This must not apply for proxychains of SSH and/or encrypted VPN servers - has not been researched yet. But you can not get so many SSH and/or VPN servers for free (without hacking of course) and/or anonymous payment anyway.

=== License ===

<font size="-3">License of &quot;Comparison of Tor and proxychains&quot;: This was originally posted by adrelanos (proper) to the [https://trac.torproject.org/projects/tor/wiki/doc/TorFAQ#Arent10proxiesproxychainsbetterthanTorwithonly3hops-proxychainsvsTor TorFAQ] ([http://www.webcitation.org/6Gmyhtntt w]) ([https://trac.torproject.org/projects/tor/wiki/doc/LegalStuff license]) ([http://www.webcitation.org/6GmySlraB w]). Adrelanos didn't surrender any copyrights and can therefore re-use it here. It is under the same license as the rest of the page. </font>

== Comparison of Tor and VPN services ==

=== Comparison ===

If you run the VPN software directly on the same machine as also the client software such as web browser runs, [https://sourceforge.net/p/whonix/wiki/DataCollectionTechniques/#active-web-contents active contents] can read your real IP address. This can be prevented, if you use a virtual or physical VPN-Gateway or your router. However, please note that active contents may still read a lot of data about your computer and network configuration.

* Some providers force the user to use their proprietary closed source software and have no option to allow being used by reputable VPN software, such as OpenVPN.
* On one hand, their software usually does not ensure, that users also have an uniform appearance on the Web aside their IP address (see [https://sourceforge.net/p/whonix/wiki/DataCollectionTechniques/ Data Collection Technique]). The users are thus distinguishable and easily identifiable by merging the data.
* And on the other hand, a local observer on your network (ISP, WLAN) could guesstimate websites requested over VPN simply by analyzing size and timing of the encrypted VPN data stream. Tor is quite resilient against this attack (a scientific article which demonstrates the attack is found [http://epub.uni-regensburg.de/11919/1/authorsversion-ccsw09.pdf here]; the success rates are over 90% for VPNs).
* Moreover, VPN systems, as inherent to their functional principle, normally do not filter or replace your computer's TCP packets. They thereby do not protect you from [https://sourceforge.net/p/whonix/wiki/DataCollectionTechniques/#tcp-timestamps TCP timestamp attacks] as Tor does.
* Even when using a virtual or physical VPN-Gateway, due to browser fingerprinting problems it's only [https://sourceforge.net/p/whonix/wiki/DoNot/#do-not-confuse-anonymity-with-pseudonymity pseudonymous rather than anonymous].
* You should also keep in mind that VPN hosts can, unlike Tor, can track and save every step of yours, since they control all servers in the VPN.
* VPN providers only offer privacy by policy, while Tor offers privacy by design. A VPN provider can claim not to log, but you'll never know until it's too late. When using Tor, you also never know, if any of the three hops keeps logs. One malicious node will have less impact. The entry guard will not know where you are connecting to, thus it's not a fatal problem if they log. The exit node won't know who you are, but can see your unencrypted traffic, which can be a problem if you send sensitive data (which you are advised not to do), but if you act accordingly, it isn't a problem. It's unlikely (thus not impossible), that you choose a circuit where an adversary controls all three nodes. However, while using VPN providers you're putting all trust into the policy of one provider, using Tor distributes trust.
* Don't get fooled by advertisements for Double, Triple or Multi Hop VPNs. Unless it's the user, who builds it's own custom VPN chain by carefully choosing different VPN providers, owned by different companies, you're still fully trusting only one provider.

Whether it's worth to combine Tor with a VPN, either as pre-Tor-VPN (user -&gt; VPN -&gt; Tor) or as post-Tor-VPN (user -&gt; Tor -&gt; VPN) is quite a controversial topic and discussed on the [https://trac.torproject.org/projects/tor/wiki/doc/TorPlusVPN Tor plus VPN] ([http://www.webcitation.org/6FPudSpvr w]) page. In case you decide to do so, it's easy with Whonix, see [https://sourceforge.net/p/whonix/wiki/Features/#vpn-tunnel-support VPN/Tunnel Support].

=== License ===

<font size="-3">Thanks to [https://anonymous-proxy-servers.net/ JonDos] ([https://anonymous-proxy-servers.net/forum/viewtopic.php?p=31220&sid=ac8a6ca16eb768b3322be30b20375c97#p31220 Permission]). The &quot;Comparison of Tor and VPN services&quot; chapter of the &quot;Whonix Comparision with Others wiki page&quot; contains content from the JonDonym documentation [https://anonymous-proxy-servers.net/en/help/otherServices.html Other Services] page.</font>

= Footer =

[[include ref=WikiFooter]]

