from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UL = "unordered_list"
    OL = "ordered_list"
    
def block_to_block_type(md):
    regex = r"^#{1,6}\s"
    matches = re.findall(regex, md)
    if matches:
        return BlockType.HEADING
    if md[0:4] == '```\n' and md[-3:] == '```':
        return BlockType.CODE
    md_list = md.split('\n')
    quote = True
    for item in md_list:
        if item[0] != ">":
            quote = False
    if quote:
        return BlockType.QUOTE
    ul = True
    for item in md_list:
        if item[0:2] != "- ":
            ul = False
    if ul:
        return BlockType.UL
    if md.startswith("1. "):
        index = 1
        for item in md_list:
            if not item.startswith(f"{index}. "):
                return BlockType.PARAGRAPH
            index += 1
        return BlockType.OL
    return BlockType.PARAGRAPH

