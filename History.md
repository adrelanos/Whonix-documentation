[[include ref=WikiHeader]]

[TOC]

# History of Whonix #
Originally called TorBOX, called aos (which stud for anonymous operating system) in meanwhile and finally renamed to Whonix.

TorBOX didn't start as a software project. Originally it was only a wiki site. The goal was to simplify the instructions how to use Tor as a [Transparent Proxy](https://trac.torproject.org/projects/tor/wiki/doc/TransparentProxy) ([w](http://www.webcitation.org/6Fg0ru2Rm)). **Adrelanos** was amazed by the idea, to have a (virtual) machine where all traffic is routed through Tor and where IP or DNS leaks are impossible with the additional benefit, that there are no proxy settings for any applications necessary anymore. Check the [first version of the torproject.org TorBOX wiki site](https://trac.torproject.org/projects/tor/wiki/doc/TorBOX?version=1) ([w](http://www.webcitation.org/6Fg0uhbsR)) how simple it looked like, that was on 2012-01-11.

Quickly other contributors improved the article. You can check that using [torproject.org's wiki history feature](https://trac.torproject.org/projects/tor/wiki/doc/TorBOX?action=history) ([w](http://www.webcitation.org/6Fg0wldJ5)). The TorBOX wiki site grew steady in size, information and complexity. Given the complexity of the required steps, it was necessary to provide leak tests, which was done by **smarm**. **Anonymous** created a shell script to do the many steps in an automated way. **Anonymous** created the first downloadable TorBOX images as well. In the past we had separate articles for manual creation of TorBOX, building using the shell scripts and using the downloads. It became to much overhead to maintain the comprehensive manual instructions to build TorBOX while updating the shell scripts as well. The TorBOX developers agreed to drop the manual creation in favor of the shell scripts. Still, nothing got lost doing this transition. The full documentation, an explanation and justification, why each and any step is done was migrated into the shell scripts. Since all shell scripts were written in bash, anyone able to use the command line was still be able to read the bash script and to do the steps manually.

The shell scripts grew steady because more and more knowledge has been researched, more and more things had to be done to make TorBOX even safer or to add even more functionality. After the release of TorBOX 0.1.3 there was no one willing to create new images, because the process of creation was tiresome. Installing the operating system manually, putting the scripts into the virtual machines and running them for every improvement seemed boring and time consuming. The TorBOX developers agreed to make the build process fully automated. It became also clear, that TorBOX may no longer consist of only two shell scripts. The big scripts had to be spitted to many more files. Rather it became clear, that a wiki is no longer suited for lots of development related discussion and source code commits. Also a dedicated TorBOX website became required.

Andrew Lewman told adrelanos in private mail, that it would be better if TorBOX was renamed. Even though it was announced on the website that it's unaffiliated with the Tor project, people confused TorBOX with the Tor project. A new name for the project had to be found. In a rush adrelanos renamed to project to aos, which stud of anonymous operating system. The name was a suboptimal choice. Searching for it in search engines did not bring up any results because it was already used for too many other things. Also a name starting with a small character is suboptimal, because at the beginning of a sentence it must be a big character. Adrelanos asked on the tor-talk mailing list for ideas for an anonymous operating system project and got lots of suggested. Whonix was suggested and one of the very few unused terms in search engines, therefore it was chosen as new project name by adrelanos.

TransPort, SocksPort, Transparent Proxy, Isolating Proxy, ...

...

Whonix developer ([w](http://www.webcitation.org/6Eny0UfAI)), [named proper in past]((https://trac.torproject.org/projects/tor/wiki/doc/proper?version=1)) ([w](http://www.webcitation.org/6Fg1zUNeQ)), [renamed itself to adrelanos](https://trac.torproject.org/projects/tor/wiki/doc/proper?version=6) ([w](http://www.webcitation.org/6Fg2p2YK3)), [published its OpenPGP key on 05/29/12](https://trac.torproject.org/projects/tor/wiki/doc/proper?version=3) ([w](http://www.webcitation.org/6Fg336X1H)) ([wiki history](https://trac.torproject.org/projects/tor/wiki/doc/proper?action=history) ([w](http://www.webcitation.org/6Fg24cX1W))). Its OpenPGP key is mirrored online on seven different places, see [TrustingWhonixSigningKey](https://sourceforge.net/p/whonix/wiki/TrustingWhonixSigningKey/) ([w](http://www.webcitation.org/6Fg3L8QCZ)).

# Whonix versions #
## Source for downloaded image ##
The scripts used to build a certain downloaded version of a TorBOX-Gateway or TorBOX-Workstation image can be **also** found in the VM at /usr/share/doc/torbox (in TorBox 0.2 at /usr/local/bin/tor-*) and through the wiki history.

## TorBOX 0.1.3 (old, outdated, released) ##
TorBOX 0.1.3, which was **released** as build from source and download version.

[BuildDocumentation_0.1.3](https://sourceforge.net/p/whonix/wiki/BuildDocumentation_0.1.3) ([w](http://www.webcitation.org/6Fg0zx0gG))
[Source Code 0.1.3](https://github.com/adrelanos/Whonix/zipball/0.1.3) ([w](http://www.webcitation.org/6Fg10ot0Q)) (Available as signed git tag. Signed by adrelanos.)

It no longer builds, due to breaking changes from Tor 0.2.2 to Tor 0.2.3.

## TorBOX 0.2.0-debootstrap (only development version) ##
There was also an attempt by **anonymous** to build TorBOX 0.2.0-debootstrap. It has been dropped because there were too many issues. The open issues are noted within the files. **Never released.** If anyone wants to continue working on it that's certainly possible, let's discuss this on Whonix/Dev then.

[Old-development-only source code](https://sourceforge.net/projects/whonix/files/old-development-only/) ([w](http://www.webcitation.org/6Fg16vX9G)) has been archived.

## TorBOX 0.2.0-no-network-while-preseeding (only development version) ##
Based on TorBOX 0.2.0-debootstrap, there was also an attempt by **adrelanos** to create TorBOX 0.2.0-no-network-while-preseeding, which failed. **Never released.** (The goal was to save time while installing/preseeding.) That attempt failed, because of an issue with grub, see [Wrong root device when using update-grub inside chroot (building VM images)](https://lists.gnu.org/archive/html/help-grub/2012-07/msg00008.html) ([w](http://www.webcitation.org/6Fg1AjpT9)). Another issue was a limitation in preseed, see [Problem trying to preseed netcfg/no_interfaces](http://lists.debian.org/debian-boot/2008/12/msg00159.html) ([w](http://www.webcitation.org/6Fg1BaR16)). Build documentation was never written but the build script was self explanatory. If anyone wants to continue working on it that's certainly possible, let's discuss this on Whonix/Dev then.

[Old-development-only source code](https://sourceforge.net/projects/whonix/files/old-development-only/) ([w](http://www.webcitation.org/6Fg1CVt7H)) has been archived.

## TorBOX 0.2.1 (old, released) ##
https://sourceforge.net/projects/whonix/files/old-development-only/torbox-0.2.1/ ([w](http://www.webcitation.org/6Fg1DOC9r))

https://sourceforge.net/p/whonix/wiki/BuildDocumentation_0.2.1 ([w](http://www.webcitation.org/6Fg1EC5on))

## Whonix 0.3.0 (never released) ##
Last example implementation based on Ubuntu. Was never released due to potential trademark issues, see [Switch from Ubuntu to Debian](https://sourceforge.net/p/whonix/wiki/OperatingSystem/#switch-from-ubuntu-to-debian) ([w](http://www.webcitation.org/6Fg1N14Op)).

https://sourceforge.net/p/whonix/wiki/BuildDocumentation_0.3.0 ([w](http://www.webcitation.org/6Fg1Nt5p0))

## Whonix 0.4.4 (old, released) ##
Still contained a lot usability bugs. There was need to rush for that release. The 0.2.1 release was already quite old. There was need due to potential trademark issues to switch Whonix example implementation from Ubuntu to Debian, see [Switch from Ubuntu to Debian](https://sourceforge.net/p/whonix/wiki/OperatingSystem/#switch-from-ubuntu-to-debian) ([w](http://www.webcitation.org/6Fg1N14Op)). *Adrelanos* wrote a news on *2012-28-09*: "*I did not want to delay this release any further. The mess with multiple project names and websites had to come to an end. I've seen people loosing interest in open source projects, because there was no visible progress. This is no vaporware.*".

Introduced fully automated build system based on bash scripts, grml-debootstrap and chroot.

https://sourceforge.net/p/whonix/wiki/BuildDocumentation_0.4.0 ([w](http://www.webcitation.org/6Fg1R13pY))

## Whonix 0.4.5 (old, released) ##
Released on *2012-09-10*. Fixed many usability bugs and other small bugs. Was the first version which was announced on the [tor-talk mailing list](https://lists.torproject.org/pipermail/tor-talk/2012-October/025921.html) ([w](http://www.webcitation.org/6Fg1Rq0QI)). Received some press.

https://sourceforge.net/p/whonix/wiki/BuildDocumentation_0.4.0 ([w](http://www.webcitation.org/6Fg1Sido0))

# Footer #
[[include ref=WikiFooter]]