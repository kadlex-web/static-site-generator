from textnode import *
from htmlnode import *
from copy_static import *

def main():
    destination = "/Users/ak/workspace/github.com/kadlex-web/static-site-generator/public"
    source = "/Users/ak/workspace/github.com/kadlex-web/static-site-generator/static"
    copy_static(source, destination)
main()