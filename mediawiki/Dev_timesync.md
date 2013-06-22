[[include ref=WikiHeader]]

[TOC]

= Introduction =

[https://tails.boum.org/contribute/design/Time_syncing/ tails_htp] has already been copied into Whonix. This file documents the steps done to copy it and implementation differences.

See also [https://sourceforge.net/p/whonix/wiki/Security/#whonixs-secure-and-distributed-time-synchronization-mechanism Whonix's Secure And Distributed Time Synchronization Mechanism].

= Overview =

<table>
<thead>
<tr class="header">
<th align="left"></th>
<th align="left">Tails</th>
<th align="left">Whonix</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">adduser htp</td>
<td align="left">/chroot_local-hooks/06-adduser_htp</td>
<td align="left">Done in [https://github.com/adrelanos/Whonix/blob/master/whonix_workstation/usr/local/bin/whonix_internal_install_script whonix_internal_install_script] (s).</td>
</tr>
<tr class="even">
<td align="left">init script</td>
<td align="left">/etc/init.d/htpdate</td>
<td align="left">[https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/init.d/htpdate /etc/init.d/htpdate] <sup>1</sup></td>
</tr>
<tr class="odd">
<td align="left">tails_htpdate configuration file</td>
<td align="left">/etc/default/htpdate</td>
<td align="left">[https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/default/htpdate /etc/default/htpdate] <sup>6</sup></td>
</tr>
<tr class="even">
<td align="left">tails_htpdate binary</td>
<td align="left">/usr/local/sbin/htpdate</td>
<td align="left">[https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/sbin/htpdate /usr/local/sbin/htpdate] <sup>7</sup></td>
</tr>
<tr class="odd">
<td align="left">anachron script</td>
<td align="left">Not used in Tails.</td>
<td align="left">[https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/cron.hourly/htpdate /etc/cron.hourly/htpdate] <sup>2</sup></td>
</tr>
<tr class="even">
<td align="left">anachron helper delay script</td>
<td align="left">Not used in Tails.</td>
<td align="left">[https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/bin/htpdate_hourly /usr/local/bin/htpdate_hourly] <sup>3</sup></td>
</tr>
<tr class="odd">
<td align="left">timesync gui</td>
<td align="left">Not used in Tails.</td>
<td align="left">[https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/bin/timesync /usr/local/bin/timesync] <sup>4</sup></td>
</tr>
<tr class="even">
<td align="left">/etc/init.d/htpdate sudoers exception</td>
<td align="left">Not used in Tails.</td>
<td align="left">[https://github.com/adrelanos/Whonix/blob/master/whonix_shared/etc/appendto_sudoers /etc/sudoers] <sup>5</sup></td>
</tr>
</tbody>
</table>

Whonix changes:

* <sup>1</sup> Deactivates Virtual Box guest additions time sync; socks proxy IP and port adapted for Whonix.
* <sup>2</sup> Minimal script which simply runs ''/usr/local/bin/htpdate_hourly''. The delay isn't done in this script, since this would make anachron wait until it's done.
* <sup>3</sup> Runs htpdate every hour at a random minute.
* <sup>4</sup> Optional graphical user interface.
* <sup>5</sup> Allows running ''sudo /etc/init.d/htpdate'' without a password.
* <sup>6</sup> See bottom of this page.
* <sup>7</sup> Uses ''/usr/bin/curl'' instead of ''curl'' to circumvent uwt wrapper, because htpdate uses socks settings.

= How tails_htp was initially imported into Whonix =

<pre># Get the Tails signing key:
# https://tails.boum.org/doc/about/openpgp_keys/index.en.html
#
# https://tails.boum.org/contribute/git/
git clone git://git.immerda.ch/amnesia.git
cd amnesia
git tag -v 0.12

# Alternatively it's also possible to download Tail's CD and to unpack it.
# sudo unsquashfs -x -dest /home/user/b filesystem.squashfs</pre>
.

<pre># /amnesia/config/chroot_local-packageslists/tails-common.list contains a list of all Tails dependencies.
# Seach for &quot;needed by htpdate&quot;. You'll see tails_htp depends on the following packages.
libdatetime-perl libdatetime-format-dateparse-perl libgetopt-long-descriptive-perl libtry-tiny-perl</pre>
.

<pre># adduser htp
/home/user/amnesia/config/chroot_local-hooks/06-adduser_htp
# Has been added to whonix_internal_install_script(s).

# We need tails_htpdate, the actual binary.
cp /home/user/amnesia/config/chroot_local-includes/usr/local/sbin/htpdate /home/user/whonix/whonix_shared/usr/bin/htpdate</pre>
.

<pre># Init script.
mkdir -p /home/user/whonix/whonix_shared/etc/init.d/
cp /home/user/amnesia/config/chroot_local-includes/etc/init.d/htpdate /home/user/whonix/whonix_shared/etc/init.d/htpdate
# got added by whonix_internal_install_script: update-rc.d htpdate defaults</pre>
.

<pre># Copy server pool for tails_htp.
cp /home/user/amnesia/config/chroot_local-includes/etc/default/htpdate /home/user/whonix/whonix_shared/etc/default/htpdate</pre>
.

<pre># The server pool /etc/default/htpdate contains a line:
# config/chroot_local-includes/usr/local/bin/getTorbuttonUserAgent
#
# Will not be used in Whonix, since there is also no Ubuntu package with Tor Button.
# Open Tor Browser about:config and search for &quot;useragent_override&quot;, copy the value.
# Manually add to /home/user/whonix/whonix_shared/etc/default/htpdate
# Replace
HTTP_USER_AGENT=&quot;$(/usr/local/bin/getTorbuttonUserAgent)&quot;
# with
#HTTP_USER_AGENT=&quot;$(/usr/local/bin/getTorbuttonUserAgent)&quot;
HTTP_USER_AGENT=&quot;Mozilla/5.0 (Windows NT 6.1; rv:10.0) Gecko/20100101 Firefox/10.0&quot;</pre>
= Long Term Plan =

Rename tails_htp to sdwdate and get it into Debian.

Repository created:

* https://github.com/adrelanos/sdwdate

'''Help welcome!'''

= Footer =

[[include ref=WikiFooter]]

