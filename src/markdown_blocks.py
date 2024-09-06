import re
from htmlnode import ParentNode
from inline_mardown import text_to_text_nodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        filtered_blocks.append(block.strip())
    return filtered_blocks

def block_to_block_type(block):
    if re.match(r"^#{1,6} ", block):
        return block_type_heading
    lines = block.split("\n")
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    quote = True
    unordered_list = True
    for line in lines:
        if not line.startswith(">"):
            quote = False
        if not line.startswith("* ") and not line.startswith("- "):
            unordered_list = False
    if quote:
        return block_type_quote
    if unordered_list:
        return block_type_ulist
    ordered_list = True
    for i, line in enumerate(lines):
        if not line.startswith(f"{(i + 1)}. "):
            ordered_list = False
    if ordered_list:
        return block_type_olist
    return block_type_paragraph

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        htmlnode = block_to_htmlnode(block)
        children.append(htmlnode)
    return ParentNode("div", children, None)

def block_to_htmlnode(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_htmlnode(block)
    if block_type == block_type_heading:
        return heading_to_htmlnode(block)
    if block_type == block_type_code:
        return code_to_htmlnode(block)
    if block_type == block_type_quote:
        return quote_to_htmlnode(block)
    if block_type == block_type_olist:
        return ordered_list_to_htmlnode(block)
    if block_type == block_type_ulist:
        return unordered_list_to_htmlnode(block)
    raise ValueError("Invalid block type")

def text_to_children(text):
    text_nodes = text_to_text_nodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_htmlnode(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_htmlnode(block):
    i = 0
    for char in block:
        if char == "#":
            i += 1
        else:
            break
    if i + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {i}")
    text = block[i + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{i}", children)

def code_to_htmlnode(block):
    if not block.startswith("```") and not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4: -3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", code)

def quote_to_htmlnode(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    quote = " ".join(new_lines)
    children = text_to_children(quote)
    return ParentNode("blockquote", children)

def ordered_list_to_htmlnode(block):
    lines = block.split("\n")
    items = []
    for line in lines:
        text = line[3:]
        children = text_to_children(text)
        items.append(ParentNode("li", children))
    return ParentNode("ol", items)

def unordered_list_to_htmlnode(block):
    lines = block.split("\n")
    items = []
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        items.append(ParentNode("li", children))
    return ParentNode("ul", items)