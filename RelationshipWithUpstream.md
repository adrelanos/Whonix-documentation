<!--
Copyright:

   Whonix RelationshipWithUpstream wiki page Copyright (C) Amnesia <amnesia at boum dot org>
   Whonix RelationshipWithUpstream wiki page Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
   
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
The Whonix RelationshipWithUpstream wiki page is forked from the Tails RelationshipWithUpstream page, from this exact source <http://git.immerda.ch/?p=amnesia.git;a=blob;f=wiki/src/contribute/relationship_with_upstream.mdwn;hb=f755d5cbf6f7a67543729e531c33e319d4db4c5c>.
-->

[[include ref=WikiHeader]]

[TOC]

# Why this document? #
The [Debian Derivatives Guidelines](https://wiki.debian.org/Derivatives/Guidelines) encourages "derivative distributions to mention and define their relationship with Debian". Because this seems like a great idea to me, I wrote this statement that not only covers Whonix's relationship with Debian, but also Whonix's relationship with any one of its upstream projects.

# Summary #
For various reasons Whonix tries to diverge by the smallest possible amount from its upstream projects, and especially from Debian:

* Adrelanos wants to share his work with the rest of the Free Software community.
* Adrelanos values maintainability very much: I believe my users are best served if I keep the amount of work needed to maintain Whonix the smallest possible.

# How #
## Debian specific ##
### Derivatives Census ##
[Whonix participates in the Derivatives Census.](http://wiki.debian.org/Derivatives/Census/Whonix)

### Infrastructure ###
Debian Derivatives Guidelines recommends *"We encourage derivative distributions to use Debian infrastructure and the software that powers Debian infrastructure where possible."*.

Whonix makes heavy use of that. Only official Debian repositories are used. Adrelanos is very thankful, that Debian derivatives are allowed to do so. The Whonix project has neither the infrastructure, the founding nor the manpower to run it's own repositories.

### Debian packages ###
Neither binary nor source packages are modified.

### Keyrings ###
Whonix does not modify keyrings.

Adrelanos's GPG key is copied into Whonix virtual machines at build time. It is only used to ensure authenticity of Whonix News.

### Releases ###
See [About Debian](https://sourceforge.net/p/whonix/wiki/OperatingSystem/#about-debian) for reasons to choose Wheezy. When Wheezy gets stable, Whonix will be based on stable. Depending on user feedback Whonix will remain based on stable. Depending on user feedback and stability of testing, Whonix might be based on testing.

### Trademark ###
Whonix is and will never be called Debian. It must always be clear that Whonix is a Debian derivative or based on Debian.

Adrelanos e-mailed trademark at debian.org and briefly explained Whonix. Debian Leader Stefano Zacchiroli said, there will be no trademark issues as long as Whonix will not claim to be Debian, which will of course never happen.

### De-/Re-branding ###
Not necessary. See Trademark above.

### Bug reports ###
Reportbug is unchanged. No Debian packages are modified. This still needs discussion.

### Popularity Contest ###
Not installed in Whonix. Reasons are in the [Popularity Contest](https://sourceforge.net/p/whonix/wiki/OperatingSystem/#popularity-contest) chapter.

## General ##
### Upstream software ###
When my technical skills and time allows, I try to push my changes upstream when we need to modify software I ship. Only package selection, configuration files and scripts are modified.

### Upstream Bug tracking systems ###
All bugs found in Whonix, will be checked, if they also apply to upstream. If that is the case, adrelanos will look if the bug has already been reported. If adrelanos can contribute something constructive, he will do so. In case there is not yet a bug report, adrelanos will report.

The same goes for wishlist/enhancement requests.

# License #
    Whonix RelationshipWithUpstream wiki page Copyright (C) Amnesia <amnesia at boum dot org>
    Whonix RelationshipWithUpstream wiki page Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
    
    This program comes with ABSOLUTELY NO WARRANTY; for details see the wiki source code.
    This is free software, and you are welcome to redistribute it
    under certain conditions; see the wiki source code for details.

# Footer #
[[include ref=WikiFooter]]