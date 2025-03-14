
import re
import os
from markdown_to_html_node import *

# Pulls h1 element from a markdown file and returns it. Strips # and leading/trailing whitespace
def extract_title(markdown):
    pattern = "^# {1}.*\n"
    x = re.findall(pattern, markdown)
    if len(x) == 0:
        raise Exception("No title found")
    else:
        title_text = x[0].split("# ")[1].strip()
        return title_text

# Generates an index page at the provided dest_path (in .html) from a from_path(markdown) and a template(.html)
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    # Opens the source markdown file and reads the contents into a variable
    with open(from_path) as source_file:
        source_file_contents = source_file.read()
    # opens the template file and reads the contents into a variable
    with open(template_path) as template_file:
        template_file_contents = template_file.read()

    # Converts the source file contents into a markdown node and then converts that to readable html
    html_string = markdown_to_html_node(source_file_contents).to_html()
    # Finds the title in the markdown file and extracts it
    title_text = extract_title(source_file_contents)
    # Use a regex pattern to replace the content field in the template with the generated HTML
    new_file = re.sub("{{ Content }}", html_string, template_file_contents)
    # Uses a regex pattern to replace the title field in the now modified template with the extracted title
    new_file = re.sub("{{ Title }}", title_text, new_file)
    
    # Creates and opens the new file, writes the HTML, and closes the file
    dest_file = open(dest_path, "w")
    dest_file.write(new_file)
    dest_file.close()