[[include ref=WikiHeader]]

[TOC]

<!--
Copyright:

   Whonix Download wiki page Copyright (C) Amnesia <amnesia at boum dot org>
   Whonix Download wiki page Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
   
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
This wiki page is a fork of the Tails Download page, from this exact source <http://git.immerda.ch/?p=amnesia.git;a=blob;f=wiki/src/download.html;hb=19d48ad8b7d23548aae126ed6cb873c91255f876>.
-->

= First time user? =

'''The default user is:''' '''''user'''''

'''The default password is:''' '''''changeme'''''

* If you don't know what a metadata or a man-in-the-middle attack is.
* If you think no-one can eavesdrop on your communications because you are using Tor.
* If you have no notion on how Whonix works.

Then, check first the [About] and [Warning] pages to make sure that Whonix is the right tool for you and that you understand well its limitations.

= Download Whonix virtual machine images =

'''The default user is:''' '''''user'''''

'''The default password is:''' '''''changeme'''''

[https://sourceforge.net/projects/whonix/files/whonix-0.5.6/ Download Whonix 0.5.6 from sourceforge.net]

= Verify the Whonix virtual machine images =

It is important to check the integrity of the virtual machine images you downloaded to make sure no man in the middle attack or file corruption happened. (See [DownloadSecurity].)

Whonix virtual machine images are cryptographically signed using OpenPGP by Whonix developer adrelanos. OpenPGP is a standard for data encryption that provides cryptographic privacy and authentication through the use of keys owned by its users.

If you already know how to use an OpenPGP key you can download the Whonix signing key and the Whonix signatures straight away.

Otherwise, read our instructions to check the virtual machine images integrity:

* [https://sourceforge.net/p/whonix/wiki/Verify_the_virtual_machine_images_using_Linux/ Using Linux: Ubuntu, Debian, Whonix, etc. using kgpg]
* [https://sourceforge.net/p/whonix/wiki/Verify_the_virtual_machine_images_using_the_command_line/ Using Linux with the command line]
* [https://sourceforge.net/p/whonix/wiki/Verify_the_virtual_machine_images_using_other_operating_systems/ Using other operating systems]

= Whonix signing key =

You can learn about the signing key on the [https://sourceforge.net/p/whonix/wiki/TrustingWhonixSigningKey/ Trusting Whonix Signing Key] page.

= Whonix signature =

[https://sourceforge.net/projects/whonix/files/whonix-0.5.6-sig/ Whonix 0.5.6 signatures]

= Install Whonix =

== 1. Pre Install Advice ==

Read and apply: [https://sourceforge.net/p/whonix/wiki/Pre%20Install%20Advice/ Security Advice before installing Whonix].

== 2. Install ==

Just import both Whonix .ova images into Virtual Box. Do not change any settings! (You could do that later.) Do not change MAC address!

The .ova images should be imported into Virtual Box. <font size="-3">There is also highly experimental support for [VMware], but only Virtual Box is fully supported, rather use Virtual Box.</font>

=== If you need more help with Installing ===

There is a tutorial with screenshots, see [Install].

There are also [http://whonix.sourceforge.net/videos.html Video Tutorials].

<font size="-3">([http://whonix.sourceforge.net/videos.html#video-help Video Help])</font>

If you still need help, please go to the [https://sourceforge.net/p/whonix/discussion/ User Help Forum].

== 3. Post Install Advice ==

Read and apply: [https://sourceforge.net/p/whonix/wiki/Post%20Install%20Advice/ Post Install Advice].

= Stay tuned =

== Introduction ==

Reading the latest news is important to stay on top of latest developments. Should security vulnerabilities ever be found in Whonix or should an improved version be released, you should be informed.

== Whonix News Blogs ==

There are two ways to get news. Choose at your preference.

# [https://sourceforge.net/p/whonix/blog/ Important Blog] - Most important stuff only. Security vulnerabilities and new versions only. For people with very limited time and interest in Whonix development and news.
# [https://sourceforge.net/p/whonix/featureblog/ Feature Blog] - Includes everything from the Important Blog. Has a relaxed posting policy. I will also blog about updated articles, new features, future features, development, call for testing, general project thoughts and so on.

When you start '''Tor Browser Recommend''' [[Image:http://whonix.sourceforge.net/pictures/important.ico|r]] (there is a shortcut on the desktop), it will open both blogs in a privacy friendly way. It's recommend at least to read the Important Blog if you are in a hurry. Have a look into the Feature Blog if you are generally interested to learn about anonymity/privacy/security related things or to see what's going on with Whonix.

== Operating System Updates ==

You should regularly check for operating system updates on your host operating system, in Whonix-Workstation and on Whonix-Gateway as highly recommend in the [Security Guide].

== Tor Browser ==

There is no auto-update feature for Tor Browser. You will be notified about new Tor Browser versions by whonixcheck. Tor Browser's built in stock update check mechanism also works in Whonix. For simple instructions how to update the browser, see [TorBrowser]. Additionally it might be also wise to subscribe to https://blog.torproject.org for news.

== Whonix Version ==

Furthermore you will be automatically notified about new Whonix versions by whonixcheck.

== Debian Announcements ==

Since Whonix is based on Debian, it takes advantages of the all of the work done by the Debian security team. As quoted from (http://security.debian.org/):

<pre>Debian takes security very seriously. We handle all security problems brought to our
attention and ensure that they are corrected within a reasonable timeframe. Many
advisories are coordinated with other free software vendors and are published the same
day a vulnerability is made public and we also have a Security Audit team that reviews
the archive looking for new or unfixed security bugs. 

Experience has shown that &quot;security through obscurity&quot; does not work. Public disclosure
allows for more rapid and better solutions to security problems. In that vein, this
page addresses Debian's status with respect to various known security holes, which
could potentially affect Debian.</pre>
Consider also subscribing to the Debian security announcement mailing list.

== Social Media Profiles ==

There are some [https://sourceforge.net/p/whonix/wiki/OnlineProfiles/ Whonix Social Media Profiles], but please don't rely on them for getting Whonix News and please don't use them to contact Whonix developers. (See [Contact] for contact information.)

Because some people will do so even though recommend against, messages from the Whonix Feature Blog will be automatically mirrored to [https://twitter.com/Whonix Whonix Twitter Profile] and to [https://plus.google.com/108150429836421683225/about Whonix Google+ Profile].

[https://www.facebook.com/pages/Whonix/369240439779108 Whonix Facebook Profile] won't get any updates, because [https://sourceforge.net/p/whonix/featureblog/2013/01/facebook-asking-for-government-issued-photo-id-ex-passport-drivers-license---whonix-facebook-account-permanently-blocked/ Facebook is asking for governmental issued photo ID].

<font size=-3>[http://status.net/open-source/issues/3581 identi.ca's mirroring feature is still down], therefore no mirroring to [https://identi.ca/whonix Whonix identi.ca Profile]</font>

If you don't get into trouble, by letting others to know, that you like or use Whonix, feel free to follow or like those profiles (with your anonymous account) as a little way to [Contribute].

== Source Code ==

In case your are interested in Whonix source code changes, see [https://sourceforge.net/p/whonix/wiki/Dev_git/#subscribe-to-code-changes subscribe to code changes].

= Known bugs =

None at the moment.

= License =

<pre>Whonix Download wiki page Copyright (C) Amnesia &lt;amnesia at boum dot org&gt;
Whonix Download wiki page Portions Copyright (C) 2012 adrelanos &lt;adrelanos at riseup dot net&gt;

This program comes with ABSOLUTELY NO WARRANTY; for details see the wiki source code.
This is free software, and you are welcome to redistribute it
under certain conditions; see the wiki source code for details.</pre>
= Footer =

[[include ref=WikiFooter]]

