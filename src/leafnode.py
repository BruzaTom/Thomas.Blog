from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        if self.tag in 'pibh1h2h3h4h5h6blockquotecodeli':
            return f'<{self.tag}>{self.value}</{self.tag}>'
        if self.tag == 'a':
            if self.props == None:
                raise ValueError
            return f'<a{self.props_to_html()}>{self.value}</a>'
        if self.tag == 'img':
            return f'<img{self.props_to_html()}>'
        #use parent node for ul or ol
        #if self.tag in 'ulol':
        #    string = f'<{self.tag}>'
        #    for prop in self.props:
        #        string += f'<li>{self.props[prop]}</li>'
        #    string += f'</{self.tag}>'
        #    return string
        

        