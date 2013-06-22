[[include ref=WikiHeader]]

[TOC]

= On Whonix-Gateway =

To change the '''keyboard layout''' in Whonix-Gateway:

<pre>sudo dpkg-reconfigure console-data

## French keyboards:
## Perhaps an upstream bug.
## ( http://free.nchc.org.tw/clonezilla-live/stable/Known-issues-Clonezilla-live.txt )
## If you are using French Keymap, Remember to use &quot;Select keymap from full list&quot;
## 1. Select keymap from full list
## 2. pc / azerty / French / Same as X11 (latin 9) /Standard

## Does not work in Debian for some reason.
#sudo dpkg-reconfigure keyboard-configuration</pre>
= On Whonix-Workstation =

If you want to change the '''keyboard layout''' from the default &quot;us&quot; to something else:

<pre>KDE -&gt; Start menu button -&gt; Applications -&gt; Settings -&gt; System Settings -&gt;
input devices -&gt; layout -&gt; add yours and remove default one -&gt; apply -&gt; Done.</pre>
Or:

<pre>Start menu button -&gt; search -&gt; keyboard -&gt; layout -&gt; add yours and remove default one</pre>
= Footer =

[[include ref=WikiFooter]]

