[[include ref=WikiHeader]]

[TOC]

# About this page #
**This is outdated documentation which no longer applies. Kept in case it it will be required again in future.**

# Updating Tor #
Tor was installed on Whonix according to [official instructions for Ubuntu](https://www.torproject.org/docs/debian#ubuntu). You can update Tor (and the rest of the system) using *apt-get update* and *apt-get dist-upgrade*.

If you run in the following error message when running *apt-get update* on the Gateway...

    W: GPG error: http://deb.torproject.org precise Inrelease: The following signature were invalid: Keyexpired 1346668560

...or into the following error message on the Gateway when running *apt-get dist-upgrade*:

    Warning: The following packages cannot be authenticated!
    deb.torproject.org-keyring tor
    Install these packages without varification?

...please use the workaround below. Please do not install without verification for your own safety!

Temporary fix. Run these two commands. (Check if they are still current and genuine in official instructions for Ubuntu.)

    gpg --keyserver keys.gnupg.net --recv 886DDD89

    gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | sudo apt-key add -

(If they fail for the first time, perhaps because you are on a slow network or slow Tor circuit, run them a few times until the succeed.)

,, Technical problem: The latest Whonix release is a few days ago and in meanwhile there is a new deb.torproject.org-keyring got renewed while the old torproject deb keys expired. Fixing the problem requires a new Whonix release. It will be fixed in 0.3.0.

# VirtualBox Guest Additions #
## Introduction ##
Written and tested with Whonix 0.2.1 (Ubuntu precise). Many things can go wrong and none or the very least of them will be caused by Whonix. This has only limited support by the Whonix developers, because 1. it's not recommend, for security reasons and 2. the guest additions related bugs and instructions are somewhat out of the scope of the Whonix project.

Installation is somewhat difficult and no packages exist. Just search the internet and you'll see, that loads of people having issues installing the VirtualBox guest additions. People having problems for years. VMware is of no alternative, people are also having trouble installing the VMware tools into Linux guests. The issue with the guest additions is ridiculous. For years no solution has been found. With each kernel update, recompilation is required, and quite often, due to some updates, complication becomes difficult or impossible for a long time.

Also see article, [The VirtualBox Kernel Driver Is Tainted Crap](http://www.phoronix.com/scan.php?page#news_item&px#OTk5Mw).

If you are having trouble, than in most cases not because of Whonix. The Whonix setup is a regular Ubuntu Linux and VirtualBox. You can try asking the regular VirtualBox and Ubuntu resources if you have trouble.

# TorChat source package #
## HowTo ##
**EXPERIMENTAL** Experimental as in it is difficult to install. Only use it in case you trust TorChat. There shouldn't be any anonymity leaks and it should be as safe as other hidden services in general and in Whonix.

Learn about [Hidden Services](https://sourceforge.net/p/whonix/wiki/Hidden%20Services/) in Whonix first and learn how to set up the hidden webserver. This will ease following this guide.

On Whonix-Gateway.

Open torrc.

    sudo nano /etc/tor/torrc

Add.

    HiddenServiceDir /var/lib/tor/torchat_service/
    HiddenServicePort 11009 192.168.0.11:11009

Save. Reload Tor.

    sudo service tor reload

On Whonix-Gateway.

Install dependencies.

    sudo apt-get install python python-wxgtk2.8

Get your onion address.

    nano /var/lib/tor/torchat_service/hostname

Backup your key, if you want to ever restore it one another machine, a newer Whonix-Workstation or after hdd failure.

    /var/lib/tor/torchat_service/private_key

Download the latest Python version of TorChat source code, for example as time of writing torchat-source-0.9.9.553.zip - Python source code (classic standalone 0.9.9 version) from (https://github.com/prof7bit/TorChat/downloads) and store it in */home/user*.

Unpack.

    unzip torchat-source-0.9.9.553.zip

Get into the torchat source folder. For example.

    cd /home/user/torchat-source-0.9.9.553/

Get into the src folder.

    cd src

Get into the Tor folder.

    cd Tor

Rename tor.sh.

    mv tor.sh backup_tor.sh

Go back to the src folder.

    cd ..

Create torchat.ini.

    nano torchat.ini

Add the following content.

    [client]
    listen_interface = 192.168.0.11
    listen_port = 11009
    own_hostname = <your onion hostname without .onion>

    [tor]
    tor_server = 192.168.0.10
    tor_server_control_port = 9154
    tor_server_socks_port = 9154

    [tor_portable]
    tor_server = 192.168.0.10
    tor_server_control_port = 9154
    tor_server_socks_port = 9154

Make torchat executable.

    chmod +x torchat.py

Run torchat.

    ./torchat

### Alternative ###
After installing the dependencies we could also force install the torchat deb package.

    sudo dpkg -i --force-depends torchat-0.9.9.553.deb

And then configure the files inside */home/user/.torchat*. I don't know if that may be the better way.

# Mixmaster #
## MX capable DNS resolver ##
No longer required.

<font size="-3">
Mixmaster needs to resolve MX DNS records, [while Tor does not support that](https://trac.torproject.org/projects/tor/ticket/7829). We have to install a DNS resolver capable of doing that. It still comes with caveats.

Required knowledge:

* Introduction chapter of [Secondary DNS Resolver](https://sourceforge.net/p/whonix/wiki/Secondary%20DNS%20Resolver/)

The [Example with CZ.NIC Labs DNS resolver](https://sourceforge.net/p/whonix/wiki/Secondary%20DNS%20Resolver/#example-with-cznic-labs-dns-resolver) worked in this case.
</font>

<font size=-3>
Security considerations when replacing the system wide DNS resolver:

* The third party DNS resolver traffic goes through it's own circuit, which is good.
* All (custom installed) applications not configured to use a SocksPort (see [Stream Isolation]), would resolve their DNS through the system wide DNS resolver, which would be the third party resolver, giving too much power to it, because it's always the same, only one service provider, not changing like Tor circuits but static.
</font>
## Install Postfix ##

    sudo apt-get install postfix
    ## configure postfix as sattelite system, default settings

<font size=-3>Technical background:
Mixmaster requires either
- a) An (open) smtp server SMTPRELAY in */etc/mixmaster/remailer.conf*. Unfortunately, I haven't found any open smtp server (search term: open relay). A mailserver where the user registers first would probable work, but this would defeat the original idea: sending e-mails without depending on registration. Or,
- b) a mta (mail transfer agent), which speaks to the remailer directly. **TODO**: Are there enough Tor exit nodes, which allow the SMTP port and does their ISP allow to speak SMTP? If there are too few servers, it could be bad for anonymity.
</font>

Open */etc/postfix/main.cf*.

    kdesudo leafpad /etc/postfix/main.cf

Replace the content with the following.

    # See /usr/share/postfix/main.cf.dist for a commented, more complete version


    # Debian specific:  Specifying a file name will cause the first
    # line of that file to be used as the name.  The Debian default
    # is /etc/mailname.
    #myorigin = /etc/mailname

    smtpd_banner = $myhostname ESMTP $mail_name (Debian/GNU)
    biff = no

    # appending .domain is the MUA's job.
    append_dot_mydomain = no

    # Uncomment the next line to generate "delayed mail" warnings
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
    #relayhost = 2.2.2.2

## Debugging Postfix ##
Looking into the mail log.

    tail -f /var/log/mail.info

Should contain something like this.

    <date> <time> debian postfix/pickup[id]: id2: uid=1000 from=<user>
    <date> <time> debian postfix/cleanup[id]: id2: message-id=<id3.id4@host.localdomain>
    <date> <time> debian postfix/qmgr[id]: id2: from=<user@host.localdomain>, size=30000, nrcpt=1 (queue active)
    <date> <time> debian postfix/smtp[300]: id2: to=<remailer@breaka.net>, relay=mail.breaka.net[202.75.54.8]:25, delay=30, delays=0.30/0.01/30/3.0, dsn=2.0.0, status=sent (250 OK id=id5-id6-id7)
    <date> <time> debian postfix/qmgr[id]: id2: removed

Reading local mail.

    ## Either with cli tool mail.
    mail

    ## Or using gui tool Icedove (Debian version of Mozilla Thunderbird)
    ## using movemail.

If all went well, there will be no local mail. Only error messages result in local mails.

# Bugs #
* In Whonix 0.4.5, due to a [Tor Browser upstream bug](https://trac.torproject.org/projects/tor/ticket/7668) (they forgot to update the changelog) and because the keyserver is/was down, the torbrowser and whonixcheck script in Whonix can no longer find out which Tor Browser version is locally installed. ([Whonix Bug Report](https://sourceforge.net/p/whonix/discussion/general/thread/6122990d/)) The [Update Tor Browser](https://sourceforge.net/p/whonix/wiki/TorBrowser/#update-tor-browser) chapter contains a workaround and a fix is available for testers.

# Attack matrix in different order #

attack | TBB | TBB in a VM | Tails | Tails in a VM | Whonix Standard Download version host+vm+vm | Whonix Physical Isolation
------------- |  ------------- | ------------- | ------------- | ------------- | ------------- | -------------
(1) Protocol IP leak | fail | fail | fail | fail | safe | safe
(2) exploit + Unsafe Browser | fail | fail | fail | fail | safe | safe
(3) exploit + root exploit + Unsafe Browser | fail | fail | fail | fail | safe | safe
(4) root exploit + Unsafe Browser | fail | fail | fail | fail | safe | safe
(5) exploit + vm exploit + Unsafe Browser | fail | fail | fail | fail | fail | safe
(6) exploit + vm exploit + exploit against physically isolated Whonix-Gateway | fail | fail | fail | fail | fail | fail
(7) vm exploit | safe | fail | safe | fail | fail | safe
(8) vm exploit + exploit against physically isolated Whonix-Gateway | safe | fail | safe | fail | fail | fail
(9) exploit against Tor process | fail | fail | fail | fail | fail | fail
(10) attack against the Tor network | fail | fail | fail | fail | fail | fail

# E-Mail Notification #
Users, who have an (anonymous) sourceforge.net account, could go to the [Whonix sf.net Project Page](https://sourceforge.net/projects/whonix/), scroll down to *Update Notifications* and hit the *Subscribe to Updates* button. They would receive notifications about new releases sent to their (anonymous) [E-Mail] address.

<font size="-3">
There is currently no way for users to subscribe to sf.net blogs or wiki, but such a feature [has been requested](https://sourceforge.net/p/allura/tickets/5702/).
</font>

## Sourceforge.net E-Mail Notification ##
Didn't work reliable.

E-mail notification: For users having an account on sf.net, there is on [sf.net](https://sourceforge.net/p/whonix/code/) git is an [E-Mail] subscribe button: **M**.

This is an example how such a mail could look like:

*experimental: comment by adrelanos http://sourceforge.net/p/whonix/code/ci/a1740dfcd391cedfa625d72b990b2a587620df30/*

*experimental: Whonix-Workstation_packages: added gtk3-engines-oxygen by adrelanos http://sourceforge.net/p/whonix/code/ci/7375070a7986230028bf4e82a6ab3ecb420bfd60/*

*---*

*Sent from sourceforge.net because you indicated interest in <https://sourceforge.net/p/whonix/code/>*

*To unsubscribe from further messages, please visit <https://sourceforge.net/auth/prefs/>*

# Footer #
[[include ref=WikiFooter]]