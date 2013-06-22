[[include ref=WikiHeader]]

[TOC]

= Comparison of different Whonix variants =

== Related to Virtualization or Hardware ==

<table>
<thead>
<tr class="header">
<th align="left">Name</th>
<th align="left">Number of systems</th>
<th align="left">Security</th>
<th align="left">Usability</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">[OneVM]</td>
<td align="left">host+VM=2</td>
<td align="left">Better security than Tor Browser Bundle, Tor Live CDs.</td>
<td align="left">Installation instructions depend on host operating system.; More difficult to install.</td>
</tr>
<tr class="even">
<td align="left">Standard [Download] version</td>
<td align="left">host+VM+VM=3</td>
<td align="left">Same as OneVM.</td>
<td align="left">Easily redistributable and installable.</td>
</tr>
<tr class="odd">
<td align="left">[PhysicalIsolation] with bare metal Gateway</td>
<td align="left">host+VM+host=3</td>
<td align="left">Stronger than Standard Download version.</td>
<td align="left">Difficult to install, advanced users only.</td>
</tr>
<tr class="even">
<td align="left">[PhysicalIsolation] with virtualized Gateway</td>
<td align="left">host+VM+host+VM=4</td>
<td align="left">Higher attack surface.</td>
<td align="left">Easier to deploy. Four operating systems must be kept updated.</td>
</tr>
<tr class="odd">
<td align="left">[PhysicalIsolation] without any virtualization</td>
<td align="left">host+host=2</td>
<td align="left">Basically same as standard Physical Isolation.; Smaller attack surface <sup>1</sup> because not using Virtual Machines.; No protection against hardware fingerprinting.;</td>
<td align="left">Difficult to install, advanced users only.</td>
</tr>
</tbody>
</table>

Virtual machines can provide following security related features:

* Network isolation (connections can easily be forced through tor)
* Hardware isolation (hide unique hardware serials)
* Roll back feature
* Cheap and simple multi-level security through running multiple clones/VMs

Live CDs offer:

* Non-persistence in case of software compromises
* Anti-Forensics and deniability (no encryption keys to disclose, if it's powered down and RAM is wiped/faded everything is &quot;gone&quot;)
* But: difficult to roll out security updates

Footnotes:

<font size="-3"> ,, <sup>1</sup> See forum topic [https://sourceforge.net/p/whonix/discussion/general/thread/05abffad/ More or Less Protection inside a VM?] for some more discussion. </font>

== Related to Operating System ==

Multiple options for operating system.

* Debian Wheezy GNU/Linux (Default-Download-Version, recommend!).
* See also [OtherOperatingSystems], especially [https://sourceforge.net/p/whonix/wiki/OtherOperatingSystems/#security-comparison-whonix-download-workstation-vs-whonix-custom-workstation Security Comparison: Whonix-Download-Workstation vs. Whonix-Custom-Workstation]
* Any other, see ''Whonix Framework''.
* There is [https://sourceforge.net/p/whonix/wiki/HardenedGentooTG/ Hardened Gentoo based Whonix-Gateway]. (outdated, experts only, needs maintainer!)

== Security Comparison: Whonix-Download-Workstation vs. Whonix-Custom-Workstation ==

See [https://sourceforge.net/p/whonix/wiki/OtherOperatingSystems/#security-comparison-whonix-download-workstation-vs-whonix-custom-workstation Security Comparison: Whonix-Download-Workstation vs. Whonix-Custom-Workstation].

Unless otherwise stated, the documentation and design is about the Default-Download-Version.

= Footer =

[[include ref=WikiFooter]]

