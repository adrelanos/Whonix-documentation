[[include ref=WikiHeader]]

[TOC]

# Redistribution

See [Release Folder](https://github.com/adrelanos/Whonix/tree/development/release) in Whonix source code.

* Don't forget to update Whonix version number.
* [LeakTests]!
* [Test] the images before release! TODO: Needs big revision with all Whonix features.
* See if [Documentation] still makes sense.
* Update the [Changelog].
* See https://github.com/adrelanos/Whonix/blob/development/release/whonix_release

* Source Code

Whonix-Gateway

    sudo ./debug-steps/download-source -tg

Whonix-Workstation

    sudo ./debug-steps/download-source -tw

Compress. Upload.

* Upload the images.
* At least a few testers should test before posting a news. Testers may be found by posting a news.
* Check, if [ManualTBupdate] is still up to date.
* Update [Download].

* Only next version: Update gpg verification instructions. (Change from .sig to .asc.)
* Only next version: chmod -x / +x no longer required for [BrowserPlugins] and [Dev_Flashtutorial].
* Only next version: [whonixcheck]

* Only next version: chmod -x / +x update [Tunnel_Proxy_or_SSH_or_VPN_through_Tor]
* Update [Stream Isolation] chmod -x / +x no longer recommend, use /etc/whonix.d instead


* Update [PhysicalIsolation].
* Update [BuildDocumentation].
* Update [Features].
* Update [sf.net project page](http://sourceforge.net/projects/whonix/).
* Update sf.net default download.
* New documentation from [Next].
* Finally announce: Post a news.

    * In Whonix Important and Feature Blog.

    * http://lists.debian.org/debian-derivatives/
        * debian-derivatives@lists.debian.org

    * https://lists.torproject.org/pipermail/tor-talk/
        * tor-talk@lists.torproject.org

    * https://lists.sourceforge.net/lists/listinfo/whonix-devel
        * whonix-devel@lists.sourceforge.net

    * full-disclosure@lists.grok.org.uk

    * https://mailman.stanford.edu/mailman/listinfo/liberationtech
        * liberationtech@lists.stanford.edu

# Footer #
[[include ref=WikiFooter]]