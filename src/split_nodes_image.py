from split_delimiter import extract_markdown_images
from textnode import TextNode, TextType

def split_nodes_image(old_nodes):
    if len(old_nodes) == 0:
        raise ValueError("Node List must contain at least one element.")
    
    new_nodes = []
    for node in old_nodes:
        node_text = node.text
        link_tuples = extract_markdown_images(node.text)
        if link_tuples == []:
            return old_nodes
        
        for pair in link_tuples:
            img_alt, img_url = pair
            sections = node_text.split(f"![{img_alt}]({img_url})", 1)
            if sections[0]:
                new_node = TextNode(sections[0], TextType.NORMAL_TEXT)
                new_nodes.append(new_node)
            if img_alt:
                link_node = TextNode(img_alt, TextType.IMAGE_TEXT, img_url)
                new_nodes.append(link_node)
            node_text = sections[1]
    if node_text:
        final_node = TextNode(node_text, TextType.NORMAL_TEXT)
        new_nodes.append(final_node)
    return new_nodes

node = TextNode(
    "This is text with two images. First ![to boot dev](https://www.boot.dev) Second ![to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.NORMAL_TEXT,
)

result = split_nodes_image([node])
print(result)