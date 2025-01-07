import unittest

from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):
    def test_delimiter_single_node(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL_TEXT)
        node2 = TextNode('This is text with a **bold block** word', TextType.NORMAL_TEXT)

        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        new_nodes2 = split_nodes_delimiter([node2], "**", TextType.BOLD_TEXT)

        new_nodes_test = [
            TextNode("This is text with a ", TextType.NORMAL_TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" word", TextType.NORMAL_TEXT),
        ]

        new_nodes_test2 = [
            TextNode("This is text with a ", TextType.NORMAL_TEXT),
            TextNode("bold block", TextType.BOLD_TEXT),
            TextNode(" word", TextType.NORMAL_TEXT),
        ]
        self.assertEqual(new_nodes, new_nodes_test)
        self.assertNotEqual(new_nodes, new_nodes2)
        self.assertEqual(new_nodes_test2, new_nodes2)

    def test_delimiter_multiple_nodes(self):
        node_list = [
            TextNode("This is text with a `code block` word", TextType.NORMAL_TEXT),
            TextNode("This is text with a *italic block* word", TextType.NORMAL_TEXT),
            TextNode("This is text with a **bold block** word", TextType.NORMAL_TEXT),
            TextNode("This is text with a *italic block* word", TextType.NORMAL_TEXT),            
        ]
        new_nodes = split_nodes_delimiter(node_list, "**", TextType.BOLD_TEXT)

        new_node_test = [
            TextNode("This is text with a `code block` word", TextType.NORMAL_TEXT),
            TextNode("This is text with a *italic block* word", TextType.NORMAL_TEXT),
            TextNode("This is text with a ", TextType.NORMAL_TEXT),
            TextNode("bold block", TextType.BOLD_TEXT),
            TextNode(" word", TextType.NORMAL_TEXT),
            TextNode("This is text with a *italic block* word", TextType.NORMAL_TEXT),            
        ]
        self.assertEqual(new_nodes, new_node_test)

if __name__ == "__main__":
    unittest.main()