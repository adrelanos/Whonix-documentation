<!--
Copyright:

   Whonix Trust wiki page Copyright (C) Amnesia <amnesia at boum dot org>
   Whonix Trust wiki page Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
   
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
The Introduction chapter of this website is forked from the Tails trust page, from this exact source <http://git.immerda.ch/?p=amnesia.git;a=blob;f=wiki/src/doc/about/trust.mdwn;hb=d249db72228b498407d85fb762b49ec155871ded>.
-->

[[include ref=WikiHeader]]

[TOC]

= Introduction =

Trust is a very problematic issue, and that's the essence of why security is difficult in every field, including computers and Internet communication. Do you trust Whonix and its developers? Do you think we have planted backdoors in Whonix so we can take control of your computer, or that we make Whonix generate compromised encryption keys in order to enable the government to spy on you? Do you simply trust our word on that we are legit?

No matter what your opinion is in this matter you should ask how you reached that conclusion. Both trust and distrust need to be established based on facts, not gut feeling, paranoid suspicion, unfounded hearsay or our word. Of course, we claim to be honest, but written assurances are worthless. In order to make an informed decision you must look at the greater picture of what Whonix is comprised of, our affiliations, and possibly how others trust us.

== Free software and public scrutiny ==

Free software, like Whonix, enables its users to check exactly what the software distribution consists of and how it functions since the source code must be made available to all who receive it. Hence a thorough audit of the code can reveal if any malicious code, like a backdoor, is present. Furthermore, with the source code it is possible to build the software, and then compare the result against any version that is already built and being distributed, like the Whonix ova images you can download from sourceforge.net. That way it can be determined whether the distributed version actually was built with the source code, or if any malicious changes have been made.

Of course, most people do not have the knowledge, skills or time required to do this, but due to public scrutiny anyone can have a certain degree of implicit trust in Free software, at least if it is popular enough that other developers look into the source code and do what was described in the previous paragraph. After all, there is a strong tradition within the Free software community to publicly report serious issues that are found within software.

== Trusting Debian GNU/Linux ==

