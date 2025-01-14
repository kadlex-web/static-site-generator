'''This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'''
'''
[
    TextNode("This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev"),
]
'''
'''
Given a string of raw markdown -- apply each of the split methods to get the appropriate list of text nodes
Order will matter -- I believe it would go as follows:
Bold -> Italic -> Code -> Image -> Link

'''
from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link

def text_to_textnodes(text):
    # Check to make sure the initial text passed to the function is string type, raise error if it isn't
    if isinstance(text, str):
        if len(text) > 0:
            # Create a TextNode object inside a list from the initial raw markdown text
            working_nodes = [TextNode(text, TextType.NORMAL_TEXT)]
            # Perform the first split using the bold delimiter
            first_split = split_nodes_delimiter(working_nodes, "**", TextType.BOLD_TEXT)
            # Perform the second split using the italic delimiter but on the new list of nodes
            second_split = split_nodes_delimiter(first_split, "*", TextType.ITALIC_TEXT)
            # Perform the third split using the code delimiter but on the new list of nodes
            third_split = split_nodes_delimiter(second_split, "`", TextType.CODE_TEXT)
            # In theory we should now have a list of TextNodes which contains the bold, italic, and code text pulled out but the image/link text is unsplit
            fourth_split = split_nodes_image(third_split)
            final_split = split_nodes_link(fourth_split)
            return final_split
        raise ValueError('Markdown text must contain some string data.')
    raise TypeError("Markdown text must be str type to begin conversion to text nodes")