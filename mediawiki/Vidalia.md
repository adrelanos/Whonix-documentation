[[include ref=WikiHeader]]

[TOC]

= Introduction =

'''Not recommend.''' '''Advanced users only!''' '''Not tested since version 0.1.3!''' Better use Arm. See [TorController].

You have two possibility to get Vidalia. 1. Vidalia on the Host and 2. Vidalia on the Whonix-Gateway. Each option has it's pros and cons, we'll discuss here.

= 1. Vidalia on the Host =

Ok, this is an ugly hack, but it works. Vidalia can be installed on the host, in this example on a Windows host but you can most likely do it also on a Linux host. We have to &quot;trick&quot; Vidalia because Vidalia really wants to start Tor.

You will be able to stop Tor using Vidalia, but not be able to start it again. Restarting Tor has to be done manually in console or ssh. &quot;Start proxy application when Tor starts&quot; will probable work (untested) but it will start it on the host and not on the Whonix-Gateway. What also won't work are all settings which modify torrc, because our torrc will be just a dummy one and the real torrc is inside the Whonix-Gateway. All settings in the settings, network tab won't work. Neither the &quot;Sharing/Setup Relaying&quot; tab will work (there will be instructions how to do it manually in torrc for the Whonix-Gateway). Services tab will also not work, this is covered above under Hosting Hidden Services. The &quot;Start Tor&quot; button will actually not start Tor, but connect to the Control Port inside the Whonix-Gateway. &quot;View the network&quot;, &quot;Use a New Identity&quot; and &quot;Message Log&quot; should be functional.

<ol start="0" style="list-style-type: decimal;">
<li>You need to ensure yourself, that port 9051 is firewalled on your host. It must not be accessible from the internet.</li>
<li>Create a folder Vidalia somewhere you like it. Ensure that your current user account has the neccessary rights read, create, modify.</li>
<li>Grab some dummy exe, for example cmd.exe from C:32.exe and copy it to your new Vidalia folder.</li>
<li><p>Login as root ''sudo su''. Go to your Whonix-Gateway and type in console.</p>
<p>tor --hash-password password</p></li></ol>

This will result in something like

<pre>16:E61CFDC2FF3FDCDE605D8EDC3631F268B554612B0721E99F95588282B5

## copy it into the clipboard.</pre>
<ol start="4" style="list-style-type: decimal;">
<li><p>''nano /etc/tor/torrc'' and add</p>
<p>ControlPort 9051 ControlListenAddress 10.0.2.15:9051 HashedControlPassword 16:E61CFDC2FF3FDCDE605D8EDC3631F268B554612B0721E99F95588282B5</p></li>
<li><p>''nano /etc/firewall.sh'' and look out for the following</p>
== Allow incoming SSH connections on the external interface ==

<p>iptables -A INPUT -i $EXT_IF -p tcp --dport 22 -j ACCEPT</p></li></ol>

and add additionally the following below

<pre>## Allow incomming Tor ControlPort connections on the external interface
iptables -A INPUT -i $EXT_IF -p tcp --dport 9051 -j ACCEPT</pre>
<ol start="6" style="list-style-type: decimal;">
<li><p>Then go to your host and create a file named ''control_auth_cookie'' inside your Vidalia folder. Insert the password only, this example we used &quot;password&quot;. Choose your secure password. control_auth_cookie has no file extension, be sure that Windows will normally show you file extensions (like .exe, .pdf...), otherwise you will be probable unable to create a file without extension.</p></li>
<li><p>We need a start file, otherwise Vidalia will use the default documents and settings folder. Call it ''vidalia.bat'' and create it inside your Vidalia folder. The content of vidalia.bat must be</p>
<p>start do_not_start.exe --datadir .\</p></li>
<li><p>And of course you will be needing the Vidalia binaries. Download the Tor Browser Bundle for your platform. Go to *Browser* and copy the following files into your Vidalia directory.</p>
<p>libeay32.dll libgcc_s_dw2-1.dll libgnurx-0.dll mingwm10.dll QtCore4.dll QtGui4.dll QtNetwork4.dll QtXml4.dll ssleay32.dll vidalia.exe</p></li></ol>

tor.exe and tor-resolv.exe will not be needed (we have our own dummy tor.exe).

<ol start="9" style="list-style-type: decimal;">
<li><p>Rename vidalia.exe to do_not_start.exe.</p></li>
<li><p>Create a file called ''vidalia.conf'' inside your Vidalia directory. The content must be</p>
<p>[Tor] TorExecutable=.\tor.exe Torrc=.\torrc DataDirectory=.\ UseRandomPassword=false ControlPassword=password Changed=true ControlPort=9052 ControlAddr=127.0.0.1</p></li>
<li><p>Create a file torrc inside your Vidalia directory, leave it empty, it's just another dummy file for Vidalia's fate.</p></li>
<li><p>In the Whonix-Gateway VM network settings. Set up Port Forwarding: within the &quot;Adapter 1&quot; tab click &quot;Advanced&quot;, then Port Forwarding. Insert a new rule as follows: Name: Vidalia; Protocol: TCP; Host IP: 127.0.0.1; Host Port: 9052; Guest IP: leave blank; Guest Port: 9051</p></li>
<li><p>That's it. From now you can vidalia.bat. For your convinience create a shortcut of vidalia.bat on your desktop.</p></li></ol>

<font size="-3">

* Optional, for debugging if you have problems.
** We test if the IP/Port is reachable from the host. ''telnet 192.168.0.10 9051'', press enter should say &quot;514 Authenication required.&quot;
** [https://trac-vidalia.torproject.org/projects/vidalia/wiki/FAQ%20Vidalia Vidalia FAQ] </font>

= 2. Vidalia on the Whonix-Gateway =

Install a &quot;minimal&quot; desktop environment on the Whonix-Gateway:

<pre>sudo apt-get install xinit xterm openbox vidalia</pre>
You'll be asked to add your user to the debian-tor group. Do so! To apply this change you need to log out (type ''exit'') and log in again. Then use ''startx'' from the console to launch the graphical desktop. Right-click on the desktop to open the menu, open a terminal and from that launch vidalia. A more user-friendly graphical environment would drastically increase RAM requirements and [https://en.wikipedia.org/wiki/Attack_surface attack surface].

Do not be tempted to use Whonix-Gateway as a client OS!

= Footer =

[[include ref=WikiFooter]]

