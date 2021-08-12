from random import random
import params
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt 

class Network():
    N = params.network_dimention

    def generate_network(self):
        return nx.grid_2d_graph(self.N, self.N)

    def plot_network(self, graph):
        pos = {(x,y):(y,-x) for x,y in graph.nodes()}
        labels = dict(((i, j), f"{i},{j}") for i, j in graph.nodes())
        plt.close()
        nx.draw_networkx(
            graph,
            pos=pos,
            labels=labels,
            node_size=400,
            node_color="green"
        )
        plt.axis("off")
        plt.show()