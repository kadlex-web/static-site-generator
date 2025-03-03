from block_to_block_type import *
from markdown_to_blocks import *
from htmlnode import *
from textnode import TextNode
from text_to_textnodes import text_to_textnodes

def heading_tag(block):
    heading_value = block.count('#')
    return f'h{heading_value}'

def code_tag(block):
    pass

def unordered_list_element(block):
    split_blocks = block.split("\n")
    node_list = []
    for line in split_blocks:
        trimmed_line = line.split(" ", 1)[1]
        node = LeafNode(tag='li',value=trimmed_line)
        node_list.append(node)
    return node_list

def ordered_list_element(block):
    split_blocks = block.split("\n")
    node_list = []
    for line in split_blocks:
        trimmed_line = line.split(" ", 1)[1]
        node = LeafNode(tag='li',value=trimmed_line)
        node_list.append(node)
    return node_list


def text_to_children(block):
    list_of_text_nodes = text_to_textnodes(block)
    list_of_html_nodes= []
    for text_node in list_of_text_nodes:
        list_of_html_nodes.append(text_node.text_node_to_html_node())
    return list_of_html_nodes

'''
Heading -- DONE
Code 
Quote
Unordered List - DONE
Ordered List - DONE
Paragraph -- DONE

After helper function figures out the tag -- we need to find all the children within the block

function needs to end by returning a master HTML node with has all the other nodes in it.
return HTMLNode(div,children_node_list) -- does not need any value assigned to it (it's a div) but needs to contain all child nodes
building up the html_node_list is essentially creating the children structure

NEED TO DO:
need to look at text and see if there's any in-line in it. in particular the block quote contains markdown
need to fix blockquote to trim the blockquote characters
need to write condition for code block
'''
def markdown_to_html_node(markdown):
    markdown_to_blocks_list = markdown_to_blocks(markdown)
    node_list = []
    # Iterate through all of the blocks that were found in the markdown and construct a HTMLNode based on certain conditions
    for block in markdown_to_blocks_list:
        # Computes the type of block we are dealing with
        block_type = block_to_block_type(block)
        # If the block type is a heading - function determines what heading level it is (1-6)
        if block_type == 'heading':
            tag = heading_tag(block)
            block_text = block.split(" ", 1)[1]
            node = HTMLNode(tag, block_text)
            node_list.append(node)

        elif block_type == 'quote':
            tag = 'blockquote'
            block_text = block.split(" ", 1)[1]
            node = HTMLNode(tag, block)
            node_list.append(node)

        elif block_type == 'code':
            list_elements = code_tag(block)

        elif block_type == "unordered_list":
            list_elements = unordered_list_element(block)
            node = ParentNode(tag='ul', children=list_elements)
            node_list.append(node)

        elif block_type == "ordered_list":
            list_elements = ordered_list_element(block)
            node = ParentNode(tag='ol', children=list_elements)
            node_list.append(node)
        else:
            tag = 'p'
            l = text_to_children(block)
            node = ParentNode(tag=tag, children=l)
            node_list.append(node)
    return node_list
    return HTMLNode('div',node_list)

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

result = markdown_to_html_node(markdown)
for node in result:
    print(f'{node}\n')