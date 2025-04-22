class Vertex:
    def __init__(self, vertex_label):
        self.label = vertex_label
    
    def get_label(self):
        return self.label
    
    def set_label(self, new_label):
        self.label = new_label