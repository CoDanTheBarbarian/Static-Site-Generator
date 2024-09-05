import re

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
        return "heading"
    lines = block.split("\n")
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].endswith("```"):
        return "code"
    quote = True
    unordered_list = True
    for line in lines:
        if not line.startswith(">"):
            quote = False
        if not line.startswith("* ") and not line.startswith("- "):
            unordered_list = False
    if quote:
        return "quote"
    if unordered_list:
        return "unordered_list"
    ordered_list = True
    for i, line in enumerate(lines):
        if not line.startswith(f"{(i + 1)}. "):
            ordered_list = False
    if ordered_list:
        return "ordered_list"
    return "paragraph"
