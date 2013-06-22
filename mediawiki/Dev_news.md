[[include ref=WikiHeader]]

[TOC]

= Whonix News File Format =

'''Version 0.2''' used by Whonix 0.5.6

First line contains version and may not contain any spaces!

<pre>0.3.0

news text here
some more news text
...</pre>
= How to create a valid Whonix News File =

== Manually ==

(1). safe as whonix_news

<pre>.</pre>
(2). sign

<pre>gpg --clearsign whonix_news</pre>
(3). test

<pre>gpg --verify whonix_news.asc</pre>
== Using Maintainer Script ==

https://github.com/adrelanos/Whonix/blob/master/release/upload_download_readme

= Extra implementation info =

Signing and verification (as sanity check) of [https://github.com/adrelanos/Whonix/blob/master/release/whonix_news whonix_news] is automated by [https://github.com/adrelanos/Whonix/blob/master/release/upload_whonix_news upload_whonix_news].

[https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/bin/whonixcheck-scripts/50_check-whonix-news 50_check-whonix-news] will find out the current installing version by:

<pre>## Read only FIRST line.
read -r INSTALLED_WHONIX_VERSION &lt; /usr/local/share/whonix/version
## Remove ALL spaces.
INSTALLED_WHONIX_VERSION=&quot;${INSTALLED_WHONIX_VERSION//[[:space:]]}&quot;</pre>
While phrasing the whonix_news, it's not required to remove the OpenPGP Signature, because the function verify_whonix_news in [https://github.com/adrelanos/Whonix/blob/master/whonix_shared/usr/local/bin/whonixcheck-scripts/50_check-whonix-news 50_check-whonix-news] will use ''gpg --decrypt'' to get plain text, which will result in the Whonix News File Format.

= Changelog =

0.1 to 0.2

* /usr/share/whonix/version changed to /usr/local/share/whonix/version

= Footer =

[[include ref=WikiFooter]]

