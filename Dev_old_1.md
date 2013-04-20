[[include ref=WikiHeader]]

[TOC]

# Closed Tasks
## OPTIONALFEATURE Multiple Gateways
* (adrelanos) Currently we have only one Tor-Gateway. To push forward the tickets "Support for proxies as Tor replacement [ProxyBOX]", "Support for Freenet [FreenetBOX]" and "Support for VPNs as Tor replacement [VPNBOX]" it would help, if we were able to use multiple gateways. I am personally not going to connect to single proxies, JonDonym oder VPN's directly, since I don't want to give up my anonymity as a Whonix developer while doing so.
* (adrelanos) But I'd be interested for example in a two gateway solution. Tor-Workstation -\> VPN-Gateway -\> Tor-Gateway. The VPN would be tunneled through Tor, i.e. user -\> Tor -\> VPN. As soon that is working, it would be possible to change the order, i.e. connect to the VPN first, then connect to tor, i.e. user -\> VPN -\> Tor. Or to drop one or another gateway, i.e. for example, Workstation -\> Proxy-Gateway. Or to do other interesting combinations, such as, Tor-Workstation -\> VPN-Gateway -\> Tor-Gateway -\> another VPN-Gateway.
* (anonymous) Note that doing that makes mitigating id correlation pretty much impossible (you'd have to run multiple VPN instances on the second gateway).
     * (adrelanos) I don't think so. We have to look at, at least two different ways. Adding something behind Tor, i.e. connection scheme like Tor -\> VPN, presses everything into the same pseudonym, adds a permanent "exit".
     * (adrelanos) As long as Tor is the last one in the chain, i.e. connection scheme like T-W -\> VPN -\> ... -\> VPN -\> Tor, circuits and exits can still change. To establish such a connection scheme, the gateways have to be chained the other way around, i.e. T-W -\> Tor -\> VPN -\> ... -\> VPN. Even IsolateSocksAuth were still supported. T-W would still communicate with Tor's Socks-, Dns- and TransPorts. Tor would have to connect through those additional hops (in this example, VPN's). Tor would havet oconnect through all those VPNs and from the last VPN, finally connect to the Tor network. In the end the connection scheme would look like T-W -\> Tor -\> VPN -\> ... -\> VPN -\> entry guard or bridge -\> middle node -\> exit node. Identity correlation can still be prevented.
     * (anonymous) Sure, that's true. I was replying to your explicit example Tor-Workstation -\> VPN-Gateway -\> ..., not the whole post.
     * (adrelanos) Thanks for asking. That's difficult to describe. Unless my brain totally messed up, it should work like that, not tested yet. I like to start documenting this. At least the theory, discussed right now. Do you know a generic term for proxy/VPN/SSH?
     * (anonymous) I don't think there exists a proper term. Anonymity network (redirects to proxy server on wikipedia), anonymizer, anonymizing forwarding gateway, anonymizing proxy. Proxy can be used as a generic Term, at least SSH, real proxies, I2P and Tor are associated with it. VPN not so much because usually it refers to private networks, but I don't see why an anonymizing VPN server shouldn't be a proxy.

