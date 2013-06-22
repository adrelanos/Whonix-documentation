[[include ref=WikiHeader]]

[TOC]

= Introduction =

The [https://sourceforge.net/p/whonix/wiki/Technical%20Introduction/#whonix-framework Whonix Framework] supports any operating system.

'''''Using a Whonix-Download-Workstation is easier and provides more Security out of the box!''''' It's your responsibility to get the same security features for a Whonix-Custom-Workstation, see [https://sourceforge.net/p/whonix/wiki/OtherOperatingSystems/#security-comparison-whonix-download-workstation-vs-whonix-custom-workstation Security Comparison: Whonix-Download-Workstation vs. Whonix-Custom-Workstation] at the bottom of the page for details.

The Whonix-Gateway already supports torification of any operating system, including Microsoft Windows and others. As an transparent or isolating proxy, see below for more information.

= Windows-Whonix-Workstation =

XP, Vista and Windows 7 are are known to work behind Whonix-Gateway. While it's possible, it's not recommend and only for advanced users. This is because, there are issues with Windows. Those are not Whonix issues. Whonix developers can not fix those issues. One issue is, that Windows is closed source. Rather, Windows is affected by [https://trac.torproject.org/projects/tor/wiki/doc/TransparentProxyLeaks Transparent Proxy Leaks] and other issues. For more information and depending on your security requirements, read the following chapters.

== Easiest ==

Easiest, but least secure option.

(1). Download and use the default Whonix-Gateway.

Import it the same way you would do for Whonix-Default/Download-Version

(2). Create a Virtual Box VM.

Virtual Box -&gt; Machine -&gt; New -&gt; Next -&gt; Enter Name -&gt; Enter Operating System and Version -&gt; Next -&gt; define RAM -&gt; Next &gt; create a new hdd (or not) -&gt; Next -&gt; disk format doesn't matter, VDI works fine however -&gt; Next -&gt; dynamically or fixed size is a matter of preference -&gt; Next hdd size and location is a matter of preference -&gt; Next -&gt; Create

(3). Switch Virtual Box VM settings.

Choose the newly created VM -&gt; Settings -&gt; System -&gt; Motherboard -&gt; Hardware Clock in UTC

System -&gt; Processor -&gt; Enable PAE/NX if available

Network -&gt; Adapter 1 -&gt; attached to Internal Network (Important!)

Network -&gt; Adapter 1 -&gt; Name (of Internal Network) (Important!): Whonix

USB -&gt; uncheck Enable USB controller

-&gt; OK

(4). Start VM and Install Operating System.

You don't have to install updates while installing. You can do that right after installing, after the network has been set up.

username: user computer name: host

(5). Configure network:

For Windows 7 (similar in Windows XP): In Control Panel &gt; Network and Sharing Center: click on &quot;Change adapter settings&quot; Right-click on local area connection &gt; properties In property window: double-click Internet Protocol Version 4, use the following settings:

<pre>IP address 192.168.0.50
Subnet netmask 255.255.255.0
Default gateway 192.168.0.10
Preferred DNS server 192.168.0.10</pre>
(6). Download operating system updates.

= Whonix-GNU/Linux-Workstation =

== Easiest ==

Easiest, but least secure option.

(1). Download and use the default Whonix-Gateway.

Import it the same way you would do for Whonix-Default/Download-Version

(2). Create a Virtual Box VM.

Virtual Box -&gt; Machine -&gt; New -&gt; Next -&gt; Enter Name -&gt; Enter Operating System and Version -&gt; Next -&gt; define RAM -&gt; Next &gt; create a new hdd (or not) -&gt; Next -&gt; disk format doesn't matter, VDI works fine however -&gt; Next -&gt; dynamically or fixed size is a matter of preference -&gt; Next hdd size and location is a matter of preference -&gt; Next -&gt; Create

(3). Switch Virtual Box VM settings.

Choose the newly created VM -&gt; Settings -&gt; System -&gt; Motherboard -&gt; Hardware Clock in UTC

System -&gt; Processor -&gt; Enable PAE/NX if available

Network -&gt; Adapter 1 -&gt; attached to Internal Network (Important!)

Network -&gt; Adapter 1 -&gt; Name (of Internal Network) (Important!): Whonix

USB -&gt; uncheck Enable USB controller

-&gt; OK

(4). Start VM and Install Operating System.

You don't have to install updates while installing. You can do that right after installing, after the network has been set up.

username: user computer name: host

(5). Configure network:

Open a Terminal and type.

<pre>sudo nano /etc/network/interfaces</pre>
You only need to configure eth0:

<pre># This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

# The loopback network interface, leave as it is
auto lo
iface lo inet loopback

auto eth0
#iface eth0 inet dhcp
iface eth0 inet static
# increment last octet on additional workstations
       address 192.168.0.12
       netmask 255.255.255.0
       #network 192.168.0.0
       #broadcast 192.168.0.255
       gateway 192.168.0.10</pre>
Open /etc/resolv.conf.

<pre>sudo nano /etc/resolv.conf</pre>
and delete everything, then add

<pre>nameserver 192.168.0.10</pre>
(6). Download operating system updates.

Debian based Linux, such as Ubuntu:

<pre>sudo apt-get update &amp;&amp; sudo apt-get dist-upgrade</pre>
= More security =

Recommendations:

* Verify operating system installation CD, compare with sha256 hash or even better verify the gpg signature, if available.
* Install while the Virtual Machine has no internet connection.
* Set your username to ''user''.
* Disable Internet Time Syncing.
* Set your Time Zone to ''UTC''.
* Set up a static IP.
* In case you want to run more than one Whonix-Workstation at the same time, it's recommend reading the Introduction in the [Multiple Whonix-Workstations] article.
* Read [Security Guide], [Documentation] and [Design] (which is Whonix-Example-Implementation-Workstation (based on Debian GNU/Linux) specific) and try to apply as much from it to Windows as possible.

= Even more security =

== General ==

Recommendations:

* Prevent [https://trac.torproject.org/projects/tor/wiki/doc/TransparentProxyLeaks Transparent Proxy Leaks] by disabling Whonix-Gateway's Transparent Proxy feature. Instead use your Windows Whonix-Workstation behind an [https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO/IsolatingProxy Isolating Proxy]. See [Stream Isolation] for more information and instructions on how to disable the Transparent Proxy feature.
* Check your host clock out of band (use a watch or atomic clock).
* Set your host and your Workstation clock to show seconds as well. After booting the Whonix-Windows-Workstation, add a random skew to your clock, maybe +/- 1 to 30 seconds. Optimal values are still under investigation. For reference, see [https://sourceforge.net/p/whonix/wiki/TimeSync/ Whonix's Secure And Distributed Time Synchronization Mechanism], it's Whonix-Example-Implementation-Workstation (based on Debian GNU/Linux) specific, but most information also applies to Windows. Since I am not aware of a tails_htp alternative for Windows, you have to do it manually.

== VM settings ==

'''TODO''': Check and expand.

In Whonix source code look into ''whonix_createvm'' for the functions general_setup, workstation_specific and hardware_modifications. Find out your VM name using.

<pre>vboxmanage list vms</pre>
You can and should drop the &quot;sudo -u $USERNAME&quot;.

Apply all required settings. Not required (because recommended earlier or done by the gui creation process):

--name storagectl --memory --pae --hardwareuuid <sup>1</sup> sethduuid <sup>1</sup> --intnet1 --cableconnected1 --macaddress1 <sup>1</sup> --audiocontroller --audio

<sup>1</sup> You can only use those, if you are not using a Whonix-Default/Download-Workstation, otherwise they conflict.

Example:

<pre>VBoxManage modifyvm &quot;yourvmname&quot; --synthcpu on</pre>
= Most security =

Use the default Whonix VMs and build them yourself from source.

= Ubuntu =

== General ==

Moved to [https://sourceforge.net/p/whonix/wiki/Ubuntu/ Ubuntu]

== About Ubuntu ==

Moved to [https://sourceforge.net/p/whonix/wiki/Ubuntu/#about-ubuntu About Ubuntu].

== Guest additions for Ubuntu Precise ==

Moved to [https://sourceforge.net/p/whonix/wiki/Ubuntu/ Ubuntu].

= Debian =

Whonix-Default/Download-Version is already based on Debian Wheezy. In case you want to build on top of stable, sid or whatever, you may be interested to read:

* How to obtain Debian safely: [https://sourceforge.net/p/whoni/wiki/Debian/ Debian ISO gpg verification]

= Security Comparison: Whonix-Download-Workstation vs. Whonix-Custom-Workstation =

== Introduction ==

Read first: [https://sourceforge.net/p/whonix/wiki/Comparison%20of%20different%20Whonix%20variants/ Comparison of Whonix, Tails and TBB]!

Note: Whonix-BuildYourselfFromSource-Workstation is of course the same as Whonix-Download-Workstation.

== Table ==

<table>
<thead>
<tr class="header">
<th align="left">_</th>
<th align="left">Whonix-Download-Workstation</th>
<th align="left">Whonix-Custom-Workstation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Based on</td>
<td align="left">Debian Wheezy GNU/Linux</td>
<td align="left">Any of your choice.</td>
</tr>
<tr class="even">
<td align="left">Amnesic</td>
<td align="left">No</td>
<td align="left">No</td>
</tr>
<tr class="odd">
<td align="left">Protection against root exploits (Malware with root rights) on the Workstation <sup>18</sup></td>
<td align="left">Yes <sup>1</sup> <sup>a</sup></td>
<td align="left">Yes <sup>1</sup> <sup>a</sup></td>
</tr>
<tr class="even">
<td align="left">IP/DNS protocol leak protection</td>
<td align="left">Full <sup>1</sup></td>
<td align="left">Full <sup>1</sup></td>
</tr>
<tr class="odd">
<td align="left">Takes advantage of Entry Guards</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
</tr>
<tr class="even">
<td align="left">Operating System Updates persist once updated</td>
<td align="left">Yes</td>
<td align="left">Depends if gets installed or is a Live CD.</td>
</tr>
<tr class="odd">
<td align="left">Hides hardware serials from malicious software</td>
<td align="left">Yes <sup>16</sup></td>
<td align="left">Yes <sup>16</sup></td>
</tr>
<tr class="even">
<td align="left">Collects (virtual) hardware serials</td>
<td align="left">No</td>
<td align="left">Depends on the custom operating system</td>
</tr>
<tr class="odd">
<td align="left">Includes Tor Browser</td>
<td align="left">Yes</td>
<td align="left">Your responsibility to install Tor Browser.</td>
</tr>
<tr class="even">
<td align="left">Includes Firefox privacy patches ([https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO/WebBrowsers reference]) and Tor Button (=Tor Browser)</td>
<td align="left">Yes, because it uses Tor Browser (without Tor/Vidalia).</td>
<td align="left">Your responsibility to install Tor Browser.</td>
</tr>
<tr class="odd">
<td align="left">Prevents Tor over Tor for Tor Browser</td>
<td align="left">Yes</td>
<td align="left">Your responsibility to prevent Tor over Tor.</td>
</tr>
<tr class="even">
<td align="left">Stream isolation to prevent identity correlation through circuit sharing</td>
<td align="left">Yes</td>
<td align="left">Your responsibility to use Stream Isolation.</td>
</tr>
<tr class="odd">
<td align="left">Stream isolates Tor Browser</td>
<td align="left">No <sup>14</sup></td>
<td align="left">No <sup>14</sup></td>
</tr>
<tr class="even">
<td align="left">Encryption</td>
<td align="left">Should be applied on host.</td>
<td align="left">Should be applied on host.</td>
</tr>
<tr class="odd">
<td align="left">Cold Boot Attack Protection <sup>8</sup></td>
<td align="left">No</td>
<td align="left">No</td>
</tr>
<tr class="even">
<td align="left">Secure Distributed Network Time Synchronization</td>
<td align="left">Yes</td>
<td align="left">Your responsibility to install it.</td>
</tr>
<tr class="odd">
<td align="left">Hides your time zone (set to UTC)</td>
<td align="left">Yes</td>
<td align="left">Your responsibility to set clock to UTC.</td>
</tr>
<tr class="even">
<td align="left">Hides your operating system account name</td>
<td align="left">Yes, set to user.</td>
<td align="left">Your responsibility to set username to user.</td>
</tr>
<tr class="odd">
<td align="left">Hides your MAC address from websites</td>
<td align="left">Invalid <sup>19</sup></td>
<td align="left">Invalid <sup>19</sup></td>
</tr>
<tr class="even">
<td align="left">Secures your MAC address from local LAN (sometimes ISP) <sup>20</sup></td>
<td align="left">No, planed, see. <sup>21</sup></td>
<td align="left">Your responsibility. <sup>20</sup> <sup>21</sup></td>
</tr>
<tr class="odd">
<td align="left">Hides your hosts MAC address from applications</td>
<td align="left">Yes <sup>24</sup></td>
<td align="left">Yes <sup>24</sup></td>
</tr>
<tr class="even">
<td align="left">Secure gpg.conf</td>
<td align="left">Yes</td>
<td align="left">Your responsibility to use a secure gpg.conf.</td>
</tr>
<tr class="odd">
<td align="left">Privacy enhanced IRC client configuration.</td>
<td align="left">Yes</td>
<td align="left">Your responsibility to configure the IRC client for enhanced privacy.</td>
</tr>
</tbody>
</table>

== Footnotes ==

Same footnotes as in [https://sourceforge.net/p/whonix/wiki/Comparison%20of%20different%20Whonix%20variants/ Comparison of Whonix, Tails and TBB / Security].

== Conclusion ==

The Whonix-Download-Workstation is already preconfigured with all Whonix extra security features.

A Whonix-Custom-Workstation ''can be made'' (Your responsibility!) as secure as a Whonix-Download-Workstation. If you simply create<sup>1</sup> a Whonix-Custom-Workstation it has still ''some'' security advantages, <font size="-3">for example full IP/DNS protocol leak protection</font>, but ''not all'', <font size="-3">for example it lacks Secure Distributed Network Time Synchronization</font>. The details are listed in the table above.

<font size="-3"> <sup>1</sup> Install or use a Live CD/DVD into Whonix-Workstation. </font>

= Footer =

[[include ref=WikiFooter]]

