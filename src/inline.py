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

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]", text)
    url_matches = re.findall(r'\((.*?)\)', text)
    tups = []
    for i in range(0, len(matches)):
        tups.append((matches[i], url_matches[i]))
    return tups

def split_nodes_link(old_nodes):
    formated = []
    nodes_list = []
    def remove_strings(tupLst, text, i=0):
        new_text = []
        if (f'[{tupLst[i][0]}]({tupLst[i][1]})' not in text):
            return TextNode(text, None)
        other = text.split(f'[{tupLst[i][0]}]({tupLst[i][1]})')
        nodes_list.append(TextNode(f'"{other[0]}"', None))
        nodes_list.append(TextNode(f'"{tupLst[i][0]}"', '"link"', f'"{tupLst[i][1]}"'))
        for string in other:
            if string != other[0]:
                new_text.append(string)
        if i+1 >= len(tupLst):
            return nodes_list
        return remove_strings(tupLst, ''.join(new_text), i + 1)
    
    for node in old_nodes:
        imagetups = extract_markdown_links(node.text)
        formated.append(imagetups)#list of tuple lists
    t = 0
    for node in old_nodes:
        remove_strings(formated[t], node.text)
        t += 1

    return nodes_list

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]", text)
    url_matches = re.findall(r'\((.*?)\)', text)
    tups = []
    for i in range(0, len(matches)):
        tups.append((matches[i], url_matches[i]))
    return tups


def split_nodes_image(old_nodes):
    formated = []
    nodes_list = []
    def remove_strings(tupLst, text, i=0):
        new_text = []
        if (f'![{tupLst[i][0]}]({tupLst[i][1]})' not in text):
            return TextNode(text, None)
        other = text.split(f'![{tupLst[i][0]}]({tupLst[i][1]})')
        nodes_list.append(TextNode(f'"{other[0]}"', None))
        nodes_list.append(TextNode(f'"{tupLst[i][0]}"', '"image"', f'"{tupLst[i][1]}"'))
        for string in other:
            if string != other[0]:
                new_text.append(string)
        if i+1 >= len(tupLst):
            return nodes_list
        return remove_strings(tupLst, ''.join(new_text), i + 1)
    
    for node in old_nodes:
        imagetups = extract_markdown_images(node.text)
        formated.append(imagetups)#list of tuple lists
    t = 0
    for node in old_nodes:
        remove_strings(formated[t], node.text)
        t += 1

    return nodes_list

#node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", 'image',)
#print(split_nodes_image([node]))