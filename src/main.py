from textnode import *
from htmlnode import *

def main():
    parent_node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

    test_text_node = TextNode("howdy", TextType.NORMAL_TEXT, "www.google.com")
    print(test_text_node.text_node_to_html_node())

main()