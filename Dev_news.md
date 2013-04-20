[TOC]

# Whonix News File Format #
**Version 0.2**

First line contains version and may not contain any spaces!


    0.3.0

    news text here
    some more news text
    ...

# How to create a valid Whonix News File #
(1). safe as whonix_news

    .

(2). sign

    gpg --clearsign whonix_news

(3). test

    gpg --verify whonix_news.asc

# Extra implementation info #
Signing and verification (as sanity check) of https://github.com/adrelanos/Whonix/blob/development/release/whonix_news is automated by https://github.com/adrelanos/Whonix/blob/development/release/upload_whonix_news.

https://github.com/adrelanos/Whonix/blob/development/whonix_shared/usr/local/bin/whonixcheck-scripts/50_check-whonix-news will find out the current installing version by:

    ## Read only FIRST line.
    read -r INSTALLED_WHONIX_VERSION < /usr/local/share/whonix/version
    ## Remove ALL spaces.
    INSTALLED_WHONIX_VERSION="${INSTALLED_WHONIX_VERSION//[[:space:]]}"

While phrasing the whonix_news, it's not required to remove PGP Signature, because the function verify_whonix_news in https://github.com/adrelanos/Whonix/blob/development/whonix_shared/usr/local/bin/whonixcheck-scripts/50_check-whonix-news will use gpg --decrypt to get plain text, which will result in the Whonix News File Format.

# Changelog #
0.1 to 0.2

* /usr/share/whonix/version changed to /usr/local/share/whonix/version

# Footer #
[[include ref=WikiFooter]]