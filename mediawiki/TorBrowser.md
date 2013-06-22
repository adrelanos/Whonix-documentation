<!--
Copyright:

   Whonix Tor Browser wiki page Copyright (C) Amnesia <amnesia at boum dot org>
   Whonix Tor Browser wiki page Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
   
   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 3 of the License, or
   (at your option) any later version.
         
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
      
   You should have received a copy of the GNU General Public License
   along with this program; if not, write to:

    Free Software Foundation, Inc. 
    51 Franklin St, Fifth Floor
    Boston, MA 02110-1301, USA.

On Debian GNU/Linux systems, the complete text of the GNU General Public
License can be found in the /usr/share/common-licenses' directory.

The complete text of the GNU General Public License can also be found online on gnu.org <https://www.gnu.org/licenses/gpl.html>, in Whonix virtual machine images in /usr/share/common-licenses/GPL-3 file or in Whonix wiki on <https://sourceforge.net/p/whonix/wiki/GPLv3/>.
-->

<!--
The Whonix Tor Browser wiki page is forked from the Tails Browsing the web with Iceweasel page, from this exact source <http://git.immerda.ch/?p=amnesia.git;a=blob;f=wiki/src/doc/anonymous_internet/iceweasel.mdwn;hb=c65e9614d6df9784072ac1e506e2fc83b062f2b0>.
-->

[[include ref=WikiHeader]]

[TOC]

= Introduction =

