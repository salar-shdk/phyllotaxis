import math

class Node:
    def __init__(self, angel, distance):
        self.angel = angel
        self.distance = distance
    
    def get_position(self):
        return (math.cos(math.radians(self.angel)) * self.distance,
            math.sin(math.radians(self.angel)) * self.distance)

class Phyllotaxis:
    def __init__(self, pieces_number, angel_gap = 137.5, scale_ratio = 13.7):
        self.pieces_number = pieces_number
        self.angel_gap = angel_gap
        self.scale_ratio = scale_ratio
        self.nodes = []

    def calculate_nodes(self):
        angel = 0
        for node_count in range(1, self.pieces_number + 1):
            self.nodes.append(Node(angel, self.scale_ratio * math.sqrt(node_count)))
            angel += self.angel_gap

    def get_node_list(self):
        if not self.nodes:
            self.calculate_nodes()
        return self.nodes