# Stuff that doesn't fit... #
this is only temporary anyway, till we get a real bug tracker.

## Problem getting software form Tails [SOLVED] ##
* (adrelanos) Following Tails is also very hard. I though about grabbing tails_htp. They have a git but that's [https://mailman.boum.org/pipermail/tails-dev/2012-June/001252.html not protected by SSL or SSH]. Only way to safely extract something out Tails is downloading the iso, verifying the iso, unpacking squashfs (btw: "sudo unsquashfs -x -dest /home/user/tails filesystem.squashfs" and grabbing it from there. They also don't have an apt repository yet and they are also not like upstreaming all their work.
* (anonymous) but they say git is signed, what's the problem? https://mailman.boum.org/pipermail/tails-dev/2012-June/001254.html  
 * (adrelanos) Do you know how to verify it? I haven't found out.
  * (anonymous) git tag -v; commits after the last signed tag are not to be trusted. There are tons of git tutorials and guides.
  * (adrelanos) I was on the wrong path, understood "only the download iso is signed". "git tag -v 0.12" worked for me.
* (adrelanos) I'd also like to extract torsocks/libtorsocks from Tails, because they fixed the "The symbol res_query() was not found in any shared library. The error reported was: not found!" bug. Perhaps that's not necessary and we can use the Debian package, if they fixed that upstream.

## [MISC] Ubuntu server 64-bit [ANSWERED] ##
* (adrelanos) Any objections using Ubuntu server 64-bit as T-W's operating system? At least for private builds? What I see so far: fingerprinting issues, the exit node and mirror can guess, that someone uses Whonix with 64-bit instant of 32-bit. Since the streams are now separated, I see no big issue with that. Anything else? As long as we have PAE as requirement, we could also switch to 64-bit? Do all PAE-featured CPU's also support 64-bit?
* (anonymous) I don't know. AMD64 is older than PAE. However, 32bit software runs without problems on 32bit and 64bit hosts, 64bit software no so much. Because we generally don't control what host OS people use I chose to base Whonix on 32bit. Vbox does support that mode for some time but I assumed that there are performance implications. Secondly 64bit software needs more RAM, we already run 3 OS (or more) on a system which eat RAM, better minimize that (KVM and other solutions improve RAM usage through page sharing or what it's called, VBox doesn't). Thirdly, according to Brad Spengler and/or PAX team amd64 is a brain dead instruction set and actually worse than x86, despite the large address space making ASLR more effective. They recommended to use grsec on x86 and I hope we can switch to a grsec kernel (wheezy has one, let's see if they maintain it).
* (adrelanos) Moved to faq https://trac.torproject.org/projects/tor/wiki/doc/Whonix/FAQ#Whydoyouusethe32bitoperatingsystemnot64bit

## [0.2] [MISC] [WEBSITE] Not affiliated with torproject notice [DONE] ##
* (adrelanos) Important link: [https://www.torproject.org/docs/trademark-faq.html.en tpo trademark faq]. Less important link about being [https://trac.torproject.org/projects/tor/ticket/2474 experimental software]].
* (adrelanos) I've been in e-mail contact with tpo and I wish I could publish the few mails, but I can not. My questions, if we can discuss it in public or if I can can publish the mails, remained unanswered. I don't want to publish them anyway, because I don't want to challenge them. This is also why I added a second sentence to the Whonix homepage root.
{{{
Whonix is a non-offical, community project. We are not affiliated with torproject.org. The Tor developers are not responsible for this project. See Disclaimer for more information.

Whonix is produced independently from the Tor® anonymity software and carries no guarantee from The Tor Project about quality, suitability or anything else. 
}}}
* (adrelanos) Also with Whonix 0.1.3 it happened, that people mirrored Whonix and offered it for download from their site without linking to our homepage. People might use Whonix without ever reading the notice. We**must** make it**absolutely** clear for anyone, that Whonix is not torproject.
* (adrelanos) For the (trademarkdomain user disappeared) website it might be best to add the non-affiliated-with-tpo notice to root page and to all sub pages. (People on forums/blog/etc. enjoy posting deep links.)
* (adrelanos) Here is my proposal for the Whonix message on Whonix-Gateway.
{{{
# Whonix help/welcome message
cp /home/$USERNAME/.bashrc.backup /home/$USERNAME/.bashrc
echo \
'echo "Welcome to Whonix Tor-Gateway Version $TORBOX_VERSION!"
echo "Whonix is a non-offical, community project. We are not affiliated with torproject.org. The Tor developers are not responsible for this project. See Disclaimer for more information."
echo "Whonix is produced independently from the Tor® anonymity software and carries no guarantee from The Tor Project about quality, suitability or anything else."
echo "Whonix is based on Tor."
echo "Whonix is experimental software by means of concept and design. Do not rely on it for strong anonymity."
echo "Type: "torbox" <enter> for help."
' | sudo -u $USERNAME tee -a /home/$USERNAME/.bashrc
}}}
* (adrelanos) For Whonix-Workstation I propose to add this notice to our torcheck script.
* (trademarkdomain user disappeared) All looks good to me. Will do on (trademarkdomain user disappeared) website.
 * (adrelanos) I think it were best if this notice must only be changed once (variable) and effects changing it on all sub pages. Only admins may change it.
   * (trademarkdomain user disappeared) Definitely. Good idea... I'm working on implementing only one HTML/CSS template source anyway, since I hate to have to manage & modify several template versions. But for even easier updating of text blurbs like this, I can put this in the database. Abstracting it out of the HTML into the database might be done upfront at launch or a bit later, depending upon time & launch motivation. Easily doable though.
* (adrelanos) Ok, not the most pretty solution, not the best places, but should be okay. Open for suggestions.

## [MISC] better Marketing [DONE] ##
* (adrelanos) Currently the main page is way too geeky, scary and complicated. I appreciate being upfront about security and other issues but we should perhaps orientate more on front pages of successful projects, such as Tor and Tails. Successful in having lots of developers, users, supporters and progress. Without having users the most promising implementation is not very useful or secure. Users attract interest, more user, more reviewers, devs and so on. Of course, we will always be upfront with the interested ones about open issues, but that are the ones who click to a sub page and who read the full documentation. When you look at the torproject.org you also won't see a "Uh, we actually have no defense against traffic confirmation, internet exchange point spying, don't pin SSL certificates, have no deterministic builds, no apparmor and a huge amount of other critical issues". It's a fact that most users don't read documentation. I'll aim to make offer a project which provides them with as much as security then possible, at very least more security than the Tor Browser Bundle. The interested ones and those who really care will always be very welcome and they will be offered additional information on how they can get best safety. And when they learned everything they may help us to improve the project even further (use multiple vm's/snampshots, physical isolation, etc.).
* (adrelanos) I plan to make big changes, a rewrite to the Whonix front page. News and You Can Help will be moved to the Readme.