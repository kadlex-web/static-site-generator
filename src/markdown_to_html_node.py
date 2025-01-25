from block_to_block_type import *
from markdown_to_blocks import *
from htmlnode import *
from textnode import TextNode
from text_to_textnodes import text_to_textnodes

def heading_tag(block):
    heading_value = block.count('#')
    return f'h{heading_value}'

# Need to figure out what the tag is and if the node has any possible children
def markdown_to_html_node(markdown):
    markdown_to_blocks_list = markdown_to_blocks(markdown)
    node_list = []
    html_node_list = []
    for block in markdown_to_blocks_list:
        block_type = block_to_block_type(block)
        if block_type == "heading":
            tag = heading_tag(block)
            node = HTMLNode(tag, block)
            html_node_list.append(node)
        else:
            tag = 'p'
            node = HTMLNode(tag, block)
            html_node_list.append(node)
    for node in node_list:
        print(f"{node}\n")
    return html_node_list

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
3. Aut ad aevum Colophonius quae luridus gloria'''

b = markdown_to_html_node(markdown)
print(b)