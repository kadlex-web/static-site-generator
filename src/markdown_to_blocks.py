'''Takes raw markdown text as a string and converts it to a list of block strings
A block is a piece of text between line breaks
Might be error in here where the ValueError is flagging
This code works:
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks
'''
def markdown_to_blocks(markdown):
    if isinstance(markdown, str):
        if markdown != '':
            markdown_blocks = []
            current_markdown = markdown.split("\n\n")
            for element in current_markdown:
                if element != '':
                    markdown_blocks.append(element.strip())
            return markdown_blocks
        raise ValueError('Markdown must contain some text')
    raise TypeError("Markdown must be string type")

markdown = '''# This is a heading


This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item'''

result = markdown_to_blocks(markdown)
