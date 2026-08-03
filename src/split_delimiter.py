from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        s = node.text.split(delimiter)
        if len(s) % 2 != 1:
            raise Exception("no closing delimiters")
        else:
            for i in range(len(s)-1):
                new_nodes.extend([TextNode(s[i], TextType.TEXT)])
                new_nodes.extend([TextNode(s[i+1], d)])
        return new_nodes




