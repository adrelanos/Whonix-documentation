[[include ref=WikiHeader]]

[TOC]

# Remailer #
## Introduction ##
Quoted from the Wikipedia [Anonymous remailer article](https://en.wikipedia.org/wiki/Anonymous_remailer):
"*An anonymous remailer is a server that receives messages with embedded instructions on where to send them next, and that forwards them without revealing where they originally came from.*"

In Whonix-Workstation, remailers can be used over Tor. Not with the goal to offer even more anonymity for (web) e-mails than Tor could provide, just as a cheap tool to send mails without registration.

In theory, remailers or to be more concrete, high latency networks are more secure than low latency networks like Tor. If you are interested in this, please see [Anonymity Network]. The anonymity provided by the remailer would add up to the anonymity provided by Tor. Given the facts, the there is almost no activity activity (press, blog posts, forum, mailing list discussion, development ceased) it's easy to assume that remailers have very few remaining servers and users.

In practice, its safer to assume that so few people are using remailers, that they provide no additional anonymity. Adrelanos would enjoy seeing high latency networks reborn, unfortunately there is absolutely no implication that this is going to happen.

For this reason, for faster delivery and better reliability it makes sense to use only one remailer and not a chain of them. Of course, if you believe remailer chains will make you even more anonymous you are free to use any path length. By the way, if you want to use a remailer for anonymity, you shouldn't test the remailer by sending a remailed mail to yourself.

Depending on what you want to do, it is recommend to encrypt the content of your mail. ^1^ **TODO**: what about the subject? Empty? ""? "-"? Random?

You can install and use remailer software directly inside Whonix-Workstation over Tor, which is the better way. Another method is using a Third Party Webinterface (at the bottom of this page), which is less secure, because the owner of the website could monitor how you type, metadata (send when, to whom) and cleartext (unencrypted content) communication.

A small test with Mixmaster using only one remailer revealed that it takes between 10 and 120 minutes until the mail arrives in the recipients inbox.

<font size=-3>
^1^ Otherwise the last (or only) remailer and the recipient's mail provider could read it.
</font>

## Mixmaster ##
Fully documented on it's own [Mixmaster] page.

## Third Party Webinterface in Tor Browser ##
Note, that everything said in introduction applies and additionally the server administrator can read plaintext as you type or paste. Use with care, perhaps for lower security needs.

### Mixmaster ###
* awxcnx e-mail
	* [clearnet SSL version](https://www.awxcnx.de/mm-anon-email.htm)
	* [Tor hidden service version](http://a5ec6f6zcxtudtch.onion/mm-anon-email.htm)
	* [I2P eepsite version](http://awxcnx.i2p/mm-anon-email.htm)

* awxcnx [usenet](https://en.wikipedia.org/wiki/Usenet)
	* [clearnet SSL version](https://www.awxcnx.de/mm-anon-news.htm)
	* [Tor hidden service version](http://a5ec6f6zcxtudtch.onion/mm-anon-email.htm)
	* [I2P eepsite version](http://awxcnx.i2p/mm-anon-email.htm)

* [webmixmaster paranoici clearnet SSL](https://webmixmaster.paranoici.org/)

* [gilc.org clearnet](http://gilc.org/speech/anonymous/remailer.html)
* [cotse.net clearnet SSL](https://www.cotse.net/cgi-bin/mixmail.cgi)

### Unknown ###

* [anon 978, broken SSL](https://anon.978.org/)
* [anonymouse, clearnet](http://anonymouse.org/anonemail_de.html)
* [hummer55.hu.funpic, clearnet](http://humer55.hu.funpic.de/)
* [send-email.org, clearnet](http://send-email.org/)

## Cypherpunk remailer ##
This may be wrong, feel encouraged to check if I am correct.

Although there is a big [Cypherpunk remailer wikipedia article](https://en.wikipedia.org/wiki/Cypherpunk_anonymous_remailer) and [list of Cypherpunk remailer servers](http://www.noreply.org/echolot/rlist2.html), [cypherpunks.to/remailers/](http://www.cypherpunks.to/remailers/) says it's using Mixmaster and the [helpfile](http://www.cypherpunks.to/remailers/help.txt) explains, that it's safer to use Mixmaster and that Cypherpunk remailer is just an e-mail based interface. Since the [full list of typ I and typ II remailer servers](http://www.noreply.org/echolot/) reveals, that most type I (Cypherpunk) are also type II (Mixmaster) servers, I don't see much point into learning and documenting how Cypherpunk remailer works. It doesn't look like an alternative, i.e. doesn't look like Cypherpunk remailer could be used if Mixmaster doesn't work for some reason. It would also defeat the point of this page: sending mails without registration, because you would still require a mail provider.

# Footer #
[[include ref=WikiFooter]]