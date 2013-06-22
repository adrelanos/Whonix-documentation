[[include ref=WikiHeader]]

[TOC]

= Comparison of Whonix, Tails, Tor Browser Bundle and Qubes OS TorVM =

== Usability ==

<table>
<thead>
<tr class="header">
<th align="left"></th>
<th align="left">Whonix</th>
<th align="left">Tails</th>
<th align="left">Tor on the host</th>
<th align="left">Qubes OS TorVM</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Difficulty to install additional software while IP remains hidden <sup>1</sup></td>
<td align="left">easy <sup>2</sup></td>
<td align="left">medium <sup>3</sup></td>
<td align="left">hard <sup>4</sup></td>
<td align="left">easy</td>
</tr>
<tr class="even">
<td align="left">Difficulty to initially install the anonymity software</td>
<td align="left">medium <sup>5</sup></td>
<td align="left">easy</td>
<td align="left">easy</td>
<td align="left">easy (?)</td>
</tr>
<tr class="odd">
<td align="left">Required knowledge to prevent the user shooting it's own feet <sup>7</sup></td>
<td align="left">hard</td>
<td align="left">hard</td>
<td align="left">hard</td>
<td align="left">hard</td>
</tr>
<tr class="even">
<td align="left">Pre-installed applications</td>
<td align="left">Not many. <sup>6</sup></td>
<td align="left">Nice selection.</td>
<td align="left">None.</td>
<td align="left">Not many. (?)</td>
</tr>
<tr class="odd">
<td align="left">Host clock too much off</td>
<td align="left">No connection to the Tor network until clock gets manually fixed.</td>
<td align="left">Uses [https://tails.boum.org/contribute/design/Time_syncing/ tordate] to fix it.</td>
<td align="left">No connection to the Tor network until clock gets manually fixed.</td>
<td align="left">No connection to the Tor network until clock gets manually fixed.</td>
</tr>
</tbody>
</table>

<font size="-3"> ,, <sup>1</sup> To do it safely. <sup>2</sup> Easy: In Whonix one could also install an [https://blog.torproject.org/blog/bittorrent-over-tor-isnt-good-idea Tor-unsafe] BitTorrent client. In worst case it would be pseudonymous (IP still hidden) rather than anonymous. <sup>3</sup> Medium: Tails has a firewall to block non-Tor traffic, but an [https://tails.boum.org/todo/applications_audit/ audit] at protocol level is still required. Quoted from the [https://tails.boum.org/security/index.en.html Tails Security Page]: ''&quot;Until an [https://tails.boum.org/todo/applications_audit/ audit] of the bundled network applications is done, information leakages at the protocol level should be considered as ? at the very least ? possible.&quot;'' <sup>4</sup> Hard: It's left to the user to prevent non-Tor traffic, DNS leaks and protocol level leaks. <sup>5</sup> Text, screenshot or video instructions [https://sourceforge.net/p/whonix/wiki/Download/#install-whonix available]. <sup>6</sup> This and the whole documentation will be improved in next Whonix version. <sup>7</sup> Examples what not to do: [https://sourceforge.net/p/whonix/wiki/DoNot/ DoNot]. </font>

== Features ==

'''Comparing Whonix 0.4.5 with Tails 0.16.'''

<table>
<thead>
<tr class="header">
<th align="left"></th>
<th align="left">Whonix</th>
<th align="left">Tails</th>
<th align="left">Tor Browser Bundle</th>
<th align="left">Qubes OS TorVM</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Default Desktop</td>
<td align="left">KDE</td>
<td align="left">GNOME</td>
<td align="left">?</td>
<td align="left">?</td>
</tr>
<tr class="even">
<td align="left">Multi language support</td>
<td align="left">No</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
<td align="left">?</td>
</tr>
<tr class="odd">
<td align="left">Fits on a DVD.</td>
<td align="left">No</td>
<td align="left">Yes</td>
<td align="left">?</td>
<td align="left">?</td>
</tr>
<tr class="even">
<td align="left">VPN support</td>
<td align="left">Can be manually installed. <sup>1</sup></td>
<td align="left">No <sup>2</sup></td>
<td align="left">?</td>
<td align="left">?</td>
</tr>
<tr class="odd">
<td align="left">IRC client pre-configured for privacy</td>
<td align="left">Yes (XChat)</td>
<td align="left">Yes (Pidgin)</td>
<td align="left">Not an operating system.</td>
<td align="left">No</td>
</tr>
<tr class="even">
<td align="left">Flash Support</td>
<td align="left">Can be manually installed. <sup>3</sup></td>
<td align="left">No <sup>4</sup></td>
</tr>
<tr class="odd">
<td align="left">Mixmaster over Tor</td>
<td align="left">Yes <sup>5</sup></td>
<td align="left">No</td>
<td align="left">Not an operating system.</td>
<td align="left">No.</td>
</tr>
<tr class="even">
<td align="left">TorChat</td>
<td align="left">Can be manually installed. <sup>6</sup></td>
<td align="left">Not supported. <sup>7</sup></td>
<td align="left">Not applicable.</td>
<td align="left">?</td>
</tr>
<tr class="odd">
<td align="left">FTP Support</td>
<td align="left">Partial <sup>8</sup></td>
<td align="left">No? <sup>9</sup></td>
<td align="left">Not an operating system.</td>
<td align="left">?</td>
</tr>
<tr class="even">
<td align="left">Download Manager</td>
<td align="left">Can be manually installed. <sup>10</sup></td>
<td align="left">Can be manually installed. <sup>11</sup></td>
<td align="left">?</td>
<td align="left">?</td>
</tr>
<tr class="odd">
<td align="left">Webmail can be uses in browser</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
</tr>
<tr class="even">
<td align="left">E-Mail Client</td>
<td align="left">Can be manually installed. <sup>14</sup></td>
<td align="left">? <sup>15</sup></td>
<td align="left">?</td>
<td align="left">?</td>
</tr>
<tr class="odd">
<td align="left">Hidden service support</td>
<td align="left">Can be manually installed. <sup>16</sup></td>
<td align="left">Can be manually installed. <sup>17</sup></td>
<td align="left">?</td>
<td align="left">?</td>
</tr>
<tr class="even">
<td align="left">Hidden Server configuration GUI</td>
<td align="left">No</td>
<td align="left">No <sup>13</sup></td>
<td align="left">?</td>
<td align="left">?</td>
</tr>
<tr class="odd">
<td align="left">Support for free wifi hotspots</td>
<td align="left"><sup>18</sup></td>
<td align="left">Yes <sup>19</sup></td>
<td align="left">Yes <sup>20</sup></td>
<td align="left">?</td>
</tr>
<tr class="even">
<td align="left">Works on 32 bit PCs</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
<td align="left">?</td>
</tr>
<tr class="odd">
<td align="left">Works on 64 bit PCs</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
</tr>
<tr class="even">
<td align="left">32 bit builds</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
<td align="left">?</td>
</tr>
<tr class="odd">
<td align="left">64 bit builds</td>
<td align="left">No <sup>21</sup></td>
<td align="left">No</td>
<td align="left">Yes</td>
<td align="left">?</td>
</tr>
<tr class="even">
<td align="left">64 bit builds can be created from source code</td>
<td align="left">Yes <sup>22</sup></td>
<td align="left">?</td>
<td align="left">?</td>
<td align="left">?</td>
</tr>
<tr class="odd">
<td align="left">Host Kernel</td>
<td align="left">When using VMs, can be any supporting Virtual Box.; When using Physical Isolation: Not applicable.</td>
<td align="left">When using VMs, can be any supporting Virtualizer.; When not using VMs: Not applicable.</td>
<td align="left">?</td>
<td align="left">?</td>
</tr>
<tr class="even">
<td align="left">i486 Kernel for compatibility</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
<td align="left">Not an operating system. Up to the user.</td>
<td align="left">?</td>
</tr>
<tr class="odd">
<td align="left">686-pae Kernel</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
<td align="left">Not an operating system. Up to the user.</td>
<td align="left">?</td>
</tr>
<tr class="even">
<td align="left">64 bit Kernel</td>
<td align="left">Could be manually installed.</td>
<td align="left">No.</td>
<td align="left">Not an operating system. Up to the user.</td>
<td align="left">?</td>
</tr>
<tr class="odd">
<td align="left">Kernel Autodetection at Boot Time</td>
<td align="left">No</td>
<td align="left">Yes</td>
<td align="left">Not a distribution. Not applicable.</td>
<td align="left">?</td>
</tr>
<tr class="even">
<td align="left">Video/Streaming Software</td>
<td align="left">Can be manually installed.</td>
<td align="left">Can be manually installed.</td>
<td align="left">Not an operating system.</td>
<td align="left">Can be manually installed.</td>
</tr>
</tbody>
</table>

<font size="-3"> ,, <sup>1</sup> Included, although there is no nice gui, it's available as Optional Configuration, see [https://sourceforge.net/p/whonix/wiki/Features/#vpn-tunnel-support VPN/tunnel support]. <sup>2</sup> Tails Status: https://tails.boum.org/todo/vpn_support/ <sup>3</sup> Done, see [https://sourceforge.net/p/whonix/wiki/BrowserPlugins/ Browser Plugins]. <sup>4</sup> Tails Status: https://tails.boum.org/todo/Flash_support/ <sup>5</sup> Installed by default, see [Mixmaster]. <sup>6</sup> Can be manually installed, see [Chat]. <sup>7</sup> Tails: Not supported. [https://tails.boum.org/todo/Torchat_installed_by_default/ Tails wishlist] <sup>8</sup> [https://trac.torproject.org/projects/tor/ticket/1259#comment:16 wget ftp support broken].; Filezilla (not pre-installed) works. <sup>9</sup> Tails Status: https://tails.boum.org/todo/fix_Internet_FTP_support/ <sup>10</sup> Users can install one of their choice, preferably using SocksPort, TransPort works as well. ''wget -c'' (pre-configured to use SocksPort) is also working. <sup>11</sup> Users can manually install the download manager of their choice in Tails. It just needs to be configured to use the proper SOCKS proxy. <sup>12</sup> Placeholder. <sup>13</sup> [https://tails.boum.org/todo/server_edition/ Tails server: Self-hosted services behind Tails-powered Tor hidden services] <sup>14</sup> Optional configuration, see [https://sourceforge.net/p/whonix/wiki/E-Mail/#mozilla-thunderbird-with-torbirdy Mozilla Thunderbird with TorBirdy]. <sup>15</sup> Tails Status: [https://tails.boum.org/todo/Return_of_Icedove__63__/ Return of Icedove] <sup>16</sup> Hidden services can be used without IP/DNS leaks, see [https://sourceforge.net/p/whonix/wiki/Hidden%20Services/ Hidden Service Support]. There is no nice graphical user interface to setup a hidden service, works well nonetheless. <sup>17</sup> Can be used using ordinary mechanisms with torrc.; Tails Status: [https://tails.boum.org/todo/persistence_preset_-_tor/ persistence preset - tor] <sup>18</sup> When using VMs: Can be easily done on the host.; When using Physical Isolation: As in Whonix 0.5.6 there is no unsafe browser. A separate third machine with clearnet access could be used. <sup>19</sup> Tails has a unsafe browser for such tasks. <sup>20</sup> Mechanism of the host operating system can be used. <sup>21</sup> TODO: Still lacks 64 bit guest builds. 64 bit builds would offer more ALSR entropy, would safe some memory ([https://www.virtualbox.org/manual/ch04.html#guestadd-pagefusion page fusion?]) and provide more performance. <sup>22</sup> Building them from source is already supported, see [http://sourceforge.net/p/whonix/wiki/Dev_SourceCodeIntro/#debugging Build Configuration]. </font>

= Footer =

[[include ref=WikiFooter]]

