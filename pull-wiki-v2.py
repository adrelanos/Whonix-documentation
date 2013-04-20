#!/usr/bin/env python

## License
## Thanks to:
## https://sourceforge.net/p/allura/tickets/3154/

import warnings
with warnings.catch_warnings():
    import re
    import sys
    from optparse import OptionParser
    import urllib
    import json
    import markdown
	
def resolve_page_references(page_source, pages):
    '''
    Find references to pages in the
    specified source (markdown and
    replace with references to our generated pages
    @return the modified source
    '''

    result = page_source
    for page in pages:
        result = re.sub(r'\(%s\)' % (page), r'(%s.html)' % (page), result)

        # [page] without ()'s
        result = re.sub(r'\[%s\]([^\(])' % (page), r'[%s](%s.html)\1' % (page, page), result)

    return result

    
def get_page_source(project_name, page_name):
    '''
    Get the source of the page and unescape the JSON
    @return the page source
    '''
    opener = urllib.FancyURLopener({})
    stream = opener.open('http://sf.net/rest/p/%s/wiki/%s' %(project_name, page_name))
    result = json.load(stream)
    source = result['text']
    source = re.sub(r'\\"', '"', source)
    source = re.sub(r'\\r', '', source)
    source = re.sub(r'\r', '', source)
    source = re.sub(r'\\n', '\n', source)
    return source
    
    
def get_pages(project):
    opener = urllib.FancyURLopener({})
    stream = opener.open('http://sf.net/rest/p/%s/wiki' % (project))
    result = json.load(stream)
    return result['pages']

def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser = OptionParser()

    (options, args) = parser.parse_args(argv)
    
    # error-checking for command-line argument
    if len(argv) != 2:
        print "Usage: python pull-wiki.py <PROJECTNAME>"
        sys.exit(1)
    
    project_name = argv[1]

    pages = get_pages(project_name)
    for page in pages:
        print page
        with open('%s.md' % (page), 'w') as markdown_file:
            source = get_page_source(project_name, page).encode('utf-8').strip()
            markdown_file.write(source)
            #resolved = resolve_page_references(source, pages)
            #html = markdown.markdown(resolved)
            #with open('%s.html' % (page), 'w') as html_file:
            #    html_file.write(html)
        
if __name__ == "__main__":
    sys.exit(main())
    
