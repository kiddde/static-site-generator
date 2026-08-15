import unittest
from textnode import TextNode, TextType
from text_to_text_nodes import text_to_text_nodes
from split_nodes_image import split_nodes_image 
from split_nodes_link import split_nodes_link
from split_delimiter import split_nodes_delimiter
class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_neq(self):
        node1 = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)
    def test_none(self):
        node1 = TextNode("This is a link", TextType.LINK)
        node2 = TextNode("This is a link", TextType.LINK, "localhost")
        self.assertNotEqual(node1, node2)
    def test_same_text(self):
        node1 = TextNode("This is not a link", TextType.BOLD)
        node2 = TextNode("This is not a link", TextType.TEXT)
        self.assertNotEqual(node1, node2)
    def test_text_to_textnodes(self):
        nodes = text_to_text_nodes(
            "This is **text** with an _italic_ word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes,
        )


if __name__ == "__main__":
    unittest.main()

