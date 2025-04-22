from DirectedGraph import DirectedGraph
from AdjacencyListVertex import AdjacencyListVertex
from Edge import Edge  # Import the Edge class

class AdjacencyListGraph(DirectedGraph):
    def __init__(self):
        self.vertices = []
    
    # Creates and adds a new vertex to the graph, provided a vertex with the
    # same label doesn't already exist in the graph. Returns the new vertex on
    # success, None on failure.
    def add_vertex(self, new_vertex_label):
        if self.get_vertex(new_vertex_label) is None:
            new_vertex = AdjacencyListVertex(new_vertex_label)
            self.vertices.append(new_vertex)
            return new_vertex
        return None
    
    # Adds a directed edge from the first to the second vertex. If the edge
    # already exists in the graph, no change is made and False is returned.
    # Otherwise the new edge is added and True is returned.
    def add_directed_edge(self, from_vertex, to_vertex):
        if from_vertex is not None and to_vertex is not None:
            if to_vertex not in from_vertex.adjacent:
                from_vertex.adjacent.append(to_vertex)
                return True
        return False
    
    # Returns a list of edges with the specified from_vertex
    def get_edges_from(self, from_vertex):
        edges = []
        if from_vertex is not None:
            for adjacent_vertex in from_vertex.adjacent:
                edges.append(Edge(from_vertex, adjacent_vertex))
        return edges
    
    # Returns a list of edges with the specified to_vertex
    def get_edges_to(self, to_vertex):
        edges = []
        if to_vertex is not None:
            for vertex in self.vertices:
                if to_vertex in vertex.adjacent:
                    edges.append(Edge(vertex, to_vertex))
        return edges
    
    # Returns a vertex with a matching label, or None if no such vertex exists
    def get_vertex(self, vertex_label):
        for vertex in self.vertices:
            if vertex.get_label() == vertex_label:
                return vertex
        return None
    
    # Returns true if this graph has an edge from from_vertex to to_vertex
    def has_edge(self, from_vertex, to_vertex):
        if from_vertex is not None and to_vertex is not None:
            return to_vertex in from_vertex.adjacent
        return False

    def get_vertices(self):
        return self.vertices

    def get_edges(self):
        all_edges = []
        for vertex in self.vertices:
            all_edges.extend(self.get_edges_from(vertex))
        return all_edges