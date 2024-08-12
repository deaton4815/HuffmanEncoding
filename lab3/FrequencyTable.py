from lab3.Node import Node


def comparison_key(node: Node):
    return ~node.frequency, len(node.name), node.name


class FrequencyTableQueue:

    def __init__(self, frequency_list):
        self.frequency_queue = []
        self.preorder_traversal = []
        self.create_huffman_tree(frequency_list)

    def create_huffman_tree(self, frequency_list):

        self.initialize_tree(frequency_list)

        while len(self.frequency_queue) > 1:
            self.merge()

        self.traverse_tree(self.frequency_queue[0])

    def initialize_tree(self, frequency_list):
        # initialize tree
        for entry in frequency_list:
            new_node = Node(entry[0], entry[1], None, None)
            self.frequency_queue.append(new_node)
        self.sort_queue()

    def merge(self):
        right = self.frequency_queue.pop()
        left = self.frequency_queue.pop()

        name = left.name + right.name
        frequency = left.frequency + right.frequency

        merged_node = Node(name, frequency, left, right)
        self.frequency_queue.append(merged_node)
        self.sort_queue()

    def sort_queue(self):
        self.frequency_queue.sort(key=comparison_key)

    def traverse_tree(self, node: Node) -> None:
        self.preorder_traversal.append((node.name, node.frequency))

        if node.left:
            self.traverse_tree(node.left)
        if node.right:
            self.traverse_tree(node.right)

    def get_huffman_tree(self):
        return self.frequency_queue

    def get_preorder_traversal(self) -> str:
        return self.preorder_traversal
