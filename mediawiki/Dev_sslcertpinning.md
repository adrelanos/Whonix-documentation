[[include ref=WikiHeader]]

[TOC]

'''''DRAFT! UNFINISHED!'''''

= PIN Certificate Authority =

Weaker method (still better than no pinning at all), more easy to maintain.

Install required software:

<pre>apt-get install ca-certificates curl</pre>
Download.

<pre>curl --verbose --tlsv1 --proto =https --capath /invalid/ --cacert /usr/share/ca-certificates/mozilla/DigiCert_High_Assurance_EV_Root_CA.crt https://check.torproject.org</pre>
= PIN Certificate Directly =

== curl method ==

Better method, more difficult to maintain.

Install required software:

<pre>apt-get install ca-certificates curl</pre>
Download the public SSL certificate:

<pre>openssl s_client -connect torproject.org:443 -CAfile /usr/share/ca-certificates/mozilla/DigiCert_Assured_ID_Root_CA.crt &gt;./x.cert &lt;/dev/null</pre>
Or better:

<pre>echo -n | openssl s_client -connect torproject.org:443 -CAfile /usr/share/ca-certificates/mozilla/DigiCert_Assured_ID_Root_CA.crt | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' &gt; ./torproject.pem</pre>
Get SHA-1 fingerprint:

<pre>openssl x509 -noout -in torproject.pem -fingerprint -sha1</pre>
Get SHA-256 fingerprint:

<pre>openssl x509 -noout -in torproject.pem -fingerprint -sha256</pre>
Manually compare SHA-1 and SHA-256 fingerprints with [https://www.torproject.org/docs/faq.html.en#SSLcertfingerprint torproject.org FAQ: SSL].

<pre>.</pre>
Optionally render the ca-certificates useless for testing purposes. <font size="-3">Using ''curl'' here, but ''wget'' has a bug [https://lists.gnu.org/archive/html/bug-wget/2012-07/msg00008.html Bug] and uses the ca-files anyway.</font>

<pre>sudo mv /usr/share/ca-certificates /usr/share/ca-certificates_</pre>
Download with curl and the pinned certificate:

<pre>curl --cacert ./torproject.pem https://check.torproject.org/ &gt; check.html</pre>
== Alternate perl method ==

[http://security.stackexchange.com/questions/20399/how-to-verify-the-ssl-fingerprint-by-command-line-wget-curl Source]. '''''Not reviewed!'''''

<pre>#!/usr/bin/perl
# http://security.stackexchange.com/questions/20399/how-to-verify-the-ssl-fingerprint-by-command-line-wget-curl
# Code snippets taken from Net::SSLeay documentation and mildly modified.
# Requires a newer version of SSLeay (tested with 1.48)
# Needless to say, verify correct $host and $fingerprint before testing!!!

use Net::SSLeay qw(get_https3);

$host = &quot;www.google.com&quot;;
$port = 443;
$fingerprint = &quot;C1:95:6D:C8:A7:DF:B2:A5:A5:69:34:DA:09:77:8E:3A:11:02:33:58&quot;;

($p, $resp, $hdrs, $server_cert) = get_https3($host, $port, '/');
if (!defined($server_cert) || ($server_cert == 0)) {
    warn &quot;Subject Name: undefined, Issuer  Name: undefined&quot;;
} elsif (Net::SSLeay::X509_get_fingerprint($server_cert, &quot;sha1&quot;) ne $fingerprint) {
    warn 'Invalid certificate fingerprint '
        .  Net::SSLeay::X509_get_fingerprint($server_cert, &quot;sha1&quot;)
        . ' for ' . Net::SSLeay::X509_NAME_oneline(
             Net::SSLeay::X509_get_subject_name($server_cert));
} else {
    print $p;
}</pre>
= Sources =

<font size="-3"> Sources:

* [http://sourceforge.net/tracker/?func=detail&aid=3569642&group_id=976&atid=350976 curl Feature Request: Pinning SSL certificates / check SSL fingerprints - ID: 3569642]
* [http://stackoverflow.com/questions/7084482/how-to-save-the-ldap-ssl-certificate-from-openssl How to save the LDAP SSL Certificate from OpenSSL]
* [http://www.madboa.com/geek/openssl/ OpenSSL Command-Line HOWTO] </font>

= Footer =

[[include ref=WikiFooter]]#

