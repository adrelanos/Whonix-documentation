<!--
Copyright:

   Whonix Verify_the_virtual_machine_images_using_the_command_line wiki page Copyright (C) Amnesia <amnesia at boum dot org>
   Whonix Verify_the_virtual_machine_images_using_the_command_line wiki page Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
   
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
The Whonix Verify_the_virtual_machine_images_using_the_command_line wiki page is forked from the Tails Verify the ISO image using the command line  page, from this exact source <http://git.immerda.ch/?p=amnesia.git;a=blob;f=wiki/src/doc/get/verify_the_iso_image_using_the_command_line.html;hb=ec769a098398fc009b617d9f0aef56310497e518>.
-->

[[include ref=WikiHeader]]

[TOC]

= Verify the virtual machine images using the command line =

You need to have GnuPG installed. GnuPG is the common OpenPGP implementation for Linux: it is installed by default under Debian, Ubuntu, Whonix and many other distributions.

First, [https://sourceforge.net/p/whonix/wiki/TrustingWhonixSigningKey/ download Whonix signing key].

Open a terminal and import Whonix signing key with the following commands:

<pre>cd [the directory in which you downloaded the key]
cat adrelanos.asc | gpg --keyid-format long --import</pre>
The output should tell you that the key was imported:

<pre>gpg: key 9C131AD3713AAEEF: public key &quot;adrelanos &lt;adrelanos at riseup dot net&gt;&quot; imported
gpg: Total number processed: 1
gpg:               imported: 1  (RSA: 1)</pre>
'''If you had already imported Whonix signing key in the past''', the output should tell you that the key was not changed:

<pre>gpg: key 9C131AD3713AAEEF: &quot;adrelanos &lt;adrelanos at riseup dot net&gt;&quot; not changed
gpg: Total number processed: 1
gpg:              unchanged: 1</pre>
'''If you are shown the following message''' at the end of the output:

<pre>gpg: no ultimately trusted keys found</pre>
Analyse the other messages as usual: this extra message doesn't relate to the Whonix signing key that you downloaded and usually means that you didn't create an OpenPGP key for yourself yet, which of no importance to verify the virtual machine images.

Now, '''download the cryptographic signature''' corresponding to the virtual machine images you want to verify and save it in the same folder as the virtual machine images:

https://sourceforge.net/p/whonix/wiki/Download/#whonix-signature

Then, '''start the cryptographic verification''', it can take several minutes:

<pre>cd [the virtual machine images directory]
gpg --keyid-format long --verify Whonix-Gateway.ova.sig Whonix-Gateway.ova</pre>
'''If the ISO image is correct''' the output will tell you that the signature is good:

<pre>gpg: Signature made Sun Nov 25 21:48:54 2012 UTC
gpg:                using RSA key 9C131AD3713AAEEF
gpg: Good signature from &quot;adrelanos &lt;adrelanos at riseup dot net&quot;</pre>
This might be followed by a warning saying:

<pre>gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 9B15 7153 925C 303A 4225  3AFB 9C13 1AD3 713A AEEF</pre>
This doesn't alter the validity of the signature according to the key you downloaded. This warning rather has to do with the trust that you put in Whonix signing key. See, [https://sourceforge.net/p/whonix/wiki/TrustingWhonixSigningKey/ Trusting Whonix signing key]. To remove this warning you would have to personally sign Whonix signing key with your own key.

'''If the ISO image is not correct''' the output will tell you that the signature is bad:

<pre>gpg: Signature made Sun Nov 25 21:48:54 2012 UTC
gpg:                using RSA key 9C131AD3713AAEEF
gpg: BAD signature from &quot;adrelanos &lt;adrelanos at riseup dot net&gt;&quot;</pre>
'''Repeat these steps for Whonix-Workstation as well.'''

<pre>cd [the virtual machine images directory]
gpg --keyid-format long --verify Whonix-Workstation.ova.sig Whonix-Workstation.ova</pre>
= License =

<pre>Whonix Verify_the_virtual_machine_images_using_the_command_line wiki page Copyright (C) Amnesia &lt;amnesia at boum dot org&gt;
Whonix Verify_the_virtual_machine_images_using_the_command_line wiki page Portions Copyright (C) 2012 adrelanos &lt;adrelanos at riseup dot net&gt;

This program comes with ABSOLUTELY NO WARRANTY; for details see the wiki source code.
This is free software, and you are welcome to redistribute it
under certain conditions; see the wiki source code for details.</pre>
= Footer =

[[include ref=WikiFooter]]

