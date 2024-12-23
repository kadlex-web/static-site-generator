import unittest

from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):

    def test_repr(self):
        # tests functionality of the repr method
        node = HTMLNode("p", "This is a html node", "children", "props")
        string = 'HTMLNode (Tag: p, Value: This is a html node, Children: children, Props: props)'
        self.assertEqual(
            string, repr(node)
        )

    def test_props_to_html(self):
        # checks to make sure function works as designed
        props = {
            "href": "https://www.google.com", 
            "target": "_blank", 
            }
        node = HTMLNode(props=props)
        node_string = node.props_to_html()
        test_string = f' href="https://www.google.com" target="_blank"'

        self.assertEqual(node_string, test_string)

    def test_props_to_html2(self):
        # Checks to see what happens when props is empty
        node = HTMLNode("span", "this is a span")
        node_string = node.props_to_html()
        self.assertIsNone(node_string)

if __name__ == "__main__":
    unittest.main()