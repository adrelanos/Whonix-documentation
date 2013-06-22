[[include ref=WikiHeader]]

[TOC]

<!--
Copyright:

   Whonix Warning wiki page Copyright (C) Amnesia <amnesia at boum dot org>
   Whonix Warning wiki page Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
   
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
This wiki page is a fork of the Unsafe Browser page, from this exact source <http://git.immerda.ch/?p=amnesia.git;a=blob;f=wiki/src/doc/anonymous_internet/unsafe_browser.mdwn;hb=21aa4cc26d72a02adf3f9818d6beca1a6a03fcd1>.
-->

= Logging in to captive portals =

== When Using VMs ==

Many publicly accessible Internet connections (usually available through a wireless network connection) require its users to register and login in order to get access to the Internet. This include both free and paid for services that may be found at Internet cafes, libraries, airports, hotels, universities etc. Normally in these situations, a so called ''captive portal'' intercepts any website request made and redirects the web browser to a login page. None of that works inside Whonix-Workstation, so a browser with unrestricted network access is necessary. The browser on the host operating system must be used for this purpose. Note that this means that '''the browser on the host is NOT anonymous''', so use it carefully.

== When Using Physical Isolation ==

As in Whonix 0.5.6, there is no unsafe browser on Whonix-Gateway. This is subject to change for next Whonix version.

In meanwhile you could use a third machine, which has access to clearnet or boot the hardware which runs Whonix-Gateway with another operating system (from USB), which isn't torified.

== Security recommendations ==

* While this browser can be used unrestrictively for anything, it is ''highly'' recommended to only use it for the purpose stated above, i.e. to access and login on captive portals.
* Do not run this browser at the same time as the normal, anonymous web browser. This makes it easy to not mistake one browser for the other, which could have catastrophic consequences for your anonymity.

= License =

<pre>Whonix Logging in to captive portals wiki page Copyright (C) Amnesia &lt;amnesia at boum dot org&gt;
Whonix Logging in to captive portals wiki page Portions Copyright (C) 2012 adrelanos &lt;adrelanos at riseup dot net&gt;

This program comes with ABSOLUTELY NO WARRANTY; for details see the wiki source code.
This is free software, and you are welcome to redistribute it
under certain conditions; see the wiki source code for details.</pre>
= Footer =

[[include ref=WikiFooter]]

