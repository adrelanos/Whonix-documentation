<!--
Copyright:

   Copyright (C) Amnesia <amnesia at boum dot org>
   Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
   
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
This wiki page is a fork of the Tails Trusting Tails signing key page, from this exact source <http://git.immerda.ch/?p=amnesia.git;a=blob;f=wiki/src/doc/get/trusting_tails_signing_key.mdwn;hb=63b68fb4970361131cbd1713b40521244e88c204>.
-->

[[include ref=WikiHeader]]

[TOC]

= Introduction =

Note that since all Whonix releases are signed with the same key, you will not have to verify the key every time and the trust you might progressively build in it will be built once and for all. Still, you will have to check the virtual machine images every time you download a new ones!

This page is strongly related to the [Trust] page.

= Simple =

<ol style="list-style-type: decimal;">
<li><p>Download adrelanos's OpenPGP key from [https://sourceforge.net/p/whonix/code/ci/b5e205ccb19a11e901124fe7f101fcb0c71b0c8c/tree/adrelanos.asc?format=raw sourceforge.net].</p></li>
<li><p>Store it as ''adrelanos.asc''.</p></li>
<li><p>Import the key.</p>
<p>gpg --import adrelanos.asc</p></li>
<li><p>Verify.</p>
<p>gpg --fingerprint 9B157153925C303A42253AFB9C131AD3713AAEEF</p></li></ol>

Should show.

<pre>pub   4096R/713AAEEF 2012-03-02
      Key fingerprint = 9B15 7153 925C 303A 4225  3AFB 9C13 1AD3 713A AEEF
uid                  adrelanos &lt;adrelanos at riseup dot net&gt;
sub   4096R/794279C4 2012-03-02</pre>
<ol start="5" style="list-style-type: decimal;">
<li>For better security, read below.</li></ol>

= Advanced =

== Correlates several downloads of Whonix signing key ==

A simple technique to increase the trust you can put in Whonix signing key would be to download it several times, from several locations, several computers, possibly several countries, etc.

You could also use this technique to compare keys downloaded by your friends or other people you trust.

Downloading the key from the same server only lowers the possibility of a man-in-the-middle attack for a part of the route. The following figure illustrates that best.

<pre>user &lt;-&gt; user ISP &lt;-&gt; internet &lt;-&gt; sourceforge.net ISP &lt;-&gt; sourceforge.net server
MITM less likely for this route |  no help for this route</pre>
For this reasons adrelanos's homepage, which describes and contains adrelano's OpenPGP key is mirrored at seven different places. Download adrelanos's key from all those places and store it as ''adrelanos1.asc'', ''adrelanos2.asc'', ''adrelanos3.asc'', etc.

