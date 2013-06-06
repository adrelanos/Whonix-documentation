[[include ref=WikiHeader]]

[TOC]

# Things NOT to do #
## I wonder what my site looks like when I'm anonymous. ##
"I wonder what my site looks like when I'm anonymous" <font size=-3>([source](https://lists.torproject.org/pipermail/tor-dev/2012-April/003472.html))</font>

It's best not to visit your own personal website where real names or pseudonyms (which have been ever tied to a non-Tor connection/IP) are attached.

This is because how many people are visiting your personal website? 90% of all Tor users or just you or just very few people? That's a weak anonymity. Once you visit a website your Tor circuit gets dirty. The exit node knows that someone visited your website and if the site is not that popular, it's a good guess that this someone was you. It wouldn't be hard to assume that further connections originate that exit node come from your machine.

<font size="-3">Source: [Tor Browser should set SOCKS username for a request based on referer](https://trac.torproject.org/projects/tor/ticket/3455).</font>

## Login into your real life Facebook account and think you are anonymous. ##
Don't login into your personal Facebook account. No matter if your real name is attached or only a pseudonym. You most likely added your friends and they know who the account belongs to. Through your social network Facebook can guess who you are.

No anonymity solution is magic. Online anonymity software may reliable hide your IP/location. But Facebook does no longer need your IP/location. They already know who you are, who your friends are, which private messages you send and so on. All those data is at least stored on Facebook server. No kind of software can delete that data. Only Facebook and crackers could.

So if you log into your personal Facebook account you only get location privacy. No anonymity.

<font size=-3>
Quoted from [The Tor Blog: To Toggle, or not to Toggle: The End of Torbutton](https://blog.torproject.org/blog/toggle-or-not-toggle-end-torbutton): *"mike, am i completely anonymized if i log onto my facebook account? im using firefox 3.6 with tor and no script on windows 7 machine. thank you."*.
</font>

## Never login into accounts you ever used without Tor. ##
Always assume that each time you visit a website, that they will log the IP/location which visited the website, at which time and what you did.

Also assume, that each time you're online your ISP (Internet Service Provider) will log your online time, IP/location and perhaps traffic. Your ISP could also log to which IPs/locations you connected, how much traffic and what you send and revived. (Unless it's encrypted, then they'll see only garbage.) The following tables should give you an simplified overview how those logs could look like.

ISP Log:

| Name | Time | IP/location | traffic
------------- |  ------------- | ------------- | -------------
John Doe | 16 pm to 17 pm | 1.1.1.1 | 500 megabytes 

[Extended](https://en.wikipedia.org/wiki/Deep_packet_inspection) ISP Log:

| Name | Time | IP/location | traffic | Destination | Content
------------- |  ------------- | ------------- | ------------- | ------------- | -------------
John Doe | 16 pm to 17 pm | 1.1.1.1 | 1 megabytes | 16.00 pm to 16.10 pm: google.com (searched for thing one, thing two...)
John Doe | 16 pm to 17 pm | 1.1.1.1 | 490 megabytes | 16.10 pm to 16.20 pm: youtube.com (view video 1, video 2, ...)
John Doe | 16 pm to 17 pm | 1.1.1.1 | 9 megabytes | 16.20 pm to 16.30 pm: facebook.com (encrypted traffic)

Website Log:

| Time | IP/location | traffic | Content
------------- |  ------------- | ------------- | ------------- | ------------- | -------------
16.00 pm to 16.10 pm | 1.1.1.1 | 1 megabytes | searched for thing one, thing two...

You'll see, when websites and ISP keep logs, no one needs Sherlock Holmes to conclude.

If you mess up for one time, and login with a non-Tor connection/IP, which can be tied to you, then the whole account is compromised.

## Don't login into your bank account, paypal, ebay or other important personal accounts unless... ##
Logging into your bank, paypal, ebay or other important personal accounts registered on your name where money is involved could risk, that your account gets suspended, due to "suspicious activity" by the fraud prevention system. This is because crackers sometimes use Tor for committing fraud. That's probable not what you want.

It's not anonymous for reasons already explained. It's pseudonymous and offers circumvention (in case access to the site is blocked by your ISP) and location privacy. The difference of anonymity and pseudonymity is covered in a later chapter on this page.

In many cases you will be able to contact the support and to get your account unblocked again or on request, even the fraud protection policy gets relaxed for your account.

Whonix developer adrelanos is not against using Tor for circumvention and/or location privacy, you just should know the risk of your account getting (temporarily) suspended and the other things mentioned on this page and the other warnings from the Whonix documentation. So if you know what you are doing, feel free.

## Don't alternate Tor with open WiFi. ##
You may think open WiFi is faster and equally safe as Tor since the IP/location can not be tied to your real name?

Better use an open WiFi AND Tor, but not or.

The approximate location of any IP address can be tied down to a city, region or even a street. Even if you are already away, you still gave away your city or approximate location since most people don't switch the continent.

While this doesn't break your anonymity, the circle of suspects decreased from the world, a continent or the country to a region. This strongly hurts your anonymity. Keep as many pieces of information for yourself.

## Prevent Tor over Tor scenarios. ##
**Whonix specific.**

When using a transparent proxy (Whonix includes one), it is possible to start a Tor session from the client as well as from the transparent proxy, creating a "Tor over Tor" scenario. 

This happens when installing Tor inside Whonix-Workstation or when using the Tor Browser Bundle without configuring it to use a SocksPort instead of the TransPort. (Covered in the [Tor Browser](https://sourceforge.net/p/whonix/wiki/TorBrowser/) article.)

Doing so produces undefined and potentially unsafe behavior. In theory, however, you can get six hops instead of three, but it is not guaranteed that you'll get three different hops - you could end up with the same hops, maybe in reverse or mixed order. It is not clear if this is safe. It has never been discussed.

You can [choose an entry/exit point](https://www.torproject.org/docs/faq.html.en#ChooseEntryExit), but you get the best security that Tor can provide when you leave the route selection to Tor; overriding the entry / exit nodes can mess up your anonymity in ways we don't understand. Therefore Tor over Tor usage is highly discouraged.

<font size="-3">License of "Prevent Tor over Tor scenarios.":
This was originally posted by adrelanos (proper) to the [TorifyHOWTO](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO#ToroverTor) ([w](http://www.webcitation.org/6GmyI6qMN)) ([license](https://trac.torproject.org/projects/tor/wiki/doc/LegalStuff)) ([w](http://www.webcitation.org/6GmySlraB)). Adrelanos didn't surrender any copyrights and can therefore re-use it here. It is under the same license as this DoNot page.
</font>

## Don't send sensitive data without end-to-end encryption. ##
As already explained on the [Warning] page, Tor exit nodes can eavesdrop on communications and other Man-in-the-middle attacks can happen. The only way to get sensitive data from the sender to the recipient while withholding it from third parties, is using end-to-end encryption.

## Don't disclose identifying data about yourself. ##
Deanonymsation is not only possible with connections/IP addresses but by social threats too. Some recommendations to avoid deanonymisation collected by Anonymous:

 * Do not include personal informations in your nickname
 * Do not discuss personal informations, where you are from...
 * Do not mention your gender, tattos, piercings or physical capacities.
 * Do not mention your profession, hobbies or involvement in activist groups.
 * Do not use special characters on keyboard, which are existent only in your language.
 * Do not post informations to the regular internet while you are anonymous. Do not use Twitter and Facebook. This is easy to correlate.
 * Do not post links to facebook images. The image name contains a personal ID.
 * Do not connect to same destination at the same time. Try to alternate.
 * IRC, other chats, forum, mailing list, etc. are public, keep that in mind.
 * Heroes only exist in comic books keep that in mind! There are only young heroes and dead heroes.

If it's a must to disclose identifying data about yourself, treat it as "sensitive data" in the point above.

<font size="-3">License: From the [JonDonym documentation](https://anonymous-proxy-servers.net/en/help/anonymous-irc.html) ([Permission](https://anonymous-proxy-servers.net/forum/viewtopic.php?p=31220&sid=914c87f9be91ef7afaa638d1d7f2a881#p31220)).</font>

## Do use bridges if you think Tor usage is dangerous/suspicious in your country. ##
Quoted from the [Bridges] page:
"*Bridges are important tools that work in many cases but they are **not an absolute protection** against the technical progress that an adversary could do to identify Tor users.*"

## Don't use different online identities at the same time. ##
They easily correlate. [Whonix doesn't magically separate your different contextual identities](https://sourceforge.net/p/whonix/wiki/Warning/#whonix-doesnt-magically-separate-your-different-contextual-identities).

Also read the points below.

## Don't log into Twitter, Facebook, Google, etc. longer than necessary. ##
Restrict the time your are logged in accounts for Twitter, Facebook, Google and any other account based services (web forum etc.) to the time you are using them. After you are done with reading, posting and so on, log out. At least log out, shut down Tor Browser, change your Tor circuit using a [Tor Controller](https://sourceforge.net/p/whonix/wiki/TorController/), wait a few seconds until the circuit changed, restart Tor Browser. For better security follow the [Recommendation to use multiple VM Snapshots](https://sourceforge.net/p/whonix/wiki/Security%20Guide/#recommendation-to-use-multiple-vm-snapshots) and/or to [use multiple Whonix-Workstations](https://sourceforge.net/p/whonix/wiki/Multiple%20Whonix-Workstations/).

This is because many websites include one or more of the many integration buttons, such as "I like" and "twitter this" and Google analytics, adsense etc. Those buttons tell the originating service that you visited that website because you were still logged into their service.

Also note the chapter "Don't use different online identities at the same time." above.

## Do not mix Modes of Anonymity! ##
Let us begin with an overview of the different Modes of Anonymity:

### mode(1): user anonymous; any recipient ###
* Scenario: post anonymously a message in a message board/mailing list/comment field
* Scenario: whistleblower and such
* You are anonymous.
* Your real IP/location stays hidden.
* Location privacy: your location remains secret.

### mode(2): user knows recipient; both use Tor ###
* Scenario: both sender and recipient know each other and both use Tor.
* They can communicate with each other without any third party being wise to their activity or even the the knowledge that they are communicating with each other.
* You are NOT anonymous.
* Your real IP/location stays hidden.
* Location privacy: your location remains secret.

### mode(3): user with no anonymity using Tor; any recipient ###
* Scenario: login with your real name into any services, such as webmail, Twitter, Facebook, etc...
* You are obviously NOT anonymous. As soon as you log into an account where you entered your real name the website knows your identity. Tor can not make you anonymous in these situations.
* Your real IP/location stays hidden.
* Location privacy. Your location remains secret.

### mode(4): user with no anonymity; any recipient ###
* Scenario: normal browsing without Tor.
* You are NOT anonymous.
* Your real IP/location gets revealed.
* Your location gets revealed.

### Conclusion ###
It's not wise to combine mode(1) and mode(2). For example, if you have an IM or email account and use that via mode(1), you are advised not to use the same account for mode(2). We have explained previously why this is an issue.

**It's also not wise to mix two or more modes inside the same Tor session**, as they could share the same exit node (identity correlation).

It's also possible that other combinations of modes are dangerous and could lead to the leakage of personal information or your physical location.

### License ###
<font size="-3">License of "Do not mix Modes of Anonymity!":
This was originally posted by adrelanos (proper) to the [TorifyHOWTO](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO#ToroverTor) ([w](http://www.webcitation.org/6GmyI6qMN)) ([license](https://trac.torproject.org/projects/tor/wiki/doc/LegalStuff)) ([w](http://www.webcitation.org/6GmySlraB)). Adrelanos didn't surrender any copyrights and can therefore re-use it here. It is under the same license as this DoNot page.
</font>

## Don't customize settings if you don't know their consequences. ##
Changing user interface settings for applications, which do not connect to the internet, mostly safe. For example, checking a box "don't show this tip of the day anymore" or "hide this menu bar" will have no effect on anonymity.

Look into the Whonix documentation, if changing the settings you are interested in, is documented or recommend against. Try to live with the defaults.

Changing settings for applications, which connect to the internet, even user interface settings, has to be thoroughly reviewed. For example removing a menu bar or using Full Screen in Tor Browser is recommend against. The latter is known to modify the screen size, which is bad for the web fingerprint.

You should only modify network settings with great care if you know their consequences. For example, you should stay away from the advice related to "Firefox Tuning". <font size=-3>If you believe the settings are suboptimal, the changes should be proposed upstream, so they get changed for all Tor Browser users with the next release.</font>

## Do not use clearnet and Tor at the same time. ##
Using your non-Tor browser and Tor Browser at the same time, risks that you at some point confuse one for the other and deanonymize yourself.

Using clearnet and Tor at the same time, highly risks, that you connect to any server anonymously and non-anonymously at the same time, which is recommend against. The reason for this is explained in the point below.

If you really want not to follow this recommendation, use at least two different desktops to prevent confusing one browser for another.

## Do not connect to any server anonymously and non-anonymously at the same time! ##
It's highly recommended that you do not connect to any remote server in this manner. That is, do not create a Tor link and a non-Tor link to the same remote server at the same time. In the event your internet connection breaks down (and it will eventually), all your connections will break at the same time and it won't be hard for an adversary to put the pieces together and determine what public IP/location belongs to what Tor IP/connection, potentially identifying you directly.

<font size="-3">License of "Do not connect to any server anonymously and non-anonymously at the same time!":
This was originally posted by adrelanos (proper) to the [TorifyHOWTO](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO#ToroverTor) ([w](http://www.webcitation.org/6GmyI6qMN)) ([license](https://trac.torproject.org/projects/tor/wiki/doc/LegalStuff)) ([w](http://www.webcitation.org/6GmySlraB)). Adrelanos didn't surrender any copyrights and can therefore re-use it here. It is under the same license as this DoNot page.
</font>

## Do not confuse Anonymity with Pseudonymity. ##
This chapter explains the difference between anonymity and pseudonymity. Word definitions are always a difficult topic because a majority of people has to agree with it.

An anonymous connection is defined as a connection to a destination server, where the destination server has no means to find out the origin (IP/location) of that connection nor to associate and an identifier ^1^ to it.

A pseudonymous connection is defined as a connection to a destination server, where the destination server has no means to find out the origin (IP/location) of a connection, but can associate it with an identifier ^1^.

In an ideal world, the Tor network, Tor Browser (and the underlying operating system, hardware, physical security, etc.) is perfect. For example the user could fetch a news website and neither the news website nor the website's ISP has any idea if that user has ever contacted the news website before. ^2^

The opposite of this, when using software incorrectly, for example using Firefox instead o of the Tor-safe browser Tor Browser, the original (IP/location) of a connection is still hidden, but an identifier (for example Cookies) can be used to make that connection pseudonymous. The destination website could log for example "user with id 111222333444 viewed video title a at time b on date c, video title d at time e at date f.". These information can be used for profiling. Over time these profiles become more and more comprehensive, which reduces anonymity, i.e. in worst case it could lead to de-anonymization.

As soon as someone logs into a website (for example into a forum or e-mail address) with a username the connection is by definition no longer anonymous, but pseudonymous. The origin of the connection (IP/location) is still hidden, but the connection can be associated with an identifier ^1^, i.e. in this case, an account name. Identifiers can be used to keep a log of various things. When a user wrote what, date and time of login and logout, what a user wrote, to whom the user wrote, IP address (useless, if it's a Tor exit node), browser fingerprint etc.

Maxim Kammerer, developer of [Liberté Linux](http://dee.su/liberte), has a interesting different opinion. [Quote](http://forum.dee.su/topic/anon-test-for-ll-on-ipcheck-info#65650000000264003) [(w)](http://www.webcitation.org/6EEeh3pNp) I don't want to withhold from you:

> I have not seen a compelling argument for anonymity, as opposed to pseudonymity. Enlarging anonymity sets is something that Tor developers do in order to publish incremental papers and justify funding. Most users only need to be pseudonymous, where their location is hidden. Having a unique browser does not magically uncover user's location, if that user does not use that browser for non-pseudonymous activities. Having good browser header results on anonymity checkers equally does not mean much, because there are many ways to uncover more client details (e.g., via Javascript oddities).

<font size="-3">
,,
Footnotes:
^1^ An identifier could be for example a (Flash) Cookie with an unique number.
^2^ Fingerprinting defense isn't perfect yet in any browser. There are still open bugs. ^3^
^3^ See [tbb-linkability](https://trac.torproject.org/projects/tor/query?status=accepted&status=assigned&status=needs_information&status=needs_review&status=new&status=reopened&order=priority&col=id&col=summary&col=keywords&col=status&col=owner&col=type&col=priority&keywords=tbb-linkability) and [tbb-fingerprinting](https://trac.torproject.org/projects/tor/query?status=accepted&status=assigned&status=needs_review&status=needs_revision&status=new&status=reopened&order=priority&col=id&col=summary&col=keywords&col=status&col=owner&col=type&col=priority&keywords=tbb-fingerprinting).
^4^ Reference: [Tor Blog: EFF's Panopticlick and Torbutton](https://blog.torproject.org/blog/effs-panopticlick-and-torbutton).
</font>

## Don't be the first one to spread your own link. ##
You created anonymously a blog or hidden service? Great. You have a twitter account with lots of followers, run a big clearnet news page or similar? Great. Do not get tempted to be one of the first ones who advertise your new anonymous project! The more you separate identities, the better. Of course, at some point you may or even must be "naturally" get aware of it, but be very careful at this point.

## Don't open random files or links. ##
Someone send you an pdf by mail or gave you a link to a pdf? That sender/mailbox/account/key could be compromised and the pdf could be prepared to infect your system. Don't open it with the tool you were expected to open it with. For example, don't open a pdf with a pdf viewer. If the content is public anyway, try using a free online pdf viewer.

## Don't do (mobile) phone verification. ##
Websites such as Google, Facebook and others will ask for a (mobile) phone number if you login over Tor. Unless, you are really clever or have an alternative, you shouldn't do it.

Reason:
The number you give away will be logged. The SIM card is most likely registered on your name. And even if not, receiving an SMS gives away your location. Even if you anonymously bought a SIM card and do it from a point far away from your home, there is still a risk. The phone. Each time the phone logs into the mobile network, the provider will log the SIM card serial number ^1^ AND the phone serial number ^2^. If you bought the SIM card anonymously, but not the phone, it's not anonymous, because these two serials will get linked. If you want to do it, you need a spot far away from your home, a fresh phone, a fresh SIM card, and you must turn of the phone, leave and burn the phone and the SIM card right after doing it.

You could try to find an online service receiving SMS for you. That would work and would be anonymous. The problem is, that it most likely won't work for Google and Facebook, because they actively blacklist such numbers for verification. Or you could try to find someone else receiving the SMS for you, but that would only mitigate the risk from you to the other person.

<font size="-3">
,,
^1^ [IMSI](https://en.wikipedia.org/wiki/International_mobile_subscriber_identity)
^2^ [IMEI](https://en.wikipedia.org/wiki/International_Mobile_Station_Equipment_Identity)
</font>

## Why this page? ##
You can skip "*Why this page?*".

<font size="-3">This page highly risks to state obvious things. Obvious to whom? Developers, hackers, geeks, etc. may call that common sense.

Those groups tend to lose contact to actual non-techy users. It's good sometimes to read usability papers or feedback from people who do not post on mailing lists or in forums.

For example:</font>

* <font size="-3">[tor-dev First-time tails/tor user feedback](https://lists.torproject.org/pipermail/tor-dev/2012-April/003472.html))</font>
* <font size="-3">[Eliminating Stop-Points in the Installation and Use of. Anonymity Systems](http://petsymposium.org/2012/papers/hotpets12-1-usability.pdf)</font>
* <font size="-3">Quote, [North Korea: On the net in world's most secretive nation](http://www.bbc.co.uk/news/technology-20445632) ([w](http://www.webcitation.org/6Fg09O7AR)): "*"In order to make sure the mobile phone frequencies are not being tracked, I would fill up a washbasin with water and put the lid of a rice cooker over my head while I made a phone call," said one interviewee, a 28-year-old man who left the country in November 2010.*"

## Attribution ##
Thanks to intrigeri and anonym, who provided feedback and suggestions for this page on the Tails-dev mailing list.

# Footer #
[[include ref=WikiFooter]]