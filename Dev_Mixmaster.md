[[include ref=WikiHeader]]

[TOC]

# Mixmaster #
## Introduction ##
Motivation behind this:
"*What if there where a bookmark pointing to mail.local (or something like that) where you can simply enter an e-mail address, from sender (optional), subject and text, click send and mail is on it's way?*

*No sign-up/registration/smtp server required. Could look like [this](https://www.awxcnx.de/mm-anon-email.htm). (Or [this](https://www.cotse.net/cgi-bin/mixmail.cgi) or [this](https://webmixmaster.paranoici.org/mixemail-user.cgi).)*" ([Development discussion](https://mailman.boum.org/pipermail/tails-dev/2012-December/002384.html))

[Mixmaster](https://en.wikipedia.org/wiki/Mixmaster_anonymous_remailer) is a Remailer. Please read the [Remailer] article first as introduction.

There are two ways of using the Mixmaster network. Installing mixmaster in Debian, which is recommend but more difficult. Unfortunately, there is no nice graphical user interface for the Mixmaster for Debian GNU/Linux. There are web interfaces at the bottom of this page, I don't know yet how to use them.

This is quite an unusual setup. At time of writing there where no references that ever anyone ever successfully used the mixmaster software to remail over Tor. Therefore it might make clear, that you are a Whonix user.

## Mixmaster inside Whonix-Workstation ##
### Third Party Information ###
#### Tutorial Videos ####
There is a video without speech on Ubuntu, but steps on Debian are the same. No speech, but good video anyway.

* https://www.youtube.com/watch?v=jmIHcrrkj2w

There is also a video with speech explaining Mixmaster. Video comments:

* Before 4:38 min he explains general things about Mixmaster. I don't agree, for reasons explained above. The video is already four years old.
* Before 4:38 min he explains to manually install it. We don't have to do it, since it's available as Debian package.
* You could watch https://www.youtube.com/dzbrFPO4604 beginning from 4:38 min.

#### Documentation ####
debian-administration.org: [Using mixmaster to send anonymous email](http://www.debian-administration.org/articles/483) from 2006 written by Jacob Appelbaum. Still contains useful information. <font size="-3"Even though */etc/mixmaster/remailer.conf* contains a *SENDMAIL* directive, a [Mixmaster Tutorial Third](http://www.plex86.org/linux2/Mixmaster-Tutorial-Third-Draft-Comments--This-message-did-not-originate-from-the-Sender-address-above.html) says Postfix is Mixmaster default. This directive does not required changing.</font>

### Installing ###
#### Installation ####
##### Whonix-Gateway #####
/etc/tor/torrc contains.

    mapaddress 1.1.1.1 k54ids7luh523dbi.onion
    mapaddress 2.2.2.2 gbhpq7eihle4btsn.onion

##### Whonix-Workstation #####
Has mixmaster installed by default.

/home/user/.Mix/mix.cfg contains.

    #SMTPRELAY      1.1.1.1
    SMTPRELAY       2.2.2.2

/etc/hostname contains.

    host

/etc/hosts contains.

    127.0.0.1 host.localdomain host

This is because mixmaster leaks these information to the mixmaster node, it's better to have it uniform.

### Configuration ###
A fresh list of Mixmaster nodes is required. You can either update using the ncurses interface or using the Debian method. Both are documented below.

#### ncurses method ####
In Terminal:

    sudo mixmaster

    ## Press keys:
    # 1
    u      for update
    # 2
    *      to begin update
    # 3
    k      worked for me 
    # 4
    q      for quit (no longer run it as root)

#### Debian method ####

    sudo mixmaster-update --verbose 

There is an exception in */etc/sudoers* for mixmaster-update to allow running mixmaster-update without root.

### Using ###
In Terminal:

    mixmaster

and use the text interface. Perhaps watch the video as explained above.

If you don't like the text interface you may use it by command line. If you want to read the manual.

    man mixmaster

Mails can also be send by command line. See documentation article [Mixmaster] for instructions how to use it.

### Debugging ###
After sending when there is no error.

    Chain: breaka

Error example.

    Error: SMTP relay not ready. 
    Error: SMTP relay not ready. 
    Error: Unable to execute sendmail. Check path!
    Error: SMTP relay not ready. 
    Error: SMTP relay not ready. 
    Error: Unable to execute sendmail. Check path!

## Webinterface ##
http://remailer.paranoici.org/scripts/webscripts.tar.gz

 * Online demo looks good.
 * GNUPL license needs clarification.

http://www.cotse.net/mixweb.tgz

 * Online demo looks good.
 * Unfree license. Only free for non-commercial use. Although there is a promise not to sue one, commercial users are required to buy a license.
 * Therefore not suited as default in Whonix.

http://pyanon.sourceforge.net

 * Looks great.
 * Requires Apache 2 with mod_python.
 * Therefore not suited as default in Whonix. (Users may want to use Apache for running a hidden service. Also quite big. Might be re-considered.)

## Development ##
Note: Mixmaster gets confused if there are # comments at the top of *~/.Mix/mix.cfg*.

[Stream Isolation] as in forcing Mixmaster traffic through a separate SocksPort has not yet been figured out and help is welcome. Mixmaster traffic goes through Tor's TransPort. Since we are only connecting to Mixmaster relays, which provide a hidden service, identity correlation should be prevented. To make sure, asked [tor-talk: Are connections to two different hidden services stream isolated?](https://lists.torproject.org/pipermail/tor-talk/2013-January/027116.html).

Other ideas:

 * Postfix has an option to skip MX lookups for a given hostname: look for "square brackets" in postconf(5).
 * [Using Postfix with Tor](http://www.groovy.net/ww/2011/12/torfix)
 * [Using Postfix with Tor (bis)](http://www.groovy.net/ww/2012/01/torfixbis)

The [Deprecated] page contains information related to Mixmaster: MX DNS requests, MX capable DNS resolver, using Postfix and debugging Postfix.

## Credits ##
* [Remops mailing list](http://lists.mixmin.net/pipermail/remops/2012-December/000671.html) helped creating this page with advice.

# Footer #
[[include ref=WikiFooter]]