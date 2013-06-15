[[include ref=WikiHeader]]

[TOC]

# Basic Troubleshooting #
## Before you start ##
[Verify the Whonix virtual machine images](https://sourceforge.net/p/whonix/wiki/Download/#verify-the-whonix-virtual-machine-images).

## On the host ##
### General ###
Always test first, if your host internet connection is working. (ping 8.8.8.8, ping google.com, etc). On your host:

    ping google.com

Check time.

    date

*sudo dpkg-reconfigure -a* must be silent, i.e. not show any errors, must show output at all. Will take a while...

    sudo dpkg-reconfigure -a

*sudo dpkg --configure -a* must be silent, i.e. not show any errors, must show output at all. Will take a while...

    sudo dpkg --configure -a

Get all updates:

    sudo apt-get update
    sudo apt-get dist-upgrade

Check Virtual Box version.

    vboxmanage --version

Get the Tor Browser Bundle from torproject.org and test if it's working.

    # If you can not get the Tor Browser Bundle to work,
    # you will most certainly not get Whonix to work either.
    #
    # In the Whonix Readme it is recommend to have a current
    # copy of the Tor Browser Bundle at all times.
    #
    # The Tor Browser Bundle is great for testing if you live in a
    # censored area or not, if Tor is blocked by your ISP or not.
    # When you need (private) (obfuscated) bridges for the Tor Browser Bundle,
    # you will need them for Whonix as well.

### Import Whonix images ###
Importing the images with the Virtual Box gui should work well in most cases. If not, please check first if you have enough free disk space. Please also refer to the [Whonix Install Screenshot or Video Tutorial](https://sourceforge.net/p/whonix/wiki/Readme/#if-you-need-more-help-with-installing). Also check if the checksums of the ova images match, which is explained at the top of  this page.

Delete any half imported or otherwise broken virtual machine images by using the VBoxManage command line tool. Copy the output.

    VBoxManage unregistervm "Whonix-Workstation" --delete

Go to the folder where you downloaded Whonix. Import Whonix-Workstation by using the VBoxManage command line tool.

    VBoxManage import Whonix-Workstation.ova

Clean (anonymize) the output.

    # Remove operating system user name or any problematic paths.

[Contact Whonix developer](https://sourceforge.net/p/whonix/wiki/Contact/) by sending the output.

    .

## On the Gateway ##
### Login as user ###

Check your `route` command, make sure the network 192.168.0.0 is associated with eth1.

    route

Check if Tor is running with 'pgrep tor -l', this should return something like "103 tor". If not try 'sudo service tor start' and check for any errors.

    pgrep tor -l

Check the status of Tor.

    sudo service tor status | less

Should reply with.

    tor is running.

Restart Tor.

    sudo service tor restart | less

Tor should show only notices, no errors.

Verify Tor configuration is valid:

    sudo tor --verify-config | less

You should see confirmation:

    Configuration was valid

Ping the Whonix-Workstation.

    ping 192.168.0.11

Ping Virtual Box.

    ping 10.0.2.2
    ping 10.0.2.2

Should show *Packet filtered*.

nslookup should NOT work.

    nslookup google.com

Should show timeout.

### Login as unsafe ###
**The following tests might reveal, that you are a Whonix user. Omit them, if that is of concern for you.**

unsafe user account has no password. Login with

    sudo su unsafe

Remove write protection from /etc/resolv.conf

    chattr -i /etc/resolv.conf

Restart networking. DHCP will rewrite /etc/resolv.conf (Temporary login as root.)

    service networking restart

Check /etc/resolv.conf.

    nano /etc/resolv.conf

Content should be:

    nameserver 10.0.2.2

Check if dns resolution is functional.

    nslookup google.com

## Tests on both Virtual Machines ##
Run the following tests on Whonix-Gateway and on Whonix-Workstation.

Check time.

    date

*sudo dpkg-reconfigure -a* must be silent, i.e. not show any errors, must show output at all. Will take a while...

    sudo dpkg-reconfigure -a

*sudo dpkg --configure -a* must be silent, i.e. not show any errors, must show output at all. Will take a while...

    sudo dpkg --configure -a

Test update-grub.

    sudo update-grub

Run 'locale'. Must not report any error.

    locale
    sudo locale

Restart networking:

    sudo service networking restart | less

Apt-get must be fully functional.

    sudo apt-get update
    sudo apt-get dist-upgrade

Test whonixcheck.

    whonixcheck

Test whonixcheck with debugging.

    whonixcheck --verbose

Check the timezone.

    cat /etc/timezone

Must be *Etc/UTC*.

# Advanced users / developers and testers only #
## On Whonix-Gateway and Whonix-Workstation ##

Install dpkg-dev, which is required for dpkg-vendor.

    sudo apt-get install --no-install-recommends dpkg-dev

Run *dpkg-vendor --query vendor*.

    dpkg-vendor --query vendor

The output must be "Whonix".

Check apt config and see if periodic updates are disabled.

    apt-config dump

Install test wise new kernel.

    .

Remove test wise linux-image-486 kernel.

    sudo apt-get remove linux-image-486

Check content of */etc/network/interfaces*.

    nano /etc/network/interfaces

Check content of */etc/resolv.conf*.

    nano /etc/resolv.conf

Check */etc/apt/sources.list*.

    nano /etc/apt/sources.list

Check contents of */etc/resolv.conf*.

    nano /etc/resolv.conf

Check iptables.

    sudo iptables --list | more

### Extra ###
Check if /var/run/bootclockrandomization/success exists.

    nano /var/log/bootclockrandomization.log

    sudo service bootclockrandomization status

    echo $?

Check if /var/run/timesanitycheck/success exists.

    nano /var/log/timesanitycheck.log

    sudo service timesanitycheck status

    echo $?

Check if /var/run/htpdate/success exists

    nano /var/log/htpdate.log

    sudo service htpdate status

    echo $?

## Test on Whonix-Gateway ##
Check the logs.

    less /var/log/tor/log

Test if arm is fully functional.

    sudo arm

Test if arm's new identity function is working.

    .

Install a small text-based browser and torsocks

    sudo apt-get -y install links torsocks ca-certificates

Now use the tools together to connect to the special “testing” site via tor:

    usewithtor links https://check.torproject.org/

You should receive a “Congratulations.  Your browser is configured to use Tor.” message.  If not, there is some issue with the Tor installation or firewall configuration.  Find more information [here on troubleshooting your Tor installation](https://www.torproject.org/docs/tor-doc-unix.html.en#verify). [See documentation on torsocks here.](https://trac.torproject.org/projects/tor/wiki/doc/torsocks)

[See Tor documentation for testing](https://www.torproject.org/docs/tor-doc-unix.html.en#verify).

    .

After logging in you should see Whonix help/welcome/disclaimer message.

    .

## Test Whonix-Workstation ##
### Basics ###
Ping the Whonix-Gateway. Will *NOT* work.

    # You will not be able to ping the Whonix-Gateway,
    # because ICMP is blocked by the firewall.
    # If you want to test it, you have to adjust the firewall,
    # or to deactivate the firewall while testing.
    ping 192.168.0.10

Power off Whonix-Gateway. Try to ping outside or to use the browser in Whonix-Workstation. Obviously, should NOT work.

    .


Power on Whonix-Gateway again. Visit https://check.torproject.org/ with Tor Browser. You should see a “Congratulations”.

    .


Use a Tor Browser to visit a .onion address (Try the [torproject.org hidden service](http://idnxcnkne4qt76tg.onion))

    http://idnxcnkne4qt76tg.onion

Note: Ping commands should NOT work for external addresses from your Whonix-Workstation, [ICMP traffic](http://en.wikipedia.org/wiki/Internet_Control_Message_Protocol) is not proxied, and filtered by /usr/local/bin/whonix_firewall, because Tor does not support UDP. 

    .

**dig google.com** must only return a single IP, compare with the output on Whonix-Gateway or Host.

    dig google.com

Test gpg.

    # Example:
    gpg --keyserver keys.gnupg.net --recv A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89

Test wget uwt wrapper.

    wget http://idnxcnkne4qt76tg.onion

Test wget through TransPort.

    /usr/bin/wget http://idnxcnkne4qt76tg.onion

Setup a hidden service on Whonix-Gateway and test if it works. You can access your own test hidden service using Tor Browser.

    .

See if whonixcheck gets autostarted.

    .


Test XChat, connect to a an SSL protected IRC server.

    .

test XChat, connect to a hidden IRC server.

    .

### Applications ###

* [Metadata]
* [Mixmaster]
* [TorBrowser]

# Footer #
[[include ref=WikiFooter]]