* (anonymous) Would be interesting if it just works, i.e. do two (or three) t-gs in a row still work (not that we should do that, it's tor over tor). I would like to know what secret sauce Tor is using for its transparent proxy feature. Everything else related to transparently proxying seems to require ip\_forwarding, DNAT... Resources: SSH (only supports tcp, you need to tunnel dns over that somehow) [http://tomatousb.org/forum/t-326180/poor-man-vpn-with-ssh-transparent-proxy-only-tcp](http://tomatousb.org/forum/t-326180/poor-man-vpn-with-ssh-transparent-proxy-only-tcp) [https://github.com/apenwarr/sshuttle](https://github.com/apenwarr/sshuttle) Theoretically these should also just work. Or not? To this day Tor's transparent proxy function amazes me. AFAIK it's absolutely unique. Tor must keep track of all packets sent to it and then send them back to the correct source IP (local host, t-w client) even though the source is not the destination IP. In other words, implement ip\_forwarding in user space. Or it's SOCKS on steroid. Maybe a tor dev can give us a better explanation. Anyway, duplicate this functionality with other privacy/anonymity solutions like VPN, SSH, IPSEC, looks a bit more complicated than the transparent tor setup, they work some layers down on the OSI model.
     * (adrelanos) There are other applications, which also implement as TransPort, with no requirement for DNAT or ip forwarding. One of them is redsocks, documented in [Whonix/OptionalConfigurations\#TransparentProxying](https://trac.torproject.org/projects/tor/wiki/doc/TorBOX/OptionalConfigurations#TransparentProxying) and [Whonix/OtherAnonymizingNetworks\#ProxiesasaTorreplacementProxyBOX](https://trac.torproject.org/projects/tor/wiki/doc/TorBOX/OtherAnonymizingNetworks#ProxiesasaTorreplacementProxyBOX). Supporting proxies should be easy, once the skeleton for multiple gateways is ready. And SSH can been seen as an "extension" to proxies, since SSH can offer a socks5 proxy. Once an account for SSH has been setup, allowed communicate "in the clear" (perhaps to the next gateway), redsocks/iptables can be used to redirect all traffic into redsocks's TransPort. No ip forwarding required. I don't know yet how to forward the traffic from AnyBOX to a VPNBOX to WAN, perhaps that VPNBOX really requires ip 
forwarding.

* (anonymous) I haven't looked into it but if redsocks is fully transparent, Tor is probably doing a similar thing and traffic on trans\_port is internally routed to an internal SOCKS port. This also means, if they drop that functionality (which came up at one point), there's still a way around that. What do you mean by AnyBOX-\>VPNBOX? VPN doesn't seem to support SOCKS interface so we can't use redsocks. Therefore we'd need forwarding, is that what you meant?
     * (adrelanos) redsocks is fully transparent and can do even more. It requires iptables to redirect TCP and/or UDP (!) traffic to redsocks's "TransPort's". redsocks can forward that traffic to http (supports due to nature of http proxy, only http, no SSL or other services), http-connect, socks4(a) or socks5 proxies. One minus for redsocks: does not offer a DnsPort yet. Afaik DnsPort is unique in Tor. The non-DnsPort with redsocks is a non-issue, if the Tor is the last chain in the connection scheme, since the proxy(or ssh) would only have to forward TCP and Tor would keep care on resolving DNS.
     * (anonymous) if it's t-w \<-\> "redBOX" \<-\> t-g you probably don't want let DNS bypass your second proxy and undo much of the additional security you wanted to gain.
     * (adrelanos) Is the example a connection scheme or "physical" box order? Anyway, I answer both.
     * (adrelanos) Connection scheme: T-W -\> Proxy (redBOX) -\> Tor... Or the same as physical ordering: T-W -\> T-G -\> redBOX. DNS is a non-issue here, 
since the redBOX simply has to forward TCP to the Tor network.
     * (adrelanos) The other way around... Connection scheme: T-W -\> Tor -\> Proxy (redBOX). Or same as physical ordering: T-W -\> Proxy (redBOX) -\> T-G... Transparent Proxying is an issue here, since no DnsPort is available on redBOX. redBOX could only forward it to a known (=you know the IP) DNS resolver (such as OpenDNS). The exit IP's who connect to OpenDNS may change but OpenDNS still could correlate all DNS requests to the same identity. This is not recommend anyway, since the last proxy in the connection scheme can correlate a lot stuff.
     * (anonymous) I meant the latter.
     * (anonymous) Isn't having a local tcp enabled dns listerner fully transparent, i.e. you iptables redirect all dns from t-w tojust like t-w does with the dns port.
     * (adrelanos) This won't work. redsocks has no DnsPort. redsocks can forward UDP (port 53) traffic to a public DNS server (example: DnsCrypt by OpenDNS). This is because socks proxies support hostname resolution, not DNS. If the second part in the physical ordering, i.e. T-W -\> T-G is not given, DNS will be an issue.
     * (anonymous) But it will be transparent. transparent just means that the client (other OS or local application) doesn't have to care about being proxied. Sure, DNS to a single provider is a usually bad, but with redsocks you are already using a single exit provider for ALL and full pseudonymous connections, that's much worse than just domain names.
     * (adrelanos) Yes. Well connection scheme like T-W -\> Tor -\> Proxy/SSH/VPN is not recommend anyway. There aren't much useful use cases, perhaps "plug" that thing in (if we can make it "plugable") to access websites, which otherwise ban Tor or if, in their threat model, the Any is less likely to sniff/manipulate the traffic.
     * (adrelanos) Connection scheme like: T-W -\> Any -\> Tor, i.e. "physical" ordering like: T-W -\> T-G -\> redBOX is a fine thing. The missing DnsPort on redBOX won't matter. Tor won't know who you are behind the Any, it's an additional hop and even might circumvent when Tor is censored and even might obscure the fact, you are using Tor.
     * (adrelanos) "What do you mean by AnyBOX-\>VPNBOX?" With "AnyBOX" I wanted to create a generic term for "some box", either T-W or any other kind of other gateway.
     * (adrelanos) "VPN doesn't seem to support SOCKS interface so we can't use redsocks. Therefore we'd need forwarding, is that what you meant?" Yes. If we are not going to find a better/other solution.
* (adrelanos) About the multiple gateways "skeleton" I talked about above... If T-G is 192.168.0.1, a ProxyBOX should be probable "192.168.0.1 - 1 something". Perhaps a MultipleGateway should be 192.168.0.199 198 and on. I don't think chaining multiple T-G's in a chain as an exercise is hard. Once that exercise is working, new combinations are possible.
* (anonymous) I don't think that's "correct". I'd use |t-w 192.168.3.2 eth0| \<-\> |t-g 192.168.3.1 eth1; 192.168.4.2 eth0| \<-\> |AnyBOX 192.168.4.1 eth1; 192.168.1.2 eth0| \<-\> |physical router/modem: 192.168.1.1 publicIP wan0|. We probably should replace our default 192.168.0.\* and with a higher number because it is widely used on LANs already and can confuse and complicate setups. You'd need to change the eth0 settings on t-g for that, but otherwise it should just plug in. When changing the order (t-w\>anybox\>t-g) the IPs have to be changed accordingly but otherwise it should just work.
* (adrelanos) Agreed with everything and that's how I liked it to be. We can start a new draft, it's perhaps best placed as Multiple Gateways under OtherAnonymizingNetworks.
     * (anonymous) I don't think we can do a generic anybox, every solution requires different networking and firewall settings. I'd just start with a "redBOX" and then try to chain all 3 in different order.
     * (adrelanos) Yes. Would still be nice if we could call it "Chaining Multiple Gateways" or so and if some changes were generic and some dependent on using proxy, ssh or VPN.
* (adrelanos) This whole discussion can be converted into documentation. I think we recognized, to prevent confusion, it's useful to always describe the connection scheme and the "physical" ordering (that term may be exchanged). And let's call Proxy/VPN/SSH Any or let's make a new term "the AnyAnonymizer" or the "AnyProxy"?
     * (anonymous) I like AnyProxy - got the "An" for anonymitym, though we need to explain that term. I'd also change "connection scheme" to routing scheme or better yet routing order.
     * (adrelanos) Some other ideas: AnyProxy (your idea), AnProxy, AnyAnProxy (Anonymous Any (=proxy/SSH/VPN) Proxy), AnAnyProxy (Anonymous Any Proxy), AnPSVproxy (Anonymous Proxy/SSH/VPN Proxy) or PVS-proxy (Proxy VPN SSH). I'll agree with any of them. We define all terms at the beginning of the article. Also agreed with the term routing order.
 * (adrelanos) Done. https://sourceforge.net/p/whonix/wiki/Advanced%20Security%20Guide/#chaining-anonymizing-gateways

## FEATURE Vidalia by default/Graphical Gateway

-   (adrelanos) Looks good: [Vidalia on the Tor-Gateway](https://trac.torproject.org/projects/tor/wiki/doc/TorBOX/OptionalConfigurations#a2.VidaliaontheTor-Gateway)
    I think we could attract more users, if the Gateway were graphical.
    More people know Vidalia, it's easier to use compared to arm and
    more popular. What about making that default? CLI-only Gateway could
    be optional. Arm can remain installed.
-   (adrelanos) Would require some minor tweaks. 1) Reduce default
    screen to 640\*480 (just to please Vidalia, xterm, arm) and the VM
    window must not be scrolled. 2) poweroff / restart / start vidalia
    right click menu 3) autostart vidalia
