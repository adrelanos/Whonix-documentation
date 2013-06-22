[[include ref=WikiHeader]]

[TOC]

= Basic Troubleshooting =

== Before you start ==

[https://sourceforge.net/p/whonix/wiki/Download/#verify-the-whonix-virtual-machine-images Verify the Whonix virtual machine images].

== On the host ==

=== General ===

Always test first, if your host internet connection is working. (ping 8.8.8.8, ping google.com, etc). On your host:

<pre>ping google.com</pre>
Check time.

<pre>date</pre>
''sudo dpkg-reconfigure -a'' must be silent, i.e. not show any errors, must show output at all. Will take a while...

<pre>sudo dpkg-reconfigure -a</pre>
''sudo dpkg --configure -a'' must be silent, i.e. not show any errors, must show output at all. Will take a while...

<pre>sudo dpkg --configure -a</pre>
Get all updates:

<pre>sudo apt-get update
sudo apt-get dist-upgrade</pre>
Check Virtual Box version.

<pre>vboxmanage --version</pre>
Get the Tor Browser Bundle from torproject.org and test if it's working.

<pre># If you can not get the Tor Browser Bundle to work,
# you will most certainly not get Whonix to work either.
#
# In the Whonix Readme it is recommend to have a current
# copy of the Tor Browser Bundle at all times.
#
# The Tor Browser Bundle is great for testing if you live in a
# censored area or not, if Tor is blocked by your ISP or not.
# When you need (private) (obfuscated) bridges for the Tor Browser Bundle,
# you will need them for Whonix as well.</pre>
=== Import Whonix images ===

Importing the images with the Virtual Box gui should work well in most cases. If not, please check first if you have enough free disk space. Please also refer to the [https://sourceforge.net/p/whonix/wiki/Readme/#if-you-need-more-help-with-installing Whonix Install Screenshot or Video Tutorial]. Also check if the checksums of the ova images match, which is explained at the top of this page.

Delete any half imported or otherwise broken virtual machine images by using the VBoxManage command line tool. Copy the output.

<pre>VBoxManage unregistervm &quot;Whonix-Workstation&quot; --delete</pre>
Go to the folder where you downloaded Whonix. Import Whonix-Workstation by using the VBoxManage command line tool.

<pre>VBoxManage import Whonix-Workstation.ova</pre>
Clean (anonymize) the output.

<pre># Remove operating system user name or any problematic paths.</pre>
[https://sourceforge.net/p/whonix/wiki/Contact/ Contact Whonix developer] by sending the output.

<pre>.</pre>
== On the Gateway ==

=== Login as user ===

Check your <code>route</code> command, make sure the network 192.168.0.0 is associated with eth1.

<pre>route</pre>
Check if Tor is running with 'pgrep tor -l', this should return something like &quot;103 tor&quot;. If not try 'sudo service tor start' and check for any errors.

<pre>pgrep tor -l</pre>
Check the status of Tor.

<pre>sudo service tor status | less</pre>
Should reply with.

<pre>tor is running.</pre>
Restart Tor.

<pre>sudo service tor restart | less</pre>
Tor should show only notices, no errors.

Verify Tor configuration is valid:

<pre>sudo tor --verify-config | less</pre>
You should see confirmation:

<pre>Configuration was valid</pre>
Ping the Whonix-Workstation.

<pre>ping 192.168.0.11</pre>
Ping Virtual Box.

<pre>ping 10.0.2.2
ping 10.0.2.2</pre>
Should show ''Packet filtered''.

nslookup should NOT work.

<pre>nslookup google.com</pre>
Should show timeout.

=== Login as unsafe ===

'''The following tests might reveal, that you are a Whonix user. Omit them, if that is of concern for you.'''

unsafe user account has no password. Login with

<pre>sudo su unsafe</pre>
Remove write protection from /etc/resolv.conf

<pre>chattr -i /etc/resolv.conf</pre>
Restart networking. DHCP will rewrite /etc/resolv.conf (Temporary login as root.)

<pre>service networking restart</pre>
Check /etc/resolv.conf.

<pre>nano /etc/resolv.conf</pre>
Content should be:

<pre>nameserver 10.0.2.2</pre>
Check if dns resolution is functional.

<pre>nslookup google.com</pre>
== Tests on both Virtual Machines ==

Run the following tests on Whonix-Gateway and on Whonix-Workstation.

Check time.

<pre>date</pre>
''sudo dpkg-reconfigure -a'' must be silent, i.e. not show any errors, must show output at all. Will take a while...

<pre>sudo dpkg-reconfigure -a</pre>
''sudo dpkg --configure -a'' must be silent, i.e. not show any errors, must show output at all. Will take a while...

<pre>sudo dpkg --configure -a</pre>
Test update-grub.

<pre>sudo update-grub</pre>
Run 'locale'. Must not report any error.

<pre>locale
sudo locale</pre>
Restart networking:

<pre>sudo service networking restart | less</pre>
Apt-get must be fully functional.

<pre>sudo apt-get update
sudo apt-get dist-upgrade</pre>
Test whonixcheck.

<pre>whonixcheck</pre>
Test whonixcheck with debugging.

<pre>whonixcheck --verbose</pre>
Check the timezone.

<pre>cat /etc/timezone</pre>
Must be ''Etc/UTC''.

= Advanced users / developers and testers only =

== On Whonix-Gateway and Whonix-Workstation ==

Install dpkg-dev, which is required for dpkg-vendor.

<pre>sudo apt-get install --no-install-recommends dpkg-dev</pre>
Run ''dpkg-vendor --query vendor''.

<pre>dpkg-vendor --query vendor</pre>
The output must be &quot;Whonix&quot;.

Check apt config and see if periodic updates are disabled.

<pre>apt-config dump</pre>
Install test wise new kernel.

<pre>.</pre>
Remove test wise linux-image-486 kernel.

<pre>sudo apt-get remove linux-image-486</pre>
Check content of ''/etc/network/interfaces''.

<pre>nano /etc/network/interfaces</pre>
Check content of ''/etc/resolv.conf''.

<pre>nano /etc/resolv.conf</pre>
Check ''/etc/apt/sources.list''.

<pre>nano /etc/apt/sources.list</pre>
Check contents of ''/etc/resolv.conf''.

<pre>nano /etc/resolv.conf</pre>
Check iptables.

<pre>sudo iptables --list | more</pre>
=== Extra ===

Check if /var/run/bootclockrandomization/success exists.

<pre>nano /var/log/bootclockrandomization.log

sudo service bootclockrandomization status

echo $?</pre>
Check if /var/run/timesanitycheck/success exists.

<pre>nano /var/log/timesanitycheck.log

sudo service timesanitycheck status

echo $?</pre>
Check if /var/run/htpdate/success exists

<pre>nano /var/log/htpdate.log

sudo service htpdate status

echo $?</pre>
== Test on Whonix-Gateway ==

Check the logs.

<pre>less /var/log/tor/log</pre>
Test if arm is fully functional.

<pre>sudo arm</pre>
Test if arm's new identity function is working.

<pre>.</pre>
Install a small text-based browser and torsocks

<pre>sudo apt-get -y install links torsocks ca-certificates</pre>
Now use the tools together to connect to the special “testing” site via tor:

<pre>usewithtor links https://check.torproject.org/</pre>
You should receive a “Congratulations. Your browser is configured to use Tor.” message. If not, there is some issue with the Tor installation or firewall configuration. Find more information [https://www.torproject.org/docs/tor-doc-unix.html.en#verify here on troubleshooting your Tor installation]. [https://trac.torproject.org/projects/tor/wiki/doc/torsocks See documentation on torsocks here.]

[https://www.torproject.org/docs/tor-doc-unix.html.en#verify See Tor documentation for testing].

<pre>.</pre>
After logging in you should see Whonix help/welcome/disclaimer message.

<pre>.</pre>
== Test Whonix-Workstation ==

=== Basics ===

Ping the Whonix-Gateway. Will ''NOT'' work.

<pre># You will not be able to ping the Whonix-Gateway,
# because ICMP is blocked by the firewall.
# If you want to test it, you have to adjust the firewall,
# or to deactivate the firewall while testing.
ping 192.168.0.10</pre>
Power off Whonix-Gateway. Try to ping outside or to use the browser in Whonix-Workstation. Obviously, should NOT work.

<pre>.</pre>
Power on Whonix-Gateway again. Visit https://check.torproject.org/ with Tor Browser. You should see a “Congratulations”.

<pre>.</pre>
Use a Tor Browser to visit a .onion address (Try the [http://idnxcnkne4qt76tg.onion torproject.org hidden service])

<pre>http://idnxcnkne4qt76tg.onion</pre>
Note: Ping commands should NOT work for external addresses from your Whonix-Workstation, [http://en.wikipedia.org/wiki/Internet_Control_Message_Protocol ICMP traffic] is not proxied, and filtered by /usr/local/bin/whonix_firewall, because Tor does not support UDP.

<pre>.</pre>
'''dig google.com''' must only return a single IP, compare with the output on Whonix-Gateway or Host.

<pre>dig google.com</pre>
Test gpg.

<pre># Example:
gpg --keyserver keys.gnupg.net --recv A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89</pre>
Test wget uwt wrapper.

<pre>wget http://idnxcnkne4qt76tg.onion</pre>
Test wget through TransPort.

<pre>/usr/bin/wget http://idnxcnkne4qt76tg.onion</pre>
Setup a hidden service on Whonix-Gateway and test if it works. You can access your own test hidden service using Tor Browser.

<pre>.</pre>
See if whonixcheck gets autostarted.

<pre>.</pre>
Test XChat, connect to a an SSL protected IRC server.

<pre>.</pre>
test XChat, connect to a hidden IRC server.

<pre>.</pre>
=== Applications ===

* [Metadata]
* [Mixmaster]
* [TorBrowser]

= Footer =

[[include ref=WikiFooter]]