(1.) [https://github.com/adrelanos/Whonix adrelanos's homepage on github]; ([https://raw.github.com/adrelanos/Whonix/master/adrelanos.asc key download])

Github.com is accessible over SSL. <sup>1</sup>

(2.) [https://sourceforge.net/p/whonix/code/ci/1c4dc70fde6459002437c4965fe02c9e7a1ab5c8/tree/ adrelanos's homepage on sourceforge.net]; [https://sourceforge.net/p/whonix/code/ci/b5e205ccb19a11e901124fe7f101fcb0c71b0c8c/tree/adrelanos.asc sourceforge]; ([https://sourceforge.net/p/whonix/code/ci/b5e205ccb19a11e901124fe7f101fcb0c71b0c8c/tree/adrelanos.asc?format=raw key download])

SSL <sup>1</sup> available for users logged into sourceforge.net.

(3.) [https://gitorious.org/whonix/whonix/blobs/master/README.g adrelanos's homepage on gitorious]; ([https://gitorious.org/whonix/whonix/blobs/raw/master/adrelanos.asc key download])

Gitorious.org is accessible over SSL. <sup>1</sup>

(4.) [http://su6ephfi7dtxnbtb.onion/ adrelanos's homepage on Free Onion Hosting Service]

Encrypted end-to-end <sup>2</sup>. Anonymous admin.

(5.) [https://trac.torproject.org/projects/tor/wiki/doc/proper adrelanos's homepage on torproject.org wiki]

SSL available. <sup>1</sup> Anyone can edit the torproject.org wiki and exchange content with malicious one. Therefore check the history feature. Obviously, I do trust Tor and torproject.org. My wiki account &quot;''proper''&quot; should be genuine, therefore changes by &quot;''proper''&quot; should be legit.

(6.) [https://savannah.gnu.org/people/viewgpg.php?user_id=89289 adrelanos OpenPGP key mirror on savannah.gnu.org profile page]

SSL available. <sup>1</sup> The following command is recommend to enforce downloading the key over SSL.

<pre>## Not forced through Tor, unless you are using Whonix, torsocks or similar.
curl --tlsv1 --proto =https --output adrelanos.asc.4 https://savannah.gnu.org/people/viewgpg.php?user_id=89289</pre>
(7.) [http://p4vm6o4n4hbfqxhy.onion/ adrelanos's homepage on torhost.onion Free Onion Hosting Service]

Encrypted end-to-end <sup>2</sup>. Anonymous admin.

(8.) adrelanos's OpenPGP key mirror on OpenPGP keyserver

No SSL. Should really be only used as a mirror.

<pre>## Not forced through Tor, unless you are using Whonix, torsocks or similar.
gpg --keyserver x-hkp://pool.sks-keyservers.net --recv-keys 9B157153925C303A42253AFB9C131AD3713AAEEF</pre>
Verify.

<pre>gpg --fingerprint 9B157153925C303A42253AFB9C131AD3713AAEEF</pre>
Should show.

<pre>pub   4096R/713AAEEF 2012-03-02
      Key fingerprint = 9B15 7153 925C 303A 4225  3AFB 9C13 1AD3 713A AEEF
uid                  adrelanos &lt;adrelanos at riseup dot net&gt;
sub   4096R/794279C4 2012-03-02</pre>
Footnotes: <font size="-3"> ,, <sup>1</sup> See [SSL] for comments on SSL (in)security. <sup>2</sup> Because it's a Tor hidden service. Not exactly end-to-end, see [https://sourceforge.net/p/whonix/wiki/Threat%20Model/#notes-about-end-to-end-security-of-hidden-services Notes about End-to-end security of Hidden Services] for details. </font>

Each time you re-import the key from a different source.

<pre>gpg --import adrelanos.asc 
gpg --import adrelanos1.asc 
gpg --import adrelanos2.asc 
...</pre>
It should always show.

<pre>gpg: key 713AAEEF: &quot;adrelanos &lt;adrelanos at riseup dot net&gt;&quot; not changed
gpg: Total number processed: 1
gpg:              unchanged: 1</pre>
And.

<pre>gpg --fingerprint</pre>
Should always show the same fingerprint and only contain. (Besides keys you imported knowingly earlier, perhaps your friends keys.)

<pre>pub   4096R/713AAEEF 2012-03-02
      Key fingerprint = 9B15 7153 925C 303A 4225  3AFB 9C13 1AD3 713A AEEF
uid                  adrelanos &lt;adrelanos at riseup dot net&gt;
sub   4096R/794279C4 2012-03-02</pre>
Unless the new key is signed with the old key, something fishy is going on.

== Further reading on OpenPGP ==

* [https://en.wikipedia.org/wiki/GNU_Privacy_Guard GnuPG wikipedia], a free OpenPGP software
* [http://www.apache.org/dev/openpgp.html Apache: How To OpenPGP]
* [http://www.debian.org/events/keysigning Debian: Keysigning], a tutorial on signing keys of other people
* [http://www.rubin.ch/pgp/weboftrust.en.html rubin.ch: Explanation of the web of trust of PGP]
* [https://sourceforge.net/p/whonix/wiki/OpenPGP/ OpenPGP key distribution strategies]

== See Also ==

* [Trust]
* [https://sourceforge.net/p/whonix/wiki/OpenPGP/ OpenPGP key distribution strategies]

= License =

<pre>Whonix Trusting Whonix Signing Key wiki page Copyright (C) Amnesia &lt;amnesia at boum dot org&gt;
Whonix Trusting Whonix Signing Key wiki page Portions Copyright (C) 2012 adrelanos &lt;adrelanos at riseup dot net&gt;

This program comes with ABSOLUTELY NO WARRANTY; for details see the wiki source code.
This is free software, and you are welcome to redistribute it
under certain conditions; see the wiki source code for details.</pre>
= Footer =

[[include ref=WikiFooter]]

