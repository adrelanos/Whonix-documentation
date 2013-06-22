[[include ref=WikiHeader]]

[TOC]

= Change the User Interface Language =

== Introduction ==

Because Whonix is nothing special and based on Debian GNU/Linux and KDE, you are free to change the system language. The technical steps are the same. You could also refer to Debian or KDE upstream documentation. If you are happy with the default English, you do not have to do anything.

== Tor Browser ==

=== Method 1 ===

'''Whonix-Workstation ONLY!'''

<ol style="list-style-type: decimal;">
<li><p>Start Tor Browser.</p></li>
<li><p>Find out which ESR Firefox version Tor Browser is using.</p>
<p>Tor Browser -&gt; Help -&gt; About Tor Browser</p></li></ol>

Should be something like ''10.0.11''.

<ol start="3" style="list-style-type: decimal;">
<li>Install a language pack.</li></ol>

Go to [http://download-origin.cdn.mozilla.net/pub/mozilla.org/firefox/releases/10.0.11esr/linux-i686/xpi/ http://download-origin.cdn.mozilla.net/pub/mozilla.org/firefox/releases/'''10.0.11'''esr/linux-i686/xpi/]. You may need to change the '''bold''' part of that link depending on which ESR Firefox version Tor Browser is using!

<ol start="4" style="list-style-type: decimal;">
<li><p>Restart Tor Browser.</p></li>
<li><p>Done.</p></li></ol>

=== Method 2 ===

'''Whonix-Workstation ONLY!'''

'''Please TEST and leave feedback.'''

<ol style="list-style-type: decimal;">
<li><p>Update the package lists.</p>
<p>sudo apt-get update</p></li>
<li><p>Search for available language packs.</p>
<p>apt-cache search iceweasel-l10n-</p></li>
<li><p>Install a language pack.</p>
== Example, replace the -ar with your language! ==

<p>sudo apt-get install iceweasel-l10n-ar</p></li>
<li><p>Change setting in Tor Browser.</p>
<p>sudo find /usr/lib/iceweasel/extensions -maxdepth 1 -name 'langpack*.xpi' -exec ln -s '{}' /home/user/tor-browser_en-US/Data/profile/extensions/ ';'</p></li></ol>

== System ==

=== All Languages ===

'''Whonix-Workstation ONLY!'''

<ol style="list-style-type: decimal;">
<li><p>Open konsole</p>
<p>Start menu -&gt; Applications -&gt; System -&gt; Terminal.</p></li>
<li><p>Update the package lists.</p>
<p>sudo apt-get update</p></li>
<li><p>Search for available language packs.</p>
<p>apt-cache search kde-i18n</p></li></ol>

Or [http://packages.debian.org/search?keywords=kde-l10n&searchon=names&suite=stable&section=all search the Debian package archive].

<ol start="4" style="list-style-type: decimal;">
<li><p>Install a language pack.</p>
== Example, replace the -ar with your language! ==

<p>sudo apt-get install kde-l10n-ar</p></li>
<li><p>Change setting in KDE.</p>
<p>Start menu -&gt; Applications -&gt; System -&gt; System Settings -&gt; Locale -&gt; Languages -&gt; Change Language</p></li></ol>

=== Korean ===

User contributed instructions originally posted in [https://sourceforge.net/p/whonix/discussion/general/thread/fff34595/ Whonix Forum - Korean language support] by Anonymous. You can also use that thread for support questions.

<ol style="list-style-type: decimal;">
<li><p>Open konsole</p>
<p>Start menu -&gt; Applications -&gt; System -&gt; Terminal.</p></li>
<li><p>Update the package list.</p>
<p>sudo apt-get update</p></li>
<li><p>View available language packs.</p>
<p>apt-cache search kde-i18n</p></li>
<li><p>Install Korean language pack.</p>
<p>sudo apt-get install kde-l10n-ko</p></li>
<li><p>Install Korean fonts.</p>
<p>sudo apt-get install ttf-unfonts-core ttf-unfont-extra</p></li>
<li><p>Open system settings and set eungulim as kde's font.</p></li>
<li><p>Open konsole and</p>
<p>sudo dpkg-reconfigure locales</p></li>
<li><p>Set &quot;''ko KR.UTF-8 UTF-8''&quot; as Default locale.</p></li>
<li><p>Install nabi.</p>
<p>apt-get install nabi</p></li>
<li><p>Restart your Whonix-Workstation and start nabi.</p></li>
<li><p>Done. You can write and read Korean now.</p></li></ol>

= Footer =

[[include ref=WikiFooter]]

