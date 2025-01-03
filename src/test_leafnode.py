import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_repr(self):
        # tests functionality of the repr method
        node = LeafNode(tag="p", value="This is a html node", props="props")
        string = 'LeafNode (Tag: p, Value: This is a html node, Props: props)'
        self.assertEqual(
            string, repr(node)
        )
    def to_html_with_props(self):
        # checks to make sure function works as designed with props
        props = {
            "href": "https://www.google.com", 
            "target": "_blank", 
            }
        node = LeafNode(tag="a", value='Click this!', props=props)
        node_string = node.to_html()
        test_string = f'<a href="https://www.google.com" target="_blank">Click this!</a>'

        self.assertEqual(node_string, test_string)

    def to_html_without_props(self):
        # checks to make sure function works as designed without props
        node = LeafNode("span", "this is a span")
        node_string = node.to_html()
        test_string = f'<span>this is a span</span>'
        self.assertEqual(node_string, test_string)

    def test_value_error(self):
        # checks to make sure LeafNode triggers a value error when passed no value
        node = LeafNode(value=None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_tag(self):
        node = LeafNode(tag=None, value="There, there little one")
        node_value = node.to_html()
        test_value = "There, there little one"
        self.assertEqual(node_value, test_value)

if __name__ == "__main__":
    unittest.main()