[[include ref=WikiHeader]]

[TOC]

<!--
Copyright:

Liberte Linux Philosophy page Copyright (C) 2013 Maxim Kammerer <mk at dee dot su>
Whonix E-Mail wiki page Copyright (C) 2013 adrelanos <adrelanos at riseup dot net>

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

The complete text of the GNU General Public License can also be found online on gnu.org <http://www.gnu.org/licenses/gpl-2.0.html>, in Whonix virtual machine images in /usr/share/common-licenses/GPL-2 file or in Whonix wiki on <https://sourceforge.net/p/whonix/wiki/GPLv2/>.
-->

# Introduction #
You can either use Webmail through [TorBrowser] (see below) or Mozilla Thunderbird with TorBirdy. (see below)

None of the solutions is perfect. This is not a Whonix related issue. It is a general issue with e-mail over Tor.

# Threats #
It is often recommend to use mail encryption (enigmail). Yes, that's good. Use it. Remember, as stated on the [Warning] page, subjects are always unencrypted. That's not everything however.

Registering the e-mail address anonymous, i.e. not entering personal data and only accessing it over Tor is a sure thing.

If you have a website or other kind of project, you must publish your e-mail address so others can write.

The e-mail provider is always a single point of failure. If the provider gets pressured, forced or decides not to like your opinion anymore or feels like terminating the service for everyone, the e-mail account can be easily terminated in seconds. This can significantly slow down correspondence. Therefore it's always good to have a few backup e-mail address and alternative communication channels.

Even if subjects are random, hidden, -, empty or misleading and the content is encrypted, the e-mail provider can still log valuable data. When you logged in, how long, how often you fetch mail, how fast you type ^1^, how long you read a message ^1^, which spelling mistakes you make and correct ^1^, to which address mails are send, when you receive mails form which addresses and when. That's quite a lot metadata, which may lead into (false) assumptions by an adversary.

<font size="-3">
^1^ Web mail with javascript enabled only.
</font>

# Encryption #
E-mail encryption is recommend. Mastering e-mail encryption isn't hard, but involves a learning curve. It's outside the scope of this guide, see external documentation.

Documentation:

