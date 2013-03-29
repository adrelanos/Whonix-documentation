[[include ref=WikiHeader]]

# Draft

(*Start with a freshly and fully usable Whonix-Workstation, which is fully booted up.*)

This video will explain, how you can view flash videos without any DNS leaks and without revealing your IP address or location.

We will use Whonix.

Whonix is an **anonymous**

operating

system.

It is  very important to know, that this video assumes, that you have already installed Whonix and booted into Whonix-Workstation.

If you still need to do that, there are other tutorial videos on that channel on how to download and install Whonix.

Open Tor Browser.

(Wait until check.torproject.org reports "you are using Tor".)

Go to the Whonix homepage.

h t t p : / / whonix  .  s   f  .  net

Look around.

Click on Flash Support.

Scroll down and read that page.

It is about possible alternative to Flash

And goes into details on what level of security and anonymity you are going to get.

It also contains tips on how to improve security and anonymity.

If you are really paranoid or have very high security needs, you shouldn't use Flash at all and stick to the alternatives.

However, we believe, that Whonix is currently your best bet to use Flash while protecting you from DNS leaks,

hiding your location and IP address.

Open a terminal.

Copy or type "sudo chmod -x /usr/local/bin/wget".

This is because of a small bug in uwt,

or if you want so, because of a missing feature in torsocks.

Hopefully in future, this step won't be necessary anymore.

Press enter.

Copy or type "sudo apt-get install flashplugin-nonfree" and press enter.

Copy or type "sudo chmod +x /usr/local/bin/wget",

press enter.

For better privacy,

to delete Flash Cookies,

it is recommend to install a Firefox Add On called BetterPrivacy.

Right click on BetterPrivacy.

Choose

Open Link in a New Tab.

Click.

Check,

that there is a the padlock.

Check, that you are connected to h t t p    **s**    : // addons  .  mozilla  .  org

Click on Add to Firefox.

Click on Allow.

Click on Install Now.

Right click on Tor Button -> Click on Preferences... -> Click on Security Settings -> Click uncheck, "Disable Plugins during Tor usage".

We have to restart Tor Browser.

Close Tor Browser.

(*Wait a few seconds so it's really closed.*)

Restart Tor Browser.

(*Wait until check.torproject.org reports "you are using Tor".*)

Let's test it.

Go to h t t p    **s**    : / / youtube  .  com

Let's click on some random video.

It's working.

(*Right click on Video to show it's really a Flash video. If not, click on some other random recommend video and right click on Video again until you got a Flash (not a html5) one.*)

That's it. Link to Whonix is inside the video description.

# Footer #
[[include ref=WikiFooter]]