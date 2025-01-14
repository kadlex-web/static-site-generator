'''
You're correctly handling empty input lists with a ValueError
You return the original nodes if no links are found
You're properly splitting the text around links
You're only creating nodes when there's actual content (no empty nodes)
You've fixed the logic for handling link nodes vs surrounding text
You've cleaned up the final text handling
'''

import unittest
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
    def test_split_link(self):
        pass

    def test_split_image(self):
        pass


if __name__ == "__main__":
    unittest.main()