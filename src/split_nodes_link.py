
import re
from textnode import TextType, TextNode
from extract import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        links = extract_links(images)
        text = re.split(r'[(.*?)\]\((.*?)\)')
        if images is not None or images != "":
            new_nodes.extend([TextNode(links[0],TextType.LINK,links[1])])
        for t in text:
            new_nodes.extend([TextNode(t, TextType.TEXT)])
    return new_nodes
        