-   (anonymous) That pretty much doubles the TCB. Put more users before
    security? We had that discussion some months ago... If you had a
    look at "WhonixÂ²" on the security page you'll know that my vision
    is incompatible with this proposal. But, as I said then, I won't
    stand in the way as long as the more secure custom setups (=build
    from source, "Whonix-Pi") are still working and maintained.
-   (adrelanos) Yes I want this and Short: I don't put security over
    more users. Long answer: Example: [ Mixminion vs
    Tor](http://www.mail-archive.com/liberationtech@lists.stanford.edu/msg00022.html).
    Similar applies here. Mixminion is a high latency remailer, with
    cover traffic, protection against traffic confirmation (end-to-end
    correlation), theoretically more secure than Tor. The problem is
    "theoretically". They couldn't attract enough users and without
    enough users it's equally (in)secure as Tor. That's why they
    decided, to no longer work on Mixminion. Whonix also needs also lots
    of users, to 1) get press/publicity 2) more developers 3) more
    research and audits. 2) and 3) will result in more security. The
    graphical gateway feature in T-G script can be a function, which is
    easy to out comment before using the script. First we attract loads
    of users, get them interested and informed and the ones who want
    more security and easily harden Whonix.
-   (anonymous) I'd argue that the Mixminion vs Tor decision was
    ultimately short sighted and wrong. Mixminion could have been
    significantly improved and had attracted more users by building in
    bidirectional communication right from the start and creating a
    proper front end. Further, by building Mixminion into Tor or on top
    of it, the choice would again have been high, high vs low, low. As
    an alternative to short-sightedness one could let the conspiracy
    guys speak. I'll leave it at that for the off topic. Your argument
    on Whonix misses the point that we are building on the strength of
    Debian/Linux and Tor. Realistically we will get the most security
    improvements by improving the upstream projects. For example. he
    number of actual Whonix users will always be small compared to the
    number of total Linux users. You last line however is a good one.
    Hence, no further objections from my side ;)
-   (adrelanos) Vidalia "default" features (it might be impossible to
    support all of them): start Tor; stop Tor; new identity; network
    map; bridges; modify torrc permanently (comments get lost!)
-   (adrelanos) Vidalia also has some feature "[Tor] Changed=True",
    which I do not understand yet. It might modify Tor temporarily,
    expand torrc permanently or modify Tor through ControlPort once
    Vidalia started.
-   (adrelanos) Vidalia features in Tails lack after short glimpse:
    start Tor; stop Tor. Have they modified Vidalia or is that an
    option?
-   (adrelanos) Harder than I though. For testing "sudo apt-get install
    --no-install-recommends vidalia tor tor-geoipdb" (to prevent
    installing unpatched torsocks)... Will end up with a defunct
    Vidalia, since Tor is run as service/daemon on startup as root and
    drops to user debian-tor. Vidalia expects, by default, Tor to run
    under the same account as Vidalia. We can't run Tor as user "user",
    because by Whonix design, only user debian-tor may establish clear
    connections. User "user" can run apt-get and DNS over Tor. The X
    server, Openbox and Vidalia should (must?) run as user "user". I run
    into permission problems. Tails runs Tor under a different user
    account and runs Vidalia as the desktop user. There is a solution.
    Not sure if Vidalia is suited for Whonix.
-   (anonymous) I suppose you either need
    HashedControlPassword/CookieAuthentication or run vidalia as
    debian-tor
-   (adrelanos) Running as debian-tor works. Do you know how to fix the
    following error...

    No protocol specified
    No protocol specified
    vidalia: cannot connect to X server :0
    
-   (adrelanos) When not using gksudo, kdesudo or similar?
-   (adrelanos) There might be also security consideration when running
    Tor and Vialia under user debian-tor. Might be safer to run Vidlia
    in it's own user account. But these considerations do not severely
    apply to Whonix. With TBB everything, TorBrowser, Tor and Vidalia
    are running under the same account. For better security the whole X
    can be removed.
-   (adrelanos) And even if I set /etc/tor/torrc's permissions to let
    anyone edit it and owner to debian-tor, vidalia still complaints
    about not being able to write to /etc/tor/torrc.
