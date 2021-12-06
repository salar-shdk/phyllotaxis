import matplotlib.pyplot as plt
import math

class Plot:
    def __init__(self, phyllotaxis, circle_radius=7.2):
        self.phyllotaxis = phyllotaxis
        self.circle_radius = circle_radius

    def render(self):    
        figure, axes = plt.subplots()
        map_size = self.phyllotaxis.scale_ratio * math.sqrt(len(self.phyllotaxis.get_node_list())) + 10
        axes.set_xlim(-1 * map_size, map_size)
        axes.set_ylim(-1 * map_size, map_size)
        for node in self.phyllotaxis.get_node_list():
            axes.add_artist( plt.Circle(node.get_position(), self.circle_radius, fill=False ) )
        plt.title('Phyllotaxis')
        plt.show()