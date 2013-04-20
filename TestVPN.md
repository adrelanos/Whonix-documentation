[[include ref=WikiHeader]]

[TOC]

# Introduction #
The purpose of this page is mainly to demonstrate, how easy it is, to add a VPN to Whonix, to tunnel user -> Tor -> VPN or the other way around. 

Read first [Whonix VPN disclaimer](https://sourceforge.net/p/whonix/wiki/Authorship/#whonix-vpn-disclaimer).

Can be either:

* [Tunnel Tor through VPN](https://sourceforge.net/p/whonix/wiki/Tunnel_Tor_through_proxy_or_VPN_or_SSH/). (Read first!) (Install on Whonix-Gateway.)
* [Tunnel VPN through Tor](https://sourceforge.net/p/whonix/wiki/Tunnel_Proxy_or_SSH_or_VPN_through_Tor/). (Read first!) (Install on Whonix-Workstation.)

Leave no personal information while signing up. Use an extra e-mail address for registration, which you will never use for anything else. If you plan to use user -> Tor -> VPN, you should obviously also sign up using Tor. (Not sure, whats best, Tor or not, to sign up when planing on using user -> VPN -> Tor. Probable Tor can't hurt.)

# Examples #
## Riseup.net ##
### Riseup.net Quick VPN Command Line Test ###
Known to support TCP, UDP, SSL.

(1) You need a riseup.net account.

(2) You need to know your riseup account name.

(3) Go to riseup.net -> help -> VPN and obtain your VPN secret. (VPN password)

(4) Look inside the [riseup VPN help page](https://help.riseup.net/en/vpn-howto) for [*RiseupCA.pem*](https://help.riseup.net/en/riseup-ca) and download it.

(5) Open a terminal. (konsole) Get into the same folder, you stored *RiseupCA.pem*.

(6) Install openvpn.

    apt-get install openvpn

(7) The following line from the [riseup OpenVPN help page](https://help.riseup.net/en/openvpn-linux) won't work for user -> Tor -> VPN, because the Tor network does not support UDP.

    sudo openvpn --client --dev tun --auth-user-pass --remote vpn.riseup.net 1194 --ca RiseupCA.pem

The following line works for user -> Tor -> VPN.

    sudo openvpn --client --dev tun --auth-user-pass --remote vpn.riseup.net 1194 --ca RiseupCA.pem --proto tcp

(8) For DNS, see Riseup DNS below.

### Riseup.net riseup.ovpn ###
Known to support TCP, UDP, SSL.

(1) You need a riseup.net account.

(2) You need to know your riseup account name.

(3) Go to riseup.net -> help -> VPN and obtain your VPN secret. (VPN password)

(4) Look inside the [riseup VPN help page](https://help.riseup.net/en/vpn-howto) for [*RiseupCA.pem*](https://help.riseup.net/en/riseup-ca) and download it.

(5) Create a file *auth.txt* inside the same folder.

    riseupusername
    vpnsecret

(6) Create a file *riseup.ovpn* inside the same folder.

    client
    dev tun
    auth-user-pass auth.txt
    #remote vpn.riseup.net 443
    #remote seattle.vpn.riseup.net 443
    remote nyc.vpn.riseup.net 80
    ca RiseupCA.pem
    remote-cert-tls server
    script-security 1
    #user nobody
    #group nobody
    proto tcp

(7) Start OpenVPN.

    sudo openvpn riseup.ovpn

(8) For DNS, see Riseup DNS below.

### Riseup DNS ###
#### Setup ####
Open */etc/resolv.conf*.

    kdesudo kwrite /etc/resolv.conf

Comment out.

    #nameserver 192.168.0.10

Add.

    ## Riseup.net OpenVPN DNS server
    nameserver 172.27.100.1

If you want to be sure, that */etc/resolv.conf* does not get overwritten by other packages. (Such as DHCP or resolvconf.)

    sudo chattr +i /etc/resolv.conf

If you ever want to remove it, use *-i*.

#### Testing ####
When using "*nameserver 192.168.0.10*"...

    nslookup idnxcnkne4qt76tg.onion

Will show.

    Server:         192.168.0.10
    Address:        192.168.0.10#53
    
    Non-authoritative answer:
    Name:   idnxcnkne4qt76tg.onion
    Address: 10.192.0.1

When using "*nameserver 172.27.100.1*"...

    nslookup idnxcnkne4qt76tg.onion

Will show.

    Server:         172.27.100.1
    Address:        172.27.100.1#53

    ** server can't find idnxcnkne4qt76tg.onion: NXDOMAIN

Because you can not access .onion domains when a VPN has be chained. (user -> Tor -> VPN)

Resolving clearnet DNS should work.

    nslookup riseup.net

Should show.

    Server:         172.27.100.1
    Address:        172.27.100.1#53

    Non-authoritative answer:
    Name:   riseup.net
    Address: 198.252.153.35

## securityKISS.com ##
Unfortunately securityKISS.com drops many TCP and UDP ports beside ports 80 and 443. That limits it's usefulness for testing purposes, such as [Tunnel UDP over Tor](https://sourceforge.net/p/whonix/wiki/TunnelUDPoverTor/). If you know a less restrictive free VPN provider, we'd be thankful for a comment.

Install openvpn.

    apt-get install openvpn

Register at securitykiss.com, login and download their OpenVPN package to /home/user. Unpack. The folder contains contains ca.cert, client.cert, client.key, README.txt (with list of their servers and ports). Rename the folder to securitykiss. Structure should be like /home/user/ca.cert etc.

*nano /etc/openvpn/client.conf*, edit server IP and port and past it. (It's almost only the default openvpn client.conf with minor changes.)

    ##############################################
    # Sample client-side OpenVPN 2.0 config file #
    # for connecting to multi-client server.     #
    #                                            #
    # This configuration can be used by multiple #
    # clients, however each client should have   #
    # its own cert and key files.                #
    #                                            #
    # On Windows, you might want to rename this  #
    # file so it has a .ovpn extension           #
    ##############################################

    # Specify that we are a client and that we
    # will be pulling certain config file directives
    # from the server.
    client

    # Use the same setting as you are using on
    # the server.
    # On most systems, the VPN will not function
    # unless you partially or fully disable
    # the firewall for the TUN/TAP interface.
    ;dev tap
    dev tun

    # Windows needs the TAP-Win32 adapter name
    # from the Network Connections panel
    # if you have more than one.  On XP SP2,
    # you may need to disable the firewall
    # for the TAP adapter.
    ;dev-node MyTap

    # Are we connecting to a TCP or
    # UDP server?  Use the same setting as
    # on the server.
    proto tcp
    ;proto udp

    # The hostname/IP and port of the server.
    # You can have multiple remote entries
    # to load balance between the servers.
    remote 91.121.208.218 443
    ;remote my-server-2 1194

    # Choose a random host from the remote
    # list for load-balancing.  Otherwise
    # try hosts in the order specified.
    ;remote-random

    # Keep trying indefinitely to resolve the
    # host name of the OpenVPN server.  Very useful
    # on machines which are not permanently connected
    # to the internet such as laptops.
    resolv-retry infinite

    # Most clients don't need to bind to
    # a specific local port number.
    nobind

    # Downgrade privileges after initialization (non-Windows only)
    user nobody
    group nogroup

    # Try to preserve some state across restarts.
    persist-key
    persist-tun

    # If you are connecting through an
    # HTTP proxy to reach the actual OpenVPN
    # server, put the proxy server/IP and
    # port number here.  See the man page
    # if your proxy server requires
    # authentication.
    ;http-proxy-retry # retry on connection failures
    ;http-proxy [proxy server] [proxy port #]

    # Wireless networks often produce a lot
    # of duplicate packets.  Set this flag
    # to silence duplicate packet warnings.
    ;mute-replay-warnings

    # SSL/TLS parms.
    # See the server config file for more
    # description.  It's best to use
    # a separate .crt/.key file pair
    # for each client.  A single ca
    # file can be used for all clients.
    ca /home/user/securitykiss/ca.crt
    cert /home/user/securitykiss/client.crt
    key /home/user/securitykiss/client.key

    # Verify server certificate by checking
    # that the certicate has the nsCertType
    # field set to "server".  This is an
    # important precaution to protect against
    # a potential attack discussed here:
    #  http://openvpn.net/howto.html#mitm
    #
    # To use this feature, you will need to generate
    # your server certificates with the nsCertType
    # field set to "server".  The build-key-server
    # script in the easy-rsa folder will do this.
    ns-cert-type server

    # If a tls-auth key is used on the server
    # then every client must also have the key.
    ;tls-auth ta.key 1

    # Select a cryptographic cipher.
    # If the cipher option is used on the server
    # then you must also specify it here.
    ;cipher x

    # Enable compression on the VPN link.
    # Don't enable this unless it is also
    # enabled in the server config file.
    comp-lzo

    # Set log file verbosity.
    verb 3

    # Silence repeating messages
    ;mute 20

To initially start the VPN type:

    sudo /etc/init.d/openvpn start
    sudo openvpn /etc/openvpn/client.conf

After rebooting the VPN will be automatically started. 

If you do not wish to start the VPN automatically for some reason: *nano /etc/default/openvpn*

    AUTOSTART=="none"

DNS settings have not been considered for this securitykiss.com chapter.

## usaip.eu ##
For testing purposes, in past, [usaip.eu](https://www.usaip.eu/) was used. They have been chosen, because they were free and didn't block the tested outgoing UDP port. The free version of usaip.eu can probable only be used for testing purposes, as it's only a test version, which force disconnects every 7 minutes. For longer and serious/stable use, you'll probable need another, VPN account.

**Note, usaip probable blocks SSL, therefore** */usr/bin/curl --tlsv1 --proto =https https://check.torproject.org* **will not work.**

Install OpenVPN.

    sudo apt-get install openvpn

Go to [usaip.eu](http://usaip.eu/en/index.php) and click on free demo. Download the *usaip.zip*. It contains the OpenVPN configuration files. Unpack. Open a shell and get into the folder *cd usaip*. List all files *dir*. Connect to a VPN, for example:

    sudo openvpn /home/user/usaip/eu-luxemburg.ovpn

At time of writing, the page stated, the password was *demo*, password also *demo*. Wait until it's connected. When success, it will show "Initialization Sequence Completed". It might happen, that the connection will not succeed for some unknown reason. In this case try replacing the eu-luxemburg.ovpn from the example above with another <country>.ovpn from the usaip folder.

DNS settings have not been considered for this usaip.eu chapter.

## Using a graphical user interface ##
### KDE Network Manager ###
If you want to install the KDE Network Manager.

    sudo apt-get install network-manager-kde

Start menu -> System Settings -> Network Settings

At time of writing the [riseup.net OpenVPN instructions for KDE](https://www.riseup.net/en/openvpn-linux#kde) where not finished. Perhaps you'll find out yourself, use another guide for KDE Network Manager or use the command line based examples above.

Don't wonder if you don't see Whonix-Workstation's (virtual) wired network interface to Whonix-Gateway. That's still managed by the ordinary ifupdown way in /etc/network/interfaces. See [Dev_NetworkManager] if you want to know why it's not installed by default in Whonix.

### GNOME Network Manager ###
Although Whonix is by default based on KDE, you can usually integrate GNOME applications.

In case of GNOME Network Manager it just requires some more fiddling because upstream developers wanted to make GNOME and KDE as compatible as possible, which includes that one settings manager won't show up when the other desktop has been started in a dual (KDE, GNOME) installation.

If you want to install the GNOME Network Manager.

    sudo apt-get install network-manager-gnome network-manager-openvpn-gnome

If you want to autostart GNOME Network Manager, open /etc/xdg/autostart/nm-applet.desktop with root rights.

    kdesudo kwrite /etc/xdg/autostart/nm-applet.desktop

And comment out.

    NotShowIn=KDE;

If you want to make the nm-applet start menu entries visible and to start it manually, open /usr/share/applications/nm-applet.desktop.

    kdesudo kwrite /usr/share/applications/nm-applet.desktop

And comment out.

    NotShowIn=KDE;

And add.

    Categories=GNOME;GTK;Settings;X-GNOME-NetworkSettings;

If you want to make the nm-connection-editor start menu entries visible and to start it manually, open nm-connection-editor.

    kdesudo kwrite /usr/share/applications/nm-connection-editor.desktop

And comment out.

    NotShowIn=KDE;

Then you could open the settings.

    Applications -> Settings -> Network Connections 

You could try the [riseup.net OpenVPN instructions for GNOME](https://www.riseup.net/en/openvpn-linux#gnome).

# Footer #
[[include ref=WikiFooter]]