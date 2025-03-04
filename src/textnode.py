from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    NORMAL_TEXT = "normal"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK_TEXT = "link"
    IMAGE_TEXT = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    type = text_node.text_type
    if type is TextType.NORMAL_TEXT:
        return LeafNode(tag=None, value=text_node.text)
    if type is TextType.BOLD_TEXT:
        return LeafNode(tag="b", value=text_node.text)
    if type is TextType.ITALIC_TEXT:
        return LeafNode(tag="i", value=text_node.text)
    if type is TextType.CODE_TEXT:
        return LeafNode(tag="code", value=text_node.text)
    if type is TextType.LINK_TEXT:
        return LeafNode(tag="a", value=text_node.text, props={"href":text_node.url})
    if type is TextType.IMAGE_TEXT:
        return LeafNode(tag="img", value='', props={"src":text_node.url, "alt":text_node.text})
    raise ValueError(f"Invalid text type: {text_node.text_type}")