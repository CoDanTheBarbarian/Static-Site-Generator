class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        output = ""
        if not self.props:
            return output
        for key, value in self.props.items():
            output += f' {key}="{value}"'
        return output
    
    def __repr__(self):
        props_text = self.props_to_html() if self.props else "{}"
        children_text = "[" + ", ".join(repr(child) for child in self.children) + "]"
        return f'HTMLNode(tag="{self.tag}", value="{self.value}", children: {children_text}, props={props_text})'
    
"""
This is the way it was done in the solution code.
I wasn't sure if simply calling the self values in the returned f string for repr would produce the desired result.
I tried to account for odd situations, maybe I over coded?
def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
"""