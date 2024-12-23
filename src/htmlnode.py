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