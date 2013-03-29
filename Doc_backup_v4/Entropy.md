[[include ref=WikiHeader]]

[TOC]

# Introduction #
Whonix 0.5.5 and above have haveged installed by default. (see below)

The [Linux Kernel man page](http://www.kernel.org/doc/man-pages/online/pages/man4/random.4.html) says:
> "*\[...\] /dev/random should be suitable for uses that need very high quality randomness* \[...\]".

Quoted from the [riseup.net page about entropy](https://we.riseup.net/riseup+tech/entropy): 
> "*\[...\] entropy-estimation is a black-art and not very well understood \[...\]*".

While it would be good to be cautions, i.e. learning about the entropy quality in Virtual Machines and if required learning about methods to improve it, it's not a critical problem. Successful entropy estimation attacks have never been reported for any software.

# Information resources #
## Resources ##
* [Gentoo wiki: Generating better random numbers](http://en.gentoo-wiki.com/wiki/Generating_better_random_numbers#Dieharder)
* [HAVEGE: PolarSSL Security Advisory 2011-02](https://polarssl.org/tech-updates/security-advisories/polarssl-security-advisory-2011-02)
* [Qemu: virtio-rng, virtual random generator](http://wiki.qemu.org/Features/VirtIORNG)

## Virtual Box Bug Reports ##
* [entropy quality](https://www.virtualbox.org/ticket/11296)
* [poor entropy performance](https://www.virtualbox.org/ticket/11297)

## Software Packages ##
It has to be researched if they do work well inside Virtual Machines (Virtual Box). Simply installing all of them may not be wise.

* [entropy broker](http://www.vanheusden.com/entropybroker/): Not in Debian.
* rng-tools: In Debian.
* timer_entropyd: [Not in Debian.](http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=545148)
* audio-entropyd: Not in Debian.
* video-entropyd: Not in Debian.
* clrngd: In Debian.
* ekeyd: In Debian.
* HAVEGE: In Debian. See below.

### haveged ###
Haveged is an entropy gathering daemon.

Quoted form the [haveged testing page](http://www.issihosts.com/haveged/ais31.html):
> "*\[...\] will behave similarly in a virtual environment is a more risky proposition \[...\] there have been reports of VM that implement the processor time stamp counter as a constant and there are known differences in cpuid operation in others. \[...\]*"

Will haveged create sufficient entropy in Virtual Box? Luckily, haveged comes with tools to check the if the entropy it creates.

The README in the haveged source folder and the [haveged website](http://www.issihosts.com/haveged/index.html) contains [instructions](http://www.issihosts.com/haveged/ais31.html) for testing haveged.

    apt-get source haveged
    cd haveged-*
    ./configure --enable-nistest
    make check

    ## perhaps repeat
    #make clean
    #make check

Should say something like

    0 failed individual tests
    PASS: nist/test.sh
    ==================
    All 2 tests passed
    ==================

This was tested in Virtual Box.

# Entropy Key #
[Entropy Key](http://www.entropykey.co.uk/); Hardware not fully open source. Some resources say, it's okay as an additional source of entropy. Where to add it? Since Whonix depends on a host operating system, the Whonix-Gateway and the Whonix-Workstation, where it does make most sense to add it? Perhaps adding it to the host and using a entropy broker could be the most effective method. Better than buying three entropy keys.

# Footer #
[[include ref=WikiFooter]]