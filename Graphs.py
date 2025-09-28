'''
A Graph is a non-linear data structure consisting of vertices and edges. The vertices are sometimes also referred to as nodes and the edges are lines or arcs that connect any two nodes in the graph. More formally a Graph is composed of a set of vertices( V ) and a set of edges( E ). The graph is denoted by G(V, E).

Representations of Graph
Here are the two most common ways to represent a graph : For simplicity, we are going to consider only unweighted graphs in this post.

Adjacency Matrix
Adjacency List
Adjacency Matrix Representation
An adjacency matrix is a way of representing a graph as a matrix of boolean (0's and 1's)

Let's assume there are n vertices in the graph So, create a 2D matrix adjMat[n][n] having dimension n x n.

If there is an edge from vertex i to j, mark adjMat[i][j] as 1. 
If there is no edge from vertex i to j, mark adjMat[i][j] as 0.
Representation of Undirected Graph as Adjacency Matrix:
The below figure shows an undirected graph. Initially, the entire Matrix is ​​initialized to 0. If there is an edge from source to destination, we insert 1 to both cases (adjMat[source][destination] and adjMat[destination][source]) because we can go either way.


'''
def addEdge(mat,i,j):
    mat[i][j] = 1
    mat[j][i] = 1 # Undirect
def displayMatris(mat):
    for row in mat:
        print(" ".join(map(str,row)))
if __name__ == '__main__':
    V = 4
    mat = [[0] * V for _ in range(V)]
    addEdge(mat,0,1)
    addEdge(mat,0,2)
    addEdge(mat,1,2)
    addEdge(mat,2,3)

    print(displayMatris(mat))