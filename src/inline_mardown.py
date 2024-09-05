from textnode import TextNode, text_type_bold, text_node_to_html_node, text_type_code, text_type_image, text_type_italic, text_type_link, text_type_text
import re

def text_to_text_nodes(text):
     nodes = [TextNode(text, text_type_text)]
     nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
     nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
     nodes = split_nodes_delimiter(nodes, "`", text_type_code)
     nodes = split_nodes_image(nodes)
     nodes = split_nodes_link(nodes)
     return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_node_list = []

    for node in old_nodes:
        if node.text_type != text_type_text:
            new_node_list.append(node)
            continue
        split_nodes = []
        section = node.text.split(delimiter)

        if len(section) % 2 == 0:
            raise ValueError("no closing delimiter found")
        for i in range(len(section)):
            if section[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(section[i], text_type_text))
            else:
                split_nodes.append(TextNode(section[i], text_type))
        new_node_list.extend(split_nodes)
    return new_node_list

def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        image_extraction = extract_markdown_images(old_node.text)
        updated_node_text = old_node.text
        if len(image_extraction) == 0:
            new_nodes.append(old_node)
            continue
        for image_alt, image_url in image_extraction:
            split_text = updated_node_text.split(f"![{image_alt}]({image_url})", 1)
            if len(split_text) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], text_type_text))
            new_nodes.append(TextNode(image_alt, text_type_image, image_url))
            updated_node_text = split_text[1]
        if updated_node_text != "":
            new_nodes.append(TextNode(updated_node_text, text_type_text))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        link_extraction = extract_markdown_links(old_node.text)
        updated_node_text = old_node.text
        if len(link_extraction) == 0:
            new_nodes.append(old_node)
            continue
        for anchor_text, link_url in link_extraction:
            split_text = updated_node_text.split(f"[{anchor_text}]({link_url})", 1)
            if len(split_text) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], text_type_text))
            new_nodes.append(TextNode(anchor_text, text_type_link, link_url))
            updated_node_text = split_text[1]
        if updated_node_text != "":
            new_nodes.append(TextNode(updated_node_text, text_type_text))
    return new_nodes
