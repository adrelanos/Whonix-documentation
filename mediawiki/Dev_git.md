[[include ref=WikiHeader]]

[TOC]

= Branches =

== Introduction ==

While the project is small adrelanos thinks it's best not to make a too difficult policy.

== master ==

* <s>Adrelanos's progress of work.</s>
* Does not exist at the moment.
* Not calling it unstable, because the changes will most likely never make it unstable but it's just not tested if it still builds.
* Branching model, project readme, information, gpg...

== stable ==

* last released and recommended Whonix version
* ready to include hotfixes

== development ==

* candidate for next Whonix version
* <s>must always build</s>
* currently restructuring
* we can make an always building development branch as soon as someone else commits code

== untested_adre ==

== untested_yourname ==

== perhaps 0.5.x etc. as release branches ==

== feature branches when it makes sense ==

== signed git tags ==

Releases will be tagged and gpg signed.

== temporary git tags ==

Will be named like: adretemp1

Can be ignored. They are only internally used by adrelanos to safely transfer code to a build machine.

Can get deleted from time to time.

== Link to Source Code ==

<a href="https://github.com/adrelanos/Whonix"><img style="position: absolute; top: 0; right: 0; border: 0;" src="https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png" alt="Fork me on GitHub"></a>

= subscribe to code changes =

== git ==

Adrelanos always pushes code to both [https://github.com/adrelanos/Whonix github] and [https://sourceforge.net/p/whonix/code/ sf.net].

A git specific work flow could be:

<pre>git fetch</pre>
every (few) day(s) and then git diff(tool), merge, etc.

== Github Commits Mailing List ==

[https://lists.sourceforge.net/lists/listinfo/whonix-commits Whonix-commits read only mailing list]

== Twitter ==

If you prefer Twitter, use the [https://twitter.com/WhonixSource Secondary Twitter Account for Source Code Commit Notification].

== Feed notification ==

Feed notification: There is on [https://sourceforge.net/p/whonix/code/ sf.net] git is a [rss] subscribe button: '''F'''.

= Goodies =

Optional. Just sharing. Like it or not.

* Bash completion can complete git commands and branch names.
* [http://www.opinionatedprogrammer.com/2011/01/colorful-bash-prompt-reflecting-git-status/ Colorful git prompt.]

[[Image:http://www.opinionatedprogrammer.com/post-img/git-prompt-screenshot.png|frame|none]]

= Footer =

[[include ref=WikiFooter]]

