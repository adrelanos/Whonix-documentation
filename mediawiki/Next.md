'''Documentation for the NEXT Whonix version! ONLY for developers! No gurantee it really makes into the next Whonix version.'''

= TOC =

[[#toc|TOC]]

= Tor Browser =

Available languages as in October 2012:

<pre>ar
de
en-US
es-ES
fa
fr
it
ko
nl
pl
pt-PT
ru
vi
zh-CN</pre>
To check if further languages are supported visit https://www.torproject.org/dist/torbrowser/linux/ or http://idnxcnkne4qt76tg.onion/dist/torbrowser/linux/.

Always use.

<pre>export TB_LANG=&quot;&lt;language code&gt;&quot;</pre>
to set the language before running the Tor Browser Updater.

For example, for Vietnamese use:

<pre>export TB_LANG=&quot;vi&quot;</pre>
Replace &quot;vi&quot; with &quot;zh-CN&quot; for Chinese and so on.

= DNS on Whonix-Gateway =

Working.

Explanation http://sourceforge.net/p/whonix/discussion/general/thread/41116dda/

<pre>sudo chattr -i /etc/resolv.conf
sudo rm /etc/resolv.conf
sudo service networking restart
sudo su clearnet
ping google.com
# working</pre>
= Remove Proxy Settings =

Open ''start-tor-browser'' in the root of the Tor Browser folder and add right below ''#!/bin/sh''. <sup>1</sup> <sup>2</sup> <sup>3</sup> <sup>4</sup>

<pre>unset TOR_SOCKS_HOST
unset TOR_SOCKS_PORT</pre>
Now you could use Tor Button's settings dialog to set it to any other proxy.

Alternatively, if you want to set it to no proxy, you could additionally add below &quot;''unset TOR_SOCKS_PORT''&quot;.

<pre>export TOR_TRANSPROXY=1</pre>
= uwt =

We no longer place uwt wrappers into /usr/local/bin/<uwt-wrapped-application>. Therefore we now use dpkg-divert /usr/bin/<uwt-wrapped-application> to /usr/bin/<uwt-wrapped-application> and symlink /usr/bin/<uwt-wrapped-application> to /usr/bin/uwtwrapper.

Search for /usr/bin/* in documentation and update to /usr/bin/<uwt-wrapped-application>.real.

apt-cacher-ng-uwt moved to /usr/share/whonix/.

= Tor Controller =

Change documentation from arm to armwrapper.

= Dummy Tor =

Update dummy tor design page.

= Trust =

Add to [[#trust|Trust]].

== Introduction ==

At the moment, adrelanos is the only Whonix developer holding the Whonix APT repository OpenPGP signing key.

Since Whonix 0.6.2, Whonix provides an auto updater. While building Whonix using the build script, a APT repository has been added to /etc/apt/sources.list.d/whonix.list and Whonix's (adrelanos's) APT repository OpenPGP signing key has been added to apt-key by the whonix_repository tool.

When updated Whonix deb packages are uploaded to Whonix's APT repository, they will automatically get installed, next time you are upgrading your system using &quot;sudo apt-get update &amp;&amp; sudo apt-get dist-upgrade&quot;. If this is not what you want, this can be optionally disabled. Below is a security discussion about the advantages, disadvantages and differences and instructions on how to disable Whonix's APT repository.

== When Building from Source Code ==

When it comes to trust, there is a big difference if you are building Whonix from source code. When you build Whonix using the build script and verified the source code to be non-malicious and reasonable bug free, Whonix developers have no way to access your system. With Whonix's APT repository enabled however, Whonix developers holding a Whonix repository signing key could always release a malicious update and gain full access on your machines.

If you distrust Whonix developers, you can omit adding Whonix's APT repository signing key and omit the creation of /etc/apt/sources.list.d/ to your build. Just create a file in <whonix_source_folder>/buildconfig.d and add &quot;export WHONIX_APT_REPOSITORY_DISTRUST_ENV=1&quot; at the bottom of help-steps/variables.

<pre>export WHONIX_APT_REPOSITORY_DISTRUST_ENV=1</pre>
To prevent Whonix's APT repository getting added if you later create an updated Whonix deb package, you should create <whonix_source_folder>/whonix_shared/etc/environment (while building or /etc/environment if you already build and forget this step) and add.

<pre>WHONIX_APT_REPOSITORY_DISTRUST_ENV=1</pre>
(And/)or create a file <whonix_source_folder>/whonix_shared/etc/whonix.d/50_aptrepository_user and add.

<pre>WHONIX_APT_REPOSITORY_DISTRUST_CONFIG=&quot;1&quot;</pre>
If you want to delete all related code, get into Whonix source code folder and delete the following two files.

<pre>rm --verbose whonix_shared/usr/share/whonix/postinst.d/70_whonix_apt_key
rm --verbose whonix_shared/usr/bin/whonix_repository</pre>
== When using the Whonix-Default-Download Version ==

There is also a difference when using Whonix-Default-Download version. On one hand, when not using Whonix's APT repository, Whonix developers could sneak in a backdoor into the binary builds (download version) (the rest of the page above goes into this subject), which is worse enough. And on the other hand, while using Whonix's APT repository, Whonix developers could sneak in a backdoor at any time. Also notable, while the binary builds contain binary packages (which are downloaded from Debian repository while building), which makes it easier to sneak a backdoor in, the the Whonix deb packages do not contain any compiled code yet (only configuration files, scripts, comments) (which might change with a malicious update). As long as there is no compiled code inside Whonix deb packages, it might be easier for auditors, to catch a backdoor in update deb packages (unless its a targeted attack) compared to the binary builds (download version).

If Whonix is already installed, you can disable Whonix's APT repository using.

<pre>whonix_repository --disable</pre>
If you don't want to disable Whonix's APT repository after manually updating Whonix (manually downloading and installing updated Whonix deb packages), create a file /etc/environment.

<pre>sudo nano /etc/environment</pre>
And add.

<pre>export WHONIX_APT_REPOSITORY_DISTRUST_ENV=1</pre>
(And/)or create a file /etc/whonix.d/50_aptrepository_user.

<pre>sudo nano /etc/whonix.d/50_aptrepository_user</pre>
And add.

<pre>WHONIX_APT_REPOSITORY_DISTRUST_CONFIG=&quot;1&quot;</pre>
The whonix_repository tool has also a man page, which summarizes how to use it.

<pre>man whonix_repository</pre>
When Whonix's APT repository is disabled, there is no auto updater and the situation is the same as in Whonix 0.5.6 below.

== Security Conclusion ==

Legend:

* *: one star.
* one star: bad
* more stars: better
* 4 starts: best

<table>
<thead>
<tr class="header">
<th align="left"></th>
<th align="left">Whonix-Default-Download with Whonix APT Repository</th>
<th align="left">Whonix-Default-Download without Whonix APT Repository</th>
<th align="left">Building from Source Code and using Whonix APT Repository</th>
<th align="left">Building from Source Code without using Whonix APT Repository</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">security</td>
<td align="left">*</td>
<td align="left">**</td>
<td align="left">''*''</td>
<td align="left">****</td>
</tr>
<tr class="even">
<td align="left">convenience</td>
<td align="left">****</td>
<td align="left">''*''</td>
<td align="left">**</td>
<td align="left">*</td>
</tr>
</tbody>
</table>

The least secure and most convenient way is to use Whonix is using Whonix-Default-Download and to leave Whonix's repository enabled.

It's a bit safer to use Whonix-Default-Download version and to disable Whonix's APT repository. When updated Whonix deb packages are released, download them manually, verify them manually and install them manually. Big security bonus points for verifying the deb package contents before installing them.

== system requirements ==

1024x768 for terminal (before the desktop environment starts) set in /etc/default/grub, unless manually reduced.

128 MB RAM for Whonix-Gateway without graphical desktop environment 768 MB RAM for Whonix-Gateway with graphical desktop environment

128 MB RAM for Whonix-Workstation without graphical desktop environment 768 MB RAM for Whonix-Workstation with graphical desktop environment

== whonixcheck/timesync writing to tty1 ==

Its difficult to keep terminal users, i.e. for users who are not using a graphical desktop environment, posted with the status if their system. Therefore two applications coming with Whonix, timesync and whonixcheck, will do something unique, or at least very rare.

Even if you are logged into your terminal tty1 and see a command prompt, it can happen that you suddenly see status messages from whonixcheck or timesync. This can be nice for example once your Whonix-Gateway configured to your liking (if you needed to do that at all) and just want to get posted with status messages about your system. On the other hand, this can be disturbing, if you're currently doing something, like editing a configuration file and then suddenly status messages are written to your screen. In that case, it's advises to log into tty other than tty1, for example tty2.

* Default-Download-Version users can use the Virtual Box host key (right ctrl by default) and F2: right ctrl + F2
* Physical isolation users can use the standard feature, which comes with Debian: ctrl + ALT + F2

== Autostart Desktop Environment based on Free RAM and Other Settings ==

When booting up, you will be prompted and can always manually press ctrl + c to prevent KDE from starting.

By default, since Whonix 0.6.2, Whonix-Gateway comes with 768 MB virtual RAM. This can be reduced on systems with low resources.

* If there is more than 512 MB RAM in total, the desktop environment (KDE by default) will be started.
* If less than 512 MB RAM in total (for example, only 128 MB RAM in total), KDE (kdm) will not be started.

This should be be quite convenient, because users with low RAM could reduce (Whonix-Gateway) RAM to 128 MB and even if they sometimes wanted to configure/check something, they could assign 512 RAM and automagically boot into the graphical KDE desktop. There are also many settings in /etc/whonix.d/ to configure this feature, so if you want, you can also add a lot RAM and still don't boot into a desktop environment, use different display managers and so on.

= Footer =

[[include ref=WikiFooter]]

