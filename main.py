import pprint

# Graph Data
nodes = ["A", "B", "C", "D", "E", "F", "G", "Z", "H","I","J","K",]
edges = [ ("A", "B", 4), ("A", "E", 4), ("B", "C", 5), ("E", "D", 2), ("D", "C", 6), ("C", "Z", 10),
         ("D", "Z", 8), ("D", "G", 8), ("G", "Z", 8), ("F", "G", 3), ("E", "F", 4), ("H", "A", 7),
         ("I", "C", 5), ("J", "K", 1), ("K", "B", 8)]

# List/Heap/Sort/Search Data
data = [4,5,3,6,2,7,1,8,9,10,0]




class Graph:
    """
    Undirected Weighted Graph
    Example output:
    A: [('B', 4), ('E', 4), ('H', 7)]
    B: [('A', 4), ('C', 5), ('K', 8)]
    C: [('B', 5), ('D', 6), ('Z', 10), ('I', 5)]
    D: [('E', 2), ('C', 6), ('Z', 8), ('G', 8)]
    E: [('A', 4), ('D', 2), ('F', 4)]
    F: [('G', 3), ('E', 4)]
    G: [('D', 8), ('Z', 8), ('F', 3)]
    Z: [('C', 10), ('D', 8), ('G', 8)]
    H: [('A', 7)]
    I: [('C', 5)]
    J: [('K', 1)]
    K: [('J', 1), ('B', 8)]

    """

    def __init__(self):
        self.graph = {}

    def add_node(self, value):
        if value not in self.graph:
            self.graph[value] = []

    def add_edge(self, value):
        if value[0] in self.graph and value[1] in self.graph:
            self.graph[value[0]].append((value[1], value[2]))
            self.graph[value[1]].append((value[0], value[2]))
        else:
            print("Node not in graph")


    def all_paths(self, start, end, path=[]):
        """
        :param start: Starting Node
        :param end:  Ending Node
        :param path: Tracking Paths
        :return: All Valid Paths
        """

        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph:
            return None

        paths = []
        for edge in self.graph[start]:
            if edge[0] not in path:
                all_paths = self.all_paths(edge[0], end, path)
                for node in all_paths:
                    paths.append(node)
        return paths

    def dijkstras(self, node):
        """
        :param node: Starting Node
        :return: Shortest Paths & Shortest Paths Total ***BY WEIGHT***
        """
        distances = {vertex: float("inf") for vertex in self.graph}
        paths = {vertex:[node] for vertex in self.graph}
        distances[node] = 0

        queue = [(0, node)]

        while queue:
            curr_dist, curr_vtx = queue.pop(0)

            if curr_dist > distances[curr_vtx]:
                continue

            for vtx, weight in self.graph[curr_vtx]:
                dist_thru = weight + curr_dist
                if dist_thru < distances[vtx]:
                    distances[vtx] = dist_thru
                    paths[vtx] = paths[curr_vtx] + [vtx]
                    queue.append((distances[vtx], vtx))

        print("Distances")
        pprint.pprint(distances)
        print("Paths")
        pprint.pprint(paths)

        return True

    def shortest_distance(self, start, end, path=[]):
        """
        :param start: Starting Node
        :param end: Ending Node
        :param path: Path Tracker
        :return: Shortest Path -> Path Lenght
        """

        path = path + [start]

        if start == end:
            return path

        if start not in self.graph:
            return None

        shortest = None
        for edge in self.graph[start]:
            if edge[0] not in path:
                short = self.shortest_distance(edge[0], end, path)
                if short: # Check if not None
                    if shortest is None or len(short) < len(shortest):
                        shortest = short

        return shortest

    def dfs(self, vertex, visited=None, order=None):
        if visited is None and order is None:
            visited = set() # use set O(1) lookup
            order = []

        if vertex not in visited:
            """Update visted and 
            order each recursive call"""

            visited.add(vertex)
            order.append(vertex)

            for edge in self.graph[vertex]:
                if edge[0] in self.graph:
                    # Recursive call when edge[0] is in graph
                    self.dfs(edge[0], visited, order)
                else:
                    order.append(edge[0])
        return order

    def bfs(self, vertex):
        visited = set()
        order = []
        queue = []

        visited.add(vertex)
        queue.append(vertex)

        while queue:
            curr_vtx = queue.pop(0)
            order.append(curr_vtx)

            if curr_vtx in self.graph:
                for edge in self.graph[curr_vtx]:
                    if edge[0] not in visited:
                        visited.add(edge[0])
                        queue.append(edge[0])

        return order

    def output(self):
        for node in self.graph:
            print(str(node) + ":", self.graph[node])

