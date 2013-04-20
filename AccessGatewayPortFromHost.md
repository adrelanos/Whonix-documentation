[[include ref=WikiHeader]]

[TOC]

# Access Whonix-Gateway Port From Host
**This is very esoteric and you probable don't need it!**
**Advanced users only!**

## Example: Make port 9050 accessible from the host.
On the host...

In the Whonix-Gateway VM network settings. Set up Port Forwarding: within the "Adapter 1" tab click "Advanced", then Port Forwarding. Insert a new rule as follows.

    Name: 9050
    Protocol: TCP
    Host IP: 127.0.0.1
    Host Port: 9050
    Guest IP: leave blank
    Guest Port: 9050

Or the same as command line.

    VBoxManage modifyvm "Whonix-Gateway" --natpf1 "9050",tcp,127.0.0.1,9050,,9050

Inside Whonix-Gateway...

Add to /etc/tor/torrc.

    ## 10.0.2.15 is usually obtained form Virtual Box's DHCP server.
    ## Hope this always works, otherwise you have to edit /etc/network/interfaces
    ## and use a static virtual LAN IP.
    SocksPort 10.0.2.15:9050

    ## The next line is not strictly required, neat for debugging.
    SocksPort 127.0.0.1:9050

Reload Tor.

    sudo service tor reload

We need to /usr/local/bin/whonix_firewall. Look for.

    ## Allow incoming SSH connections on the external interface.
    ## DISABELD BY DEFAULT. Only for testing/debugging.
    if [ "$GATEWAY_ALLOW_INCOMING_SSH" = "1" ]; then
       iptables -A INPUT -i "$EXT_IF" -p tcp --dport 22 -j ACCEPT
    fi

And below that, add.

    iptables -A INPUT -i "$EXT_IF" -p tcp --dport 9050 -j ACCEPT

## Debugging
Inside Whonix-Gateway...

Switch to clearnet user.

    su clearnet
    ## default password: changeme

Test if the port you want to make available on the host is available from inside Whonix-Workstation. (If that's not the case, something is fundamentally wrong and you need to fix this first.)

    ## Circumventing uwt curl wrapper.
    /usr/bin/curl 127.0.0.1:9050

    ## Circumventing uwt curl wrapper.
    /usr/bin/curl 10.0.2.15:9050

It should answer "Tor is not a http proxy".

## Testing
On the host...

    /usr/bin/curl 127.0.0.1:9050

It should answer "Tor is not a http proxy". If you see that, that indicates that Tor is, which runs inside Whonix-Gateway is accessible on the host as well.

## Forwarding that port to LAN
On the host...

This is untested, but should work, otherwise get in contact.

You can use something like rinetd to redirect that port 127.0.0.1:9050 to a different network interface. Otherwise you could experiment with the Whonix-Gateway VM network settings.

# Footer #
[[include ref=WikiFooter]]