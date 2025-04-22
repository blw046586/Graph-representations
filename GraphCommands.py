from Edge import Edge
from DirectedGraph import DirectedGraph

class DirectedGraphTestCommand:
    # Returns True if the test passes, False if the test fails
    def execute(self, test_feedback, graph):
        pass
    
    # Utility method that checks if a list of edges has a particular edge
    @staticmethod
    def has_edge(edges, from_vertex, to_vertex):
        # Iterate through the collection's edges
        for edge in edges:
            if edge.from_vertex is from_vertex and edge.to_vertex is to_vertex:
                return True
        return False
    
    @staticmethod
    def edges_to_string(edges, separator = ", ", prefix = "", suffix = ""):
        # Start with the prefix
        result = prefix
        
        # Add edges
        added_first = False
        for edge in edges:
            if added_first:
                result += f"{separator}{edge}"
            else:
                result += str(edge)
                added_first = True
        
        # Add suffix and return
        result += suffix
        return result

# Command that adds a new vertex to the graph and verifies that the addition
# either failed or succeeded
class AddVertexCommand(DirectedGraphTestCommand):
    def __init__(self, vertex_label, should_succeed):
        self.label = vertex_label
        self.should_succeed = should_succeed
    
    def execute(self, test_feedback, graph):
        # Try to add the vertex. If the return value is non-None, then addition
        # is successful, otherwise addition has failed.
        new_vertex = graph.add_vertex(self.label)
        
        if new_vertex != None:
            if not self.should_succeed:
                test_feedback.write(f'FAIL: add_vertex("{self.label}") returned ' +
                    "a vertex object, but should have returned None due to " +
                    "the label already being in use")
                return False
            
            test_feedback.write(f'PASS: add_vertex("{self.label}") returned ' +
                "a valid node")
            return True
        
        if self.should_succeed:
            test_feedback.write(f'FAIL: add_vertex("{self.label}") returned ' +
                "None, but should have returned a node object")
            return False
        
        test_feedback.write(f'PASS: add_vertex("{self.label}") returned None ' +
            "because the label is already in use")
        return True

# Command that gets a vertex by label and verifies the result
class GetVertexCommand(DirectedGraphTestCommand):
    def __init__(self, vertex_label, vertex_should_exist):
        self.label = vertex_label
        self.should_exist = vertex_should_exist
    
    def execute(self, test_feedback, graph):
        # Get the vertex by calling get_vertex()
        vertex = graph.get_vertex(self.label)
        
        # Check if the returned vertex is non-None
        if vertex != None:
            # If the vertex shouldn't exist, then print a failure message
            if not self.should_exist:
                test_feedback.write(f'FAIL: get_vertex("{self.label}") ' +
                    "returned a vertex object, but should have returned None")
                return False
            
            # Verify the vertex's label
            actual_label = vertex.get_label()
            if self.label != actual_label:
                test_feedback.write(f'FAIL: get_vertex("{self.label}") ' +
                    f'returned a vertex with incorrect label "{actual_label}"')
                return False
            
            test_feedback.write(f'PASS: get_vertex("{self.label}") returned a ' +
                "vertex with the correct label")
            return True
        
        # The returned vertex is None, so check if None is expected
        if self.should_exist:
            test_feedback.write(f'FAIL: get_vertex("{self.label}") returned ' +
                "None, but should have returned a Vertex object")
            return False
        
        # PASS
        test_feedback.write(f'PASS: get_vertex("{self.label}") returned None')
        return True

# Command that adds an edge to a graph
class AddEdgeCommand(DirectedGraphTestCommand):
    def __init__(self, from_vertex_label, to_vertex_label, should_succeed):
        self.from_label = from_vertex_label
        self.to_label = to_vertex_label
        self.should_succeed = should_succeed
    
    def execute(self, test_feedback, graph):
        # Find both vertices
        from_vertex = graph.get_vertex(self.from_label)
        to_vertex = graph.get_vertex(self.to_label)
        
        # Add the edge
        added_edge = False
        if from_vertex != None and to_vertex != None:
            added_edge = graph.add_directed_edge(from_vertex, to_vertex)
        
        if added_edge == self.should_succeed:
            # PASS
            message = "PASS: "
            if added_edge:
                message += (f'Added edge from "{self.from_label}" to ' +
                    f'"{self.to_label}"')
            else:
                message += (f'Attempt to add edge from "{self.from_label}" ' +
                    f'to "{self.to_label}" returned False')
            test_feedback.write(message)
            return True
        
        # FAIL
        test_feedback.write(f'FAIL: Add edge from "{self.from_label}" to ' +
            f'"{self.to_label}"')
        return False

