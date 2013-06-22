[[include ref=WikiHeader]]

[TOC]

= Dummy Tor =

'''Beginning with Whonix 0.5.x...'''

Whonix-Workstation has an empty Tor package installed by default, called Dummy Tor package. It contains no files, besides some default files <sup>1</sup>, which are required to create a dummy package. Debian packages are standard Unix '''ar''' archives, auditors can unpack and check them.

The reason for installing the Dummy Tor package inside Whonix-Workstation is to prevents installing the Tor package from the repository, to prevent running Tor over Tor. This allows installation of packages, which depend on Tor, such as TorChat and parcimonie.

To prevent the package from upgrading

<pre>echo &quot;tor hold&quot; | sudo dpkg --set-selections</pre>
has been run while building Whonix from source code.

To check the status an auditor could run.

<pre>dpkg --get-selections | grep tor</pre>
To undo holding the packing a user could run.

<pre>echo &quot;tor install&quot; | sudo dpkg --set-selections</pre>
= Implementation =

* Everything is inside the ''whonix_workstation/usr/local/share/whonix/dummytor/'' folder in Whonix source code
* and subsequently in /usr/local/share/whonix/dummytor/ in Whoix-Workstation.
* .deb package format
* /usr/local/share/whonix/dummytor/tor is the control file
* /usr/local/share/whonix/dummytor/tor_1.0_all.deb is the package which was installed using dpkg by whonix_workstation/usr/local/share/whonix_internal_install_script.
* whonix_workstation/usr/local/share/whonix/dummytor/dummytor is the &quot;build script&quot; for the package, which is actually only a single &quot;equivs-build ./tor&quot; command.

= How it would look... =

...if a Tor version higher than 1.0 was released.

<pre>sudo apt-get dist-upgrade

Reading package lists... Done
Building dependency tree       
Reading state information... Done
Calculating upgrade... Done
The following packages have been kept back:
  tor</pre>
= Footnotes =

<font size="-3"> ,, <sup>1</sup> changelog.gz copyright README.Debian control control.tar.gz data.tar.gz debian-binary md5sums </font>

= Footer =

[[include ref=WikiFooter]]

