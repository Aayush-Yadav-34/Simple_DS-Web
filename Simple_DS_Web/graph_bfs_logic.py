from graphviz import Digraph

class GraphBFS:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            # Remove all edges to this vertex
            for v in self.graph:
                if vertex in self.graph[v]:
                    self.graph[v].remove(vertex)
            # Remove the vertex itself
            del self.graph[vertex]

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            self.graph[vertex1].remove(vertex2)

    def bfs(self, start_vertex):
        visited = set()
        queue = [start_vertex]
        traversal_order = []

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                traversal_order.append(vertex)
                queue.extend([neighbor for neighbor in self.graph[vertex] if neighbor not in visited])

        return traversal_order

    def create_graph(self):
        dot = Digraph()
        for vertex in self.graph:
            dot.node(str(vertex))
            for adj in self.graph[vertex]:
                dot.edge(str(vertex), str(adj))
        return dot