# Command that verifies the return value from a call to has_edge()
class HasEdgeCommand(DirectedGraphTestCommand):
    def __init__(self, from_vertex_label, to_vertex_label, expected_return_val):
        self.from_label = from_vertex_label
        self.to_label = to_vertex_label
        self.expected = expected_return_val
    
    def execute(self, test_feedback, graph):
        # Find both vertices
        from_vertex = graph.get_vertex(self.from_label)
        to_vertex = graph.get_vertex(self.to_label)
        
        # Call has_edge() to get the actual return value
        actual = graph.has_edge(from_vertex, to_vertex)
        
        if actual != self.expected:
            test_feedback.write("FAIL: has_edge() should have returned " +
                ("True" if expected else "False") + " for an edge from " +
                (from_vertex.get_label() if from_vertex else "None") +
                " to " +
                (to_vertex.get_label() if to_vertex else "None") +
                ", but instead returned " +
                ("True" if actual else "False"))
            return False
        
        test_feedback.write("PASS: has_edge() returned " +
            ("True" if self.expected else "False") + " for an edge from " +
            (from_vertex.get_label() if from_vertex else "None") +
            " to " +
            (to_vertex.get_label() if to_vertex else "None"))
        return True

# Base class for VerifyEdgesFromCommand and VerifyEdgesToCommand
class VerifyEdgesCommand(DirectedGraphTestCommand):
    def execute(self, test_feedback, graph):
        # Must be implemented in derived class
        pass
    
    def verify(self, test_feedback, actual, expected, test_name):
        passed = True
        expected_edges_str = None
        if len(actual) == len(expected):
            for expected_edge in expected:
                # If actual does not have the edge then the test fails
                if not DirectedGraphTestCommand.has_edge(actual, expected_edge.from_vertex, expected_edge.to_vertex):
                   passed = False
                   break
                
                if expected_edges_str == None:
                    expected_edges_str = str(expected_edge)
                else:
                    expected_edges_str += f", {expected_edge}"
        else:
            passed = False
        
        # Print pass or fail message along with actual and expected collections
        actual_str = DirectedGraphTestCommand.edges_to_string(
            actual, ", ", "  Actual:   {", "}")
        expected_str = DirectedGraphTestCommand.edges_to_string(
            expected, ", ", "  Expected: {", "}")
        test_feedback.write(("PASS" if passed else "FAIL") +
            f': {test_name}\n' +
            f"{actual_str}\n{expected_str}")
        
        return passed

class VerifyEdgesFromCommand(VerifyEdgesCommand):
    def __init__(self, from_vertex_label, to_vertex_labels):
        self.from_label = from_vertex_label
        self.to_labels = list(to_vertex_labels)
    
    def execute(self, test_feedback, graph):
        # Find from_vertex
        from_vertex = graph.get_vertex(self.from_label)
        if from_vertex == None:
            test_feedback.write(f'FAIL: get_vertex("{self.from_label}") ' +
                "returned None for a vertex that should exist")
            return False
        
        # Ask the graph for edges from from_vertex
        actual = graph.get_edges_from(from_vertex)
        
        # Make the list of expected edges
        expected = list(map(
            lambda lbl: Edge(from_vertex, graph.get_vertex(lbl)),
            self.to_labels))
        
        return self.verify(test_feedback, actual, expected,
            f'Get edges from "{self.from_label}"')

class VerifyEdgesToCommand(VerifyEdgesCommand):
    def __init__(self, to_vertex_label, from_vertex_labels):
        self.to_label = to_vertex_label
        self.from_labels = from_vertex_labels
   
    def execute(self, test_feedback, graph):
        # Find to_vertex
        to_vertex = graph.get_vertex(self.to_label)
        if to_vertex == None:
            test_feedback.write(f'FAIL: get_vertex("{self.to_label}") ' +
                "returned None for a vertex that should exist")
            return False
        
        # Ask the graph for edges to to_vertex
        actual = graph.get_edges_to(to_vertex)
        
        # Make the list of expected edges
        expected_edges = list(map(
            lambda lbl: Edge(graph.get_vertex(lbl), to_vertex),
            self.from_labels))
        
        return self.verify(test_feedback, actual, expected_edges,
            f'Get edges to "{self.to_label}"')