[[include ref=WikiHeader]]

[TOC]

= What is Metadata? =

Office documents, pictures, videos and other files contain lots of information in the meta tags that may deanonymize their author. Before uploading them to the Internet you should remove this meta data.

For more information about metadata please read the [https://mat.boum.org/ MAT] website. Information about metadata is also on the [https://sourceforge.net/p/whonix/wiki/Warning/#whonix-doesnt-clear-the-metadata-of-your-documents warning] page.

= Guidelines =

Metadata can not be used to de-anonymization, if you follow the following guidelines:

* Always think twice before uploading anything.
* Upload only files, which you, either:
** created inside your Whonix-Workstation
** downloaded using your Whonix-Workstation
** carefully scrubbed yourself
* For example, if you want to upload photos or videos, unless you know what you are doing, get an extra device, which you only use for anonymous usage.
* Keep in mind, that even if de-anonymization is not possible, that still identity correlation to the same pseudonym might happen. For example, let's suppose your created a video using any video creation software and you uploaded it to a popular video portal under the pseudonym A. Then you create a another video using the same machine (and same application) and upload it under the pseudonym B. An adversary checking the metadata could correlate pseudonym A with pseudonym B.
* Look into [https://mat.boum.org/ MAT] (Metadata Anonymisation Toolkit). Preinstalled on Whonix.

= MAT - Metadata Anonymisation Toolkit =

Start graphical user interface from start menu:

<pre>Start menu button -&gt; Applications -&gt; Utilities -&gt; Metadata Anonymisation Toolkit</pre>
Or the command line interface:

<pre>mat
# or for gui
mat-gui</pre>
[[Image:http://whonix.sourceforge.net/screenshots/mat.png|frame|none]]

<font size="-3">Thanks for the MAT public domain screenshot to [https://www.awxcnx.de/handbuch_43.htm awxcnx.de].</font>

Add the files you want to clean to list. If the state was &quot;dirty&quot; you can clean it. The cleaned files are stores in the same directory like the original files with an an extension &quot;.cleaned&quot; in the name.

= License =

Thanks to [https://anonymous-proxy-servers.net/ JonDos] ([https://anonymous-proxy-servers.net/forum/viewtopic.php?p=31220&sid=ac8a6ca16eb768b3322be30b20375c97#p31220 Permission]). The Metadata page contains content from the JonDonym documentation [https://anonymous-proxy-servers.net/en/help-live-cd/jondo-live-cd9.html Anonymizing Documents and Pictures] page.

= Footer =

[[include ref=WikiFooter]]

