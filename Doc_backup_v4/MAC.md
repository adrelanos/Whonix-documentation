[[include ref=WikiHeader]]

[TOC]

# Introduction

I was trying to sketch a user interface for a MAC changer, fulfilling everything mentioned on https://tails.boum.org/todo/macchanger/

To understand the problem better myself and to make sure we are all talking about the same thing, I thought it may be a good idea to create an overview. Therefore I made a nice table, which is attached below. 

There are so many different threat models and goals, I am not sure it gets too difficult for the average user. For supporting all use cases, the user interface would become giant, just for deciding on which MAC touse.

# use case overview
public computer could be a library.

public network_C could be a free wifi hotspot in a mall.

public network_A, public network_B, public network_D and public network_E could be different coffee houses with free wifi.

number | place | past usage | threat model | new recommendation
------------- | ------------- | ------------- | ------------- | -------------
1 | home computer | real mac | none | macchiato mac random
2 | public computer | real mac | changing mac gets admin attention and/or network breaks | real mac
3 | public network_A | real mac | admin looks for consistent mac | real mac
4 | public network_B | macchanger random mac_B | admin looks for consistent mac, but not for Tor or popular vendor ids | macchanger random mac_B
5 | public network_C | never used | many users, admin logs mac addresses and looks out for unpopular vendor ids | random macchiato mac
6 | public network_D | never used | admin logs mac addresses, looks for unpopular vendor ids, looks for consistent mac | macchiato mac_D
7 | public network_E | never used | admin logs mac addresses, looks for unpopular vendor ids, looks for consistent mac | macchiato mac_E

Legend:

* Consistent mac: always the same after choosing one. Not showing up with a new mac each time.
* macchiato mac random: popular vendor id, latter part varies every time
* macchiato mac_D (or E): popular vendor id, latter part was random when the mac address was first created, after creating macchiato mac_D always get macchiato mac_D when choosing macchiato mac_D

# Or in words...

1. "I am using my home computer, give me a macchiato mac random. I don't really need it, just give it to me. Feel so much better. Just in case."
2. "I am using a public computer, don't change the mac. Otherwise this might bring unwanted admin attention or the network simply gets unaccessible."
3. "I am using public network_A. I always used my real mac in past. The admin knows everyone and gets suspicious if someone changes its mac. Stick to my real mac."
4. "I am in public network_B again, I previously used macchanger to get the random mac_B. The admin looks if I am sticking to that mac, but doesn't know, that the vendor id doesn't even exist. Stick to the old random mac_B."
5. "I am using public network C for the first time. There are many users. I think the admin logs all mac addresses. I also think the admin knows about unpopular vendor ids and gnu macchanger. It's a popular network. The admin however won't remember me or anyone else. Give me a random mac from with a popular vendor id (macchiato)."
6. "I am using public network D for the first time. I think the admin logs mac addresses. I also think the admin looks for unpopular mac addresses and knows gnu macchanger. The admin also get suspicious if someone changes its mac. Give me a random mac with a popular vendor id, call it mac_D and re-use it when I next time visit this network."
7. "Yes, network_E has very similarities with network_D. I think the admin logs mac addresses. I also think the admin looks for unpopular mac addresses and knows gnu macchanger. The admin also get suspicious if someone changes its mac. Give me a random mac with a popular vendor id, call it mac_E and re-use it when I next time visit this network. Don't confuse it with other mac's"

# Thoughts
Supporting use cases 6 and 7 would either require persistence or the user would have to remember or write down the mac address, which is difficult.

An ideal solution doesn't require persistence.

The user enters a word and using that word will result in creating the same macchiato mac_D or macchiato mac_E.

# Footer #
[[include ref=WikiFooter]]