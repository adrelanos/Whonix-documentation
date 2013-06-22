[[include ref=WikiHeader]]

[TOC]

= OLD =

'''Old instructions for copy and paste. This is available now as a script, see [LeakTests].'''

= Introduction =

This leak testing article was written by adrelanos and smarm for Whonix but it can be useful for other projects as well.

Discussion: “Leak testing” (as defined here), is the process of verifying that the Whonix-Gateway will not send unencrypted / “in the clear” network traffic. Only Tor traffic should be observed coming from the Whonix-Gateway.

= Leak through the Whonix-Gateway =

Due to misconfiguration of the Whonix-Gateway the Whonix-Gateway might forward traffic for Whonix-Workstation which goes not trough Tor. The following tests are designed to test for such behaviour.

== Step 0: restrict Tor outgoing ports while testing ==

Why we do this will be clarified in Step 5.

'nano /etc/tor/torrc' and uncomment

<pre>#+# #OptionalFeatureNr.6#
#+# See Whonix/LeakTests. Activate this while testing for leaks. (Step 0)
#+# Deactivate after you are done! (Important!) (Step 9)
ReachableDirAddresses*:80
ReachableORAddresses*:443
FascistFirewall 1</pre>
and restart Tor using '/etc/init.d/tor restart'

This has to be undone after you finished testing. You will be reminded at the end of this chapter.

== Step 1: Prepare the testing infrastructure ==

Three tools are used during testing:

