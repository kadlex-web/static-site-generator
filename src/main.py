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

    parent_html = parent_node.to_html()
    print(parent_html)
main()