g = Graph()
for i in nodes:
    g.add_node(i)
for i in edges:
    g.add_edge(i)
print("ALL PATHS")
pprint.pprint(g.all_paths("A", "Z"))
print("")
print("Dijkstras")
g.dijkstras("A")
print("")
print("Shortest Path - Path list length")
pprint.pprint(g.shortest_distance("A", "Z"))
print("")
print("Depth First Search - Graph")
pprint.pprint(g.dfs("A"))
print("")
print("Breadth First Search")
pprint.pprint(g.bfs("A"))
print("")
print("------------------------")
print("")

class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

    def add_leaf(self, value):
        if value == self.root:
            return None
        elif value < self.root:
            if self.left:
                self.left.add_leaf(value)
            else:
                self.left = BinaryTree(value)
        else:
            if self.right:
                self.right.add_leaf(value)
            else:
                self.right = BinaryTree(value)

    def find_min(self):
        """
        Helper function for node removal
        :return: Minimum value in tree
        """
        if self.left is None:
            return self.root
        else:
            return self.left.find_min()

    def remove_value(self, value):
        if value < self.root:
            if self.left:
                self.left = self.left.remove_value(value)
        elif value > self.root:
            if self.right:
                self.right = self.right.remove_value(value)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                min_val = self.right.find_min()
                self.root = min_val
                self.right = self.right.remove_value(min_val)

        return self

    def in_order_traversal(self):

        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.root)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = [self.root]

        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.root)

        return elements

print("Binary Tree")

tree = BinaryTree(data[0])
for i in data[1:]:
    tree.add_leaf(i)
    print(tree.in_order_traversal())
for i in data:
    tree.remove_value(i)
    print(tree.in_order_traversal())

print("")
print("------------------")
print("Linked Lists!!")
class Node:
    """
    Node class that will be used for all
    linked lists
    """
    def __init__(self, root):
        self.data = root
        self.prev = None
        self.next = None

class CircualrLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_node(self, value):
        new_node = Node(value)

        if self.size == 0:
            """
            Circualr Linked List, tail connects to another node 
            in this example, the head
            """
            self.head = new_node
            new_node.next = self.head
        else:
            """
            Adding node in the second posistion
            for quick additions
            """
            new_node.next = self.head.next
            self.head.next = new_node

        self.size += 1
        return True

    def remove_node(self, value):
        curr = self.head
        prev = None

        while True:
            if curr.data == value:
                if prev != None:
                    prev.next = curr.next
                else:
                    while curr.next != self.head:
                        curr = curr.next
                    curr.next = self.head.next
                    self.head = self.head.next

                self.size -= 1
                return
            elif curr.next == self.head:
                return False
            else:
                prev = curr
                curr = curr.next

    def __str__(self):
        """Ouput method"""
        output = ""
        curr = self.head
        output += "%s->" % curr.data
        curr = curr.next
        while curr != self.head:
            output += "%s->" % curr.data
            curr = curr.next
        return output

print("")
print("Circular Linked list")
cll = CircualrLinkedList()
for i in data:
    cll.add_node(i)
    print(cll)
for i in data:
    cll.remove_node(i)
    print(cll)