-   (adrelanos) Really hard for me. Not sure if I can get it done in
    time... Tails patches Vidalia.
    [\#4716](/projects/tor/ticket/4716 "defect: vidalia-0.2.15-1~oneiric tries to start a per-user Tor with system-wide ... (assigned)")
    and
    [\#6209](/projects/tor/ticket/6209 "task: Add Vidalia to tpo precise repository (new)")
    are blocking bugs. Problem is, Tor is managed as a service, starts
    system wide, starts as root, drops to debian-tor. Vidalia expects
    Tor to be installed not-system-wide. The start/stop Tor button will
    not work as expected, they use different torrc's.
-   (adrelanos) Tor will listen to the "user" instance, i.e. user
    debian-tor. When Vidalia (running as debian-tor) wants to restart
    Tor, Tor will not start and complain "you already start me as
    debian-tor, don't set user debian-tor then". I will have to look
    further into this...
-   (adrelanos) One thing could work: let Vidalia manage (=start/stop)
    Tor. But I don't like that solution either. Autostart as service
    were no longer possible, custom autostart were required, removal (or
    not installing X, Vidalia were more complicated)... Perhaps no good
    idea, when Tor gets updated, it will enable the default autostart
    hooks again.
-   (adrelanos) Maybe I have a solution... All files (i.e. cached-certs,
    cached-microdescs, control, lock, state, torrc.orig.1,
    cached-microdesc-consensus, cached-microdescs.new,
    control.authcookie, log, torrc) will be placed in /home/user/tor.
    Vidalia, X and Tor run under the same user account.
    -   (anonymous) as long as tor alone, without x and vidalia works
        just the same it's OK for me.

-   (anonymous) For most users, tor will "just work" in the background.
    People who want to tweak it should know what they are doing, they
    then can install vidalia if they want to themselves. As a default
    options it really only makes sense if everything works seamless and
    logically. Does tail achieve that? And second question: is it worth
    the effort to merge their changes into Whonix?
    -   (adrelanos) Yes, Tails archives that. They also have a nice
        [ bridge
        mode](https://tails.boum.org/doc/first_steps/startup_options/bridge_mode/index.en.html).
        I don't know their patches yet. Perhaps they want to forbid
        stopping Tor, because all applications still run on the same
        system.
    -   (adrelanos) chiiph said on IRC, it's a custom patch by Tails,
        which hides Vidalia's start/stop buttons. Since he hasn't seen
        the patch, he doesn't know if he wants to add it upstream. They
        are about to ask
        [ https://tails.boum.org/todo/robust\_and\_strict\_New\_Identity\_feature/](https://tails.boum.org/todo/robust_and_strict_New_Identity_feature/).
    -   (adrelanos) Dunno about further patches.
        -   (anonymous)
            [ http://git.immerda.ch/?p=tails\_vidalia.git;a=tree;f=debian/patches;h=094c1722d47fd758e5526eb196e6984dfcfe252b;hb=HEAD](http://git.immerda.ch/?p=tails_vidalia.git;a=tree;f=debian/patches;h=094c1722d47fd758e5526eb196e6984dfcfe252b;hb=HEAD)

-   (adrelanos) Still not sure if it makes sense to add Vidalia. Yes, it
    looks nice, has an integrated torrc editor... But... One drawback
    with Vidalia 0.2.15 remains... As soon as you edit torrc with
    Vidalia (i.e. add non-obfuscated bridges, all comments in torrc get
    lost, i.e. comments how to add obfuscated bridges get lost.). I'll
    look into Vidalia 0.4... Update, there is no 0.4, only 0.3.x. I'll
    look into that one.
    -   (anonymous) well, that's a bug and should be reported.
    -   (adrelanos)
        [\#5475](/projects/tor/ticket/5475 "defect: Vidalia torrc editor is confused by # comments (closed: fixed)")
        will be fixed in Vidalia 0.3.2-alpha. Update: the torrc editor
        in 0.3.2-alpha is good.
    -   (proper **Vidalia 0.2 can not be used. Not being able to edit
        torrc is a blocker.**

-   (adrelanos) Functions which must be tested. All tests using
    0.3.2.-alpha. (Only tested locally, no image build yet.)
    -   Tor running as User "user".
        -   Impossible. IRC: proper: "service tor stop" and "service tor
            status" do not work when User in torrc is anything else than
            debian-tor? (ubuntu precise, Tor v0.2.3.17-beta) expected?
            known bug? \<not sure allowed to post name\> proper: That's
            a security feature, to keep whatever can write to tor.pid
            from tricking root into killing processes running in other
            user account

    -   cli: sudo service tor stop
        -   Working

    -   cli: sudo service tor start
        -   Working

    -   Vidalia: connect to existing Tor (started on startup as service)
        -   Working

    -   Vidalia: start Tor (if closed with sudo service tor stop or
        Vidalia stop tor)
        -   Impossible.
        -   ~After\\ *sudo\\ service\\ tor\\ stop*...\\ Trying\\ to\\ start\\ Tor\\ with\\ Vidalia\\ will\\ fail.~

            Warning Error setting groups to gid 118: "Operation not permitted".
            Warning If you set the "User" option, you must start Tor as root.
            Warning Failed to parse/validate config: Problem with User value. See logs for details.
            Error Reading config failed--see warnings above.

    -   Vidalia: stop Tor
        -   Impossible.
        -   When Tor is autostarted (as service), or started with *sudo
            service tor start*... If you try to terminate Tor using
            Vidalia, the output will be: "Vidalia was unable to stop the
            Tor software. Vidalia has not started Tor. You need to stop
            Tor through the interface you started it.".

    -   Vidalia: edit torrc
        -   Working.

    -   Vidalia: tor log
        -   Working.

    -   Vidalia: add (non-obfuscated bridges)
        -   Not yet tested.

    -   Vidalia: add obfuscated bridges
        -   Not implemented yet. There is somewhere a ticket.

-   (anonymous) (old TODO): openbox menu entries, autostart X
-   (adrelanos) This ticket is outdated. Vidalia 0.3 won't come. No one
    working on it anymore and because it's C/Qt based, it seems
    unattractive/unlikely that someone will take over. It's more likely
    someone is going to create a python rewrite of Vidalia.

## OPTIONALFEATURE Freenet Support/FreenetBOX NEEDS_INFORMATION

* (anonymous) Freenet could also be installed on t-g and accessed from t-w. UPDATE: or not...? There's the option to have more locked down webinterface that doesn't expose admin/debug/... functions
* (adrelanos) (Freenet homepage: [with www](https://www.freenetproject.org) has SSL error. Use the version [without www](https://freenetproject.org), no SSL error.)
* (anonymous) AFAIK Freenet in opennet mode isn't quite as secure as i2p and Tor, then there's the problem how to configure it securely, there's some kind of proxy support in Freenet but how mature and how secure?
     * (adrelanos) You mean fproxy?
     * (anonymous) Not sure what it's called. I meant like that freenet proxy web site you posted, you enter keys and download stuff. Only the website would run on t-g, not a remote server. I know there's such a feature already built into Freenet webui.
     * (adrelanos) Well, a freenet gateway. Like a i2p inproxy. That's very useful, unfortunately, I searched extensively, and there are no more working freenet gateways.

* (anonymous) Ideally we'd tunnel it over something, i2p supports udp but then we could only reach other freenet nodes also running over i2p. i2p is said to get a data store that's similar to freenet but more secure than opennet.
     * (adrelanos) You mean, run i2p on T-G and run Freenet on T-G or T-W? Both options seem possible. I know fproxy may run on another computer. What I haven't found yet, are any proxy/socks settings in freenet, do you have a reference for that? Or do you mean transparently tunnel it?
     * (anonymous) Transparently tunnel it. But as I said, it's pointless because you could only connect to i2p (or onioncat) users and freenet is small and slow enough as it is.
     * (adrelanos) Well, if we could still access the whole freenet content and not only the i2p fraction, that still would make sense. Regardless of speed, it can run in background and continue downloads. If it's only 3 times slower I would still interested to see what content they offer.
     * (adrelanos) New idea: Tunneling UDP over Tor. (See topic below.) If we get this done, we can use it for freenet. Freenet security settings: lowest possible, highest speed (like for i2p); (reason: Tor offers already security).
     * (adrelanos) [Freenet over Tor](https://trac.torproject.org/projects/tor/wiki/doc/TorBOX/OtherAnonymizingNetworks#FreenetinsidetheTor-WorkstationFreenetoverTor) works, if you have a VPN behind Tor, which does not block UDP/freenet. This is done.

* (adrelanos) About the idea with the FreenetBOX, where Freenet is running on Tor-Gateway. Freenet is a background process and the browser is only used to access the webinterface. When freenet were to run on T-G, the cache and all downloaded files were also stored on T-G. The only real advantage, users were encouraged to use the Tor Browser and if they follow any links on freesites to normal internet, they were protected by Tor. If the Tor-Workstation can't access the downloaded content it would be pretty pointless. How it could access it? Afaik you can't download through the browser, the browser only tells freenet what to do. We'd need to enable T-W access on T-G's freenet download folder. And the question again, if the freenet webinterface could be locked down enough to prevent T-W from getting the external IP address.
* (adrelanos) We could contact the Freenet guys, if they are interested and to get the answers.

## OPTIONALFEATURE I2P Support WAIT/LOOKING for contributors/more mature upstream

* (anonymous) i2p could only used in addition, not as a replacement for tor: apt-get needs tor, there are no i2p mirrors for any distro. IRC is covered, web not really, i2p eepsites are too limited. i2p would need to run on t-g, i know it's possible but it's not just a simple "apt-get install i2p".
     * (adrelanos) Indeed only as an addition. I also see now way to use it as a replacement. I2p has outproxies (http, https, socks). Unfortunately, there are only a very few of them and those are very unreliable. It would be next to impossible to use them for reliable operating system updates. On the other hand, if it were to work, i2p is designed for such big file transfers.

* (adrelanos) I made myself familiar with i2p inside T-W, at least inside there, I feel safe. New site: [OtherAnonymizingNetworks](https://trac.torproject.org/projects/tor/wiki/doc/TorBOX/OtherAnonymizingNetworks) (also about i2p inside T-W). Also the topic i2p on T-G stays interesting.
* (anonymous) gpm and links/links2 works for quick web interface interaction on t-g.
     * (adrelanos) Good idea.

* (anonymous) I've tested i2p in t-g, older CPU, 256 MB RAM should suffice, with Tor and i2p active it hardly goes over 120 MB (non-cache) RAM. But I was pretty disappointed by the performance of i2p. Firewalled but with \>10 peers eepsites are considerably slower than .onion sites. There are some servers that have both an i2p and an onion address which I used to test. It's not so much throughput (I tried well seeded torrent and it was pretty acceptable) but latency and stability of the connection are a problem: frequently it would time out and complain about congestion/server down (while the server was fast and working over the tor address). Contrast that with their "Designed and optimized for hidden services, which are much faster than in Tor" [http://www.i2p2.de/how\_networkcomparisons](http://www.i2p2.de/how_networkcomparisons) All inproxies I found are dead: i2p.us i2p.to i2p.tin0.net "eepsite darknet" is much smaller than the "onion darknet", the whole thing after all these years still feels more like 
proof of concept than a viable alternative for at least a subset of the things people use the clear net for. The only interesting thing is torrents/p2p but I only found one tracker with a small community. Basically I pretty much lost all interest in i2p again. It could be a replacement for Tor if 1) performance was at least as good, 2) there were a lot or stable and fast outproxies, java is no longer a counter argument and if 1 and 2 were fixed I'm sure content and users would follow. But without these two it would only be an addition to tor, significantly make Whonix users more discoverable and vulnerable but not bring any features except for torrents. All in all not worth the investment currently.
     * (adrelanos) Interesting test and opinion. We also don't need scripting support everywhere, we don't have that for all optional configurations as well. A small explanation of the steps is sufficient. Anyway, if we are not motivated enough, we don't have to add it. The least we can do, is informing them in their forums about the possibility. Would be a waste, if someone creates a clone of Whonix for something which is very similar. After posting in their forums we will see if someone contributes.

* (adrelanos) [Contacted i2p](http://forum.i2p2.de/viewtopic.php?t=7037).
     * (adrelanos) Barely any interest.

* (anonymous) there's proxy support, by default only listening on localhost, config at .i2p/i2ptunnel.config We should ask on the forum if their proxy support fits our threat model (i.e. can be reasonably trusted to not leak or disclose the external IP to T-W.
     * (adrelanos) Small clarification for any other readers. They do not have proxy support in sense of tunneling over http or socks. (Source: Google site:i2p2.de socks) They only support a http proxy for "reseeding" (bootstrapping). (Source google cache: trac.i2p2.de/ticket/22) However, as I have already described, transparently tunneling i2p over Tor works. And what you said above is still valid, but another kind of proxy support. i2p were to run ton T-G and T-W would access that proxy that i2p provides for the browser to access .i2p domains.
     * (anonymous) But they do, http proxy on 4444, it proxies http over false.i2p outproxy and eepsites are resolved. there's a separate https proxy. What they don't have is a transparent proxy, dns proxy...

* (adrelanos) Minimal interest/help from the i2p community. We have i2p over Tor and inproxies, sufficient for me alone. If we are not going to implement it, it won't happen. I propose new status: CLOSED / STALLED. We do not reject the feature. If someone wants to do it, fine, otherwise, not going to happen.

## OPTIONALFEATURE Proxies as Tor replacement/ProxyBOX WAIT for feature: Multiple Gateways

* (adrelanos) I spitted up the JonDonym related part. JonDonym is just another local http (free) or optional local socks (premium) proxy. Getting proxy support done, automatically also gets JonDonym support done.
* (anonymous) let's merge with the other ticket?
* (adrelanos) Can do.

### JonDonym

* (adrelanos) JonDonym over Tor guide is written (JonDo inside T-W). That one was easy.
* (adrelanos) JonDonym also supports tunneling UDP, only for premium users, what is a shame.
* (adrelanos) JonDonym can be used as a Tor replacement. While JonDo is less secure, won't expose IP to T-W.
* (anonymous) Not really interested in "supporting" (=recommending) a commercial system. Is the "free version" capable enough for a real replacement (overlooking the security/trust issue)?     * (adrelanos) Answered in the wiki article now.

* (adrelanos) Theoretically it would be possible to tunnel Tor through JonDo-free (torrc: ReachableDirAddresses \*:80; ReachableORAddresses \*:443).     * (adrelanos) That wouldn't make much sense. If one wants to do so, they recommend the other way around. Tunneling JonDo trough Tor.

* (adrelanos) [ContactedJonDo.](https://anonymous-proxy-servers.net/forum/viewtopic.php?f=10&t=6680&sid=24b1980990c5ae69e021bc998c878370)
     * (adrelanos) That was fast. We got two answers by JonDo admins. Friendly, helpful.
     * (adrelanos) Updated the [Whonix JonDonym wiki topic](https://trac.torproject.org/projects/tor/wiki/doc/TorBOX/OtherAnonymizingNetworks#UsingJonDonym).
     * (adrelanos) Still waiting for their announced wiki article "how to use JonDonym as transparent proxy".
     * (adrelanos) They posted help [how to use JonDonym with transsocks](https://anonymous-proxy-servers.net/en/help/transocks.html).
     * (adrelanos) Still in contact. Their developers answer all questions and are helpful. It looks like Whonix and JonDonym are compatible. Free users may be able to use services on port 80/443 and premium users everything. JonDonym may replace Tor, of course only optional. Let's see what comes up. Maybe they come up with their own JonDoBOX some day, add new features, review, etc. Both projects profit.
     * (adrelanos) With free cascades: some progress (see tunnel transparent proxy in whonix documentation in tunnel proxy through tor page) I've been able to connect to http on port 80, but not be able to connect to http**s** on port 443. That's a strange issue. When using JonDo as http proxy, http and https are supported. When using the http proxy as transparent proxy (with help from privoxy) https gets broken.
     * (adrelanos) Contact with their devs stalled. Over all development of that feature stalled as well. TODO: I should try with redsocks.
     * (adrelanos) Everything with free cascades... redsocks has to be set to http-relay ip 127.0.0.1 port 4001. Both, redsocks and jondoconole running under user account redsocks. Iptables redirect into redsocks, redsocks to http-relay. http-connect will not work. Viewing http sites works, viewing https sites does not work for some reason. Redsocks output: "accepted, malformed request came, httpr\_toss\_http\_firstline, dropping client". Update: asked their devs explicitly if they are interested in allowing free users to use transparent proxying. If there is no response, that will be a "no" and I don't think ever find out how to do it (for https, http works).

### proxies

* (adrelanos) Also added a [proxy](https://trac.torproject.org/projects/tor/wiki/doc/TorBOX/OtherAnonymizingNetworks#Proxy) section. Thanks to the JonDo devs, we have almost complete instructions for using any socks proxy as Tor replacement. Not done yet, documentation needs to be tweaked and needs testing.
* (adrelanos) There has been some progress. Whonix/OptionalConfigurations\#TransparentProxying is about additional transparent proxying through an extra proxy (user -\> Tor -\> proxy) on T-W but as soon that works well, it can be used as a replacement for T-G as well. Biggest remaining open issue is, that I haven't found out how to remotely resolve DNS through a proxy, while there is no DnsPort and while not using a public DNS resolver. I am not sure that is possible at all. Asked on [redsocks mailing list](http://librelist.com/browser/redsocks/2012/5/15/transparent-proxy-dns-without-public-dns-server/).
* (adrelanos) transocks\_ev is a similar redirector for trans2socks. The [transocks\_ev readme](http://oss.tiggerswelt.net/transocks_ev/README) mentions DNS but it's not done. I mailed the author and he told me, that transocks\_ev does not support UDP and therefore no DNS yet (Mai 2012).
* (anonymous) progress? roadmap?
* (adrelanos) Quite some progress, [1](https://trac.torproject.org/projects/tor/wiki/doc/TorBOX/OtherAnonymizingNetworks#Proxy); [2](https://trac.torproject.org/projects/tor/wiki/doc/TorBOX/OptionalConfigurations#TunnelingproxythroughTor). Roadmap: Not a high priority. It works within T-W. I am afraid to do more thoroughly testing on a standalone ProxyBOX-Gateway (i.e. ProxyBox-Workstation -\> ProxyBOX-Gateway). That is because I don't want to connect to anything, without using Tor. I therefore postponed that feature, until multiple gateways are documented. And that can be done after Whonix 0.2.0 release.

## OPTIONALFEATURE VPNs as Tor replacement/VPNBOX WAIT FOR FEATURE: Multiple Gateways

* (adrelanos) The VPNs are far more widespread than Tor. VPNs are good for people with lower anonymity needs and are faster. We already provide documentation, to tunnel VPNs through Tor. [Tunnel Tor through VPN](https://trac.torproject.org/projects/tor/wiki/doc/TorBOX/OptionalConfigurations#TunnelTorthroughVPN) needs revision. Solution might be to modify route with pre-up (delete default route). I am currently searching the answers. VPNs can be added to [Other Anonymizing Networks](https://trac.torproject.org/projects/tor/wiki/doc/TorBOX/OtherAnonymizingNetworks). Not sure how that could be done best, can we avoid enabling IP forwarding? How to call it? The term VPNBOX would have been nice, it's already taken on Google.
* (anonymous) VPNBox is, VPNBOX isn't ;) Hereby I officially declare, on the 18th April 2012 AD, VPNBOX was "taken" by the Whonix Project. We won't sue you if you "steal" our name but know that it's bad for your karma. So, I think we've got that covered.
* (anonymous) About the technical aspects, I can't help with that. I needed to do my research myself first. One question though about VPNs, you wrote "It has the additional effect of making all your different kinds of traffic look similar to an eavesdropper." What do you mean by that?
     * (adrelanos) Actually I only reformated (newlines) an existing text, without reading it, because the preview of that page was messed up for this reason. The text is there since ages. The text is not so important, do with it whatever you decide.

* (anonymous) Why would anyone be interested in a VPNBOX? The design has two big advantages: security and making it easy to use arbitrary applications anonymously. The first one doesn't apply because someone who's using only a VPN already expressed to not really care about security that much. The second doesn't apply either because VPN can be easily set up to transparently tunnel any application (it's even easier than Whonix because of UDP support).
     * (adrelanos) Not sure, no one is interested. There are even companies who sell snakeoil [list](https://torrentfreak.com/how-to-make-vpns-even-more-secure-120419/) (ex: killing applications on VPN breakdown, already described in other anonymizing networks article). Additionally VPNBOX offers good protection against IP leaks, even when the Workstation gets rooted. It would be a nice service to document or provide a preconfigured safe setup. Finally it's supposed to find more developers and users. If other developers take up our idea and start JonDoBOX, i2pBOX, VPNBOX, also Whonix would ultimately benefit (more features, more audits, etc.).

* (adrelanos) Low priority. Waiting for feature: Multiple Gateways.

## OPTIONALFEATURE Read Only/Portable/Live System LOOKING FOR CONTRIBUTOR

* (anonymous) Live CDs have certain advanatages which in some user cases make them better suited despite all their issues. How to: [http://myhowtosandprojects.blogspot.com/2008/07/live-cd-from-your-in-installation.html](http://myhowtosandprojects.blogspot.com/2008/07/live-cd-from-your-in-installation.html)
* (adrelanos) Do we need a real Live CD (why?) or is it sufficient to disable persistence, i.e. all changes to the hdd go to the RAM and are cleared after poweroff and restart.
* (anonymous) true, live cd's are no longer the portable OS of choice (usb/sd is). how to: [https://help.ubuntu.com/community/aufsRootFileSystemOnUsbFlash](https://help.ubuntu.com/community/aufsRootFileSystemOnUsbFlash)
* (adrelanos) Do you propose Whonix-Workstation's operating system should be optionally a Live OS or do you propose whole Whonix as Live OS?
* (anonymous) I'd propose an OneVM based system which can on boot up be instructed to either act as a client to another PhyIso Gateway or to start Tor on the host itself. If we only care about Whonix-Workstation (which already got non-persistence covered) we haven't solved the actual issue: the host would still save data to the disk which we have to worry about. If a PhyIso gateway is used it probably doesn't have to be read only, it only has to mount tor cache and log dirs in tmpfs and not use a swap (which we don't and isn't necessary).
* (adrelanos) Design decision: *using Tor cache* or *not using Tor cache*
 
     * (adrelanos) If using Tor cache you can make of Tor's "long term brain" which enables essential security improvements in Tor's core: entry guards. Without cache there are no entry guards. That's the typical Live CD approach. I don't know if Tails with its new persistence feature for USB does store the Tor cache.
     * (adrelanos) Hard to decide... Depends on someone's individual threat model. Do you rather expect your adversary to use malicious entry guards or would you rather hide the fact, that you used Tor/Whonix *from hdd analysis*.
     * (anonymous) It's not about hiding that you use Tor. You aren't going to swallow CDs or even SDs, that's obstruction and destruction of evidence. If the storage media holding the tor executable is encrypted you haven't solved anything. You'd have to download tor itself, anonymously, into RAM - without having Tor available. That's simply impossible. The goal of the proposed enhancement is primarily protecting communication data.
     * (adrelanos) To get both: we could simply start Tor with new entry guards, download our old Tor cache from a hidden service storage (stored there in encrypted form), decrypt, put in cache, restart Tor, use old entry guards. That's probable difficult to implement. But a worthy goal. That anonymous encrypted storage could also contain other configuration files and hidden services.
     * (anonymous) If that's built into Whonix the next question is going to be: give us the key to your "cloud". The entry guards are not the problem, they are pretty public (ISP/VPN sees them), we can store them unencrypted (or encrypted and hand out the keys). I'm only worried about cache files that could reveal whole circuits or even destination addresses. Tor devs would have to fill us in on the details here. Entry guards are only a protection against weak adversaries which usually do not have the legal and physical force that necessities such precautions. Strong adversaries already control or can monitor your permanent "entry 
node" (ISP), I'd guess they wouldn't care either way, if anything, more stable and predictable circuits make timing, end to end and tagging attacks easier.
     * (adrelanos) Recent discussion with better solutions: [tor-talk Location-aware persistent guards](https://lists.torproject.org/pipermail/tor-talk/2012-October/025975.html)

* (adrelanos) You essentially propose Whonix to be Amnesic. There are different levels for being amnesic.

     * (adrelanos) One easy thing we could and should do either way: encrypt the USB HDD. People in sane areas who do not get forced to give out there passwords can not be proven, they have used Whonix. Those who have used obfsproxy or other means of hiding Tor use can not even be proven to have used Tor. Next points assume password has been given out.
     * (anonymous) In the standard Whonix encryption is already recommended and left to the user (as we do not control the host OS). It can also already be installed to external medias without having to change anything. (SD, USB, eSATA)
     * (adrelanos) If we are going to deploy a read-only medium, we should probable deploy the whole host and apply encryption by default.
     * (anonymous) Uh, I think you will notice that is impossible. One can't preinstall a "secret" key...
     * (adrelanos) Only option: Doing it like the Tails USB creator. An installer creates and encrypts the device.
     * (adrelanos) We can prevent getting any activity in Whonix-Workstation to be ever written on disk.
     * (anonymous) unless enforced by hardware, software can still circumvent software write blocks. Whonix threat model includes remote code execution as root. SD cards have a write lock, CD/DVD-R are save too. For everything else you'd need something like tripwire from a trusted medium.
     * (adrelanos) No. Only Whonix-Workstation is not to be trusted in our threat model. The Whonix-Gateway and Whonix-Host are trusted. If they enforce, that all written changes go to the RAM, no read-only hardware is required. (Although recommending read-only devices for a defensive in depth is a good idea.)
     * (anonymous) I', talomg about Physical Isolation. The VM based isolation between Host and Workstation is weak. If the latter is compromised the former can be relatively easy too. The notion untrusted is not really accurate any more, it's more of a security redundancy: still offer security if one of the two is comromised (I'
ll expand on that on the security page, essentially neither T-G nore T-W are fully trusted or untrusted, it's more like 50:50). The host is a bit more trusted and should guard hardware serials but that's it. Offering a tamper resistand host is still very desireable.
     * (adrelanos) We can prevent writing to the whole USB disk (once installed) and hide (from local hdd analysis (!)) Whonix ever got started. (This disables Tor cache and entry guards! Unless we use the workaround I described above.)
     * (adrelanos) We can also torify the Whonix-Host traffic to prevent any kind of Whonix-Host specific network fingerprint.
     * (adrelanos) Conclusion: if we include all those levels... When they use obfsproxy (assumed it does its job or other means), they can use all features (entry guards, hidden services), it can not be proven they used Whonix/Tor and if they reveal the password it only proves they installed Whonix at some point.
     * (anonymous) It's in the name, "obfuscation", it's not a "stegoproxy" (which I doubt is possible at all for bi-directional channels). All the schemes to hide the fact that you use tor are weaker than tor itself. Against strong adversaries they can only help with your perceived security (false sense).
     * (adrelanos) obfsproxy is not perfect. If it were easy to detect, hosting Tor based on private obfsproxy bridges were pointless, but it's not. There are great developments in this area, like SkypeMorph or the system, where the webserver/ISP helps, connection looks like normal http, unfortunately forgot the name. Kinda perfect stenography. That's up to the obfsproxy/transport plugin people. Talking 
about strong adversaries makes no sense, you could argue that whole Tor has no point then.
    * (anonymous) Yes, that's my point. My personal interest in Whonix is fixing that... (see Security page). Something like SkypeMorph is a lot more interesting than the obfusproxy (although skype crypto is broken so the implementation is broken too and there's ample room for timing and traffic ananlyis that would probably reveal it's hidden use). However, such methods require a friend to friend network (like Freenet darknet), there is no such infrastructure for Tor yet - though there is no reason it wouldn't work. The real problem is, you are hiding traffic in encrypted traffic. In restricted environemts all encrypted traffic (but whitelisted destinations like banks and .gov) may be blocked completely. A strong stego solution should still work, e.g. post to flickr, youtube... but such methods are always high latency and one-directional and therefore incompatible with Tor.
     * (adrelanos) If I understand correctly, skypemorph could also be implemented as a plugin for obfsproxy and if not, obfsproxy needs to be updated. See [https://www.torproject.org/docs/pluggable-transports.html.en](https://www.torproject.org/docs/pluggable-transports.html.en) for even more stuff in development. Another promising: https://telex.cc/ - it would look like you connect to a legitimate website (anypage.com) and with help of the website server's ISP providing stenography and some magic you get forwarded to the Tor network. If I remember correctly it required some ISPs (or websites) to cooperate.

-   Latest statements: [https://sourceforge.net/p/whonix/wiki/FAQ/\#will-there-be-a-whonix-live-cd-or-dvd](https://sourceforge.net/p/whonix/wiki/FAQ/#will-there-be-a-whonix-live-cd-or-dvd) and [https://sourceforge.net/p/whonix/wiki/FAQ/\#is-there-something-like-whonix-live](https://sourceforge.net/p/whonix/wiki/FAQ/#is-there-something-like-whonix-live)















# Footer
[[include ref=WikiFooter]]