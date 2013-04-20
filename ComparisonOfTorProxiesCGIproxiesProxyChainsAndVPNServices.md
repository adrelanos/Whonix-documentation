[[include ref=WikiHeader]]

[TOC]

# Comparison #
## Comparison of Tor and Proxies ##
### Introduction ###
Proxy services are particularly famous for this kind of "anonymization on demand", besides the already mentioned services. They are literally "proxy PCs" which switch communication between your PC and the Internet. They relay your data traffic to the target and send the answer back to your PC so that the web site cannot see your IP address.

### Comparison ###
This is a brief overview with a comparison of features of proxies, which you can find on many free proxy sharing websites. It's not about the proxy protocol. Not a comprehensive discussion of all aspects of proxies. Some points required for understanding. 

Footnotes:

^1^ Not when being used as a transparent proxy. Only when being used as proxy settings.
^2^ Tor offers a socks5 proxy but Tor does not support UDP.
^3^ Some http and https proxies don't even hide your IP, if these are setup to send the '[http forwarded for](https://trac.torproject.org/projects/tor/wiki/doc/TorPlusVPN#VPNSSHversusProxy)' header. Proxies not sending http forwarded for, are sometimes called "elite" or "anonymous" proxies.
^4^ To the destination server, for example to the webserver torproject.org.
^5^ Without user-to-proxy encryption the ISP (internet service provider) or any man in the middle, can see connection details, including destination server IP and package content. (Package content will be only hidden, when end-to-end encryption such as SSL is being used.) 
^6^ Depends on proxy.
^7^ Not yet supported by the Tor network.
^8^ Socks interface only available to paying users.
^9^ eepsites only. Connections to clearnet only possible through outproxies (no SSL to destination site).
^a^ Do not support the connect method (see below). Therefore connections to SSL protected websites is impossible.
^b^ https proxy is misleading, as the connection to the proxy is not encrypted. The proxy additionally supports the connect method, which is required to access SSL protected websites and other services than http.
^c^ Tor can offer a SocksPort (socks4(a)/5), DnsPort and TransPort. Third party http 2 socks converter (privoxy) available.
^d^ For a more detailed review of that network, see [JonDonym](https://sourceforge.net/p/whonix/wiki/JonDonym/).

proxy type | comment | http ^4^ | https ^4^ | UDP | Remote DNS | http forwarded for header ^3^ | user-to-proxy encryption ^5^
------------- |  ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- 
http | ^a^ | yes | no | no | yes ^1^| depends ^6^ | no
https | ^b^ | yes  | yes |  no | yes ^1^ | depends ^6^ | no
socks4 | - | yes  | yes | no | no |  no | no
socks4a | - | yes | yes | no | yes |  no | no
socks5 | - | yes | yes | yes | yes | no | no
CGI | see below | depends ^6^ | depends ^6^ | no | yes | depends ^6^ | depends ^6^

anonymization service | comment | http ^4^ | https ^4^ | UDP | Remote DNS | http forwarded for header ^3^ | user-to-proxy encryption ^5^
------------- |  ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- 
i2p | - | ^9^ | ^9^ | ? | yes | no | yes
JonDo | ^d^ | yes | yes | premium only ^8^ | yes | no | yes
Tor | ^c^ | yes | yes | no ^7^ | yes | no | yes

### Conclusion ###
Other than anonymization services such as JonDo, i2p and Tor, unfortunately, proxies have a high susceptibility to misuse and user data theft: many proxies are PCs hijacked by hackers or criminals, or even exclusively offered for the purpose of user observation. ^3^ Even if they were legitimately offered, it would be a security by policy, rather than protection by design - because a single operator can decide to enable logging.

Some proxies automatically give your IP address away to the target webserver ^4^.

Connections with proxies are almost always unencrypted ^1^, so that an eavesdropper on your connection could observe your surfing behavior. Moreover, the proxy operator can, of course, watch exactly what you are doing. Proxies offer thus, if at all, only weak protection against destination website logging and no protection from third parties eavesdroppers. Their usage is risky.

<font size="-3">
^1^ I am not aware of any http(s) or socks4(a)/5 proxies ^2^, supporting encryption.
^2^ (other than anonymity networks, which use http(s) socks4(a)/5 proxies just as an interface)
^3^ I haven't found any http(s) or socks4(a)/5 proxies ^2^ as legitimate offer. Most proxies are found on (free) proxy sharing and it's dubious if they those proxies are aware of it want to be listed there or if they are only open proxies. (misconfigured machines)
^4^ (http forwarded for header)
</font>

### License ###
<font size="-3">License of "Comparison of different proxy types": This was originally posted by adrelanos (proper) to the [TorifyHOWTO/proxy](https://trac.torproject.org/projects/tor/wiki/doc/proxy) ([license](https://trac.torproject.org/projects/tor/wiki/doc/LegalStuff)). Adrelanos didn't surrender any copyrights and can therefore re-use it here. It is under the same license as the rest of the page.
</font>

<font size="-3">Thanks to [JonDos](https://anonymous-proxy-servers.net/) ([Permission](https://anonymous-proxy-servers.net/forum/viewtopic.php?p=31220&sid=ac8a6ca16eb768b3322be30b20375c97#p31220)). The "this" chapter of the "" contains content from the JonDonym documentation [Other Services](https://anonymous-proxy-servers.net/en/help/otherServices.html) page.</font>

## Comparison of Whonix, Tails, Tor Browser Bundle and CGIproxies ##
### Introduction ###
Point of view: using them in Mozilla Firefox on the host without using something such as Whonix or Tails.

CGIproxies are webproxy services, Internet pages with a form field in which the user can input the target address that he want's to visit anonymously. The webproxy subsequently delivers the content of the requested website and automatically patches all links to use the webproxy when clicked. For using webproxy services the browser configuration does not have to be changed.

Compared to network proxies, they have the disadvantage not to be able to replace each link correctly, in particular on web sites with JavaScript code. This makes it easier that the user IP address gets "leaked" to the web server, which the proxy should actually prevent. The https://ip-check.info anonymity test displays the weakness of some web proxies in the comparison table.

They could only anonymize browser traffic and not other applications, but to be fair, they don't claim more than anonymizing browser traffic.

### Comparison ###
Required knowledge:

* [CGIProxy](https://en.wikipedia.org/wiki/CGIProxy)
* Legend:
    * Broken: Real IP address gets uncovered.
    * *: The thereby marked service does not even reach the test site if JavaScript is activated. It parses so bad, that the browser just leaves the service silently in some cases...
    * Ok: no leak found.
    * ?: Not tested and therefore unknown.
    * NI: Not installed by default.
    * DE: Deactivated even if installed.
    * RA: recommend against by maintainers.
    * ^1^ encrypted connection to the CGI proxy (SSL) ^2^ or Tor exit node
    * ^2^ with proper SSL certificate recognized by certificate authorities

| Software / Provider | HTML/CSS/FTP | JavaScript | Java | encrypted ^1^
------------- |  ------------- | ------------- | ------------- | -------------
Whonix | Ok | Ok | NI DE RA Ok | Yes
Tails | Ok | Ok | NI DE RA ? | Yes
Tor Browser Bundle | Ok | Ok | NI DE RA (Broken) | Yes
Anonymouse | Broken | Broken* | Broken | premium only
Hide My Ass! | Ok | Broken* | Broken | Yes
WebProxy.ca | Ok | Broken | Broken | No
KProxy | Broken | Broken* | Broken | Yes
Guardster | Ok | Broken (if allowed)* | Broken | premium only
Megaproxy | Broken | premium only | premium only | Yes
Proxify | premium only | ? | ? | ?
Ebumna PHProxy | Broken | Broken* | Broken | No

### Links to Software / Provider and Test ###
"(check manually)" in the following table means, enter the test link manually in the browser.

| Link | ip-check.info
------------- |  ------------- 
[Whonix](http://whonix.sourceforge.net/) | [click](https://ip-check.info/?lang=en) (check manually)
[Tails](https://tails.boum.org) | [click](https://ip-check.info/?lang=en) (check manually)
[Tor Browser Bundle](https://www.torproject.org/) | [click](https://ip-check.info/?lang=en) (check manually)
[Anonymouse](http://anonymouse.org/) | [click](http://anonymouse.org/cgi-bin/anon-www.cgi/https://ip-check.info/?lang=en)
[Hide My Ass!](https://hidemyass.com/) | [click](http://3.hidemyass.com/ip-4/encoded/Oi8vaXAtY2hlY2suaW5mby8_bGFuZz1lbg%3D%3D)
[WebProxy.ca](http://www.webproxy.ca/) | [click](http://www.webproxy.ca/) (check manually)
[KProxy](https://www.kproxy.com/) | [click](http://www.kproxy.com/) (check manually)
[Guardster](http://www.guardster.com/) | [click](http://tproxy.guardster.com/proxy.php/333000024320ce282929b0d2d7cf2cd04dce484dced6cbcc4bcbd7b7cf49cc4bb74dcd0300)
[Megaproxy](https://www.megaproxy.com/) | [click](http://www.megaproxy.com/freesurf/) (check manually)
[Proxify](https://proxify.com/) | [click](http://proxify.com/) (check manually)
[Ebumna PHProxy](http://phproxy.ebumna.net/) | [click](http://phproxy.ebumna.net/index.php?s=aHR0cDovL2lwLWNoZWNrLmluZm8vP2xhbmc9ZW4%3D) | No

### Conclusion ###
In comparison to Tor, CGIproxies are only a one hop proxies, thus they know who is connecting and where the user connects to. They could read all transmissions, even if entering SSL protected domain names. This makes them much inferior to Tor.

Due to these disadvantages, other security features, which have been discussed above in chapter comparison of Whonix, Tails and Tor Browser bundle, such as UTC timezone, fingerprinting didn't appear worthwhile to compare.

### License ###
<font size="-3">Thanks to [JonDos](https://anonymous-proxy-servers.net/) ([Permission](https://anonymous-proxy-servers.net/forum/viewtopic.php?p=31220&sid=ac8a6ca16eb768b3322be30b20375c97#p31220)). The "Whonix Comparison of Whonix, Tails, Tor Browser Bundle and CGIproxies" chapter of the "Whonix Comparision with Others wiki page" contains content from the JonDonym documentation [Other Services](https://anonymous-proxy-servers.net/en/help/otherServices.html) page.</font>

## Comparison of Tor and Proxy Chains ##
### Aren't 10 proxies (proxychains) better than Tor with only 3 hops? - proxychains vs Tor ###
Maybe you've seen the funny picture "I am behind 10 proxies, so what?". Nevermind.

10 open proxies are not as secure as Tor. Many people are not aware of that.

As outlined above, proxies are not very secure.

With Tor the first hop won't see the IP of the last hop because it can't decrypt the message for the second hop. If one hop can be trusted, the connection is secure (see the onion design).

Even if you are using "elite" or "anonymous" proxies... Or even Socks Proxies...

* All connections between you and all proxies are unencrypted.
* This has nothing to do with SSL, but for demonstration, let's assume you are connecting to an SSL protected web server.
* In human understandable form, this is a sketch how the package for the first proxy in your chain of 5 would look like:
* Hey Proxy1, can you please forward "forward to Proxy3; forward to Proxy4; forward to Proxy5; forward to https://encrypted.google.com 'c8e8df895c2cae-some-garbage-here-(encrypted)-166bad027fdf15335b'" to Proxy2? Thanks!
* You see, your actual transmission will be safely encrypted and can be only decrypted by the https protected webserver, but every proxy will see it's predecessor IP and all successor IP's.
* There is no way to encrypt that information, no way to make your own onion. The proxy protocols (http(s), socks4(a)/5) do not support encryption.

As you would have to trust any of them the IP of all it's successors... The second question about open proxies is, who hosts them?

* most of them are a simple misconfiguration, the owners are not aware of it and do not want the public to use them
* many of them are compromised machines (worm infected)
* some are honeypots, logging or exploiting (dns spoofing, protocol spoofing, ssl spoofing)
* few of them are are from generous people who just want your best and give you anonymity (similar to most Tor server admins)

This must not apply for proxychains of SSH and/or encrypted VPN servers - has not been researched yet. But you can not get so many SSH and/or VPN servers for free (without hacking of course) and/or anonymous payment anyway.

### License ###
<font size="-3">License of "Comparison of Tor and proxychains": This was originally posted by adrelanos (proper) to the [TorFAQ](https://trac.torproject.org/projects/tor/wiki/doc/TorFAQ#Arent10proxiesproxychainsbetterthanTorwithonly3hops-proxychainsvsTor) ([license](https://trac.torproject.org/projects/tor/wiki/doc/LegalStuff)). Adrelanos didn't surrender any copyrights and can therefore re-use it here. It is under the same license as the rest of the page.
</font>

## Comparison of Tor and VPN services ##
### Comparison ###
If you run the VPN software directly on the same machine as also the client software such as web browser runs, [active contents](https://sourceforge.net/p/whonix/wiki/DataCollectionTechniques/#active-web-contents) can read your real IP address. This can be prevented, if you use a virtual or physical VPN-Gateway or your router. However, please note that active contents may still read a lot of data about your computer and network configuration.

* Some providers force the user to use their proprietary closed source software and have no option to allow being used by reputable VPN software, such as OpenVPN.
* On one hand, their software usually does not ensure, that users also have an uniform appearance on the Web aside their IP address (see [Data Collection Technique](https://sourceforge.net/p/whonix/wiki/DataCollectionTechniques/)). The users are thus distinguishable and easily identifiable by merging the data.
* And on the other hand, a local observer on your network (ISP, WLAN) could guesstimate websites requested over VPN simply by analyzing size and timing of the encrypted VPN data stream. Tor is quite resilient against this attack (a scientific article which demonstrates the attack is found [here](http://epub.uni-regensburg.de/11919/1/authorsversion-ccsw09.pdf); the success rates are over 90% for VPNs).
* Moreover, VPN systems, as inherent to their functional principle, normally do not filter or replace your computer's TCP packets. They thereby do not protect you from [TCP timestamp attacks](https://sourceforge.net/p/whonix/wiki/DataCollectionTechniques/#tcp-timestamps) as Tor does.
* Even when using a virtual or physical VPN-Gateway, due to browser fingerprinting problems it's only [pseudonymous rather than anonymous](https://sourceforge.net/p/whonix/wiki/DoNot/#do-not-confuse-anonymity-with-pseudonymity).
* You should also keep in mind that VPN hosts can, unlike Tor, can track and save every step of yours, since they control all servers in the VPN.
* VPN providers only offer privacy by policy, while Tor offers privacy by design. A VPN provider can claim not to log, but you'll never know until it's too late. When using Tor, you also never know, if any of the three hops keeps logs. One malicious node will have less impact. The entry guard will not know where you are connecting to, thus it's not a fatal problem if they log. The exit node won't know who you are, but can see your unencrypted traffic, which can be a problem if you send sensitive data (which you are advised not to do), but if you act accordingly, it isn't a problem. It's unlikely (thus not impossible), that you choose a circuit where an adversary controls all three nodes. However, while using VPN providers you're putting all trust into the policy of one provider, using Tor distributes trust.
* Don't get fooled by advertisements for Double, Triple or Multi Hop VPNs. Unless it's the user, who builds it's own custom VPN chain by carefully choosing different VPN providers, owned by different companies, you're still fully trusting only one provider.

Whether it's worth to combine Tor with a VPN, either as pre-Tor-VPN (user -> VPN -> Tor) or as post-Tor-VPN (user -> Tor -> VPN) is quite a controversial topic and discussed on the [Tor plus VPN](https://trac.torproject.org/projects/tor/wiki/doc/TorPlusVPN) ([w](http://www.webcitation.org/6FPudSpvr)) page. In case you decide to do so, it's easy with Whonix, see [VPN/Tunnel Support](https://sourceforge.net/p/whonix/wiki/Features/#vpn-tunnel-support).

### License ###
<font size="-3">Thanks to [JonDos](https://anonymous-proxy-servers.net/) ([Permission](https://anonymous-proxy-servers.net/forum/viewtopic.php?p=31220&sid=ac8a6ca16eb768b3322be30b20375c97#p31220)). The "Comparison of Tor and VPN services" chapter of the "Whonix Comparision with Others wiki page" contains content from the JonDonym documentation [Other Services](https://anonymous-proxy-servers.net/en/help/otherServices.html) page.</font>

# Footer #
[[include ref=WikiFooter]]