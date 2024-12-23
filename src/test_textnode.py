import unittest

from textnode import TextNode, TextType


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
if __name__ == "__main__":
    unittest.main()