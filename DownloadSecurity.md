[[include ref=WikiHeader]]

[TOC]

# General #
The "Simple" chapter on this page tries to keep it as short and easy as possible while the "More difficult" chapter goes more into detail, reasoning and theory.

# Simple #
There is no digital security like 0 or 1 or insecure or secure. I am afraid, the message of this page will be, the more time one invests the more security one can gain.

Just downloading the images in the clear without any verification is the least safe method. On the other hand, how insecure is it? There is for example [gpg4win](http://www.gpg4win.org/), [Firefox Portable](http://portableapps.com/apps/internet/firefox_portable) and so on. There is no SSL available to download those software projects. If you compare how often software gets downloaded and how few times the accompanying signatures are downloaded, very few people do care. Yet, reports of downloads which got compromised by a man-in-the-middle attack (for any project) happen seldom. I am not aware of any examples, please contact me if you have some.

Sourceforge.net does not support SSL for downloads.

Viewing the download page (https://sourceforge.net/projects/whonix/files/whonix-x.x.x/) while logged into sourceforge.net you can see the MD5 and SHA1 hash (provided by sourceforge.net) after clicking the **i** button (View details).

Comparing the hash sums from the SSL protected page and verifying (comparing them) with what was downloaded is safer than no verification at all.

OpenPGP verification (as noted on the [Download] wiki page) is even more safe.

Building Whonix from source code oneself is most secure option to obtain Whonix. (Many bonus points for auditing the source code before using it.)

# Related Wiki Pages #
* [Download]
* [Trust]
* [TrustingWhonixSigningKey]

# More difficult #
Of course, providing downloadable images over SSL and/or a hidden service would be safer. This risk can be circumvented when images are verified. Practically it will be difficult to provide SSL protected downloads. Many important software projects can only be downloaded in the clear, such as Ubuntu, Debian, Tails, Qubes OS, etc. This is because someone has to pay the bill and SSL (encryption) makes it more expensive.

It would also be safer if the download server would be under full control of the developers and not under control of a big company. But that's not how things work today. Self-hosting is very expensive. (Requires fast internet connection, home user contracts won't be fast enough, many servers, electricity power and physical security (officers).) Even the servers of The Tor Project are not hosted in some developers home.

Building from source code is also safer, because the developer itself does not have to be trusted. Even if the developer were trusted, self building is still safer. It removes the risk, that the developer build machine got infected by a targeted attack. See also, [Trust].

# Footer #
[[include ref=WikiFooter]]