def markdown_to_blocks(markdown):
    list_of_lines = markdown.split('\n\n')   
    result = []
    for line in list_of_lines:
        if line == "":
            continue
        result.append(line.strip())
    return result
