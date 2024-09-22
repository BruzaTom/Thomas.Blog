from htmlnode import HTMLNode
from textnode import TextNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError('no tag in ParentNode')
        if self.children == None:
            raise ValueError('no children in ParentNode')
        string = f'<{self.tag}>'
        for node in self.children:
            if isinstance(node, TextNode):
                node = TextNode.text_node_to_html_node(node)
            html = node.to_html()
            string += f'{html}'
        string += f'</{self.tag}>'
        return string
    
    def __repr__(self):
        return f'ParentNode({self.tag}, {self.value}, {self.children}, {self.props})'

        