import unittest

from textnode import TextNode, TextType
from htmlnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, "www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT, "www.boot.dev")
        self.assertEqual(node, node2)

        node3 = TextNode("This is a text node", TextType.CODE_TEXT, "www.boot.dev")
        node4 = TextNode("This is a text node", TextType.CODE_TEXT, "www.boot.dev")
        self.assertEqual(node3, node4)

    def test_noteq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node3 = TextNode("This is a text node", TextType.BOLD_TEXT, "www.google.com")
        node5 = TextNode("This isn't a text node", TextType.CODE_TEXT)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node, node5)
        self.assertNotEqual(node3, node5)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, "www.boot.dev")
        string = f'TextNode(This is a text node, bold, www.boot.dev)'
        self.assertEqual(
            string, repr(node)
        )

    def test_normal_text_node(self):
        node = TextNode("howdy", TextType.NORMAL_TEXT)
        leaf_node = node.text_node_to_html_node()
        test_string = 'howdy'
        self.assertIsInstance(leaf_node, LeafNode)
        self.assertEqual(leaf_node.to_html(), test_string)

    def test_other_simple_text_nodes(self):
        # Creates three different TextNodes of Bold, Italic, and Code type
        # Converts them to LeafNode and tests the following
            # Are they LeafNode objects and do they output the expected HTML
        bold_node = TextNode("hey there", TextType.BOLD_TEXT)
        italic_node = TextNode("italic node", TextType.ITALIC_TEXT)
        code_node = TextNode("code node", TextType.CODE_TEXT)
        leaf_node = bold_node.text_node_to_html_node()
        italic_leaf_node = italic_node.text_node_to_html_node()
        code_leaf_node = code_node.text_node_to_html_node()

        test_string1 = f'<b>hey there</b>'
        test_string2 = f'<i>italic node</i>'
        test_string3 = f'<code>code node</code>'

        self.assertIsInstance(leaf_node, LeafNode)
        self.assertIsInstance(italic_leaf_node, LeafNode)
        self.assertIsInstance(code_leaf_node, LeafNode)

        self.assertEqual(leaf_node.to_html(), test_string1)
        self.assertEqual(italic_leaf_node.to_html(), test_string2)
        self.assertEqual(code_leaf_node.to_html(), test_string3)

        self.assertNotEqual(bold_node, code_node)

    def test_link_text_node(self):
        node = TextNode("Google.com", TextType.LINK_TEXT, "www.google.com")
        leaf_node = node.text_node_to_html_node()
        test_string = f'<a href="www.google.com">Google.com</a>'
        self.assertEqual(leaf_node.to_html(), test_string)

    def test_image_text_node(self):
        node = TextNode("A picture depicting a large orange cat", TextType.IMAGE_TEXT, "www.google.com")
        leaf_node = node.text_node_to_html_node()
        test_string = f'<img src="www.google.com" alt="A picture depicting a large orange cat"></img>'
        self.assertEqual(leaf_node.to_html(), test_string)

if __name__ == "__main__":
    unittest.main()