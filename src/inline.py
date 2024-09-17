from textnode import TextNode
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    formated = []
    normal = []
    nodes_list = []
    for node in old_nodes:
        if delimiter in node.text:
            node.text = node.text.replace('"', '')# giving me "string" from node.text for some reason
            #print(node.text)
            split_text = node.text.split(delimiter)
            normal.extend(split_text)
            formated.extend(split_text[1::2])
        else:
            nodes_list.append(node)
    if normal != []:
        t = 0
        for i in range(0, len(normal)):
            if normal[i] == formated[t]:
                nodes_list.append(TextNode(f'"{formated[t]}"', f'"{text_type}"'))
                if t < len(formated)-1:
                    t += 1
            else:
                nodes_list.append(TextNode(f'"{normal[i]}"', '"text"'))
    return nodes_list
    

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_link(old_nodes):
    formated = []
    nodes_list = []
    def remove_strings(tupLst, text, i=0):
        text = text.replace('"', '')# giving me "string" from node.text for some reason
        other = text.split(f'[{tupLst[i][0]}]({tupLst[i][1]})')
        nodes_list.append(TextNode(f'"{other[0]}"', '"text"'))
        nodes_list.append(TextNode(f'"{tupLst[i][0]}"', '"link"', f'"{tupLst[i][1]}"'))
        if i+1 >= len(tupLst):
            for i in range(1, len(other)):
                if other[i] != '':
                    nodes_list.append(TextNode(f'"{other[i]}"', '"text"'))
            return nodes_list
        return remove_strings(tupLst, ''.join(other[0:]), i + 1)
    t = 0
    for node in old_nodes:
        imagetups = extract_markdown_links(node.text)
        if imagetups != []:
            formated = imagetups#list of tuple lists
            remove_strings(formated, node.text)
            if t+1 < len(formated):
                t += 1
        else:
            nodes_list.append(node)
    return nodes_list

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_image(old_nodes):
    formated = []
    nodes_list = []
    def remove_strings(tupLst, text, i=0):
        text = text.replace('"', '')# giving me "string" from node.text for some reason
        other = text.split(f'![{tupLst[i][0]}]({tupLst[i][1]})')
        nodes_list.append(TextNode(f'"{other[0]}"', '"text"'))
        nodes_list.append(TextNode(f'"{tupLst[i][0]}"', '"image"', f'"{tupLst[i][1]}"'))
        if i+1 >= len(tupLst):
            for i in range(1, len(other)):
                if other[i] != '':
                    nodes_list.append(TextNode(f'"{other[i]}"', '"text"'))
            return nodes_list
        return remove_strings(tupLst, ''.join(other[0:]), i + 1)
    t = 0
    for node in old_nodes:
        imagetups = extract_markdown_images(node.text)
        if imagetups != []:
            formated = imagetups#list of tuple lists
            remove_strings(formated, node.text)
            if t+1 < len(formated):
                t += 1
        else:
            nodes_list.append(node)
    return nodes_list

def text_to_textnodes(text):
    nodes_list = []
    init = TextNode(text, None)
    nodes_list = split_nodes_delimiter([init], '**', 'bold')
    nodes_list = split_nodes_delimiter(nodes_list, '*', 'italic')
    nodes_list = split_nodes_delimiter(nodes_list, '`', 'code')
    nodes_list = split_nodes_image(nodes_list)
    nodes_list = split_nodes_link(nodes_list)
    return nodes_list