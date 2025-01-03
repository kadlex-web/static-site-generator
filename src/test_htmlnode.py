import unittest

from htmlnode import HTMLNode, ParentNode, LeafNode

@unittest.skip("skip the original tests")
class TestHTMLNode(unittest.TestCase):

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

class TestParentNode(unittest.TestCase):
    def test_repr(self):
        # Test repr method to ensure proper output
        parent_node = ParentNode(
        "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],)
        string = 'ParentNode (Tag: p, Children: [LeafNode (Tag: b, Value: Bold text, Props: None), LeafNode (Tag: None, Value: Normal text, Props: None), LeafNode (Tag: i, Value: italic text, Props: None), LeafNode (Tag: None, Value: Normal text, Props: None)], Props: None)'
        self.assertEqual(
            string, repr(parent_node)
        )
        
    def test_multiple_children(self):
        node = ParentNode(
        "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],)
        node_string = node.to_html()
        test_string = f'<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(node_string, test_string)

    def test_no_tag(self):
        # test parent node to make sure it requires (1)tag and (2)children
        node = ParentNode (
            tag=None,
        children= [
            LeafNode("b", "Bold text",)
        ],)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_children(self):
        # test parent node to make sure it requires (1)tag and (2)children
        node_no_kids = ParentNode (
            tag ="p",
            children = None,)
        with self.assertRaises(ValueError):
            node_no_kids.to_html()

    def test_nested_parents(self):
        # Tests parent node to allow for nested parent nodes
        node = ParentNode (
            "div",
            [
                ParentNode("div",[LeafNode("a", "Bold text")])
            ],
        )
        node_string = node.to_html()
        test_string = f'<div><div><a>Bold text</a></div></div>'
        self.assertEqual(node_string, test_string)

    def test_nested_parents2(self):
        # Tested parent node for nested functionality with props
        node = ParentNode (
            "div",
            [
                ParentNode("div",[LeafNode("a", "Click this!", {"href":"www.google.com"}),])
            ],
        )
        node_string = node.to_html()
        test_string = f'<div><div><a href="www.google.com">Click this!</a></div></div>'
        self.assertEqual(node_string, test_string)

if __name__ == "__main__":
    unittest.main()