The vast majority of all software shipped in Whonix comes from the [http://www.debian.org/ Debian GNU/Linux distribution]. Debian is arguably the Linux distribution whose software packages are under the deepest public scrutiny. Not only is Debian itself one of the largest Linux distros, but it's also one of the most popular distros to make derivatives from. Ubuntu Linux, for instance, is a Debian derivative, and the same goes transitively for all of its derivatives, like Linux Mint. Thus there are countless people using Debian's software packages, and countless developers inspect their integrity. Very serious security issues have been discovered (like the infamous [https://lists.debian.org/debian-security-announce/2008/msg00152.html Debian SSH PRNG vulnerability] ([http://www.webcitation.org/6EnxsukxM w]), but backdoors or other types of intentionally placed security holes have never been found to our knowledge.

== Trusting Tor ==

Whonix anonymity is based on Tor, which is developed by [https://www.torproject.org/ The Tor Project]. The development of Tor is under a lot of public scrutiny both academically (research on attacks and defenses on onion routing) and engineering-wise (Tor's code has gone through several external audits, and many independent developers have read through the sources for other reasons). Again, security issues have been reported, but nothing malicious like a backdoor -- we would argue that it's only uninformed conspiracy theorists that speculate about deliberate backdoors in Tor these days. Furthermore, Tor's distributed trust model makes it hard for a single entity to capture an individual's traffic and effectively identify them.

== Trusting Whonix ==

One could say that Whonix is the union of Debian and Tor. What we do, essentially, is gluing it all together. Hence, if you trust Debian and The Tor Project, what remains to establish trust for Whonix is to trust our &quot;glue&quot;. As has been mentioned, Whonix is Free software, so its source code is completely open for inspection, and it's mainly comprised by a specification of which Debian software packages to install, and how they should be configured. While Whonix surely doesn't get the same amount of attention as Debian or Tor, <s>we do have some eyes on us from especially the Tor community, and also some of the general security community (see our [https://sourceforge.net/p/whonix/wiki/Security%20Reviews%20and%20Feedback/ audits page].</s> Given that Whonix source code is comparably small and devoid of complexities, we're in a pretty good spot compared to many other projects of similar nature. Our specification and design document (See [Design].) is a good starting point to understand how Whonix works, by the way.

With all this in light (which you ideally also should try to verify), you should be able to make an informed decision on whether or not you should trust our software.

= How can I trust the download images? =

Don't trust 'us'! You don't know us. Never trust people you don't know, especially not on the internet. Even if you decided to blindly trust Whonix developer adrelanos for some strange reason, well, adrelanos feels honored, but since Whonix is/could become a high profile target, it's a bad idea to assume, that adrelanos's build machine is clean from sophisticated targeted attacks.

You can trust these binary images to some extent if you can verify that you get exactly the same code as hundreds of other users (you can check sourceforge how often the builds where downloaded) and no one found and publicly reported any security issue. In order to verify that, beginning from Whonix 0.4.5 OpenPGP signatures are uploaded.

Sourceforge ensures some trust and integrity of the hash file through TLS (check the certificate), unfortunately only for users who are registered and logged in.

Binary releases and source code tags for releases are OpenPGP signed by anonymous Whonix developer adrelanos. The Whonix project exists since 2012-01-11. (Earlier project names were TorBOX and aos ([History]).)

If that's not good enough, you are very much welcome to build your own Whonix images using the [BuildDocumentation]. It is easy.

= Misc =

== TLS ==

TLS/SSL/HTTPS with the CA model is flawed. We don't trust it and you shouldn't either. Even if all the implementation details (revocation not working, every CA can issue certs for anything, including &quot;*&quot;) were sorted out, having to trust a 3rd party is a no go. But, we still have to rely on it to some extent for that lack of a widely used web of trust or other alternative.

== OpenPGP ==

OpenPGP: Usually you get a fingerprint on a web site (insecure, or secured with the broken TLS) and then download that from a key server (insecure, or secured with the broken TLS). Unless you have attended any key signing parties and have a trust path to everyone you need to connect with, OpenPGP is only as secure as TLS!

To mitigate this, it is recommended to check OpenPGP fingerprint from multiple &quot;secure&quot; sites. Bonus points for using different authentication systems. For example: https://www.torproject.org/docs/signing-keys.html.en AND http://idnxcnkne4qt76tg.onion/docs/signing-keys.html.en. Note, that hidden services do not offer very strong authentication. A powerful adversary is more likely than not able to impersonate a hidden service, but together with multiple sources it becomes increasingly costly and improbably that a single adversary can impersonate all of them.

All current Whonix developers prefer to stay anonymous. There's no way to get OpenPGP key signed (real life &quot;key party&quot;) while remaining anonymous. Binary downloads are OpenPGP signed by Whonix developer adrelanos. The source code is available from github over TLS, you can git clone over https. Each release git tag is OpenPGP signed by Whonix developer adrelanos. If desired, you can request signed git development tags from adrelanos.

Whonix developer ([http://www.webcitation.org/6Eny0UfAI w]), [[(https://trac.torproject.org/projects/tor/wiki/doc/proper?version=1)|named proper in past]] ([http://www.webcitation.org/6Fg1zUNeQ w]), [https://trac.torproject.org/projects/tor/wiki/doc/proper?version=6 renamed itself to adrelanos] ([http://www.webcitation.org/6Fg2p2YK3 w]), [https://trac.torproject.org/projects/tor/wiki/doc/proper?version=3 published its OpenPGP key on 05/29/12] ([http://www.webcitation.org/6Fg336X1H w]) ([https://trac.torproject.org/projects/tor/wiki/doc/proper?action=history wiki history] ([http://www.webcitation.org/6Fg24cX1W w])). Its OpenPGP key is mirrored online on seven different places, see [https://sourceforge.net/p/whonix/wiki/TrustingWhonixSigningKey/ TrustingWhonixSigningKey] ([http://www.webcitation.org/6Fg3L8QCZ w]).

The OpenPGP key ensures, should the Whonix infrastructure ever be compromised by a powerful adversary (domain seizure/takeover etc.), that the original Whonix developers can at least prove, that they are the same people who owned the infrastructure.

Even if you distrust Whonix developers, OpenPGP verifying binary downloads or git tags is still useful. If you want to audit Whonix, you should ensure, that you actually got your download from Whonix developers and that no third party tampered with it. Examples:

* [http://www.extremetech.com/computing/120981-github-hacked-millions-of-projects-at-risk-of-being-modified-or-deleted An attacker could modify source codes on github] ([http://www.webcitation.org/6Eny2zbS1 w])
* [http://sourceforge.net/blog/sourceforge-attack-full-report/ sourceforge hacked] ([http://www.webcitation.org/6Eny40bV9 w])
* [http://www.theregister.co.uk/2012/09/26/sourceforge_backdoor_code_compromise/ sourceforge mirror hacked] ([http://www.webcitation.org/6Enz6vyNP w])

== What do the Digital Signatures Prove and What They DO NOT Prove ==

Most people, even programmers, often confuse the basic ideas behind digital signatures. Most people should read this section, even if it looks trivial at first sight.

Digital Signatures can prove, that a given file is authentic, i.e. that is has been indeed created by a person that signed it, and that its contents have not been tampered (so, integrity is preserved).

Digital Signatures do '''not''' prove any other property, e.g. that the file is not malicious. In fact there is nothing that could stop people from signing a malicious program (and it happens from time to time in reality).

The point is, of course, that people need to choose to trust some people, e.g. Linus Torvalds, Microsoft, etc. and assume that if a file(s) was indeed signed by those individuals, then indeed it should not be malicious and buggy in some horrible way. But the decision of whether to trust certain people (e.g. those behind the Whonix Project) is beyond the scope of digital signatures. It's more of a sociological and political decision.

However, once we make a decision to trust somebody (e.g. The Whonix Project and the files released by them), then the digital signatures are useful, because they make it possible to limit our trust only to those few people we chose, and not to worry about all the Bad Things That Can Happen In The Middle between us and them (i.e. the vendor), like e.g.: server compromises, dishonest IT staff at the hosting company, dishonest staff at the ISPs, WiFi attacks, etc.

If we verify all the files we download from the vendor, we don't need to worry about all the above bad things, because we would easily be able to detect when the file(s) has been tampered (and not execute/install/open them).

However, for the digital signatures to make any sense, one should ensure that the public keys we use for signature verification are indeed the original ones. Anybody can generate a OpenPGP key pair that would pretend to be for &quot;Whonix Project&quot;, but only the key pair that I (adrelanos) generated is the legitimate one. Securely obtaining Whonix signing key is documented on a later page, [TrustingWhonixSigningKey].

== Whonix developer OpenPGP guidelines ==

All Whonix developers who use long term pseudonyms, are encouraged to:

* Create a 4096/4096 RSA/RSA OpenPGP key.
* Get the latest gpg.conf (which comes with Whonix-Workstation) for stronger hashes, no-emit-version, etc.
* Store the private key inside an encrypted file.
* Make a backup of that encrypted file.
* Remember the password, check yourself regularly.
* Also upload the encrypted file to some (free) online cloud hosting, in case of thief, fire, tornado, etc.
* Since the project started in 2012, the earlier the OpenPGP public key was published, the less likely is it, that the public key is affected from an evil developer attack. Adrelanos expects evil developer attacks not to happen against relatively new, unpopular and insignificant projects.

== evil developer attack ==

This is only a theoretical attack, as far as we know. We are not aware that it ever happened to any software project. This is not an Whonix specific problem. It applies to all open source software projects, but more to those where the developers stay anonymous. Examples for such anonymously developed software projects are TrueCrypt, Tails, i2p, Whonix... As of April 2012 all Whonix developers are also anonymous.

The attack works like this: 1. Start a new software project. Alternatively join an existing software project. 2. Behave well, publish your sources. Gain trust. 3. Build binaries directly from your sources and offer them for download. 4. Make a great product, get a lot of users. 5. Continue to develop it. 6. Make a second branch of your sources and add malware. 7. Continue to publish your clean sources, but offer your malicious binaries for download. 8. Done! You infected a lot of users.

It is very difficult for end users to notice this attack. Of course, if all users would be added to a botnet, there would be news about this incident very soon and everyone would know. On the other hand, if the backdoor is barely used, it may remain secret for a long time.

The myth, that open source software is automatically more secure than closed source, is still strong and widespread. Yes, open source has advantages but certainly not for this threat model. Who checks if the binaries are made from the proclaimed source and publishes the results? That is called deterministic builds (google it) and it's quite difficult to archive that. We are not aware of any projects, who done that already. For example, the Tor developers also want to offer it but still struggle, see #3688. If you are interested on how complex it is, also google 'trusting trust'.

All that is very difficult and it all comes back to trust. How can you trust anonymous developers? Even if they were not anonymous, you still do not know them and can not trust them? And even if you know them, can you trust them not to have made any mistakes?

These are serious questions to think about. Whonix is also affected by this issue, just like TrueCrypt, Tails, i2p, etc. Most projects (such as TrueCrypt) do not even admit and inform about this fact. Whonix is just an ordinary software project, unfortunately we are unable to fix all problems in the world.

Whonix doesn't distribute any binaries, only redistributes unmodified upstream binaries, shell scripts, we do not create our own binaries. That's what we claim, but it's a lot easier to verify than if we were distributing our own binaries from source code we wrote. Users should worry about the motives and internal security of everyone contributing to torproject.org, all of the distro devs and maintainers and the hundreds of upstream devs and contributors. Trusted computing base size of a modern operating system today is so ridiculously big and so many people are involved we'd be really surprised if none of the &quot;bugs&quot; were intentional. And then there's the hardware. You think that even AMD could understand an Intel chip or vice versa? Of course one can't compare an anonymous contributor with no investment but time with a multi-national company. On the other hand, detection here is just ridiculously simple (diff the hash sums), while finding and then proving that something is not a bug but a backdoor in a compiler, well designed source code let alone a CPU is impossible. Anonymous or not no longer matters these days. We are in a more or less open &quot;cyber war&quot; or that's what media and lawmakers want us to believe. Fact is, today players are backed by governments, they can use their real identities without fear of repercussion, fake IDs can be created, trustworthy people can be coerced into giving up their OpenPGP and ssh keys if projects even make use of any strong authentication. Judging by the lack of signatures on many open source upstream and even downstream downloads I'm sure many lack any internal security enforcement and still trust DNS to provide authenticity and clear text to provide integrity. About open source, yeah, you can bet Apple, Google and Microsoft have better internal security than the global open source community. However that doesn't make their code trustworthy or says anything about whether closed or open is more secure...

== adrelanos's reasons to stay anonymous ==

For anyone curious to know... Protection and paranoia (depending on definition). Just a few examples...

People failing to understand the software making death threats:

* https://tails.boum.org/forum/Too_frequent_IP_address/#comment-cfc122dfc8de737737c076399250a766 ([http://www.webcitation.org/6EnyCThAn w])

Making threats to &quot;burn down his house&quot;, &quot;pay him an overdue visit&quot;:

* http://fscked.org/blog/something-rotten-opdarknet ([http://www.webcitation.org/6EnzTQo5k w])

Harassment on border:

* http://www.huffingtonpost.com/2010/08/02/jacob-appelbaum-wikileaks_n_667665.html ([http://www.webcitation.org/6EnyCThAn w])
* http://news.cnet.com/8301-27080_3-20012253-245.html ([http://www.webcitation.org/6EnzUVsJn w])

Security and trust shouldn't depend on showing a face:

* [https://tails.boum.org/forum/Who_is_behind_Tails__63__ Tails] ([http://www.webcitation.org/6EnyCggbX w])

Other reasons:

* Staying out of press with real name.
* Separating private, professional and project's activities.

== Also interesting ==

* Tails is a live CD or live USB that aims at preserving your privacy and anonymity. [https://tails.boum.org/doc/about/trust/index.en.html Tails about trust.] ([http://www.webcitation.org/6EnyJvTnn w])
* I2p (anonymizing network) does also talk about [http://www.i2p2.de/how_threatmodel.html#dev development attacks]. ([http://www.webcitation.org/6EnyKSGdn w])
* [http://wiki.qubes-os.org/trac/wiki/VerifyingSignatures Qubes OS: What do the Digital Signatures Prove and What They DO NOT Prove] ([http://www.webcitation.org/6EnyL8AQn w])
* [http://hyper.to/blog/link/attack-scenarios-software-distribution/ Miron’s Weblog: Attack Scenarios on Software Distributions] ([http://www.webcitation.org/6EnzaBTdP w])

= How to improve the situation? =

This page may sound a bit sad. The situation is less than optimal. The good news is, that it's not an unsolvable problem. It's what I've been able to work on. I can't do it all alone. It can be improved! [https://sourceforge.net/p/whonix/wiki/Contribute/ Contributors] can help to improve the situation.

Other <font size="-3"(non-anonymous)</font> persons are trusted by different groups. They could contribute by [https://sourceforge.net/p/whonix/wiki/Contribute/#packager-for-binary-builds creating and signing binary builds].

Skilled developers could help to implement [https://sourceforge.net/p/whonix/awiki/Dev/#security-deterministic-builds-open-needs_research-needs_discussion Deterministic builds]. This would provide proof, that a binary was created from genuine source.

= License =

<pre>Whonix Trust wiki page Copyright (C) Amnesia &lt;amnesia at boum dot org&gt;
Whonix Trust wiki page Portions Copyright (C) 2012 adrelanos &lt;adrelanos at riseup dot net&gt;

This program comes with ABSOLUTELY NO WARRANTY; for details see the wiki source code.
This is free software, and you are welcome to redistribute it
under certain conditions; see the wiki source code for details.</pre>
<font size="-3">Thanks to Qubes OS ([https://groups.google.com/forum/?fromgroups=#!topic/qubes-devel/zALZnu9pTuU Permission]) ([http://www.webcitation.org/6EnxWzgfq w]). The &quot;What do the Digital Signatures Prove and What They DO NOT Prove&quot; chapter contains content from the [http://wiki.qubes-os.org/trac/wiki/VerifyingSignatures Qubes OS: What do the Digital Signatures Prove and What They DO NOT Prove] page.</font>

= Footer =

[[include ref=WikiFooter]]

