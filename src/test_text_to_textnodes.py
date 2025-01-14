import unittest

from textnode import TextNode, TextType
from text_to_textnodes import *

class TestTextNode(unittest.TestCase):
    # Tests conversion of raw markdown to node list where markdown contains all node types
    def test_functionality(self):
        text = 'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        result = [
                    TextNode("This is ", TextType.NORMAL_TEXT),
                    TextNode("text", TextType.BOLD_TEXT),
                    TextNode(" with an ", TextType.NORMAL_TEXT),
                    TextNode("italic", TextType.ITALIC_TEXT),
                    TextNode(" word and a ", TextType.NORMAL_TEXT),
                    TextNode("code block", TextType.CODE_TEXT),
                    TextNode(" and an ", TextType.NORMAL_TEXT),
                    TextNode("obi wan image", TextType.IMAGE_TEXT, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and a ", TextType.NORMAL_TEXT),
                    TextNode("link", TextType.LINK_TEXT, "https://boot.dev"),
        ]  
        test = text_to_textnodes(text)
        self.assertEqual(result, test)

    def test_functionality2(self):
        # Tests conversion of raw markdown to node list which contains two link blocks
        text = 'This is **text** with an *italic* word and a `code block` and an [link](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        result = [
                    TextNode("This is ", TextType.NORMAL_TEXT),
                    TextNode("text", TextType.BOLD_TEXT),
                    TextNode(" with an ", TextType.NORMAL_TEXT),
                    TextNode("italic", TextType.ITALIC_TEXT),
                    TextNode(" word and a ", TextType.NORMAL_TEXT),
                    TextNode("code block", TextType.CODE_TEXT),
                    TextNode(" and an ", TextType.NORMAL_TEXT),
                    TextNode("link", TextType.LINK_TEXT, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and a ", TextType.NORMAL_TEXT),
                    TextNode("link", TextType.LINK_TEXT, "https://boot.dev"),
        ]
        test = text_to_textnodes(text)
        self.assertEqual(test, result)

    def test_functionality3(self):
        # Tests conversion of raw markdown to node list where markdown does not contain Bold, Italic, or Code text
        text = 'This is text with a ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        result = [
                    TextNode("This is text with a ", TextType.NORMAL_TEXT),
                    TextNode("obi wan image", TextType.IMAGE_TEXT, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and a ", TextType.NORMAL_TEXT),
                    TextNode("link", TextType.LINK_TEXT, "https://boot.dev"),
        ]
        test = text_to_textnodes(text)
        self.assertEqual(test, result)

    def test_functionality4(self):
        # Tests conversion of raw markdown to node list where markdown contains only Bold, Italic, or Code text
        text = 'This is **text** with an *italic* word and a `code block`'
        result = [
                    TextNode("This is ", TextType.NORMAL_TEXT),
                    TextNode("text", TextType.BOLD_TEXT),
                    TextNode(" with an ", TextType.NORMAL_TEXT),
                    TextNode("italic", TextType.ITALIC_TEXT),
                    TextNode(" word and a ", TextType.NORMAL_TEXT),
                    TextNode("code block", TextType.CODE_TEXT),
        ]
        test = text_to_textnodes(text)
        self.assertEqual(test, result)

    def test_functionality5(self):
        # Tests to see if raw markdown contain only text returns a node list of only one text node
        text = 'This is just text!'
        result = [
                    TextNode("This is just text!", TextType.NORMAL_TEXT),
        ]
        test = text_to_textnodes(text)
        self.assertEqual(test, result)

    def test_incorrect_type(self):
        # Tests function to make sure it raises appropriate errors if passed incorrect type or raw markdown which is an empty string
        text = ['This is a bold word text **text**']
        with self.assertRaises(TypeError):
            test = text_to_textnodes(text)
        text2 = ""
        with self.assertRaises(ValueError):
            test = text_to_textnodes(text2)        

if __name__ == "__main__":
    unittest.main()