Tor Browser is a fork of the [http://www.mozilla.com/firefox/ Mozilla Firefox] web browser, optimized for anonymity, developed by The Tor Project. Given its popularity many of you have probably used it before and its user interface is like any other modern web browser.

Here are a few things worth mentioning in the context of Whonix.

= HTTPS Encryption =

Using HTTPS instead of HTTP encrypts your communication while browsing the web.

All the data exchanged between your browser and the server you are visiting are encrypted. It prevents the [https://sourceforge.net/p/whonix/wiki/Warning/#tor-exit-nodes-can-eavesdrop-on-communications Tor exit node to eavesdrop on your communication].

HTTPS also includes mechanisms to authenticate the server you are communicating with. But those mechanisms can be flawed, [https://sourceforge.net/p/whonix/wiki/Warning/#man-in-the-middle-attacks as explained on our warning page].

For example, here is how the browser looks like when we try to log in an email account at [http://lavabit.com/ lavabit.com], using their [https://lavabit.com/apps/webmail/src/login.php webmail interface]:

[[Image:http://whonix.sourceforge.net/pictures/lavabit.png|frame|none|alt=|caption Whonix browser]]

Notice the small area on the left of the address bar saying &quot;lavabit.com&quot; on a blue background and the address beginning with &quot;https://&quot; (instead of &quot;http://&quot;):

[[Image:http://whonix.sourceforge.net/pictures/address-bar.png|frame|none|alt=|caption address bar showing lavabit.com]]

These are the indicators that an encrypted connection using [https://en.wikipedia.org/wiki/HTTP_Secure HTTPS] is being used.

You should try to only use services providing HTTPS when you are sending or retrieving sensitive information (like passwords), otherwise its very easy for an eavesdropper to steal whatever information you are sending or to modify the content of a page on its way to your browser.

= HTTPS Everywhere =

[[Image:http://whonix.sourceforge.net/pictures/https-everywhere.jpg|frame|none|alt=|caption HTTPS Everywhere logo]]

[https://www.eff.org/https-everywhere HTTPS Everywhere] is a Firefox extension shipped in Whonix and produced as a collaboration between [https://torproject.org/ The Tor Project] and the [https://eff.org/ Electronic Frontier Foundation]. It encrypts your communications with a number of major websites. Many sites on the web offer some limited support for encryption over HTTPS, but make it difficult to use. For instance, they may default to unencrypted HTTP, or fill encrypted pages with links that go back to the unencrypted site. The HTTPS Everywhere extension fixes these problems by rewriting all requests to these sites to HTTPS.

To learn more about HTTPS Everywhere you can see:

* the [https://www.eff.org/https-everywhere HTTPS Everywhere homepage]
* the [https://www.eff.org/https-everywhere/faq/ HTTPS Everywhere FAQ]

= Torbutton =

Tor alone is not enough to protect your anonymity and privacy while browsing the web. All modern web browsers, such as Firefox, support [https://en.wikipedia.org/wiki/JavaScript JavaScript], [https://en.wikipedia.org/wiki/Adobe_Flash Adobe Flash], [https://en.wikipedia.org/wiki/HTTP_cookie cookies] and other features which have been shown to be able to defeat the anonymity <sup>1</sup> provided by the Tor network.

In Tor Browser all such features are handled from inside the browser, because it's a modified version of Firefox <sup>2</sup> and contains an extension called [https://www.torproject.org/torbutton/ Torbutton]. These do all sorts of things to prevent the above type of attacks. But that comes at a price: since this will disable some functionalities and some sites might not work as intended. Don't worry too much about this, the vast majority of websites works very well.

To learn more about Torbutton you can see:

* [https://www.torproject.org/torbutton/ the Torbutton homepage]
* [https://www.torproject.org/torbutton/torbutton-faq.html.en the Torbutton FAQ]

To learn more about Data Collection Techniques, Fingerprinting you can see:

* [https://sourceforge.net/p/whonix/wiki/DataCollectionTechniques/ Data Collection Techniques]

<font size="-3"> <sup>1</sup> [https://sourceforge.net/p/whonix/wiki/DoNot/#do-not-confuse-anonymity-with-pseudonymity Reducing anonymity to pseudonymity.]. <sup>2</sup> [https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO/WebBrowsers Patches]. </font>

= Protection against dangerous JavaScript =

Having all JavaScript disabled by default would disable a lot of harmless and possibly useful JavaScript and render unusable many websites. This would scare away lots of potential users &quot;because it just don't work&quot;. Torbutton disables all potentially dangerous JavaScript. On the other hand, having a big user base is important for good anonymity as this very interesting [http://www.mail-archive.com/liberationtech@lists.stanford.edu/msg00022.html mail by Roger Dingledine] explains.

That's why '''JavaScript is enabled by default''' in Tor Browser. We consider this as a necessary compromise between security and usability and as of today we are not aware of any JavaScript that would compromise Whonix anonymity.

For more technical details you can refer to the [https://www.torproject.org/torbutton/en/design/ Torbutton design document]. Another related discussion justifying why JavaScript is enabled by default in Tor Browser was [https://lists.torproject.org/pipermail/tor-talk/2012-May/024227.html tor-talk Tor Browser disabling Javascript anonymity set reduction].

= NoScript =

[[Image:http://whonix.sourceforge.net/pictures/noscript.png|frame|none|alt=|caption NoScript logo]]

NoScript also comes with Tor Browser and provides many protections, even thought JavaScript is enabled by default. You shouldn't mess with NoScript settings in Tor Browser unless you exactly know what you are doing.

For more information you can refer to the NoScript [http://noscript.net/ website] and [http://noscript.net/features features].

= Tor Browser in Whonix differences =

== Introduction ==

The regular Tor Browser Bundle and Tor Browser in Whonix slightly differ. Tor Browser has been slightly modified by Whonix to work behind the Whonix-Gateway. The network and browser fingerprint however, is the same.

Tor Browsers internal update check mechanism is untouched and works fine. Default homepage is untouched and still https://check.torproject.org.

== New Identity Button ==

Note, that if you are using the Tor Browser, which comes with Whonix, that the New Identity button of Tor Button is defunct (greyed out). This is because Tor Button can not access Tor's control port. Due to Whonix Technical [Design], Tor Browser and Tor are isolated from each other, which means there is no way to fix this without loosing the added security by Whonix.

When using the regular Tor Browser Bundle (not Whonix!), the New Identity button unlinks your old identity, changes your circuit (exit node IP) and creates a fresh identity.

As a workaround close Tor Browser, change your circuit with [https://sourceforge.net/p/whonix/wiki/TorController/ Arm] and start Tor Browser again.

This isn't a big issue, since the New Identity button isn't perfect yet anyway, there are open bugs. (See [https://trac.torproject.org/projects/tor/query?status=accepted&status=assigned&status=needs_information&status=needs_review&status=new&status=reopened&order=priority&col=id&col=summary&col=keywords&col=status&col=owner&col=type&col=priority&keywords=tbb-linkability tbb-linkability] and [https://trac.torproject.org/projects/tor/query?status=accepted&status=assigned&status=needs_review&status=needs_revision&status=new&status=reopened&order=priority&col=id&col=summary&col=keywords&col=status&col=owner&col=type&col=priority&keywords=tbb-fingerprinting tbb-fingerprinting].)

== Whonix Proxy Settings / user.js ==

When running ''torbrowser -update'', the update script creates a ''user.js'' file, for example ''~/tor-browser_en-US/Data/profile/user.js''. User.js is used to override some Tor Button defaults, namely the SocksProxy settings and other minor misc settings. <sup>1</sup> See also the [https://sourceforge.net/p/whonix/wiki/Stream%20Isolation/#tor-browser Tor Browser sub chapter] on the [Stream Isolation] page.

<font size="-3"> <sup>1</sup> If you are curious which these are in details, or for reviewers or auditors, see [https://github.com/adrelanos/Whonix/blob/stable/whonix_workstation/usr/local/bin/torbrowser torbrowser script and user.js on github]. </font>

== More than one Tor Browser in Whonix ==

For better isolation of different identities. For advanced users. Moved to the [https://sourceforge.net/p/whonix/wiki/Advanced%20Security%20Guide/#more-than-one-tor-browser-in-whonix Advanced Security Guide].

= Update Tor Browser =

== Introduction ==

There is no auto-update feature for Tor Browser. You will be notified about new Tor Browser versions by whonixcheck. Tor Browser's built in stock update notification mechanism also works in Whonix. Additionally it might be also wise to subscribe to https://blog.torproject.org for news.

== Updating ==

Tor Browser version check and update (after confirmation) in Whonix can be done with:

<pre>torbrowser -update</pre>
A future update of Tor Button might break Tor Browser running in Whonix-Workstation, since the update resets the network settings. If that happens, update Tor Browser.

In case Tor Browser inside Whonix-Workstation breaks, a news with instructions on how to fix the issue will be posted within a few days. If not, the Whonix developer is not aware of the issue.

If the Tor Browser update script is ever broken, you are advised to update manually, see [https://sourceforge.net/p/whonix/wiki/ManualTBupdate/ Manually Update Tor Browser].

= Browser Plugins / Flash / Java =

See [BrowserPlugins].

= Remove Proxy Settings =

== General ==

'''This is an advanced topic. You most likely only need it for advanced tunneling scenarios.'''

== Whonix 0.5.5 ==

It's best to get a fresh copy of Tor Browser, which has never been started before. This is due to an upstream bug <sup>2</sup> preventing from changing proxy settings to &quot;no proxy&quot;.

Whonix modifies user.js as documented in the [https://sourceforge.net/p/whonix/wiki/TorBrowser/#whonix-proxy-settings-userjs Tor Browser chapter].

Open ''/home/user/tor-browser_en-US_my/Data/profile/user.js''.

<pre>leafpad /home/user/tor-browser_en-US_my/Data/profile/user.js</pre>
Comment out all network settings.

<pre>## network settings
#user_pref(&quot;extensions.torbutton.use_privoxy&quot;, false);
#user_pref(&quot;extensions.torbutton.settings_method&quot;, &quot;custom&quot;);
#user_pref(&quot;extensions.torbutton.socks_host&quot;, &quot;192.168.0.10&quot;);
#user_pref(&quot;extensions.torbutton.socks_port&quot;, 9100);
#user_pref(&quot;network.proxy.socks&quot;, &quot;192.168.0.10&quot;);
#user_pref(&quot;network.proxy.socks_port&quot;, 9100);
#user_pref(&quot;extensions.torbutton.custom.socks_host&quot;, &quot;192.168.0.10&quot;);
#user_pref(&quot;extensions.torbutton.custom.socks_port&quot;, 9100);</pre>
Now you can use Tor Button's settings dialog to set it to any other proxy.

Alternatively, if you want to set it to no proxy, you could open ''start-tor-browser'' in the root of the Tor Browser folder and add right below ''#!/bin/sh''. <sup>1</sup> <sup>2</sup> <sup>3</sup> <sup>4</sup>

<pre>export TOR_TRANSPROXY=1</pre>
If you are having problems, it's most likely a problem with Tor Browser / Tor Button's proxy settings. In Tor Browser open the pseudo url &quot;''about:config''&quot; and search for &quot;''network.proxy''&quot; and check if these settings are sane.

== Later version of Whonix ==

Will probable be different... See [Next]...

== Footnotes ==

<font size="-3">,, <sup>1</sup> These steps are required to remove proxy settings. After they have been removed, you can point a socksifier to ''start-tor-browser'' and it should work as usual. <sup>2</sup> This is required because of an upstream bug in Tor Button, [https://trac.torproject.org/projects/tor/ticket/6566 broken &quot;Transparent Torification (Requires custom transproxy or Tor router)&quot;]. <sup>3</sup> TOR_SOCKS_HOST and TOR_SOCKS_PORT were set for [Stream Isolation]. TOR_TRANSPROXY tells Tor Button to use &quot;no proxy&quot;. (It will of course still be forced through Tor. Not through Tor's SocksPort anymore, but through Tor's TransPort.) <sup>4</sup> And because Whonix sets by default TOR_SOCKS_HOST and TOR_SOCKS_PORT using ''/etc/environment''. </font>

= Browser Language =

If you want the browser interface in a different language than English, see [Language].

= License =

<pre>Whonix Tor Browser wiki page Copyright (C) Amnesia &lt;amnesia at boum dot org&gt;
Whonix Tor Browser wiki page Portions Copyright (C) 2012 adrelanos &lt;adrelanos at riseup dot net&gt;

This program comes with ABSOLUTELY NO WARRANTY; for details see the wiki source code.
This is free software, and you are welcome to redistribute it
under certain conditions; see the wiki source code for details.</pre>
= Footer =

[[include ref=WikiFooter]]

