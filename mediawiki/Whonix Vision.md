[[include ref=WikiHeader]]

[TOC]

= Whonix² =

That's just a code name for a '''BOX''' setup &quot;2.0&quot; that may eventually offer strong guarantees of security and anonymity.

It should address all the current single points of failure:

'''CPU:''' Even in a microkernel + IOMMU system the CPU (and to some extend the GPU, this ) needs to be trusted blindly. The system needs to consists of multiple (diverse) CPUs. Whonix with Physical Isolation already does that. This is just an reminder that software based isolation (through next gen sandboxing and microkernel design) will never be able to replace hardware isolation.

'''Software/Compiler''' Even if the TCB is small and verifiable to some extent there is an inherently unsolvable problem: Compilers (&quot;trusting trust&quot;). The only option to improve this I see is to rely on a diverse &quot;polyculture&quot; of software stacks and infrastructure instead of our current Windows and gcc monocultures. (I suppose most .mil and all research microkernels are written on monolithic untrusted &quot;legacy&quot; systems). Alternatives do exist (most likely built with gcc...) but probably not mature enough, though I hear OpenBSD kernel can be built with pcc. clang/LLVM is probably the best bet. This also extends to the build system, workstations and gateways should be built on their respective target platforms, not a single build system.

'''Software updates:''' Currently, one single bad update from Debian and it's game over. Software updates are always a root &quot;backdoor&quot;, they grant unknown people full remote access to all your systems. This needs to be changed. If the TCB is small and well tested there won't be many security updates and they will be simple, small patches. Deterministic binary builds could make that userfriendly. At least we should not rely on a single organization to provide security updates for all systems in Whonix (this includes having the same upstream for complicated software, i.e. the Linux kernel...).

'''Tor:''' Currently, one serious Tor vulnerability and it's game over. Even with true end-to-end communications, if Tor (or its TCB) is subverted an adversary can find out who is talking and to whom one is talking. Whonix should route all traffic over at least two strong anonymity networks (not just single hop proxy/VPN/SSH). Further, there should be the option to use a high latency network. This could be as simple as a single hidden service (which would have to be fully trusted to not collude with our &quot;global adversary&quot;. A real solution would of course have to be decentralized. The only options so far are remailers (Mixminion...) but those have few users (poor anonymity set) which is probably related to their outdated user interface and experience. However, even with a small number of users, if remailers are routed through Tor they are still more secure than Tor (in this context the resulting anonymity is cumulative).

''* &quot;Protocol leaks&quot;, Anonymity set reduction:''* The current platform of choice (for pretty much everything, including anonymous communication) is the web browser. Browser really suck when it comes to privacy, anonymity or security. Allowing scripting, storing IDs (cookies and more), constantly changing features (html5, webgl, websockets...), [http://rdist.root.org/2010/11/29/final-post-on-javascript-crypto/ lack] of strong crypto environment make the web browser one of the worst platforms imaginable for strong anonymity (or security). Why? Because we also lack a credible alternative. One such alternative could have been the now dead or in limbo [http://syndie.i2p2.de/ Syndie] (&quot;Syndie's design as an anonymity-sensitive client application carefully avoids the intricate data sensitivity problems that nearly every application not built with anonymity in mind does not.&quot;)

In summary: Whonix² needs to consist of at least two very diverse systems, different hardware manufacturers, different kernels, different companies/orgs providing support and offer at least two different anonymizing networks. Bonus points for utilizing diverse crypto systems and cascades. Neither system should &quot;know&quot; both who is communicating and with whom.

= Footer =

[[include ref=WikiFooter]]

