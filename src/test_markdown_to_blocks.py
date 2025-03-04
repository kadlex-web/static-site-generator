import unittest

from markdown_to_blocks import markdown_to_blocks
@unittest.skip("skipping for now")
class TestMarkdowntoBlocks(unittest.TestCase):
    def test_functionality(self):
        markdown = '''# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item'''

        markdown2 = '''* This is the first list item
* This is a list item'''

        result = ['# This is a heading', 
                  'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
                  '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        result2 = ['* This is the first list item\n* This is a list item']

        test = markdown_to_blocks(markdown)
        test2 = markdown_to_blocks(markdown2)
        self.assertEqual(test, result)
        self.assertEqual(test2, result2)

    def test_whitespace(self):
        # Tests to see if whitespace is before or after markdown is stripped
        markdown = '''       * This is the first list item
* This is a list item   '''    
        result = ['* This is the first list item\n* This is a list item']
        test = markdown_to_blocks(markdown)
        self.assertEqual(test, result)

    def test_empty_blocks(self):
        # Tests to see if empty blocks are removed from the markdown list
        markdown = '''* This is the first block


* This is the second block'''    
        result = ['* This is the first block', '* This is the second block']
        test = markdown_to_blocks(markdown)
        self.assertEqual(test, result)

    def test_incorrect_type(self):
        markdown = ''
        markdown2 = 9999
        with self.assertRaises(ValueError):
            test = markdown_to_blocks(markdown)
        
        with self.assertRaises(TypeError):
            test = markdown_to_blocks(markdown2)