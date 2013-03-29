[[include ref=WikiHeader]]

[TOC]

# What is Metadata? #
Office documents, pictures, videos and other files contain lots of information in the meta tags that may deanonymize their author. Before uploading them to the Internet you should remove this meta data.

For more information about metadata please read the [MAT](https://mat.boum.org/) website. Information about metadata is also on the [warning](https://sourceforge.net/p/whonix/wiki/Warning/#whonix-doesnt-clear-the-metadata-of-your-documents) page.

# Guidelines #
Metadata can not be used to de-anonymization, if you follow the following guidelines:

* Always think twice before uploading anything.
* Upload only files, which you, either:
    * created inside your Whonix-Workstation
    * downloaded using your Whonix-Workstation
    * carefully scrubbed yourself
* For example, if you want to upload photos or videos, unless you know what you are doing, get an extra device, which you only use for anonymous usage.
* Keep in mind, that even if de-anonymization is not possible, that still identity correlation to the same pseudonym might happen. For example, let's suppose your created a video using any video creation software and you uploaded it to a popular video portal under the pseudonym A. Then you create a another video using the same machine (and same application) and upload it under the pseudonym B. An adversary checking the metadata could correlate pseudonym A with pseudonym B.
* Look into [MAT](https://mat.boum.org/) (Metadata Anonymisation Toolkit). Preinstalled on Whonix.

# MAT - Metadata Anonymisation Toolkit #
Start graphical user interface from start menu:

    Start menu button -> Applications -> Utilities -> Metadata Anonymisation Toolkit

Or the command line interface:

    mat
    # or for gui
    mat-gui

![](http://whonix.sourceforge.net/screenshots/mat.png)

<font size="-3">Thanks for the MAT public domain screenshot to [awxcnx.de](https://www.awxcnx.de/handbuch_43.htm).</font>

Add the files you want to clean to list. If the state was "dirty" you can clean it. The cleaned files are stores in the same directory like the original files with an an extension ".cleaned" in the name.

# License #
Thanks to [JonDos](https://anonymous-proxy-servers.net/) ([Permission](https://anonymous-proxy-servers.net/forum/viewtopic.php?p=31220&sid=ac8a6ca16eb768b3322be30b20375c97#p31220)). The Metadata page contains content from the JonDonym documentation [Anonymizing Documents and Pictures](https://anonymous-proxy-servers.net/en/help-live-cd/jondo-live-cd9.html) page.

# Footer #
[[include ref=WikiFooter]]