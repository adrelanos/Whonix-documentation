[[include ref=WikiHeader]]

[TOC]

# Hosting Location/IP Hidden Servers
## Introduction
If you are only interested in Tor hidden services, move on to [Hidden Services]. This page discusses and compares different kinds of Location/IP Hidden Servers.

There are three different ways to run location hidden servers. Tor Hidden Services, pagekite. .onion webspace and Anonymous Third Party Hosts. Below is an overview.

If you don't know which one to use, probable Tor Hidden Services are most easy and most anonymous. Below is also a conclusion and a comparison table.

## Tor Hidden Services
* 99% of this page is about Tor Hidden Services,
* censor resistant, no one can take the .onion domain offline ^1^,
* additionally accessible over tor2web over http ^2^
* they are completely free
* no sign up required
* and don't require any additional software besides of course the server software you want to anonymize.
* Can be run at home; on any server you physically own; or on (anonymous) third party hosts.
* Has it's own wiki page, see [Hidden Services].

<font size="-3">
,,
^1^ Besides hack (crack) and flood attack.
^2^ Which doesn't offer as much censor resistance as the .onion domain does.
</font>

## pagekite
* alternative service called [pagekite](https://pagekite.net/)
* must comply with [pagekite terms of service](https://pagekite.net/humans.txt)
* requires registration and an (anonymous) [E-Mail] address
* free for Free Software authors; can apply for a free account; or subscription based service
* known to work inside Whonix-Workstation out of the box
* less tested by Whonix developers 
* there is no documentation besides this chapter, however, usage is simple and their service is well documented. See [Running PageKite over Tor](https://pagekite.net/wiki/Howto/PageKiteOverTor/).
    * Instead of localhost you could use the Whonix-Gateway IP 192.168.0.10 and a custom port such as 9159, i.e. replace "*--torify=localhost:9050*" with "*--torify=192.168.0.10:9159*".
    * Or you could drop the "*--torify*" switch at all and even follow the default pagekite GNU/Linux tutorial, because *misc traffic* in Whonix-Workstation gets automatically routed through Tor's TransPort.
    * See [Stream Isolation] for an explanation of *misc traffic*, custom Socks Ports and Tor's TransPort in Whonix.

## Anonymous Third Party Hosts
* Has it's own wiki page, see [Hosting].
* There are some free .onion web hosting services. Also paid ones.
* There are also anonymous VPS servers, although no free ones, which would require [anonymous money](https://sourceforge.net/p/whonix/wiki/Money/).

## Conclusion
Each way to run location hidden servers has it's own advantages and disadvantages.

With Tor Hidden Services, you don't have to learn and obtain anonymous money, which is difficult on it's own. You have to trust no one, but your own skills setting up a server. No one can censor the server, there is no signup, no terms of service. Disadvantage is, if someone compromises your hidden service either by an successful attack against Tor hidden services are by an successful attack against your server software and breaking out of Whonix, it's game over. It's only accessible over .onion (visitors need Tor) and tor2web does not get indexed by search engines. Tor Hidden Services are only online as long as your server is online.

A free (or paid) .onion web space host can steal your domain any time and take it over. You don't have to worry about server security and successful attacks against the Tor hidden services won't lead to your location or IP address.

Anonymous Third Party Hosts for VPS hosting involve anonymous money, which is difficult on it's own. They can provide clearnet domains and/or you can use them to host Tor hidden services. You don't have to worry about server security and successful attacks against Tor hidden services won't lead to your location or IP address.

## Comparison Table

| | Tor Hidden Services | pagekite | .onion webspace | Anonymous Third Party Hosts
------------- |  ------------- | ------------- | ------------- | -------------
accessible over Tor .onion | Yes | No | Yes | Yes, if you install Tor.
.onion domain censor resistance | Highest | There is no .onion domain. | Depends on .onion webspace host. ^6^ | Depends on Anonymous Third Party Hosts. ^6^
server admin can take away your .onion domain | No, you are the admin. | There is no .onion domain. | Yes | Yes
accessible over clearnet http(s) | tor2web only | Yes | tor2web only | Yes ^1^
clearnet domain censor resistance | Depends on tor2web legislative. | Depends on pagekite legislative. | Depends on tor2web legislative. | Depends on Anonymous Third Party Hosts legislative.
server admin can take away your clearnet domain | Yes, tor2web can. ^5^ | Yes ^5^ | Yes, tor2web can. ^5^ | Yes ^5^
other services than web | Yes | Yes | No | Yes
price | Free | Depends | Some are free | Paid only
requires anonymous money | No | Depends | Depends | Yes
no need to sign up | Yes | No | No | No
always online | As long as your server is online. | As long as your server is online. | Yes ^2^ | Yes ^2^
attack against Tor (hidden services) | Fail ^3^ | Fail ^3^ | Safe ^4^ | Safe ^4^
attack against server software (lighttpd, etc.) | Fail ^3^ | Fail ^3^ | Safe ^4^ | Safe ^4^
further reading | [Tor Hidden Services](https://sourceforge.net/p/whonix/wiki/Hidden%20Services/) | [pagekite](https://pagekite.net/) | [Anonymous Third Party Hosts](https://sourceforge.net/p/whonix/wiki/Hosting/) | [Anonymous Third Party Hosts](https://sourceforge.net/p/whonix/wiki/Hosting/)

<font size="-3">
,,
^1^ Yes, if you buy a domain.
^2^ Besides server downtime, in which case you can do nothing but wait until the host has fixed it.
^3^ Fail as in, it would deanonymize you.
^4^ Safe as in, you are still anonymous. The domain may be lost.
^5^ They must do so, if they are forced by legislation or other reasons.
^6^ The admin can and will most likely do what users are doing on their server and decide accordingly.
</font>

# Footer #
[[include ref=WikiFooter]]