* [GnuPG documentation](http://www.gnupg.org/documentation/)
* [Enigmail documentation](http://www.enigmail.net/documentation/)
* [KDE upstream KGpg documentation](http://docs.kde.org/stable/en/kdeutils/kgpg/using-kgpg.html)
* [openSUSE KGpg documentation](https://doc.opensuse.org/documentation/html/openSUSE_113/opensuse-apps/cha.crypto.html)
* [OpenPGP key distribution strategies](https://sourceforge.net/p/whonix/wiki/OpenPGP/)
* [OpenPGP Best Practices](https://we.riseup.net/riseuplabs+paow/openpgp-best-practices)

KGpg ([KGpg Homepage](http://utils.kde.org/projects/kgpg/); [KGpg wiki with screenshot](https://en.wikipedia.org/wiki/KGPG)) and GnuPG are pre-installed.

# Webmail #
Many webmail services require JavaScript, display web bugs and you must be careful when receiving attachments.

**TODO**: Expand.

# Mozilla Thunderbird with TorBirdy #
Mozilla Thunderbird (called Icedove in Debian) together with the TorBirdy add-on ([homepage](https://trac.torproject.org/projects/tor/wiki/torbirdy)) ([github]((https://github.com/downloads/ioerror/torbirdy))) can be used as an anonymous (or pseudonymous) e-mail client. TorBirdy is an equivalent of TorButton

The following everything on your Whonix-Workstation.

(1) Install Mozilla Thunderbird (Icedove).

    # For special setups, Ubuntu etc.
    #sudo apt-get install thunderbird

    # Whonix default: in Debian.
    sudo apt-get install icedove

(2) If you like, you can also optionally install [enigmail](http://www.enigmail.net/home/index.php) (A simple interface for OpenPGP email encryption.).

    sudo apt-get install enigmail

Note, TorBirdy issue: as per [Enigmail (OpenPGP GPG for Thunderbird/Icedove)](https://trac.torproject.org/projects/tor/wiki/torbirdy#EnigmailOpenPGPGPGforThunderbird) Enigmail traffic with TorBirdy currently fails.

Whonix users can use GPG command line to get or to push keys from/to keyservers, because GPG in Whonix is already configured safely.

(3) Go to Tools -> Addons -> Plugins -> deactivate all.

(4) Go to Tools -> Addons -> Addons -> deactivate all.

(5) Download the most recent .xpi of [TorBirdy](https://www.torproject.org/dist/torbirdy/) from torproject.org. At time of writing there was a link to the latest version, [torbirdy-current.xpi](https://www.torproject.org/dist/torbirdy/torbirdy-current.xpi).

(6) Also download the corresponding signature. At time of writing there was a link to the latest corresponding signature, [torbirdy-current.xpi.asc](https://www.torproject.org/dist/torbirdy/torbirdy-current.xpi.asc).

(7) Get Jacob Appelbaums GPG key. (Bug: https://trac.torproject.org/projects/tor/ticket/6382)

(8) GPG verify.

    gpg --verify torbirdy-current.xpi.asc torbirdy-current.xpi

Must be "Good Signature".

(9) Go to Thunderbird/Icedove -> Tools -> Addons -> Install Addon from file (button in the upper right) -> choose torbirdy.xpi.

(10) There are no proxy settings required ^1^, because since TorBirdy 0.1.0, TorBirdy natively supports Whonix. ^2^

(11) If you are using enigmail for gpg encryption, it's recommend to check "Always confirm before sending" checked in Enigmail -> Preferences -> Sending.

## Footnotes ##
<font size="-3">
,,
^1^ For [Stream Isolation].
^2^ TorBirdy sets Socks Host to 192.168.0.10 and Port to 9102, if the WHONIX variable is set, which is the default in /etc/environment since Whonix 0.5.5.
</font>

# Remailer - Sending e-mails without registration #
See [Remailer].

# E-Mail Provider Comparison #
## Introduction ##
Adrelanos has been asked whether i2pmail is safer than tormail, riseup, gmail and so on. The *Threats* chapter above states "*e-mail is always a single point of failure*". It doesn't really matter, apart from privacy by policy, no e-mail provider can significantly improve privacy by design. The most important thing about e-mail providers you should ask about e-mail providers is: Will they tolerate me singing up by Tor and exclusively using the e-mail service over Tor? Will they suspend my e-mail account because I speak against someone and they get forced to suspend my account? The latter question is applies more, if you run a project, movement or something like that and less for accounts, which barely anyone knows.

Other than privacy by design, privacy by policy is always a weak protection. An exception might be services, which are not classical e-mail and therefore incompatible, but e-mail alike services such as Usenet (see below), I2P-Bote (see below), RetroShare or TorChat (See [Chat]).

A few frequently discussed mail providers are described above with some facts. There is no recommendation for or against any mail providers.

## tormail.org ##
* Not affiliated with The Tor Project.
* Rumors about being hosted by a secret service. It doesn't really matter, you shouldn't trust mail providers anyway. Assume, anything they can log, they will log forever.
* They technically can not even store Tor exit IP addresses (perhaps mail clients without TorBirdy, put aside) because it's a hidden service.
* Does not work reliable for mailing lists. After a while the user gets unsubscribed because tormail bounces too many mails.
* I haven't heard about any e-mail accounts which got suspended. (Well, I don't know about spam abuse, but that's another story.)
* They are obviously Tor-friendly.
* Things said in the *Threats* chapter still apply.

## i2pmail.org ##
* Quoted from [wikipedia I2P](https://en.wikipedia.org/wiki/I2P): "*I2P has a free pseudonymous e-mail service run by an individual called Postman. Susimail is a web-based e-mail client intended primarily for use with Postman's mail servers, and is designed with security and anonymity in mind. Susimail was created to address privacy concerns in using these servers directly using traditional email clients, such as leaking the user's hostname while communicating with the SMTP server. It is currently included in the default I2P distribution, and can be accessed through the I2P router console web interface. Mail.i2p can contact both i2p email users, via user@mail.i2p and public internet email users from a user@i2pmail.org address.*"
* Cleaning the mail header is nice, but TorBirdy can do the same.
* It's technically impossible to encrypt mails to cleranet addresses ^1^, unless the sender and recipient are using end-to-end encryption such as gpg.
* Therefore it's no more/less secure than using riseup, tormail, etc.
* Even though based on i2p, you can still use it in Whonix over Tor, see [i2p] for information how to tunnel i2p over Tor.
* I haven't heard about any e-mail accounts which got suspended. (Well, I don't know about spam abuse, but that's another story.)
* Things said in the *Threats* chapter still apply.

<font size="-3">
,,
^1^ Such as gmail, riseup etc.
</font>


## I2P-Bote ##
Is not a classical e-mail provider and deserves it's own chapter, see below.

## riseup.net ##
* Recommend by Jacob Appelbaum.
* Works reliable on mailing lists.
* Privacy by policy.
* Tor friendly.
* Servers hosted in the US.
* I haven't heard about any e-mail accounts which got suspended. (Well, I don't know about spam abuse, but that's another story.)
* Things said in the *Threats* chapter still apply.

## gmail ##
* Mike Hearn from Google addressed this issue on [tor-talk](https://lists.torproject.org/pipermail/tor-talk/2012-October/025923.html):

> Access to Google accounts via Tor (or any anonymizing proxy service) is not allowed unless you have established a track record of using those services beforehand. You have several ways to do that:

> 1) With Tor active, log in via the web and answer a security quiz, if any is presented. You may need to receive a code on your phone. If you don't have a phone number on the account the access may be denied.

> 2) Log in via the web without Tor, then activate Tor and log in again WITHOUT clearing cookies. The GAPS cookie on your browser is a large random number that acts as a second factor and will whitelist your access.

> Once we see that your account has a track record of being successfully accessed via Tor the security checks are relaxed and you should be able to use TorBirdy.

* Recommend against. Not Tor friendly. It would be very difficult to sign up using Tor and to exclusively use it over Tor. They most likely ask for phone verification and this is almost impossible to do without jeopardizing anonymity. ^1^

<font size="-3">
,,
^1^ Because they are also aware of online phone and messaging services and blacklisting the for verification upon knowledge.
</font>

# I2P-Bote #
Quoted from [wikipedia I2P](https://en.wikipedia.org/wiki/I2P):

"*I2P-Bote is an I2P-internal, fully decentralized and distributed e-mail system. It supports different identities and does not expose e-mail headers. Currently, it is still alpha software and can only be accessed via its web interface, but POP support is planned. All bote-mails are transparently end-to-end encrypted and, optionally, signed by the sender's public key, thus removing the need for PGP or other privacy software. I2P-Bote offers additional anonymity by allowing for the use of mail relays with variable length delays. As it is decentralized, there is no e-mail server that could link different e-mail identities as communicating with each other (profiling): Even the nodes relaying the mails do not know the sender, and apart from sender and receiver, only the end of the high-latency mail route and the storing nodes will know to whom (which I2P node - the user's ip is still hidden by I2P) the mail is destined. The original sender can have gone offline long before the mail becomes available on the other side.*"

Not yet reviewed by adrelanos, looks promising.

# Usenet #
## Introduction ##
Interesting parts of Usenet other than discussion, include alt.anonymous.messages, Nym servers and Nym server URL Retrieval.

## alt.anonymous.messages ##
alt.anonymous.messages is a public newsgroups supposed to be used to post encrypted and anonymous messages. Getting anonymity and encrypting the messages is up to the user.

It may sound like a disadvantage, but it's an advantage. In comparison, you can never know how many people are using an e-mail provider. Posting in alt.anonymous.messages everyone knows which messages got posted when, but when done right, no one knows who posted a message and what the content of the message is.

Do not use a web service to read individual messages in alt.anonymous.messages. Use an NNTP client (such as Icedove with TorBirdy). Subscribe to the whole newsgroup and download all messages including headers.

Posting to alt.anonymous.messages can be done using Mixmaster and when it's run inside Whonix-Workstation, it's traffic gets routed through Tor beforehand. See the [Mixmaster] article for instructions on using Mixmaster.

Using alt.anonymous.messages could be suspicious by itself, but if you do it right, your adversary may not even know, that you are using it. Since the use of remailer is tunneled through Tor, no one should know, that you are aware of the existence of the remailer network at all.

Further information:

 * [Remailer]
 * [Mixmaster]
 * [Faq](http://www.faqs.org/faqs/privacy/anon-server/faq/use/part7/)

## Nym server protected e-mail inbox ##
Nym server can illustrated as:

    some@mail.sender sends an mail to alice@nymserver.com

    alice@nymserver.com -> mail server A -> mail server B -> ... -> mail server Z -> final@inbox.com

It's a kind of protection, a proxy chain in front of an e-mail inbox.

Or in other words, a Nym server provides an e-mail address, where incoming mails are forwarded through a configurable chain of mail servers ([Remailer]), while not revealing the recipient's inbox to the sender.

This adds several advantages,

 * e-mails can be received, while the e-mail provider is protected from pressure or force of an adversary and
 * where the e-mail provider doesn't necessarily know, where the e-mail address has been published
 * the e-mail provider doesn't know the sender e-mail address and can only see that the recipient became a mail from a remailer

It is my understanding, that the sender's email address will not be known to the recipient, because the remailer will strip it. (Unless the sender specifies it in the text.) However, the one sender of an e-mail is responsible for their own anonymity.

Another question is, if today's remailer really improve security. (See [Anonymity Network] for explanation.)

Further information:

* [Definition - What does Nym Server mean?](http://www.techopedia.com/definition/1696/nym-server)
* [pseudonymous remailer](https://en.wikipedia.org/wiki/Pseudonymous_remailer)
* [Remailer]
* [Mixmaster]
* [Is Not My Name Nymserver](http://www.mixnym.net/)
* [Nym creation and use for mere mortals](http://www.iusmentis.com/technology/remailers/nym.html)
* [paranoia remailer](http://remailer.paranoici.org/nym.php)

Please not, that Whonix developer adrelanos can not answer support requests related to Nym servers. This possibility has just been pointed out and wasn't tested in practice. It's a whole different thing than Whonix and very technical, difficult with many stumble points. Please look for another way, if you need support. Setting up Nym is not Whonix specific. Success stories, use cases, comments, improved documentation etc. however is welcome.

## Nym server URL Retrieval ##
Nym server URL Retrieval is a way to download a web page with high latency and especially when combined with Tor, in theory, safer then Tor alone. In practice, there may be no additional anonymity from today's high latency networks and you could end up being one of the very few people using such, in theory, great services. (For explanation about high latency network anonymity see [Anonymity Network].) Further information on the bottom of [mixnym.net](http://www.mixnym.net/).

Further information:

* [Is Not My Name Nymserver](http://www.mixnym.net/)

Please not, that Whonix developer adrelanos can not answer support requests related to Nym servers. This possibility has just been pointed out and wasn't tested in practice. It's a whole different thing than Whonix and very technical, difficult with many stumble points. Please look for another way, if you need support. Setting up Nym is not Whonix specific. Success stories, use cases, comments, improved documentation etc. however is welcome.

## Discussion ##
Quoted from [Wikipedia](https://en.wikipedia.org/wiki/Usenet): "*Usenet is a worldwide distributed Internet discussion system.*" The wikipedia article is worth reading as an introduction.

There are binary groups and non-binary groups. Whonix itself doesn't restrict access to any of those groups. However, the Tor network is banned by some NNTP servers. Binary groups are not covered here, it will be almost impossible to find a free open NNTP server, allowing access to binary groups.

* [Usenet FAQ](https://groups.google.com/forum/?fromgroups#!forum/news.announce.newusers)

## News Reader ##
You can read news groups either using an NNTP client, such as Icedove (+ TorBirdy) or an online reader such as Google Groups. Posting to usenet using Google Groups is not recommend, it's (almost) impossible or at least very difficult to create an anonymous google account, which is required for posting, because Google requires Tor users to use mobile phone verification, which is not available for anonymous users. Google bans sms to web services as well. I don't know if there are other online hosted NNTP readers, which allow posting for Tor users.

If using newsgroups with Icedove + TorBirdy is safe is still under discussion ([TorBirdy upstream ticket](https://trac.torproject.org/projects/tor/ticket/7847)), but it looks like it's safe.

Mixmaster can be used to post to news groups. When it's in in Whonix-Workstation following the instructions in the [Mixmaster] article, Mixmaster traffic will be even routed through the Tor network.

## NNTP Server ##
An open news server is defined as allowing access to all news discussion groups.

It's difficult to find a free NNTP server even for discussion groups. And no, we are **not** looking for a trial. Use search terms like "free NNTP server". The [nyx.net list](http://www.nyx.net/~bkraft/) may be worth checking, I didn't try any of the servers which require registration. Ideally, the news server supports SSL and does not require registration, such as [aioe](https://www.aioe.org/) or is available as a hidden service. I haven't found any news servers hosted as hidden service, they were all down. While aioe allows reading news groups, it does not allow Tor users to post. I haven't found any open news server allowing Tor users to post. (Use Mixmaster over Tor, see above.)

I haven't got NNTPS (SSL encrypted connection to the NNTP server) to work. [Maybe it is an upstream bug.](https://trac.torproject.org/projects/tor/ticket/8069) This shouldn't be of too much concern. Everything posted to newsgroups is open to the public anyway. An encrypted connection to the NNTP server would only prevent Tor exit nodes and their ISP's to tamper with the traffic, well, and login data (username and password) for password protected NNTP servers could get stolen. The NNTP server is untrusted in this threat model anyway.

# License #
    Liberte Linux Philosophy page Copyright (C) 2013 Maxim Kammerer <mk at dee dot su>
    Whonix Anonymity wiki page Copyright (C) 2013 adrelanos <adrelanos at riseup dot net>

    This program with ABSOLUTELY NO WARRANTY; for details see the wiki source code.
    This is free software, and you are welcome to redistribute it
    under certain conditions; see the wiki source code for details.

# Footer #
[[include ref=WikiFooter]]