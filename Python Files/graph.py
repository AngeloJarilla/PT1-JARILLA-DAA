'''
JARILLA, ANGELO CHRISTIENE M.
3) Graphs:
A graph is made up of nodes, also known as vertices, which are groups of points connected by edges. Graphs can depict a wide range of relationships found in the real world, including computer networks, social networks, and road maps. They might be undirected, meaning that connections flow both ways, like a two-way street, or directed, meaning that connections have direction, like a one-way street.
'''

class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_edge(self, FirstNode, SecondNode):
        if FirstNode not in self.graph_dict:
            self.graph_dict[FirstNode] = []
        self.graph_dict[FirstNode].append(SecondNode)

    def show(self):
        for node in self.graph_dict:
            print(f"{node} -> {self.graph_dict[node]}")


Graph = Graph()
Graph.add_edge("A", "B")
Graph.add_edge("A", "C")
Graph.add_edge("B", "D")
Graph.show()

#Sorry for the CamelCase