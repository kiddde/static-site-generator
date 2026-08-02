import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_create(self):
        node1 = HTMLNode() 
        assert node1.tag == None and node1.value == None and node1.props == None and node1.children == None
    def test_repr(self):
        node1 = HTMLNode("p", "Some txt")
        node2 = HTMLNode("a", "text in link", props={"href": "https://boot.dev"}, children=None)
        print(node1)
        print(node2)
    def test_props(self):
        pass
if __name__ == "__main__":
    unittest.main()
