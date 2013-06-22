[ Main Article - Whonix][TOC]

[Dev/ArchivedDiscussion ArchivedDiscussion]

= SECURITY =

== Question about ApplicationWarningsAndNotes &gt; Identity correlation through circuit sharing [[#security|SECURITY]] ==

* recent edit at: https://trac.torproject.org/projects/tor/wiki/doc/Whonix/ApplicationWarningsAndNotes?action#diff&amp;version#35<br /> I don't understand what you mean with &quot;redirect (...) to another workstation&quot;. Also how should a local dns server provide protection against correlation. You'd still run a single instance that multiple clients share.
* (adrelanos) Thanks for pointing me to it. Yes, that's hard to describe. I added a new more sentences. Hopefully it's now more clear. Perhaps I should have discussed this before and tested it before. The mailing list implies that different SocksPort offer different circuits. I hope the same is valid for TransPort.
* (adrelanos) Closed this one, hope it is resolved/obsolete by now. We have now a new critical thread about Identity correlation anyway.

== advise users to use UTC time zone [[#security|SECURITY]] ==

* (adrelanos) We all should use the same time zone. Irc clients due to CTCP (and probable other applications) do leak the time zone. We have not told the users in past to use UTC. Changing is easy. 'sudo dpkg-reconfigure tzdata', choose 'etc', choose 'UTC', done. I'll wait a few days, if no one complains (security doubts), then I'll add it to the guide.
* (anonymous) do it, no need to wait. TBB uses UTC too (JS reports time zone 0)
* (adrelanos) done

== Leak Testing [[#security|SECURITY]] ==

* (adrelanos) One issue is that this will also track your own SSH traffic into the VM.
* (smarm) done, see [LeakTests#Step5:Settingupanon-TortrafficcapturewithWireshark revision on LeakTests under Step 5]
* (adrelanos) Assume only the gateway is started. Start this tshark command using screen. Then simple restart Tor. Go back to the screen session. You'll see a lot of traffic from nat IP to -&gt; Tor router IP. I think this is because of the non-standard ports you mentioned. As long as the target IP is a Tor router, everything is fine?
* (adrelanos) If that is so, to prevent any of such noise, I'll suggest for testing only we use a fixed Tor route (fixed entry, middle and exit node for testing only) on standard ports only. What do you think?
* (smarm) Sounds good, can you implement? Working on the VPN(s) at the moment
* (adrelanos) I guess [https://www.torproject.org/docs/faq.html.en#ChooseEntryExit choose] Entry would be needed, as the Entry will define which outgoing ports are used. Now I think that was a bad idea, choosing a single Entry is much worse then a single Exit... Otherwise we'd need to offer a big list with entry nodes on the standard ports. New iptables rules are probable, to allow only 80 and 443 as outgoing ports would make the test pointless. Maybe the solution is to tell Tor only to use a few outgoing ports, those listed [https://trac.torproject.org/projects/tor/wiki/doc/TorFAQ#DoIhavetoopenalltheseoutboundportsonmyfirewall here] and tell to using [https://www.torproject.org/docs/faq#FirewallPorts this]. I'll try.
* (adrelanos) [https://www.torproject.org/docs/faq#FirewallPorts this] worked well, just use the thing in that box and add it temporary in your torrc. So far I done all your leak tests and found no leaks. Can you add it, or I add it, or do you believe that method isn't wise?
* (adrelanos) Small other suggestion: suggest file names for the .py files, so we all have the same ones.
* (anonymous) Since we rewrote most of the how tos, iptable, added loads of new optional configurations I think we need to retest everything one last time to be confident that the set up is sound and secure.
* (anonymous) Does this affect us? http://archives.seul.org/or/talk/Jul-2010/msg00012.html
* (adrelanos) I would to ask the author of that post by e-mail and from his posts I would be awaiting a friendly answer. Unfortunately he seems to remain offline for unknown reasons. It's one of the Tor VM developers, his e-mail can be found in the original Tor VM design document and he seems not to post anything online anymore since August 2011. So let's discuss it. I guess the part you are not sure about is the following one, if another one, please quote. &quot;note that even with'''transparent proxy configuration and DNS port''' you are at risk if the attacker can'''direct explicit DNS requests to a local resolver''' (over link-local route, not default gateway). this type of attack affects all VPN or transparent proxy configurations that do not use a'''/29 point-to-point router path'''.&quot; There are many kind of transparent proxy configurations, the one he could meant, could be the torified user account. Maybe not the anonymizing middlebox. The Tor-Workstation does not have a own local DNS resolver and can not access the Tor-Gateways local DNS resolver. I guess with local route he means what's shown in the left column with 'route'. Even when adding new routers I do not think he could reach the Tor-Gateways local DNS resolver, as it's firewalled. I am really unsure what he means with &quot;/29 point-to-point router path&quot;, I found no reference for it on Google. It would be nice if any other peers could look into that issue. In doubt we should ask a question about DNS leaks with transparent proxy on the Tor users mailing list, posting only very few things, only the relevant conf
** (anonymous) Yes that's what I meant. Suppose it's just PPPoE/PPTP. &quot;/29&quot; must mean subnet, I have no idea why exactly that one, /31 would make some sense to me because it's specially for point-to-point. I can't see how this could apply to our design, there is no way to bypass T-G from the T-W. This would only be a problem if Tor itself does something stupid. The &quot;Connect to a Tor Gateway on your local network using PPTP VPN (OPTIONAL)&quot; is probably affected but that's not really a problem because that set up assumes and uncompromised client with proxy obeying applications.
* (adrelanos) Okay, I overworked the [LeakTests Whonix/LeakTests] it's now hopefully more copy and paste friendly, to make it more inviting to use it. Also no leaks with VirtualBox found. Imho we can close this ticket. As long as no new users test for leaks or new developers look into, we won't come up with new ways to test for leaking. We can make a notice on the front page, that we done our best for leak testing and invite people to do further leak testing. It's now like with any software project, we done our best, anyone is invited to audit, and if someone reports a vulnerability, we'll try to close it. -- (anonymous) Agreed. CLOSED.
* (adrelanos) We can encourage to do more individual leak testing by adding all necessary stuff by default. The packager is compelled to do testing, which includes leak testing and this task is time consuming enough. Should we add installing and configuring the necessary tools for leak testing by default into T-G and T-W script?
* (adrelanos) It's probable not too much work to do that and disk space shouldn't hurt too much as well. I'd do it. Should we also deploy the leak test scripts by default?
* (anonymous) agreed. can you add this step to the build instructions?
* (adrelanos) (It's already implicit &quot;test your image before relese&quot;, test is linked. Anyway...) Soon. As soon as I added the required software for leak testing to the scripts. I hope there will be no dependencies to packages, which we apt-get remove.
* (adrelanos) What do I do will all those python scripts from Whonix/LeakTests? One way or another they have to arrive in T-W. I could simply add echo '...' &gt; /home/user/leaktest/tcp_test.py etc. Disadvantage: it would blow the script up and make it less readable. Alternatively we could think about a &quot;#include&quot; directive. Most projects consist of several source files, it would be good if we can prevent that but I am not sure how long we can. Your opinion?
* (anonymous) anything leak test related should go into a separate script, it should be entirely optional if you build torbox yourself (e.g. wireshark increases attack surface)
* (adrelanos) Okay, when it's in the end only two single scripts, it also should be motivating and easy enough to do the leak tests. By the way there were no leaks like expected.
* (adrelanos) Updated [LeakTests LeakTests]. I am not happy with the results. If you look into the howto it's still too much work. Not very comfortable. One issue is, that #OptionalFeatureNr.6# has to be enabled/disabled and Tor has to be restarted after toggle #OptionalFeatureNr.6#. Another issue is, that you still have to transfer two scripts, make two scripts executable, start two scripts. I could add a -install and a -test switch, but that's overkill. Or always install again, which shouldn't hurt, apart from looking ugly. But that won't help either, you would still have to transfer two scripts, make two scripts executable, run two scripts. Another option (and probable overkill) could be to start a software project. Offer a leaktest-gateway and a leaktest-workstation package, which can be downloaded with apt-get. But I don't know, Ubuntu would take a while until they add the package to the repo, if they even would ever do. And PPA are also no option, would make it more complicated as well. It all comes back to deploy this by default. Not install something, but offer include script to install the needed tools and start testing. But that blows our shell scripts up, dunno if that were acceptable. Or we leave it as it is with LeakTestsOld, which is also a mess. Your opinion?
* (anonymous) since we've reworked the script we can integrate it into the one. the scripts are already long anyway.
* (adrelanos) Do you know how to automate the &quot;ReachableDir/OR&quot; step? I am not happy with that one. We could either backup torrc, append &quot;ReachableDir/OR&quot;, restart Tor, and after testing copy back backup of torrc. Or do you know a way to undo append? A command like &quot;remove <this> from file content&quot; or even better &quot;outcomment <this>&quot; would be handy.
* (anonymous) DONE?
* (adrelanos) Unfortunately not. I have to merge Whonix/LeakTest into T-W script. And the ed lines in /home/user/leaktest/leaktest.sh are broken.
* (adrelanos) I double checked by torrc. It contains at the top: {{{ ... #+# #OptionalFeatureNr.6# #+# See Whonix/LeakTests. Activate this while testing for leaks. (Step 0) #+# Deactivate after you are done! (Important!) (Step 9) #ReachableDirAddresses'':80 #ReachableORAddresses'':443 ... }}} Here is the output: {{{ ... INFO: You can uninstall tshark later manually using: sudo apt-get remove tshark INFO: Setting capabilities to run wireshark with user privileges. INFO: Modifying /etc/tor/torrc... ? INFO: Listing for leaks stopped. INFO: Reverting /etc/tor/torrc to original state. ? ? INFO: Reloading Tor, using normal settings again Reloading tor daemon configuration: tor. INFO: Done. user@ubuntu:~/leaktest$ }}}
* (anonymous) I really can't reproduce, error must be on your side, try puiing those things into a new file and running ed on that. Whitespaces and multiple copies of the string wouldn't cause that error. If all fails make a copy of torrc, run -uninstall, then reinstall, then diff the two torrcs.
* (adrelanos) torrc is triple checked and reinstalled. I narrowed the error down. It's a problem with escaping. The &quot;&quot;, &quot;'&quot; and &quot;#&quot; get &quot;lost&quot;. Try echo the first line, you'll see, chars get lost. {{{ what works for me for example when I copy from web (with sudo): ed -s /etc/tor/torrc &lt;&lt;&lt; <math>',s/ReachableDirAddresses \*:80/#ReachableDirAddresses*:80/g w' what arrives inside /home/user/leaktest.sh                    : ed -s /etc/tor/torrc <<< </math>,s/#ReachableDirAddresses'':80/ReachableDirAddresses'':80/gnw }}}
* (anonymous) Thanks for troubleshooting! Fixed. What else is left to be done?
* (adrelanos) I haven't tested it yet but I think it needs testing. Probable won't work due to mkdir as root and tee as user. leaktest-install.sh should be merged into leaktest_all.sh. What we can also do, is rename test_all.sh to leaktest.sh. Then we end up with one single command on both machines, that'd be great.
* (anonymous) should simple_ping be part of the test_all? Because it never stops until I hit ctrl-c and it doesn't really do anything useful anyway.
* (adrelanos) Strange, I never needed to press ctrl-c. It probable can be get ride of. I think we should deploy it for testing but not run it by default, as it was merly made to test scappy, not to provoke a leak.
* (anonymous) try with tor-workstation down (or change the target)
* (adrelanos) Anyway. We don't need it.
* (adrelanos) Tested everything and I am very happy with the results. Leak testing is now so easy, it won't take so much time in future.

== Iptables: filtering malformed packages [[#security|IMPLEMENTED]] ==

* (adrelanos): filtering malformed packages is a topic on it's own and should be implemented no matter what the result of &quot;TransListenAddress and DNSListenAddress on localhost only&quot; may be
* (anonymous): Don't agree, see top rated answer: http://security.stackexchange.com/questions/4603/tips-for-a-secure-iptables-config-to-defend-from-attacks-client-side
* (anonymous): anyway, these don't seem to hurt, put them into firewall.sh right after the default policy: {{{

= DROP INVALID =

iptables -A INPUT -m state --state INVALID -j DROP

= DROP INVALID SYN PACKETS =

iptables -A INPUT -p tcp --tcp-flags ALL ACK,RST,SYN,FIN -j DROP iptables -A INPUT -p tcp --tcp-flags SYN,FIN SYN,FIN -j DROP iptables -A INPUT -p tcp --tcp-flags SYN,RST SYN,RST -j DROP

= DROP PACKETS WITH INCOMING FRAGMENTS. THIS ATTACK ONCE RESULTED IN KERNEL PANICS =

iptables -A INPUT -f -j DROP

= DROP INCOMING MALFORMED XMAS PACKETS =

iptables -A INPUT -p tcp --tcp-flags ALL ALL -j DROP

= DROP INCOMING MALFORMED NULL PACKETS =

iptables -A INPUT -p tcp --tcp-flags ALL NONE -j DROP }}} * (adrelanos): He uses a good argument on stackexchange, &quot;Well, how do you know the future flaw will be in the TCP handler and not in the iptables TCP parser?&quot;. For this situation I say, the next flaw, related to malformed packages is more likely inside Tor than inside kernel/iptables.

== iptables: Default DROP for outgoing traffic? [SECURITY][REJECTED] ==

* (adrelanos) What about whitelisting iptables also for outgoing connections? Would it make sense to suspect Tor-Gateway contamination (either only user account or root)?
* (anonymous): If the gateway is compromised it's game over anyway. There are so many ways to evade egress filtering. An adversary could in any case leak sensitive information over the allowed outgoing Tor connection. I'd label this optional (i.e. tinfoil hat setting). Root and tor-user account is always fatal, there are no other processes run by other users that could be attacked (see security/hardening, assuming dhcp and ssh are removed).
* (adrelanos) Agreed, not possible. See firewallleaktester and personal firewalls... Status changed.

== TransListenAddress and DNSListenAddress on localhost only [SECURITY][CLOSED] ==

* (anonymous): But forwarding is disabled on Tor-Gateway, this can only work if we enable forwarding! This would require an absolute bulletproof iptables setup. Right now we have a two layered defense. What would be the benefit of not having Tor listen directly on the two ports. The client can send malformed data regardless. This does not protect Tor-Gateway or Tor specifically for network layer attacks.
* (adrelanos): This is a good question. I list some reasons.
* It is a requirement by design. The Tor-Gateway is designed to be a gateway server (like a home router). Any home router allows you to request DNS through it's gateway/dns functionality but it will not have any open ports (beside webinterface 80 and dns 53).
* It is true, TransPort and DNSPort will probable drop malformed packets. But I haven't checked how well this is implemented (my skill do not allow that). My common sense tells me, that there are many more iptables users and programmers then Tor and Transparent Proxy users, that's why I suspect that iptables's implementation had more security reviews. And iptables can reject malformed packages as well, that's why we should direct this task to iptables.
* At the moment the Tor-Workstation can do strange things, such as sending TCP requests to the DNSPort and sending DNS requests or any other UDP traffic to the TransPort.
* closing TransPort and DNSPort allows the Tor-Workstation only to use the gateway feature, impossible to talk to those ports directly
* If it were implemented, for example, no UDP packages could reach TransPort anymore. That would be an advantage if there were are vulnerability inside TransPort which could be exploited using UDP only.
* For implementation details... I am not sure yet. Would be neat if some iptables geek would show up. I do not think we need net.ipv4.ip_forward.
* The old article [https://trac.torproject.org/projects/tor/wiki/doc/TransocksifyingTor Transocksifying Tor] could give some hints how to do it using DNAT, he is also doesn't use net.ipv4.ip_forward.
* Feel free to discuss this further. Just my thoughts.
* (anonymous): I agree, we should try to do that. I'm pretty sure we'll need to enable forwarding. With the Transocksifying Tor clients and tor run on the same system, no forwarding was required. But with Whonix, while we can send the gateway traffic without a problem getting replies back will be more difficult. This will require NATing and forwarding, I can't think of any other way.
* (anonymous): Update: I was wrong about the forwarding but I found out how to do it. tl;dr: it's pointless.
* On Tor-Gateway
* We need to set up an alias address for lo because apparently Linux still doesn't allow DNAT to known localhost IPs
* source: http://lists.netfilter.org/pipermail/netfilter/2004-November/057312.html
* <code>sudo ip addr add 192.168.10.11 dev lo</code>
* then modify iptables.sh, replace the two PREROUTING commands with:
* <code>iptables -t nat -A PREROUTING -i $INT_IF -p udp --dport 53 -j DNAT --to-destination 192.168.10.11:53</code>
* <code>iptables -t nat -A PREROUTING -i $INT_IF -p tcp -j DNAT --to-destination 192.168.10.11:9040</code>
* edit torrc (replace old entries):
* DNSListenAddress 192.168.10.11
* TransListenAddress 192.168.10.11
* restart tor, run firewall script, verify it's working
* to prove that tor is indeed running only on localhost:
* install nmap on Tor-Workstation
* comment out the two PREROUTING commands, run firewall script and run these two commands on tor-workstation:
* sudo nmap -sU -p 53 192.168.0.1
* nmap -p 9040 192.168.0.1
* both must return STATE: closed
* if you change back torrc to listen on 192.168.0.1 both return STATE:open
* Here's why doing so only complicates things for no benefit:
* This change is completely &quot;transparent&quot; to Tor-Workstation. The difference is only visible on the gateway itself: packet flow is either input-&gt;redirect or input-&gt;DNAT, this is'''internal''' packet flow. In other words, the gateway will still look exactly the same to Tor-Workstation. In both cases Tor will listen on all ports, all ports will be reported as open. And this seems to be a requirement by design because unlike traditional routers and gateways Whonix doesn't just forward packets, it has to feed them all into Tor which runs on it. It's actually more like a server than a router. A multi-protocol and multi-port server which handles http, irc, pop and so on. Theoretically it could work differently but this is a limitation of the current Tor implementation which we can't change. Please correct me if I'm wrong.
* We can already filter what packets go through to Tor with the input chain:
* iptables -A INPUT -i $INT_IF -p udp --dport 53 -j ACCEPT
* iptables -A INPUT -i $INT_IF -p tcp -j ACCEPT
* these can be made a lot more restrictive, all power of iptables is available to us. udp and icmp is already blocked, we could restrict it to only accept tcp on 80, 443 and whatever else the user requires, we can discard malformed packets. e.g.: <code>iptables -A INPUT -i $INT_IF -p tcp --dport 9040 -j ACCEPT</code>
* <code>iptables -t nat -A PREROUTING -i $INT_IF -p tcp --match multiport --dports 80,443 --syn -j REDIRECT --to-ports $TRANS_PORT</code>
* if you nmap Tor-Gateway again you'll see only port 80, 443 and 53 are open
* (adrelanos): I am still reading and understanding your writing. In meanwhile new related topics came up. (&quot;DnsPort, do not use DnsPort, reject UDP port 53&quot;, &quot;iptables: filtering malformed packages&quot;.
* (anonymous): I think I have finally wrapped my head around this... Forwarding a port listening on localhost to INT_IF or directly listening on INT_IF makes no difference and is pointless. For this to work as envisioned initially I think Tor would have to be part of the OS network stack. Because it operates beneath it it can't directly manipulate packets. Instead it has to first collect them from the OS, manipulate, and then hand them back. For this it needs to have open ports which are nothing but communication interfaces for exchanging packets between the network stack and applications. Therefore impossible and CLOSED.

== DnsPort, do not use DnsPort, reject UDP port 53 [SECURITY][REJECTED] ==

* (adrelanos): This one is related but not the same. It seams that port 53 needs to stay open on Tor-Gateway, otherwise Tor-Workstation can not get any DNS. But stop, the Tor-Gateway must not offer DNS service. The Tor-Workstation could use TCP, which is forwarded through Tor, and resolve DNS on it's own. This could result in a smaller attack surface for Tor. Let's discuss if this approach makes sense.
* (anonymous): There's a big advantage in staying with Tor's DNS resolver: Less traceable and more decentralized. Otherwise you'd be using one single DNS server for all requests (See tails docs re ttdnsd). As longs as no applications break because of limitations (e.g. no AAAA) I don't think we should change this.
* (adrelanos): We wouldn't have to use a centralized DNS resolver. Also an alternative DNS resolve system could be looked into.
* (adrelanos): However, the Tor DnsPort is somewhat made for what we use it right now. Improving DNS is beyond the scope of Whonix. CLOSED

== UDP firewall rule unnecessary? [SECURITY][WONT FIX] ==

* (anonymous): Probably redundant as ipv4 forwarding is disabled on the proxy and ipv6 connectivity is completely disabled.
* (adrelanos): The motivation behind this is improved connectivity. Applications relying on UDP, ICMP or own DNS might work better (faster) when they are instantly informed about which features are allowed by the firewall and which are not. And the implementation would be &quot;cleaner&quot; (obeying protocol). It's also better for debugging. Affected applications are those normally try to tunnel are firewall, such as OpenVPN, voip, messengers or ping, portscan. At the moment the behaviour is drop (ignore unsupported packages), this must be changed to reject (inform about unsupported action).
* (adrelanos): I am not sure about the reject-with either. I used ping on Tor-Workstation with XP guest. Normally ping should fails instantly (rejected) and not waiting for timeout (dropped)? How can we test it?
* (anonymous): Pings to the VM are rejected, the reject-with is correct. Pings to other hosts are matched by &quot;iptables -A'''FORWARD''' -j REJECT --reject-with icmp-port-unreachable&quot;. Forward rules only seem to take effect if forwarding is enabled (sudo echo &quot;1&quot; &gt;/proc/sys/net/ipv4/ip_forward). I'm really not sure if this is a good trade off. If iptables has a bug it's game over anyway I guess but it &quot;feels&quot; saver to have this two-layered protection. Whether it's worth it depends on how useful the instant reject is. All I know, web browsing and TCP only communication in general is not affected. If we can't come up with relevant user cases we should leave the default as, perhaps inform about all this in an OPTIONAL step.
* (adrelanos): [https://svn.torproject.org/svn/torvm/trunk/doc/design.html A Tor Virtual Machine Design and Implementation] &quot;If the Tor VM is unable to proxy traffic it must not let the traffic through unaltered, but instead present an error to the user via the user interface describing the nature of the failure to communicate and possible remedies if any.&quot; - That's why I started this. But following your arguments I really must agree with your resolution. As soon as someone comes up with a useful use case, we can add an optional step.

== Tor enforcement [[#security|SECURITY]] ==

* (adrelanos) Anything else from https://tails.boum.org/contribute/design/Tor_enforcement/ we should consider?
* (adrelanos) We seam to cover all topics. (Feb 2012)

== different netmasks for eth0 and eth1 255.255.25'''2'''.0 vs 255.255.25'''5'''.0 [[#security|SECURITY]] ==

* (adrelanos) If I remember correctly, as a security layer, it was advised somewhere to use different netmasks, because the 252 netmask will be unable to communicate with the 255 netmask. &quot; using NAT adapter instead of bridge adapter&quot;
* (anonymous) The benefit of doing that seems dubious, we already enforce network isolation twice, with iptables and by disabling forwarding. I'd go with the default. There are some more differences, for example there is no broadcast line in your setup. I'm really not sure either way. On second thought, if I understand it correctly &quot;255&quot; is a subset of &quot;252&quot;. If anything this setting would enable communications across 192.168.0.* and 192.168.1.* for example. Same goes for broadcast, the 255.255.255.0 is very restrictive and only allows broadcast on 192.168.0.* (i.e. one class c) But maybe I'm totally off. I'm not good with subnet masks. Better use the default from the script. However, better yet, ask someone who knows for sure ;#)
* (anonymous) Ok, I think that settles that: https://gitweb.torproject.org/torouter.git/blob/HEAD:/packages/torouter-prep/configs/interfaces netmask 255.255.255.0 broadcast*.255 and a network line as well. Going to change our iterfaces accordingly.
* DONE, please reopen if you disagree!

== Test iptables [SECURITY][DONE] ==

* (adrelanos) from http://git.immerda.ch/?p#amnesia.git;a#blob_plain;f#config%2Fchroot%5Flocal%2Dincludes%2Fetc%2Ffirewall%2Econf and http://git.immerda.ch/?p#amnesia.git;a#blob_plain;f#config%2Fchroot_local-includes%2Fetc%2Ffirewall6.conf - has been implemented by anonymous
* (anonymous) Done? Needs testing
* (anonymous) Test iptables for leaks and conflicts.
* (adrelanos) I've done [LeakTests Whonix/LeakTests], also [Dev#LeakTestingOPEN see]. Looks very well so far. It would be still excellent to hear more opinions, as this isn't a strong ability of mine.
* (anonymous): remaining issues are to be discussed in the leak testing ticket

== VM Fingerprinting Attacks [SECURITY][CLOSED] ==

* (adrelanos) If I understand correctly [https://svn.torproject.org/svn/torvm/trunk/doc/design.html A Tor Virtual Machine Design and Implementation] - an attacker who got access to the Workstation, shall not be able to gain any specific information about the hardware (intel or amd cpu, clock frequency and so on), so that he is unable to distinguish different Whonix users. It might be possible with a real emulator (Bochs), all hardware could be the same there, but the emulator is so slow, we can not use it. Not sure, but I think this is really out of scope, all virtual machines I know, leak that information, it would be possible to fake all those things, but that's worth a whole new project (either forking a virtual machine or providing a new option through patches). I'll guess a feature request for the existing virtual machines wouldn't have much of a chance.
* (adrelanos) Furthermore, as soon as the user uses it's Workstation the same way he uses his desktop computer, he installs custom packages, then he can be fingerprinted so or so. So it would only make sense for users who reset their virtual machine. And someone who uses bare metal, would also have to use a VM to get this feature or restore to a certain state. Tails also thought about this, look at the [https://tails.boum.org/todo/Two-layered_virtualized_system/#index2h2 picture]. (I don't think someone is really working on it.)
* (adrelanos) It's part of the design document, if we make our own, we should probable kick it, it's too much work and to much skill required. Open for discussion.
* (anonymous) AFAIK VMs under VBox only leak the CPU. Chipset, BIOS and motherboard serial number are all &quot;virtualized away&quot;. Off the shelf CPUs are hardly very identifying. If we recommend Tails (depends on whether we can disable built in tor). this ticket can be closed - IMHO.
* (adrelanos) As soon as the Tor-Workstation is compromised, I guess it's over with protection against pseudonym detection anyway. There are too many ways to distinguish different compromised Tor-Workstation's. For example if the attacker would benchmark the virtual hdd, ram, and cpu during idle time, he could gather so much unique information that the probability to link it to a certain pseudonym is sufficient, together with the observed activity. And if the Tor-Workstation is compromised this is one of the smaller problems anyway, attacks against the Virtual Machine, Tor-Gateway or host are a much more valuable goal for the attacker.
* (adrelanos) For this reasons we shouldn't implement it. I'd suggest status change &quot;CLOSED&quot; or &quot;LOW PRIORITY - WAITING FOR CONTRIBUTOR&quot;.
* (anonymous) agreed, it's covered in the &quot;updates&quot; ticket anyway. More that using a generic VM is impossible. (Emulators may work in ten years when we really have fast computers) Therefore CLOSED.

== Tor Control Port / Vidalia [[#security|SECURITY]] ==

* (adrelanos) We either should disable or use it.
* (adrelanos) Vidalia can not be used anymore because the Tor-Gateway does not have a desktop and Tor-Workstation may not have access for security reasons. So we could potentially implement some shell scripts to reach Tor Control Port's feature by command line (such as switch identity).
* (anonymous): we can use telnet to communicate with tor. This is secure as long as it's available only on localhost.
* (adrelanos): I agree, telnet to localhost is fine.
* (adrelanos): New idea... Never good to reinvert the wheel. We can simply install Vidalia on the host and configure it to access the Tor-Gateway. Only a new firewall rule and a little configuration needed.
* (adrelanos): It's [OptionalConfigurations#VidaliaforWhonix done].
* (adrelanos): I reopened it. Since we switched from bridged to NAT networking it's broken. Of course this is no reason to switch back to bridged networking. torrc wants to know on which address it shall listen. But the internal (nated) IP inside the Tor-Gateways is now dynamic.
* (anonymous) You can still set a static IP for the T-G and if you only use one NAT Adapter in total it will always be at 10.0.2.15.
* (adrelanos) Thanks, fixed.

== Call for Testers: Test the Shell script [SECURITY][DONE] ==

* (anonymous) Please test [ShellScript Whonix/ShellScript] to set up the transparent Proxy on Tor-Gateway.
* (anonymous) Made a lot of improvements to it. It's complete and ready I think. But no one has tested it so far :(
* (adrelanos) There three be two reasons for it. 1. Currently in the Whonix article it's not absolutely clear, what are the technical explanations, and what is essential for &quot;brain off, just copy and paste tutorial&quot; - we should somehow mark clearly, everything the user absolutely has to do - to compare if all those commands are inside the shell script. 2. Whonix isn't well known, there is a lot of interest in a Tor transparent proxy (VM), as there are loads of related projects and questions everywhere, but who knows Whonix. 3. trust issues, it's only a wiki and anyone can take your account. If it where on sourceforge or anywhere else, I guess more people would trust it (even if it's questionable, if sourceforge would grant security).
* (anonymous) anything in step 1 to 6 that isn't labeled optional, verify or test is absolutely required. Should we just tag the remaining unlabeled steps as such? I've added a short paragraph to &quot;General&quot;, maybe that's enough. Eventually I think everyone should use the shell script and we outsource the manual tor-gateway config steps. Trust is a good argument, I was thinking about that too. people familiar with linux can just quickly read through the script and see what it's doing but those people don't really need the script in the first place. A read-only,verified by someone trusted/reputable version would be nice. We should only look into that once we are comfortable that nothing will have to be changed anytime soon.
* (adrelanos) Someone asked me by e-mail and reported, that it's currently not working with VMware. I guess it is because VMware uses different IP addresses. The users is currently not told about this. I redirected him to this resource, let's see if he joins this discussion. Sorry for my false edit in Whonix/shellscript.
* (anonymous) The IP for the internal network is the same. I've expanded the assumption section to include that the external interface needs to be configured already. Maybe the order of eth1/eth0 is reversed. I'm sure if all assumptions are met the script will work in VMware too.
* (anonymous) The main how to now depends on the shell script. Someone please double check I didn't miss any steps. Optional: test how it handles failures.
* (anonymous) I only tested the script (extensively) on Virtualbox with ubuntu host and ubuntu guest. Would be interesting to hear if it works as well with Windows Host, VMware, Debian Guest (we do make this claim after all).
* (adrelanos) Test: VMware on Windows. It took me a while to finally do it, I moved that task every day. #) Biggest issue was trust. But in the end I don't think anyone can hide a backdoor inside a shell script. Minor edits to render it useless may be possible but no way to notify a third server with my IP and SSH password. I'd trust anonymous who wrote the script. Problem is that anyone can use that account. I might be wrong, people get hacked, but after a while I trust people who are constructive rather then destructive. There where so many edits and at some point I could follow all. But now I guess most is done (technically side of the shell script) and less frequent edits will be necessary. Minor issues: there is no scp on Windows, WinSCP does the job. We should tell people to create a file WhonixShellScript.sh and paste the content of the ShellScript box. The &quot;Import gpg keys. .... Verify that it is correct!&quot; should link rather [https://www.torproject.org/docs/debian.html.en#ubuntu here]? About the script itself. Amazing! For test I setup a new T-G and everything worked out of the box. Other people are still invited to test.
* (anonymous) This is &quot;me&quot; again, (but how can you know for sure...). Off topic reply: A clever &quot;bad guy&quot; would exactly act like me, be helpful, constructive to gain trust. Then one day I, I mean he, inserts something bad, and baaam, you're pwned. Just food for thought.
* (adrelanos) Yes, indeed. That is how most open source projects work. And people spreading FUD, &quot;no backdoor possible in Open Source projects&quot;. :)
* (anonymous) Back to topic, yes the script is finished as of today (March 1), I don't plan to change it till Ubuntu 12.04 comes out - unless there's a security issue (e.g. in the firewall or permissions) or a really must have new feature is proposed. For someone with a bit more*NIX experience reading through a bash script is like reading plain text - even without the comments. No way to hide anything in there that is hard to detect AND actually useful for an adversary - trust me on that one ;) The verify link is deliberate and imo correct (I've also added yet another). the debian/ubuntu link is in the comments for documentation but not required for verification. Copy and paste into an open nano works fine as an alternative to scp. This can be added to the how to.
* (adrelanos) Okay. The paste into nano didn't come into my mind, indeed.
* (adrelanos) About the keys again... On https://www.torproject.org/docs/debian.html.en is exactly {{{ gpg --keyserver keys.gnupg.net --recv 886DDD89 gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | sudo apt-key add - }}} available for copy and paste. I don't see that on the other pages.
* (anonymous) ok, fixed, and scp for windows is available too.
* (adrelanos) Agreed, done. If someone reports a problem, we can still make changes

== Mitigate DNS related identity correlation [SECURITY][DRAFT] ==

(untested, in theory, probable not needed anymore) Assuming you trust OpenDNS, not to collaborate with the evil exit node you can do the following.

To stop DNS related identity correlation, you could run your own local DNS resolver inside Tor-Workstation. [https://www.opendns.com/technology/dnscrypt/ DNSCrypt] for [https://blog.opendns.com/2012/02/16/tales-from-the-dnscrypt-linux-rising/ Linux] is currently the only local DNS resolver which uses encrypted connections to contact the DNS server - the exit node can not sniff that request. Point your applications, which you do not want to be affected by DNS identity correlation to use that DNS resolver. Doing so you have at least two different DNS resolvers. The standard DnsPort through Tor and DNSCrypt (encrypted TCP to the [https://www.opendns.com/ OpenDNS] DNS server).

Alternatively you could also use more than one TransPort and redirect all identity you don't want to be linked to another Tor-Workstation. Add an additional TransPort to torrc and use [OptionalConfigurations#MorethanoneTor-Workstation More than one Tor-Workstation] pointing at this TransPort. Change your /etc/torboxfirewall.sh accordingly.

== SELinux AppArmor grsecurity [SECURITY][REJECTED: Upstream issue] ==

* (adrelanos) [http://www.cyberciti.biz/tips/selinux-vs-apparmor-vs-grsecurity.html SELinux AppArmor grsecurity - introduction]. Related to [SecurityAndHardening Whonix/SecurityAndHardening]. We can provide instructions to add an additional security layer for critical (network communicating) components, such as iptables, Tor, kernel (if possible), Tor Browser, XChat, etc. It shouldn't end in a maintenance hell. We got to discover which system is the most easy to use one, click and go, if that is possible.
* (anonymous) this also applies to t-g (but we only need to protect the tor process, if this one is compromised, it's game over). However, these are things that should be done by upstream (would be too much work anyway). For Tor see:
* https://trac.torproject.org/projects/tor/ticket/4522
* https://trac.torproject.org/projects/tor/ticket/5024
* https://trac.torproject.org/projects/tor/ticket/5210
* Grsec: definitely an upstream project, there's been some progress from the Ubuntu front in the past 2 years, let's hope this continues.
* Apparmor: we could do this ourselves, very easy to create new rules and it's simple to redistribute and automate that set up.
* Easy means: not much knowledge required, it can still be time consuming to make a rule that is ready for redistribution.
* SELinux: forget about it, more complicated than doing all the other security patches, IDS, MAC on one system together but still weaker than grsec alone
* created https://trac.torproject.org/projects/tor/wiki/doc/AppArmorForTBB
* (adrelanos) Nice. Why rejected? I am going to look into your new profile. And if it's not too hard, I will also start creating profiles.
* Reject because this shouldn't be part of Whonix but part of Ubuntu and/or TPO.
* (adrelanos) Closed: And it all comes down to the question, what is the most secure operating system anyway. However, anyone welcome to provide profiles...

== More than one Tor-Browser instance / foxyproxy [SECURITY][ANSWERED] ==

* (adrelanos) It would be handy, if more then one Tor-Browser could be run at the same time. For example, one instance, with a http (i2p) proxy added. I added -no-remote (./App/Firefox/firefox -profile ./Data/profile -no-remote) to start-tor-browser. Unfortunately it's not working. &quot;Firefox is already running, but is not responding. To open a new window, you must first close the existing Firefox process, or restart your system.&quot; This works, with a second folder for TB. Is this an acceptable solution?
* (anonymous) It &quot;works&quot; but it's not a nice solution. It can be done with a single instance of TBB and an additional proxy plugin (afaik &quot;foxyproxy&quot;, just see how it's done in tails).
* (adrelanos) I guess this problem has a very limited amount of users anyway. New: [https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO/WebBrowsers#MorethanoneTorBrowserbehindatransparentproxyorWhonix More than one Tor Browser behind a transparent proxy or Whonix] And about foxyproxy, I am not sure it's good to suggest that. Does it introduce new problems? Tpo recommends not to install any custom addons into TBB.
* (anonymous) Tails is recommended by tpo and tails is using foxyproxy. so &quot;by proxy&quot; tpo is recommending &quot;custom&quot; addons at least when they come preinstalled and preconfigured where it absolutely makes sense.
* (adrelanos) Ok. Tails doesn't use Tor Browser or Tor Button. Will it be compatible/safe?
* (anonymous) Tails uses Tor Button. If foxyproxy doesn't have a backdoor, i.e. it does what it's supposed to do, it is safe.
* (adrelanos) Okay, when we reach a point where we need foxyproxy, we recommend it. I closed this one, if I was to fast, reopen.
* (adrelanos) [https://www.torproject.org/torbutton/torbutton-faq.html.en#extensionconflicts TorButton FAQ regarding foxyproxy]; [https://tails.boum.org/todo/iceweasel_addon_-_FoxyProxy/ Tails foxyproxy comments]; It will need testing if foxyproxy will be still compatible after #3455 got implemented.
* (anonymous) why should there be a problem? these two things are totally separate.

== developement related leaks removed: resolv.conf auth.log [SECURITY][FIXED] ==

* (adrelanos) You removed &quot;rm /etc/resolv.conf&quot; and &quot;rm /var/log/auth.log&quot;. [Dev/TGScript?action#diff&amp;version#42&amp;old_version#41 diff] Why?
* (anonymous) cause it doesn't leak anything. /var/log/* can be deleted as a whole to save space, resolv.conf already contains the valid IP (VBox network).
* (adrelanos) /etc/resolv.conf always contains after networking restart, the IP and the name of my hardware router. Is this script version specific? I doubt that.
* (anonymous) oops...
* (adrelanos) Resolved, both are taken care of with T-G wiki version 100.

== /var/lib/tor issue [SECURITY][SOLVED ] ==

* (anonymous) How did you find out that this is an issue? It crossed my mind that it could be a security risk if all users had the same tor state but I could find nothing about it documented anywhere. I admit I should have posted about my concerns right away instead of just guessing it would be OK.
* (adrelanos) Please read [https://www.torproject.org/docs/faq.html.en#EntryGuards entry guards]. As far I understand, Tor chooses them randomly (with few requirements to meet for them) and keeps them for a while. It's Tor's job to choose them, not Whonix's job. Whonix has no business choosing entry guards. More people using Whonix means even more load for those fixed entry guards. Whonix users shouldn't be easily distinguishable from &quot;non-Whonix but Tor users&quot;, as they are probable more interesting targets (hidden services, etc.). People report online, that they are using Whonix for their hidden services and an attacker shouldn't know which entry guards they are using, which would be clear, if they reported to use the downloaded version. Also someone could claim &quot;Whonix developers work for''*'' and choose entry guards, which are under their control&quot;. (Entry guards are a critical part when it comes to deanonymization.)
* (anonymous) I knew and read that but where does it say this is stored in &quot;/var/lib/tor/cached-*&quot;? The names and content looks pretty harmless as in &quot;nothing system specific&quot; just a snapshot of the full Tor network. Hence my - possible - misjudgement.
* (adrelanos) Not sure about how serious spreading the consensus is, to be sure, we simply shouldn't do it. Guard nodes are critical and are stored in /var/lib/tor/state. It's configured through torrc DataDirectory /var/lib/tor.

== Development related leaks? [SECURITY][DONE?] ==

* auth.log leaks IP of ssh clients, this is taken care of in the script
* resolv.conf leaks gateway IP, it is replaced on T-W and deleted on T-G
* Mirrors/ISP could probably figure out some things if we don't set up the build over Tor.
* lastlog but as auth.log will only leak internal VBox NAT 10.0.2.2

== Mac Address / harddrive UUID / harden VirtualBox [SECURITY][DONE] ==

* (adrelanos) All builds should share the same mac address. Each time the packager or private builder creates a new virtual machine, it gets a new random mac address. I propose to add to the build documentation, to manually set always the same mac address.
* (adrelanos) The same goes for the harddrive UUID.
* (adrelanos) And from our harden VirtualBox section. Shouldn't we list to deactivate USB?
* I don't think disabling it for T-W is a good idea as this also disables mouse integration. The rest of your suggestions are implemented, thanks for bringing them up!

== Whonix user open proxy [SECURITY][ANSWERED] ==

* (adrelanos) It came to my knowledge, that there is an open proxy on ports 9100, 9101 and 9050. Those ports could be used as socks proxy and were proxied through Tor. Using them as http proxy resulted in &quot;Tor is not an HTTP Proxy&quot;. I assume that someone is using Tor-Gateway on bare metal without VM while he does not use a hardware firewall and somehow must have messed up our firewall rules. Portscan revealed loads of other windows related open ports. By default we leave only port 22 open on external interface. Consequently, we can not be blamed for this issue or any adverse effects for this user. Anyway, should we post a news? (with hope that the particular user will notice) And add to some article &quot;use a hardware firewall, open ports only carefully, to not mess with our fw unless you know what you are doing&quot;? (I don't want to publish the (full) IP, in case of interest I'd send to torboxdev@).
* (anonymous) 100 bucks it's not a Whonix? Could be a honeypot, or just some stupid user who thought he could set up an open proxy and tor at the same time. The proxy is protected twice: through torrc only listening on the local IF and through iptables. You don't accidentally mess that up...
* (adrelanos) Okay, thanks.

== Hide DNS and DHCP info from Virtual Box [SECURITY][ANSWERED] ==

[Splitted off] * (adrelanos) New, maybe more clean solution to solve this whole &quot;DNS from host leak&quot; in the first place: [http://www.virtualbox.org/manual/ch09.html VirtualBox networking manual], &quot;Enabling DNS proxy in NAT mode&quot; and &quot;Using the host's resolver as a DNS proxy in NAT mode&quot;. * (anonymous) what does that solve? t-g non-torified works beautiful. when it's torified it MUST NOT use any dns but tor's own dns resolver. * (adrelanos) Above you suggested 'echo &quot;supersede domain-name-servers 127.0.0.1;&quot; &gt;&gt; /etc/dhcp/dhclient.conf', which works. (Replaces the router ip with localhost.) What still leaked from the host, what I reported, into resolv.conf was 'domain', 'search' and whatever else maybe written into resolv.conf (what I am not aware of and what won't happen to me, because of my network configuration). That would be prevented and the solution would be complete. * (anonymous) I didn't try it but it says &quot;DNS server&quot;, not &quot;DHCP server&quot;, those additional entries in resolv.conf are not related to DNS. Anyway, we want tor-gateway to work on bare metal and vm with minimal modifications and we should try to keep VM platform agnostic as far as possible. * (adrelanos) I didn't try yet either. Virtual Box is the first VM platform, who does not proxy that information by default anyway. Which is imho a stupid decision by VBox and a &quot;bug&quot;. Anyway, perhaps you are right.

== Tor stream isolation features [SECURITY][DONE] ==

=== IsolateClientAddr ===

* (adrelanos)'''IsolateClientAddr''': enabled by Tor default. Good for more than one Tor-Workstation. No changes suggested.
* (adrelanos) After reading Nicks answer, still no changes suggested. We just have to keep in mind, that the Tor-Workstations can change their IP's at will. As long as [Dev#EncryptionandAuthenticationbetweenT-GandT-WOPTIONALFEATURE:MultipleTor-Workstations Encryption and Authentication between T-G and T-W] isn't done, this feature works only as long as Tor-Workstation is not compromised.

=== IsolateSOCKSAuth ===

* (adrelanos)'''IsolateSOCKSAuth''': enabled by Tor default. Good as soon as Tor Browser fixes bug #3455. No changes suggested. As soon as #3455 is fixed, we have to test if it's compatible with Whonix's Tor Browser SocksPort 9100.
* (adrelanos) After reading Nicks answer, still no changes suggested.

=== IsolateClientProtocol ===

* (adrelanos)'''IsolateClientProtocol''': is it enabled or disabled by default? It doesn't say it's enabled by default (but also not the opposite). I guess it's not enabled by default, we might ask the Tor devs. Enabling IsolateClientProtocol sounds good at first sight, but might create issues. DNS will be resolved through one exit and connection will come from another exit. This might confuse some applications.
* (anonymous) not necessary for default t-w: http and irc are already isolated by SOCKSAuth, could be an optional feature for people who install custom applications (however, these days pretty much everything goes over http).
* (adrelanos) So leave it the Tor default? We may ask, what the default will be.
* (adrelanos) In #5437 Robert Ransom says, it's disabled by default.
* (anonymous) the answer to that depends on what &quot;dfbe779a450c089&quot; says which I couldn't find.
* (adrelanos) We really should consider enabling it. &quot;Don’t share circuits with streams using a different protocol. (SOCKS 4, SOCKS 5, TransPort connections, NATDPort connections, and DNSPort requests are all considered to be different protocols.)&quot; Tor Browser uses SOCKS 5. Apt-get currently uses TransPort and DNSPort. They would get isolated from one another, which were a really good thing.
* (adrelanos) Nicks related answer... {{{ &gt; IsolateClientProtocol &gt; Why is it disabled by default?

Most of the stuff you'd want to do with it is better done by having separate ports--especially if you're using RESOLVE calls. (This flag makes it so that socks4 and socks5 sent'''on the same client port''' won't get sent over the same circuit.) }}} * (adrelanos) It's indeed safe, but it doesn't do what I wanted. What I wanted, is done by default: Different ports and different types of ports, such as Socks, Dns and TransPorts do not share the same circuit anyway. We could enable it without sacrificing anything, but also with very little gain. I am neutral here.

=== IsolateDestPort ===

* (adrelanos)'''IsolateDestPort''': disabled by Tor default. Maybe we should enable it. Enabling sounds good at first sight, but might create issues. If an application uses several ports at once, the server could get confused by getting answers from different exit IP's. The Tor devs may have a reason, for not enabling it by default.
* (anonymous) This sounds pretty theoretical, are there any examples known? For default T-W setups it's not necessary because web and irc don't go over many ports, correlation of 80 and 443 on the same domain is not a concern as far as I see.
* (adrelanos) After Nicks answer we shouldn't enable it.
* (adrelanos) No known examples, only theoretical, never tested. It might happen, this introduces strange behavior, we'll see.

=== IsolateDestAddr ===

* (adrelanos)'''IsolateDestAddr''': disabled by Tor default. Maybe we should enable it. Enabling sounds good at first sight, but might create issues. If an application uses several destination IP's at once, the servers or the client application could get confused by getting answers from different exit IP's / circuits. The Tor devs may have a reason, for not enabling it by default.
* (anonymous) hardly a problem with confusion, the reason is most likely performance both for the end user as well as node operators. This setting results in tons of short lived circuits being created for ordinary web browsing, maybe not as bad as bittorrent but still. This definitely should be left disabled.
* (adrelanos) After Nicks answer we shouldn't enable it.

=== Nick's answer ===

* (adrelanos) I plan to ask tpo about their reasons for setting default yes/no for the flags. In past they always had some surprising reasons and insights. Let's create a message for the mailing list. (deleted draft, because posted to the mailing list)
* (anonymous) good idea!
* (adrelanos) Just posted. [https://lists.torproject.org/pipermail/tor-talk/2012-May/024401.html tor-talk Tor's stream isolation features defaults]
* (adrelanos) [https://lists.torproject.org/pipermail/tor-talk/2012-May/024403.html Nick answered]; [https://gitweb.torproject.org/torspec.git/blob/HEAD:/proposals/171-separate-streams.txt proposals 171]

=== Conclusion ===

* (adrelanos) [https://www.torproject.org/docs/tor-manual-dev.html.en Tor alpha manual], about stream isolation features. We'll need to decide which flags we should/could enable/disable.
* (adrelanos) Discussed everything. No changes required. If you disagree, reopen.

== Ask TPO if 0.2.3 is &quot;ready&quot; yet? [SECURITY][ANSWERED] ==

* (anonymous) #3449 doesn't look like it will be closed anytime soon. Current Whonix depends on 0.2.3 and won't ever become stable or see a new release till Tor 0.2.3 is stable enough to be used &quot;in production&quot;. Stable Tor is already called &quot;experimental software&quot;, the alpha branch is labeled something like &quot;more bugs than usual&quot;. If those bugs are just minor annoyances the added security features would be worth it, if these bugs include (potential) security issues this branch shouldn't be touched by any real users but only testers and devs. I think Whonix should ask on the mailing list and Tails what they recommend and plan to do. Switch to tor-0.2.3 and declare it a ready &quot;beta&quot; version (a real stable 1.0 is far in the future anyway for all 3 projects) or switch back to tor-0.2.2 for the current &quot;supported&quot; or &quot;stable&quot; Precise based Whonix-0.2 release, at the cost of stream isolation. On that note: If all you do is use the browser Whonix is exactly as susceptible to correlation as the latest TBB. It's not really that critical if you think about it that way...
* (adrelanos) I agree, let's create a message for the tpo mailing list. I am going to use most of your insight. Asking Tails is also a good idea, not sure we need an extra message. You can revise the text (anything, I don't want to disagree a lot, no need for perfection) and then you or me will post it on the list. (deleted draft, because it has been posted to the mailing list)
* (anonymous) get's my OK. Please post it.
* (adrelanos) Posted. [https://lists.torproject.org/pipermail/tor-talk/2012-May/024408.html tor-talk Tor 0.2.3 Alpha ready for redistributed projects?]
* (adrelanos) [https://lists.torproject.org/pipermail/tor-talk/2012-May/024426.html Nick answered].
* (adrelanos) If I were to summarize his very nice and detailed answer with a very few words, I'd write:'''&quot;No, it's not ready.&quot;'''. Therefore we shouldn't do it. A pity, but at least, we know it.

== Torify T-G by default / Hide Whonix fingerprint / Enhance obfuscated bridge support / Enhance Hide Tor use support [SECURITY][IMPLEMENTED] ==

* (adrelanos) Old discussions: [Dev/ArchivedDiscussion/OPTIONALFEATURE#forbidnon-ToremissionshideyourTorWhonixusageOPTIONALFEATUREIMPLEMENTED forbid non-Tor emissions / hide your Tor/Whonix usage]; [Dev/ArchivedDiscussion/OPTIONALFEATURE#HideWhonixusageTorifyT-GoptionalOPTIONALFEATUREIMPLEMENTED Hide Whonix usage / Torify T-G].
* (adrelanos) At the moment obfuscated bridge users are very poorly supported by Whonix. Transport plugins, obfsproxy, SkypeMorph and such, are the future. They have to torify T-G, otherwise their updates are blocked by their ISP. Activating #OptionalFeatureNr.1# is too inconvenient. Each time they get an updated script and/or download the binaries, they have to prevent non-tor emissions, i.e. they have to pull the (virtual) network cable. They have to enable the feature again by uncommenting loads of lines, re-apply the firewall, restart Tor and plug in the (virtual) network cable again. We're asking for too much. Also the chapter [OptionalConfigurations#HidethefactthatyouareusingTorWhonix Hide the fact that you are using Tor/Whonix] is a mess and way too complicated.
* (adrelanos) Also Tails has the requirement not to reveal any Tails specific fingerprint to the ISP. We are not tails, but we should listen to their expertise, their project is much older and mature. We clearly have our own fingerprint, 1) torproject repository 2) minimal installation + removed packages + few selected installed package 3) no NTP 4) no automatic updates 5) no graphical desktop (#command line user, this group is much smaller than the desktop user group). All these things together make Whonix's Tor-Gateway pretty unique.
* (adrelanos) And it's also good for security and marketing. Only the Tor process were allowed to establish direct connections. That's the safest method against leaks. Even if T-W manages somehow (bug/exploit) to connect to some IP, he shouldn't connect to, the outgoing request for the internal IP would be routed through Tor and ignored.; Another advantage: We can finally fix [Dev#Nameserverdomainsearchetc.mightleakintoresolv.confSECURITY Nameserver, domain, search, etc. might leak into resolv.conf]. We'll know what to write into resolv.conf: &quot;nameserver 127.0.0.1&quot; and protect resolv.conf with +i.
* (adrelanos) Disadvantage for this change: apt-get downloads are slower. Well, they are already slow on T-W. They must not be ultra fast, it's important to do them.

== Nameserver, domain, search, etc. might leak into resolv.conf [SECURITY][FIXED] ==

* (adrelanos) With -vm switch. Module on: optional_torifytg. Module off: optional_staticvboxip. Haven't found the bug yet. (That's why I wanted detailed echos for each ifup/ifdown step to narrow it down.) {{{ ###################################################### -Start networking-. ###################################################### ifdown eth1 --force ifup eth0 OK: Latest firewall updates can always be found here: OK: https://trac.torproject.org/projects/tor/wiki/doc/Whonix OK: Loading Whonix firewall... OK: The firewall should show any messages besides output beginning with prefix OK:... OK: Whonix firewall loaded. RTNETLINK answers: File exists ^C ###################################################### ERROR: Script failed! INFO: Rolling back configuration... ###################################################### cleanup(): set +e... cleanup(): stopping tor... Stopping tor daemon: not running (there is no /var/run/tor/tor.pid). cleanup(): restoring backup files... cleanup(): deleting /etc/torboxfirewall.sh... cleanup(): deleting /home/user/leaktest/... cleanup(): flushing iptables rules... cleanup(): ifdown -a... cleanup(): ifdown eth1 --force... cleanup(): ifup eth0... RTNETLINK answers: File exists ^Ccleanup(): ifup -a... }}}
* (adrelanos) The &quot;RTNETLINK answers: File exists&quot; persists until CTRL + c is pressed.
* (anonymous) RTNETLINK is a bitch. It's a bug in ubunut and I have no idea how to even begin to fix it because I don't know how to trigger it. I can't reproduce, works for me: enabled all OptFeature1 (torrc, firewall, vm) and it didn't complain. I remember it got something to do with 'route'...
* (adrelanos) It was probable still because chattr +i on /etc/resolv.conf. Unfortunately it's not fixed anyway.
* (adrelanos) With this configuration &quot;on: optional_torifytg; off: optional_staticvboxip&quot;, DHCP is still used for eth0 in /etc/network/interfaces. Subsequently DHCP rewrites /etc/resolv.conf and inserts the name and ip of my router. - That's what I wanted to prevent with chattr +i on /etc/resolv.conf earlier.
* (anonymous) echo &quot;supersede domain-name-servers 127.0.0.1;&quot; &gt;&gt; /etc/dhcp/dhclient.conf<br /> Don't use chattr. Please test.
* (adrelanos) That replaces nameserver with 127.0.0.1. domain and search (in /etc/resolv.conf) has still the name of my router.
* (anonymous) how did you restart networking? removed resolvconf? tried deleteing /etc/resolv.conf? It doesn't happen for me...
* (adrelanos) Removed resolvconf: was already removed.; tried deleteing /etc/resolv.conf?: yes, it will be created again with those contents.; how did you restart networking?: sudo /etc/init.d/networking restart; It doesn't happen for me: My network/router might me slightly different. I wonder since I use VirtualBox how the VM comes to find out what name my router has...
* (anonymous) that could be it. Try changing /etc/dhcp/dhclient.conf e.g. remove the request domain-search, domain-name... or supersede it.
* (anonymous) How it finds out about it, well either it queries the dhcp client on the host or it does its own dhcp &quot;lookup&quot;, then it proxies that information to the guest (i guess).
* (anonymous) ed -s /etc/dhcp/dhclient.conf &lt;&lt;&lt; $',s/domain-name,//g w'
* (adrelanos) Sorry, I am not done testing that. And if, I want to add a generic solution in the T-G script.
* (anonymous) Generic as in VBox, other VM and bare metal? So keep dhcp and make it work with &quot;nameserver localhost&quot;?
* (adrelanos) 1) Generic as in VBox and bare metal. 2) So keep dhcp and make it work with &quot;nameserver localhost&quot;?: Yes. Use dhcp but configure network and to leave resolv.conf untouched, if that is possible at all. If that isn't possible, we can simply set manual network and inform about the necessary manual adjustments.
* (anonymous) Generic Solution: Keep dhcp, don't edit resolv.conf at all and add a prepend or supersede nameserver 127.0.0.1 and the options from above to prevent domain and search (I don't think they are needed at all). Prepending means that the Tor DNS server will fail open: If tor is down if you try to use apt-get it will make a dns request for deb.torproject.org in clear text. Does Tor need a working DNS resolver to bootstrap? If not we can use supersede. Needs testing.
* (adrelanos) Tor does not require a working DNS resolver to bootstrap. From guessing: at least when using bridges, it were fatal to rely on DNS. From testing: I stopped Tor, deleted /var/lib/tor and restarted Tor while DNS was defunct (no entry in /etc/resolv.con), Tor was useable. Domain and search were indeed never required for me. I am fine omitting them. When using optional_torifytg, it's not a good idea to make any DNS requests in the clear. That would defeat the whole purpose of that feature. Your proposed solution sounds fine.
* (adrelanos) After some reading I don't believe, that supersede is a good solution. We knew, that nameserver, domain and search could contain leaks. After reading the [http://linux.die.net/man/5/resolv.conf resolv.conf manual] (no idea how up to date it is] it comes up, that there is also sortlist. And the [http://manpages.ubuntu.com/manpages/precise/man5/dhcp-options.5.html dhcp options] are endless. And if at any point new stuff is added to that file, that were also bad. The only solution can be, to not let DHCP edit resolv.conf at all. [http://www.cyberciti.biz/faq/dhclient-etcresolvconf-hooks/ How To: Make Sure /etc/resolv.conf Never Get Updated By DHCP Client]. +i is no option, since boot will take too long. I didn't find an option in dhclient to completely disable modifying resolv.conf once and for ever. Overriding make_resolv_conf() is also no option for our case, when dhclient gets updated, that file could get replaced. Completely remove DHCP, no problem with VirtualBox, but makes T_G bare metal setup more complicated.
* (adrelanos) Perhaps we can use +i. That could be a fine solution, if this [https://bugs.launchpad.net/ubuntu/+source/upstart/+bug/886414 bug] were fixed. There is a [http://www.codewhirl.com/2011/10/ubuntu-11-10-waiting-up-to-60-more-seconds-for-network-configuration/ workaround]. If that were to work, that'd be a fine solution.
* (adrelanos) Done. What's left is automating the workaround. But that's left as a TODO notice in the script.

== do not use .onion for tbb download [SECURITY][DONE] ==

* (anonymous) There is no security or privacy reason to use the TPO HS but it breaks building t-w over clear net.
* (adrelanos) There is one security reason. Using the SSL version is vulnerable to malicious certificate authorities. The HS version is encrypted end-to-end (or to be exact, Tor to Tor).
* (anonymous) But we already use gpg for authenticity and integrity, which is a bit more secure than 80 bit (no pun intended).
* (adrelanos) Good point. I recently had a similar discussion on the Tails mailing list. Start post: [https://mailman.boum.org/pipermail/tails-dev/2012-June/001245.html Tails-dev Removing SSL CA dependency for HTP]; My reasoning on [https://mailman.boum.org/pipermail/tails-dev/2012-June/001247.html HS vs SSL]; convinced [https://mailman.boum.org/pipermail/tails-dev/2012-June/001260.html intrigeri].
* (adrelanos) My motivation in HS was, once an adversary spoofed torproject.org SSL, he couldn't even run an attack against wget's download mechanism. I wish someone breaks the 80 bit system and they'll finally update to something more secure. And I forgot, that the GPG key fingerprints are already hardcoded and not dynamically downloaded. I forgot, that it's not like downloading a file and a hash from the very same source. The GPG check is not only a integrity check, it's also authentication. And that point won't make sense until check.torproject.org gets an HS (if ever, before thandy, if thandy comes ever to live). I am ok with commenting out. Please leave in as comments, to let the idea alive (in case they upgrade from 80 bit to something stronger and check.tpo get's an HS).
* (anonymous) I understand where you are coming from. The thing is, HS is not the real answer to fixing TLS. It will always have to make a trade off between being rememberable, secure and global (you sure have seen this triangle), it's not true end-to-end and it isn't portable enough and there's the bootstrapping problem (you already need tor running, this comes into play again with htp over HS). The -stop gap- solution is certificate pinning. wget doesn't do it but Firefox Addons (#TorButton) make use of it. There's I think a real need for a cli or lib that can offer certificate pinning to other low level utilities.
* (adrelanos) Where to file a ticket?
** (anonymous) uh, kickstarter? I don't know, I can't think of a project where this would even fit on a whish list, this would be new project from scratch.
* (adrelanos) Another minor advantage using HS is, it makes [https://blog.torproject.org/blog/experimental-defense-website-traffic-fingerprinting website fingerprinting] harder, since there is no exist, who can monitor an encrypted connection to tpo.
* (anonymous) Fingerprinting can be done by everyone in the circuit, it's most interesting for entry/guards node. They already know who you are and can this way relatively cheaply discover who you are communicating with.
* (adrelanos) Done.

== No longer temporarily add a NAT adapter to Tor-Workstation / Getting T-W script into T-W [SECURITY][Whonix 0.2.0] [DONE] ==

* (adrelanos) We should not even temporary add a NAT adapter to Tor-Workstation. Pros of temporary NAT adapter: 1) faster download during installation. Cons: 1) IP and mac address might get stored somewhere Tor-Workstation's log files. We've overseen the mac udev rule already. Mac address gets stored within udev rules. 2) The apt-get install line reveals (ISP), that someone is installing Whonix. 3) Forgetting or failing (future bug) to remove the NAT adapter is a disaster. 4) It lengthens the build documentation. 5) We can't download TorBrowser from torproject's hidden service (flawed SSL certificate authority system). Conclusion: The disadvantages clearly outweigh the minor advantage. Unless there is a real disagreement here, I am going to change that soon.
* (adrelanos) Without nat adapter, there is also no port forwarding. I probable have to add a temporary [https://www.virtualbox.org/manual/ch06.html#network_hostonly host only adapter] for ssh.
* (anonymous) Doesn't that add the host's MAC and stuff again? This could be solved if we remaster the install iso to already include our script (see Ubuntu unattended (automatic) installation)
* (adrelanos) Indeed, T-W would temporarily see the host's MAC. Is that a problem? Does that MAC get logged somewhere?
* (adrelanos) And T-W would store the MAC of the host only adapter, even that host only adapter gets removed later. This MAC could be shared among all Whonix users and be deleted while running the T-W script.
* (adrelanos) We have several ways to get the script into T-W. 1) We could install openssh-server on T-W and ssh it from T-G, transfer the script. 2) install a temporarily, while building, a tiny webserver on T-G, on T-W wget 192.168.0.1 to get the script. (To prevent connecting to the &quot;wrong&quot; gateway, which could be an already running compromised T-W, we could use a self singed SSL certificate.) 3) Mount the hdd image on the host, insert the script, unmount. Not sure if mounting the hdd image on the host will (not) leak something from the host into the image. 4) Remaster the CD, not how complex/flexible/complicated that is (see Ubuntu unattended (automatic) installation).
* (adrelanos) Let's do the fully automated builds after Whonix 0.2.0. I'd be happy with a quick fix for Whonix 0.2.0.
* (adrelanos) As a quick fix for Whonix 0.2.0 I am inclined to ssh T-W from T-G. Any objections?
* (anonymous) No, not on a clean system.
* (adrelanos) This won't work. After VM Creation and Installation, Tor-Workstation does not even have a network interface. Apt-get is defunct, openssh-server can not be installed.
* (adrelanos) The best quick fix might be to mount the image.
* (adrelanos) Done. Looks good, imo. Any feedback?
* (anonymous) with debootstrap we need to re-investigate this issue.

== Identity correlation through circuit sharing [SECURITY][SOLVED] ==

* (adrelanos) old title: Identity correlation through circuit sharing / TransPort and DnsPort only optional
* (adrelanos) Robert Ransom ([https://www.torproject.org/about/corepeople.html.en Tor core people]) said that he [https://lists.torproject.org/pipermail/tor-talk/2012-March/023536.html is not a fan] of Whonix because &quot;Whonix provides pseudonymity, not anonymity&quot;. The Tor developers opinion should be very important to us. And also in my own opinion it is not good to let an evil exit node build a profile about all application one is using.
* (adrelanos) I don't like to propose it, but I have to. I propose to make TransPort and DnsPort optional, to comment it out in torrc. It is the only way to mitigate both, TCP and DNS identity correlation. This kinda defeats one of Whonix's biggest advantages, that there were not manual proxy settings necessary. On the other hand, Whonix would still be very useful. It's still an isolated system were no one even with root can break out.
* (adrelanos) Implementation idea for the shell script: Can we set variables like SOCKS_PORT_TB and SOCKS_PORT_IRC globally, so we can also use those variables inside torrc? In torrc we could add then SocksListenAddress 192.168.0.1:SOCKS_PORT_TB or something like that. Unfortunately torsocks has a dependency to Tor. So we have on the Tor-Workstation to do 'apt-get install torsocks --no-install-recommends libevent-2.0-5 libreadline5 polipo socat tor tor-geoipdb' (untested).
* (anonymous) This needs to be tested but it seems one can put variables within single quotes by single quoting them again (var#Variable &amp;&amp; echo 'this '$var' works'). I already wanted to do that because''_IF#eth'' should really be declared at the top...
* (adrelanos) We would also have to check the other articles what would need change/be broken. Actually quite a lot. Leak testing for example. Also a chain of Tor Workstation Tor -&gt; Proxy/VPN/SSH would not work so well anymore (only using proxychains or privoxy). I already started to revise the [https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO TorifyHOWTO], as we will have to tell our users to use it. What is also bad, that torsocks does not support command line options, there would be a new configuration file and new socks port needed for each application. And like Robert Ransom said in the mail, we also would have to use Tor alpha until stream isolation is in Tor stable.
* (anonymous) Currently we have 3 applications that are routed through Tor: TB, xchat and apt-get. Using the new optional socksport settings in the script all concerns by rransom are answered. Just add a warning to the top of the home page and we got ourselves covered and no one can claim Whonix users could even remotely be mislead. However, the whole argument is moot as longs as TB goes through a single SocksPort and Tor isn't intelligent enough to isolate different user contexts/sessions in different tabs and windows. I remember reading something about Tor looking for empty referrers which would indicate that the user opened a new tab and entered a new domain or clicked on a bookmark. As long as the current stable doesn't do that we don't need to do anything. Compared to correlation within TB(B) the apt-get issue is just ridiculously unimportant:
* (adrelanos) Indeed it doesn't make sense, that Whonix should be guilty of what everyone [https://lists.torproject.org/pipermail/tor-talk/2012-March/023535.html was affected] during all the years. Your [https://lists.torproject.org/pipermail/tor-talk/2012-March/023543.html answer] on the mailing list was very good. Unfortunately there was no reply again. So what shall we think now... That he is convinced now that the severity is not as bad as originally thought or does he see it as trolling and doesn't want to answer again...
* How often do people run apt-get manually via command line anyway?
* T-W is small, there are few and small updates (apart from the 0-2 monthly kernel updates)
* apt-get update takes a few seconds
* t-w fingerprint by default is not unique, that's not pseudonymity, it's only anonymity set reduction.
* there's already enough documentation on that on Whonix/* (like: before and after updating get a new ID)
* Yes, this is critical, but wrt to TBB through it's own sockport OR shared transport not our current binary/default Whonix implementation. I strongly believe we can continue using DNSport and transport - if only as a fallback for less critical communications.
* UPDATE: found it: #3455 Also, why shouldn't #1865 work with transport and dnsport just as well as with socks?
* (adrelanos) After reading the [https://www.torproject.org/docs/tor-manual-dev.html.en Tor Alpha Manual] I also don't see why the stream isolation wouldn't work with TransPort. We can not simply switch to use the alpha version. It fixes one problem but then we may be criticized for encouraging to use the alpha version. However, the isolation flags look very well. It's a feature I am looking forward to. It needs testing, but for now it looks like with IsolateDestPort and IsolateDestAddr any identity correlation should be very unlikely. This doesn't include the Tor Browser issue, but that is outside the scope of Whonix.
* (adrelanos) We have a workaround in our wiki. [ApplicationWarningsAndNotes#Identitycorrelationthroughcircuitsharing Identity correlation through circuit sharing] With the release of Tor stable 0.2.3 we will fix this. UPDATE: our shell scripts are already working with Tor alpha and prepared for the next Tor stable.
* (anonymous) close? tor beta is stable enough for a torbox beta...
* (adrelanos) Solved. Documentation needs revision to match Whonix 0.2.0 but I do that right away.

== Tor-Workstation requires a firewall [SECURITY][IMPLEMENTED: OPTIONAL FEATURE] ==

* (adrelanos) After reading again [SecurityAndHardening#NotesaboutEnd-to-endsecurityofHiddenServices Notes about End-to-end security of Hidden Services], it came to my mind, that we actually care about two things. 1. Hiding the users IP/location and 2. keeping data confident. If we assume, that an adversary could break into the Tor-Gateway (because he found a zero day in Tor's code), the user still does not want to give away all data hosted on his hidden server etc. The firewall for Tor-Workstation could also drop invalid packages and drop all prevent exposing local services (in case the user installed any) to the Tor-Gateway. If the user is using hidden services, that port has probable to remain open, needs testing. The firewall becomes even more interesting when [Dev#MultipleGatewaysOPTIONALFEATURE Multiple Gateways] are possible.
* (adrelanos) Here is my first draft. (Can be deleted from the wiki, as soon it gets added.) Feel free to comment/modify. UPDATE 5: deleted from /Dev, added to T-W script. Done.
* (anonymous) &quot;# - Should allow unlimited TCP/UDP/IPv6 traffic on the virtual external interface (OnionCat / OpenVPN).&quot;
* (anonymous) It obviously can't mean allow &quot;anything anywhere&quot; or we wouldn't need a firewall in the first place, do you mean something like firewall eth0 and allow tun0? I think for openvpn to work you need allow rules for eth0 as well. Think of it as virtual being routed over the physical, if you block the latter completely everything will stop. I think we need more fine-grained default rules: allow socks ports in and out, dns port, with the torsocks wrapper available we can even add a block 80/443 rule, we could set openvpn default port to allow. Not sure about OnionCat at all, pretty much a dead project last time I looked
* (adrelanos) The idea was, the the default network interface on T-W, eth0 gets firewalled by us by default. If the users adds any adapter himself, i.e. connecting to Tor -&gt; VPN service or adds some virtual device such as OnionCat, that it won't interfere with it. It's up to the user to secure additional virtual network adapters.
* (anonymous) I'd prefer not using any firewall by default for now, there are no listening services on t-w, and if the user installs one (ssh, webserver, vpn) he probably wants them to be reachable. Right now the firewall only breaks things and adds no security benefits I can see.
* (adrelanos) Good to have some feedback about this one. Did you read the &quot;# DESIGN NOTES:&quot; in the firewall comments? It has some pros and cons. Not best invention ever, but do you think it's really pointless?
* (anonymous) still do. &quot;Some additional security.&quot; Some is meaningless if we can't measure it... For example, if Tor on Tor-Gateway were compromised through a zero day exploit&quot; - with the default set up the firewall blocks nothing from t-g (because no listening services are enabled). &quot;In future, there will be an optional feature, to chain&quot; - it's these features that first get broken by the firwall, I experienced that when testing openvpn between t-w and t-g. A firewall becomes absolutely necessary if one runs services on t-w and has multiple t-w, both is non standard and will require non-standard firewall scripts depending on the particular set up. There's a good reason OSs come with permissive firewalls by default, out of the box they don't offer any new security but only break things...
* (adrelanos) At least the filtering of bogus packages makes sense.
* (anonymous) we had that discussion with the t-g firewall too. Bottom line: bogus packages that we know about (like XMAS) will at worst be a DOS (which we can't really prevent anyway), they don't result in code execution.
* (adrelanos) Anyway, we can leave the firewall optional. We simply have to disable the pre-up in interfaces. The firewall is mostly important when installing additional software or using multiple workstations at once. But I agree, it comes in the way sometimes.
* (anonymous) agreed

== [[#security|SECURITY]] Automatic Updates [REJECTED] ==

* (anonymous) Should we use them? On both, only T-G?
* (adrelanos) On T-W: depending on what's the outcome of &quot;updates over Tor, should not waste Tor bandwidth&quot;.
* (adrelanos) On T-G: if we do so, we should inform the user (and tell how to disable them). Some might use internet access with limited quota very quota is very expensive. There are not much reasons against it, only quite paranoid and unlikely ones, ff Ubuntu's update mechanism were compromised (a backdoored update would be pushed) then it would make sense for users to read news before manually updating. Any more pro/cons?
* (adrelanos) Ok, after reading [https://lists.torproject.org/pipermail/tor-talk/2012-March/subject.html#23507 this] we shouldn't use automatic updates. At least not at a fixed time, if, then at randomized times. What we could do would be notify the user without actually sending requests to the network.
* (anonymous) Problematic for many reasons. For example: when using manual updates you'll probably register a stale mirror attack (Ubuntu is vulnerable).
* (adrelanos) Reopened. Some time passed. We can reconsider this. Lots of things changes. Traffic is a non-issue, torproject.org did NOT ask us to cease downloading updates over Tor. Time zone is now set to UTC. Stale mirror attack can not be mount over a longer amount of time, since exit nodes change, unless there is a big attack on Tor but not using automatic updates wouldn't circumvent this either. Identity correlation will be no longer at risk with the current version in development (Whonix 0.2.0) due to use of stream isolation (apt-get uwt wrapper).
* (adrelanos) One thing: if you have a well known hidden service called X with some special configuration, let's say as example you provide pop, imap, irc, thttpd for anyone, that may be a very special mix of services. So when you update, the exit/mirror can find out: hidden service X runs updating. Imho this is a non issue, it would happen when not using automatic updates as well.
* (adrelanos) Knowing all that... So what's the difference of running'''apt-get update''' and'''apt-get dist-upgrade''' once a day at some human-random point versus automatic updates? Does the exit/mirror get the unixtime while updating? Even if yes, we have to partially solve the time sync ticket. If the time is not exact for host/clear-updates vs T-G/W/torified-updates the exit/mirror should not be able to correlate them.
* (anonymous) Automatic updates are dangerous. All updates are dangerous. They are remote root backdoors (with some restrictions and checks of course). The problem is, if &quot;something&quot; goes wrong it will automatically propagate accross all users in a very short amount of time. On the other hand, if you update manually a day later or so, it's likely that somone else has noticed the problem and notified Canonical and you stay save. Lots of things can &quot;go wrong&quot;: a dev system, a build system, the key or the crypto system could become compromised. It has happened several times, openssl issue, Fedora/RedHat, kernel.org, Flame malware. Not all of them would be mitigated by using manual updates (only donwloading the patches, reviewing them and manually applying them would. Sadly for that to be usable the TCB is too complex and large, it just wouldn't scale. Software updates are messy but right now a necessary evil. I feel more comfortable not letting them run in the background without any verbose output. The one day more or not will not impact security. With Linux distros it already takes time anyway between upstream fix and downstream release. Further, if it's a 0day you already lost that one (and have to rely on the additional security that Whonix provides). A single security issue should never impact security in a fatal way. It still does in Whonix 0.* but I hope that can be changed. i.e. we need to migrate away from using the same OS for t-w and t-g. This includes the kernel and I'm not really sure what alternatives there are. Essentially there's only*BSD. See new ticket...
* (adrelanos) Must agree. That is still true and will remain so. Thanks for revisiting.

== [[#security|SECURITY]] update-notifier [IMPLEMENTED] ==

* (adrelanos) I hate to dig again into this topic, we rejected automatic updates, but what about an update notifier? I experiment with installing update-notifier and if I manage to force it through it's own SocksPort I consider to install it by default.
* (adrelanos) Done in github devel branch, will be in 0.3 and above.

== [SECURITY][FINGERPRINTING] torcheck checking SocksPort, TransPort or both [DONE] ==

* (adrelanos) Which port should torcheck check? Tor's TransPort or Tor's SocksPort or both? The SocksPort will most likely always use Tor, because it accesses the port directly. No matter if the user installed VPN on Whonix-Workstation, it will use Tor. On the other hand, when testing TransPort, the user will see if he set up a transparent proxy or VPN within Whonix-Workstation. The TransPort is also sightly more probable to leak, because if there is ever something leaking (which is unlikely), than not the correctly torified applications will leak, but those who are supposed to use the TransPort.
* (adrelanos) On the other hand, using wget on https://check.torproject.org leaves a clear Whonix fingerprint and pollutes the TransPort circuit for maximum 10 minutes.
* (adrelanos) The pollution issue makes me think, that if we are using SocksPort, we should probable use uwt to redirect wget to use a special SocksPort, which is solely used for torcheck.
* (adrelanos) And if we would check TransPort and SocksPort we could compare the IP's and demonstrate, that stream isolation is functional or even deploy big scale testing and catch a bug. Implementation is easy and I'd do it. Design decision is to be discussed.
* (anonymous) TransPort isn't used for anything by default, it's supposed to become &quot;polluted&quot; and not to be used for anything where circuit correlation could be problematic. TODO: this needs to be documented... Torcheck doesn't leak much, it only leaks to torproject.org that someone is using wget to scrape the site, that's not even a clear indication that someone is using Whonix. Exit nodes can only see that someone is accessing tpo, not with what browser, that information is pretty much meaningless. The only bad thing that can happen is a TLS MITM, against which the SOCKSPort doesn't do anything (but running against multiple exits does!) Having the script test stream isolation is a nice idea, just keep in mind there'll likely be occasional false positives.
* (adrelanos) Stream isolation test has been added. The feature requires explanation, but the whole feature needs explanation. Not even tpo explains it. (#6102 no owner, no assignee, no milestone # I doubt anyone will do it anytime soon.) Not sure if there can be false positives with the stream isolation test. Tor is supposed to give those ports a different circuit. I don't know if different circuit includes &quot;must be also a different exit&quot; or if it's simply &quot;different route, may be the same exit&quot;.

== [[#security|SECURITY]] encrypted update download ==

* (adrelanos) I think I can spare out why this is useful. Downloading updates, using apt-get over SSL or a similar solution would be very useful. Can you think of a solution we can use right now? If we don't find a solution our self, we can at least promote [http://brainstorm.ubuntu.com/idea/26541/ Idea #26541: Enable end-to-end SSL for Ubuntu Updates] on our front page.
* (anonymous) I don't see how that helps. This requires us to trust mirrors and mirrors by design are never to be trusted. Also https sucks for security. This wouldn't offer protection if tor was outlawed. National firewall can simply issue their own cert for deb.torproject.org (the proposed solution to use a hardcoded cert doesn't work with the mirror infrastructure, or do they think handing out the private key to every mirror is a good idea?) Protection against fingerprinting of T-W can simply be achieved by making apt-get go through a separate socks port so it gets it's own circuit that can't be correlated with your other activities. As detailed on the mailing list I do not consider this very security critical.
* (adrelanos) Advantage: hash collision is more likely than breaking into AES encryption. Signing is nice but encrypting everything makes it much harder to inject anything.; Not all governments are able to issue a spoofed SSL certificate. Even if we assume that governments can not be excluded, it works well against exit nodes, this would certainly make fingerprinting much harder (we could use automatic updates) and hash collision more unlikely. Ubuntu.com would still sign everything, name the mirrors, publish the trusted mirror list including each of their specific fingerprints. Each mirror had their own SSL certificate. An certificate authority is not needed.
* (adrelanos) It's also questionable how much is signed. Also the answer with which packages are updatable? Because the traffic is not encrypted, an adversary (exit node) can spare out one update or another.
* (anonymous) These are all well and long know issues a software update system should protect against today. From 2008: https://www.cs.arizona.edu/stork/packagemanagersecurity/ As a response there was the project apt-secure which replaced the old insecure apt-get. Everything is (or should be) signed now. Debian does protect against maliciousness exits preventing individual updates. Much to my surprise, Ubuntu doesn't seem to use that feature! https://bugs.launchpad.net/launchpad/+bug/716535 I think we should set a Max-ValidTime in apt.conf. This will throw a false positive if there hasn't been any update to a repository in N time. About hash collision vs AES: TLS depends Hashes (still see md5 around), Tor depends on sha1, gpg depends on sha1. If a pre-image attack is possible against sha1 we are all f****ed anyway.
* (adrelanos) That [https://bugs.launchpad.net/launchpad/+bug/716535 bug] is really sad. It's not even confirmed because less then 5 people clicked the &quot;I am also affected button.&quot;. Not sure if Max-ValidTime in apt.conf is a good idea. Have you tested it? What do we do once we have the first false negatives?
* (anonymous) Maybe we'll see this getting fixed soon: ubuntu.5.n6.nabble.com/Re-The-following-packages-cannot-be-authenticated-td1817427.html I couldn't get Max-ValidTime to only apply to security updates. apt.conf syntax is the most awful thing I've ever seen for a config file. We can only apply this setting to security, and update repos, the release repos don't get updated after release (i.e. it complains &quot;invalid since 139d&quot;). However I can't figure out how to do that, I can only set Max-ValidTime for all &quot;Ubuntu&quot; repos, or none. The problem is the way they handle the &quot;Label&quot; in releases ([http://security.ubuntu.com/ubuntu/dists/oneiric-security/Release Ubuntu] vs [http://security.debian.org/debian-security/dists/stable/updates/Release Debian]). The only option that works so far is disabling stable repos in source. This should mean we still get security fixes but one can't install new software via apt-get. (But one can still install new software if it has been updated since release, and doing so I got some scary warnings about missing verification). Messy stuff, I don't see how we can offer a reliable workaround, we'll have to wait for upstream - or change upstream.
* (adrelanos) Added warning/information under [ApplicationWarningsAndNotes#Softwareupdaters Software updaters].'''Solution''': either we or the user switch to Debian or to some other operating system not affected by this issue. (see thread &quot;Switching T-G to Debian?&quot;)
* (adrelanos) Can the package apt-transport-https be of any help? Https would give us privacy, from the exit node, over what we are downloading.
* (anonymous) since tg is now torified by default additional encryption is no longer necessary. Also the ubuntu bug is of a much lesser concern because with ever changing exit nodes there is a very slim chance for an attacker to mount a freeze attack over any extended amount of time (i.e. &gt;10 minutes...) I don't want to close this because no using all apt security features is still stupid. BTW, no update on that bug, wheezy is supposed to reach feature freeze this month.
* (adrelanos) Encrypted updates would still offer an advantage. Exit nodes couldn't even guess that someone uses Whonix. That would make it harder for exit nodes to exploit something, would also add more privacy about installed packages. I don't think upstream will add this feature anytime soon. Ubuntu doesn't even offer download of images over https. I saw a discussion somewhere, that they don't want to do it because that would cause quite some CPU load. That might be the same with apt-get. I think we can close this one as [UPSTREAM ISSUE].
* (anonymous) That would be called security through obscurity, and even that wouldn't work out because exits can see you making a connection to a known ubuntu server. apt-get freeze attack issue is tracked in related bugs, therefore closed.

