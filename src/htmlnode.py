class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f'HTMLNode (Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props})'
    
    def to_html(self):
        raise NotImplementedError("Feature not added")
    
    def props_to_html(self):
        if self.props == None:
            return None
        props_string = ""
        for prop in self.props:
            element = f' {prop}="{self.props[prop]}"'
            props_string += element
        return props_string

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__()
        self.tag = tag
        self.value = value
        self.props = props
        self.children = None

    def __repr__(self):
        return f'LeafNode (Tag: {self.tag}, Value: {self.value}, Props: {self.props})'
    
    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return self.value
        html_props = self.props_to_html()
        if html_props == None:
            html_string = f'<{self.tag}>{self.value}</{self.tag}'
            return html_string
        return f'<{self.tag}{html_props}>{self.value}</{self.tag}'