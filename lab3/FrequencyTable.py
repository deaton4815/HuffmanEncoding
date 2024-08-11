from Node import Node


def compare(node1: Node, node2: Node) -> bool:
    node1_higher_priority = False
    if node1.frequency > node2.frequency:
        node1_higher_priority = True
    elif node1.frequency == node2.frequency:

        name1 = node1.name
        name2 = node2.name

        if len(name1) == 1:
            if len(name2) > 1:
                node1_higher_priority = True
            elif name1 < name2:
                node1_higher_priority = True

        elif len(name2) > 1:
            if name1[0] < name2[0]:
                node1_higher_priority = True

    return node1_higher_priority


class FrequencyTableQueue:

    def __init__(self, frequency_list):
        self.frequency_queue = []
