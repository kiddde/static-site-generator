import re
from textnode import TextType, TextNode
from extract import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        images = extract_markdown_images(node)
        text = re.split(r'\[(.*?)\]\((.*?)\)', node.text)
        if images is not None or images != "":
            new_nodes.extend([TextNode(images[0],TextType.IMAGE,images[1])])
        for t in text:
            new_nodes.extend([TextNode(t, TextType.TEXT)])
    return new_nodes
        

