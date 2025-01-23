import unittest

from block_to_block_type import *

class TestBlocktoBlockType(unittest.TestCase):
    def test_functionality(self):
        # Heading Test
        markdown1 = "### Heading"
        self.assertEqual(block_to_block_type(markdown1), "heading")
        # Code Test
        markdown2 = "```Code block incoming```"
        self.assertEqual(block_to_block_type(markdown2), "code")
        # Quote Test
        markdown3 = '''> YOWZA\n> Next!\n> Finallllly'''
        self.assertEqual(block_to_block_type(markdown3), "quote")
        # Unordered List Test
        markdown4 = '''- this list\n- isn't really\n- in order'''
        self.assertEqual(block_to_block_type(markdown4), "unordered_list")
        # Ordered List Test
        markdown4 = '''1. but this list\n2. is really\n3. in order'''
        self.assertEqual(block_to_block_type(markdown4), "ordered_list")
        # Paragraph List Test
        markdown5 = "#####Just a regular old paragraph"
        self.assertEqual(block_to_block_type(markdown5), "paragraph")

    def test_functionality2(self):
        # tougher test
        markdown1 = '''#### Heading 4
        ```with code ticks in it? and a list character >'''
        self.assertEqual(block_to_block_type(markdown1), "heading")

if __name__ == "__main__":
    unittest.main()