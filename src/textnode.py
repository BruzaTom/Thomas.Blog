from leafnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, TextNode):
        if (self.text == TextNode.text) & (self.text_type == TextNode.text_type) & (self.url == TextNode.url):
            return True
        return False
    
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
    
    def text_node_to_html_node(text_node):
        type = [
            "text",
            "bold",
            "italic",
            "code",
            "link",
            "image"
        ]

        if text_node.text_type not in type:
            raise ValueError(f'text type {text_node.text_type} not supported.')
        if text_node.text_type == type[0]:
            return LeafNode(None, text_node.text)
        if text_node.text_type == type[1]:
            return LeafNode('b', text_node.text)
        if text_node.text_type == type[2]:
            return LeafNode('i', text_node.text)
        if text_node.text_type == type[3]:
            return LeafNode('code', text_node.text)
        if text_node.text_type == type[4]:
            return LeafNode('a', text_node.text, {"href":text_node.url})
        if text_node.text_type == type[5]:
            return LeafNode('img', '', {'src': text_node.url, 'alt': text_node.text})
        