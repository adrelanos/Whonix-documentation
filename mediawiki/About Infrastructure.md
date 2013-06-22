[[include ref=WikiHeader]]

[TOC]

= Current Situation =

== Introduction ==

Currently Whonix is hosted on sourceforge.net. This page talks about Whonix online hosting and (non-existing) testing infrastructure.

== About sourceforge.net ==

The wiki, forum, the mailing list and download mirrors provided by sf.net provides unlimited traffic, which is very good.

The forum provided by sourceforge.net is currently not very well suited for Whonix. Most users are expected to post to the forums over Tor. sourceforge.net doesn't handle changing IP's very well. Registered users often have to post twice until their message gets stored. And if they haven't stored their draft beforehand it's lost, which is really annoying. Good points are, that the forum is viewable over SSL, but only for registered users. Let's say they could store a message, then it's still confusing because the message has to be manually moderated due to automatic spam scripts targeting Whonix forum.

The wiki is unfortunately not viewable over SSL, which is very bad.

sf.net generally provides two different categories of hosting. [http://sourceforge.net/p/allura/ Allura] with &quot;some&quot; SSL, i.e. the wiki, forum, mailing list, download mirrors on the other hand [http://sourceforge.net/apps/trac/sourceforge/wiki/Project%20web%20and%20developer%20web%20platform project web].

Project web (no SSL) has somewhat low limited traffic, but according to their support will be manually increased.

One of the major issues with sf.net is, that is does not support SSL everywhere. The [Contribute] page contains a [https://sourceforge.net/p/whonix/wiki/Contribute/#vote-ideas Vote] chapter and one of the votes users are encouraged to, is [http://sourceforge.net/apps/ideatorrent/sourceforge/ideatorrent/idea/721/ Idea #721: Allow SSL for SourceForge pages whenever possible]. Unfortunately, very few users are voting.

A very strong point for sf.net is, that big files (virtual machine images) and unlimited traffic is allowed. Another strong one of course is, that sf.net allows Whonix to be hosted on sf.net.

Other severe usability bugs:

* [https://sourceforge.net/p/allura/tickets/5661/ Improve Support for Tor Browser; option to disable IP check]
* [https://sourceforge.net/p/allura/tickets/5662/ Prevent drafts from getting lost]
* [https://sourceforge.net/p/allura/tickets/6207/ Long content pages broken]

== Bug / Feature Request Tracker ==

Now hosted on github: https://github.com/Whonix/Whonix/issues

A bit suboptimal, since people have to create a second account just for github and it probable won't scale well enough in long term. Positive points are, that it works for many big projects such as Bitcoin and attracts a lot pull requests (for them). So lets see how that works.

== Conclusion ==

In summary there where no open source hosting sites, which offer SSL everywhere and unlimited download of big files. An open source hosting facility providing free webspace and SSL everywhere would be much desirable, but doesn't exist. Since there is no founding and no webmaster, the decision was made to host the project on sf.net for now.

It would still be desirable to find better hosting. See Requirements for Good Hosting and Ideal Hosting below.

== Testing infrastructure ==

Whonix is neither Microsoft with Windows nor Canonical with Ubuntu or similar. At the moment there is only one Whonix developer.

Testing infrastructure is limited to adrelanos's hardware. There is no big test laboratory, where Whonix could be tested on a variety of different machines and systems. Probable due to the web infrastructure being quite limited (not encouraging people to register and volunteer enough) and the project being quite young (since 2012), there are very few testers. On the other hand the project has no founding and no webmaster for self-hosting. Some people anonymously post comments, but due to not having a pseudonym (account name) this has limited reputation.

Let's see what happens when adrelanos calls for testing the next Whonix release.

= Future =

== Requirements for Good Hosting ==

=== Requirements ===

* Some webspace and sufficient traffic.
* Needs a wiki, a forum, a blog, a mailing list.
* We can either use free project hosting or own hosting.
* Tor friendly.
* No tracking scripts. (Google analytics etc.)
* Permit to sign up and to use the page exclusively over Tor.
* A wiki on that site (media wiki). (And spoilers.) (And flagged revisions.)
* A free SSL certificate.
* All parts off the website reachable over SSL without any warnings.
** sourceforge.net does not offer that (SSL warnings).
** startssl.com offers free SSL certificates. You simply have to prove, that you have control over the domain - but that's not possible with subdomains.
* Hosting and domain.
** Censor resistant in sense of &quot;Whonix will not get deleted.&quot;
** Free - if that is possible. No one is willing to pay and in the beginning there are no donations.
* We allow guest/anonymous postings (bug report, feedback, etc.) and moderate it very non-restrictive. (Allow any critique. Only delete off topic talk such as warez.)
** It's still desired to have the less critical parts of the wiki open for guest edits.
** Where no random trolls/crackers can modify anything important.
** A wiki where guest edits are allowed only works when having a feature for [https://en.wikipedia.org/wiki/Flagged_revisions Flagged revisions] Sighted versions, where admins review changes and manually make the edited version the default visible page for everyone. To my knowledge, only mediawiki has such a feature.

=== Answered Questions ===

* Is there a free project hosting fulfilling all requirements?
** Last time checked, no.

=== Open Questions ===

* Q/A forum or ordinary forum?
* Mailing list can stay on sf.net?
* Blog can stay on sf.net? Integration with new website?
* Downloads must most likely stay on sourceforge.net? Because no other hoster allows such big downloads? And other means of downloading (torrent) are more complicated and more difficult to do anonymously (using TBB)?

=== Links, that may be helpful ===

* [https://en.wikipedia.org/wiki/Comparison_of_open_source_software_hosting_facilities Comparison of open source software hosting facilities]

== Ideal Hosting offers additionally... ==

* We better don't choose something based in non-free countries, such as US.
* Fully accessible by text mode browsers.
* Fully accessible without JavaScript.
* Optionally reachable by a hidden service.

== Reviewed Hosting Services ==

=== sourceforge.net / Google Code ===

Google Code and sf.net, block users from &quot;Cuba, Iran, North Korea, Sudan, Syria&quot;.

=== wikimedia / wikpedia ===

Last time I checked wikipedia (wikimedia) derivatives and wikia weren't Tor friendly.

=== savannah ===

* https://savannah.nongnu.org (with SSL) looked promising and I don't expect them to be gone soon or to do any other stupid stuff (banning countries etc.). They offer homepages, for example http://www.nongnu.org/qwe/ but I haven't seen subdomains (qwe.nongnu.org) with SSL (for nongnu.org). That's the minimum requirement.

=== github ===

* Already using github as main git repository.
* github.com offers [https://github.com/blog/272-github-pages sub domains], but they are not reachable over SSL. I can't believe, there are no open source project hosting services with web hosting and SSL.
* github triggers [https://trac.torproject.org/projects/tor/ticket/7084 a] [https://trac.torproject.org/projects/tor/ticket/7265 scary], [https://trac.torproject.org/projects/tor/ticket/6253 error] message. After either many pages trigger that error so it doesn't matter any more or until this message gets fixed in Tor Browser, we shouldn't use the github as issue tracker or website to avoid FUD. When that got somehow a non-problem, we could think about using github as issue tracker.
* I haven't found out how to autocreate table of contents using markdown on github, but...
* Github also [https://github.com/github/markup/ supports] mediawiki syntax.
** Seems it automatically creates a table of contents, good!
** Bug: [https://github.com/github/markup/issues/193 Mediawiki Pictures now shown in Github Wiki], unless this bug gets fixed, we could think about using the github source code hosting as website, see [https://github.com/adrelanos/testw/blob/master/README.mediawiki example].
** I haven't found out yet how to use [[include ref=WikiHeader]] for github mediawiki pages. It's an important feature for Whonix pages.
** Looks like mediawiki support is just a gimmick. More advanced formatting like font size, syntax highlighting and so on doesn't work.

=== gitorious ===

* Nice as a git mirror. [https://gitorious.org/whonix/whonix In use] as a git mirror.
* SSL for the whole page including the wiki.
* The wiki supports less features, no html (not that important) and no tables. The side bar takes too much space and leaves too less page for the wiki. The wiki is more suited for smaller documentation but not as a whole website replacement like Whonix needs.

=== self hosted hidden service ===

* I am not willing to do it.

=== free onion hosting service ===

* We could host a website on third party (free) hidden service webspace service.
* Risky, because those services can go away any time without notice.
* Can they handle the load when we release a new version? Not talking about bandwidth. Just about page views.
* Clearnet users could only access them through onion.to and tor2web.
** onion.to has a scary landing page.
** tor2web [https://lists.torproject.org/pipermail/tor-talk/2013-February/027344.html does not yet appear in search engines]
* [http://bj6sy3n7tbt3ot2f.onion OnionHosting]
** Price 5 BTC of &quot;life time&quot;.
** I think it's a legit service. The Administrator is hosting many services in onionland for a long time.
** I don't have 5 BTC to open an account.
* [http://torhostg5s7pa2sn.onion/ torhost]
** I don't know for how long it will stay.
** I [http://p4vm6o4n4hbfqxhy.onion/ have a sponsored account], which has the same features as the fair paid account.

= Footer =

[[include ref=WikiFooter]]

