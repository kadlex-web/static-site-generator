from textnode import *
from htmlnode import *
from copy_static import *
from server_utility import *

def main():
    destination = "./public"
    source = "./static"
    print("Moving static files...")
    copy_static(source, destination)

    dir_path_content = "./content"
    template_path = './template.html'
    print("Generating pages...")
    generate_pages_recursive(dir_path_content, template_path, destination)
    
main()