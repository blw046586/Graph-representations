class Edge:
    def __init__(self, from_vertex, to_vertex):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
    
    def __eq__(self, other):
        return (self.from_vertex is other.from_vertex and
            self.to_vertex is other.to_vertex)
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    # Returns a string for this edge in the form "A to B", where "A" is
    # from_vertex's label and "B" is to_vertex's label.
    def __str__(self):
        return f"{self.from_vertex.get_label()} to {self.to_vertex.get_label()}"