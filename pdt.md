[[include ref=WikiHeader]]

# Summary
This is a proposal to defend a **permanent takedown threat**. A mechanism to securely download project metadata, which includes censor resistance, defeating rollback and infinite freeze attacks. 

In comparison to [TUF](https://www.updateframework.com/) (The Update Framework), it does not require software to be running on a server and can be run on any (free) web space.

# Definitions
<font size="-3">Definition by adrelanos:</font>

> **Project metadata**. Is defined as version information, news, update information, project homepage and so on.

<font size="-3">Definition by adrelanos:</font>

> **Permanent takedown threat.** An attacker takes down a mirror by taking over the domain or by taking down the server using [DoS attack](https://en.wikipedia.org/wiki/Denial-of-service_attack), cracking down the server with malware or by pressuring humans (the server administrator).

<font size="-3">Quote: [TUF: Attacks and Weaknesses](https://www.updateframework.com/wiki/Docs/Security#AttacksandWeaknesses) ([w](http://www.webcitation.org/6F7Io2ncN)):</font>

> **Rollback attacks.** An attacker presents a software update system with older files than those the client has already seen, causing the client to use files older than those the client knows about.

<font size="-3">Quote: [TUF: Attacks and Weaknesses](https://www.updateframework.com/wiki/Docs/Security#AttacksandWeaknesses) ([w](http://www.webcitation.org/6F7Io2ncN)):</font>

> **Indefinite freeze attacks.** An attacker continues to present a software update system with the same files the client has already seen. The result is that the client does not know that new files are available.

# Motivation
What happens if an adversary ever manages to ban project websites such as Tails or Whonix? Boum.org domain and server seizure, Whonix kicked from sf.net.

The project admins will lose the ability to inform their users about critical security updates and communications break down. Users will no longer be able to visit the original homepage, which could even get replaced with a malicious version.

It would take some time to reorganize hosting, move to censor resistant hosting and to inform the existing user base.

# Discussion
Using a single server, i.e. single domain/server for project metadata is recommend against, as it introduces a single point of failure. When the server goes offline, project metadata can no longer be distributed. The server could also serve either due to a bug or by malicious indent a gpg signed, but outdated project metadata.

To prevent disclosing which software is fetching project metadata, the request must go through Tor. Identity correlation through circuit sharing must be circumvented by using a separate circuit for project metadata fetches.

GPG signing of project metadata is a must, since it's independent from SSL certificate authorities.

The public key of the signer must be included into the software project at build time. Distributed trust could be implemented by using X signing keys and defining, that project metadata has to be signed by at least Y of X signers to be accepted as valid.

To my knowledge, there are is no distributed censor resistant data storage available over Tor. Freenet is a distributed censor resistant data storage, which can unfortunately not be accessed over Tor. ^1^ Otherwise Freenet could be well suited for this purpose.

# Implementation
There are web services run by different organizations, which allow (free) web hosting, which can be used for project metadata. Examples are github pages, sourceforge file release system and a free onion hosting services. ^2^

Below is an example, how a project metadata file could look like.

    -----BEGIN PGP SIGNED MESSAGE-----
    Hash: SHA512

    projectversion: 0.4.5

    metadataversion: 536
    validuntil: 1369159330

    homepage: http://whonix.sourceforge.net/

    news: No important News.

    mirror 1: http://whonix.sourceforge.net/whonix_news.asc
    mirror 2: http://su6ephfi7dtxnbtb.onion/whonix_news.asc
    mirror 3: https://adrelanos.pages.github.com/whonix_news.asc

    -----BEGIN PGP SIGNATURE-----

    xxxSIGNATURExxx
    -----END PGP SIGNATURE-----

Such a project metadata file is supposed to be initially copied into the project's binary distribution at build time. The purpose is to initially equip the metadata fetcher with a list of mirrors.

From all available mirrors, the metadata fetcher uses all ^3^ mirrors at each run time to download the current project metadata. If metadata mirrors are modified or expanded, the updated file will possibly be stored persistently and overrule the metadata file which was included at build time.

The *projectversion* variable contains the version of the project and can be anything. The *homepage* variable contains the latest homepage of the project. It can be useful to inform users about the new homepage in case the old one has been taken down. The *news* variable contains a plain text string. Most of the times it shouldn't contain anything and should only be used to inform users about urgent things, such as when a takedown attack is in place.

The *metadataversion* variable is a consecutive number, i.e. after 536 follow 537. Each update of the metadata file increases that number. The client may not accept lower metadata version numbers, than the client already knows about. This should defeat rollback attacks.

Defeating indefinite freeze attacks is technically a bit more difficult. Each metadata fetch against a different mirror has to go through it's own Tor circuit. Going through it's own Tor circuit, most times a different Tor exit will be used (and connections to hidden services are stream isolated so or so). This will result in using different ISP's to connect to the metadata mirror and as long as not all Tor exit nodes or all Tor exit nodes's ISPs or all metadata mirrors are compromised, no indefinite freeze attack can be successfully mounted. When fetching from hidden services, there are no ISP's involved, who could tamper with the metadata.

The *validuntil* variable represents how long the file is valid, until the mirror is considered outdated. The number represents the time in [unixtime](https://en.wikipedia.org/wiki/Unix_time). If a mirror is considered outdated, a new mirror will be tried.

Distributed trust for the signers has not yet been considered. The signers gpg key is fully trusted. To implement this, one could look into the TUF project, since the TUF project already contains code to define a threshold of signers.

Specifically for Whonix, [whonixcheck] and the [Whonix News Format](https://sourceforge.net/p/whonix/wiki/Dev_news/) could be extended.

# Footnotes
^1^ Freenet could be accessed over Tor, by tunneling UDP over Tor using a VPN. This is too unsuitable for most users to be considered as a workaround. Most VPNs cost money, VPN over Tor is a hack alone and there are not as many VPN nodes as Tor exits, are there?
^2^ Such as [torhost](http://torhostg5s7pa2sn.onion/).
^3^ Or if load balancing is required, using multiple and random mirrors.