[[include ref=WikiHeader]]

[TOC]

# Voice over IP #
## Introduction ##
The Voice over IP Introduction chapter and instructions about mumble voice chat are finished. Instructions for other Voip client's aren't finished yet, but this shouldn't stop you from using mumble or experimenting with other clients. Please test and leave feedback!

Anonymizing Voice over IP is very difficult, if possible at all. It's not so much about hiding the IP, which is easy with Whonix, it's about voice recognition and slow Tor network speed (latency). Pseudonymous use or hidden voice communication with known contacts is possible. It depends on your threat model.

For people behind Tor, who know each other, talking to each other, it is possible to hide the fact, that they are talking with each other, from their ISP, government, exit nodes, man-in-the-middle, etc. That wouldn't be anonymous, because they know each other.

You can't anonymously use your own voice and whistleblow over Voip, be a snitch or whatever. Voice gets recorded and voice recognition works well. When you are having a phone call later over a non anonymous connection (which almost everyone had at least once in it's life, so everyone supplied a sample of their voice and name), they can correlate the two identities. You would have to use a voice scrambler and how good that works is a whole new field for research, which is outside the scope of Whonix.

You could type and let a artificial voice speak (like in anonymous videos), that could work. But is that the point? You better write a mail then.

It's also recommend against to voice chat with other anonymous people. (Like you can talk in a forum.) You don't know who you are talking to. That voice also could be correlated later, putting aside voice scrambler, or artificial voice, which wouldn't make sense.

