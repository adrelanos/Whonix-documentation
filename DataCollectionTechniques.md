[[include ref=WikiHeader]]

[TOC]

# Data Collection Techniques

The actual techniques employed by the data miners on the Web are briefly introduced below.

## Cookies

Cookies are used to identify and remember a web surfer. Without cookies, certain services would be complicated to realize. If a user requests a page from a webserver, it cannot readily match requests of previous pages requested from this server to that same user. HTTP is a stateless protocol.

Nevertheless, some services require a sort of memory. Shopping portals are an example: a server has to remember what goods were placed into the virtual shopping cart. This "memory" is usually written into cookies, i.e. small text files which are being sent to you by the server upon every page request. When your browser contacts the server again, it also
automatically sends back the cookie stored earlier. The server thereby allocates the right shopping cart to you.

But cookies can also be abused to track your steps on the Internet. This works exceptionally well with web portals (e.g. Yahoo) and search engines (e.g. Google) for you use these a lot in order to reach other websites. With cookies, a web host can record large parts of your surfing behavior over years and easily relate it to you as a person with
your "accumulated" profile data. Most Internet users have collected hundreds of cookies from various websites on their PC without their knowledge. The following example shows you just a small amount of cookies you get if you request *www.nytimes.com*:

![Cookies set by nytimes.com](http://whonix.sourceforge.net/pictures/cookies_nytimes.png)

Websites embedding several external ad and tracking services is nothing unusual. A [study by University Berkeley](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=1898390) done in 2011 has analyzed the top 100 websites and found 5,675 cookies. Thereby 4,914 cookies were set by third parties, i.e. not by the website the user visited intentionally. While surfing on these 100 websites data to 600 servers was transmitted with the help of those cookies.

Modern browsers usually integrate an optional function for this, but it has to be activated by the user first. In [TorBrowser] (come with Whonix) it has been made default and you will get some more functions to administrate your cookies collection and preferences.

## Evercookies

More than 80% of the users disapprove of tracking while surfing the web. Many surfers use browser settings which prevent a long-term tracking. Therefore, ad and tracking networks are moving on to use more sophisticated methods to distinguish each user.

-   Flash-Cookies (LSOs) are deployed since several years to recover deleted cookies with the same identification mark. Clearspring Technologies Inc. has been using this technique successfully (untilit got sued in 2010) and promotes its precise data of 200 million Internet users.
-   In a [study of the University of California, Berkeley](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=1898390) the methods of Space Pencil, Inc., aka KISSmetrics, were exposed which, in addition to cookies and flash cookies, used cache cookies via ETags, DOMStorage and IE-userData in order to distinguish each user. KISSmetrics got sued as well and is going to dispense with using Etags. Rather, it is going to respect the HTTP header [Do Not Track](http://donottrack.us/).
-   The tracking service [Yahoo! Web Analytics](http://help.yahoo.com/l/us/yahoo/ywa/documentation/install_guide/ig_get_started.html) is bragging about being able to set cookies on 99,9% of the users. This[indicates](http://smorgasbork.com/component/content/article/84-a-study-of-internet-users-cookie-and-javascript-settings) that [cookie generating JavaScript](http://www.truststc.org/reu/10/Reports/GomezG,YalajuJ_paper.pdf) is deployed and/or e.g. Flash cookies are added as well.
-   Samy Kamkar shows with [evercookie - never forget](http://samy.pl/evercookie/) further possible methods to mark Internet users individually.

[TorBrowser] (comes with Whonix) resists evercookies.

## Active Web Contents

Webcontent accessible by browser plugins such as Flash, Java, ActiveX and Silverlight renders the Web more dynamic and colorful but also more dangerous, for they allow websites to execute code on your PC. If executed, these plugin contents are able to read some details about your computer and network configuration and send it to the web server. By certain manipulations they moreover can read and edit files on your machine and in an extreme case even gain complete control over it.

Especially beware signed Java applets: by accepting its signature, the applet, and thereby the visited webserver, automatically receives all user rights on your machine. In particular, it may then read your [IP address](#ip), your [MAC address](https://sourceforge.net/p/whonix/wiki/DataCollectionTechniques/#mac-address) and even hard disk contents. It does not help to only surf websites you deem trustworthy either. This concept is outdated since nowadays even numerous large and notorious websites are being hacked and filled with malicious code. Only blocking/deactivating these plugin contents provides real security.

In Whonix reading the IP address wouldn't give meaningful results. It's either a local IP address shared among all Whonix users or the IP of a Tor exit node, which is safe as well. [MAC address](https://sourceforge.net/p/whonix/wiki/DataCollectionTechniques/#mac-address) is a virtual one and shared among all Whonix users as well, therefore meaningless. Active content, although it couldn't reveal your real [IP address](#ip), is deactivated in Tor Browser by default. See [BrowserPlugins] for a detailed anonymity, security and privacy discussion of browser plugins in Whonix.

## JavaScript

The browser is a bit better protected against attacks on your privacy using the scripting language *JavaScript* ("scripts", "active scripting") than against those using the aforementioned plugins. But it is not completely safe, though. JavaScript is not to be confused with *Java* or the *active Java plugin*, respectively, which is a completely different thing despite the similar name (see above).

It is possible to compromise your browser or operating system using software bugs or a bad designed website. An attacker can e.g. inject malicious JavaScript code by [Cross Site
Scripting](http://en.wikipedia.org/wiki/Cross-site_scripting) and thus try phishing for login creditials, bank accounts or other sensitive data.

Using JavaScript it is possible for web masters to access many information about your browser, your desktop settings and your hardware. All these information may be accumulated to an individual fingerprint of a particular user. By this fingerprint a user may be recognized. The anonymity test [ip-check.info](http://ip-check.info/?lang=en) shows **only some examples** of values which maybe gathered (JavaScript needs to be enabled). It demonstrates the labeling of users by JavaScript, too (same effect like cookies).

[ip-check.info some false values and confuses TBB users](https://anonymous-proxy-servers.net/forum/viewtopic.php?f=10&t=7319)

<s>Therefore, we recommend you to only activate JavaScript contents if needed and to block them otherwise.</s> <font size=-3>[Tor Browser disabling Javascript anonymity set reduction](https://lists.torproject.org/pipermail/tor-talk/2012-May/024224.html)</font>

To conclude the last two paragraphs (Active Web Contents/JavaScript): You should not surf the Internet without a well secured browser, as your PC is otherwise in danger of being attacked quite soon. Instead of configuring the browser yourself, which takes quite some experience, you may use for example [TorBrowser] (comes with Whonix). It looks like Mozilla Firefox and does not only block most dangerous technologies at default it is also equipped with further ample security mechanisms. Most websites will still be reachable. YouTube videos and videos of other such portals which are rendered by Flash may be downloaded with special software and then viewed with a video player. Websites which demand usage of active plugins should be avoided if possible, otherwise see [BrowserPlugins]

## Fingerprinting of Browser (HTTP) Header

With every request for a webpage, browsers send information within the framework of the HTTP protocol that can be analyzed by the visited site: language, browser name and version, operating system and version, supported charsets, files, codecs and the last visited webpage. Sending these headers is usually not necessary for rendering websites, but it can be exploited for reidentifying, profiling and analyzing websurfers. The project [Panopticlick](http://panopticlick.eff.org) of the EFF demonstrated browser fingerprinting. Most surfers are traceble by an unique browser fingerprint.

As of today, different filter applications and services have been developed that allow hiding or changing problematic browser headers (e.g. Privoxy). Unfortunately, these applications cannot filter encrypted connections: once you load a presumably "secure" website (HTTPS, browser lock) all filtering fails. Plus, these programs allow every user to define the header data himself. But setting an individual browser type e.g. is in itself what renders you quasi perfectly trackable. [TorBrowser] always sends the same profile for encrypted connections too. This guarantees that websites may at maximum realize that it is a Tor Browser user visiting, but not who.

<font size="-3">
[Tor Blog: EFF's Panopticlick and Torbutton](https://blog.torproject.org/blog/effs-panopticlick-
and-torbutton)
</font>

Fingerprinting defense isn't perfect yet in any browser. There are still open bugs. <font size="-3">(See [tbb-linkability](https://trac.torproject.org/projects/tor/query?status=accepted&status=assigned&status=needs_information&status=needs_review&status=new&status=reopened&order=priority&col=id&col=summary&col=keywords&col=status&col=owner&col=type&col=priority&keywords=tbb-linkability) and [tbb-fingerprinting](https://trac.torproject.org/projects/tor/query?status=accepted&status=assigned&status=needs_review&status=needs_revision&status=new&status=reopened&order=priority&col=id&col=summary&col=keywords&col=status&col=owner&col=type&col=priority&keywords=tbb-fingerprinting).)</font>

## Browser History and Cache

A [publication of the from the University of California](http://cseweb.ucsd.edu/users/lerner/papers/ccs10-jsc.pdf) provide an analyses of the TOP 50.000 websites. 1% of these websites
collect information about web surfers by history sniffing. Using malicious JavaScript code and CSS hacks information about visited websites were collected. Webmasters who are not familiar with sniffing technologies can use services like Tealium or Beencounter for real-time history sniffing.

Collected information are not only used for advertisements. It can be uses for de-anonymisation of surfers too. A [publication of Isec](http://www.iseclab.org/papers/sonda-TR.pdf) shows a possible way. Using the browser history the visited groups of the social network Xing were collected. Because there are not two people members of the same groups in a social network it was possible to get the real names and e-mail addresses.

By certain trickery, websites can tell which other websites are saved in your browser history. For this, the visited website embeds special formatting commands (CSS, Stylesheets) that contain external links "of interest" on the pages you visit. If you have visited one of the external websites, your browser will react by executing a command defined in the format, e.g. download a small picture form the website. The website can thereby completely or largely guess the contents of your browser history.

From the contents of your browser cache one can conclude on previously visited, thus already cached, websites. Together with every website an ETag is send by the server and stored in the browser cache. If the website was called again, the Etag is send first to ask for changes. This tag may contain an unique user ID. [KISSmetrics](http://www.kissmetrics.com/) was using ETags in this way to identify visitors of some TOP100 websites.

Additionally, the time required for loading a website changes when part of it is already in the browser cache. By subtle placement of the images on the website, the server can analyze the cache one by one.

At the moment, there is no reliable protection against the analysis of browser histories apart from deactivating this feature, which has been made default in Tor Browser.

Unlike deactivating your browser history, deactivating your cache would have tremendous effect on your surfing speed, which is why we don't recommend it. IN Tor Browser a protective mechanism has been integrated instead which bypasses cache for third party content. Also, the cache is deleted automatically when you close the browser. A website can thus no longer gain information about other websites, only about itself.

## Webbugs and Banner Ads

Very likely, you will find one or more [cookies](#cookies) in your browser from data miners such as [doubleclick.com](http://www.doubleclick.com/), [advertisement.com](http://www.advertisement.com/) or [Google](http://www.google.com), although you have never even visited their websites. This is due to the fact that these enterprises use, on other web sites, a simple trick to nevertheless plant cookies on you and watch your browsing: *Webbugs*.

"Webbugs" are usually pictures of 1x1 pixels and therefore invisible to the viewer. However, they can also be coded into banner ads embedded in a website. The website contains a picture (webbug) that is loaded from another server running a statistics service (such as Doubleclick, Google Analytics). Thereby the statistics service may set or edit a cookie in your browser unnoticeably. The browser will then send this cookie back to the statistics service with every new request for a site where any webbug of this service is embedded. If the service is used on many different websites, it can now track large parts of your browsing session. If the owner of the statistics service moreover collaborates with the owner of your preferred search engine, he gets an almost complete picture of your Internet activities.

The privacy functions of most current browsers that either flatly deny cookies or only deny third party cookies, and alternatively also delete all cookie data when closing the browser, do not achieve optimal protection.

<s>? To prevent session tracking, all cookies should be blocked by default if possible and only allowed in if needed for the duration of the session. Tor Browser is therefore preconfigured to deny all cookies but allow single websites at the expense of two mouse clicks. We recommend allowing cookies only on a temporary basis, so that they will be automatically blocked again after the session. ?</s>

Another nasty feature of webbugs is, that they send, besides cookies, also your [IP address](#ip) to the statistics service upon request. Even with a very good browser configuration, by switching off cookies and by using webbug filters, you are never able to reliably prevent this. The only effective protection against this are anonymisation services like Tor.

## TCP Timestamps

The Transmission Control Protocol (TCP) is a protocol for transferring data between computers. It is necessary for using Internet services like http (WWW), smtp (E-Mail) and ftp. When your computer sends a request for a web site, for example, this data is sent within many small so-called TCP packets. Besides that request data, such a TCP packet also
contains some optional information fields (optional headers). One of those options is the TCP timestamp. The value of this timestamp is proportional to the current time of your computer and is incremented according to your computer's internal clock.

The timestamp may be used by the client and/or server machine for performance optimization. However, an Internet server may recognize and track your computer by observing those timestamps: By measuring the clock skew of the timestamps, it may calculate an [individual clock skew profile](http://www.cs.washington.edu/homes/yoshi/papers/PDF/) for your computer. Moreover, it may estimate the time when your machine was last booted. These ricks work even if you have otherwise perfectly anonymised your Internet connections.
 
If you were using Whonix, you are however protected against being observed this way. The clock in Whonix-Workstation does not match your clock on the host and the clock in Whonix-Workstation is set by tails_htp over https, which will result in slightly different results compared using the more accurate NTP.

If you were using Tor, you are however protected against being observed this way: The Tor relays automatically replace your potentially insecure TCP packets by their own.

<font size="-3">
[source 1: Tor trac #8169 replace TCP timestamp](https://trac.torproject.org/projects/tor/ticket/8169)
[source 2: Tor wiki FAQ](https://trac.torproject.org/projects/tor/wiki/doc/TorFAQ#DoesTorresistremotephysicaldevicefingerprinting)
</font>

## IP Address

The IP address is given to you by your provider on dialing into the Internet. The provider usually saves it for months or even years together with your customer data and your online time. It is your distinct identifier on the Internet which is sent along whenever you make a direct connection to any Internet service. The IP address tells the server where to send his response. As long as your IP does not change, it is easy to monitor when and what website you have contacted. The IP also reveals your provider, many times your location and sometimes (in case of a company or computer center) even what terminal you are on. In many cases, an IP address relates directly to one person.

All that your IP-address is revealing:

- Your current whereabouts

The country and the city/region where you are. With the help of data bases [free of charge](http://www.netop.org/services/ip-geolocation) or [with costs](http://www.maxmind.com/app/ip-location) even districts and office buildings can be identified. This is called geolocation.

- Your Internet-provider

Personal data can be retrieved using your provider.

- Your access technology

With the help of data bases one can find out whether you are using, for instance, DSL, a modem or a mobile in order to surf the Web.

- Your company / your authority

In case you are surfing from within the network of a company or an authority its name can be find out.

Some of the information that is given away by your IP or browser can be reviewed on [ip-check.info](http://ip-check.info/?lang=en).

While the traces mentioned so far can be blurred without any special services needed, the same cannot be said about your IP address. That is why Tor has been developed: In order to blur any connection between your IP and the websites you visit. Whonix connects to the service Tor network. <font size="-3"[How Tor works](https://www.torproject.org/about/overview.html.en)</font>

## MAC Address

The MAC address (MAC=Media-Access-Control, sometimes also called *Ethernet-ID*, *Airport-ID* or *physical address*) is the hardware address of each individual network device. Each computer may have several of such physical or virtual network devices (bound to a cable *(LAN)*, wireless *(WLAN)*, mobile *(GPRS, UMTS)*, virtual *(VPS)*, ...). The MAC address serves as a unique identifier for the respective device in a local area network. On the Internet, it is neither used nor transmitted. Also, your access provider may only see it if your computer is not connected to the Internet over a router, but directly, for example by a modem. You may moreover [change the MAC address yourself](http://translate.google.com/translate?hl=en&sl=de&tl=en&u=http://de.wikipedia.org/wiki/MAC-Adresse).

There is an extra chapter about the [MAC address later in documentation in the Pre Install Advice](https://sourceforge.net/p/whonix/wiki/Pre%20Install%20Advice/#mac-address).

# License
<font size="-3">Thanks to [JonDos](https://anonymous-proxy-servers.net/) ([Permission](https://anonymous-proxy-servers.net/forum/viewtopic.php?p=31220&sid=ac8a6ca16eb768b3322be30b20375c97#p31220)) ([w](http://www.webcitation.org/6EBuJGESE)). The DataCollectionTechniques page contains content from the JonDonym documentation [DataCollectionTechniques](https://anonymous-proxy-servers.net/en/help/wwwprivacy_technik.html) page.</font>

# Footer #
[[include ref=WikiFooter]]