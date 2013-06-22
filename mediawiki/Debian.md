[[include ref=WikiHeader]]

[TOC]

= Download and Verification =

The recommend way to verify the Debian Signing key is to use the [https://sourceforge.net/p/whonix/wiki/OpenPGP/ web of trust], which is more secure, but not available to everyone.

This chapter documents an alternative and supplementary way to verify the Debian Signing key using an existing installation such as Ubuntu, which is already trusted, for example because you bought it from a reseller or got it from a friend who verified it.

'''Should work for Debian and any Debian derivative.'''

# Go to the [http://cdimage.debian.org/ Debian Download Page]. Example, the [http://cdimage.debian.org/cdimage/release/current/i386/iso-dvd/ Debian Wheezy DVD i386 folder].
# Download.

* SHA512SUMS
* SHA512SUMS.sign
* DVD-1.iso

<ol start="3" style="list-style-type: decimal;">
<li><p>Install the debian-keyring package, which contains the signing key. This is because the the [http://www.debian.org/CD/verify Debian Verify] instructions are not accessible over SSL, neither the debian-keyring package can be downloaded over SSL. Downloading the debian-keyring package from the repository, lets apt-get verify it's integrity.</p>
<p>sudo apt-get install debian-keyring</p></li>
<li><p>Open a terminal and get into the folder where you downloaded SHA512SUMS and SHA512SUMS.sign (and DVD-1.iso).</p></li>
<li><p>Verify the SHA512SUMS file.</p>
<p>gpg --no-default-keyring --keyring /usr/share/keyrings/debian-role-keys.gpg --verify SHA512SUMS.sign</p></li>
<li><p>Must show.</p>
<p>gpg: Good signature</p></li></ol>

Otherwise something is wrong.

This might be followed by a warning saying:

<pre>gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.</pre>
This doesn't alter the validity of the signature according to the key you downloaded. This warning rather has to do with the trust that you put in key.

<ol start="7" style="list-style-type: decimal;">
<li>Done.</li></ol>

= Install =

** UNFINISHED! **

From usability perspective, [http://raphaelhertzog.com/2011/06/13/why-you-should-always-have-a-network-connection-when-installing-debian/ you should always have a network connection when installing Debian].

From security perspective, [http://www.debian.org/doc/manuals/securing-debian-howto/ch3.en.html#s3.3 you should not plug to the Internet until ready].

You may have noticed, the default desktop environment for Whonix's Virtual Machines is KDE. (You could change that.) It doesn't matter, which desktop environment you are going to use for Debian. The default desktop environment of Debian is GNOME. If you are already accustomed to Whonix (KDE), you could also use KDE for your Debian host as well (not a must).

<pre>Debian boot menu -&gt; Advanced Options -&gt; Alternative Desktop Environments -&gt;
Feel free to choose:
- KDE
- XDE
- XFCE</pre>
It's also possible to install another desktop environment after installing or to switch from one to another.

If you are wondering what the &quot;default&quot;, &quot;notebook&quot; or &quot;standard&quot; packages are about, see [http://wiki.debian.org/tasksel tasksel].

Check open ports.

<pre>su
netstat -anltp | grep &quot;LISTEN&quot;</pre>
Must should be none, i.e no reply.

Remove services, which open ports. <sup>1</sup>

<pre>su
apt-get remove dovecot-core openbsd-inetd bind9 samba cups apache2 postgres* 
apt-get remove exim4 exim4-daemon-light rpcbind openssh-server apache2.2-bin
apt-get autoremove</pre>
Check open ports again.

<pre>su
netstat -anltp | grep &quot;LISTEN&quot;</pre>
Must should be none, i.e no reply.

https://github.com/adrelanos/Whonix/blob/stable/host/whonix_firewall

<font size="-3"> ,, <sup>1</sup> For documentation purposes I made a Debian installation and installed as much services with taskel as possible, while having a network connection. (Simulating user misunderstanding.) A Debian default installation with default setting does not install all those packages. </font>

= Security =

[http://www.debian.org/doc/manuals/securing-debian-howto/ch12.en.html Quote]:

<blockquote>''Is Debian more secure than X?''

''A system is only as secure as its administrator is capable of making it. Debian's default installation of services aims to be secure, but may not be as paranoid as some other operating systems which install all services disabled by default.''
</blockquote>
I am not sure if they are referring to running services after installing them or having no services running (open ports) after a default installation with default settings. Debian doesn't do the latter, which is a pity.

Don't participate in popularity contest.

Some useful links. Parts of it are outdated (old Debian versions). Some stuff doesn't apply to Whonix host's.

* [http://www.debian.org/doc/manuals/securing-debian-howto Securing Debian Manual]
* [http://www.debian.org/doc/manuals/securing-debian-howto/ch12.en.html Securing Debian Manual Chapter 12 - Frequently asked Questions (FAQ)]
* [http://www.hermann-uwe.de/blog/towards-a-moderately-paranoid-debian-laptop-setup--part-1-base-system Towards a moderately paranoid Debian laptop setup (not only useful for laptops)]

= Footer =

[[include ref=WikiFooter]]

