from lab3.Node import Node


def comparison_key(node: Node):
    return ~node.frequency, len(node.name), node.name


class FrequencyTableQueue:

    def __init__(self, frequency_list):
        self.frequency_queue = []
        self.create_huffman_tree(frequency_list)

    def create_huffman_tree(self, frequency_list):
        # initialize tree
        for entry in frequency_list:
            new_node = Node(entry[0], entry[1], None, None)
            self.frequency_queue.append(new_node)
        self.sort_queue()

    def sort_queue(self):
        self.frequency_queue.sort(key=comparison_key)
