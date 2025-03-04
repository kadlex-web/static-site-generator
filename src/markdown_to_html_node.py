from block_to_block_type import *
from markdown_to_blocks import *
from htmlnode import *
from textnode import *
from text_to_textnodes import text_to_textnodes

def heading_tag(block):
    heading_value = block.count('#')
    return f'h{heading_value}'

def unordered_list_element(block):
    split_blocks = block.split("\n")
    node_list = []
    for line in split_blocks:
        if line.strip():
            trimmed_line = line.split(" ", 1)[1]
            child_nodes = text_to_children(trimmed_line)
            node = ParentNode(tag='li',children=child_nodes)
            node_list.append(node)
    return node_list

def ordered_list_element(block):
    split_blocks = block.split("\n")
    node_list = []
    for line in split_blocks:
        if line.strip():
            trimmed_line = line.split(" ", 1)[1]
            child_nodes = text_to_children(trimmed_line)
            node = ParentNode(tag='li',children=child_nodes)
            node_list.append(node)
    return node_list

'''Function which takes markdown text and returns a list of HTML Nodes representing the in-line contained within'''
def text_to_children(text):
    list_of_text_nodes = text_to_textnodes(text)
    list_of_html_nodes = []
    for text_node in list_of_text_nodes:
        list_of_html_nodes.append(text_node_to_html_node(text_node))
    return list_of_html_nodes
    
'''Main Function'''
def markdown_to_html_node(markdown):
    markdown_to_blocks_list = markdown_to_blocks(markdown)
    node_list = []
    # Iterate through all of the blocks that were found in the markdown and construct a HTMLNode based on certain conditions
    for block in markdown_to_blocks_list:
        # Checks for empty blocks and does not iterate over them via continue. otherwise processing continues
        if not block.strip():
            continue
        # Computes the type of block we are dealing with
        block_type = block_to_block_type(block)

        if block_type == "code":
            lines = block.split("\n")
            # Skip the first and last lines (they contain ```)
            code_lines = lines[1:-1]
            
            # Remove leading whitespace from each line
            code_lines = [line.lstrip() for line in code_lines]
            
            # Add a trailing newline to match the expected output
            code_content = "\n".join(code_lines) + "\n"
            
            # Create a TextNode with the raw code content
            text_node = TextNode(code_content, TextType.NORMAL_TEXT)
            code_node = text_node_to_html_node(text_node)
            pre_node = ParentNode("pre", [ParentNode("code", [code_node])])
            node_list.append(pre_node)

        # If the block type is a heading - function determines what heading level it is (1-6)
        elif block_type == 'heading':
            tag = heading_tag(block)
            block_text = block.split(" ", 1)[1]
            child_nodes = text_to_children(block_text)
            node = ParentNode(tag, child_nodes)
            node_list.append(node)

        # If the block is a quote - split at the delimiter and create a blockquote HTMLNode
        elif block_type == 'quote':
            # Remove the '>' prefix from each line
            lines = block.split("\n")
            quote_content = []
            for line in lines:
                if line.startswith('>'):
                    # Remove '>' and one space if present
                    line = line[1:]
                    if line.startswith(' '):
                        line = line[1:]
                    quote_content.append(line)
    
            # Join the lines back together and process for inline markdown
            processed_content = ' '.join(quote_content)
            child_nodes = text_to_children(processed_content)
            node = ParentNode('blockquote', child_nodes)
            node_list.append(node)

        elif block_type == "unordered_list":
            list_elements = unordered_list_element(block)
            node = ParentNode(tag='ul', children=list_elements)
            node_list.append(node)

        elif block_type == "ordered_list":
            list_elements = ordered_list_element(block)
            node = ParentNode(tag='ol', children=list_elements)
            node_list.append(node)
            
        elif block_type == "paragraph":
            tag = 'p'
            # Clean up the text: trim and normalize whitespace
            clean_text = block.strip().replace("\n", " ")
            # Normalize multiple spaces to single spaces (optional but good practice)
            while "  " in clean_text:
                clean_text = clean_text.replace("  ", " ")
            
            l = text_to_children(clean_text)
            node = ParentNode(tag=tag, children=l)
            node_list.append(node)
    
    return ParentNode('div',node_list)

markdown ='''# Esset artifices

## Celebrandaque omni alimenta Tiberinus erat congesta simul

Lorem markdownum fecit Charybdis numina exstitit tempora tulit telum diffugiunt
relinquet, [trepidantem](http://eandem.org/)? Pictae istis, quod
[atque](http://occultat.net/) signisque coniunx aliquisque pestis petunt nec
*maius* minus laudatis pectore materiam. A flamina ademptam quoque tu ille
[Graiumque dei oscula](http://www.inseris.io/aliis.html) hospite quaeque tumet
nec, deae.

1. Tum hanc lupus unum ut inter in
2. Ternis in signis et piscem poteram
3. Aut ad aevum Colophonius quae luridus gloria

> Tendere sine ut omnia iuvenes, sub aures pararet amplectitur **verba**.
> Vigoris sint foret pignora moratur falsisque stetimus, in Iovem cerata lecto
> altum. Meorum volat cognoscere Polypemonis omnes nemus autem. *Fata gratia*
> hac cum exhalat colla. Est spoliare, Iovis, correptus et oris, has quid,
> Telamone in.

* Eurytidos haec Siculique
* Cortex nympharum et cupidine damus illiusque pro
* Neve depositum gerunt rura abest iunctarum Ampycides
* Quadripedis divae pavonibus
'''