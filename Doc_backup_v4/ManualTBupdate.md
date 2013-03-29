[[include ref=WikiHeader]]

[TOC]

# Manually updating Tor Browser #
## Updating ##
(1) Go to https://www.torproject.org/ and/or http://idnxcnkne4qt76tg.onion/ and download the Tor Browser Bundle for Linux 32 bit. Store it in */home/user/*.

(2) Read https://www.torproject.org/docs/verifying-signatures.html.en and/or http://idnxcnkne4qt76tg.onion/docs/verifying-signatures.html.en and learn about gpg verification.

(3) Go to https://www.torproject.org/docs/signing-keys.html.en and/or http://idnxcnkne4qt76tg.onion/docs/signing-keys.html.en to get the gpg keys.

(4) Verify the Tor Browser Bundle download.

(5) Go into */home/user/* with the file manger. (Dolphin)

(6) Extract the Tor Browser Bundle. Right click on the downloaded archive -> extract -> extract archive here.

(7) In case you downloaded another version than *en-US*, rename the tor-browser_*lang* folder to *tor-browser_en-US*. This is important, because the paths in the following script are hardcoded.

(8) Go into the */home/user/tor-browser_en-US* folder.

(9) Delete *start-tor-browser* or move it to the */home/user/tor-browser_en-US/Docs* folder.

(10) Create a new file within the */home/user/tor-browser_en-US/* folder called *start-tor-browser* with the following content.

<pre>
    #!/bin/bash
    ## Whonix Tor Browser start script
    
    cd ~
    ~/tor-browser_en-US/App/Firefox/firefox --profile ~/tor-browser_en-US/Data/profile
    
    ## End of Whonix Tor Browser start script
</pre>

(11) Make the *start-tor-browser* script executable. Right click on *start-tor-browser* -> Properties -> Permissions -> enable the *Is executable* box -> ok.

(12) Go to */home/user/tor-browser_en-US/Data/profile/* and create a file *user.js* with the following content.

    ## Begin of patched user.js.

    ## If you edit this file while Firefox is running, your changes will be
    ## overwritten, when you close Firefox.

    ## How to create the user.js network settings:
    ## 1. Make a backup of prefs.js.
    ## 1. Start Tor Browser with the patched start script.
    ## 2. Apply proxy settings using the Tor Button settings dialog..
    ## 3. Make a diff from the old and the new pref.js.
    ## 4. Copy the relevant changes to user.js.
    
    ## network settings
    ## (Are now set in /etc/environment - or not...)
    ## (See /etc/environment.)
    user_pref("extensions.torbutton.use_privoxy", false);
    user_pref("extensions.torbutton.settings_method", "custom");
    user_pref("extensions.torbutton.socks_host", "192.168.0.10");
    user_pref("extensions.torbutton.socks_port", 9100);
    user_pref("network.proxy.socks", "192.168.0.10");
    user_pref("network.proxy.socks_port", 9100);
    user_pref("extensions.torbutton.custom.socks_host", "192.168.0.10");
    user_pref("extensions.torbutton.custom.socks_port", 9100);

    ## End of Whonix user.js.

(13) If you want to make 100% sure you never have Tor over Tor, you must shut down Whonix-Gateway while doing the following tests.

(14) If there is **no** green Vidalia icon in the task bar, everything is fine.

(15) Start Tor Browser and run

    ps aux | grep tor

If you see something like.

    109 /usr/sbin/tor

Or.

    /home/user/my_tor-browser_en-US/App/tor

Something went wrong and you're running Tor over Tor, which is recommend against.

(16) If the tests results are as expected, everything went fine.

(17) Don't forget to restart Whonix-Gateway, if you shut it down in step (13).

(18) Done.

# General information about Tor Browser in Whonix #
See [Tor Browser](https://sourceforge.net/p/whonix/wiki/TorBrowser/).

# Footer #
[[include ref=WikiFooter]]