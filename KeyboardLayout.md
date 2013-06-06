[[include ref=WikiHeader]]

[TOC]

# On Whonix-Gateway #
To change the **keyboard layout** in Whonix-Gateway:

    sudo dpkg-reconfigure console-data

    ## French keyboards:
    ## Perhaps an upstream bug.
    ## ( http://free.nchc.org.tw/clonezilla-live/stable/Known-issues-Clonezilla-live.txt )
    ## If you are using French Keymap, Remember to use "Select keymap from full list"
    ## 1. Select keymap from full list
    ## 2. pc / azerty / French / Same as X11 (latin 9) /Standard

    ## Does not work in Debian for some reason.
    #sudo dpkg-reconfigure keyboard-configuration
    
# On Whonix-Workstation #
If you want to change the **keyboard layout** from the default "us" to something else:

    KDE -> Start menu button -> Applications -> Settings -> System Settings ->
    input devices -> layout -> add yours and remove default one -> apply -> Done.

Or:

    Start menu button -> search -> keyboard -> layout -> add yours and remove default one

# Footer #
[[include ref=WikiFooter]]