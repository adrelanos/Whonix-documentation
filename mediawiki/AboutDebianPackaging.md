[[include ref=WikiHeader]]

[TOC]

= About Debian Packaging =

debian/control: There are separate meta packages for dependencies and recommend packages.

If we used the Recommends field for Whonix meta packages (those who pull the required Debian upstream packages for creating Whonix), we could not install them using apt-get with --install-recommends, which is apt-get's default option, because that would also install packages recommend by any dependency we install.

On the other hand, if we installed using apt-get --no-install-recommends, the packages Whonix's meta packages recommends, will not get installed.

Therefore splitting them, appeared to be the only solution. Otherwise it would install packages such as virtuoso, soprano and vlc, which are not useful '''in context of''' Whonix-Gateway.

= Footer =

[[include ref=WikiFooter]]

