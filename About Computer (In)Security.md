[[include ref=WikiHeader]]

[TOC]

# About Computer (In)Security #
A secure and trustworthy computer is a computer that only does what _you_ (think you) tell it to.

Computers are insecure and not trustworthy and there is nothing we can do about that. Computers are "universal machines" (see Von Neumann, Turing). They can be instructed to do anything they can do according to the laws of physic. It's important to understand that a computer can't discern between "good" and "bad" instructions, bits are bits. There are two general problems: 

(1) There are a lot of people who can instruct a given machine to do something (anything!), we need to trust them all, or verify everything, which is impossible

If you read or write all instructions (kernel, software, firmware) yourself, study the hardware design (so you understand what an instruction actually does) and compare that with the actual hardware and then make sure you are the only one who can access the machine and give it new instructions, you need to trust that other people only give the machine instructions to do things that you want it to do. You can tell it to accept other, external untrusted instructions in a restricted, controlled fashion (like "render that html but other wise don't touch my system") but this is next to impossible to do reliably because of point 2). Otherwise you could never connect that machine to a network or transfer any input from another system to it ("input" and "instructions" has to be understood in a very broad sense, it's not just about executable code, it can as well be media files or hardware devices that are being attached).

The "Trusted Computing Base" (TCB) refers to all instructions and hardware used to restrict a "universal machine" from accepting and acting on (other) arbitrary instructions. It is used to set a certain security policy to enforce that a computer only does what these trusted instructions allow it to. "Trusted" simply means that we have to trust it, not that it's wise to trust it. The TCB tries to restrict what instructions can do but it consists of instructions itself. It can't restrict or police itself. Any flaw whatsoever in the TCB directly results in a compromise of the security of the system.

(2) The machines themselves and the instructions are incredibly complex

Even in an ideal world with mathematically verified hardware and software we may think we are giving instructions to do A while in reality the instructions tell it to do B, or also B. Machines can not make "mistakes" but they certainly can do unexpected things...  

We can't give machines instructions in our language (programming language) it needs to be in machine code. The translation is so complex that we need another machine to do that for us, and to create that machine another was used and so on. This expands our chain of trust to basically all machines and humans involved to the first compiler created by an assembler which in turn was created by hand-written machine code.

Hardware is fallible, hardware failure can result in entirely unpredictable results. Cosmic rays "flipping a bit" or just bad memory and extreme temperatures? Look up "Bit-squatting" for an example. Software depends on the hardware to function perfectly, what happens if the most basic assumptions are betrayed? 

Another example for complexity, side channel attacks: they are very difficult to protect against and poorly understood by most software developers. E.g. through power or CPU load analysis otherwise isolated parts outside the TCB can influence or eavesdrop on privileged encryption. In other words, determining what is part of the TCB and what is definitely not, is a very hard problem.

If that wasn't enough we also have the problem that circuit layouts, microcode and firmware of most vendors is proprietary. Part because of competition concerns, part because they are afraid of patents... In any case, this makes verification even more difficult that it already is. Further "hardware" (which includes firmware, i.e. software) is becoming more and more capable (#complex and dangerous). Features like Trusted Computing when used to prevent ring 0 access from the user and owner of the computer, EFI that has Internet connectivity and can update itself or Intel RMM which can grant remote access that is invisible to the user and OS combined with a less than perfect track record (e.g. see Intel related research by Invisible Things Lab) doesn't exactly spell trustworthy and 100% dependable.

Conclusion:
The TCB can never really be trustworthy. The source code of every currently usable OS kernel alone is too complex and large to completely audit and make error free, not just for a single human but even for large groups like the "Linux community". But let's assume we solve that (e.g. through using microkernels and formal verification): How do you make sure compiled binaries are actually doing what the source intended? Or, how can you verify that complex hardware and integrated circuits are actually built according to their intended design? For all the verification and auditing processes we are dependent on other complex computer systems that would have to be trusted unconditionally. Bootstrapping trust is a chicken and egg problem. We would have to be able to verify systems with just looking at them with our bare eyes and hands or build/verify all systems necessary to bootstrap a modern compiler and hardware development platform. This may have been possible for the first "computers" in the first half of the last century but not anymore.

Since there's nothing we can do about that, what else can we do then?

We need to design our systems in a way that makes it no longer necessary to trust them 100%. We only need to trust that it's good enough and that it's astronomically unlikely that multiple diverse systems are untrustworthy in the same way.

If you don't want a computer to be able to tell anyone your location or identity better make sure the computer doesn't know either... The Whonix security design in some ways mimics the security design of the Tor network itself: Don't trust any single entity to be trustworthy. We only rely on the fact that it's unlikely that all entities (nodes, computers) are compromised and colluding. To be precise, that's a goal that isn't achieved yet with Whonix alone, see [Whonix²](https://sourceforge.net/p/whonix/wiki/Security/#whonix2). One could also say that the actual TCB of such a "system" (actually multiple systems) becomes the design, arrangement and usage policy which is very well possible for every user to comprehend and verify.

This could be compared to the "Air Gap" used on most high security networks. They assume that the TCBs are not trustworthy and work around that using a simple and easily verifiable policy that basically eliminates the complete attack surface or hardware and software bugs and even protects against most backdoors (for example, a subverted PRNG could still result in weak crypto being exported from the trusted network where it can be recorded and "cracked" by an adversary. A strong pyhiscal isolation based system could then encrypt data twice on different systems using different PRNG implementations to protect against such attacks.)

Physical Isolation in the sense of Whonix is not a new idea, see [Verifiable Computer Security and Hardware: Issues by William D. Young. September 1991 (PDF!)](http://www.cs.utexas.edu/ftp/boyer/cli-reports/070.pdf) page 18 for a summary. It seems like the idea was rediscovered by Whonix (independently, and we came up with the same term), to our knowledge Whonix is currently the only project following this approach in a defined way.

# Footer #
[[include ref=WikiFooter]]