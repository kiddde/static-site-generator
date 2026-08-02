import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_neq(self):
        node1 = TextNode("This is a text node", TextType.PLAIN)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)
    def test_none(self):
        node1 = TextNode("This is a link", TextType.LINK)
        node2 = TextNode("This is a link", TextType.LINK, "localhost")
        self.assertNotEqual(node1, node2)
    def test_same_text(self):
        node1 = TextNode("This is not a link", TextType.BOLD)
        node2 = TextNode("This is not a link", TextType.PLAIN)
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()

