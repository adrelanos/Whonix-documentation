[[include ref=WikiHeader]]

**2012-09-10**

Whonix **ALPHA** version **0.4.5** has been released and is ready for testing. Many usability bugs have been fixed. Security was further and slightly improved. Since it's an alpha version, there can be further unknown bugs. Known bugs are on the [Download] page. Changelog: [Changelog] Release announcement: [tor-talk Mailing List](https://lists.torproject.org/pipermail/tor-talk/2012-October/025921.html); [Debian Derivatives Mailing List](http://lists.debian.org/debian-derivatives/2012/10/msg00007.html); [Whonix Devel Mailing List](http://sourceforge.net/mailarchive/forum.php?forum_name=whonix-devel)

**2012-28-09**

Whonix **ALPHA** version **0.4.4** has been released and is ready for testing. There some usability bugs inside, but workarounds are available in this readme. Since it's an alpha version, there can be further unknown bugs.

I did not want to delay this release any further. The mess with multiple project names and websites had to come to an end. I've seen people loosing interest in open source projects, because there was no visible progress. This is no vaporware. Changelog: [Changelog]

**2012-09-05**

^1^ A bug in Whonix 0.2.1 when trying to update Tor has been [reported](https://sourceforge.net/p/torbox/discussion/general/thread/e938932d/). The bug has been confirmed by Whonix developer adrelanos. Thanks to the anonymous user for reporting the bug and for testing the workaround! You can find the workaround in the Readme under [Readme#UpdatingTor](https://sourceforge.net/p/whonix/wiki/Readme/#updating-tor).

^2^ I am still having problems with the new webhost. Aos development made steady progress (see in [git](https://github.com/adrelanos/Whonix) if you are interested). The project is still very active and I am still interested and going to develop it further. One the webhost problem has been fixed, the 0.3.0 will be released.

**2012-07-17**

^1^ Rebranding. **aos** is the new project name. The process of rebranding is ongoing. Also all links have to be renamed. That will be done as soon as a new home for Whonix has been found. 

^2^ A Whonix (previously called Whonix) source code 0.2.1 is now on [github](https://github.com/adrelanos/Whonix). The source code will be polished so it will be easier to understand, maintain and contribute.

**2012-07-16**

^1^ Whonix 0.2.1 has been released. It's Alpha quality software. There were no testers beside **proper**. You can download it. While this release contains many security enhancements, new minor usability bugs have been introduced. See [Changelog](https://sourceforge.net/p/whonix/wiki/Changelog) for a comprehensive list of changes and known issues. **adrelanos** decided to release this even with the minor bugs since the security improvements are important. 
^2^ The gnome-terminal has a minor bug, at startup the it's black on black, therefor you can't see anything. Simply change the colors manually. 

^3^ **proper** has a new pseudonym, **adrelanos**. 

^4^ Due to [trademark issues](https://www.torproject.org/docs/trademark-faq.html.en), Whonix must be rebranded. Whonix needs a new name, and a new home, a new website. Stay tuned for updates. 

**2012-07-14**

Whonix 0.2.1 will come out soon. Before officially releasing it, I'd like to have a few testers. If you are interested, please contact adrelanos a-t riseup do-t net.

**2012-06-14**

A bad news and a good news. 
^1^ Unfortunately, the upcoming download version, Whonix 0.2.0, will not be functional on older hardware with non-PAE CPU's. 

^2^ Fortunately, users with non-PAE CPU's, will still be able to build Whonix 0.2.0 from source. The situation may improve in future. The [FAQ](https://sourceforge.net/p/whonix/wiki/FAQ/) has been updated.

**2012-06-02**

^1^ The latest TorButton update may break Tor Browser within Whonix. We'll post soon an update with a solution. The Readme explains how you can update Tor Browser.

^2^ A bug crashing Whonix has been [reported offsite](http://ra.fnord.at/2011/05/easy-and-secure-anonymous-internet-usage/). It happens when you try to run Whonix on older hardware, which does not support PAE. A new [FAQ entry](https://sourceforge.net/p/whonix/wiki/FAQ/#whonix-crashes-because-of-pae) with a interim solution has been posted. The bug will be fixed in Whonix 0.2.0. UPDATE: Unfortunately will only partially fixed, see news above. 

**2012-05-29**

^1^ The New Identity button of Tor Button in Tor Browser with Whonix is defunct. See [Whonix/ApplicationWarningsAndNotes#TorBrowser](https://sourceforge.net/p/whonix/wiki/Applications/#tor-browser) for an explanation why, what the New Identity button does and for a workaround.

**2012-05-21**

^1^ New article: All about [Browser Plugins](https://sourceforge.net/p/whonix/wiki/Applications/#browser-plugins) (such as Flash) in conjunction with Whonix.

**2012-04-25**

^1^ New optional feature. You can use a Secondary DNS resolver (Optional Feature).

**2012-04-24**

^1^ New optional feature. There is now a limited workaround for Tunneling UDP over Tor using VPNs.

**2012-04-10**

We have a bunch of new/updated articles/stuff. Here is a selection. 
^1^ new: Rudimentary Whonix Support for Other Anonymizing Networks. (People who are only interested in Tor, do not have to read.)

^2^ updated: Whonix/SecurityAndHardening.

^3^ new: Whonix/Trust.

^4^ updated: Tunneling Proxy/SSH/VPN through Tor (Tor -> Proxy/SSH/VPN).

^5^ new: A Free example VPN working with Whonix for testing purposes.

^6^ new: Tunneling UDP over Tor (Update: see news)

^7^ Optional new feature: Hide your Whonix usage / Torify the Whonix-Gateway

^8^ Dev only: Hardened Gentoo based Whonix-Gateway

**2012-04-02**

^1^ **Critical issue** with /var/lib/tor for all users who downloaded the Whonix Download Binary images 0.1.3. 
Users who manually configured Whonix or used build from source are not affected. 

On your Whonix-Gateway. 
1. If you were using hidden services, backup your keys (/var/lib/tor/hidden_service/). 
2. Execute the following:

    sudo -i 
    service tor stop
    rm -r /var/lib/tor/*
    service tor start
    exit


This will delete the content of the Tor data directory /var/lib/tor. Technical background: the Tor consensus and your [https://www.torproject.org/docs/faq.html.en#EntryGuards entry guards] are stored there. These should not be shared along all Whonix users.

**2012-03-25**

^1^ Binary images for Whonix 0.1.3 are now available! These are affected by the critical issue above.

**2012-03-24**

^1^ All users should update to 0.1.3! 
Users of Whonix 0.1.* can update using the update script. Users of Whonix versions prior the introduction of version numbers should reinstall following our build instructions or Physical Isolation instructions. Update: or download the latest ready-made images.

**2012-03-22**

^1^ Whonix has now a logo. Thanks to XJ!

**2012-03-06**

^1^ Identity correlation through circuit sharing (Update: This is now closed, there is nothing we can do about till the current alpha version of Tor becomes stable; Update 2: Whonix is already working with the current Tor alpha and prepared for the next Tor stable, see Whonix-Gateway.sh.)

**2012-03-03**

^1^ Alpha builds available at http://sourceforge.net/projects/torbox/files/

**2012-02-16**

^1^ This is resolved in the latest version of Whonix. Resolved in Whonix 0.1.3 and above. Only important prior Whonix 0.1.3.
It would be prudent if all Whonix users would use the same time zone, as some applications do leak it, this hasn't been advised earlier. Do this on your Whonix-Workstation and on your Whonix-Gateway. Type in console

    sudo dpkg-reconfigure tzdata

then choose etc (at the bottom) and then choose UTC.  

^2^ new: Hosting hidden services

**2012-01-11**

^1^ Project started. [Historical very first version](https://trac.torproject.org/projects/tor/wiki/doc/TorBOX?version=1).

# Footer #
[[include ref=WikiFooter]]