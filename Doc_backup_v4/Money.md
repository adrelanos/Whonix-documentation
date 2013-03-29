[[include ref=WikiHeader]]

[TOC]

# General #
**This page is not yet finished! Don't rely on it!**
**Please check if it legal in your legislation before attempting to do it.**
**Please read the whole page, in case you are interested in anonymous money.**

This is a very difficult topic. Should anything be outdated or incorrect, should you have suggestions for improvement, please notify.

Quoted from the [Introduction] page: "*The more you know, the safer and the more anonymous you can be.*" This is even more true here. If you research on your own, you can verify if the information on this page is (still) correct or if new developments changed the situation. With more knowledge you may be able to reach stronger anonymity.

# Legality #
Quoted from [Bitcoin wiki](https://en.bitcoin.it/wiki/Anonymity), <font size="-3">(available under [Creative Commons Attribution 3.0](http://creativecommons.org/licenses/by/3.0/))</font>: "*Obviously, using Bitcoin anonymity techniques for the purposes of [money laundering](http://en.wikipedia.org/wiki/money_laundering) is illegal, but participating or running schemes which others use for money laundering may also be illegal or at least leave the participant vulnerable to accusations of aiding criminals and terrorists. Bitcoin anonymity techniques involving bitcoins worth large amounts of money (over some value between FJ$1,100 and US$58,000, depending on your jurisdiction) is illegal in most jurisdictions, being in violation of [anti-structuring laws](http://en.wikipedia.org/wiki/Structuring).*"

# From Payer perspective #

| Method | Anonymous Registration accepted ^1^ | Usage over Tor allowed ^2^ | Processor can freeze account |
------------- |  ------------- | ------------- | -------------
PayPal | No | No | Yes
Western Union | ? | ? | Yes
Anonymous credit card, Giftcard, Paysafecard, Ukash, etc. | ^a^ ^b^ | ? | ? | Yes
Bitcoin | Yes | Yes | No
Bank transfer | No | No | Yes
Cash by land mail | No | - | No
Meeting in person | No ^c^ ^d^ | No | No

^1^ Accepted as in possible and as in account won't get closed once notified about the account being anonymous. There is no statement about this type of payment being legal in any legislative.
^2^ Or possible. Obviously not possible to use an internet based anonymizer for real world activities such as snail mail or meeting in person.

# From Payee perspective #

| Method | Personal data transferred | Accounting period | Comment |
------------- |  ------------- | ------------- | -------------
PayPal | E-mail address | 5-10 minutes | -
Western Union ^4^	| ? | up to a week | transaction fees
Anonymous credit card, Giftcard, Paysafecard, Ukash, etc. | ^a^ ^b^ | < 1 minute | only €, no $ | -
Liberty Reserve | Account number | < 1 minute |
Bitcoin | ^6^ | ~2 hours | 1 BTC = ~10 €
Bank transfer | Bank account number | 1-3 days | -
Cash by land mail ^3^ | Fingerprint, DNA, handwriting, mail center location | 1-7 days
Meeting in person | ^c^ ^d^ | Needs setting up a meeting. | -

^3^ Please note: Neither third parties are liable for money sent by mail. Do not send registered letters with reply advice.
^4^ Payment by Western Union is possible only for 40 Euro and above. You have to pay the complete transaction fees and it may take up to a week until payment arrives.

<font size="-3">
Thanks to [JonDos](https://anonymous-proxy-servers.net/) ([Permission](https://anonymous-proxy-servers.net/forum/viewtopic.php?p=31220&sid=ac8a6ca16eb768b3322be30b20375c97#p31220)). The "From Payment Receiver perspective" chapter of the Whonix Money wiki page contains content from the [JonDonym payment page](https://shop.anonymous-proxy-servers.net/bin/payment?lang=en).
</font>

# From Payment Processor perspective #

| Method | Personal data | IP address | transaction history |
------------- |  ------------- | ------------- | -------------
PayPal | Yes | Yes | Yes ^7^
Western Union | ? | Yes | Yes ^7^
Anonymous credit card, Giftcard, Paysafecard, Ukash, etc. | ^a^ ^b^ | Yes | Yes ^7^
Liberty Reserve | ? | Yes | Yes ^7^
Bitcoin | ^6^ | Yes | Yes ^8^
Bank transfer | Yes | Yes | Yes ^7^
Cash by land mail | Yes ^5^ | No ^5^ | ?
Meeting in person | ^c^ ^d^ | No | Yes

^5^ ATM registers serial numbers of bank notes, where and when given to whom. Often cameras watch the ATM's. Credit card number is very often tied to card holder data.
^6^ Bitcoin will be discussed in detail below.
^7^ Transaction history, i.e. which account number payed how much, at which point, to whom, is available to the payment processor, law enforcement, tax investigation and who knows to whom else.
^8^ Quoted from [theymos, bitcointalk.org administrator](https://bitcointalk.org/index.php?topic=241.0): "*The history of a coin is publicly available. Anyone can see the flow of BitCoins from address to address.*"

# Footnotes #
^a^ Cash codes are printed once bought and could contain a code tied down to the exact shop location, perhaps date and time. I don't know if that already happens. If so that would be non-anonymous if they also keep camera recordings and/or bought by non-anonymous means (ex: credit card). The country code is already encoded into the cash code of Paysafecard and Ukash. A country code and/or city code already decreases anonymity.
^b^ Anonymous credit cards and gift cards are **not** anonymous if you need to leave your real name and/or address or if you can't buy them with cash. Footnote ^a^ also applies.
^c^ Appearance, clothes, name?, date, time, if using a car: license plate number, etc. 
^d^ If someone can remember your appearance this can not be considered strong anonymity.

# Using prepaid cards #
One can buy prepaid cards at a lot of newspaper stands, gas stations and supermarkets anonymously ^9^ using cash. In Germany there is a limit of 100 €/month due to the [Gesetz über das Kreditwesen (Banking Act)](http://www.gesetze-im-internet.de/kredwg/__25i.html).

Outlets selling cash codes (paysafecard, Ukash etc.) close to you may be found with the "Find sales outlets" search on the website of the provider. In order to a guarantee a smooth and anonymous deployment of cash codes you should consider the following advices:

* Refrain from checking the cash codes before using them. Use the codes immediately. Due to restrictive security settings cash codes are blocked automatically if they are entered from more than one IP address.
* If your cash code got blocked automatically, you could try writing an email to the support of the provider. If you provide a copy of that cash code they may give you a new one which is unblocked.

^9^ Please see the comparison about for further comments on how anonymous it is.

<font size="-3">
Thanks to [JonDos](https://anonymous-proxy-servers.net/) ([Permission](https://anonymous-proxy-servers.net/forum/viewtopic.php?p=31220&sid=ac8a6ca16eb768b3322be30b20375c97#p31220)). The "Using prepaid cards" chapter of the Whonix Money wiki page contains content from the [JonDonym anonymous payment page](https://anonymous-proxy-servers.net/en/help/premium_jondo4.html).
</font>

# Bitcoin #
## Introduction ##
### General ###
Quoted from [Bitcoin.org](http://bitcoin.org/) and [Wikipedia](http://en.wikipedia.org/wiki/Bitcoin): "*Bitcoin is an **experimental**, decentralized digital currency that enables instant payments to anyone, anywhere in the world. Bitcoin uses peer-to-peer technology to operate with no central authority: managing transactions and issuing money are carried out collectively by the network.*"

Without proper precautions paying with Bitcoins is not anonymous. All transactions are saved in a publicly available "eternal logfile". Researchers of the Darmstadt University of Technology have provided an [analysis of Bitcoin's anonymity](http://events.ccc.de/congress/2011/Fahrplan/events/4746.en.html) on the Chaos Communication Congress 2011. Another [analysis](http://eprint.iacr.org/2012/584) was published by D. Ron und A. Shamir. They were able to identify the IP addresses of users and link the different Bitcoin addresses of an account. For an example informations about the Bitcoin usage of Wikileaks were published. Until March 2012 Wikileaks used 83 Bitcoin addresses and got 2605.25 BTC from supporters.

This is only a very short introduction into Bitcoin. It's highly recommend, to learn about Bitcoin in general before attempting to use it anonymously. That could be done for example by reading Wikipedia, Bitcoin website, Bitcoin wiki, Bitcoin forum and maybe some news articles. Additionally to this page it is also recommend reading the sources of this website (at the bottom), especially the [Bitcoin wiki article about anonymity](https://en.bitcoin.it/wiki/Anonymity).

### Clients ###
It is a real pity, that there is no Bitcoin client with graphical user interface in Debian package sources. [The official Bitcoin client](http://bitcoin.org/) however works inside Whonix-Workstation. Downloading and verifying the blockchain unfortunately takes a very long time.

The nonofficial thin client [Electrum.org](http://electrum.org/) (not yet tested by adrelanos) however looks very well and appears to be well designed. It does not need to download/verify the blockchain.

**TODO**: Add instructions to get those clients safely (gpg or form source).

### eWallets ###
There are also webservices to manage your Bitcoins using Tor Browser. **Be careful with Bitcoin webservices / ewallet!** It happened in past that such a service (mybitcoin.com) [got compromised](http://www.tribbleagency.com/?p=8133), all Bitcoin were stolen. Use them only for small amounts you don't care much to loose.

For example [Blockchain](https://www.blockchain.info/wallet) and [StrongCoin](https://www.strongcoin.com/) are offering the administration of an anonymous eWallet on their web servers. Registration at StrongCoin just needs an email address. Access to the wallet is protected by the common combination of username and password. [InstaWallet](https://instawallet.org/) and [EasyWallet.org](https://easywallet.org/) are suited for the administration of smaller amounts. A registration is not necessary. Accessing your eWallet is only possible with a unique link which is generated once you enter InstaWallet's website. There is no password protection. Feel free to look for other services.

<font size="-3">
Thanks to [JonDos](https://anonymous-proxy-servers.net/) ([Permission](https://anonymous-proxy-servers.net/forum/viewtopic.php?p=31220&sid=ac8a6ca16eb768b3322be30b20375c97#p31220)). The "eWallets" chapter of the Whonix Money wiki page contains content from the [JonDonym anonymous payment page](https://anonymous-proxy-servers.net/en/help/premium_jondo4.html).
</font>

## Accepting Bitcoin as Payee ##
Receiving Bitcoin anonymously (strictly speaking, pseudonymous) as a payee alone is quite easy. Just install a Bitcoin client inside Whonix-Workstation (as described in the introduction chapter) and get a Bitcoin wallet up and running. Give the Bitcoin address to the people likely to give money to you, for example if you are running some sort of anonymous website and like people do donate to you, just publish the Bitcoin address.

The payer is responsible for its own anonymity on its own. Some organizations try to increase the privacy of the payer by giving each payer an extra Bitcoin payment address, I can't say if this will improve things much or obfuscate your income better. At least [this](http://www.wired.com/threatlevel/2012/05/fbi-fears-bitcoin/) news source claims FBI said so. It's being discussed controversy. Anyway, the payer should feel responsible for itself when wanting to stay anonymously while paying.

Spending the received Bitcoin anonymously is a whole other story and covered in the following chapters.

## Founding a Bitcoin wallet ##
### General ###
You can either mine Bitcoin or buy them. Both methods are quite difficult to do in a significant amount while staying anonymous.

### Mining ###
Mining Bitcoin needs a lot of computation power and it is my understanding, that solo mining is next to impossible. You would have to join a mining pool (or to create your own). Even if you did, it takes quite some time and/or computation power which also means electricity costs. Mining Bitcoin is not a part of this guide, feel free to research that yourself. Any kind of mining software should be safe in Whonix-Workstation. If that mining software can be made working effectively in a virtual machine is a whole different question, the answer may be yes, but it could be difficult.

### Buying ###
You can also fill your wallet by buying Bitcoin. At the top of this page is a comparison of different non-Bitcoin payment methods. Any of them could theoretically be used to buy Bitcoin from a Bitcoin market. Practically it will be impossible to buy Bitcoin as an anonymous untrusted person with a payment method which can be charged back, due to a significant risk of fraud. Those include (non exclusive list) credit cards and Paypal.

#### Bank Wire Transfer ###
Bank wire transfer can be used to buy Bitcoin, but it's difficult (Impossible? Legally forbidden everywhere?) to open an anonymous bank account.

#### Anonymous credit card, Prepaid Cash Cards ####
Anonymous credit card, Giftcard, Paysafecard, Ukash, etc. could be more anonymous, but be sure to read footnote ^a^ (near the top, you notice when you read from the top to the bottom).

It will be difficult (not impossible) to find an exchange Paysafecard/Ukash for Bitcoin, because Paysafecard stated, that they don't want to be involved into Bitcoin and anonymity services. Also the fees are exorbitant. Search for "paysafecard or ukash Bitcoin exchange" or similar, if you are still interested.

Since the exchanges are not part of the Bitcoin network, you have to ensure that they are legitimate. (And don't take the money and don't send Bitcoin.) It may be safer if you send small amounts until you have enough to lower the risk.

#### Buying with Cash ####
You can buy Bitcoins by cash or send cash by land mail without bank transfer and without leaking name or address to the Bitcoin seller. Please not the comparison about these methods on the top of this page.

* You may use the website [LocalBitcoins.com](https://localbitcoins.com/) to search for contacts of Bitcoin seller near your location and buy Bitcoins via in-person meeting.
* [Bitcoins in Berlin](http://bitcoinsinberlin.com/) accept cash by snail mail or you can buy Bitcoins via in-person meeting in Germany. You have to add the QR code of your Bitcoin address to your cash deposit. This QR code you may create at the website [btc.to](https://btc.to/).
* You may use the IRC channel [#bitcoin-otc](http://bitcoin-otc.com/) in the Freenode network to contact a Bitcoin seller. Offers of sale you may find in the open order book. On IRC you may approach a prospective salesman and negotiate arbitrary methods for the money transfer. A [web interface](http://webchat.freenode.net/?channels=#bitcoin-otc) for the chat is available if you did not like an IRC client like XChat ([Chat] article). There is an option to [register a pseudonym](http://wiki.bitcoin-otc.com/wiki/GPG_authentication) (it is not mandatory, though) which needs an OpenPGP key. As a registered user you may earn reputation. Check the reputation of other users to avoid scam.
* Feel free to look for other services.

<font size="-3">
Thanks to [JonDos](https://anonymous-proxy-servers.net/) ([Permission](https://anonymous-proxy-servers.net/forum/viewtopic.php?p=31220&sid=ac8a6ca16eb768b3322be30b20375c97#p31220)). The "Buying with Cash" chapter of the Whonix Money wiki page contains content from the [JonDonym anonymous payment page](https://anonymous-proxy-servers.net/en/help/premium_jondo4.html).
</font>

### Conclusion ###
While Bitcoin can be accepted anonymously as described above, founding an account anonymously is very difficult, since there are no perfectly anonymous methods to get money into the Bitcoin ecosystem.

By cross reading many forum posts in the Bitcoin forums it looks like many Bitcoin users do not care to be anonymous at all. Others like to be anonymous and use another strategy. They accept, that their payment method to buy Bitcoin, for example bank wire transfer is non-anonymous, but (try) to anonymize their Bitcoin afterwards. This is discussed in the next chapter.

Before using non-anonymous methods, especially bank wire transfer, to purchase Bitcoins, you should consider, that buying Bitcoins, which magically disappeared afterwards, may be alone suspicious enough. Bank statements are being kept long time. It may depend on your location, legislation, the amount of money and your personal threat model, if that is acceptable to you.

## Anonymzing existing Bitcoins ##
(a) One method to anonymize already existing Bitcoins could be to get them out of the Bitcoin eco system and to get them anonymously back into it afterwards. (Not implying that this is easier.) Of course, this only works if it does not matter to you if the existing Bitcoins can get linked to you personally.

(b) Since the methods to purchase Bitcoins with strong anonymity are limited, many people recommend to route them through many Bitcoin exchanges run by different parties. I can't make a statement on how secure that is. In summary various sources say, depends on the amount of money, if the exchange can be trusted, if the exchanges keeps logs, how many people are using the exchange and if you get back your own or different Bitcoins. The [Bitcoin wiki anonymity page](https://en.bitcoin.it/wiki/Anonymity) covers this topic better. You can find discussions about this topic in the Sources chapter on this page.

## Paying Bitcoin ##
This chapter assumes, that you successfully anonymously founded a Bitcoin wallet or that you successfully anonymized existing Bitcoins. Once that is done, not saying the previous steps are easy, not so much is to do. Connection security is already provided, thanks to Whonix-Workstation and Tor. You can anonymously (strictly speaking pseudonymous) send Bitcoin to any other Bitcoin address.

It's important, that you keep care not to de-anonymize yourself by re-using the same Bitcoin address to buy stuff, which can be linked to your person. If you plan on re-using the Bitcoin address to spend the remaining Bitcoins in that wallet, you should read (b) in chapter "Anonymzing existing Bitcoins" above.

## Withdrawing Bitcoin ##
This chapter assumes, the Bitcoins are already anonymized. Either because of anonymously Accepting Bitcoin as Payee (see chapter above) or because because existing Bitcoin were anonymized. (see chapter above)

Buying items and sending them to an address should be safe (assumption valid above) as long as the price isn't to high and doesn't create suspicion. Like always, I can't give you a guarantee, that this is true, but I don't know what I might oversee after reading a lot about this topic. The items you bought could be converted into cash, if you sell them. You have to be careful not to create suspicion as well.

Anonymously cashing out Bitcoin directly into cash looks very difficult. (Impossible, while preserving strong anonymity.) Even thought, Bitcoin can be made more anonymous, when you leave the Bitcoin ecosystem you are left to the conditions of the other payment methods. Have a look again at the top of this page for a comparison of various payment methods to recall their advantages and disadvantages. Cash by land mail (to an anonymous inbox) or meeting in person appears to be most anonymous, but is still far away from strong anonymity.

# Sources #
* https://bitcointalk.org/index.php?topic=241.0
* https://en.bitcoin.it/wiki/Anonymity
* http://arxiv.org/abs/1107.4524
* http://anonymity-in-bitcoin.blogspot.com/2011/07/bitcoin-is-not-anonymous.html
* https://bitcointalk.org/index.php?topic=31539.0
* http://uscyberlabs.com/blog/2012/06/24/government-vs-bitcoin-anonymity/

# Footer #
[[include ref=WikiFooter]]