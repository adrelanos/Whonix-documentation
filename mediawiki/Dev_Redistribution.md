[[include ref=WikiHeader]]

[TOC]

= Redistribution =

See [https://github.com/adrelanos/Whonix/tree/development/release Release Folder] in Whonix source code.

Clean source code

* get ride of .directory files inside the source code: dolphin -&gt; preferences -&gt; general -&gt; behavior -&gt; use common view properties for all folders
* get ride of ~backup files: find ./ -name '*~' | xargs trash-put

Other important stuff

* Don't forget to update Whonix version number.
* write proper debian/changelog with debchange
* git add --force debian/changelog
* [LeakTests]!
* [Test] the images before release! TODO: Needs big revision with all Whonix features.
* See if [Documentation] still makes sense.
* Update the [Changelog].
* See https://github.com/adrelanos/Whonix/blob/development/release/whonix_release
* Source Code

Whonix-Gateway

<pre>sudo ./debug-steps/download-source -tg</pre>
Whonix-Workstation

<pre>sudo ./debug-steps/download-source -tw</pre>
Compress. Upload.

* Upload the images.
* At least a few testers should test before posting a news. Testers may be found by posting a news.
* Check, if [ManualTBupdate] is still up to date.
* Update [Download].
* Only next version: Update gpg verification instructions. (Change from .sig to .asc.)
* Only next version: chmod -x / +x no longer required for [BrowserPlugins] and [Dev_Flashtutorial].
* Only next version: [whonixcheck]
* Only next version: [XChat]
* Only next version: chmod -x / +x update [Tunnel_Proxy_or_SSH_or_VPN_through_Tor]
* Only next version: point sf important blog to https://anonymousoperatingsystem.wordpress.com/category/important/feed/ and sf feature blog to https://anonymousoperatingsystem.wordpress.com/feed/ (set up as internal feed in https://sourceforge.net/p/whonix/admin/tools)
* Update [Stream Isolation] chmod -x / +x no longer recommend, use /etc/whonix.d instead
* Update [PhysicalIsolation].
* Update [BuildDocumentation].
* Update [Features].
* Update [http://sourceforge.net/projects/whonix/ sf.net project page].
* Update sf.net default download.
* New documentation from [Next].
* Finally announce: Post a news.
** In Whonix Important and Feature Blog.
** http://lists.debian.org/debian-derivatives/
*** debian-derivatives@lists.debian.org
** https://lists.torproject.org/pipermail/tor-talk/
*** tor-talk@lists.torproject.org
** https://lists.sourceforge.net/lists/listinfo/whonix-devel
*** whonix-devel@lists.sourceforge.net
** full-disclosure@lists.grok.org.uk
** https://mailman.stanford.edu/mailman/listinfo/liberationtech
*** liberationtech@lists.stanford.edu

= Footer =

[[include ref=WikiFooter]]

