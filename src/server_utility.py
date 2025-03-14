import re
import os
from markdown_to_html_node import *
from pathlib import Path

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
    # creates file
    file_name = os.path.join(dest_path, "index.html")
    # Opens the new file, writes the HTML, and closes the file
    dest_file = open(file_name, "w")
    dest_file.write(new_file)
    dest_file.close()

# Crawls a given directory, finds markdown files, converts to html and writes them to public
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    directories = os.listdir(dir_path_content)
    for file in directories:
        # Uses path to make it easier (and safer) to get the suffix
        file_name = Path(file)
        if file_name.suffix == '.md':
            source_content = os.path.join(dir_path_content, file_name)
            generate_page(source_content, template_path, dest_dir_path)
        elif file_name.suffix == '':
            new_dir_path_content = os.path.join(dir_path_content, file)
            new_dest_dir_path = os.path.join(dest_dir_path, file)
            if os.path.exists(new_dest_dir_path) != True:
                os.mkdir(new_dest_dir_path)
            print(f"moving source to {new_dir_path_content} and dest to {new_dest_dir_path}")
            generate_pages_recursive(new_dir_path_content, template_path, new_dest_dir_path)
        else:
            pass