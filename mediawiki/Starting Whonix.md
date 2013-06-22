[[include ref=WikiHeader]]

[TOC]

= Starting Whonix =

Starting Whonix is simple. Start Virtual Box -&gt; click once on the Whonix-Gateway -&gt; press start. Click once on the Whonix-Workstation -&gt; press start.

If you need more help with starting, there are [http://whonix.sourceforge.net/videos.html Video Tutorials] (which explains installing and starting).

<font size="-3">([http://whonix.sourceforge.net/videos.html#video-help Video Help])</font>

If you still need help, please go to the [https://sourceforge.net/p/whonix/discussion/ User Help Forum].

'''The default user is:''' '''''user'''''

'''The default password is:''' '''''changeme'''''

= Whonix does not start =

== PAE crash ==

If Whonix does not start because PAE is missing: Right Click on Whonix-Gateway -&gt; Settings -&gt; Processor -&gt; Disable the ''Enable PAE/NX'' Box -&gt; OK.

Repeat that for Whonix-Workstation as well.

Read the next chapter Boot Options and use the 486 kernel.

== Other reasons ==

Please have a look at the [Download] page. It contains instructions how to properly download and verify the Whonix virtual machine images. There is also help available in form of screenshot or video instructions.

If you still need help, please go to the [https://sourceforge.net/p/whonix/discussion/ User Help Forum].

= Boot Options =

In the grub boot menu you can choose for two seconds. Two kernels are installed by default.

* The default 686-pae kernel.
* A 486 kernel for compatibility.

'''If Whonix works out of the box, you do not need to change anything''' and you can stick the the default 686-pae kernel.

In case you needed to disable PAE (see chapter above), use the 486 kernel.

= Footer =

[[include ref=WikiFooter]]

