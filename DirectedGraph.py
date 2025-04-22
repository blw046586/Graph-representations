from Vertex import Vertex
from Edge import Edge

# Base class for a directed, unweighted graph
class DirectedGraph:
    # Creates and adds a new vertex to the graph, provided a vertex with the
    # same label doesn't already exist in the graph. Returns the new vertex on
    # success, None on failure.
    def add_vertex(self, new_vertex_label):
        pass
    
    # Adds a directed edge from the first to the second vertex. No change is
    # made and false is returned if the edge already exists in the graph.
    # Otherwise the new edge is added and true is returned.
    def add_directed_edge(self, from_vertex, to_vertex):
        pass
    
    # Returns a list of all of this graph's distinct edges
    def get_edges(self):
        pass
    
    # Returns a list of edges with the specified from_vertex
    def get_edges_from(self, from_vertex):
        pass
    
    # Returns a list of edges with the specified to_vertex
    def get_edges_to(self, to_vertex):
        pass
    
    # Returns a vertex with a matching label, or None if no such vertex exists
    def get_vertex(self, vertex_label):
        pass
    
    # Returns a list of all of this graph's distinct vertices
    def get_vertices(self):
        pass
    
    # Returns True if this graph has an edge from from_vertex to to_vertex
    def has_edge(self, from_vertex, to_vertex):
        pass