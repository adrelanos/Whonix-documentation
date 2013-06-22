[[include ref=WikiHeader]]

[TOC]

<!--
Copyright:

   Whonix Verify_the_virtual_machine_images_using_other_operating_systems wiki page Copyright (C) Amnesia <amnesia at boum dot org>
   Whonix Verify_the_virtual_machine_images_using_other_operating_systems wiki page Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
   
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
The Whonix Verify_the_virtual_machine_images_using_other_operating_systems wiki page is a fork of the Tails Verify the ISO image using other operating systems page, from this exact source <http://git.immerda.ch/?p=amnesia.git;a=blob;f=wiki/src/doc/get/verify_the_iso_image_using_other_operating_systems.html;hb=24b927c2053668b662664513a59b5402ba51b50a>.
-->

= Verify the virtual machine images using other operating systems =

GnuPG, a common free software implementation of OpenPGP has versions and graphical frontends for both Windows and Mac OS X. This also make it possible to check the cryptographic signature with those operating systems:

[http://www.gpg4win.org/ Gpg4win], for Windows [http://www.gpgtools.org/ GPGTools], for Mac OS X

You will find on either of those websites detailed documentation on how to install and use them.

'''For Windows using Gpg4win'''

After installing Gpg4win, download Whonix signing key:

[https://sourceforge.net/p/whonix/wiki/TrustingWhonixSigningKey/ Whonix signing key]

[http://www.gpg4win.org/doc/en/gpg4win-compendium_15.html Consult the Gpg4win documentation to import it]

Then, download the cryptographic signature corresponding to the virtual machine image you want to verify:

[https://sourceforge.net/p/whonix/wiki/Download/#whonix-signature Whonix Signature]

[http://www.gpg4win.org/doc/en/gpg4win-compendium_24.html#id4 Consult the Gpg4win documentation to check the signature]

'''For Mac OS X using GPGTools'''

After installing GPGTools, you should be able to follow the instruction for [https://sourceforge.net/p/whonix/wiki/Verify_the_virtual_machine_images_using_the_command_line/ Linux with the command line]. To open the command line, navigate to your Applications folder, open Utilities, and double click on Terminal.

= License =

<pre>Whonix Verify_the_virtual_machine_images_using_other_operating_systems wiki page Copyright (C) Amnesia &lt;amnesia at boum dot org&gt;
Whonix Verify_the_virtual_machine_images_using_other_operating_systems wiki page Portions Copyright (C) 2012 adrelanos &lt;adrelanos at riseup dot net&gt;

This program comes with ABSOLUTELY NO WARRANTY; for details see the wiki source code.
This is free software, and you are welcome to redistribute it
under certain conditions; see the wiki source code for details.</pre>
= Footer =

[[include ref=WikiFooter]]

