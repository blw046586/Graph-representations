# Graph-representations
Step 1: Inspect Vertex.py, Edge.py, and DirectedGraph.py
Inspect the Vertex class declaration in the Vertex.py file. The Vertex class represents a graph vertex and has a string for the vertex label.

Inspect the Edge class declaration in the Edge.py file. The edge class represents a directed graph edge and has attributes for a from-vertex and a to-vertex.

Inspect the DirectedGraph class declaration in the DirectedGraph.py file. DirectedGraph is an abstract base class for a directed, unweighted graph.


Step 2: Inspect AdjacencyListGraph.py and AdjacencyListVertex.py
The AdjacencyListGraph class inherits from DirectedGraph and is declared in AdjacencyListGraph.py. The vertices attribute is a list of AdjacencyListVertex references . The list contains all the graph's vertices.

The AdjacencyListVertex class inherits from Vertex and is declared in the read-only AdjacencyListVertex.py file. The adjacent attribute is a list of adjacent vertices.


Step 3: Inspect AdjacencyMatrixGraph.py
The AdjacencyMatrixGraph class inherits from DirectedGraph and is declared in AdjacencyMatrixGraph.py. The vertices attribute is a list of Vertex references. The list contains all the graph's vertices. The matrixRows attribute is a list of matrix rows. Each row itself is a list of Boolean values. If matrix_rows[X][Y] is true, then an edge exists from vertices[X] to vertices[Y].

Indices in vertices correspond to indices in matrix_rows. So if vertex "C" exists at index 2 in vertices, then row 2 and column 2 in the matrix correspond to vertex "C".


Step 4: Implement the AdjacencyListGraph class
Implement the required methods in AdjacencyListGraph. Each method has a comment indicating the required functionality. The vertices list must be used to store the graph's vertices and must not be removed. New methods can be added, if needed, but existing method signatures must not change.


Step 5: Implement the AdjacencyMatrixGraph class
Implement the required methods in AdjacencyMatrixGraph. Each method has a comment indicating the required functionality. The vertices and matrix_rows lists must be used to store the graph's vertices and adjacency matrix, respectively. Both must not be removed. New methods can be added, if needed, but existing method signatures must not change.


Step 6: Test code, then submit
File main.py contains test cases for each graph operation. The test operations are first run on an AdjacencyListGraph. Then the same test operations are run on an AdjacencyMatrixGraph. Results of each test are displayed.

After each method is implemented and all tests in main.py pass, submit the code for grading. The unit tests run on submitted code are similar but use different graphs and perform direct verification of each graph's internal attributes.


