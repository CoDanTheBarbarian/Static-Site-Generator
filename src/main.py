from textnode import TextNode, text_type_bold

def main():
    test_node = TextNode("this is a text node", text_type_bold, "https://boot.dev")
    print(test_node)

if __name__ == "__main__":
    main()