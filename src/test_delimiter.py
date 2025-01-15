import unittest

from split_delimiter import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType
@unittest.skip("skip for now")
class TestSplitDelimiter(unittest.TestCase):
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
@unittest.skip("skip for now")
class TestExtractMarkdownImages(unittest.TestCase):
    def test_functionality(self):
        img_text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        img_markdown = extract_markdown_images(img_text)
        correct_result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(img_markdown, correct_result)

    def test_bad_markdown(self):
        # Tests if None type is passed to function
        with self.assertRaises(ValueError):
            img_text = None
            img_markdown = extract_markdown_images(img_text)
            
        # Tests if non-string is passed to function
        with self.assertRaises(TypeError):
            img_text = 1
            img_markdown = extract_markdown_images(img_text)
@unittest.skip("skip for now")
class TestExtractMarkdownLinks(unittest.TestCase):
    def test_functionality(self):
        link_text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        link_markdown = extract_markdown_links(link_text)
        correct_result = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(link_markdown, correct_result)
        
if __name__ == "__main__":
    unittest.main()