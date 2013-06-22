[[include ref=WikiHeader]]

[TOC]

= Hosting Location/IP Hidden Servers =

== Introduction ==

If you are only interested in Tor hidden services, move on to [Hidden Services]. This page discusses and compares different kinds of Location/IP Hidden Servers.

There are three different ways to run location hidden servers. Tor Hidden Services, pagekite. .onion webspace and Anonymous Third Party Hosts. Below is an overview.

If you don't know which one to use, probable Tor Hidden Services are most easy and most anonymous. Below is also a conclusion and a comparison table.

== Tor Hidden Services ==

* 99% of this page is about Tor Hidden Services,
* censor resistant, no one can take the .onion domain offline <sup>1</sup>,
* additionally accessible over tor2web over http <sup>2</sup>
* they are completely free
* no sign up required
* and don't require any additional software besides of course the server software you want to anonymize.
* Can be run at home; on any server you physically own; or on (anonymous) third party hosts.
* Has it's own wiki page, see [Hidden Services].

<font size="-3"> ,, <sup>1</sup> Besides hack (crack) and flood attack. <sup>2</sup> Which doesn't offer as much censor resistance as the .onion domain does. </font>

== pagekite ==

* alternative service called [https://pagekite.net/ pagekite]
* must comply with [https://pagekite.net/humans.txt pagekite terms of service]
* requires registration and an (anonymous) [E-Mail] address
* free for Free Software authors; can apply for a free account; or subscription based service
* known to work inside Whonix-Workstation out of the box
* less tested by Whonix developers
* there is no documentation besides this chapter, however, usage is simple and their service is well documented. See [https://pagekite.net/wiki/Howto/PageKiteOverTor/ Running PageKite over Tor].
** Instead of localhost you could use the Whonix-Gateway IP 192.168.0.10 and a custom port such as 9159, i.e. replace &quot;''--torify=localhost:9050''&quot; with &quot;''--torify=192.168.0.10:9159''&quot;.
** Or you could drop the &quot;''--torify''&quot; switch at all and even follow the default pagekite GNU/Linux tutorial, because ''misc traffic'' in Whonix-Workstation gets automatically routed through Tor's TransPort.
** See [Stream Isolation] for an explanation of ''misc traffic'', custom Socks Ports and Tor's TransPort in Whonix.

== Anonymous Third Party Hosts ==

* Has it's own wiki page, see [Hosting].
* There are some free .onion web hosting services. Also paid ones.
* There are also anonymous VPS servers, although no free ones, which would require [https://sourceforge.net/p/whonix/wiki/Money/ anonymous money].

== Conclusion ==

Each way to run location hidden servers has it's own advantages and disadvantages.

With Tor Hidden Services, you don't have to learn and obtain anonymous money, which is difficult on it's own. You have to trust no one, but your own skills setting up a server. No one can censor the server, there is no signup, no terms of service. Disadvantage is, if someone compromises your hidden service either by an successful attack against Tor hidden services are by an successful attack against your server software and breaking out of Whonix, it's game over. It's only accessible over .onion (visitors need Tor) and tor2web does not get indexed by search engines. Tor Hidden Services are only online as long as your server is online.

A free (or paid) .onion web space host can steal your domain any time and take it over. You don't have to worry about server security and successful attacks against the Tor hidden services won't lead to your location or IP address.

Anonymous Third Party Hosts for VPS hosting involve anonymous money, which is difficult on it's own. They can provide clearnet domains and/or you can use them to host Tor hidden services. You don't have to worry about server security and successful attacks against Tor hidden services won't lead to your location or IP address.

== Comparison Table ==

<table>
<thead>
<tr class="header">
<th align="left"></th>
<th align="left">Tor Hidden Services</th>
<th align="left">pagekite</th>
<th align="left">.onion webspace</th>
<th align="left">Anonymous Third Party Hosts</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">accessible over Tor .onion</td>
<td align="left">Yes</td>
<td align="left">No</td>
<td align="left">Yes</td>
<td align="left">Yes, if you install Tor.</td>
</tr>
<tr class="even">
<td align="left">.onion domain censor resistance</td>
<td align="left">Highest</td>
<td align="left">There is no .onion domain.</td>
<td align="left">Depends on .onion webspace host. <sup>6</sup></td>
<td align="left">Depends on Anonymous Third Party Hosts. <sup>6</sup></td>
</tr>
<tr class="odd">
<td align="left">server admin can take away your .onion domain</td>
<td align="left">No, you are the admin.</td>
<td align="left">There is no .onion domain.</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
</tr>
<tr class="even">
<td align="left">accessible over clearnet http(s)</td>
<td align="left">tor2web only</td>
<td align="left">Yes</td>
<td align="left">tor2web only</td>
<td align="left">Yes <sup>1</sup></td>
</tr>
<tr class="odd">
<td align="left">clearnet domain censor resistance</td>
<td align="left">Depends on tor2web legislative.</td>
<td align="left">Depends on pagekite legislative.</td>
<td align="left">Depends on tor2web legislative.</td>
<td align="left">Depends on Anonymous Third Party Hosts legislative.</td>
</tr>
<tr class="even">
<td align="left">server admin can take away your clearnet domain</td>
<td align="left">Yes, tor2web can. <sup>5</sup></td>
<td align="left">Yes <sup>5</sup></td>
<td align="left">Yes, tor2web can. <sup>5</sup></td>
<td align="left">Yes <sup>5</sup></td>
</tr>
<tr class="odd">
<td align="left">other services than web</td>
<td align="left">Yes</td>
<td align="left">Yes</td>
<td align="left">No</td>
<td align="left">Yes</td>
</tr>
<tr class="even">
<td align="left">price</td>
<td align="left">Free</td>
<td align="left">Depends</td>
<td align="left">Some are free</td>
<td align="left">Paid only</td>
</tr>
<tr class="odd">
<td align="left">requires anonymous money</td>
<td align="left">No</td>
<td align="left">Depends</td>
<td align="left">Depends</td>
<td align="left">Yes</td>
</tr>
<tr class="even">
<td align="left">no need to sign up</td>
<td align="left">Yes</td>
<td align="left">No</td>
<td align="left">No</td>
<td align="left">No</td>
</tr>
<tr class="odd">
<td align="left">always online</td>
<td align="left">As long as your server is online.</td>
<td align="left">As long as your server is online.</td>
<td align="left">Yes <sup>2</sup></td>
<td align="left">Yes <sup>2</sup></td>
</tr>
<tr class="even">
<td align="left">attack against Tor (hidden services)</td>
<td align="left">Fail <sup>3</sup></td>
<td align="left">Fail <sup>3</sup></td>
<td align="left">Safe <sup>4</sup></td>
<td align="left">Safe <sup>4</sup></td>
</tr>
<tr class="odd">
<td align="left">attack against server software (lighttpd, etc.)</td>
<td align="left">Fail <sup>3</sup></td>
<td align="left">Fail <sup>3</sup></td>
<td align="left">Safe <sup>4</sup></td>
<td align="left">Safe <sup>4</sup></td>
</tr>
<tr class="even">
<td align="left">further reading</td>
<td align="left">[https://sourceforge.net/p/whonix/wiki/Hidden%20Services/ Tor Hidden Services]</td>
<td align="left">[https://pagekite.net/ pagekite]</td>
<td align="left">[https://sourceforge.net/p/whonix/wiki/Hosting/ Anonymous Third Party Hosts]</td>
<td align="left">[https://sourceforge.net/p/whonix/wiki/Hosting/ Anonymous Third Party Hosts]</td>
</tr>
</tbody>
</table>

<font size="-3"> ,, <sup>1</sup> Yes, if you buy a domain. <sup>2</sup> Besides server downtime, in which case you can do nothing but wait until the host has fixed it. <sup>3</sup> Fail as in, it would deanonymize you. <sup>4</sup> Safe as in, you are still anonymous. The domain may be lost. <sup>5</sup> They must do so, if they are forced by legislation or other reasons. <sup>6</sup> The admin can and will most likely do what users are doing on their server and decide accordingly. </font>

= Footer =

[[include ref=WikiFooter]]

