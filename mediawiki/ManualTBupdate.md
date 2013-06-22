[[include ref=WikiHeader]]

[TOC]

= Manually updating Tor Browser =

== Updating ==

# Go to https://www.torproject.org/ and/or http://idnxcnkne4qt76tg.onion/ and download the Tor Browser Bundle for Linux 32 bit. Store it in ''/home/user/''.
# Read https://www.torproject.org/docs/verifying-signatures.html.en and/or http://idnxcnkne4qt76tg.onion/docs/verifying-signatures.html.en and learn about gpg verification.
# Go to https://www.torproject.org/docs/signing-keys.html.en and/or http://idnxcnkne4qt76tg.onion/docs/signing-keys.html.en to get the gpg keys.
# Verify the Tor Browser Bundle download.
# Go into ''/home/user/'' with the file manger. (Dolphin)
# Extract the Tor Browser Bundle. Right click on the downloaded archive -&gt; extract -&gt; extract archive here.
# In case you downloaded another version than ''en-US'', rename the tor-browser_''lang'' folder to ''tor-browser_en-US''. This is important, because the paths in the following script are hardcoded.
# Go into the ''/home/user/tor-browser_en-US'' folder.
# Delete ''start-tor-browser'' or move it to the ''/home/user/tor-browser_en-US/Docs'' folder.
# Create a new file within the ''/home/user/tor-browser_en-US/'' folder called ''start-tor-browser'' with the following content.

<pre>
    #!/bin/bash
    ## Whonix Tor Browser start script
    
    cd ~
    ~/tor-browser_en-US/App/Firefox/firefox --profile ~/tor-browser_en-US/Data/profile
    
    ## End of Whonix Tor Browser start script
</pre>

<ol start="11" style="list-style-type: decimal;">
<li><p>Make the ''start-tor-browser'' script executable. Right click on ''start-tor-browser'' -&gt; Properties -&gt; Permissions -&gt; enable the ''Is executable'' box -&gt; ok.</p></li>
<li><p>Go to ''/home/user/tor-browser_en-US/Data/profile/'' and create a file ''user.js'' with the following content.</p>
== Begin of patched user.js. ==

== If you edit this file while Firefox is running, your changes will be ==

== overwritten, when you close Firefox. ==

== How to create the user.js network settings: ==

== 1. Make a backup of prefs.js. ==

== 1. Start Tor Browser with the patched start script. ==

== 2. Apply proxy settings using the Tor Button settings dialog.. ==

== 3. Make a diff from the old and the new pref.js. ==

== 4. Copy the relevant changes to user.js. ==

== network settings ==

== (Are now set in /etc/environment - or not...) ==

== (See /etc/environment.) ==

<p>user_pref(&quot;extensions.torbutton.use_privoxy&quot;, false); user_pref(&quot;extensions.torbutton.settings_method&quot;, &quot;custom&quot;); user_pref(&quot;extensions.torbutton.socks_host&quot;, &quot;192.168.0.10&quot;); user_pref(&quot;extensions.torbutton.socks_port&quot;, 9100); user_pref(&quot;network.proxy.socks&quot;, &quot;192.168.0.10&quot;); user_pref(&quot;network.proxy.socks_port&quot;, 9100); user_pref(&quot;extensions.torbutton.custom.socks_host&quot;, &quot;192.168.0.10&quot;); user_pref(&quot;extensions.torbutton.custom.socks_port&quot;, 9100);</p>
== End of Whonix user.js. ==
</li>
<li><p>If you want to make 100% sure you never have Tor over Tor, you must shut down Whonix-Gateway while doing the following tests.</p></li>
<li><p>If there is '''no''' green Vidalia icon in the task bar, everything is fine.</p></li>
<li><p>Start Tor Browser and run</p>
<p>ps aux | grep tor</p></li></ol>

If you see something like.

<pre>109 /usr/sbin/tor</pre>
Or.

<pre>/home/user/my_tor-browser_en-US/App/tor</pre>
Something went wrong and you're running Tor over Tor, which is recommend against.

<ol start="16" style="list-style-type: decimal;">
<li><p>If the tests results are as expected, everything went fine.</p></li>
<li><p>Don't forget to restart Whonix-Gateway, if you shut it down in step (13).</p></li>
<li><p>Done.</p></li></ol>

= General information about Tor Browser in Whonix =

See [https://sourceforge.net/p/whonix/wiki/TorBrowser/ Tor Browser].

= Footer =

[[include ref=WikiFooter]]

