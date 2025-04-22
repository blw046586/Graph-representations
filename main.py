from FeedbackPrinter import FeedbackPrinter
from DirectedGraph import DirectedGraph
from AdjacencyListVertex import AdjacencyListVertex
from AdjacencyListGraph import AdjacencyListGraph
from AdjacencyMatrixGraph import AdjacencyMatrixGraph
from GraphCommands import *

def test_graph(test_feedback, graph):
    commands = [
        AddVertexCommand("A", True),
        AddVertexCommand("B", True),
      
        # Verify that vertices A and B exist, but not C, D, or E
        GetVertexCommand("C", False),
        GetVertexCommand("A", True),
        GetVertexCommand("B", True),
        GetVertexCommand("E", False),
        GetVertexCommand("D", False),
      
        # Add remaining vertices
        AddVertexCommand("C", True),
        AddVertexCommand("D", True),
        AddVertexCommand("E", True),
      
        # Add edges
        AddEdgeCommand("B", "C", True),
        AddEdgeCommand("C", "A", True),
        AddEdgeCommand("C", "D", True),
        AddEdgeCommand("C", "E", True),
        AddEdgeCommand("D", "C", True),
        AddEdgeCommand("E", "A", True),
        AddEdgeCommand("E", "D", True),
      
        # Attempts to add a duplicate edge should fail
        AddEdgeCommand("C", "E", False),
        AddEdgeCommand("D", "C", False),
      
        VerifyEdgesFromCommand("A", {}),
        VerifyEdgesFromCommand("B", { "C" }),
        VerifyEdgesFromCommand("C", { "A", "D", "E" }),
        VerifyEdgesFromCommand("D", { "C" }),
        VerifyEdgesFromCommand("E", { "A", "D" }),
      
        VerifyEdgesToCommand("A", { "C", "E" }),
        VerifyEdgesToCommand("B", {}),
        VerifyEdgesToCommand("C", { "B", "D" }),
        VerifyEdgesToCommand("D", { "C", "E" }),
        VerifyEdgesToCommand("E", { "C" }),
      
        # Verify some edges
        HasEdgeCommand("A", "C", False),
        HasEdgeCommand("A", "E", False),
        HasEdgeCommand("B", "C", True),
        HasEdgeCommand("C", "A", True),
        HasEdgeCommand("C", "B", False),
        HasEdgeCommand("C", "D", True),
        HasEdgeCommand("C", "E", True),
        HasEdgeCommand("D", "C", True),
        HasEdgeCommand("E", "A", True),
        HasEdgeCommand("E", "C", False),
        HasEdgeCommand("E", "D", True)
    ]
    
    # Execute each test command, stopping if any command fails
    for command in commands:
        passed = command.execute(test_feedback, graph)
        if not passed:
            return False
    
    return True

# Main program code follows

feedback = FeedbackPrinter()

# Test AdjacencyListGraph first
graph1 = AdjacencyListGraph()
print("AdjacencyListGraph:   ")
adj_pass = test_graph(feedback, graph1)
   
# Test AdjacencyMatrixGraph second
graph2 = AdjacencyMatrixGraph()
print("\nAdjacencyMatrixGraph: ")
mat_pass = test_graph(feedback, graph2)
   
# Print test results
print("\nSummary:")
print(f"  AdjacencyListGraph:   {'PASS' if adj_pass else 'FAIL'}")
print(f"  AdjacencyMatrixGraph: {'PASS' if mat_pass else 'FAIL'}")