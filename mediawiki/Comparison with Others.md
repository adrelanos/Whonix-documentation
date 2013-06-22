[[include ref=WikiHeader]]

[TOC]

= Comparison of Whonix, Tails, Tor Browser Bundle and Qubes OS TorVM =

== Introduction ==

Quick comparison of Whonix and Tails key virtues. If ever anything in this table is incorrect/outdated feel free to contact Whonix developers, we'll correct as fast as possible.

'''Last update'''

Comparing:

* Whonix 0.4.5
* Tails 0.16.
* Qubes OS TorVM 0.1.beta1

Legend:

* ? - ''Status currently not researched by adrelanos.'' Help filling the gaps is welcome.

== Different views ==

One has always to be very careful, when talking about others. Especially, when talking about advantages and disadvantages. Different opinions are accepted and listed here.

* [https://mailman.boum.org/pipermail/tails-dev/2012-September/001704.html Tails-dev: please look at Comparison of Whonix, Tails and TBB]
* [https://mailman.boum.org/pipermail/tails-dev/2013-February/002563.html Tails-dev: please look at Comparison of Whonix, Tails and TBB #2]
* [https://groups.google.com/forum/?fromgroups#!topic/qubes-devel/GT8LyE-la-o qubes-devel: please look at Comparison of Whonix, Tails, TBB and Qubes OS TorVM]

== General ==

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
<td align="left">Focus on anonymity, privacy and security</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
</tr>
<tr class="even">
<td align="left">Type</td>
<td align="left">general purpose os available as VM images and physical isolation</td>
<td align="left">Live DVD / Live USB</td>
<td align="left">portable browser</td>
<td align="left">general purpose os, VM plugin for Qubes OS,</td>
</tr>
<tr class="odd">
<td align="left">Supported hardware</td>
<td align="left">x86 compatible and/or Virtual Box + <sup>1</sup></td>
<td align="left">x86 compatible and/or Virtual Machines</td>
<td align="left">Windows, Linux, Mac and Virtual Machines</td>
<td align="left">any capable of running Qubes OS</td>
</tr>
<tr class="even">
<td align="left">Based on</td>
<td align="left">Tor, Debian <sup>2</sup> and a Virtualizer <sup>3</sup> [Virtual Box] when not using Physical Isolation</td>
<td align="left">Tor, Debian</td>
<td align="left">Tor, Firefox</td>
<td align="left">Tor, Qubes OS, Fedora</td>
</tr>
<tr class="odd">
<td align="left">Gateway and torify any operating system (advanced users)</td>
<td align="left">Yes <sup>4</sup></td>
<td align="left">Not a Gateway.</td>
<td align="left">Not a Gateway.</td>
<td align="left">Probable (?) yes, when using [http://wiki.qubes-os.org/trac/wiki/HvmCreate HVM]</td>
</tr>
<tr class="even">
<td align="left">Live DVD</td>
<td align="left">No</td>
<td align="left">Yes</td>
<td align="left">No</td>
<td align="left">No</td>
</tr>
<tr class="odd">
<td align="left">Live USB</td>
<td align="left">No</td>
<td align="left">Yes</td>
<td align="left">No</td>
<td align="left">No</td>
</tr>
<tr class="even">
<td align="left">USB Bootable</td>
<td align="left">Yes <sup>5</sup></td>
<td align="left">Yes</td>
<td align="left">Yes <sup>5</sup></td>
<td align="left">Yes <sup>5</sup></td>
</tr>
<tr class="odd">
<td align="left">USB Installer Feature</td>
<td align="left">No <sup>7</sup></td>
<td align="left">Yes <sup>8</sup></td>
<td align="left">?</td>
<td align="left">?</td>
</tr>
<tr class="even">
<td align="left">Requires Virtual Box</td>
<td align="left">If not using Physical Isolation, yes. <sup>3</sup></td>
<td align="left">No</td>
<td align="left">No</td>
<td align="left">No</td>
</tr>
<tr class="odd">
<td align="left">Requires Qubes OS</td>
<td align="left">No</td>
<td align="left">No</td>
<td align="left">No</td>
<td align="left">Yes</td>
</tr>
<tr class="even">
<td align="left">System requirements</td>
<td align="left">higher</td>
<td align="left">lower</td>
<td align="left">lowest</td>
<td align="left">highest</td>
</tr>
<tr class="odd">
<td align="left">Can run in VM</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
</tr>
<tr class="even">
<td align="left">Persistence</td>
<td align="left">Full</td>
<td align="left">Optional for Live USB</td>
<td align="left">Yes <sup>6</sup></td>
<td align="left">Full (?)</td>
</tr>
<tr class="odd">
<td align="left">Number of developers</td>
<td align="left">one with lots of anonymous contributions</td>
<td align="left">multiple</td>
<td align="left">multiple</td>
<td align="left">One (?)</td>
</tr>
<tr class="even">
<td align="left">Maturity</td>
<td align="left">project since 2012</td>
<td align="left">established, respected project for many years</td>
<td align="left">established, respected project for many years</td>
<td align="left">project since 2012 (?)</td>
</tr>
<tr class="odd">
<td align="left">Open Source</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
</tr>
<tr class="even">
<td align="left">Anonymous Developers</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
<td align="left">No</td>
<td align="left">(?)</td>
</tr>
</tbody>
</table>

<font size="-3"> ,, <sup>1</sup> [https://sourceforge.net/p/whonix/wiki/OtherOperatingSystems Custom-Workstation]: self made builds can run on any real or virtual hardware as long as they are behind a Whonix-Gateway. Tor Browser binaries are only available for a limited amount of platforms (Windows, Linux, BSD, Mac). <sup>2</sup> Whonix-Workstation: also [https://sourceforge.net/p/whonix/wiki/OtherOperatingSystems/ OtherOperatingSystems] are supported.; Whonix-Gateway: In long term we are also agnostic about any other secure distributions. The concept is agnostic, you could use another operating system as base, but it requires effort. <sup>3</sup> Default downloads are for Virtual Box. (Subject for change in future.) [PhysicalIsolation] is an security optional feature for advancend users. Experimental optional support for [VMware]. You can build your own images for other virtualizers, but it requires effort. <sup>4</sup> See [https://sourceforge.net/p/whonix/wiki/OtherOperatingSystems/ OtherOperatingSystems]. <sup>5</sup> You can install your host operating system on USB. <sup>6</sup> You can download files and keep them, save bookmarks and passwords depending on your settings. <sup>7</sup> Whonix has no nice USB installer. Installing operating system on USB is recommend and left to the user. <sup>8</sup> Tails has a nice USB installer. </font>

== Security ==

=== General ===

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
<td align="left">Amnesic</td>
<td align="left">No <sup>6</sup></td>
<td align="left">Yes <sup>7</sup></td>
<td align="left">No <sup>12</sup></td>
<td align="left">No</td>
</tr>
<tr class="even">
<td align="left">Protection against IP/location discovery through root exploits ([https://en.wikipedia.org/wiki/Malware Malware] with root rights) on the Workstation <sup>18</sup>.</td>
<td align="left">Yes <sup>a</sup></td>
<td align="left">No <sup>2</sup></td>
<td align="left">No <sup>2</sup></td>
<td align="left">Yes</td>
</tr>
<tr class="odd">
<td align="left">IP/DNS protocol leak protection</td>
<td align="left">Full <sup>1</sup></td>
<td align="left">Depends <sup>5</sup></td>
<td align="left">Depends <sup>5</sup></td>
<td align="left">Full</td>
</tr>
<tr class="even">
<td align="left">Takes advantage of Entry Guards</td>
<td align="left">Yes</td>
<td align="left">No</td>
<td align="left">Yes</td>
<td align="left">Yes (?)</td>
</tr>
<tr class="odd">
<td align="left">Operating System Updates</td>
<td align="left">persist once updated</td>
<td align="left">are lost after reboot</td>
<td align="left">persist once updated</td>
<td align="left">persist once updated (?)</td>
</tr>
<tr class="even">
<td align="left">Hides hardware serials from malicious software</td>
<td align="left">Yes <sup>16</sup></td>
<td align="left">No <sup>17</sup></td>
<td align="left">No <sup>17</sup></td>
<td align="left">(?)</td>
</tr>
<tr class="odd">
<td align="left">Collects hardware serials</td>
<td align="left">No</td>
<td align="left">No</td>
<td align="left">No</td>
<td align="left">No</td>
</tr>
<tr class="even">
<td align="left">Includes Tor Browser</td>
<td align="left">Yes</td>
<td align="left">No</td>
<td align="left">Yes</td>
<td align="left">No</td>
</tr>
<tr class="odd">
<td align="left">Stream isolation to prevent identity correlation through circuit sharing</td>
<td align="left">Yes</td>
<td align="left">Yes <sup>13</sup></td>
<td align="left">See <sup>14</sup> <sup>15</sup></td>
<td align="left">Manually (?)</td>
</tr>
<tr class="even">
<td align="left">Stream isolates Tor Browser</td>
<td align="left">No <sup>14</sup></td>
<td align="left">No <sup>14</sup></td>
<td align="left">No <sup>14</sup></td>
<td align="left">No <sup>14</sup></td>
</tr>
<tr class="odd">
<td align="left">Encryption</td>
<td align="left">Should be applied on host.</td>
<td align="left">Yes, for persistent USB.</td>
<td align="left">Should be applied on host.</td>
<td align="left">Should be applied on host.</td>
</tr>
<tr class="even">
<td align="left">Cold Boot Attack Protection <sup>8</sup></td>
<td align="left">No, planed.</td>
<td align="left">Yes</td>
<td align="left">No</td>
<td align="left">No (?)</td>
</tr>
<tr class="odd">
<td align="left">Secure Distributed Network Time Synchronization</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
<td align="left">No</td>
<td align="left">No</td>
</tr>
<tr class="even">
<td align="left">Hides your time zone (set to UTC)</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
</tr>
<tr class="odd">
<td align="left">Hides your operating system account name</td>
<td align="left">Yes, set to user.</td>
<td align="left">Yes, set to amnesia.</td>
<td align="left">No</td>
<td align="left">Yes</td>
</tr>
<tr class="even">
<td align="left">Hides your MAC address from websites</td>
<td align="left">Invalid <sup>19</sup></td>
<td align="left">Invalid <sup>19</sup></td>
<td align="left">Invalid <sup>19</sup></td>
<td align="left">Invalid <sup>19</sup></td>
</tr>
<tr class="odd">
<td align="left">Secures your MAC address from local LAN (sometimes ISP) <sup>20</sup></td>
<td align="left">No, planed, see. <sup>21</sup></td>
<td align="left">No, planed. <sup>22</sup></td>
<td align="left">No</td>
<td align="left">(?)</td>
</tr>
<tr class="even">
<td align="left">Hides your MAC address from applications</td>
<td align="left">Yes <sup>24</sup></td>
<td align="left">No</td>
<td align="left">No</td>
<td align="left">(?)</td>
</tr>
<tr class="odd">
<td align="left">Secure gpg.conf</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
<td align="left">Not an operating system.</td>
<td align="left">No</td>
</tr>
<tr class="even">
<td align="left">Privacy enhanced IRC client configuration.</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
<td align="left">Not an IRC client.</td>
<td align="left">No</td>
</tr>
</tbody>
</table>

<font size="-3"> ,, <sup>a</sup> Whonix has Protection against IP/location discovery through root exploits ([https://en.wikipedia.org/wiki/Malware Malware] with root rights) inside Whonix-Workstation. But you really should not test it. In case Whonix-Workstation gets rooted, the adversary can not find out the users real IP/location. This is because Whonix-Workstation can only connect through the Whonix-Gateway. How difficult is it to compromise Whonix? See [https://sourceforge.net/p/whonix/wiki/Comparison%20with%20Others/#attacks Attack on Whonix] and [Design]. More skill is required. <sup>1</sup> Such kinds of leaks are impossible <sup>a</sup> in Whonix, since the Whonix-Workstation is unaware of it's external IP. <sup>2</sup> In case Tails or TBB gets rooted, the adversary can simply bypass the firewall and get the user's real IP. <sup>5</sup> See first example of [https://sourceforge.net/p/whonix/wiki/Security%20in%20Real%20World/ Whonix security in real world]. When applications in Tails are configured wrong, due to a bug in Tails or the application, IP can leak. Quoted from the [https://tails.boum.org/security/index.en.html Tails Security Page]: ''&quot;Until an [https://tails.boum.org/todo/applications_audit/ audit] of the bundled network applications is done, information leakages at the protocol level should be considered as - at the very least - possible.&quot;'' <sup>6</sup> There are no special measures to limit what is written to disk. This includes (non exclusive list) user created files, backup files, temporary files, swap, chat history, browser history and so on. Whonix acts like an ordinary installed operating system. It can also not be prevented, that the host memory [https://en.wikipedia.org/wiki/Swap swaps] to the host disk. There is a [https://sourceforge.net/p/whonix/wiki/Security%20Guide/#recommendation-to-use-multiple-vm-snapshots Recommendation to use multiple VM Snapshots] and it is is [https://sourceforge.net/p/whonix/wiki/Advanced%20Security%20Guide/#full-disk-encryption recommend] to apply Full Disk Encryption on the host. This is the price, Whonix has to pay, because many features could be more easily added to Whonix by adrelanos or can be easily installed by the user. <sup>7</sup> Done by design. <sup>8</sup> See [https://en.wikipedia.org/wiki/Cold_boot_attack Cold boot attack]. <sup>12</sup> Although it does not try to store to disk, swap can still leak. <sup>13</sup> [https://tails.boum.org/todo/separate_Tor_streams/ Tails separate Tor streams] <sup>14</sup> [https://trac.torproject.org/projects/tor/ticket/3455 Tor Browser should set SOCKS username for a request based on referer] <sup>15</sup> Tor Browser comes with it's own Tor instance. It's just a browser, not a live system or operating system. <sup>16</sup> See [https://sourceforge.net/p/whonix/wiki/Whonix%27s%20Protocol-Leak-Protection%20and%20Fingerprinting-Protection/ Whonix's Protocol-Leak-Protection and Fingerprinting-Protection] for details. <sup>17</sup> By default there get of course not send to anyone. This is only at risk in case the machine gets compromised by malware. See also, [https://tails.boum.org/forum/Are_hardware_serial_numbers_hidden_in_TAILS__63__/ Are hardware serial numbers hidden in TAILS?]. <sup>18</sup> The Workstation is the place where the browser, IRC client and so on is running. The Gateway is the place where Tor and the firewall is running. <sup>19</sup> It is in the nature of the MAC addresses, that destination servers can not see them. Therefore yes, always hidden from destination servers. <sup>20</sup> Most ISPs do not see the MAC addresses of their clients. Some ISPs are based on LANs, in that case they can see the MAC address. Also hotspots can see the MAC address. <sup>21</sup> Please read [https://sourceforge.net/p/whonix/wiki/Whonix%20in%20public%20networks%20-%20MAC%20Address/ Whonix in public networks / MAC Address]. <sup>22</sup> [https://tails.boum.org/todo/macchanger/ Tails Todo: machanger] <sup>23</sup> Placeholder. <sup>24</sup> The virtual MAC address of Whonix-Workstation and Whonix-Gateway <sup>25</sup> is shared among all Whonix users. If any (malicious) applications would spill it <sup>26</sup>, it would only be known that it's from a Whonix user. <sup>25</sup> The virtual MAC address for Whonix-Gateway's internal network interface (eth1) is shared among all Whonix users, because Whonix-Workstation can see it. However, Whonix-Workstation can not see Whonix-Gateway's external network cards (eth0) MAC address. <sup>26</sup> Which they usually won't do. Sometimes anti cheat or copyright protection tools do it. </font>

=== Fingerprint ===

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
<td align="left">Network/Web Fingerprint</td>
<td align="left">[https://sourceforge.net/p/whonix/wiki/Fingerprint/ Whonix Fingerprint Page]</td>
<td align="left">[https://tails.boum.org/doc/about/fingerprint/index.en.html Tails Fingerprint Page]</td>
<td align="left">TBB traffic is tunneled through Tor. Host traffic passes clearnet.</td>
<td align="left">-</td>
</tr>
<tr class="even">
<td align="left">Network fingerprint: ISP can trivially guess project type <sup>27</sup></td>
<td align="left">No.</td>
<td align="left">No.</td>
<td align="left">No.</td>
<td align="left">(?)</td>
</tr>
<tr class="odd">
<td align="left">Network fingerprint: ISP can guess a non-persistent Tor directory is being used</td>
<td align="left">No.</td>
<td align="left">Yes, because [https://tails.boum.org/todo/persistence_preset_-_tor/ not yet] supporting persistent entry guards.</td>
<td align="left">No.</td>
<td align="left">(?)</td>
</tr>
<tr class="even">
<td align="left">Clearnet traffic</td>
<td align="left">All Whonix-Gateway and Whonix-Workstation traffic is tunneled through Tor. Host traffic (operating system updates, eventually host browser etc.) uses clearnet.</td>
<td align="left">None, unless other users sharing the same internet connection are not using Tails.</td>
<td align="left">TBB traffic is tunneled through Tor. Host traffic (operating system updates, eventually untorified second browser etc.) uses clearnet.</td>
<td align="left">Yes, Gateway is not torified.</td>
</tr>
<tr class="odd">
<td align="left">Network fingerprint: ISP can guess which anonymity software is being used because of ratio of Tor and clearnet traffic</td>
<td align="left">Unknown. <sup>33</sup></td>
<td align="left">Can guess a Tor Live DVD is being used, unless Unsafe Browser is in use or other people sharing same internet connections not using Tails.</td>
<td align="left">?</td>
<td align="left">(?)</td>
</tr>
<tr class="even">
<td align="left">Network fingerprint: ISP can guess which anonymity software is being used because of [https://tails.boum.org/contribute/design/Time_syncing/ tordate] <sup>34</sup></td>
<td align="left">No, does not include tordate.</td>
<td align="left">Yes, if clock is too much off when booting. <sup>34</sup></td>
<td align="left">No, not an operating system.</td>
<td align="left">No, does not include tordate.</td>
</tr>
<tr class="odd">
<td align="left">Web fingerprint <sup>28</sup></td>
<td align="left">Same as TBB. <sup>29</sup></td>
<td align="left">See footnote <sup>30</sup> for latest status.</td>
<td align="left">TBB. <sup>31</sup></td>
<td align="left">Does not include Tor Browser.</td>
</tr>
<tr class="even">
<td align="left">Unsafe browser fingerprint <sup>35</sup></td>
<td align="left"><sup>36</sup></td>
<td align="left"><sup>37</sup></td>
<td align="left">?</td>
<td align="left">?</td>
</tr>
</tbody>
</table>

<font size="-3"> <sup>27</sup> Find out if Whonix, Tails or TBB is running. <sup>28</sup> Fingerprint for the websites that you are visiting <sup>29</sup> Uses the original Tor Browser from torproject.org with the only difference, that Tor runs on Whonix-Gateway instead the locally shipped Tor. <sup>30</sup> See documentation [https://tails.boum.org/doc/about/fingerprint/index.en.html For the websites that you are visiting] and todo [https://tails.boum.org/todo/evaluate_web_fingerprint/ evaluate web fingerprint] for latest status. <sup>31</sup> Is the original Tor Browser Bundle from torproject.org. <sup>32</sup> Live DVD without persistent USB storage for the Tor data directory.^^ <sup>33</sup> Whonix users might tend to have more traffic than TBB users, due to operating system updates of Whonix-Workstation and Whonix-Gateway through Tor. Unknown if this is specific enough to guess a transparent or isolating proxy is being used or if enough other Tor users run big enough amounts of traffic through Tor. Research before Whonix was created has shown that big amounts of filesharing traffic were run through Tor. Classical filesharing tends to have more upload than Whonix, but it's also unknown how many people disabled upload or moved to methods which do not involve much upload, such as file hosters. <sup>34</sup> Quoted from the [https://tails.boum.org/contribute/design/Time_syncing/#index5h1 Tails Design about Time syncing]: &quot;''Our initial time guess based on the Tor consensus is probably easier to fingerprint, though: a fresh Tor is started, and restarted again right after the consensus has been downloaded.''&quot; <sup>35</sup> Unsafe Browser: Tails and Liberte Linux contain a so called Unsafe Browser. The Unsafe Browser does not use Tor. Connects in the clear. It is useful to register on hotspots or to view content in the clear without Tor. <sup>37</sup> When using VMs: The unsafe browser on the host is untouched. It does not get any better or worse by installing Whonix.; When using Physical Isolation: As in Whonix 0.5.6 there is no unsafe browser. A separate third machine with clearnet access could be used. <sup>38</sup> Tails Todo: https://tails.boum.org/todo/improve_fingerprint_of_the_Unsafe_Browser/ </font>

=== Flash / Browser Plugin security ===

'''Note''': Whonix developer adrelanos recommend due to anonymity, privacy and security issues against using Adobe Flash when anonymity is the goal. As far I know, Tails and Tor developers recommend against it as well.

<table>
<thead>
<tr class="header">
<th align="left">Flash Tracking Technique</th>
<th align="left">Whonix-Workstation</th>
<th align="left">Tor on host</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Proxy bypass IP leak</td>
<td align="left">Protected.</td>
<td align="left">Insecure, leads to deanonymization.</td>
</tr>
<tr class="even">
<td align="left">Protocol IP leak</td>
<td align="left">Protected.</td>
<td align="left">Insecure, leads to deanonymization.</td>
</tr>
<tr class="odd">
<td align="left">Flash Cookies</td>
<td align="left">Reduce anonymity to pseudonymity. Recommend to delete Flash Cookies.</td>
<td align="left">Can link your clearnet Flash activity to your Flash activity over Tor, which leads to deanonymization (or at least a good guess) if the skew is big and rare. Also useful for fingerprinting, which is bad. <sup>1</sup></td>
</tr>
<tr class="even">
<td align="left">Number of installed fonts.</td>
<td align="left">The number of fonts inside Whonix-Workstation and your clearnet/host operating system will differ, which is good.</td>
<td align="left">Same fonts are reported for your clearnet and your Tor Flash activity, which is bad. <sup>1</sup></td>
</tr>
<tr class="odd">
<td align="left">Exact flash player version.</td>
<td align="left">Shared among all up to date Debian users. Not very useful for fingerprinting. Probable different from your clearnet/host operating system, which is good.</td>
<td align="left">Same version is reported for your clearnet and for your Flash activity over Tor, which is bad. <sup>1</sup></td>
</tr>
<tr class="even">
<td align="left">GNU/Linux Kernel version.</td>
<td align="left">Shared among all up to date Debian users. Not very useful for fingerprinting.</td>
<td align="left">Same version is reported for your clearnet and for your Flash activity over Tor. <sup>1</sup></td>
</tr>
<tr class="odd">
<td align="left">Language.</td>
<td align="left">Set to en_US for all Whonix users.</td>
<td align="left">Your local language setting. Useful for fingerprinting and anonymity set reduction, which is bad. <sup>1</sup></td>
</tr>
<tr class="even">
<td align="left">Exact date and time.</td>
<td align="left">Differs from your clearnet/host operating system, which is good. (See [https://sourceforge.net/p/whonix/wiki/TimeSync/ Whonix's Secure And Distributed Time Synchronization Mechanism] for details.)</td>
<td align="left">Same time/clockskew is reported for your clearnet and your Tor Flash activity, which is bad. <sup>1</sup></td>
</tr>
<tr class="odd">
<td align="left">Exact screen resolution and DPI.</td>
<td align="left">Shared among all Whonix users. (See [https://sourceforge.net/p/whonix/wiki/Whonix%27s%20Protocol-Leak-Protection%20and%20Fingerprinting-Protection/ Whonix's Protocol-Leak-Protection and Fingerprinting-Protection] for details.) Even if you changed it, the screen resolution and DPI it will differ from your clearnet/host operating system.</td>
<td align="left">Same screen resolution and DPI is reported for your clearnet and Tor use, which is bad. <sup>1</sup></td>
</tr>
<tr class="even">
<td align="left">Full path to your flash plugin.</td>
<td align="left">Shared among all Debian users.</td>
<td align="left">Depends on your clearnet/host operating system. In worst case it could contain your operating system user name, which is even worse if that is your real name. Same path to your flash plugin is reported for your clearnet and Tor use, which is bad. <sup>1</sup></td>
</tr>
<tr class="odd">
<td align="left">Anything else. <font size="-3">(You can check that yourself offsite on https://ip-check.info.)</font></td>
<td align="left">Assume reduction from anonymity to pseudonymity.</td>
<td align="left">Even more possibilties for fingerprinting and linking, which is bad. <sup>1</sup></td>
</tr>
<tr class="even">
<td align="left">Conclusion</td>
<td align="left">IP/location/identity will still be hidden inside Whonix-Workstation. Assume it to be [https://sourceforge.net/p/whonix/wiki/DoNot/#do-not-confuse-anonymity-with-pseudonymity pseudonymous rather than anonymous].</td>
<td align="left">Flash over Tor (on the host, without something like Whonix) is totally unsafe. In case you also ever use(ed) Flash over clearnet, linkability is possible. Assume the Flash fingerprint to be that strong, that your clearnet and your Tor Flash activity can be linked together, which leads to deanonymization.</td>
</tr>
</tbody>
</table>

<sup>1</sup> Which is bad, because it could be used for fingerprinting, linking and also deanonymization (or at least a good guess) if the fingerprint is detailed enough.

For more information about Flash and Browser Plugins in Whonix, see also [https://sourceforge.net/p/whonix/wiki/BrowserPlugins/ Browser Plugins].

== Attacks ==

=== Circumventing Proxy Obedience Design ===

Knowledge assumed:

* [https://sourceforge.net/p/whonix/wiki/Comparison%20of%20different%20Whonix%20variants/ Comparison of different Whonix variants].
* Unsafe Browser: Tails and Liberte Linux contain a so called Unsafe Browser. The Unsafe Browser does not use Tor. Connects in the clear. It is useful to register on hotspots or to view content in the clear without Tor.
* Exploit against physically isolated Whonix-Gateway: difficult against a bare metal physical isolated Whonix-Gateway. This is because Whonix-Workstation can only access Tor running on Whonix-Gateway. We minimized attack surface, hardening etc. See the whole Security and Hardening page for details.
* TBB stands for Tor Browser Bundle.
* In the following table,
** &quot;fail&quot; is defined as &quot;IP/location of user is compromised.&quot;.
** &quot;safe&quot; is defined as &quot;IP/location of user is hidden behind Tor.&quot;.
* The numbers (1) to (10) are used to numerate various attacks. Those attacks are described in more details below.

Whonix protects against IP/location discovery through root exploits ([https://en.wikipedia.org/wiki/Malware Malware] with root rights) on the Workstation<sup>1</sup>. This does not mean, risk to get infected with malware. Do not! It would still make all data inside Whonix-Workstation available to the attacker. Like said at other places as well, Whonix is not a perfect system. It can not be. Whonix is not unbreakable. What Whonix does, it higher the effort for an attacker to find out the user's real IP address, thus de-anonymizing the user. The following table shall visualize the various defense layers provided by Whonix.

<font size="-3"> ,, <sup>1</sup> The Workstation is the place where the browser, IRC client and so on is running. The Gateway is the place where Tor and the firewall is running. </font>

<table>
<thead>
<tr class="header">
<th align="left">attack</th>
<th align="left">Whonix Standard Download version host+vm+vm</th>
<th align="left">Whonix Physical Isolation</th>
<th align="left">Tails</th>
<th align="left">Tails in a VM</th>
<th align="left">TBB</th>
<th align="left">TBB in a VM</th>
<th align="left">Qubes OS TorVM</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">(1) Proxy Bypass IP leak</td>
<td align="left">safe <sup>5</sup></td>
<td align="left">safe <sup>5</sup></td>
<td align="left">safe <sup>5</sup></td>
<td align="left">safe <sup>5</sup></td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">safe</td>
</tr>
<tr class="even">
<td align="left">(2) Protocol IP leak</td>
<td align="left">safe <sup>4</sup></td>
<td align="left">safe <sup>4</sup></td>
<td align="left">fail</td>
<td align="left">safe <sup>6</sup></td>
<td align="left">fail</td>
<td align="left">safe <sup>6</sup></td>
<td align="left">safe</td>
</tr>
<tr class="odd">
<td align="left">(3) exploit + Unsafe Browser</td>
<td align="left">safe</td>
<td align="left">safe</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">safe</td>
</tr>
<tr class="even">
<td align="left">(4) exploit + root exploit + Unsafe Browser</td>
<td align="left">safe</td>
<td align="left">safe</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">safe</td>
</tr>
<tr class="odd">
<td align="left">(5) root exploit + Unsafe Browser</td>
<td align="left">safe</td>
<td align="left">safe</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">safe</td>
</tr>
<tr class="even">
<td align="left">(6) exploit + vm exploit + Unsafe Browser</td>
<td align="left">fail</td>
<td align="left">safe</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
</tr>
<tr class="odd">
<td align="left">(7) exploit + vm exploit + exploit against physically isolated Whonix-Gateway</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
</tr>
<tr class="even">
<td align="left">(8) vm exploit</td>
<td align="left">fail</td>
<td align="left">safe</td>
<td align="left">safe</td>
<td align="left">fail</td>
<td align="left">safe</td>
<td align="left">fail</td>
<td align="left">fail</td>
</tr>
<tr class="odd">
<td align="left">(9) vm exploit + exploit against physically isolated Whonix-Gateway</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">safe</td>
<td align="left">fail <sup>7</sup> <sup>8</sup></td>
<td align="left">safe</td>
<td align="left">fail <sup>7</sup> <sup>8</sup></td>
<td align="left">fail <sup>7</sup> <sup>8</sup></td>
</tr>
<tr class="even">
<td align="left">(10) exploit against Tor process</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
</tr>
<tr class="odd">
<td align="left">(11) attack against the Tor network</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
</tr>
</tbody>
</table>

# An application doesn't honor proxy settings. Example: [https://blog.torproject.org/blog/firefox-security-bug-proxy-bypass-current-tbbs Tor Browser Bundle: Firefox security bug (proxy-bypass)].
# For example proxy bypass bugs, where the application spills the users real IP. See [https://sourceforge.net/p/whonix/wiki/Security%20in%20Real%20World/ Whonix security in real world], for examples where Whonix circumvented them. It gets circumvented by Whonix because Whonix-Workstation does not know the users real IP address.
# Example: user visits a website over Tor with a torified Browser. The website uses known or zero day vulnerability to gain remote code execution on the users machine. Remote cod execution is used to install malware on the users machine. The used vulnerability allows the adversary to get &quot;only&quot; user rights, not root. The adversary could remotely start the Unsafe Browser and therefore find out the users real IP address. This attack gets circumvented by Whonix, because any applications inside Whonix, including malware, can only connect through Tor.
# Example: user visits a website over Tor with a torified Browser. The website uses known or zero day vulnerability to gain remote code execution on the users machine. Remote cod execution is used to install malware on the users machine. The used vulnerability allows the adversary to get &quot;only&quot; user rights, not root. The adversary gains root through escalate privileges using a second vulnerability. This allows the adversary to tamper with iptables rules, to make non-Tor connections and so on. This attack gets circumvented by Whonix, because Whonix's Firewall runs on another (virtual) machine. This attack gets circumvented by Whonix, because any root applications inside Whonix, including malware with root rights, can only connect through Tor.
# Example: user visits a website over Tor with a torified Browser. The website uses known or zero day vulnerability to gain remote code execution on the users machine. Remote cod execution is used to install malware on the users machine. The used vulnerability allows the adversary to get root rights. This allows the adversary to tamper with iptables rules, to make non-Tor connections and so on. This attack gets circumvented by Whonix, because Whonix's Firewall runs on another (virtual) machine. This attack gets circumvented by Whonix, because any root applications inside Whonix, including malware with root rights, can only connect through Tor.
# Example: user visits a website over Tor with a torified Browser. The website uses known or zero day vulnerability to gain remote code execution on the users machine. Remote cod execution is used to install malware on the users machine. A second exploit is being used to break out of the Virtual Machine. Whonix Standard Download version host+vm+vm is broken against this attack. Whonix Physical Isolation defeats this attack, because the Whonix-Workstation's host does not know it's real IP address, only Whonix-Gateway, running on an other physical machine knows it.
# Same as attack (5). But the adversary uses an extra vulnerability to break into Whonix-Gateway. Whonix is broken against this attack.
# Example: user visits a website over Tor with a torified Browser. The website uses known or zero day vulnerability to gain remote code execution on the host. Whonix Standard Download version host+vm+vm: fail, same as attack (5). Physical Isolation defeats this attack, same as attack (5).
# Example: user visits a website over Tor with a torified Browser. The website uses known or zero day vulnerability to gain remote code execution on the host. The adversary uses an extra vulnerability to break Whonix-Gateway. Whonix is broken against this attack.
# Example: user visits a website over Tor with a torified Browser. Tor processes the traffic. The adversary uses a vulnerability to gain remote code execution. The machine were Tor is running always <sup>2</sup> knows the users real IP address. Whonix is broken against this attack.
# Example: end to end correlation attack, but there are much more attacks where Tor is known to be broken against. Any successful attack against Tor on a Tor based anonymity operating system will naturally deanonymize the user. <sup>2</sup> <sup>3</sup>

<font size="-3"> ,, <sup>1</sup> Placeholder. <sup>2</sup> Unless you are using Multiple Gateways. (Optional Whonix feature in progress.) <sup>3</sup> Whonix defeats some attacks against Tor (and components such as Tor Browser), for example, see [https://sourceforge.net/p/whonix/wiki/TimeSync/ Whonix's Secure And Distributed Time Synchronization Mechanism] and [https://sourceforge.net/p/whonix/wiki/Whonix%27s%20Protocol-Leak-Protection%20and%20Fingerprinting-Protection/ Whonix's Protocol-Leak-Protection and Fingerprinting-Protection] and the rest of the Security and Hardening page. <sup>4</sup> Workstation doesn't know it's own external IP address. <sup>5</sup> Prevented by firewall. <sup>6</sup> VM replaces the IP with an internal LAN IP, which is safe. <sup>7</sup> Fail, because it already failed against a VM exploit. <sup>8</sup> Usually not run behind a physically isolated Whonix-Gateway. </font>

=== Network Time related ===

Knowledge assumed:

* [https://tails.boum.org/contribute/design/Time_syncing/ Tails Design: Time synching]
* [https://sourceforge.net/p/whonix/wiki/TimeSync/ Whonix Design: TimeSync]
* In the following table,
** &quot;(VM host) update/crypto block&quot; is defined as: Can prevent (VM host) operating system updates and cryptographic verification such as for SSL verification in (VM host) browser.
** &quot;u/c-block&quot; is defined as: update/crypto block
** &quot;Tor blocked&quot; is defined as: Can prevent connections to the Tor network until clock gets manually fixed.
** &quot;big clock skew&quot; is defined as: more than 1 hour in past or more than 3 hour in future. <sup>13</sup>
** &quot;small clock skew&quot; is defined as: less then 1 hour in past or less than 3 hour in future. <sup>13</sup>

<table>
<thead>
<tr class="header">
<th align="left">_</th>
<th align="left">Whonix Standard Download version host+vm+vm</th>
<th align="left">Whonix Physical Isolation</th>
<th align="left">Tails</th>
<th align="left">Tails in a VM</th>
<th align="left">TBB</th>
<th align="left">TBB in a VM</th>
<th align="left">Qubes OS TorVM</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Info: VM host time synchronization mechanism</td>
<td align="left">NTP</td>
<td align="left">Gateway: There is no VM host.; Workstation host: NTP</td>
<td align="left">There is no VM host. Same as operating system synchronization mechanism</td>
<td align="left">NTP</td>
<td align="left">There is no VM host.</td>
<td align="left">NTP</td>
<td align="left">NTP</td>
</tr>
<tr class="even">
<td align="left">Info: operating system synchronization mechanism</td>
<td align="left">tails_htp</td>
<td align="left">tails_htp</td>
<td align="left">tordate and tails_htp</td>
<td align="left">tordate and tails_htp</td>
<td align="left">NTP</td>
<td align="left">NTP</td>
<td align="left">(?)</td>
</tr>
<tr class="odd">
<td align="left">if clock is too much off</td>
<td align="left">Tor blocked</td>
<td align="left">Tor blocked</td>
<td align="left">tordate will fix it.</td>
<td align="left">tordate will fix it.</td>
<td align="left">Tor blocked</td>
<td align="left">Tor blocked</td>
<td align="left">Tor blocked</td>
</tr>
<tr class="even">
<td align="left">VM host time differs from operating system time</td>
<td align="left">Yes, <sup>2</sup></td>
<td align="left">Yes, <sup>2</sup></td>
<td align="left">There is no VM host.</td>
<td align="left">Yes. <sup>11</sup></td>
<td align="left">No. <sup>5</sup></td>
<td align="left">Maybe. <sup>6</sup></td>
<td align="left">No</td>
</tr>
<tr class="odd">
<td align="left">unsafe browser time differs from torified browser time. <sup>1</sup></td>
<td align="left">Yes. <sup>2</sup></td>
<td align="left">Yes. <sup>3</sup></td>
<td align="left">No. <sup>10</sup></td>
<td align="left">No. <sup>10</sup></td>
<td align="left">No. <sup>5</sup></td>
<td align="left">Maybe. <sup>6</sup></td>
<td align="left">No</td>
</tr>
<tr class="even">
<td align="left">big clock skew attack against NTP <sup>8</sup>: VM host effects</td>
<td align="left">u/c-block</td>
<td align="left">VM host u/c-block</td>
<td align="left">There is no VM host.</td>
<td align="left">VM host u/c-block</td>
<td align="left">There is no VM host.</td>
<td align="left">VM host u/c-block</td>
<td align="left">u/c-block</td>
</tr>
<tr class="odd">
<td align="left">big clock skew attack against NTP <sup>8</sup>: operating system effects</td>
<td align="left">Tor blocked</td>
<td align="left">Tor blocked</td>
<td align="left"><sup>7</sup>; tordate will fix it.</td>
<td align="left"><sup>7</sup>; tordate will fix it.</td>
<td align="left">Tor blocked; u/c block</td>
<td align="left">Tor blocked; u/c block</td>
<td align="left">Tor blocked</td>
</tr>
<tr class="even">
<td align="left">Fingerprintable reaction <sup>12</sup> when big clock skew attack was used</td>
<td align="left">No, fails the same way TBB fails.</td>
<td align="left">No, fails the same way TBB fails.</td>
<td align="left">Probable yes, see Fingerprint section above.</td>
<td align="left">Probable yes, see Fingerprint section above.</td>
<td align="left">TBB</td>
<td align="left">TBB</td>
<td align="left">No</td>
</tr>
<tr class="odd">
<td align="left">small clock skew attack against NTP <sup>8</sup>, VM host effects:</td>
<td align="left">VM host u/c block</td>
<td align="left">VM host u/c block</td>
<td align="left">There is no VM host.</td>
<td align="left">VM host u/c block</td>
<td align="left">VM host u/c block</td>
<td align="left">VM host u/c block</td>
<td align="left">VM host u/c block</td>
</tr>
<tr class="even">
<td align="left">small clock skew attack against NTP <sup>8</sup>, operating system effects:</td>
<td align="left">Whonix VMs: tails_htp will fix it.</td>
<td align="left">tails_htp will fix it.</td>
<td align="left">VM: tails_htp will fix it.</td>
<td align="left">tails_htp will fix it.</td>
<td align="left">If users visits a page which is under observation by the adversary, the adversary knows who is connecting. <sup>9</sup></td>
<td align="left">If users visits a page which is under observation by the adversary, the adversary knows who is connecting. <sup>9</sup></td>
<td align="left">If users visits a page which is under observation by the adversary, the adversary knows who is connecting. <sup>9</sup></td>
</tr>
</tbody>
</table>

<font size="-3"> ,, <sup>1</sup> This is important because otherwise non-anonymous activity could be linked to anonymous activity if the clock skew is too big and/or too unique. <sup>2</sup> Because unsafe browser runs on the VM host (NTP) and torified browser runs inside Whonix-Workstation. (tails_htp) <sup>3</sup> Whonix-Workstation (tails_htp) and Whonix-Gateway (separate tails_htp) time differ. <sup>4</sup> VM host time gets synchronized with NTP and VM time gets synchronized with tails_htp. <sup>5</sup> Untorified host browser uses the same clock as TBB. <sup>6</sup> Host and VM clock both get synchronized with NTP, but it could still make a difference, because they are synchronized independently. <sup>7</sup> Assumed an installed regular operating system using NTP was used earlier and the adversary introduced a clock skew. <sup>8</sup> Introduced by ISP level adversary attack. <sup>9</sup> Due to unique clock skew. <sup>10</sup> Unsafe browser and torified browser share the same clock. (tails_htp) <sup>11</sup> VM Host time gets synchronized with NTP and operating system time gets synchronized with tails_htp. <sup>12</sup> Such as running tordate. <sup>13</sup> [https://lists.torproject.org/pipermail/tor-talk/2012-February/023264.html source of information] </font>

== Usability ==

Due to a [https://sourceforge.net/p/allura/tickets/6207/ bug] on sourceforge.net, this table has its own page: [Comparison with Others2].

== Features ==

Due to a [https://sourceforge.net/p/allura/tickets/6207/ bug] on sourceforge.net, this table has its own page: [Comparison with Others2].

== Conclusion ==

Conclusion: different threat model, different implementation, different use cases, although some overlap. Different political and design decisions.

== Part 2 ==

[https://sourceforge.net/p/whonix/wiki/ComparisonOfTorProxiesCGIproxiesProxyChainsAndVPNServices/ Comparison Of Tor, Proxies, CGI proxies, Proxy Chains and VPN Services]

= Footer =

[[include ref=WikiFooter]]

