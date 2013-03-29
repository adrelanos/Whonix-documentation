[[include ref=WikiHeader]]

[TOC]

***DRAFT! UNFINISHED!***

# curl method #
Install required software:

    apt-get install ca-certificates curl

Download the public SSL certificate:

    openssl s_client -connect torproject.org:443 -CAfile /usr/share/ca-certificates/mozilla/DigiCert_Assured_ID_Root_CA.crt >./x.cert </dev/null

Or better:

    echo -n | openssl s_client -connect torproject.org:443 -CAfile /usr/share/ca-certificates/mozilla/DigiCert_Assured_ID_Root_CA.crt | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > ./torproject.pem

Get SHA-1 fingerprint:

    openssl x509 -noout -in torproject.pem -fingerprint -sha1

Get SHA-256 fingerprint:

    openssl x509 -noout -in torproject.pem -fingerprint -sha256

Manually compare SHA-1 and SHA-256 fingerprints with [torproject.org FAQ: SSL](https://www.torproject.org/docs/faq.html.en#SSLcertfingerprint).

    .

Optionally render the ca-certificates useless for testing purposes.
<font size="-3">Using *curl* here, but *wget* has a bug [Bug](https://lists.gnu.org/archive/html/bug-wget/2012-07/msg00008.html) and uses the ca-files anyway.</font>

    sudo mv /usr/share/ca-certificates /usr/share/ca-certificates_

Download with curl and the pinned certificate:

    curl --cacert ./torproject.pem https://check.torproject.org/ > check.html

# Alternate perl method #
[Source](http://security.stackexchange.com/questions/20399/how-to-verify-the-ssl-fingerprint-by-command-line-wget-curl). ***Not reviewed!***

    #!/usr/bin/perl
    # http://security.stackexchange.com/questions/20399/how-to-verify-the-ssl-fingerprint-by-command-line-wget-curl
    # Code snippets taken from Net::SSLeay documentation and mildly modified.
    # Requires a newer version of SSLeay (tested with 1.48)
    # Needless to say, verify correct $host and $fingerprint before testing!!!

    use Net::SSLeay qw(get_https3);

    $host = "www.google.com";
    $port = 443;
    $fingerprint = "C1:95:6D:C8:A7:DF:B2:A5:A5:69:34:DA:09:77:8E:3A:11:02:33:58";
    
    ($p, $resp, $hdrs, $server_cert) = get_https3($host, $port, '/');
    if (!defined($server_cert) || ($server_cert == 0)) {
        warn "Subject Name: undefined, Issuer  Name: undefined";
    } elsif (Net::SSLeay::X509_get_fingerprint($server_cert, "sha1") ne $fingerprint) {
        warn 'Invalid certificate fingerprint '
            .  Net::SSLeay::X509_get_fingerprint($server_cert, "sha1")
            . ' for ' . Net::SSLeay::X509_NAME_oneline(
                 Net::SSLeay::X509_get_subject_name($server_cert));
    } else {
        print $p;
    }

# Sources #
<font size="-3">
Sources:

* [curl Feature Request: Pinning SSL certificates / check SSL fingerprints - ID: 3569642](http://sourceforge.net/tracker/?func=detail&aid=3569642&group_id=976&atid=350976)
* [How to save the LDAP SSL Certificate from OpenSSL
](http://stackoverflow.com/questions/7084482/how-to-save-the-ldap-ssl-certificate-from-openssl)
* [OpenSSL Command-Line HOWTO
](http://www.madboa.com/geek/openssl/)
</font>

# Footer #
[[include ref=WikiFooter]]