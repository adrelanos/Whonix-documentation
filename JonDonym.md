[[include ref=WikiHeader]]

[TOC]

# JonDonym #
## Introduction ##
**adrelanos's JonDonym opinion**

JonDonym is an alternative anonymity network which will be compared with Tor in this Introduction chapter. It's easy to tunnel JonDonym over Tor inside Whonix-Workstation which we go into in the next chapter. In theory, Tor on Whonix-Gateway could be replaced with JonDo.

The [JonDonym network](https://anonymous-proxy-servers.net) is much smaller than the Tor network. At time of writing ([February 2012](http://www.webcitation.org/6EDKqyxBU), snapshot random week day, random time), there were 5 two hop free mix cascades, 11 three hop premium mix cascades and 1 test/experimental free one hop service.

The two hop free mix cascades had 1940 users with a maximum available capacity of 2750 users. 1367 users were using the test/experimental free one hope service which didn't advertise a maximum user capacity. From 16 to 63 users used one of the 11 three hop premium mix cascades and no maximum user restriction was advertised. There were 350 premium users in total.

In comparison, according to Tor metrics page ([on that day](http://www.webcitation.org/6EDLmOK0g) the Tor network had on that day had ~3000 relays. (~1000 had the guard flag and ~900 hard the entry guard flag, i.e. where useable in that position.) ~500.000 users were using the Tor network [on that day](http://www.webcitation.org/6EDMD01pu).

The path (circuit), Tor client chooses is non-predictable and changes every 10 minutes while in comparison to JonDonym, for example a user who has chosen the Speedy-Sektor free two hop mix cascade, will have a predictable entry and exit until the user manually changes it. That goes for all mix cascades. If someone knows the entry or exit, the whole path the client is using through the network is known.

The Tor network is run by volunteers from many different countries. There is no formal process to apply as a Tor node and no verification of identity for Tor node admins. Anyone can download the Tor software and volunteer a node. Therefore there are legit and malicious nodes.

In comparison to JonDonym, mix servers are operated by independent and non interrelated organizations or private individuals who all [publish their identity](https://anonymous-proxy-servers.net/en/help/certificates.html). The operators have to abide by strict provisions which prohibit saving connection data or exchanging such data with other operators.

While private data such as usernames and passwords have been already sniffed by Tor exit nodes on unencrypted or sslstripped connections, no such headline about JonDonym. Tor clearly states, that unencrypted connections can be sniffed by Tor exit nodes. ([Exit Nodes Eavesdropping](https://sourceforge.net/p/whonix/wiki/Warning/#tor-exit-nodes-can-eavesdrop-on-communications)) Trusting in JonDonym is more like trusting in their policy and server administration skills. Neither the mix server administration nor the JonDo software can prevent a man-in-the-middle attack between the mix server and the destination server.

JonDonym might be faster than Tor.

Quoted from the JonDonym [Law enforcement](https://anonymous-proxy-servers.net/en/law_enforcement.html) page ([w](http://www.webcitation.org/6EDOc3Gfi)).:

>*JonDonym does not make it impossible to uncover individual users, as there is no such thing as a 100% security. However, such a disclosure is by magnitudes more difficult than for other VPN or proxy services, as this would require the cooperation of several states and organizations.*
>
>*JonDonym is no technology for preventing law enforcement on the internet. In very serious cases, it is possible to uncover the abuse of Mix services. User connections may be individually observed, if all operators of a Mix cascade get such an official order, valid in their respective country (in Germany accourding to §100a/b StPO).*
>
>*A respective legal obligation may moreover force some Mix operators to retain certain connection data. In contrast to surveillance (where this is often not allowed), the operator has to make this transparent to the users of his JonDonym Mixes via JonDo. Usually, such a data retention does neither comprise target addresses (websites) nor contents, but IP addresses of users only. At the moment no JonDonym mix operator retain connection data.*
>
>*However, the independence of JonDonym operators vastly lowers the danger of an illegitimate law enforcement done by non-democratic states or arbitrary individual public officers. Any disclosure basically needs the cooperation of all operators of a Mix cascade. This was never realized for premium mix cascades in the past.*
>
>*Surveillance reports*
>
>*Each year, we will publish a short report of all surveillance actions that were taken and have been reported to us by the operators.*
>
>*In 2012 there has been one surveillance court order to all German mix operators and JonDos GmbH. It concerned one JonDonym account number which was known to the law enforcement agency before start of surveillance. No premium cascade and no free cascade was able to provide the requested communication data because not all operators of any cascade got a court order.*
>
>*\[...\]*
>
>*If single mix operators inform JonDos GmbH about a surveillance court order then that does not mean JonDonym as a whole has been under surveillance or JonDos GmbH was involved. Rather, single operators had to comply with these orders.*

In summary there where surveillance court orders for the last four years, but until now, no JonDonym user has ever been de-anonymized. The Tor network also suffers from legal attacks, there have been some raids of Tor exit servers, which also didn't and couldn't lead to de-anonymization. Both networks, when correctly used, i.e. not de-anonymizing oneself by posting private information, without connecting once without going through the anonymity network, without proxy bypass, without viruses, following documentation and so on, ever had any news headlines about network compromise.

The JonDo developers, although they are selling a product, seem to be honest about their network. They are also generally friendly (Whonix is allowed to re-use their documentation content under Open Source license with or without modification to improve Whonix documentation) and are also constructively participating the Tor bug tracker. It will be interesting if and what they answer will be on the thread "[ip-check.info some false values and confuses TBB users](https://anonymous-proxy-servers.net/forum/viewtopic.php?f=10&t=7319)" ([w](http://www.webcitation.org/6EDOL0OdY)).

The JonDonym receives much less attention from security researchers compared to Tor.

In some aspects JonDonym is more/less secure than Tor. Depends on your threat model Reading [network comparison](https://anonymous-proxy-servers.net/en/help/jondonym.html) and [law enforcement](https://anonymous-proxy-servers.net/en/law_enforcement.html) yourself may be worth reading.

Tunneling JonDonym over Tor makes sense in some cases. I wouldn't do it for a longer amount of time, as it adds a permanent exit server. (See [Tor plus VPN or proxy](https://trac.torproject.org/projects/tor/wiki/doc/TorPlusVPN) for background.)

Conclusion: if you want to download something, which you can not download over SSL (and if there are also no hash sums or signatures), the JonDo exit might be, in your threat model, more trustable than a random Tor exit. However, you could also try to use a specific Tor exit form someone you trust.

Q/A:

According JonDo, is it safe to tunnel JonDonym over Tor (user -> Tor -> JonDonym)?

According to JonDo, yes.

Quoted from the JonDonym [network comparison](https://anonymous-proxy-servers.net/en/help/jondonym.html) page.

> *\[...\] making surfing considerably slower but, in some individual cases, even more secure than with JonDonym alone.*

<font size="-3">
According to the JonDonym page, chapter [Access to the Tor network with JonDo](https://anonymous-proxy-servers.net/en/help/services_tor.html), JonDo natively supports to get tunneled over Tor. This also implies, that the JonDo developers do **not** argue, that tunneling JonDo through Tor is any less safe. Having such an option helps JonDo users to tunnel through Tor (user -> Tor -> JonDonym). You won't need this option in Whonix, since all traffic originating from Whonix-Workstation, will be tunneled through Tor first in any case. Enabling that JonDo option is inside Whonix-Workstation is discouraged, since it would lead in Tor over Tor.
<font size="-3">

## JonDonym over Tor inside Whonix-Workstation ##
You can tunnel JonDonym over Tor. This could be useful, to circumvent Tor bans. But note [Tor Plus VPN or Proxy](https://trac.torproject.org/projects/tor/wiki/doc/TorPlusVPN) (it adds a permanent exit node, like explained and the article). Not many changes are required. Either [download](https://anonymous-proxy-servers.net/en/software.html) and install it as usual. You need 'JonDo – the IP changer', either as the gui or console version.

Or you could try to install from their GNU/Linux repository. They have their own documentation page about the [JonDo repository](https://anonymous-proxy-servers.net/en/help/firststeps2.html). Whonix is based on Debian Wheezy. The only difference when using their repository instructions is, that your distribution is wheezy and not maverick.

You must make an informed decision, if you prefer to use JonDoFox or the Tor Browser.

A quick thought tells me, that blending in with JonDo users, i.e. using JonDoFox in this case would make more sense - could be wrong. No special settings would be required in this case.

If you want to use the Tor Browser for surfing -> user -> Tor -> JonDonym -> destination server, you have to change the proxy settings in Tor Button. That's a little bit tricky. It would help, if you already read the [Tor Browser](https://sourceforge.net/p/whonix/wiki/TorBrowser/) article, especially the [Tor Browser - Whonix Proxy Settings / user.js](https://sourceforge.net/p/whonix/wiki/TorBrowser/#whonix-proxy-settings-userjs) chapter. You would have to remove all proxy settings from *user.js*. Then start Tor Browser, open Tor Button settings, choose custom proxy settings, http 127.0.0.1 port 4001 and leave all other fields expect no proxy for 127.0.0.1 free. You can check http://ip-check.info/ if it's working. It was once tested when writing these instructions and is certainly possible. If it doesn't work for you and you are interested, please ask in the Whonix user help forum.

If you are interested in a development discussion about JonDo(Fox) getting pre-installed on Whonix, see [Dev_JonDo].

## JonDonym as Tor replacement (JonDoBOX) ##
Was just a development idea with some progress. Moved to [Inspiration].

# License #
<font size="-3">Thanks to [JonDos](https://anonymous-proxy-servers.net/) ([Permission](https://anonymous-proxy-servers.net/forum/viewtopic.php?p=31220&sid=ac8a6ca16eb768b3322be30b20375c97#p31220)). The "Whonix JonDonym" wiki page contains content from the JonDonym documentation [Network](https://anonymous-proxy-servers.net/en/help/jondonym.html) page.</font>

# Footer #
[[include ref=WikiFooter]]