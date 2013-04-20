[[include ref=WikiHeader]]

[TOC]

# Introduction
**Not recommend.** **Advanced users only!** **Not tested since version 0.1.3!** Better use Arm. See [TorController].

You have two possibility to get Vidalia. 1. Vidalia on the Host and 2. Vidalia on the Whonix-Gateway. Each option has it's pros and cons, we'll discuss here.

# 1. Vidalia on the Host
Ok, this is an ugly hack, but it works. Vidalia can be installed on the host, in this example on a Windows host but you can most likely do it also on a Linux host. We have to "trick" Vidalia because Vidalia really wants to start Tor.

You will be able to stop Tor using Vidalia, but not be able to start it again. Restarting Tor has to be done manually in console or ssh. "Start proxy application when Tor starts" will probable work (untested) but it will start it on the host and not on the Whonix-Gateway. What also won't work are all settings which modify torrc, because our torrc will be just a dummy one and the real torrc is inside the Whonix-Gateway. All settings in the settings, network tab won't work. Neither the "Sharing/Setup Relaying" tab will work (there will be instructions how to do it manually in torrc for the Whonix-Gateway). Services tab will also not work, this is covered above under Hosting Hidden Services. The "Start Tor" button will actually not start Tor, but connect to the Control Port inside the Whonix-Gateway. "View the network", "Use a New Identity" and "Message Log" should be functional.

(0) You need to ensure yourself, that port 9051 is firewalled on your host. It must not be accessible from the internet.
(1) Create a folder Vidalia somewhere you like it. Ensure that your current user account has the neccessary rights read, create, modify. 
(2) Grab some dummy exe, for example cmd.exe from C:\Windows\System32\cmd.exe and copy it to your new Vidalia folder. 
(3) Login as root *sudo su*. Go to your Whonix-Gateway and type in console.

    tor --hash-password password

This will result in something like

    16:E61CFDC2FF3FDCDE605D8EDC3631F268B554612B0721E99F95588282B5

    ## copy it into the clipboard.

(4) *nano /etc/tor/torrc* and add

    ControlPort 9051
    ControlListenAddress 10.0.2.15:9051
    HashedControlPassword 16:E61CFDC2FF3FDCDE605D8EDC3631F268B554612B0721E99F95588282B5

(5) *nano /etc/firewall.sh* and look out for the following

    ## Allow incoming SSH connections on the external interface
    iptables -A INPUT -i $EXT_IF -p tcp --dport 22 -j ACCEPT

and add additionally the following below

    ## Allow incomming Tor ControlPort connections on the external interface
    iptables -A INPUT -i $EXT_IF -p tcp --dport 9051 -j ACCEPT

(6) Then go to your host and create a file named *control_auth_cookie* inside your Vidalia folder. Insert the password only, this example we used "password". Choose your secure password. control_auth_cookie has no file extension, be sure that Windows will normally show you file extensions (like .exe, .pdf...), otherwise you will be probable unable to create a file without extension.

(7) We need a start file, otherwise Vidalia will use the default documents and settings folder. Call it *vidalia.bat* and create it inside your Vidalia folder. The content of vidalia.bat must be

    start do_not_start.exe --datadir .\\

(8) And of course you will be needing the Vidalia binaries. Download the Tor Browser Bundle for your platform. Go to *\Tor Browser\App\* and copy the following files into your Vidalia directory.

    libeay32.dll
    libgcc_s_dw2-1.dll
    libgnurx-0.dll
    mingwm10.dll
    QtCore4.dll
    QtGui4.dll
    QtNetwork4.dll
    QtXml4.dll
    ssleay32.dll
    vidalia.exe

tor.exe and tor-resolv.exe will not be needed (we have our own dummy tor.exe).

(9) Rename vidalia.exe to do_not_start.exe.

(10) Create a file called *vidalia.conf* inside your Vidalia directory. The content must be

    [Tor]
    TorExecutable=.\\tor.exe
    Torrc=.\\torrc
    DataDirectory=.\\
    UseRandomPassword=false
    ControlPassword=password
    Changed=true
    ControlPort=9052
    ControlAddr=127.0.0.1

(11) Create a file torrc inside your Vidalia directory, leave it empty, it's just another dummy file for Vidalia's fate.

(12) In the Whonix-Gateway VM network settings. Set up Port Forwarding: within the "Adapter 1" tab click "Advanced", then Port Forwarding. Insert a new rule as follows: Name: Vidalia; Protocol: TCP; Host IP: 127.0.0.1; Host Port: 9052; Guest IP: leave blank; Guest Port: 9051

(13) That's it. From now you can vidalia.bat. For your convinience create a shortcut of vidalia.bat on your desktop.

<font size="-3">

* Optional, for debugging if you have problems. 
    * We test if the IP/Port is reachable from the host. *telnet 192.168.0.10 9051*, press enter should say "514 Authenication required."
    * [Vidalia FAQ](https://trac-vidalia.torproject.org/projects/vidalia/wiki/FAQ Vidalia)
</font>

# 2. Vidalia on the Whonix-Gateway
Install a "minimal" desktop environment on the Whonix-Gateway:

    sudo apt-get install xinit xterm openbox vidalia

You'll be asked to add your user to the debian-tor group. Do so! To apply this change you need to log out (type *exit*) and log in again. Then use *startx* from the console to launch the graphical desktop. Right-click on the desktop to open the menu, open a terminal and from that launch vidalia. A more user-friendly graphical environment would drastically increase RAM requirements and [attack surface](https://en.wikipedia.org/wiki/Attack_surface).

Do not be tempted to use Whonix-Gateway as a client OS!

# Footer #
[[include ref=WikiFooter]]