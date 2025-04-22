from DirectedGraph import DirectedGraph
from Vertex import Vertex
from Edge import Edge  # Import the Edge class

class AdjacencyMatrixGraph(DirectedGraph):
    def __init__(self):
        self.vertices = []
        self.matrix_rows = []
    
    # Creates and adds a new vertex to the graph, provided a vertex with the
    # same label doesn't already exist in the graph. Returns the new vertex on
    # success, None on failure.
    def add_vertex(self, new_vertex_label):
        if self.get_vertex(new_vertex_label) is None:
            new_vertex = Vertex(new_vertex_label)
            self.vertices.append(new_vertex)
            # Add a new row and column to the adjacency matrix
            for row in self.matrix_rows:
                row.append(False)  # Add a new column
            self.matrix_rows.append([False] * len(self.vertices))  # Add a new row
            return new_vertex
        return None
    
    # Adds a directed edge from the first to the second vertex. If the edge
    # already exists in the graph, no change is made and False is returned.
    # Otherwise the new edge is added and True is returned.
    def add_directed_edge(self, from_vertex, to_vertex):
        from_index = self.get_vertex_index(from_vertex)
        to_index = self.get_vertex_index(to_vertex)
        if from_index != -1 and to_index != -1:
            if not self.matrix_rows[from_index][to_index]:
                self.matrix_rows[from_index][to_index] = True
                return True
        return False
    
    # Returns a list of edges with the specified from_vertex
    def get_edges_from(self, from_vertex):
        edges = []
        from_index = self.get_vertex_index(from_vertex)
        if from_index != -1:
            for to_index, has_edge in enumerate(self.matrix_rows[from_index]):
                if has_edge:
                    edges.append(Edge(from_vertex, self.vertices[to_index]))
        return edges
    
    # Returns a list of edges with the specified to_vertex
    def get_edges_to(self, to_vertex):
        edges = []
        to_index = self.get_vertex_index(to_vertex)
        if to_index != -1:
            for from_index in range(len(self.vertices)):
                if self.matrix_rows[from_index][to_index]:
                    edges.append(Edge(self.vertices[from_index], to_vertex))
        return edges
    
    # Returns a vertex with a matching label, or None if no such vertex exists
    def get_vertex(self, vertex_label):
        for vertex in self.vertices:
            if vertex.get_label() == vertex_label:
                return vertex
        return None
    
    # Returns True if this graph has an edge from from_vertex to to_vertex
    def has_edge(self, from_vertex, to_vertex):
        from_index = self.get_vertex_index(from_vertex)
        to_index = self.get_vertex_index(to_vertex)
        if from_index != -1 and to_index != -1:
            return self.matrix_rows[from_index][to_index]
        return False

    def get_vertices(self):
        return self.vertices

    def get_edges(self):
        all_edges = []
        for from_vertex in self.vertices:
            all_edges.extend(self.get_edges_from(from_vertex))
        return all_edges
    
    # Helper function to get the index of a vertex in the vertices list
    def get_vertex_index(self, vertex):
        try:
            return self.vertices.index(vertex)
        except ValueError:
            return -1