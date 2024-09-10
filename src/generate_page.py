import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path)
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path)
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()
    title = extract_title(markdown_content)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)

def generate_pages_recursive(content_dir_path, template_path, dest_dir_path):
    for file_name in os.listdir(content_dir_path):
        from_path = os.path.join(content_dir_path, file_name)
        to_path = os.path.join(dest_dir_path, file_name)
        if os.path.isfile(from_path):
            to_path = Path(to_path).with_suffix(".html")
            generate_page(from_path, template_path, to_path)
        else:
            generate_pages_recursive(from_path, template_path, to_path)


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2: ]
    raise ValueError("No title found")