[http://en.wikipedia.org/wiki/Scapy Scapy]: To create network traffic for testing. It is also desirable that the network traffic used in testing does not expose you to possible violations of security! Thus Scapy offers fine grained control over the creation of traffic for use with testing. Functionality defined here can be formalized into [http://en.wikipedia.org/wiki/Unit_test “Unit Tests”] via [http://www.secdev.org/projects/UTscapy/ UTScapy].

[http://en.wikipedia.org/wiki/Wireshark Wireshark]: Used to sniff network traffic. Can be configured with fine grained [http://www.wireshark.org/docs/wsug_html_chunked/ChCapCaptureFilterSection.html “Capture Filters”], which can filter the traffic reported and captured by wireshark while sniffing traffic.

[http://en.wikipedia.org/wiki/Python_%28programming_language%29 Python]: Used to support Scapy and can be used to easily script Scapy tests.

Install <code>wireshark</code> to the Whonix-Gateway:

<pre>apt-get install tshark</pre>
Set capabilities to run wireshark with user privileges

<pre>sudo setcap cap_net_raw,cap_net_admin=eip /usr/bin/dumpcap</pre>
Install <code>scapy</code> to the Whonix-Workstation:

<pre>apt-get install python-scapy</pre>
(This automatically installs Python as a dependency of Scapy)

== Step 2: Verify Wireshark is installed and working ==

(Whonix-Gateway)

'''Warning''': It is is unadvisable to run Wireshark as root. 'su user'

Starting <code>Wireshark</code> without options will begin to capture packets on the first available interface:

<pre>tshark</pre>
You should see packets begin to scroll down the screen. This indicates you are seeing normal network traffic (ARP, DHCP requests, Tor traffic, etc). This will give you some idea of what to look for when we test for “leaked” traffic below.

== Step 3: Verify Scapy is installed and working ==

(Whonix-Workstation)

Start Scapy with elevated privileges to allow both sending and receiving of packets:

<pre>sudo scapy</pre>
This should present you with an interactive prompt:

<pre>Welcome to Scapy 2.1.0
&gt;&gt;&gt;</pre>
Other “WARNING” or “INFO” items that appear when you start Scapy, are most likely not going to effect your use of Scapy for this testing.

Type the <code>ls()</code> command, to see an overview of the protocols supported by Scapy:

<pre>&gt;&gt;&gt; ls()</pre>
Type the <code>ls()</code> command and pass it a protocol type, to see information supported by that protocol and its packet construction:

<pre>&gt;&gt;&gt; ls(IP)</pre>
Type the <code>exit()</code> command to end your interactive session with Scapy:

<pre>&gt;&gt;&gt; exit()</pre>
See more information at the official [http://www.secdev.org/projects/scapy/doc/usage.html# Scapy documentation].

== Step 4: Do a simple ping test ==

(Whonix-Workstation)

Since Scapy is scriptable via Python, we'll use Scapy from within a Python script for our testing. An example script that creates a simple ICMP ping to the Whonix-Gateway's <code>eth1</code> interface:

<pre>nano simple_ping.py</pre>
Paste this code and save.

<pre>#! /usr/bin/env python

# Since it will be useful to know something about the script, for the later tests, the terms are defined here:
# (A discussion of Python language structure is beyond the scope of this document)

# [1] http://en.wikipedia.org/wiki/Ipv4
# [2] http://en.wikipedia.org/wiki/Internet_Control_Message_Protocol
# [3] http://en.wikipedia.org/wiki/IP_routing
# [4] http://en.wikipedia.org/wiki/Ping
# [5] http://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#List_of_permitted_control_messages_.28incomplete_list.29
# [6] http://www.secdev.org/projects/scapy/doc/usage.html#send-and-receive-packets-sr
# [7] http://www.secdev.org/projects/scapy/doc/usage.html#stacking-layers

import sys
from scapy.all import*

# define the target gateway &amp; data payload
target # &quot;192.168.0.1&quot;
data # &quot;testing&quot;

# define packets
# These define two variables, that are set to the object types IP and ICMP respectively. These objects in Scapy define the protocol type for IP (default IPv4) [1] and ICMP [2] respectively. And will send packets on the wire of these types when used. 
ip # IP()
icmp # ICMP()

# define packet parameters
ip.dst # target

# IP packets are used for routing [3] between networks on the Internet. So, we assign the destination (**dst**) in the IP portion of the packet we're going to assemble and send out.
icmp.type # 8
icmp.code # 0

# Defines the type of ICMP message to send out. The **8 type** is a type defined as **echo request**, e.g. a simple ping [4]. See a list here of  various types of ICMP [5] messages here.

# The  sr1() [6] command will **send and receive network traffic, returning the 1st packet received**.
# The notation of **ip/icmp/data** is the notation for encapsulation of various instances of networking protocols [7]. Read it right to left: **data encapsulated inside an ICMP message and encapsulated inside an IP datagram**.</pre>
test_ping # sr1(ip/icmp/data)

<pre>if isinstance(test_ping, types.NoneType):
        print &quot;No response&quot;
else:
# Prints a short report on the packet received (if any). 
        test_ping.summary()</pre>
Which will report the first successful ping from <code>eth1</code> on the Whonix-Gateway.

To test, simply:

<pre>sudo python simple_ping.py</pre>
Which will report with something similar to:

<pre>Begin emission:
.....Finished to send 1 packets.
.*
Received 7 packets, got 1 answers, remaining 0 packets</pre>
== Step 5: Setting up a “non-Tor traffic” capture with Wireshark ==

(Whonix-Gateway)

The command:

<pre>sudo -u user tshark -i eth0 -S -f &quot;ip and src host 10.0.2.15 and not (port 80 or port 443 or port 9001 or port 9030 or ssh)&quot;</pre>
(if you are not using VirtualBox NAT, you have to change the IP to your eth0 ip address, to find out that address type 'ifconfig') (TODO: make the command independent from the IP, use eth0)

When started wireshark should show NO packet information on the screen, as opposed to above where we capture Everything. To verify it's working correctly (and logging something, as opposed to logging nothing), (open a second SSH session or learn 'screen') from your Whonix-Gateway attempt to ping google.com. This should show something similar to:

<pre>5.115829 &lt;eth0 IP address&gt; -&gt; &lt;nearby Google mirror&gt; ICMP 98 Echo (ping) request  id#0x1010,</pre>
seq#1/256, ttl#64 5.184410 <eth0 IP address> -&gt; <DNS server> DNS 86 Standard query PTR <some reverse IP> .in-addr.arpa

Where the IP and DNS names have been redacted to protect the innocent.

Leave this capture running for subsequent tests.

'''Discussion''':

(See the [http://www.wireshark.org/docs/man-pages/tshark.html tshark manual page] for more information)

'''-S''': Decode and display packets even while writing raw packet data using the -w option.

'''-i''': Set the name of the network interface or pipe to use for live packet capture.

'''-f''': Set the capture filter expression.

The “capture expression” (the bit in quotes above, after the '-f') reads: IP packets and from host 10.0.2.15 (your '''eth0 IP''' address) where the ports are NOT 80, 443, 9901 or 9030 ([https://trac.torproject.org/projects/tor/wiki/doc/TorFAQ#DoIhavetoopenalltheseoutboundportsonmyfirewall common ports for Tor, see the FAQ]). The “ssh” keyword on the end is a predefined primitive in wireshark, used to define SSH traffic only. Adding this should not effect your capture if you are not using SSH to connect to the gateway, but should save you quite a bit of trouble filtering out your SSH traffic if you are.

See the [http://www.wireshark.org/docs/wsug_html_chunked/ChCapCaptureFilterSection.html documentation for the format of the “capture filter” here], for more information.

(Note: This may not cover all valid TOR traffic emiting from your Whonix, some Tor nodes may use non-standard ports and was observed during testing. The FAQ above, also covers this.)

== Step 6: Scapy traffic testing: IP packets ==

(Whonix-Workstation)

Other testing is in the same vein as our ping (above).

'''First''': We'll test IP datagrams of all types to see if any are emitted:

<pre>nano exhaustive_ip_send.py</pre>
Paste this code and save.

<pre>#! /usr/bin/env python

import sys
from scapy.all import*

#define the target gateway &amp; data payload
target # &quot;google.com&quot;
data # &quot;testing&quot;

#define packet
ip # IP()

#define packet parameters
ip.dst # target

#loop through all IP packet types
for ip_type in range(0,255):
        ip.proto # ip_type
        send(ip/data)</pre>
Run

<pre>sudo python exhaustive_ip_send.py</pre>
On Whonix-Gateway you should see NO output from Wireshark. Otherwise you may have discovered a leak. [http://en.wikipedia.org/wiki/IPv4#Packet_structure Documentation on IP packet structure] and [http://en.wikipedia.org/wiki/List_of_IP_protocol_numbers IP Protocol numbers].

== Step 7: Scapy traffic testing: TCP packets and ports ==

(Whonix-Workstation)

'''Second''': We'll test TCP packets across all ports: (Note: This may appear as an '''ATTACK''' from some conservative ISP's / sites, use with caution. Google fields many of these types of scan's per day, so testing like this is most likely lost in the noise)

<pre>nano tcp_test.py</pre>
Paste this code and safe.

<pre>#! /usr/bin/env python

import sys
from scapy.all import*

#define the target gateway &amp; data payload
target # &quot;google.com&quot;
data # &quot;testing&quot;

#define packets
ip # IP()
tcp # TCP()

#define packet parameters
ip.dst # target

#loop through all TCP ports
for tcp_port in range(0,65535):
        tcp.dport # tcp_port
        send(ip/tcp/data)</pre>
Run

<pre>sudo python tcp_test.py</pre>
Again Whonix-Gateway should report NO activity, otherwise we've found a leak [http://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers TCP / UDP port number documentation].

== Step 8: Scapy traffic testing: UDP packets and ports ==

(Whonix-Workstation)

'''Third''': We'll test UDP packets across all ports:

(Note: This may also be construed as an attack, Google is a good target for this, just as with the TCP test)

<pre>nano udp_test.py</pre>
Paste this code and safe.

<pre>#! /usr/bin/env python

import sys
from scapy.all import*

#define the target gateway &amp; data payload
target # &quot;google.com&quot;
data # &quot;testing&quot;

#define packets
ip # IP()
udp # UDP()

#define packet parameters
ip.dst # target

#loop through all TCP ports
for udp_port in range(0,65535):
        udp.dport # udp_port
        send(ip/udp/data)</pre>
Run

<pre>sudo python udp_test.py</pre>
Again, check for leaks. [http://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers TCP / UDP port number documentation].

== Step 9: undo Step 0 ==

Undo Step 0 now!

= Footer =

[[include ref=WikiFooter]]

