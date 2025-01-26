'''Given a single block of markdown text,determines what type of block it is.
Blocks are:
paragraph
heading
code
quote
unordered_list
ordered_list
Only takes a SINGLE block -- meaning that we are probably taking markdown_to_blocks first and creating a block list, and then iterating over the result to determine type

Thinking I can use a regex to determine the block type initially -- and then make sure it abides by block rules afterward using a helper function
'''
import re

def block_to_block_type(markdown):
    # Headings start with 1-6 # characters, followed by a space and then the heading text
    # No helper needed -- because if the block begins with a heading -- it's a heading based on the regex
    re_heading = r"\A#{1,6} .*"
    if re.search(re_heading, markdown):
        return "heading"
    re_code = r"\A`{3}.*?(?=```)"
    # Checks to see if the string (regardless of block length) begins with ``` and ends with ```
    if re.search(re_code, markdown):
        return "code"
    # Checks to see if the block begins with a > character and executes a helper function if it does
    elif markdown.startswith("> "):
        return quote_block_type(markdown)
    # Checks to see if the block begins with a * or - block character and executes a helper function if it does
    elif markdown.startswith("* ") or markdown.startswith("- "):
        return unordered_list_block_type(markdown)
    # Checks to see if the block begins with a 1. and executes a helper function if it does
    elif markdown.startswith("1. "):
        return ordered_list_block_type(markdown)
    # In all other cases -- the text would simply be a paragraph block
    else:
        return "paragraph"

def quote_block_type(markdown):
    markdown_list = markdown.split("\n")
    for block_line in markdown_list:
        if block_line.startswith("> ") == False:
            return "paragraph"
    return "quote"
    
def unordered_list_block_type(markdown):
    markdown_list = markdown.split("\n")

    if markdown_list[0].startswith("* "):
        for block_line in markdown_list:
            if block_line.startswith("* ") == False:
                return "paragraph"
        return "unordered_list"
    elif markdown_list[0].startswith("- "):
        for block_line in markdown_list:
            if block_line.startswith("- ") == False:
                return "paragraph"
        return "unordered_list"
    else:
        return "paragraph"

def ordered_list_block_type(markdown):
    markdown_list = markdown.split("\n")
    # use a range iterator to check the value of i against the value of the list number
    # if the values don't match terminate the loop and return "paragraph" because the block is actually a paragraph
    for i in range(1, len(markdown_list)):
        if markdown_list[i].startswith(f"{i+1}. ") == False:
            return "paragraph"
    return "ordered_list"