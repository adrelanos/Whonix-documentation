<!--
Copyright:

   Whonix Software wiki page Copyright (C) Amnesia <amnesia at boum dot org>
   Whonix Software wiki page Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
   
   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 3 of the License, or
   (at your option) any later version.
		 
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
	  
   You should have received a copy of the GNU General Public License
   along with this program; if not, write to:

	Free Software Foundation, Inc. 
	51 Franklin St, Fifth Floor
	Boston, MA 02110-1301, USA.

On Debian GNU/Linux systems, the complete text of the GNU General Public
License can be found in the /usr/share/common-licenses' directory.

The complete text of the GNU General Public License can also be found online on gnu.org <https://www.gnu.org/licenses/gpl.html>, in Whonix virtual machine images in /usr/share/common-licenses/GPL-3 file or in Whonix wiki on <https://sourceforge.net/p/whonix/wiki/GPLv3/>.
-->

<!--
The Whonix Software wiki page is forked from the Tails Office suite, Audio, Printing and scanning 

page.

-->

[[include ref=WikiHeader]]

[TOC]

# Anything else #
If you don't like the recommendations here, you can install applications of your choice, see [Install Software](https://sourceforge.net/p/whonix/wiki/).

# Tools #
## Encrypt, decrypt, sign, and verify text using OpenPGP; GnuPG frontend ##
KGpg ([KGpg Homepage](http://utils.kde.org/projects/kgpg/); [KGpg wiki with screenshot](https://en.wikipedia.org/wiki/KGPG)) and GnuPG are pre-installed.

Documentation:

* [GnuPG documentation](http://www.gnupg.org/documentation/)
* [Enigmail documentation](http://www.enigmail.net/documentation/)
* [KDE upstream KGpg documentation](http://docs.kde.org/stable/en/kdeutils/kgpg/using-kgpg.html)
* [openSUSE KGpg documentation](https://doc.opensuse.org/documentation/html/openSUSE_113/opensuse-apps/cha.crypto.html)
* [OpenPGP key distribution strategies](https://sourceforge.net/p/whonix/wiki/OpenPGP/)
* [parcimonie - privacy-friendly helper to refresh a GnuPG keyring](https://gaffer.ptitcanardnoir.org/intrigeri/code/parcimonie/) ([in debian](http://packages.debian.org/wheezy/parcimonie))

## E-Mail ##
See [E-Mail].

## IRC CLient ##
Pre-installed.

See [XChat].

## Media Player ##
[VLC Media Player](http://www.videolan.org/vlc/)

Pre-installed.

Start menu -> Applications -> Media -> VLC Media Player

## Image Viewer
You can install it using Start menu -> Applications -> System -> Terminal.

    sudo apt-get update
    sudo apt-get install gwenview

## Desktop Screenshot Creator ##
[shutter](http://shutter-project.org/); [shutter in wikipedia](https://en.wikipedia.org/wiki/Shutter_%28software%29)

You can install it using Start menu -> Applications -> System -> Terminal.

    sudo apt-get update
    sudo apt-get install shutter

## Desktop Video Recorder ##
[gtk-recordmydesktop Homepage](http://recordmydesktop.sourceforge.net/about.php); [RecordMyDesktop in wikipedia with screenshot](https://en.wikipedia.org/wiki/RecordMyDesktop)

You can install it using Start menu -> Applications -> System -> Terminal.

    sudo apt-get update
    sudo apt-get install gtk-recordmydesktop

## Calculator ##
[KCalc](http://utils.kde.org/projects/kcalc/)

You can install it using Start menu -> Applications -> System -> Terminal.

    sudo apt-get update
    sudo apt-get install kcalc

## Terminal ##
[Konsole Homepage](http://userbase.kde.org/Konsole); [Konsole in wikipedia](https://en.wikipedia.org/wiki/Konsole)

Pre-installed.

You can start it using Start menu -> Applications -> System -> Terminal.

# Work on sensitive documents #
## Office suite ##
[LibreOffice](http://www.libreoffice.org/) ([wikipedia](https://en.wikipedia.org/wiki/LibreOffice)) is recommend. It is a full-featured office productivity suite that provides a near drop-in replacement for Microsoft(R) Office. A word processor, a spreadsheet and a presentation application is included.

You can install it using Start menu -> Applications -> System -> Terminal.

    sudo apt-get update
    sudo apt-get install libreoffice

You can launch them from Start menu -> Applications -> Office.

## Image Editing ##
[kolourpaint4 Homepage with screenshots](http://kolourpaint.sourceforge.net/screenshots.html)

You can install it using Start menu -> Applications -> System -> Terminal.

    sudo apt-get update
    sudo apt-get install kolourpaint4

## Video Editing ##
[Kdenlive Homepage with screenshots](http://www.kdenlive.org/); [Kdenlive in wikipedia](https://en.wikipedia.org/wiki/Kdenlive)

You can install it using Start menu -> Applications -> System -> Terminal.

    sudo apt-get update
    sudo apt-get install kdenlive

## Publishing ##
[Scribus](http://www.scribus.net/) is an Open Source Desktop Page Layout accessible from the Applications → Graphics. It can be used for many tasks; from booklets design to newspapers, magazines, newsletters and posters to technical documentation. It has sophisticated page layout features like precision placing and rotating of text and/or images on a page, manual kerning of type, bezier curves polygons, precision placement of objects, layering with RGB and CMYK custom colors. The Scribus document file format is XML-based. Unlike proprietary binary file formats, even damaged documents can be recovered with a simple text editor.

You can install it using Start menu -> Applications -> System -> Terminal.

    sudo apt-get update
    sudo apt-get install scribus

## Audio Editing ##
[kwave](http://kwave.sourceforge.net/) is a multi-track audio editor for Linux/Unix, MacOS and Windows. It is designed for easy recording, playing and editing of digital audio.

You can install it using Start menu -> Applications -> System -> Terminal.

    sudo apt-get update
    sudo apt-get install kwave

## Printing and scanning ##
Printing is risky. This is not a Whonix related issues. It is a general issue with printers.

Quotes from [eff.org](https://www.eff.org/issues/printers):
*"Imagine that every time you printed a document it automatically included a secret code that could be used to identify the printer - and potentially the person who used it. Sounds like something from an episode of "Alias " right?*

*Unfortunately the scenario isn't fictional."*

I don't know if scanners also add such a kind of extra hidden data.

If you want to be secure side, buy an extra printer/scanner, which you only use for anonymous activity.

Another non-technical issue with anonymous printing nowadays is forensic, fingerprint, DNA, etc.

## scurl - SSL command line downloader ##
**Advanced users.**

scurl comes with next Whonix version 0.5.x.

It's a simple wrapper account curl. */usr/local/bin/scurl* takes precedence over /usr/bin/curl and simply adds "*--tlsv1 --proto =https*" to all runs of curl. It also has [Stream Isolation] in Whonix, because */usr/local/bin/curl* takes precedence over */usr/bin/curl*.

To invoke it.

    scurl https://check.torproject.org

All other curl/linux features continue to work, such as.

    scurl https://check.torproject.org > index.html

To store the output inside a file.

    scurl http://check.torproject.org

Will result as expected in.

    curl: (1) Protocol http not supported or disabled in libcurl

Same for.

    scurl check.torproject.org

Will result as expected in.

    curl: (1) Protocol http not supported or disabled in libcurl

Running it against an self-signed or invalid SSL certificate.

    scurl https://www.debian-administration.org

Will result in an error, for example.

    curl: (60) SSL certificate problem: self signed certificate
    More details here: http://curl.haxx.se/docs/sslcerts.html

    curl performs SSL certificate verification by default, using a "bundle"
     of Certificate Authority (CA) public keys (CA certs). If the default
     bundle file isn't adequate, you can specify an alternate file
     using the --cacert option.
    If this HTTPS server uses a certificate signed by a CA represented in
     the bundle, the certificate verification probably failed due to a
     problem with the certificate (it might be expired, or the name might
     not match the domain name in the URL).
    If you'd like to turn off curl's verification of the certificate, use
     the -k (or --insecure) option.

## License ##
    Whonix Software wiki page Copyright (C) Amnesia <amnesia at boum dot org>
    Whonix Software wiki page Portions Copyright (C) 2012 adrelanos <adrelanos at riseup dot net>
    
    This program comes with ABSOLUTELY NO WARRANTY; for details see the wiki source code.
    This is free software, and you are welcome to redistribute it
    under certain conditions; see the wiki source code for details.

# Footer #
[[include ref=WikiFooter]]