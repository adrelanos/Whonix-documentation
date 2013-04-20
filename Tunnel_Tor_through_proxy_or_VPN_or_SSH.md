[[include ref=WikiHeader]]

[TOC]

# Tunnel Tor through proxy, VPN or SSH #
## Introduction ##
**user -> proxy/VPN/SSH -> Tor**

Read first: [Tor Plus VPN or proxy](https://trac.torproject.org/projects/tor/wiki/doc/TorPlusVPN) and [Whonix VPN disclaimer](https://sourceforge.net/p/whonix/wiki/Authorship/#whonix-vpn-disclaimer).

Sometimes you are **forced to use a proxy or VPN** to make outgoing connections, some ISP's force you, or you are in a LAN with a proxy (router), or in a cooperate environment.

A proxy, VPN or SSH can also be possibly

* **used to circumvent Tor blocks** or to
* **hide the fact you are using Tor**, in that case make sure you have read [Hide Tor and Whonix from your ISP ](https://sourceforge.net/p/whonix/wiki/Hide%20Tor%20and%20Whonix%20from%20your%20ISP/).

VPN and SSH are preferred choice, as they support secure encryption between you and them. It's a question, how much you can trust the server, they'll see, that you are using Tor, but thanks to Tor, they won't see what you are doing. If you use your own server in a safe country, while you are in a dangerous country, that's probable your best bet. Anyway, not so many people seem to do use a tunnel before they connect to Tor, therefore it's not so well tested, do not rely on it too much.

If nothing above applies for you, skip this section.

## Tunnel Tor through proxy ##
**user -> proxy -> Tor**

On Whonix-Gateway:

    sudo nano /etc/tor/torrc

Depending on your proxy configuration, add the settings you'll need to your /etc/torrc. For more information on these settings, have a look in the [Tor manual](https://www.torproject.org/docs/tor-manual.html.en) and read the [FAQ](https://trac.torproject.org/projects/tor/wiki/doc/TorFAQ#MyInternetconnectionrequiresanHTTPorSOCKSproxy).

    HTTPProxy host[:port]
    HTTPProxyAuthenticator username:password
    HTTPSProxy host[:port]
    HTTPSProxyAuthenticator username:password
    Socks4Proxy host[:port]
    Socks5Proxy host[:port]
    Socks5ProxyUsername username
    Socks5ProxyPassword password

## Tunnel Tor through SSH ##
** user -> SSH -> Tor**

**This section is not fully tested/complete. Please give feedback if it worked for you.** This doesn't seam to be very popular, no one ever asked about it in over one year.

This chapter is about tunneling Tor through a SSH tunnel.

Setting up the VPN tunnel could be either done on the host or inside Whonix-Gateway.

First we have to install the ssh client.

    apt-get install ssh

Then be sure that your SSH connection itself is working well. SSH to your ssh server using *ssh yourusername@your.ssh.server*. It's recommend to set up public key authentication. (TODO: how to create a private and public key) *cd /home/yourusername*, *mkdir .ssh*, *nano authorized_keys*, paste line beginning with *ssh-rsa ...* (your public key) (TODO: how to create that line).

*exit* (terminate SSH connection) and login again using public key authentication. (TODO: how to do that) When that is working install your favorite text mode browser, for example *apt-get install lynx* and test if the shell's external internet connection is working. 
*lynx check.torproject.org* You're done with the pre-requriements. Exit your shell. *exit*

Now we will tell the SSH client to start a socks5 proxy server listening on localhost 127.0.0.1 port 1080. The following command has to be run in background (TODO: add line how to do that) on each start up, before Tor starts (TODO: to which file, to do that). It would be wise to activate public key authentication (TODO: how to add private key to use public key authentication).

    ssh -C -D 1080 your.ssh.server

Now we have to tell Tor to use the new local ssh server. *nano /etc/torrc* and add

    ## In case SSH tunnel has been setup from Whonix-Gateway.
    Socks5Proxy 127.0.0.1:1080

    ## In case SSH tunnel has been setup on the host.
    #Socks5Proxy IP:PORT

We are done, from now on, Tor will connect through the SSH server.

(TODO: if running inside Whonix-Gatewy, probable new firewall rules are required.)

## Tunnel Tor through VPN ##
### Introduction ###
**user -> VPN -> Tor**

There are too many different VPN protocols. To many to add all of them to this guide. However, at least adding OpenVPN would be worth it.

If you are using VPN not,

* **because you are forced to use VPN by your ISP**, but
* want to **add an additional layer of protection**, or
* to **hide the fact that you are using Tor**, in that case make sure you have read [Hide Tor and Whonix from your ISP ](https://sourceforge.net/p/whonix/wiki/Hide%20Tor%20and%20Whonix%20from%20your%20ISP/)

then be sure, that your VPN software is secure (ex: use OpenVPN, not pptp).

### Use a Fail Closed Mechanism ###
**TODO**:
VPN's generally fail open. This is not a Whonix specific problem. It is a general problem with VPNs. This means, if the VPN is unreachable, connections breaks down for whatever reasons and so on, in most cases, you can continue to connect to the internet without the VPN. In case of Whonix you would be left to the protections provided by Tor. This should probable matter to you, since you wanted to combine Tor with a VPN. A [Fail Closed Mechanism](https://sourceforge.net/p/whonix/wiki/VPN/) is under development and help is welcome.

### How ##
If you are forced to use a VPN server or if you are already using a VPN server, you most likely know how you can connect to it.

You can either add the VPN on the host. Whonix-Gateway will be tunneled through it.

Or you can add the VPN into Whonix-Gateway. In that case you must know how to connect to your VPN server from the linux command line. (TODO: Any new firewall rules required?)

When your VPN is properly set up, all your connections are forced through the VPN first. If you start Tor on top of that, tunneling Tor through the VPN will work.

See also [A Free example VPN working with Whonix for testing purposes](https://sourceforge.net/p/whonix/wiki/TestVPN/).

# Footer #
[[include ref=WikiFooter]]