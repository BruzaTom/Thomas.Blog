from textnode import TextNode
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    formated = []
    normal = []
    nodes_list = []
    for node in old_nodes:
        split_text = node.text.split(delimiter)
        normal.extend(split_text)
        formated.extend(split_text[1::2])
    t = 0
    for i in range(0, len(normal)):
        if normal[i] == formated[t]:
            nodes_list.append(TextNode(f'"{formated[t]}"', text_type))
            if t < len(formated)-1:
                t += 1
        else:
            nodes_list.append(TextNode(f'"{normal[i]}"', None))
    return nodes_list

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]", text)
    url_matches = re.findall(r'\((.*?)\)', text)
    tups = []
    for i in range(0, len(matches)):
        tups.append((matches[i], url_matches[i]))
    return tups

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]", text)
    url_matches = re.findall(r'\((.*?)\)', text)
    tups = []
    for i in range(0, len(matches)):
        tups.append((matches[i], url_matches[i]))
    return tups