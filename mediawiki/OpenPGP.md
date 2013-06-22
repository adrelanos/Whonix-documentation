<!--
Copyright:

   Copyright (C) Amnesia <amnesia at boum dot org>
   Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
   
   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 3 of the License, or
   (at your option) any later version.
         
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
      
   You should have received a copy of the GNU General Public License
   along with this program; if not, write to:

    Free Software Foundation, Inc. 
    51 Franklin St, Fifth Floor
    Boston, MA 02110-1301, USA.

On Debian GNU/Linux systems, the complete text of the GNU General Public
License can be found in the /usr/share/common-licenses' directory.

The complete text of the GNU General Public License can also be found online on gnu.org <https://www.gnu.org/licenses/gpl.html>, in Whonix virtual machine images in /usr/share/common-licenses/GPL-3 file or in Whonix wiki on <https://sourceforge.net/p/whonix/wiki/GPLv3/>.
-->

<!--
This wiki page is a fork of the Tails Trusting Tails signing key page, from this exact source <http://git.immerda.ch/?p=amnesia.git;a=blob;f=wiki/src/doc/get/trusting_tails_signing_key.mdwn;hb=63b68fb4970361131cbd1713b40521244e88c204>.
-->

[[include ref=WikiHeader]]

[TOC]

= Introduction =

To be written.

= Related Tools =

[https://sourceforge.net/p/whonix/wiki/Software/#encrypt-decrypt-sign-and-verify-text-using-openpgp-gnupg-frontend Encrypt, decrypt, sign, and verify text using OpenPGP; GnuPG frontend]

= Advanced Topics =

== The OpenPGP Web of Trust ==

If you want to be extra cautious and really authenticate a OpenPGP key in a stronger way than what standard HTTPS offers you, you could use the OpenPGP Web of Trust.

One of the inherent problems of standard HTTPS is that the trust we usually put on a website is defined by certificate authorities: a hierarchical and closed set of companies and governmental institutions approved by web browser vendors. This model of trust has long been criticized and proved several times to be vulnerable to attacks [https://sourceforge.net/p/whonix/wiki/Warning/ as explained on our warning page].

We believe instead that users should be given the final say when trusting a website, and that designation of trust should be done on the basis of human interaction.

The OpenPGP [https://en.wikipedia.org/wiki/Web_of_trust Web of Trust] is a decentralized trust model based on OpenPGP keys. Let's see that with an example.

''You're a friend of Alice and really trust her way of managing OpenPGP keys. You're trusting Alice's key.''

''Furthermore, Alice met Bob in a conference, and signed Bob's key. Alice is trusting Bob's key.''

This scenario creates a trust path from you to Bob's signing key that could allow you to trust it without having to depend on certificate authorities.

This trust model is not perfect either and requires both caution and intelligent supervision by users. The technical details of creating, managing and trusting OpenPGP keys is outside of the scope of this document.

We also acknowledge that not everybody might be able to create good trust path since it based on a network of direct human relationships and the knowledge of quite complex tools such as OpenPGP.

Because Whonix developer adrelanos prefers to stay anonymous, this trust model is not suited for Whonix.

== Bootstrapping OpenPGP keys from the web ==

What in case you want to totally stay anonymous or have no trust path to a OpenPGP key?

Some people just write an unencrypted mail to the recipient and ask them to send their public key. The recipient will most likely either send it's public key or at least it's fingerprint.

This works against passive attacks. An observer wouldn't know what they have been talking about in the following encrypted mails. This totally fails against active attacks. A man in the middle could replace the recipient's key with it's own malicious key. The sender would use the wrong key, the man in the middle would decrypt the message, read it, and re-encrypt it with the legit key and forward it to the recipient. Neither sender nor recipient would ever find out that there messages are being read by an adversary. - This is the whole reason, why the trust model path and key signing is recommend in the first place.

As an alternative, some people also publish their OpenPGP fingerprint or their OpenPGP key on their personal or other websites. This gets more secure, if the website is accessible over SSL and/or as a hidden service with a .onion domain. In this case, the adversary would have to break the SSL or onion encryption while someone wants to obtain the key or fingerprint or to compromise the server, which may take, depending on the adversary more resources.

For such a model, it is best if the same website is accessible over both, http'''s''' and .onion and the user visits both sites and compares if the results match.

The server compromise risk remains.

To further improve the situation the key holder can spread it's fingerprint and/or OpenPGP key to other websites. Some key holders attach their OpenPGP fingerprint to their e-mail signature (a short attachment of any mail) and participate(d) various public mailing lists. It will be difficult for an adversary to spoof all those information.

Whonix developer adrelanos peruses the strategy to deploy it's key through multiple (at time of writing 6) sources. Different websites reachable over http, http'''s''' or .onion. Hosted by both, known and anonymous people. This should make it much more expensive for an adversary to take them all down or to turn them all over and make this particular attack vector unprofitable. An example implementation of this strategy can be found on the [TrustingWhonixSigningKey] wiki page.

= License =

<pre>Whonix OpenPGP wiki page Copyright (C) Amnesia &lt;amnesia at boum dot org&gt;
Whonix OpenPGP wiki page Portions Copyright (C) 2012 adrelanos &lt;adrelanos at riseup dot net&gt;

This program comes with ABSOLUTELY NO WARRANTY; for details see the wiki source code.
This is free software, and you are welcome to redistribute it
under certain conditions; see the wiki source code for details.</pre>
= Footer =

[[include ref=WikiFooter]]

