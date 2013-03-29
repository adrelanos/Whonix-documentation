[[include ref=WikiHeader]]

[TOC]

# Single vs Double Click #
KDE uses single click instead of double click by default. If you want to change that to double click:

    KDE -> Start menu button -> Applications -> Settings -> System Settings ->
    input devices -> mouse -> double click -> apply - Done.

# Use full-screen #
It's advised to work in full-screen. This feature is also inherited from Virtual Box. Press your host key ^2^ and press F. That will activate full-screen. You end up with Whonix (and Debian) default resolution and color depth 1024x768x24. ^1^ To disable it the same key combination can be used.

<font size="-3">
,,
^1^ As per [Whonix's Protocol-Leak-Protection and Fingerprinting-Protection](https://sourceforge.net/p/whonix/wiki/Security/#whonixs-protocol-leak-protection-and-fingerprinting-protection).
^2^ Virtual Box -> Global Settings -> Input -> Host Key. You can also see the current Host Key in the bottom right corner of Virtual Box.
</font>

# Virtual Consoles #
This feature is inherited from Debian GNU/Linux and Virtual Box. It's noted in Readme because not many people are aware of it. The Debian (not Whonix) feature is to press alt + crtl + F1 or F2, F3, etc. for additional text consoles or F7 for graphical console. Because Debian already registered alt + ctrl keys. Instant of alt + ctrl, use the Virtual Box Host Key. (^2^ above) That means, use Host Key + F1, F2, F7, etc. to do the same inside Virtual Box.

# Shut down the Whonix-Gateway #
To **shut down** the gateway simply enter

    sudo poweroff

# Footer #
[[include ref=WikiFooter]]