If you are not calling from .onion to .onion (which delegates encryption to Tor), you should use a Voip client supporting encryption, such as [ZRTP](https://en.wikipedia.org/wiki/ZRTP). You'll find recommendations later below in the clients section.

Other than the things said above, adrelanos doesn't expect any additional anonymity/security problems. It's less tested, so as for performance and voice quality, just try it and see yourself and please leave feedback.

Please don't expect phone calls over Tor can't to be as convenient as phone calls over ordinary networks. This is because traffic is routed through the Tor network

Push to talk will always work however, which is more like using [walkie-talkie](https://en.wikipedia.org/wiki/Walkie-talkie), [push-to-talk](https://en.wikipedia.org/wiki/Push-to-talk).

Useful advice has been given by guardianproject.info. They recommend to use [prowords](http://en.wikipedia.org/wiki/Procedure_word). Acknowledge the end of transmission (your speech, your sentence, what you just said) with the word "Roger". Once your calling partner hears "Roger", it knows, it's safe to answer and also terminate the answer with "Roger" or "Out" when leaving the conversation.

## Voip Server ##
You most likely still require a Voip server. If no one of your group is interested in configuring a hidden Voip server, you could use a free one. I could imagine, that even latency is a bit better.

If the Voip ID gets anonymously registered, i.e. if no personal data is required for signing up, everyone only and always connects over Tor, never connected or will ever connect without Tor, and all calls are encrypted and you won't talk to strangers, I don't see what even a malicious server could do. ^1^

<font size="-3">
^1^ Apart form trying to [exploit](https://en.wikipedia.org/wiki/Exploit_(computer_security)) random Tor users.
</font>

## Voip Clients ##
### Recommendations ###
#### Jitsi ####
Jacob Appelbaum (Tor researcher) [recommends](https://jitsi.org/Main/News) [Jitsi](https://jitsi.org/). It supports OTR encryption and ZRTP. Unfortunately [it is not in Debian package sources](http://bugs.debian.org/627362) so you would have to download and install it manually following the instructions on Jitsi homepage for Debian.

**TODO**: research, does Jitsi support push to talk?

**TODO**: write a guide how to connect to a free public server, having a secure ZRTP encrypted conversation with someone using the same client.

#### sflphone ####
Nathan Freitas (Tor Orbot developer) [likes](https://lists.torproject.org/pipermail/tor-talk/2013-February/027204.html) [sflphone](http://sflphone.org/). Can be installed from Debian package sources.

It does not support OTR. You would have to keep that in mind and use another way to exchange encrypted text. This isn't a reason, not to use it, if you are aware of that.

**TODO**: research, does sflphone support push to talk?

**TODO**: write a guide how to connect to a free public server, having a secure ZRTP encrypted conversation with someone using the same client.

#### mumble
##### Introduction
[mumble](http://mumble.sourceforge.net/)

* Looks a bit like Team Speak without it's disadvantages.
* It's Open Source.
* And [supports client to server encryption](http://mumble.sourceforge.net/FAQ/English#Is_Mumble_encrypted.3F).
* [Supports push to talk](http://www.mumble.com/support/mumble-server-push-to-talk.php).
* You can (and must) [force TCP mode](http://en.kioskea.net/faq/26187-mumble-force-tcp-mode), because the Tor network does not yet support UDP.
* One has to act as server.
* Everyone else can act as client.
* If the server admin runs the server on it's local machine and also wants to connect to the server, the admin should connect locally to the server, i.e. to 127.0.0.1 and not the hidden service domain to have faster connection.
* For group chats you have to consider, that there is no end-to-end encryption and once the server acts malicious, all conversions are unsafe. However, if two people use mumble just to talk to each other this doesn't matter and you could safely do that with mumble.
* When one of the two communication partners hosts a mumble server as Tor hidden service and the other one connects over Tor, encryption is already provided by Tor. There are different ways to archive security. In this case, settings a server password (explained below), should be sufficient. <font size=-3>Mumble's own encryption isn't required. Alternatively, feel free to learn about mumble certificates for defense in depth, channel passwords instead of server password and so on.</font>

##### Mumble Server Instructions
If you want to read and introduction about hidden services and to learn about about hidden service security, see [Hidden Services].

On Whonix-Gateway.

Open */etc/tor/torrc*.

    sudo nano /etc/tor/torrc

Add.

HiddenServiceDir /var/lib/tor/mumble_service/

If you also want to run a hidden web server on the same .onion domain, optionally add. (Nice for testing, see [Hidden Services], you can comment out it later.)

    HiddenServicePort 80 192.168.0.11:80

Also add.

    HiddenServicePort 64738 192.168.0.11:64738

Reload Tor.

    sudo service tor reload

Reminder: To get your hidden service url.

    ## must be root: sudo su
    nano /var/lib/tor/hidden_service/hostname

Reminder: Backup your hidden service key, in case you want to be able to restore it, on another machine, on a newer Whonix-Gateway, after hdd failure, etc.

    ## must be root: sudo su
    /var/lib/tor/hidden_service/private_key

On Whonix-Workstation.

Update package lists.

    sudo apt-get update

To host a mumble server, install.

    sudo apt-get install mumble-server

Configure the server.

    sudo dpkg-reconfigure mumble-server

The following questions...

* Autostart, better yes. Otherwise you would have to "sudo service mumble-server start", which didn't work for me.
* Higher priority? Yes.
* Password: choose a secure password.

There is also an upstream [Murmur](http://mumble.sourceforge.net/Running_Murmur), i.e. mumble server guide. The upstream guide does not consider hidden services, that's the part already described here. For any other questions regarding the server setup, you can also refer to the upstream documentation.

Set a server password. Open */etc/mumble-server.ini*.

    kdesudo kwrite /etc/mumble-server.ini

Search for "*serverpassword=*" and file in.

    serverpassword=use_a_long_and_secure_server_password

Restart mumble-server.

    sudo service mumble-server restart

##### Mumble Client
###### Installation
Update package lists.

    sudo apt-get update

Install mumble.

    sudo apt-get install mumble

###### Start
Start mumble.

    Start menu -> Applications -> Internet -> Voice Chat.

###### Configure
Configure mumble to your linking.

Enable Force TCP mode.

    Go to Configure -> Check "Advanced" -> Network -> Check "Force TCP mode" -> Ok

###### Add Server
Add a new server:

    Server -> Connect -> Add new ->

        Label   : anything, can be same as .onion domain name
        Address : your .onion domain name or,
                  if the mumble server is running in your own
                  Whonix-Workstation choose
                  127.0.0.1
        Port    : 64738
        Username: anything

You can now connect to the server.

##### Technical Comments
<font size="-3">
Mumble (and mumble-server)'s connections go through Tor's TransPort. This shouldn't matter, because (connections to and ) hidden services (itself) are stream isolated so or so, see [Stream Isolation] for more information on TransPort, SocksPort, Stream Isolation and so on.
</font>

#### List ####
There is a [Comparison of VoIP software](https://en.wikipedia.org/wiki/Comparison_of_VoIP_softwareComparison of VoIP software) in wikipedia. The client should be Open Source and if you are not calling from .onion to .onion (and let Tor handle encryption) it should also support voice encryption such as ZRTP.

#### Development Ideas ####
[OnionCat](https://sourceforge.net/p/whonix/wiki/OnionCat/) could be useful if tunneling UDP and/or ICMP tunneling over Tor should be required. It should be avoided if possible, because it add complexity to the setup and introduces more latency because connection always goes from hidden service to hidden service.

### Warnings ###
#### TOR Fone ####
The developer of TOR Fone [recommends against](https://lists.torproject.org/pipermail/tor-talk/2013-February/027215.html) using TOR Fone. Quote: "*I did not think this project as a finished product for practical use.*" The project got overall a pretty bad review in the mailing list thread.

#### Skype ####
**Does this mean that, for example, is my IP and location safe when using Skype?**

Yes, IP and location is safe. Skype has been tested in Whonix, it "works" quite well, still recommend against. Some further comments you should be aware off...

Those are not Whonix or Tor issues, those are Skype issues. Consider Skype usage [pseudonymous rather than anonymous](https://sourceforge.net/p/whonix/wiki/DoNot/#do-not-confuse-anonymity-with-pseudonymity). Skype is closed source and given Skype's history (reading BIOS etc. just research) it's very much likely that they link all your account names inside Whonix-Workstation to the same pseudonym.

Also obviously, if you log into an account, which you have ever used without Tor, consider the account non-anonymous. You really should assume, that they have logs and link your Tor and non-Tor use together.

Security doesn't depend on your local security and key management, but on a third party, the Skype authority. Consider the Skype encryption broken by the Skype authority.

Another obvious thing, if you chat with people, who have not created their account over Tor and who have not always connected over Tor, it's also not so hard to guess who you are. Remember, you are not in control of Skype's encryption keys and Skype is not Open Source, thus do not rely on Skype's encryption. 

Voice recognition software also got very sophisticated. Since you should be unsure if the Skype encryption is broken or not, voice recognition software could be used to find out who you are.

Also read [Do not mix Modes of Anonymity!](https://sourceforge.net/p/whonix/wiki/DoNot/#do-not-mix-modes-of-anonymity).

In conclusion Skype usage does not leak IP/location, but is discouraged anyway, unless you want to use it for circumvention only, without wanting to be anonymous or pseudonymous.

What's the point in using Skype if you and all your chat partners are also willing to create and use their accounts only over Tor? You are advised to use Skype alternatives.

## Sources ##
* [guardianproject.info: Mumble and the Bandwidth – Anonymous CB radio with Mumble and Tor](https://guardianproject.info/2013/01/31/anonymous-cb-radio-with-mumble-and-tor/)

# Footer #
[[include ref=WikiFooter]]