[[include ref=WikiHeader]]

[TOC]

= About this page =

'''This is outdated documentation which no longer applies. Kept in case it it will be required again in future.'''

= Updating Tor =

Tor was installed on Whonix according to [https://www.torproject.org/docs/debian#ubuntu official instructions for Ubuntu]. You can update Tor (and the rest of the system) using ''apt-get update'' and ''apt-get dist-upgrade''.

If you run in the following error message when running ''apt-get update'' on the Gateway...

<pre>W: GPG error: http://deb.torproject.org precise Inrelease: The following signature were invalid: Keyexpired 1346668560</pre>
...or into the following error message on the Gateway when running ''apt-get dist-upgrade'':

<pre>Warning: The following packages cannot be authenticated!
deb.torproject.org-keyring tor
Install these packages without varification?</pre>
...please use the workaround below. Please do not install without verification for your own safety!

Temporary fix. Run these two commands. (Check if they are still current and genuine in official instructions for Ubuntu.)

<pre>gpg --keyserver keys.gnupg.net --recv 886DDD89

gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | sudo apt-key add -</pre>
(If they fail for the first time, perhaps because you are on a slow network or slow Tor circuit, run them a few times until the succeed.)

,, Technical problem: The latest Whonix release is a few days ago and in meanwhile there is a new deb.torproject.org-keyring got renewed while the old torproject deb keys expired. Fixing the problem requires a new Whonix release. It will be fixed in 0.3.0.

= VirtualBox Guest Additions =

== Introduction ==

Written and tested with Whonix 0.2.1 (Ubuntu precise). Many things can go wrong and none or the very least of them will be caused by Whonix. This has only limited support by the Whonix developers, because 1. it's not recommend, for security reasons and 2. the guest additions related bugs and instructions are somewhat out of the scope of the Whonix project.

Installation is somewhat difficult and no packages exist. Just search the internet and you'll see, that loads of people having issues installing the VirtualBox guest additions. People having problems for years. VMware is of no alternative, people are also having trouble installing the VMware tools into Linux guests. The issue with the guest additions is ridiculous. For years no solution has been found. With each kernel update, recompilation is required, and quite often, due to some updates, complication becomes difficult or impossible for a long time.

Also see article, [[http://www.phoronix.com/scan.php?page#news_item&px#OTk5Mw|The VirtualBox Kernel Driver Is Tainted Crap]].

If you are having trouble, than in most cases not because of Whonix. The Whonix setup is a regular Ubuntu Linux and VirtualBox. You can try asking the regular VirtualBox and Ubuntu resources if you have trouble.

= TorChat source package =

== HowTo ==

'''EXPERIMENTAL''' Experimental as in it is difficult to install. Only use it in case you trust TorChat. There shouldn't be any anonymity leaks and it should be as safe as other hidden services in general and in Whonix.

Learn about [https://sourceforge.net/p/whonix/wiki/Hidden%20Services/ Hidden Services] in Whonix first and learn how to set up the hidden webserver. This will ease following this guide.

On Whonix-Gateway.

Open torrc.

<pre>sudo nano /etc/tor/torrc</pre>
Add.

<pre>HiddenServiceDir /var/lib/tor/torchat_service/
HiddenServicePort 11009 192.168.0.11:11009</pre>
Save. Reload Tor.

<pre>sudo service tor reload</pre>
On Whonix-Gateway.

Install dependencies.

<pre>sudo apt-get install python python-wxgtk2.8</pre>
Get your onion address.

<pre>nano /var/lib/tor/torchat_service/hostname</pre>
Backup your key, if you want to ever restore it one another machine, a newer Whonix-Workstation or after hdd failure.

<pre>/var/lib/tor/torchat_service/private_key</pre>
Download the latest Python version of TorChat source code, for example as time of writing torchat-source-0.9.9.553.zip - Python source code (classic standalone 0.9.9 version) from (https://github.com/prof7bit/TorChat/downloads) and store it in ''/home/user''.

Unpack.

<pre>unzip torchat-source-0.9.9.553.zip</pre>
Get into the torchat source folder. For example.

<pre>cd /home/user/torchat-source-0.9.9.553/</pre>
Get into the src folder.

<pre>cd src</pre>
Get into the Tor folder.

<pre>cd Tor</pre>
Rename tor.sh.

<pre>mv tor.sh backup_tor.sh</pre>
Go back to the src folder.

<pre>cd ..</pre>
Create torchat.ini.

<pre>nano torchat.ini</pre>
Add the following content.

<pre>[client]
listen_interface = 192.168.0.11
listen_port = 11009
own_hostname = &lt;your onion hostname without .onion&gt;

[tor]
tor_server = 192.168.0.10
tor_server_control_port = 9154
tor_server_socks_port = 9154

[tor_portable]
tor_server = 192.168.0.10
tor_server_control_port = 9154
tor_server_socks_port = 9154</pre>
Make torchat executable.

<pre>chmod +x torchat.py</pre>
Run torchat.

<pre>./torchat</pre>
=== Alternative ===

After installing the dependencies we could also force install the torchat deb package.

<pre>sudo dpkg -i --force-depends torchat-0.9.9.553.deb</pre>
And then configure the files inside ''/home/user/.torchat''. I don't know if that may be the better way.

= Mixmaster =

== MX capable DNS resolver ==

No longer required.

<font size="-3"> Mixmaster needs to resolve MX DNS records, [https://trac.torproject.org/projects/tor/ticket/7829 while Tor does not support that]. We have to install a DNS resolver capable of doing that. It still comes with caveats.

Required knowledge:

* Introduction chapter of [https://sourceforge.net/p/whonix/wiki/Secondary%20DNS%20Resolver/ Secondary DNS Resolver]

The [https://sourceforge.net/p/whonix/wiki/Secondary%20DNS%20Resolver/#example-with-cznic-labs-dns-resolver Example with CZ.NIC Labs DNS resolver] worked in this case. </font>

<font size=-3> Security considerations when replacing the system wide DNS resolver:

<ul>
<li>The third party DNS resolver traffic goes through it's own circuit, which is good.</li>
<li><p>All (custom installed) applications not configured to use a SocksPort (see [Stream Isolation]), would resolve their DNS through the system wide DNS resolver, which would be the third party resolver, giving too much power to it, because it's always the same, only one service provider, not changing like Tor circuits but static. </font> ## Install Postfix ##</p>
<p>sudo apt-get install postfix ## configure postfix as sattelite system, default settings</p></li></ul>

<font size=-3>Technical background: Mixmaster requires either - a) An (open) smtp server SMTPRELAY in ''/etc/mixmaster/remailer.conf''. Unfortunately, I haven't found any open smtp server (search term: open relay). A mailserver where the user registers first would probable work, but this would defeat the original idea: sending e-mails without depending on registration. Or, - b) a mta (mail transfer agent), which speaks to the remailer directly. '''TODO''': Are there enough Tor exit nodes, which allow the SMTP port and does their ISP allow to speak SMTP? If there are too few servers, it could be bad for anonymity. </font>

Open ''/etc/postfix/main.cf''.

<pre>kdesudo leafpad /etc/postfix/main.cf</pre>
Replace the content with the following.

<pre># See /usr/share/postfix/main.cf.dist for a commented, more complete version


# Debian specific:  Specifying a file name will cause the first
# line of that file to be used as the name.  The Debian default
# is /etc/mailname.
#myorigin = /etc/mailname

smtpd_banner = $myhostname ESMTP $mail_name (Debian/GNU)
biff = no

# appending .domain is the MUA's job.
append_dot_mydomain = no

# Uncomment the next line to generate &quot;delayed mail&quot; warnings
#delay_warning_time = 4h

readme_directory = no

# TLS parameters
smtpd_tls_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
smtpd_tls_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
smtpd_use_tls=yes
smtpd_tls_session_cache_database = btree:${data_directory}/smtpd_scache
smtp_tls_session_cache_database = btree:${data_directory}/smtp_scache

# See /usr/share/doc/postfix/TLS_README.gz in the postfix-doc package for
# information on enabling SSL in the smtp client.

myhostname = host.localdomain
alias_maps = hash:/etc/aliases
alias_database = hash:/etc/aliases
mydestination = host, host.localdomain, localhost.localdomain, localhost
mynetworks = 127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128
mailbox_command = 
mailbox_size_limit = 0
recipient_delimiter = +
inet_interfaces = loopback-only
inet_protocols = all

relayhost = 1.1.1.1
#relayhost = 2.2.2.2</pre>
== Debugging Postfix ==

Looking into the mail log.

<pre>tail -f /var/log/mail.info</pre>
Should contain something like this.

<pre>&lt;date&gt; &lt;time&gt; debian postfix/pickup[id]: id2: uid=1000 from=&lt;user&gt;
&lt;date&gt; &lt;time&gt; debian postfix/cleanup[id]: id2: message-id=&lt;id3.id4@host.localdomain&gt;
&lt;date&gt; &lt;time&gt; debian postfix/qmgr[id]: id2: from=&lt;user@host.localdomain&gt;, size=30000, nrcpt=1 (queue active)
&lt;date&gt; &lt;time&gt; debian postfix/smtp[300]: id2: to=&lt;remailer@breaka.net&gt;, relay=mail.breaka.net[202.75.54.8]:25, delay=30, delays=0.30/0.01/30/3.0, dsn=2.0.0, status=sent (250 OK id=id5-id6-id7)
&lt;date&gt; &lt;time&gt; debian postfix/qmgr[id]: id2: removed</pre>
Reading local mail.

<pre>## Either with cli tool mail.
mail

## Or using gui tool Icedove (Debian version of Mozilla Thunderbird)
## using movemail.</pre>
If all went well, there will be no local mail. Only error messages result in local mails.

= Bugs =

* In Whonix 0.4.5, due to a [https://trac.torproject.org/projects/tor/ticket/7668 Tor Browser upstream bug] (they forgot to update the changelog) and because the keyserver is/was down, the torbrowser and whonixcheck script in Whonix can no longer find out which Tor Browser version is locally installed. ([https://sourceforge.net/p/whonix/discussion/general/thread/6122990d/ Whonix Bug Report]) The [https://sourceforge.net/p/whonix/wiki/TorBrowser/#update-tor-browser Update Tor Browser] chapter contains a workaround and a fix is available for testers.

= Attack matrix in different order =

<table>
<thead>
<tr class="header">
<th align="left">attack</th>
<th align="left">TBB</th>
<th align="left">TBB in a VM</th>
<th align="left">Tails</th>
<th align="left">Tails in a VM</th>
<th align="left">Whonix Standard Download version host+vm+vm</th>
<th align="left">Whonix Physical Isolation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">(1) Protocol IP leak</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">safe</td>
<td align="left">safe</td>
</tr>
<tr class="even">
<td align="left">(2) exploit + Unsafe Browser</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">safe</td>
<td align="left">safe</td>
</tr>
<tr class="odd">
<td align="left">(3) exploit + root exploit + Unsafe Browser</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">safe</td>
<td align="left">safe</td>
</tr>
<tr class="even">
<td align="left">(4) root exploit + Unsafe Browser</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">safe</td>
<td align="left">safe</td>
</tr>
<tr class="odd">
<td align="left">(5) exploit + vm exploit + Unsafe Browser</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">safe</td>
</tr>
<tr class="even">
<td align="left">(6) exploit + vm exploit + exploit against physically isolated Whonix-Gateway</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
</tr>
<tr class="odd">
<td align="left">(7) vm exploit</td>
<td align="left">safe</td>
<td align="left">fail</td>
<td align="left">safe</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">safe</td>
</tr>
<tr class="even">
<td align="left">(8) vm exploit + exploit against physically isolated Whonix-Gateway</td>
<td align="left">safe</td>
<td align="left">fail</td>
<td align="left">safe</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
</tr>
<tr class="odd">
<td align="left">(9) exploit against Tor process</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
</tr>
<tr class="even">
<td align="left">(10) attack against the Tor network</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
<td align="left">fail</td>
</tr>
</tbody>
</table>

= E-Mail Notification =

Users, who have an (anonymous) sourceforge.net account, could go to the [https://sourceforge.net/projects/whonix/ Whonix sf.net Project Page], scroll down to ''Update Notifications'' and hit the ''Subscribe to Updates'' button. They would receive notifications about new releases sent to their (anonymous) [E-Mail] address.

<font size="-3"> There is currently no way for users to subscribe to sf.net blogs or wiki, but such a feature [https://sourceforge.net/p/allura/tickets/5702/ has been requested]. </font>

== Sourceforge.net E-Mail Notification ==

Didn't work reliable.

E-mail notification: For users having an account on sf.net, there is on [https://sourceforge.net/p/whonix/code/ sf.net] git is an [E-Mail] subscribe button: '''M'''.

This is an example how such a mail could look like:

''experimental: comment by adrelanos http://sourceforge.net/p/whonix/code/ci/a1740dfcd391cedfa625d72b990b2a587620df30/''

''experimental: Whonix-Workstation_packages: added gtk3-engines-oxygen by adrelanos http://sourceforge.net/p/whonix/code/ci/7375070a7986230028bf4e82a6ab3ecb420bfd60/''

''---''

''Sent from sourceforge.net because you indicated interest in https://sourceforge.net/p/whonix/code/''

''To unsubscribe from further messages, please visit https://sourceforge.net/auth/prefs/''

= Footer =

[[include ref=WikiFooter]]

