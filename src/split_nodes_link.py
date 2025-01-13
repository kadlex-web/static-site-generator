from split_delimiter import extract_markdown_links
from textnode import TextNode, TextType

def split_nodes_link(old_nodes):
    if len(old_nodes) == 0:
        raise ValueError("Node List must contain at least one element.")
    
    new_nodes = []
    for node in old_nodes:
        node_text = node.text
        link_tuples = extract_markdown_links(node.text)
        if link_tuples == []:
            return old_nodes
        
        for pair in link_tuples:
            link_alt, link_url = pair
            sections = node_text.split(f"[{link_alt}]({link_url})", 1)
            if sections[0]:
                new_node = TextNode(sections[0], TextType.NORMAL_TEXT)
                new_nodes.append(new_node)
            if link_alt:
                link_node = TextNode(link_alt, TextType.LINK_TEXT, link_url)
                new_nodes.append(link_node)
            node_text = sections[1]
    if node_text:
        final_node = TextNode(node_text, TextType.NORMAL_TEXT)
        new_nodes.append(final_node)
    return new_nodes