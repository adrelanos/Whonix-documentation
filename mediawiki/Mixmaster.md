[[include ref=WikiHeader]]

[TOC]

= Mixmaster =

== Introduction ==

Motivation behind this: &quot;''What if there where a bookmark pointing to mail.local (or something like that) where you can simply enter an e-mail address, from sender (optional), subject and text, click send and mail is on it's way?''

''No sign-up/registration/smtp server required.''&quot;

[https://en.wikipedia.org/wiki/Mixmaster_anonymous_remailer Mixmaster] is a Remailer. Please read the [Remailer] article first as introduction.

There are two ways of using the Mixmaster network. Using mixmaster inside Whonix-Workstation, which is recommend, but more difficult. Unfortunately, there is no nice graphical user interface for Mixmaster on Debian GNU/Linux. The other way is using a webinterface, which is documented in the [Remailer] article.

This is quite an unusual setup. At time of writing there where no references that ever anyone ever successfully used the mixmaster software to remail over Tor. Therefore it might make clear, that you are a Whonix user.

== Mixmaster inside Whonix-Workstation ==

A fresh list of Mixmaster nodes is required. You can either update using the ncurses interface or using the Debian method. Both are documented below.

<pre>sudo mixmaster-update --verbose </pre>
Mails can be send by command line.

<pre>echo &quot;mail text&quot; | mixmaster --verbose --to=email@recipient.org --copies=1 --chain=breaka</pre>
Or instead of using echo text, you can also read the text from a file. This is handy, because you can (and should) use a spell checker and because you can (and should if applicable) encrypt the text beforehand.

<pre>echo &quot;`cat maildraftfile`&quot; | mixmaster --verbose --to=email@recipient.org --copies=1 --chain=breaka</pre>
Or if you want to add a subject. (Which you most likely don't want, because the subject can not be encrypted.)

<pre>echo &quot;mail text&quot; | mixmaster --verbose --to=email@recipient.org --subject=&quot;mail subject&quot; --copies=1 --chain=breaka</pre>
Takes a moment and shows.

<pre>Chain: breaka</pre>
Done.

== Implementation Notes ==

For technical stuff, see [Dev_Mixmaster].

== Credits ==

* [http://lists.mixmin.net/pipermail/remops/2012-December/000671.html Remops mailing list] helped creating this page with advice.

= Footer =

[[include ref=WikiFooter]]

