[[include ref=WikiHeader]]

[TOC]

# Branches #
## Introduction ##

While the project is small adrelanos thinks it's best not to make a too difficult policy.

## master ##

* Nothing much.
* No code.
* Just the branching model, project readme, information, gpg...

## stable ##

* last released and recommended Whonix version
* ready to include hotfixes

## development ##

* candidate for next Whonix version
* <s>must always build</s>
* currently restructuring
* we can make an always building development branch as soon as someone else commits code

## untested_adre ##

* <s>Adrelanos's progress of work.</s>
* Does not exist at the moment.
* Not calling it unstable, because the changes will most likely never make it unstable but it's just not tested if it still builds.

## untested_yourname ##

## perhaps 0.5.x etc. as release branches ##

## feature branches when it makes sense ##

## signed git tags ##
Releases will be tagged and gpg signed.

## temporary git tags ##
Will be named like: adretemp1

Can be ignored. They are only internally used by adrelanos to safely transfer code to a build machine.

Can get deleted from time to time.

## Link to Source Code ##
<a href="https://github.com/adrelanos/Whonix"><img style="position: absolute; top: 0; right: 0; border: 0;" src="https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png" alt="Fork me on GitHub"></a>

# subscribe to code changes #
## git ##
Adrelanos always pushes code to both [github](https://github.com/adrelanos/Whonix) and [sf.net](https://sourceforge.net/p/whonix/code/).

A git specific work flow could be:

    git fetch

every (few) day(s) and then git diff(tool), merge, etc.

## Github Commits Mailing List ##
[Whonix-commits read only mailing list](https://lists.sourceforge.net/lists/listinfo/whonix-commits)

## Twitter ##
If you prefer Twitter, use the [Secondary Twitter Account for Source Code Commit Notification](https://twitter.com/WhonixSource).

## Feed notification ##
Feed notification: There is on [sf.net](https://sourceforge.net/p/whonix/code/) git is a [rss] subscribe button: **F**.

# Goodies #
Optional. Just sharing. Like it or not.

* Bash completion can complete git commands and branch names.
* [Colorful git prompt.](http://www.opinionatedprogrammer.com/2011/01/colorful-bash-prompt-reflecting-git-status/)

![](http://www.opinionatedprogrammer.com/post-img/git-prompt-screenshot.png)

# Footer #
[[include ref=WikiFooter]]