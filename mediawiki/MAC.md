[[include ref=WikiHeader]]

[TOC]

= Introduction =

I was trying to sketch a user interface for a MAC changer, fulfilling everything mentioned on https://tails.boum.org/todo/macchanger/

To understand the problem better myself and to make sure we are all talking about the same thing, I thought it may be a good idea to create an overview. Therefore I made a nice table, which is attached below.

There are so many different threat models and goals, I am not sure it gets too difficult for the average user. For supporting all use cases, the user interface would become giant, just for deciding on which MAC touse.

= use case overview =

public computer could be a library.

public network_C could be a free wifi hotspot in a mall.

public network_A, public network_B, public network_D and public network_E could be different coffee houses with free wifi.

<table>
<thead>
<tr class="header">
<th align="left">number</th>
<th align="left">place</th>
<th align="left">past usage</th>
<th align="left">threat model</th>
<th align="left">new recommendation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">1</td>
<td align="left">home computer</td>
<td align="left">real mac</td>
<td align="left">none</td>
<td align="left">macchiato mac random</td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left">public computer</td>
<td align="left">real mac</td>
<td align="left">changing mac gets admin attention and/or network breaks</td>
<td align="left">real mac</td>
</tr>
<tr class="odd">
<td align="left">3</td>
<td align="left">public network_A</td>
<td align="left">real mac</td>
<td align="left">admin looks for consistent mac</td>
<td align="left">real mac</td>
</tr>
<tr class="even">
<td align="left">4</td>
<td align="left">public network_B</td>
<td align="left">macchanger random mac_B</td>
<td align="left">admin looks for consistent mac, but not for Tor or popular vendor ids</td>
<td align="left">macchanger random mac_B</td>
</tr>
<tr class="odd">
<td align="left">5</td>
<td align="left">public network_C</td>
<td align="left">never used</td>
<td align="left">many users, admin logs mac addresses and looks out for unpopular vendor ids</td>
<td align="left">random macchiato mac</td>
</tr>
<tr class="even">
<td align="left">6</td>
<td align="left">public network_D</td>
<td align="left">never used</td>
<td align="left">admin logs mac addresses, looks for unpopular vendor ids, looks for consistent mac</td>
<td align="left">macchiato mac_D</td>
</tr>
<tr class="odd">
<td align="left">7</td>
<td align="left">public network_E</td>
<td align="left">never used</td>
<td align="left">admin logs mac addresses, looks for unpopular vendor ids, looks for consistent mac</td>
<td align="left">macchiato mac_E</td>
</tr>
</tbody>
</table>

Legend:

* Consistent mac: always the same after choosing one. Not showing up with a new mac each time.
* [https://github.com/EtiennePerot/macchiato macchiato]
* macchiato mac random: popular vendor id, latter part varies every time
* macchiato mac_D (or E): popular vendor id, latter part was random when the mac address was first created, after creating macchiato mac_D always get macchiato mac_D when choosing macchiato mac_D

= Or in words... =

# &quot;I am using my home computer, give me a macchiato mac random. I don't really need it, just give it to me. Feel so much better. Just in case.&quot;
# &quot;I am using a public computer, don't change the mac. Otherwise this might bring unwanted admin attention or the network simply gets unaccessible.&quot;
# &quot;I am using public network_A. I always used my real mac in past. The admin knows everyone and gets suspicious if someone changes its mac. Stick to my real mac.&quot;
# &quot;I am in public network_B again, I previously used macchanger to get the random mac_B. The admin looks if I am sticking to that mac, but doesn't know, that the vendor id doesn't even exist. Stick to the old random mac_B.&quot;
# &quot;I am using public network C for the first time. There are many users. I think the admin logs all mac addresses. I also think the admin knows about unpopular vendor ids and gnu macchanger. It's a popular network. The admin however won't remember me or anyone else. Give me a random mac from with a popular vendor id (macchiato).&quot;
# &quot;I am using public network D for the first time. I think the admin logs mac addresses. I also think the admin looks for unpopular mac addresses and knows gnu macchanger. The admin also get suspicious if someone changes its mac. Give me a random mac with a popular vendor id, call it mac_D and re-use it when I next time visit this network.&quot;
# &quot;Yes, network_E has very similarities with network_D. I think the admin logs mac addresses. I also think the admin looks for unpopular mac addresses and knows gnu macchanger. The admin also get suspicious if someone changes its mac. Give me a random mac with a popular vendor id, call it mac_E and re-use it when I next time visit this network. Don't confuse it with other mac's&quot;

= Thoughts =

Supporting use cases 6 and 7 would either require persistence or the user would have to remember or write down the mac address, which is difficult.

An ideal solution doesn't require persistence.

The user enters a word and using that word will result in creating the same macchiato mac_D or macchiato mac_E.

= Footer =

[[include ref=WikiFooter]]

