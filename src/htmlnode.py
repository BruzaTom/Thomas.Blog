class HTMLNode:#base html class
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag# An HTMLNode without a tag will just render as raw text
        self.value = value# An HTMLNode without a value will be assumed to have children
        self.children = children# An HTMLNode without children will be assumed to have a value
        self.props = props# An HTMLNode without props simply won't have any attributes

    def to_html(self):
        raise NotImplementedError# Child classes will override this method to render themselves as HTML.
    
    def props_to_html(self):
        string = ''
        for prop in self.props:
            string += f' {prop}="{self.props[prop]}"'
        return string
    
    def __eq__(self, HTMLNode):
        if (self.tag == HTMLNode.tag) & (self.value == HTMLNode.value) & (self.children == HTMLNode.children) & (self.props == HTMLNode.props):
            return True
        return False

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
    
