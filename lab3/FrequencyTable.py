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

        while len(self.frequency_queue) > 1:

            right = self.frequency_queue.pop()
            left = self.frequency_queue.pop()

            print("\nMerging " + left.name + " and " + right.name)

            name = left.name + right.name
            frequency = left.frequency + right.frequency

            merged_node = Node(name, frequency, left, right)
            self.frequency_queue.append(merged_node)
            self.sort_queue()

    def sort_queue(self):
        self.frequency_queue.sort(key=comparison_key)
