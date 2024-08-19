from typing import List

from lab3.FrequencyTable import FrequencyTableQueue
from lab3.Node import Node


class HuffmanEncoder:

    def __init__(self, clear_text: str, huffman_queue: FrequencyTableQueue):
        self.clear_text = clear_text
        self.huffman_tree = huffman_queue.get_huffman_tree()
        self.encoded = self.encode_clear_text()

    def encode_clear_text(self) -> List[str]:

        code = []

        for line in self.clear_text:
            code_line = str()
            for char in line:
                if char.isalpha():
                    char = char.upper()
                    code_line = self.get_char_code(char, self.huffman_tree[0], code_line)
            code.append(code_line)

        return code

    def get_char_code(self, char: str, node: Node, code: str) -> str:

        if char == node.name:
            return code
        elif char in node.left.name:
            code += '0'
            code = self.get_char_code(char, node.left, code)
            return code
        elif char in node.right.name:
            code += '1'
            coe = self.get_char_code(char, node.right, code)
            return code

    def get_encoded_messages(self) -> List[str]:
        return self.encoded
