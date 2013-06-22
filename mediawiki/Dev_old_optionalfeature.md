[ Main Article - Whonix][TOC]

[Dev/ArchivedDiscussion ArchivedDiscussion]

= OPTIONAL FEATURES =

== be a (obfuscated) bridge or (exit) relay [OPTIONALFEATURE] ==

* (adrelanos) Add optional instructions how the Tor-Gateway can be configured as either a (obfuscated) bridge, a relay or an exit relay. Configuration of torrc on Tor-Gateway needed, forwarding from host to VM, forwarding from router to host. Link information for further reading.
* (anonymous) as explained some days ago with hidden services, no iptables changes are necessary. The ordinary bridge how tos will just work.
* (adrelanos) Not done yet. There is a Tor Obfuscated Browser Bundle with a list of public known obfuscated bridges. Not much to come, but how to get that list, link to compile obsfproxy or how to extract from that bundle. I'll do it soon and close afterwards.
* (adrelanos) This answer was in the wrong place. It was about how to use (obfuscated) (private) bridges, that's done now.
* (adrelanos) It's correct that the normal guides how to host an (obfuscated) (private) bridge or (exit) relay are the same. What's missing is a port forwarding from the host to the VM. Shouldn't be much work.
* (adrelanos) [OptionalConfigurations#hostingaprivateobfuscatedbridgeorexitrelay Done.]

== More than one Tor-Workstation [OPTIONALFEATURE] ==

* (adrelanos) it is quite simple to use more then one Tor-Workstation. Each new one needs only minimal changes in IP configuration. I'll probable add it under misc soon.

== How to tunnel through VPN, proxy, SSH first (VPN/proxy/SSH -&gt; Tor) [OPTIONALFEATURE][IMPLEMENTED] ==

* (adrelanos) add optional step: how to tunnel through VPN, proxy, SSH first (VPN/proxy/SSH -&gt; Tor)
* (anonymous) I've moved these 2 to do items as they are non-essential:
* (adrelanos) I am not sure how many people are affected by this, more in the more restrictive countries.
* (adrelanos) One reason is, some people are forced by their ISPs to use a VPN (such as some Russian ISP) or proxy (many providers).
* (adrelanos) Another reason is that one can use VPN/SSH/proxy to circumvent Tor blocks.
* (adrelanos) Or to hide the fact that they are using Tor. (proxy usage discouraged, only if no deep package inspection by ISP)
* (anonymous) Agreed, undone ;)
* (anonymous) A howto for Proxy-&gt;Tor isn't very necessary. It works the same as a stand alone VPN/SSH/Proxy set up with only one exception: No UDP. The other way round is more interesting IMO. For example we could add a 3rd VM which could protect even if Tor/Tor-Gateway was compromised. But this again is no different from a standalone VPN gateway. Only if we set up proxy on Tor-Gateway there's the potential for conflicts and we should cover that. It would be still nice and helpful to at least give some hints and link to more detailed resources.
* (adrelanos) I do not think we need a VM-3... Here are some starts to implement this...
* (adrelanos) Tunneling Tor through SSH first. SSH tunneling looks not so hard, see [https://help.ubuntu.com/community/SSH/OpenSSH/PortForwarding ubuntu wiki].
* (adrelanos) Tunneling Tor through proxy first. Seams easy. [https://www.torproject.org/docs/tor-manual.html.en link 1][https://trac.torproject.org/projects/tor/wiki/doc/TorFAQ#MyInternetconnectionrequiresanHTTPorSOCKSproxy link 2] - [#Step4x:connecttoproxyVPNorSSHfirstthenconnecttoTorOPTIONAL DONE]
* (adrelanos) Tunneling Tor through VPN... No simple solution yet in my mind, VM-3 method might work, but something simpler would be appreciated.
* (smarm) Working on this.
* (smarm) First get PPTP VPN inbound for local network connections
* (smarm) No connections from the Internet
* (smarm) Allows TorBox to become more flexible (now the local LAN either behind the TORbox or those that are routable to it, can use it)
* (smarm) Then PPTP VPN for outbound connection (PPTP client)
* (smarm) Proof of concept for other more complex / modern technologies
* (smarm) Then OpenVPN inbound (local network only first)
* (smarm) Then OpenVPN outbound
* (smarm) PPTP was chosen for its wide install-base and ease of deployment
* (smarm) Other VPN technologies (L2TP, PPPoE, etc) can be folded in later if need be
* (smarm) OpenVPN chosen for its attention to security and general awesomeness (if TorBox is ever going to accept VPN connections from the Internet, it should be via OpenVPN)
* (adrelanos) Great, my VPN related writing is rather rudimentary, if you feel up for it, feel free to kick out my implementation. I'd just prefer to include a explanation for what VPN is used (forced by ISP, anonymity, etc.).
* (smarm) PPTP server done + folded into instructions. + Brief discussion of VPN usage to enhance freedom and free speech ([http://en.flossmanuals.net/bypassing-censorship/ch025_what-is-vpn/ How to Bypass Internet Censorship @ Flossmanuals.net])
* (anonymous) should be moved. this is only an argument for &quot;tunneling tor though vpn&quot; not using a local gateway and connect to that using insecure pptp.
* (smarm) PPTP with no routing or NAT. Was quite easy after a LOT of brainstorming and research. Should not impact security as the firewall rules only exist on the system as long as the PPP connections are active, the firewall rules are exactly the same as seen in [https://trac.torproject.org/projects/tor/wiki/doc/TransparentProxy#AnonymizingMiddlebox TransparentProxy], but used with PPP interfaces on the system rather than Ethernet interfaces.
* (adrelanos) That is great. I moved your text to [#Step4x:connecttoproxyVPNorSSHfirstthenconnecttoTorOPTIONAL Step 4x: connect to proxy, VPN or SSH first; then connect to Tor (OPTIONAL)]. Hope you are okay with that? I thought that step should be there, because if someone wants to use it, it's the first thing they have to think about and to do? It should be even done, before installing Tor, otherwise they either couldn't even download Tor or their ISP would already know, they use Tor. This needs further adjusting. Your text was made in addition to the final setup, but I think it should be done at the very beginning.
* (adrelanos) The proxy part is already done and the SSH part is partially done. You did well with the VPN section.
* (smarm) Connecting to a VPN provider via PPTP is trivial, pptpclient &amp; configure. I've done it before to verify there are no &quot;leaks&quot; when not able to connect to the VPN. So branching that out to TOR should be okay.
* (smarm) The VPN server thing is the other half and more in the realm of increasing the usability of TorBox overall, rather than increased security directly. Additional users that can connect to a correctly configured TorBox have added security they wouldn't have had before.
* (smarm) Think: You want to get your roommate connected to Tor but she doesn't know how to do Linux / networking / etc, But does know how to connect to a VPN. So we use this (PPTP VPN) to get them connected and secure.
* (adrelanos) PPTP would imho only make sense inside LAN, as it hasn't got best reputation when it comes to security, but maybe it's still secure enough in real world. But when you are in LAN, you can also simply use the gateway server? [https://trac.torproject.org/projects/tor/wiki/doc/TorVPN TorVPN] was my previous project, but when supposed to be used over WAN, then better use a secure VPN implementation, such as OpenVPN.
* (smarm) They can take advantage of your secured TorBox without even the basics steps already listed as long as you can follow these directions.
* (adrelanos) I think for now, we got all the most important stuff. Therefore done and closed.

== DNS dnssec [OPTIONALFEATURE][REJECTED] ==

* (adrelanos) Not sure if we can add [https://en.wikipedia.org/wiki/Domain_Name_System_Security_Extensions dnssec]. [https://addons.mozilla.org/en-US/firefox/addon/dnssec-validator/ dnssec firefox addon], it should not leak inside Tor-Workstation, beside browser fingerprinting. Needs research.
* (adrelanos) Even without Tor this doesn't make much sense yet. Only a very few websites provide this feature. Dnsssec would have to be implemented in Tor first and it would have to be more widespread.

== OnionCat [OPTIONALFEATURE][REJECTED] ==

* (adrelanos) '<sup>2</sup> ICMP, ping, VOIP calls (in theory, untested), etc. [https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO?version#425#AboutOnionCat OnionCat could overcome these limitations]'
* (adrelanos) Research is needed onioncat could be implemented in Tor-Gateway to transparently proxy UDP, ICMP, IPv6. I doubt it, that would be somewhat revolutionary.
* (adrelanos) As far my research gone, both parties need to setup onioncat, it's not very generic. I see no use in Whonix. If someone has another opinion, go ahead. Closed for now.

== IPv6 on loopback on Tor-Gateway [OPTIONALFEATURE][REJECTED] ==

* (adrelanos) Tails allows IPv6 on loopback. Isn't required yet on Tor-Gateway, the Tor-Workstation is free to do that.
* (adrelanos) As most applications run inside the Tor-Workstation, IPv6 on loopback does not yet seem to be needed on the Tor-Gateway. Because it's easier to disable IPv6 on gateway completely, I closed this.

== Polipo [OPTIONALFEATURE][REJECTED] ==

* (adrelanos) Tails uses [https://trac.torproject.org/projects/tor/wiki/doc/SupportPrograms/Polipo Polipo], I can't help myself, but I fail to see if we would get any read advantages? We do not need any http -&gt; socks transformation. If it's not for security, but speed, then perhaps as an optional step. For now I am not going to implement it.
* (adrelanos) It wouldn't need to be implemented on the Tor-Gateway. It could be even optionally installed on the Tor-Workstation. Still not sure about the benefits.
* (adrelanos) Whonix's Tor Browser (Tor Browser Bundle, without Tor/Vidalia) should be as close to the normal Tor Browser Bundle as possible. That's why I wouldn't officially recommend using Polipo. I do not know the implications for browser fingerprinting, if we add a caching browser, while the Tor Browser Bundle users, do not use it. The felt gain in speed was minimal. If someone really wants to use Polipo he can simply install it inside the Tor-Workstation and add the settings, instructions are available Ubuntu support pages. Therefore Closed.

== Tor-Gateway with only one network card [OPTIONALFEATURE][REJECTED] ==

* (adrelanos) This would be interesting for real hardware, where only one lan port or only one wifi adapter is available. Can you think of a method using only one network card, without loosing (much) security?
* (anonymous) not possible. how do you connect 3 devices in a line topology if every device has only one port? you could only attach &quot;Tor-Workstation&quot; and &quot;Tor-Gateway&quot; (their physical counterparts) to a common router but then Tor-Workstation can bypass the gateway (app layer exploit) and the whole point of doing Whonix in the first place would be lost.
* (adrelanos) I'll see. Maybe the router would need to be configured, in a way to allow only LAN for the Tor-Workstation, but LAN and WAN for the Tor-Gateway. You think that is reliable? In any way, this would add a new disadvantage, the router as an additional attack surface.
* (anonymous) That would work but I don't think reliably. How many people have a router that supports advanced firewalling rules (or can be flashed with Linux firmware)? Add to that that even if such firmware is used it's not exactly very trustworthy code you'd have to depend on. Most open source based firmware contains binary code, the releases aren't signed, security updates rarely happen and are even less often deployed. Embedded security is a messy topic.
* (adrelanos) You're right. Ok, thanks, resolved.

== Using one VM instead of two [OPTIONALFEATURE][IMPLEMENTED] ==

* (anonymous): Maybe we should mention that this is possible. Potential problems, (dis)advantages? http://www.howtoforge.com/how-to-set-up-a-tor-middlebox-routing-all-virtualbox-virtual-machine-traffic-over-the-tor-network
* (adrelanos): We could add this to similar projects. I just moved the similar projects page to this Whonix/dev. There are so many different approaches to implement it. One even implements a torified Tor user account on Windows. The similar projects list has already almost 15 links (can add more). Not sure if we should mention all the different methods. Certainly not explain all. Maybe write an small new wiki site devoted to that topic and link it from the front page.
* (anonymous) Then we'd have to explain why we are doing things this way. What are the advantages of using two VMs with their overhead? One VM has clear advantages: easy to redistribute, a requirement if torbox ever became official; it's suited for older hardware/live cd. The bare metal approach will never be an official goal of Whonix because there's already TorRouter for that so we should focus on VM implementations.
* (anonymous) If we had a redistributable release (portable VBox+Tor+client image with TBB etc. and set up script for host firewall or a live cd) we'd also simultaneously solve the &quot;updates over Tor, should not waste Tor bandwidth&quot; and &quot;forbid non-Tor emissions&quot;.
* (adrelanos) &quot;Then we'd have to explain why we are doing things this way. What are the advantages of using two VMs with their overhead?&quot; -&gt; Okay, it makes much sense to explain that.
* (adrelanos) &quot;The bare metal approach will never be an official goal of Whonix&quot; -&gt; Beginning from [?version#1 version 1 of Whonix] bare metal has been a part. So I really do not want to kick it out. For now the Tor Browser Bundle is a very good package for most people. I started Whonix for people who want maximum security (&quot;public enemy number one&quot;) and who need a lot more applications. There are also many people want to stick with VMs, that attracts more contributors and VMs are better for developing/testing.
* (anonymous) To clarify, by official I meant endorsed/supported by Torproject. They obviously won't support two hardware gateway projects.
* (adrelanos) About the live cd... I am not sure how this would work. The biggest advantage of Whonix is that you have a persistent storage and can update, install new packages and keep your data - if that goes lost, why not use Tails? For a live CD you can look into Tails, they already have a [https://tails.boum.org/todo/Two-layered_virtualized_system/ feature request] to implement the VM approach.
* (anonymous) thanks for this link, didn't know about it. They are misguided about one thing: you can't just use any client because of fingerprinting attacks. Since the comment about Qubes there's been a blog post on the invisiblethings blog on how to set up a TorVM which acts as a transparent proxy. None of the two projects is shipping a redistributable/easy to set up TorVM configuration. Just because it's on a to do or feature request doesn't mean it's ever going to be implemented... Our approach is far easier to complete with minimal additional investment. We are building on top of Ubuntu which has a wealth of live cd remastering support. I've already tested a &quot;One VM setup&quot; and it works flawlessly with our guide and setup script plus the linked how to and I've already created a live cd from scratch (which still has some casper related issues to look into). I know it's doable but to be upfront, I won't have the time to make a polished release. You don't seem to have interest as well. That's OK of course. My suggestion only went so far as to list this as a todo/optional in case someone else might show interest and implement it and as a hint that one could build this quite easily yourself. Being able to installing persistent applications may also be a disadvantage: Now you can also install (be tricked into) malware. Hence I recommended using VMs snapshots. Persistent date storage is something Tails has to deal too and they have several docs on that. One can always use encrypted usb or cloud storage and use clever symlinks and mount points to integrate it seamlessly.
* (adrelanos) About the USB-Boot approach on older computers... I know that their BIOS often does not support USB-booting. But that does not matter so much, as long as they can boot CD or floppy. It's possible to [http://www.plop.at/en/bootmanager/features.html chainboot USB] from CD/floppy. Plop bootmanager is freeware, closed source, but very small, Assembler only, I do not think it has a backdoor and I see no need to always use the most recent version. And as we are using Linux we can also work around the USB-booting issues using kexec.
* (adrelanos) &quot;because there's already TorRouter&quot; -&gt; TorRouter is an interesting project. I hope that both projects can profit from each other. Whonix offers different/more features than TorRouter. The project does not look like, normal linux command line users are all invited to put the software on their device. Until TorRouter will be sold, it will be probable years? You can use Whonix right now and install the Gateway part on any embedded device which can run linux. The Tor-Gateway could also easily be converted into a wifi router and/or public hotspot.
* (anonymous) TorRouter is unfinished so it's a bit difficult to compare the two. It could as well support all the features Whonix has and might get in the future. The underlying architecture of bare metal Whonix and TorRouter is exactly the same. Depending on what hardware one chooses they can be very hacker and command line friendly. Done: https://trac.torproject.org/projects/tor/wiki/doc/Whonix/OneVM

== ttdnsd [OPTIONALFEATURE][REJECTED] ==

* (adrelanos) Tails uses ttdnsd. Are there any real world examples, any example applications do not work yet, but would work if we add this as an additional step?
* (anonymous) same as https://trac.torproject.org/projects/tor/wiki/doc/Whonix/Dev#DnsPortdonotuseDnsPortrejectUDPport53REJECTED If anything comes up in the future, reopen.

== Hidden Services [OPTIONALFEATURES][IMPLEMENTED] ==

* (adrelanos) optional step; the server service should listen inside the Tor-Workstation; the hidden service should be created at the Tor-Gateway; port forwarding between workstation and gateway
* (anonymous) I've moved these 2 to do items as they are non-essential:
* (adrelanos) why did you use bold?
* (adrelanos) Do you really think this is not so important? Imho this is a real killer feature. Setting up a hidden service is very complicated. Well, the hidden service as such isn't hard to set up, but the server application itself might leak dangerous private data. Apache seams to need a lot of tweaking so it does not leak anymore. I think many people are afraid to host a hidden service because of the risks. If we explain how they can confine a server into the Tor-Workstation, maybe more people would host hidden services. No other project (such as Tails) offers any help for securely hosting hidden services confined in a box.
* (anonymous) Agreed, undone ;)
* (anonymous) Update: Using Hidden services on Whonix is really easy. 1) Install a webserver on Tor-Workstation (usually runs on port 80) 2) change torrc: {{{ HiddenServiceDir /var/lib/tor/hidden_service/ HiddenServicePort 80 192.168.0.2:80 }}} after restarting tor the .onion address can be found here: sudo less /var/lib/tor/hidden_service/hostname What's left is hardening of webserver, leaktests, possibly a firewall on Tor-Workstation. Apache leak concerns do not really apply to us. We'd recommend a small webserver like thttpd, nginx or lighttpd anyway.
* (adrelanos) That sounds great. I was going to write the guide, but haven't done it yet for myself, does it still work with the [#Step4d:Createthefirewall new firewall]. I think new rules are needed.
* (anonymous) Yes, tested with my firewall script. No changes are needed. All hidden service traffic goes through tor and tor rules are already set (accept established/related and the outgoing accept policy). For the VM running the hidden service I think we can do without a firewall rule. No leaks are possible by design. Maybe someone is interested in DoS protection or something but that's really beyond scope.
* (adrelanos) I wrote [#hostinghiddenservicesOPTIONAL hosting hidden services] - anything to add?
* (adrelanos) hardening of webserver -&gt; I researched thttpd and did not find anything to harden it.
* (anonymous) thttpd drops root rights but we could set it to run on a port above 1023 right away without any adverse effect (just edit torrc and leave the virtual port at 80)
* (adrelanos) Ok, it's done.
* (adrelanos) leaktests -&gt; [LeakTests Whonix/LeakTests] sufficient? Or anything else needed? Or do you mean application level leaks? thttpd does not seam to have those. It's [https://www.torproject.org/docs/tor-hidden-service.html.en officially] recommend. They'll recommend to compile oneself, but do not explicitly reason that or recommend against packages, so I think it's not an issue.
* (adrelanos) possibly a firewall on Tor-Workstation -&gt; For what? By design it's only reachable through Tor. Only if the user were to add an additional network adapter, he should let the hidden services listen on the internal network. Anything else?
* (anonymous) Nothing left to do as far as I see.

== forbid non-Tor emissions / hide your Tor/Whonix usage [OPTIONALFEATURE][IMPLEMENTED] ==

* (adrelanos) Should we forbid any non-Tor emissions? That'd be interesting for people using bare metal (physical computer) and an [#baremetalhintsOPTIONAL] anonymous 3G modem. At the moment the Tor-Gateway does still communicate in cleartext with the internet (apt-get, [https://en.wikipedia.org/wiki/Network_Time_Protocol NTP], what else?). We include the internet service provider into our adversary model. One who uses Whonix on physical hardware with an [#baremetalhintsOPTIONAL anonymous 3G modem] might wish to hide the fact he is using Tor, he can do that to some degree using [#Step4x:usingbridgesOPTIONAL bridges] or [Dev#HowtotunnelthroughVPNproxySSHfirstVPNproxySSH-TorENHANCEMENT by tunnel through VPN/SSH first]. If that is so, he surly also wants to hide the fact he using Whonix. [https://en.wikipedia.org/wiki/Network_Time_Protocol NTP] is a major [Dev#SettingcorrecttimeNTPHTPCRITICAL weakness] here.
* (anonymous) After the installation which I have not audited in detail Ubuntu server only uses ntp and local network communications (arp, dhcp if no static ip is used) in the background, all other network activity is user-initiated. I know that server installation will try to use dhcp, ipv6 and connect to mirrors (apt-get update). Installation and use of Ubuntu doesn't have to kept a secret, it's pretty innocent as it gets. We also do not want to promote software upgrades over Tor, this is almost as bad as p2p. Hiding the fact that one is using Tor is''really'' tricky. How for example do you obtain Tor? How do you obtain bridges? Against any kind of targeted adversary it's simply impossible. Bridges are only used to escape crude automatic blocking. In our current design I don't see that we are leaking any more Tor related clear/non-anonymous traffic than TBB anyway. Host traffic is out of scope, it should obviously not be used for anything related to activity done in Tor-workstation. I think we can close this one.
* (adrelanos) How for example do you obtain Tor? -&gt; The use case isn't so limited. Some phantasy. Either get a from a trusted friend. Or, 1. You are a journalist(/...) in a low censored country, 2. configure Whonix, 3. then you make your journey to a restricted country, 4. use your Whonix over anonymous 3G modem over SSH.
* (adrelanos) Updates over Tor are a real issue, Tor-Workstation users will most likely do it. I'll create a new topic for the update problem.
* (adrelanos) I want to solve/close this, one way or another. I made two new chapters, [OptionalConfigurations#hideyourTorusagefromyourprovider hide your Tor usage from your provider] and [OptionalConfigurations#hideyourWhonixusage hide your Whonix usage].
* (adrelanos) The advise for the top targets 'hide your Whonix usage from your provider and your SSH/VPN provider' isn't done yet. Although it would be pretty easy. The user would have to download Whonix though Tor and update the Tor-Gateway though Tor. (update Tor-Workstation has it's own thread) There should be no non-Tor emissions anyway (ntp uninstalled, only automatic updates or manual apt-get would communicate clearly). Do you think it's acceptable to [https://trac.torproject.org/projects/tor/wiki/doc/TransparentProxy#LocalRedirectionThroughTor torify the Tor-Gateway]? It's only optional configuration anyway. The Tor-Gateway is quite stripped down, how much traffic this would cause for updates?
* (anonymous) Kernel updates are HUGE and frequent. The difference between t-g and t-w therefore is minimal... Apart from apt-get proxying (e.g. http://askubuntu.com/questions/35223/syntax-for-socks-proxy-in-apt-conf but https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO#AboutDNSandtsocks) this is solved I think (updated the wiki). One thing to note: you can't hide tor usage from everyone anyway, you either trust bridges a proxy or the ISP, there is no way around that (The only alternative would be end-to-end steganography, obviously Tor can never achieve that).
* (adrelanos) Sidenote: I suggested to use stenography for private bridges. [https://lists.torproject.org/pipermail/tor-talk/2012-February/023351.html tor-talk - bridges: stenography to hide Tor traffic] Unfortunally I messed up to monitor the mailing list and to answer again. Not sure if obsfproxy is real stenography. At the moment it looks for me as the censurer and the developers have a race, one updating, another one updating. But with real stenography they could never detect it, also not after seeing the source code. (Only the private key has to remain private.) About this topic: agreed, it's done.

== do not turn off screen after a while [OPTIONALFEATURE][IMPLEMENTED] ==

* (adrelanos) While this is useful on bare metal, it's a bad look and feel when using virtual machines. The screen shouldn't black out automatically after a while. Provide an optional configuration how to stop it.
* (anonymous) use at your own risk: sudo sh -c 'echo &quot;setterm -blank 0 -powersave off -powerdown 0 &gt; /dev/null 2&gt;&amp;1&quot; &gt;&gt; /etc/bash.bashrc'
* (adrelanos) I am testing to put this into /etc/rc.local. Still wondering there is no configuration file for it.
* (adrelanos) I added &quot;setterm -blank 0 -powersave off -powerdown 0 &gt; /dev/null 2&gt;&amp;1&quot; at the end of /etc/bash.bashrc. No idea why, but it doesn't work. In /etc/rc.local &quot;setterm -blank 0 -powersave off -powerdown 0&quot; doesn't work either. When you type that command in console, then it stays activated until the next reboot. Strange.
* (anonymous) then try .bashrc
* (adrelanos) It's really crazy but none of this is working.
* (anonymous) you need to log out and back in again to apply the change. Also, .bashrc in /home/user/ not /root
* (adrelanos) That's what I used and I restarted.
* (anonymous) It works for me (Ubuntu/Tor-Gateway.ova) Try the following: before the setterm line add something like 'echo &quot;disabling screen blanking&quot;, log out and in again - do you see that echoed above the command prompt? If not bashrc isn't read for some reason.

== Whonix -&gt; &quot;TorRouter&quot;, add wireless access point, possibly add Wi-Fi hotspot, torified and non-torified connection offers [OPTIONALFEATURE][REJECTED] ==

* [https://trac.torproject.org/projects/tor/query?status#accepted&amp;status#assigned&amp;status#needs_information&amp;status#needs_review&amp;status#needs_revision&amp;status#new&amp;status#reopened&amp;component#Torouter&amp;order#priority&amp;col#id&amp;col#summary&amp;col#status&amp;col#type&amp;col#priority&amp;col#milestone&amp;col#component trac search TorRouter]
* [https://gitweb.torproject.org/torouter.git git]
* (adrelanos) The term [https://trac.torproject.org/projects/tor/wiki/doc/Torouter Torouter] is protected, as there exists already an official Tor project with that name.
* (adrelanos) It seems possible to &quot;convert&quot; Whonix into something very similar (what are the differences?) to TorRouter. There are a few remaining questions. I couldn't find much information on Google.
* (adrelanos) What is Tor Router supposed to be, only a router or a router with integrated (A/S/x)DSL modem? As Tor is a worldwide project, and to many types of modem (ADSL, SDSL, dial-up, cable, satellite, 3G, ...) I suspect it will be only a router which needs an additional external modem.
* (adrelanos) Tor Router could be either connected behind a normal router or be directly connected.
* (adrelanos) [1] computers -&gt; Tor Router -&gt; standard router -&gt; modem.
* (adrelanos) [2] computers -&gt; Tor Router -&gt; standard router with integrated modem.
* (adrelanos) [3] computers -&gt; Tor Router -&gt; modem
** (adrelanos) advantage: very easy to set up as bridge, relay or exit server as their will be no hassle with NAT/port forwarding.
** (adrelanos) disadvantage: harder to sort out traffic which shall be torified and which shall be clear.
** (adrelanos) question: ideally the device would offer two Wi-Fi access points at once. A torified one and a clear one. But I guess that is technically not possible? I guess [1] and [2] would be better here, then the user would have two Wi-Fi access points (torified and clear).
** (anonymous) It is, even with just one wifi card (multiple SSIDs, VLAN). Some hardware may not be supported in Linux. ath9k is know to work.
** (adrelanos) That's great, thanks for that information.
* (adrelanos) I am not convinced of providing a Tor Hotspot (a Wi-Fi hotspot, where anyone from street can join the Wi-Fi and all traffic will be relayed over Tor. This is because there are already people doing wardriving (driving around with their car, wifi hacking or hotspot abusing for their illegal activities). People do illegal things over Tor so or so but providing a hotspot would lower the fear of getting caught even more at cost of the exit server admins. On the other hand legitimate users would also profit. I am against that feature but if you decide pro, I won't offer it at my home, but support the implementation.
* (adrelanos) Anything, no matter if [1] with Tor Wi-Fi access point (torified Wi-Fi access point), [2] with Tor Wi-Fi access point or [3] with two access points (just two Wi-Fi devices would be needed), a torified and a clear Wi-Fi access point seams possible to implement in Whonix.
* (adrelanos) Discuss!
* (anonymous) Well, I'd say let the TorRouter guys do that work. You can't run a &quot;Whonix router&quot; on most hardware people have laying around (Laptops and PCs usually have only one NIC), we'd need to enable forwarding and set up NAT and then think about how to implement fail safe-ness. It's dangerous to try that if you don't know networking/iptables very well and in the end you'll definitely end up with a solution that has more attack surface and more bugs than the original Whonix design.
* (adrelanos) We can borrow their networking/iptables, I mean, I hope for cooperation. After all Whonix and TorRouter do not need to be different projects. My current vision is Whonix to be a documentation project for TorRouter, which anyone with basic skills offers to install on older hardware, suitable boxes, or VMs.
* (adrelanos) When they have only one NIC they could buy an additional addon NIC or cheap Wi-Fi USB keys (short search, around 8$ on ebay, inclusive shipping).
* (adrelanos) TorRouter is very different from Whonix. The news (from third party site) is misleading. The torified wifi hotspot isn't one of their goals yet (just discussed as an idea). They want(ed) to ship a cheap box as bridge or relay (no decision done from tpo) by default. Together with a nice webinterface allowing less technical people participate the Tor network. I've been monitoring their devoted wiki site and active trac tickets for some time. I see no more progress at all. Can this be closed?
* (anonymous) I don't think that project is really dead but for know we can close this.
* (adrelanos) Yes, it's not dead. [https://lists.torproject.org/pipermail/tor-talk/2012-March/023798.html recent statement from tpo]

== Hide Whonix usage / Torify T-G (optional) [OPTIONALFEATURE][IMPLEMENTED] ==

* (adrelanos) At the moment any Whonix user can be easily distinguished from regular Tor users by any passive observing ISP. This is because once, the host uses apt-get and leaves a unique fingerprint and once T-G uses apt-get which leaves the Whonix fingerprint. We shouldn't make it any easier to distinguish from low and probable more high profile users. The cleanest thing, which we should add by default, is local redirection (Transparent Proxy) by default to T-G. Doing this by using a second instance of TransPort and a second instance of DnsPort.
* (adrelanos) New firewall script moved to T-G script.; /etc/tor/torrc moved to T-G script.; /etc/resolv.conf moved to T-G script.
* (anonymous) Not critical. apt-get doesn't leak that someone is using Whonix, only that someone is using Ubuntu and tor. Doing what you suggest should be optional, for many threat scenarios it doesn't improve anything but only make apt-get downloads really slow. We already provide some hints, that should be extended and tested.
* (adrelanos) Let's suppose someone uses Ubuntu as host and Ubuntu as T-G. New kernel was released and new Tor version was released. The hosts updates the kernels, that action can be observes by the ISP, because updates are only authenticated, not encrypted. Afterwards T-G updates the kernel, the ISP can guess that there are at least two machines updated. And at the same time Tor got updated? Canonical-census/popularity-contest/dnsutils/rungetty got updated on one machine and not the other? I think the updates can leak, that one is using Whonix.
* (anonymous) ISP sees multiple computers on a network sharing a public IP, one of them is using Tor, that's all they see, nothing uncommon or specific to Whonix.
* (adrelanos) And one of those machines does not have a desktop environment installed, but Tor, which is likely the be some kind of server. (No updates for gnome/kde/etc. are requested during that session, but there are some.) No desktop environment, but a server kernel and Tor installed? Suspicious.
* (anonymous) What is suspicious about it? People use headless servers for all kinds of configurations. But OK, let's assume an ISP has the gear to detect and log apt-get traffic, it can figure out that you use Tor, Ubuntu and a certain configuration indicating a (hidden) server and/or gateway. What's the threat model? What could they possibly gain from that knowledge over just detecting Tor traffic?
* (adrelanos) Assumed the cash and human resources of authorities in censored states is not unlimited... And assumed they can not observant or imprison all Tor (bridge) users at once. (What I assume.) There are always much fewer people, who host hidden services, who start discussion boards. The majority users, uses Tor only as a client. Most people do not to host servers. Revolts and revolution can be effectively stopped or slowed down, if you catch the ringleader and server admins, censor unwanted discussion boards. Whonix users have even more to hide than Tor Browser Bundle users, they are more interesting targets. Any chance to different one from another should be avoided.
* (anonymous) Everyone is different (or: you are unique, just like everybody else). The more you flaunt how Whonix users are special the more likely it will become adversaries become specifically interested in it. But seriously, a tor gateway can be run by a Linux geek, a simple user or by a &quot;ringleader&quot;. The difference in terms of being a possible &quot;person of interest&quot; between using Tor and not using Tor at all is so much more significant than the difference between TBB and custom set up users. If your threat model includes being raided as part of a regional or national anti-tor dragnet torifying the gateway will do nothing but provide a false sense of security, slower apt-get, more complicated set up. Still disagree, but as long as everything is opt in (commented out, except for the output chain which is again accept by default and therefore does nothing) it's fine by me.
* (adrelanos) No matter if my text above is right or not. Do we in general agree, that the fact that one uses Whonix should remain hidden?
* (anonymous) No, I don't agree. As detailed elsewhere, Tor doesn't hide that you use it. If people need it they can use a VPN, we've documented it. The second aspect is that Whonix users should be in the same anonymity set as TorBrowser users, as far as this is possible we fulfill this requirement.
* (adrelanos) (1) &quot;Hide your Tor usage&quot; is different form (2) &quot;Hide your Whonix usage&quot;. Of course, if you do (1), you'll automatically also do (2). We indeed covered (1) already. What we don't cover yet is (2) - depending on outcome of this discussion.
* (adrelanos) Tor Browser Bundle users and Whonix Tor Browser users indeed to not differ from viewpoint of the server. My viewpoint here is a spying ISP.
* (adrelanos) &quot;Torifiy T-G&quot; has another advantage: We could use a manual network configuration and resolv.conf wouldn't contain the IP of the router. Better portability, for use on different computers.
* (adrelanos) In Tor alpha or next Tor stable (with stream isolation feature): If we add this by default, we could probable also activate automatic updates on T-G?
* (anonymous) this could leak uptime and is problematic wrt the mentioned stale mirror attack. Also, as said above, I'm against this being a default setting.
* (adrelanos) Can I merge my changes into the T-G script? - We can out comment the 'OUTPUT' part by default. When 'OUTPUT' is out commented, only a few variable names and comments are changed, current functionality remains the same (easy to un-out comment the additional functionality).
* (anonymous) If you tested it that it works, why not.
* (adrelanos) I am merging in and testing.
* (anonymous) Please also test ssh from the external interface.
* (adrelanos) Sorry, I don't understand. Unfortunately we don't support running over SSH &quot;Make the script executeable and run it (You need to run it directly on a terminal, not through ssh!) (run on the guest)&quot;.
* (anonymous) if you run t-g on a headless bare metal router you need to somehow log into it for maintenance, e.g. with ssh from your build/dev computer which naturally sits in front of the gateway (not torified). You need to make sure the new output rule doesn't interfere with &quot;# Allow incoming SSH connections on the external interface&quot;. Maybe the &quot;established&quot; rule is enough, maybe not - that's what needs to be tested.
* (adrelanos) Understood. Unfortunately I can not test that very soon (hardware setup).
* (adrelanos) SSH to virtual machine is still working, while the rules are enabled.
* (anonymous) Good. This means bare metal will work as well.
* (adrelanos) Some of the updates broke the functionality. nslookup is no longer working when #OptionalFeatureNr.1# is enabled.
* (anonymous) is nslookup used anywhere in torbox docs?
* (adrelanos) No, but a good tool to debug if internet connections are not working. As soon as online connection does not work, first thing I check is DNS, resolv.conf, nslookup. I think it's fixed, testing again.
* (anonymous) troubleshoot if udp is blocked: ping the router/t-g, &quot;cat resolv.conf&quot;, then &quot;wget https://check.torproject.org&quot; and &quot;less index.html&quot;
* (adrelanos) Bug was: DnsPort 54 and TransPort 9041 have to be choose to match the firewall rules.
* (adrelanos) It's all working. What's left: leak testing. News leaks through this feature are unlikely. I am working on leak testing anyway. But that goes for all optional features, worth new topic.

== Support for Other Anonymizing Networks (optional) [OPTIONALFEATURE][CLOSED] ==

* (adrelanos) The basic Whonix concept is agnostic about the operating system, the virtualization platform. Also about the anonymisation platform? Alternative anonymisation platforms: [http://www.i2p2.de i2p]; [https://anonymous-proxy-servers.net JonDonym]; Freenet; RetroShare. I personally don't use any of them, because less research on security has been done. Advantages: perhaps more publicity, users and developers.
* (anonymous) Problem with i2p and Freenet: they run on java which isn't really suited for a bare metal Whonix with a small router and the router VM would need a bit more than the current 128 MB RAM. Would definitely have to be optional and opt-in. I'd start with documenting how to do add it manually to the existing Whonix image.
* (adrelanos) Informing Other Anonymizing Networks about our plans, progress: I think it's fair, relevant and hopefully interesting for Other Anonymizing Network, that we now have something like Whonix and those networks can also potentially use the same concept, implementation, with minor changes. Here are some places to post. [http://new-wiki.freenetproject.org/Contact_us freenet mailing list] (which mailing list is best suited, devel?); [http://retroshare.sourceforge.net/forum/ retroshare forum] (Use the forum? Which sub forum?) And what text? It's difficult to describe Whonix and to describe, that it's possible with their network...
* (anonymous) You went ahead a bit fast I'm afraid. Need to take back some of what I said. I'm no longer sure that any of the potential alternatives to tor can be run on t-g, be accessible from t-w and still provides the same kind of security that the goal of Whonix is: protecting the external IP from t-w. It might be possible but that needs to really be researched in depth. The default web interfaces for example are very leaky and certainly reveal the IP address! On T-W as an optional &quot;addon&quot; yes, but we are far from Whonix being anonymity network transparent/agnostic.
* (adrelanos) About being agnostic, sorry if I was a bit overly motivated. You may correct misleading statements (if any). It may also be more carefully formulated. And if something is impossible, we also add write our findings down.
* (adrelanos) The only thing, being able to replace Tor, might be JonDonym. See &quot;Support for JonDonym&quot;.
* (adrelanos) New status: CLOSED / COVERED BY OTHER TICKETS? We have tickets covering all networks we are looking into.

== Tunneling UDP over Tor [OPTIONALFEATURE][DONE] ==

=== failed socks5 proxy method ===

(adrelanos) Perhaps impossible, since UDP still goes over UDP and Tor does not support UDP. I'll leave the prior work as reference, we'll move it to the archive, in case Tor gets UDP support or someone has another insight.

Not finished/working/tested yet. Status: TCP working. UDP not working.

Using redsocks as socksifier. Currently testing using 'JonDo – the IP changer' premium, with socks5 proxy support. ([https://shop.anonymous-proxy-servers.net/bin/testcoupon Get a free testcode]). This example configuration will be migrated to a free service, as soon we have found one.

Installation

Open a terminal on your Tor-Workstation... We need to install git. (To download the source. Unfortunately there is no Ubuntu package yet.) {{{ apt-get install git }}}

Install dependencies for compiling. {{{ apt-get install libevent-dev build-essential }}}

Go into your home folder. {{{ cd /home/user }}}

Get the source code. {{{ git clone https://github.com/darkk/redsocks/ }}}

Join the source folder. {{{ cd redsocks }}}

Compile. {{{ make }}}

Add a new user 'luser'. {{{ adduser luser }}}

'nano fw.sh' and insert {{{ # You can also control that in more precise way using <code>gid-owner</code> from # iptables. groupadd socksified usermod --append --groups socksified luser iptables -t nat -A OUTPUT -p tcp -m owner --gid-owner socksified -j REDSOCKS

= Create new chain =

iptables -t nat -N REDSOCKS

= Ignore LANs and some other reserved addresses. =

= See http://en.wikipedia.org/wiki/Reserved_IP_addresses#Reserved_IPv4_addresses =

= and http://tools.ietf.org/html/rfc5735 for full list of reserved networks. =

iptables -t nat -A REDSOCKS -d 0.0.0.0/8 -j RETURN iptables -t nat -A REDSOCKS -d 10.0.0.0/8 -j RETURN iptables -t nat -A REDSOCKS -d 127.0.0.0/8 -j RETURN iptables -t nat -A REDSOCKS -d 169.254.0.0/16 -j RETURN iptables -t nat -A REDSOCKS -d 172.16.0.0/12 -j RETURN iptables -t nat -A REDSOCKS -d 192.168.0.0/16 -j RETURN iptables -t nat -A REDSOCKS -d 224.0.0.0/4 -j RETURN iptables -t nat -A REDSOCKS -d 240.0.0.0/4 -j RETURN

= Anything else should be redirected to port 12345 =

iptables -t nat -A REDSOCKS -p tcp -j REDIRECT --to-ports 12345

= UDP rule =

iptables -t nat -A REDSOCKS -p udp -j REDIRECT --to-ports 10053

= Any tcp connection made by `luser' should be redirected. =

iptables -t nat -A OUTPUT -p tcp -m owner --uid-owner luser -j REDSOCKS

= Now you can launch your specific application with GID <code>socksified</code> and it =

= will be... socksified. See following commands (numbers may vary). =

= Note: you may have to relogin to apply <code>usermod</code> changes. =

= luser$ id =

= uid#1000(luser) gid#1000(luser) groups#1000(luser),1001(socksified) =

= luser$ sg socksified -c id =

= uid#1000(luser) gid#1001(socksified) groups#1000(luser),1001(socksified) =

= luser$ sg socksified -c &quot;firefox&quot; =

= If you want to configure socksifying router, you should look at =

= doc/iptables-packet-flow.png and doc/iptables-packet-flow-ng.png =

= Note, you should have proper `local_ip' value to get external packets with =

= redsocks, default 127.0.0.1 will not go. See iptables(8) manpage regarding =

= REDIRECT target for details. =

= Depending on your network configuration iptables conf. may be as easy as: =

=== iptables -t nat -A PREROUTING --in-interface eth_int -p tcp -j REDSOCKS ===

}}}

Make executable. {{{ chmod +x fw.sh }}}

nano 'redsocks.conf' and insert {{{ base { // debug: connection progress &amp; client list on SIGUSR1 log_debug # on;

<pre>// info: start and end of client session
log_info # on;

/* possible `log' values are:
*   stderr
*   &quot;file:/path/to/file&quot;
*   syslog:FACILITY  facility is any of &quot;daemon&quot;, &quot;local0&quot;...&quot;local7&quot;
*/
log # stderr;
// log # &quot;file:/path/to/file&quot;;
// log # &quot;syslog:local7&quot;;

// detach from console
daemon # off;

/* Change uid, gid and root directory, these options require root
* privilegies on startup.
* Note, your chroot may requre /etc/localtime if you write log to syslog.
* Log is opened before chroot &amp; uid changing.
*/
// user # nobody;
// group # nobody;
// chroot # &quot;/var/chroot&quot;;

/* possible `redirector' values are:
*   iptables   - for Linux
*   ipf        - for FreeBSD
*   pf         - for OpenBSD
*   generic    - some generic redirector that MAY work
*/
redirector # iptables;</pre>
}

redsocks { /* <code>local_ip' defaults to 127.0.0.1 for security reasons,     * use 0.0.0.0 if you want to listen on every interface.     *</code>local_*' are used as port to redirect to. */ local_ip # 127.0.0.1; local_port # 12345;

<pre>// listen() queue length. Default value is SOMAXCONN and it should be
// good enough for most of us.
// listenq # 128; // SOMAXCONN equals 128 on my Linux box.

// `max_accept_backoff` is a delay to retry `accept()` after accept
// failure (e.g. due to lack of file descriptors). It's measured in
// milliseconds and maximal value is 65535. `min_accept_backoff` is
// used as initial backoff value and as a damper for `accept() after
// close()` logic.
// min_accept_backoff # 100;
// max_accept_backoff # 60000;

// `ip' and `port' are IP and tcp-port of proxy-server
// You can also use hostname instead of IP, only one (random)
// address of multihomed host will be used.
ip # 127.0.0.1;
port # 4001;


// known types: socks4, socks5, http-connect, http-relay
type # socks5;

// login # &quot;foobar&quot;;
// password # &quot;baz&quot;;</pre>
}

redudp { // `local_ip' should not be 0.0.0.0 as it's also used for outgoing // packets that are sent as replies - and it should be fixed // if we want NAT to work properly. local_ip # 127.0.0.1; local_port # 10053;

<pre>// `ip' and `port' of socks5 proxy server.
ip # 127.0.0.1;
port # 4001;
//login # username;
//password # pazzw0rd;

// kernel does not give us this information, so we have to duplicate it
// in both iptables rules and configuration file.  By the way, you can
// set `local_ip' to 127.45.67.89 if you need more than 65535 ports to
// forward ;-)
// This limitation may be relaxed in future versions using contrack-tools.
dest_ip # 8.8.8.8;
dest_port # 53;

udp_timeout # 30;
udp_timeout_stream # 180;</pre>
}

dnstc { // fake and really dumb DNS server that returns &quot;truncated answer&quot; to // every query via UDP, RFC-compliant resolver should repeat same query // via TCP in this case. local_ip # 127.0.0.1; local_port # 5300; }

// you can add more <code>redsocks' and</code>redudp' sections if you need. }}}

Starting

Start redsocks. {{{ ./redsocks }}}

Enable the firewall. {{{ sudo ./fw.sh }}}

Using

Switch to user 'luser' and use your UDP dependent applications.

=== Discussion ===

* (adrelanos) UDP would be useful for few things. Can we somehow offer UDP over Tor while Tor itself does not offer UDP (yet and in near future)? Well, let's face it. We have almost a jester's license inside T-W. I know, that an SSH tunnel can be used to circumvent very restrictive firewalls. Let's regard Tor as an restrictive firewall, which let's us access only TCP. An SSH tunnel can offer socks5. And socks5 supports also UDP. Although I haven't tested it yet, we could tunnel UDP over Tor-TCP using a free SSH server. Drawbacks: 1. there are very few free SSH servers 2. it adds a permanent connection while the tunnel is open and [https://trac.torproject.org/projects/tor/wiki/doc/TorPlusVPN adds a permanent exit node]. I think we can live with drawback 2, as we would use it only for a few things which need UDP (freenet, retroshare) and those things are encrypted anyway. There wouldn't be much our tunnel server could observe. Only an encrypted connection from a Tor exit server to an another network.
* (adrelanos) Instant of the SSH tunnel we may also use on the of &quot;sell your ass&quot; free VPN networks (only those who can be accessed without proprietary software). I think there are more of them. Open question here: can we tunnel only a few applications over that VPN instant of all? All wouldn't be advisable (permanent exit node). If not, the user would need a separate T-W for that task.
* (adrelanos) Public socks5 proxies are probable not of any help, they don't tunnel UDP over TCP.
* (adrelanos) shellmix.com offers free SSH tunnel, which I used for testing. After registration, usage is easy, 'ssh -C -D 1080 username@tunnel.shellmix.com' (screen to run it in background). And set proxy in applications or proxychains to socks5 127.0.0.1 1080. Together with foxyproxy it's very useful. I still don't know if outgoing UDP is possible. Question: Do you know how I could test, if outgoing UDP is working?
* (anonymous) ntp, ping (not udp but still), dns ('dig' with -p flag). Update: http://shellmix.com/index.php/policy &quot;All out UDP·ports blocked&quot;. Can you still test it?
* (adrelanos) I tested it. 'proxychains goole.com; proxychains ntpdate;'''dig AAAA -p 53 google.com''' Nothing brought results. We don't know if it didn't work due to shellmix restrictions are because the whole concept is flawed. Unfortunately, I haven't found any other working free ssh tunnel. Update 1: proxychains.sf.net &quot;TCP and DNS through proxy server. HTTP and SOCKS&quot;, it doesn't claim to support UDP. Therefore the test could not have been successful in the first place anyway. Update 2: For testing, to find out if this research makes sense or is a dead end, I made myself a JonDonym trial account. JonDonym [https://anonymous-proxy-servers.net/forum/viewtopic.php?f#9&amp;t#6498 claims] to support UDP over socks (premium only). Question: Is there a UDP capable socksifier?
* (adrelanos) Okay, I set something up. [OptionalConfigurations#TunnelingUDPoverTorusingSSHVPNorJonDonym Here.] Doesn't work yet. Do you have an insight?
* (anonymous) Are redsocks git tags signed? Shouldn't be in the tutorial without a way to verify sources.
* (adrelanos) I don't know. The git link is over httpS.
* (anonymous) you aren't supposed to use 53 but whatever jondonym is listening on: dig -p <udp proxy port>.
* (adrelanos) I tested 'dig -p 10053' and with different domains and ports (80, 50, etc.). Results always &quot;:connection timed out; no servers could be reached&quot;.
* (anonymous) I think you need a dns server listening on these ports..., better: sudo nmap -sU -p 123 some.ntp.server (try different ones, they might have some rate limiting), rdate -u works nicely without root privs.
** (adrelanos) Thanks for the suggestions, I try. Port scan identd should also work well (see below). My current problem is, that I haven't found a free VPN service, which doesn't block all ports beside 80 and 443 (see below). In the end, I see no technical reason, why tunneling UDP over Tor-TCP shouldn't, if a non-blocking third party server is involved.
* (adrelanos) Another try using VPN. securitykiss.com offers a free VPN account including OpenVPN support (not all offer OpenVPN, some are VPN providers only accessable using some proprietary windows-only client). Setup of securitykiss.com was easy, I can share instructions soon.
* (adrelanos) However, in comparison to Tor, securitykiss.com blocks even the most simple outgoing TCP ports. For example outgoing TCP to port 113 (Ident Protocol) is dropped. I could scan the port using'''nmap -p 113 -PN irc.server''' directly through Tor/Whonix, but not thought their VPN. No reference on their page about blocked ports. Not a good base for UDP testing in general.
* (adrelanos) From [http://manpages.ubuntu.com/manpages/karmic/man8/rdate.8.html rdate manual]. Using'''rdate -p ptbtime1.ptb.de''' (-p for print only). It's ridiculous. Working over Tor. But not working over Tor -&gt; securitykiss.com.'''rdate -p -u ptbtime1.ptb.de''' does not work over Tor like expected, of course also not over Tor -&gt; securitykiss.com. Of course also more complex problems are possible, but I believe it's port blocking from the VPN provider. I guess as soon as I find a free VPN with open ports, this will work.
* (anonymous) now you know why i never bothered ;) I've looked in the past but free servers, no matter what sort of service, suck.
* (adrelanos) I believe in genuine free services, I am cosseted in open source and Tor. Unlimited trial, unlimited traffic, etc. :) About the VPN services you might be right. Hopefully I find something.
* (anonymous) I'm talking about vpn, ssh, web hosts. that's got nothing to do with free/libre software. in fact, usually it's non-free services unless it's affero licensed or you already host it yourself. code should be free, bandwidth and storage is not. either you get a shitty service or you pay for it (directly or indirectly as with google services for example). an alternative to that is p2p, tor being one example. end of off topic.
* (adrelanos) I might have made wrong premisses about the good old proxies. Socks5 supports UDP. Tor does not support direct UDP transports but has of course no mechanism to censor UDP included. So it's worth a try to tunnel UDP over TCP, using socks5 proxies. As soon as I found some free socks5 proxies, I investigate this further.
* (anonymous) They must have the same problem as above
* (adrelanos) [https://en.wikipedia.org/wiki/Comparison_of_proxifiers Comparison of proxifiers] (for this case: needs to support UDP and Linux) (only dante and redsocks are suitable here)
* (anonymous) redsocks README &quot;Redirect UDP packets via SOCKS5 proxy server. NB: UDP still goes via UDP, so you can't relay UDP via OpenSSH.&quot;
* (adrelanos) So if UDP goes over UDP, it can not be relayed over Tor. redsocks is out of question then. That's bad. :/
* (anonymous) dante probably needs a dante server accepting udp for udp tunneling to work.
* (adrelanos) Finally I found some working socks5 proxies. Can you provide please a 100% working line for UDP testing? Where you can 100% assure, that it would work in the clear, which I can rely on for testing? (Preferably running as user, because of redsocks configuration.) None of these working over socks5:'''rdate -u -p time.u.washington.edu''';'''rdate -u -p time.nist.gov''';'''rdate -p -u ptbtime1.ptb.de'''. (I don't want to run in the clear and over Tor afterwards myself for security reasons. So if you know a reliable command and reliable udp service, that'd be great.)
* (anonymous) the commands are working, the tunnel is not. SSH can't tunnel UDP on its own, see http://zarb.org/~gc/html/udp-in-ssh-tunneling.html
** (adrelanos) It needs the server to install something, which is very unlikely, unless you know or are the admin.
* (anonymous) So far the only way that has a chance of working is openvpn...
* (adrelanos) Or dante-client. The package is broken on oneirirc and I didn't succeed compiling myself. I try again when precise gets released. Why should a dante-server be required? If dante-client implements the socks5 standard, that shouldn't be required. Open question is, goes socks5 UDP over UDP or over TCP?
* (adrelanos) Success using VPNs: [OptionalConfigurations#TunnelingUDPoverTor Tunneling UDP over Tor]. Security consideration: [ApplicationWarningsAndNotes#OtherAnonymizingNetworksoverTorUDPTunnel Other Anonymizing Networks over Tor UDP Tunnel]. There are barely any free OpenVPN providers without blocked (UDP) ports, but now that I know, that's working, I should be more motivated to search them. It looks like there are much more free PPTP providers. Even if we discard PPTP's encryption, as completely broken, given the security consideration, it doesn't speak anything against using them for [OtherAnonymizingNetworks Other Anonymizing Networks]? (over Tor, inside T-W)
* (adrelanos) Most of this ticket is done. I'll move it to closed tickets. This ticket is quite big, too big for my preference. The only thing, which is not done yet, is researching how to add PPTP VPN's to Tor-Workstation and to research if there are any free PPTP providers, which do not block UDP. We could list them, to enable people to have this alternative method for tunneling UDP over Tor and/or to use other anonymzing networks over Tor. A new ticket can be created for that.

== [OPTIONAL FEATURE][0.2] Stream isolation workaround removed [DONE] ==

* (anonymous) https://trac.torproject.org/projects/tor/wiki/doc/Whonix/Dev/TGScript?action#diff&amp;version#264&amp;old_version#263 I don't find anything in the linked mail regarding this specific issue.
* (adrelanos) Oh sorry, it was the wrong link. [https://lists.torproject.org/pipermail/tor-talk/2012-May/024403.html tor-talk Tor's stream isolation features defaults] is the correct one. Second to last paragraph.
* (anonymous) IsolateDestPort obviously doesn't work for web browsing - those other cases were it could make sense we are using the SOCKS port isolation. However, according to the email the only problem with IsolateDestAddr is performance (which was mentioned in the old comment). It's a perfectly valid workaround if security is the only objective. The decision to remove it - even if just optional - is arguable, but was for the wrong reason.
* (adrelanos) Different SocksPort are isolated anyway. I see, security depends on application / protocol. For example POP on different ports were isolated, even if they were not configured to use different SocksPorts. We can add it again if do not advertise it as workaround for isolate by sockauth (Tor Browser tab isolation).
* (adrelanos) Added again.
* (anonymous) &quot;Unfortunately it can not be used as a workaround for bug #3455&quot; IsolateDestAddr is a workaround for that, it only works too well (not just tab isolation but address isolation for every 3rd party content). If you were to only visit sane sites (this one; correctly configured https in general, most .onion) there is no 3rd party content and it works just as well as referer based isolation. That's how I understand it at least.
* (adrelanos) #3455 also theoretically (assume remaining fingerprinting and linking bugs are closed or not exploited) support multiple identities on the same IP (of course makes only sense for high visitor sites). It would only provide a false sense of security. Sometimes different URLs point to the same server and the user sees only the domain name and assumes they are separated. If we want to recommend that, we should explicitly ask tpo if its going to work as expected.
* (anonymous) I don't want to recommend those features, they are purely optional. What's missing is a comment to add IsolateDestAddr to the TBB SOCKSPort.
* (adrelanos) I don't see what's missing. It's already noted, not to expect security from using it with TBB SocksPort.
* (anonymous) That's were I disagree, I don't see how it doesn't provide security. In some ways it provides better security, more than needed for sure but not a false sense of security. Both strategies, referrer based and IP based, have their peculiarities. I too prefer the more performance oriented solution, but right now that's not a choice to make.
* (adrelanos) Feel free to document that. Btw: I would do it myself. I am happy if I can help with anything, with the easier tasks, since I can't hold up with your speed developing nice new things like debootstrap. I can't do it myself, since I am not sure I understand it correctly.

