# Whonix-documentation
## Download

    git clone https://github.com/adrelanos/Whonix-documentation.git

## Re-download documentation from sourceforge
Must be lower case "whonix".

    ./pull-wiki-v2.py whonix
    
## Convert to media wiki syntax

Use pandoc 1.11.1 (its only in Debian testing and from its homepage) the older version (in Debian stable) has too much bugs.

    ./convert-to-mediawiki
    
