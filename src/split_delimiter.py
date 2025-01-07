from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.NORMAL_TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(image_text):
    if image_text == None:
        raise ValueError("Must pass some markdown text to be converted")
    
    if isinstance(image_text, str):
        alt_text_pattern = r"(?<=!\[).*?(?=\])"
        url_pattern = r"(?<=\().*?(?=\))"
        alt_matches = re.findall(alt_text_pattern, image_text)
        url_matches = re.findall(url_pattern, image_text)
        markdown_tuples = list(zip(alt_matches, url_matches))
        return markdown_tuples
    raise TypeError("Markdown must be str type")

def extract_markdown_links(link_text):
    if link_text == None:
        raise ValueError("Must pass some markdown text to be converted")
    anchor_text_pattern = r"(?<=\[).*?(?=\])"
    url_pattern = r"(?<=\().*?(?=\))"
    anchor_matches = re.findall(anchor_text_pattern, link_text)
    url_matches = re.findall(url_pattern, link_text)
    markdown_tuples = list(zip(anchor_matches, url_matches))
    return markdown_tuples