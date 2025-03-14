from textnode import *
from htmlnode import *
from copy_static import *
from server_utility import *

def main():
    destination = "/Users/ak/workspace/github.com/kadlex-web/static-site-generator/public"
    source = "/Users/ak/workspace/github.com/kadlex-web/static-site-generator/static"

    copy_static(source, destination)

    from_path = '/Users/ak/workspace/github.com/kadlex-web/static-site-generator/content/index.md'
    template_path = '/Users/ak/workspace/github.com/kadlex-web/static-site-generator/template.html'
    dest_path = '/Users/ak/workspace/github.com/kadlex-web/static-site-generator/public/index.html'

    generate_page(from_path, template_path, dest_path)
main()