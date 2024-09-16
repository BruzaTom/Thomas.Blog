from htmlnode import HTMLNode

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
            string += f'{node.to_html()}'
        string += f'</{self.tag}>'
        return string

        