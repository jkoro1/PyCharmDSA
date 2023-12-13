# Graph Data
nodes = ["A", "B", "C", "D", "E", "F", "G", "Z", "H","I","J","K",]
edges = [ ("A", "B", 4), ("A", "E", 4), ("B", "C", 5), ("E", "D", 2), ("D", "C", 6), ("C", "Z", 10),
         ("D", "Z", 8), ("D", "G", 8), ("G", "Z", 8), ("F", "G", 3), ("E", "F", 4), ("H", "A", 7),
         ("I", "C", 5), ("J", "K", 1), ("K", "B", 8)]

# List/Heap/Sort/Search Data
data = [4,5,3,6,2,7,1,8,9,10,0]




class Graph:
    """
    Visual of graph - Undirected Weighted Graph

        H --- A ---  B --- C --- Z
    |         / |         |
    |        /  |         |
    I       E   D --- G --- F
             \ |         |
              \|         |
                J         K
    """

    def __init__(self):
        self.graph = {}

    def add_node(self, value):
        if value not in self.graph:
            self.graph[value] = []

    def add_edge(self, value):
