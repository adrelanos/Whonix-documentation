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

# First time user? #
**The default user is:** ***user***

**The default password is:** ***changeme***

* If you don't know what a metadata or a man-in-the-middle attack is.
* If you think no-one can eavesdrop on your communications because you are using Tor.
* If you have no notion on how Whonix works.

Then, check first the [About] and [Warning] pages to make sure that Whonix is the right tool for you and that you understand well its limitations.

# Download Whonix virtual machine images #
**The default user is:** ***user***

**The default password is:** ***changeme***

[Download Whonix 0.5.6 from sourceforge.net](https://sourceforge.net/projects/whonix/files/whonix-0.5.6/)

# Verify the Whonix virtual machine images #
It is important to check the integrity of the virtual machine images you downloaded to make sure no man in the middle attack or file corruption happened. (See [DownloadSecurity].)

Whonix virtual machine images are cryptographically signed using OpenPGP by Whonix developer adrelanos. OpenPGP is a standard for data encryption that provides cryptographic privacy and authentication through the use of keys owned by its users.

If you already know how to use an OpenPGP key you can download the Whonix signing key and the Whonix signatures straight away.

Otherwise, read our instructions to check the virtual machine images integrity:

* [Using Linux: Ubuntu, Debian, Whonix, etc. using kgpg](https://sourceforge.net/p/whonix/wiki/Verify_the_virtual_machine_images_using_Linux/)
* [Using Linux with the command line](https://sourceforge.net/p/whonix/wiki/Verify_the_virtual_machine_images_using_the_command_line/)
* [Using other operating systems](https://sourceforge.net/p/whonix/wiki/Verify_the_virtual_machine_images_using_other_operating_systems/)

# Whonix signing key #
You can learn about the signing key on the [Trusting Whonix Signing Key](https://sourceforge.net/p/whonix/wiki/TrustingWhonixSigningKey/) page.

# Whonix signature #
[Whonix 0.5.6 signatures](https://sourceforge.net/projects/whonix/files/whonix-0.5.6-sig/)

# Install Whonix #
## 1. Pre Install Advice ##
Read and apply: [Security Advice before installing Whonix](https://sourceforge.net/p/whonix/wiki/Pre%20Install%20Advice/).

## 2. Install ##
Just [download Whonix](https://sourceforge.net/p/whonix/wiki/Download/edit#download-whonix-virtual-machine-images) and import <u>both</u> <font size="-3">^1^</font> Whonix <u>.ova images</u> into **Virtual Box**. Do not change any settings! (You could do that later.) Do not change MAC address!

The .ova images should be imported into Virtual Box. <font size="-3">There is also highly experimental support for [VMware], but only Virtual Box is fully supported, rather use Virtual Box.</font>

<font size="-3">^1^ You need both, Whonix-Gateway.ova and Whonix-Workstation.ova. Its a two machine setup, one .ova alone isn't useful.</font>

### If you need more help with Installing ###
There is a tutorial with screenshots, see [Install].

There are also [Video Tutorials](http://whonix.sourceforge.net/videos.html).

<font size="-3">([Video Help](http://whonix.sourceforge.net/videos.html#video-help))</font>

If you still need help, please go to the [User Help Forum](https://sourceforge.net/p/whonix/discussion/).

## 3. Post Install Advice ##
Read and apply: [Post Install Advice](https://sourceforge.net/p/whonix/wiki/Post%20Install%20Advice/).

# Stay tuned #
## Introduction ##
Reading the latest news is important to stay on top of latest developments. Should security vulnerabilities ever be found in Whonix or should an improved version be released, you should be informed.

## Whonix News Blogs ##
There are two ways to get news. Choose at your preference.

(1) [Important Blog](https://sourceforge.net/p/whonix/blog/) - Most important stuff only. Security vulnerabilities and new versions only. For people with very limited time and interest in Whonix development and news.

(2) [Feature Blog](https://sourceforge.net/p/whonix/featureblog/) - Includes everything from the Important Blog. Has a relaxed posting policy. I will also blog about updated articles, new features, future features, development, call for testing, general project thoughts and so on.

When you start **Tor Browser Recommend** ![r](http://whonix.sourceforge.net/pictures/important.ico) (there is a shortcut on the desktop), it will open both blogs in a privacy friendly way. It's recommend at least to read the Important Blog if you are in a hurry. Have a look into the Feature Blog if you are generally interested to learn about anonymity/privacy/security related things or to see what's going on with Whonix.

## Operating System Updates ##
You should regularly check for operating system updates on your host operating system, in Whonix-Workstation and on Whonix-Gateway as highly recommend in the [Security Guide].

## Tor Browser ##
There is no auto-update feature for Tor Browser. You will be notified about new Tor Browser versions by whonixcheck. Tor Browser's built in stock update check mechanism also works in Whonix. For simple instructions how to update the browser, see [TorBrowser]. Additionally it might be also wise to subscribe to https://blog.torproject.org for news.

## Whonix Version ##
Furthermore you will be automatically notified about new Whonix versions by whonixcheck.

## Debian Announcements ##
Since Whonix is based on Debian, it takes advantages of the all of the work done by the Debian security team. As quoted from (http://security.debian.org/):

    Debian takes security very seriously. We handle all security problems brought to our
    attention and ensure that they are corrected within a reasonable timeframe. Many
    advisories are coordinated with other free software vendors and are published the same
    day a vulnerability is made public and we also have a Security Audit team that reviews
    the archive looking for new or unfixed security bugs. 

    Experience has shown that "security through obscurity" does not work. Public disclosure
    allows for more rapid and better solutions to security problems. In that vein, this
    page addresses Debian's status with respect to various known security holes, which
    could potentially affect Debian.

Consider also subscribing to the Debian security announcement mailing list.

## Social Media Profiles ##
There are some [Whonix Social Media Profiles](https://sourceforge.net/p/whonix/wiki/OnlineProfiles/), but please don't rely on them for getting Whonix News and please don't use them to contact Whonix developers. (See [Contact] for contact information.)

Because some people will do so even though recommend against, messages from the Whonix Feature Blog will be automatically mirrored to [Whonix Twitter Profile](https://twitter.com/Whonix) and to [Whonix Google+ Profile](https://plus.google.com/108150429836421683225/about).

[Whonix Facebook Profile](https://www.facebook.com/pages/Whonix/369240439779108) won't get any updates, because [Facebook is asking for governmental issued photo ID](https://sourceforge.net/p/whonix/featureblog/2013/01/facebook-asking-for-government-issued-photo-id-ex-passport-drivers-license---whonix-facebook-account-permanently-blocked/).

<font size=-3>[identi.ca's mirroring feature is still down](http://status.net/open-source/issues/3581), therefore no mirroring to [Whonix identi.ca Profile](https://identi.ca/whonix)</font>

If you don't get into trouble, by letting others to know, that you like or use Whonix, feel free to follow or like those profiles (with your anonymous account) as a little way to [Contribute].

## Source Code ##
In case your are interested in Whonix source code changes, see [subscribe to code changes](https://sourceforge.net/p/whonix/wiki/Dev_git/#subscribe-to-code-changes).

# Known bugs #
None at the moment.

# License #
    Whonix Download wiki page Copyright (C) Amnesia <amnesia at boum dot org>
    Whonix Download wiki page Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
    
    This program comes with ABSOLUTELY NO WARRANTY; for details see the wiki source code.
    This is free software, and you are welcome to redistribute it
    under certain conditions; see the wiki source code for details.

# Footer #
[[include ref=WikiFooter]]