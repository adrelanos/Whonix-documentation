[[include ref=WikiHeader]]

[TOC]

= Introduction =

'''This page reflects 0.5.6, the released and stable Whonix version! If you want to develop Whonix, rather get the latest, because the source code layout was heavily simplified.'''

This page documents how the binary distribution images are built. If you have any questions or need help let us know on [Dev].

Following these instructions will build version Whonix 0.5.x based on Tor and Debian Wheezy.

Knowledge assumed: Virtualization and networking basic principles; operation of your platform; Linux knowledge: how to install Debian and basic command line knowledge.

Only one prerequisites: you need a working internet connection.

For discussion related to the development and build process of Whonix images go [Dev].

= Warning =

''/dev/mapper/loop0p1'' (and ''/dev/nbd0'') (used for mounting the images) is hard coded inside Whonix build scripts. Beware if you are using such devices. It may conflict with TrueCrypt. (And possibly other tools relying on ''/dev/mapper/loop0p1'' (and ''/dev/nbd0'').)

To avoid damage to your host system, it may be wise to build Whonix inside a Virtual Machine.

= Build Anonymity =

While downloading the required tools for building Whonix your internet service provider could if he want notice that you want to build Whonix. This is especially interesting, if you want to redistribute Whonix, but still want to stay anonymous. The full story can be read in the chapter [https://sourceforge.net/p/whonix/wiki/Build%20Anonymity/ Build Anonymity].

= Build Security =

Especially, but not exclusively, if you want to distribute Whonix images, you should improve the security of your build environment.

* Build on a dedicated build system, install security updates... ([Security Guide])
* All install media and all downloaded/used code must be verified (including all software on the host).
* Hashes, fingerprints in the scripts and the wiki is not to be trusted. Verify everything.
* Read [Trust].

= Host preparation =

== Building on Linux ==

It is recommend to set your terminal (for example Konsole) to unlimited scrollback, so you can watch the full creation log.

You need to use '''Debian'''. (How to obtain Debian safely: [https://sourceforge.net/p/whonix/wiki/Debian/ Debian ISO gpg verification])

The build scripts could be adapted to run on other *NIX systems as well but currently they assume apt-get and grml-debootstrap to be available. You need about 15 GB of free space.

Become root.

<pre>su</pre>
Update package lists and upgrade.

<pre>apt-get update &amp;&amp; sudo apt-get dist-upgrade</pre>
Install build dependencies.

<pre>apt-get install virtualbox qemu apt-cacher-ng grml-debootstrap parted kpartx debootstrap mksh dialog git sudo equivs rsync</pre>
Add user to sudo group.

<pre>addgroup user sudo</pre>
Reboot.

<pre>reboot</pre>
== Building on Windows ==

Building Whonix directly on Windows is no longer supported. Redistributed Whonix builds should be build on Linux. If you want to port the Whonix build scripts to Windows, please [Contact] us. Running Whonix on a Windows host with Virtual Box installed and building Whonix inside a Virtual Machine with a Linux guest on a Windows host is still possible.

== Using an apt cache to speed up downloading ==

If you want to build multiple times (for debugging etc.), it makes sense to install a local apt proxy on your build machine. <sup>1</sup> That safes download time and traffic. <sup>2</sup> If you build Whonix on Whonix, apt-cacher-ng will go through Tor's TransPort.

<font size="-3"> ,, <sup>1</sup> Thanks to [https://linuxexpresso.wordpress.com/2011/02/13/howto-apt-cacher-ng-on-ubuntu/ source]. <sup>2</sup> It would be possible to download without an apt-cacher. But why? If you want to ignore it, ignore this chapter and change the mirror settings in grml configuration file. </font>

If you build inside Whonix-Workstation, disable the apt-get uwt wrapper.

<pre>sudo chmod -x /usr/local/bin/apt-get</pre>
Open ''/etc/apt/apt.conf''.

<pre>sudo nano /etc/apt/apt.conf</pre>
Add the following.

<pre>## /etc/apt/apt.conf
Acquire::http { Proxy &quot;http://127.0.0.1:3142&quot;; };</pre>
Restart apt-cacher-ng. Should not be required, but it was for me.

<pre>sudo service apt-cacher-ng restart</pre>
Safe and test if it's working.

<pre>sudo apt-get update</pre>
Should there ever be a problem with apt-cacher-ng (package verification failure) (rare cases), use this.

<pre>#sudo apt-get update
#sudo apt-get autoremove
#sudo apt-get dist-upgrade
#sudo apt-get clean
#sudo apt-get autoclean</pre>
= Source Code Intro =

== Introduction ==

This chapter is dedicated to give an introduction into the Whonix source code. '''If you prefer to read and understand the source code just by reading scripts you may skip this optional chapter.''' When you like to mess with the source code, it would probable help a lot if you at least knew what '''.img''', '''.vdi''', '''.vmdk''' and '''.ova''' are being used for.

Moved to [Dev_SourceCodeIntro_0.5.0].

= Build as user &quot;user&quot; =

Log in as &quot;''user''&quot;.

<font size="-3"> This is because the build script is far from perfect. The username &quot;''user''&quot; and ''/home/user/Whonix'' is hardcoded and expected as source folder. Bug: [https://trac.torproject.org/projects/tor/wiki/doc/TorBOX/Dev#SOURCECODEnolongerhardcodeuserfolder no longer hardcode user folder] </font>

== gpg keys ==

gpg keys for required for build Whonix are stored inside ''/home/user/Whonix/whonix_shared/usr/local/share/whonix/''. These include.

* adrelanos.asc - Whonix maintainer key - used for [whonixcheck] news verification
* erinn.asc - [https://www.torproject.org/docs/signing-keys.html.en obtained from torproject.org] - Used to verify downloads of Tor Browser by ''whonix_workstation/usr/local/bin/torbrowser''.
* sebastian.asc - same as erinn.asc.

To find out what the keys are good for, simply grep the source code.

<pre>cd /home/user/Whonix
grep -r adrelanos.asc *
grep -r erinn.asc *
grep -r sebastian.asc *</pre>
If you are in luck, you never have to update the keys yourself and the Whonix maintainer will keep it updated. Otherwise and also as a good precaution you can verify these keys manually. Follow the instructions form torproject.org to obtain the key. Then simply check if the keys match or update the old key with the new one.

== Rebuilding Debian packages ==

Should not be necessary. The package is already ready.

Currently only the [DummyTor] package. Documenting for the sake of completeness.

<pre>cd /home/user/Whonix/whonix_workstation/usr/local/share/whonix/dummytor/
rm tor_1.0_all.deb
./dummytor
cd /home/user/Whonix/</pre>
= Get the Whonix source code =

<pre>git clone https://github.com/adrelanos/Whonix</pre>
= Verify the Whonix source code with gpg =

This is recommend but not required. See [Trust].

<ol style="list-style-type: decimal;">
<li><p>[https://sourceforge.net/p/whonix/wiki/TrustingWhonixSigningKey/ Learn about Whonix signing key.].</p></li>
<li><p>Get a list of available git tags.</p>
<p>git tag</p></li>
<li><p>Verify the tag you want to build.</p>
== Replace with tag you want to build. ==

<p>git tag -v 0.5.6</p></li>
<li><p>Output should look like the following.</p>
<p>object 13870efc29018065267788f9f23026e6ff489684 type commit tag 0.5.6 tagger adrelanos <adrelanos at riseup dot net> 1348681401 -0400</p>
<p>0.5.6 gpg: Signature made Wed Sep 26 17:43:26 2012 UTC using RSA key ID 713AAEEF gpg: Good signature from &quot;adrelanos &lt;adrelanos at riseup dot net&quot;</p></li></ol>

The warning.

<pre>gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.</pre>
(1.1) Get into the correct [https://sourceforge.net/p/whonix/wiki/Dev_git/ git branch].

<pre>## 0.5.6
git checkout 0.5.6

## For stable hotfixes.
#git checkout stable

## In case you want to use the development branch.
#git checkout devel

## In case you want to use the bleeding edge and help with development.
#git checkout untested_adre</pre>
Is explained on the [https://sourceforge.net/p/whonix/wiki/TrustingWhonixSigningKey/ Whonix signing key] page and can be ignored.

= Create the Images =

== Preparations ==

<ol style="list-style-type: decimal;">
<li><p>Git checkout, which version you want to build.</p>
<p>git checkout 0.5.6</p></li>
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

* [https://sourceforge.net/p/whonix/wiki/File%20Transfer/#ssh-into-whonix-gateway SSH into Whonix-Gateway]
* [https://sourceforge.net/p/whonix/wiki/File%20Transfer/#mount-and-inspect-images Mount and inspect images]
* Rebuild the .ova images, while skipping the -tX-createimg step.

The &quot;''sudo ./whonix_createvm -tX-createimg''&quot; step takes far most of the build creation time. As long as no packages have been added or removed, you can repeat all other steps from a backup, which has been automatically created for you, by using.

<pre>sudo ./whonix_build -fast</pre>
* Interactively chroot Whonix-Gateway.

Open a bash shell inside the Whonix-Gateway '''.img''' image.

<pre>sudo ./whonix_createvm -tg-interactive</pre>
* Interactively chroot Whonix-Workstation.

Open a bash shell inside the Whonix-Workstation '''.img''' image.

<pre>sudo ./whonix_createvm -tw-interactive</pre>
= How to use the ova images =

Reboot both VMs. Please read the [Documentation]!

= Final Steps (Only Required For Redistribution) =

== apt.conf ==

What is ''/usr/local/share/whonix/apt.conf'' good for?

This apt.conf is only used inside chroot and currently only in effect for &quot;''./whonix_createvm -tg-source''&quot; and &quot;''./whonix_createvm -tg-source''&quot;.

It points to ''http://192.168.0.2:3142'', which is expected to be a Whonix-Workstation with apt-cacher-ng running. It's useful for running &quot;''apt-get install''&quot; and &quot;''apt-get source''&quot; inside chroot, because downloads are cached, which speeds up the build process when building several times in a row. (Debugging with only minor changes.)

In case you don't want to use it or to use another proxy, edit ''/home/user/Whonix/whonix_shared/usr/local/share/whonix/apt.conf'' (comment out with a # or change proxy settings). Don't forget ./whonix_createvm -tX-copyinto-pre after modifying the file.

== other ==

See [https://github.com/adrelanos/Whonix/tree/development/release Release Folder] in Whonix source code.

* Don't forget to update Whonix version number.
* [LeakTests]!
* [Test] the images before release! TODO: Needs big revision with all Whonix features.
* See if [Documentation] still makes sense.
* Update the [Changelog].
* See https://github.com/adrelanos/Whonix/blob/master/release/whonix_release
* Source Code

Whonix-Gateway

<pre>sudo ./whonix_createvm -tg-source</pre>
Whonix-Workstation

<pre>sudo ./whonix_createvm -tw-source</pre>
Pack. Upload.

* Upload the images.
* At least a few testers should test before posting a news. Testers may be found by posting a news.
* Check, if [ManualTBupdate] is still up to date.
* Update [Download].
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

[[include ref=WikiFooter]

