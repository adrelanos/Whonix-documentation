[[include ref=WikiHeader]]

[TOC]

# OnionCat #
## Introduction ##
**Untested. Please leave feedback if it worked for you.**

Introduction into OnionCat:

* [torproject wiki about OnionCat](https://trac.torproject.org/projects/tor/wiki/doc/OnionCat) ([w](http://www.webcitation.org/6EQUoe9Cs))
* [cypherpunk.at/onioncat](http://www.cypherpunk.at/onioncat) ([w](http://www.webcitation.org/6EQUqZawz))
* [cryptoanarchy.org about OnionCat](https://cryptoanarchy.org/wiki/OnionCat) <font size="-3">([webarchive](http://web.archive.org/web/20120810015004/https://cryptoanarchy.org/wiki/OnionCat); [webcitation](http://www.webcitation.org/6EQUZky7n))</font>

OnionCat (Tor) might work with Whonix. GarliCat (i2p) might partially work with Whonix.

General debugging hints:

* There at multiple sources for issues, you might stumble upon.
* Therefore it's recommend, before you try using OnionCat with Whonix, if that doesn't endanger you, try first to successfully test OnionCat without Whonix.
* As soon as you learnt that, it eliminated one source for possible issues (OnionCat) and can start learning how to use it with Whonix (which might introduce new issues, but enhanced security will be your reward).
* You also have to learn first, how to use hidden services with Whonix, see [hosting hidden services](https://sourceforge.net/p/whonix/wiki/Hidden%20Services/) for reference.

## Over Tor ##
As long you want to use OnionCat over Tor, it may work.

IPv6 is currently disabled on Whonix-Gateway, because Tor doesn't support IPv6 yet, and we didn't see need for it. We also have no IPv6 firewall for Whonix-Gateway yet, because it's disabled. Anyway, that will be probable no issue. IPv6 on Whonix-Workstation, where OnionCat will be running, is enabled. Since only OnionCat's underlying operating system requires IPv6, but not the Tor process there will be probable no problem. OnionCat on Whonix-Workstation will probable translate the IPv6 requests to IPv4 to the Tor process which is running on Whonix-Gateway. Therefore probable no IPv6 on Whonix-Gateway is required.

There instructions on cryptoanarchy.org look very promising. To use them with Whonix, minor modifications are required. Follow the instructions on [cryptoanarchy.org](https://cryptoanarchy.org/wiki/OnionCat) <font size="-3">([webarchive](http://web.archive.org/web/20120810015004/https://cryptoanarchy.org/wiki/OnionCat); [webcitation](http://www.webcitation.org/6EQUZky7n))</font> but execute the steps on the correct machine, either on Whonix-Gateway or on Whonix-Workstation.

(0). Install ocat <-- on Whonix-Workstation

    sudo apt-get update
    sudo apt-get install onioncat

(1). Create a hidden service <-- on Whonix-Gateway

(2). Create the directory /etc/tor/ocat <-- on Whonix-Gateway

(3). Find the hostname of your hidden service <-- on Whonix-Gateway 
Also possibly see [hosting hidden services](https://sourceforge.net/p/whonix/wiki/Hidden%20Services/) for reference. Debugging: It's recommend to test if your hidden service is reachable first (for example, use test wise a hidden webserver), before you proceed with OnionCat.

(4). Start ocat <-- on Whonix-Workstation

(5). Final nodes. <-- on Whonix-Workstation

## Over i2p ##
GarliCat over i2p might only work, if you use [ip2 over Tor](https://sourceforge.net/p/whonix/wiki/i2p/).

There was the idea to create an [i2pBOX](https://sourceforge.net/p/whonix/wiki/Inspiration/), but it never came to live due to lack of community interest, which means GarliCat directly over i2p will not be supported by Whonix.

As soon as i2p over Tor is working in Whonix-Workstation, you can probable follow the instructions on [cryptoanarchy.org](https://cryptoanarchy.org/wiki/OnionCat) <font size="-3">([webarchive](http://web.archive.org/web/20120810015004/https://cryptoanarchy.org/wiki/OnionCat); [webcitation](http://www.webcitation.org/6EQUZky7n))</font> without modifications.

# Footer #
[[include ref=WikiFooter]]