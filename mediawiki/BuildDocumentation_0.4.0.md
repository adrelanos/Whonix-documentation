[[include ref=WikiHeader]]

[TOC]

<pre># Copyright:
# adrelanos (aka proper)
# adrelanos (at) riseup (dot) net
#
# License:
# GPL v3 or any later
#
# Any changes you pull into this source will be also licensed
# under GPL v3 or any later. Additionally you grant adrelanos the right to
# re-license your work under a different license. If that is not acceptable,
# you can either fork this source under GPL v3 or any later or contact
# adrelanos. Contact adrelanos, if you require this source code under
# different license.
#
# Authors:
# adrelanos (aka proper)
# Big contributions from anonymous.
# Leaktest and other stuff contributed by smarm.</pre>
This page documents how the binary distribution images are built. If you have any questions or need help let us know on [Dev].

Following these instructions will build version Whonix 0.4.5.1 based on Tor 0.2.3 and Debian Wheezy.

Knowledge assumed: Virtualization and networking basic principles; operation of your platform; Linux knowledge: how to install Debian and basic command line knowledge.

Only one prerequisites: you need a working internet connection.

For discussion related to the development and build process of Whonix images go [Dev].

= Build Anonymity =

While downloading the required tools for building Whonix your internet service provider could if he want notice that you want to build Whonix. This is especially interesting, if you want to redistribute Whonix, but still want to stay anonymous. The full story can be read in the chapter [https://sourceforge.net/p/whonix/wiki/Security/#build-anonymity Build Anonymity].

= Build Security =

* Build on a dedicated build system, install security updates...
* All install media and all downloaded/used code must be verified (including all software on the host).
* Hashes, fingerprints in the scripts and the wiki is not to be trusted. Verify everything.
* Read [Trust]

= Host preparation =

== Building on Linux ==

We recommend you use a dedicated OS installation just for hosting the Whonix VMs. (See [Security])

You need to use Debian. The build scripts could be adapted to run on other *NIX systems as well but currently they assume apt-get to be available. You need about 15 GB of free space.

Install the latest security updates, install Virtual Box (and qemu-kvm which is required to mount the Virtual Box .vdi images). Reboot to apply kernel updates.

<pre>sudo apt-get update &amp;&amp; sudo apt-get dist-upgrade
sudo apt-get install virtualbox qemu genisoimage apt-cacher-ng grml-debootstrap parted kpartx debootstrap mksh dialog git
sudo reboot</pre>
== Building on Windows ==

Building on Windows is no longer supported. Redistributed Whonix builds should be build on Linux. If you want to port the Whonix build scripts to Windows, please contact us. Running Whonix on a Windows host with Virtual Box installed should is still possible.

== Using an apt cache to speed up downloading ==

If you want to build multiple times (for debugging etc.), it makes sense to install a local apt proxy on your build machine.<sup>1</sup> That safes download time and traffic.<sup>2</sup> If you build Whonix on Whonix, apt-cacher-ng will go through Tor's TransPort.

<font size="-3"> ,, <sup>1</sup> Thanks to [https://linuxexpresso.wordpress.com/2011/02/13/howto-apt-cacher-ng-on-ubuntu/ source]. <sup>2</sup> It would be possible to download without an apt-cacher. But why? If you want so ignore this chapter and change the mirror settings in grml configuration file. </font>

Open /etc/apt/apt.conf.

<pre>sudo nano /etc/apt/apt.conf</pre>
Add the following.

<pre># /etc/apt/apt.conf
Acquire::http { Proxy &quot;http://127.0.0.1:3142&quot;; };</pre>
Restart apt-cacher-ng. Should not be required, but it was for me.

<pre>sudo service apt-cacher-ng restart</pre>
Safe and test if it's working.

<pre>sudo /usr/bin/apt-get update</pre>
= Source Code Intro =

This chapter is dedicated to give an introduction into the Whonix source code. '''If you prefer to read and understand the source code just by reading scripts you may skip this optional chapter.'''

Moved to [Dev_SourceCodeIntro].

= Build as user &quot;user&quot; =

You need a user account named &quot;''user''&quot;. If you don't already have it, create it.

<pre>sudo adduser user</pre>
During the build process &quot;''user''&quot; also needs root.

<pre>sudo addgroup user sudo</pre>
Log in as &quot;''user''&quot;.

<font size="-3"> This is because the source code is far from perfect. The username &quot;user&quot; and /home/user/Whonix is hardcoded and expected as source folder. Bug: [https://trac.torproject.org/projects/tor/wiki/doc/TorBOX/Dev#SOURCECODEnolongerhardcodeuserfolder no longer hardcode user folder] </font>

= Get the Whonix source code =

<pre>git clone https://github.com/adrelanos/Whonix</pre>
= Verify the Whonix source code with gpg =

This is recommend but not required. See [Trust].

# [https://sourceforge.net/p/whonix/wiki/TrustingWhonixSigningKey/ Learn about Whonix signing key.].

(1.1) Get into the correct [https://sourceforge.net/p/whonix/wiki/Dev_git/ git branch].

<pre>##Not required. Still using the master branch.
##Next Whonix version will reflect the new branching model.
#git checkout stable</pre>
<ol start="2" style="list-style-type: decimal;">
<li><p>Get a list of available git tags.</p>
<p>git tag</p></li>
<li><p>Verify the tag you want to build.</p>
= Replace with tag you want to build. =

<p>git tag -v 0.4.5.1</p></li>
<li><p>Output should look like the following.</p>
<p>object 13870efc29018065267788f9f23026e6ff489684 type commit tag 0.4.5.1 tagger adrelanos [mailto:invalid@invalid invalid@invalid] 1348681401 -0400</p>
<p>0.4.5.1 gpg: Signature made Wed Sep 26 17:43:26 2012 UTC using RSA key ID 713AAEEF gpg: Good signature from &quot;adrelanos <email @ removed>&quot;</p></li></ol>

The warning.

<pre>gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.</pre>
Is explained on the [https://sourceforge.net/p/whonix/wiki/TrustingWhonixSigningKey/ Whonix signing key] page and can be ignored.

= Create the Images =

== Preparations ==

<ol style="list-style-type: decimal;">
<li><p>Git checkout, which version you want to build.</p>
<p>git checkout 0.4.5.1</p></li>
<li><p>Make the build script executable:</p>
<p>chmod +x ~/Whonix/whonix_*</p></li>
<li><p>Make sure there aren't any VMs in Virtual Box already called &quot;Whonix-Gateway&quot; or &quot;Whonix-Workstation&quot; (TODO: automate that)</p></li>
<li><p>Check if /home/user/Whonix/usr/share/version for version number.</p></li></ol>

== VM Creation ==

<ol style="list-style-type: decimal;">
<li><p>Open a shell and type:</p>
<p>sudo ~/Whonix/whonix_build -all</p></li>
<li><p>Check if all went ok.</p></li></ol>

The scripts can fail for many reasons, please report back any issues!

= Debugging =

'''OPTIONAL''' (Only in case something goes wrong or you want to audit or develop Whonix.)

* [https://sourceforge.net/p/whonix/wiki/OptionalConfigurations/#ssh-into-whonix-gateway SSH into Whonix-Gateway]
* [https://sourceforge.net/p/whonix/wiki/OptionalConfigurations/#mount-and-inspect-images Mount and inspect images]

= How to use the ova images =

Reboot both VMs. Please read the [Documentation]!

= Final Steps (Only Required For Redistribution) =

See [https://github.com/adrelanos/Whonix/tree/master/release Release Folder] in Whonix source code.

* LeakTests!
* [Test] the images before release! TODO: Needs big revision with all Whonix features.
* See if [Documentation] still makes sense.
* Update the Changelog.
* See https://github.com/adrelanos/Whonix/blob/master/release/whonix_release
* Upload the images.
* At least a few testers should test before posting a news. Testers may be found by posting a news.
* Check, if ManualTBupdate is still up to date.
* Update Download.
* Update Home.
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

