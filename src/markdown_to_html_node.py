from block_to_block_types import BlockType, block_to_block_type
from markdown_to_blocks import markdown_to_blocks
from html_node import HTMLNode
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        type = block_to_block_type(block)
        match type:
            case BlockType.HEADING:
                size = 0
                for char in block:
                    if char == "#":
                        size += 1
                    else:
                        break
                tag = f'h{size}'
                




