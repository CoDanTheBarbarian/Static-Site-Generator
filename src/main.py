from textnode import TextNode, text_type_bold, text_type_link, text_type_code, text_type_image, text_type_italic, text_type_text

def main():
    test_node = TextNode("this is a text node", text_type_bold, "https://boot.dev")
    print(test_node)

if __name__ == "__main__":
    main()