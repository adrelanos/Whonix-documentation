[[include ref=WikiHeader]]

[TOC]

<!--
Copyright:

   Whonix Verify_the_virtual_machine_images_using_Linux wiki page Copyright (C) Amnesia <amnesia at boum dot org>
   Whonix Verify_the_virtual_machine_images_using_Linux wiki page Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
   
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
This Whonix Verify_the_virtual_machine_images_using_Linux wiki page is a fork of the Tails Verify the ISO image using Linux with Gnome page, from this exact source <http://git.immerda.ch/?p=amnesia.git;a=blob;f=wiki/src/doc/get/verify_the_iso_image_using_gnome.html;hb=13f804421097ba25fe9836d7df0fd59d0da3d1f6>.
-->


# Verify the virtual machine images using Linux

You need to have the *kgpg* package installed. If you're not sure or want to install it, under Debian, Ubuntu or Whonix you can issue the following commands:

    sudo apt-get update
    sudo apt-get install kgpg

First, download Whonix signing key:

[Download Whonix Signing Key](https://sourceforge.net/p/whonix/wiki/TrustingWhonixSigningKey/)

Open *adrelanos.asc* with kgpg.

You will get notified will the following message:

(E-mail was changed to adrelanos at riseup do net, but this doesn't change anything, since the key fingerprint remains the same.)

![kgpg_key_imported_new](http://whonix.sourceforge.net/screenshots/kgpg_key_imported_new.png)

Or if you previously already imported the key:

![kgpg_key_imported_unchanged](http://whonix.sourceforge.net/screenshots/kgpg_key_imported_unchanged.png)

Now, **download the cryptographic signature** corresponding to the virtual machine image you want to verify **and store it in the same folder as the virtual machine image**:

[Download Whonix Signature](https://sourceforge.net/p/whonix/wiki/Download/#whonix-signature)

Start kgpg, go to kgpg -> File -> Open Editor -> Signature -> Verify Signature... -> Choose the downloaded cryptographic signature.

It will **take a while** and there is **no progress meter**. Please wait a few moments.

**If the virtual machine image is correct** you will get a notification telling you that the signature is good:

(E-mail was changed to adrelanos at riseup do net, but this doesn't change anything, since the key fingerprint remains the same.)

![kgpg_verification_success](http://whonix.sourceforge.net/screenshots/kgpg_verification_success.png)

**If the virtual machine image is not correct** you will get a notification telling you that the signature is bad:

(E-mail was changed to adrelanos at riseup do net, but this doesn't change anything, since the key fingerprint remains the same.)

![kgpg_verification_failed](http://whonix.sourceforge.net/screenshots/kgpg_verification_failed.png)

# License #
    Whonix Verify_the_virtual_machine_images_using_Linux wiki page Copyright (C) Amnesia <amnesia at boum dot org>
    Whonix Verify_the_virtual_machine_images_using_Linux wiki page Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
    
    This program comes with ABSOLUTELY NO WARRANTY; for details see the wiki source code.
    This is free software, and you are welcome to redistribute it
    under certain conditions; see the wiki source code for details.

# Footer #
[[include ref=WikiFooter]]