# Takes a list of lists where the inner lists are pairs of adjacent nodes.
# Converts this list of edges to an incidence list, 
#   then calls the function that generates a Prufer Sequence from an incidence list.
def edgesToPrufer(edges):
    incidence = {}
    # This amazingly gets the max value in a list of lists. I love Python.
    # The max value in the list of edges corresponds to the number of nodes in the tree.
    n = max(max(edges))

    # Initialize the incidence list with keys: 1-n, and values: empty lists.
    i = 0
    while (i < n):
        incidence.setdefault(i+1, [])
        i += 1

    # For each edge pair, add value Y to value X's incidence list and vice versa (if edges are defined as [X, Y]).
    for pair in edges:
        incidence[pair[0]].append(pair[1])
        incidence[pair[1]].append(pair[0])

    # Generate a Prufer Sequence from the incidence list.
    return incidenceToPrufer(incidence)


# Takes an adjacency matrix -
#   A list of lists that create an nxn matrix where n is the number of nodes in the tree.
# Converts this matrix to an incidence list,
#   then calls the function that generates a Prufer Sequence from an incidence list.
def matrixToPrufer(matrix):
    incidence = {}
    i = 0
    while (i < len(matrix)):
        # Initialize the incidence list with keys: 1-n, and values: empty lists.
        incidence.setdefault(i+1, [])
        j = 0
        while (j < len(matrix)):
            # If the value in the matrix is a 1, add the column number to the row number's incidence list.
            if (matrix[i][j] == 1):
                incidence[i+1].append(j+1)
            j += 1
        i += 1

    # Generate a Prufer Sequence from the incidence list.
    return incidenceToPrufer(incidence)
    

# Takes an incidence list -
#   A dictionary where keys: nodes, and values: a list of adjacent nodes.
# Generates a Prufer Sequence from the incidence list.
# This function is called initially, and calls a subfunction that calls itself recursively.
def incidenceToPrufer(incidence):
    # Call the subfunction with the added prufer argument which allows the sequence to persist through calls.
    prufer = []
    _incidenceToPrufer(incidence, prufer)
    return prufer

def _incidenceToPrufer(incidence, prufer):
    leaves = {}

    # Put nodes and their adjacency list in the leaves dictionary if they're only adjacent to one node.
    for node in incidence.keys():
        if (len(incidence[node]) == 1):
            leaves.setdefault(node, incidence[node])

    # If we aren't at the base case (a two-node tree)...
    if (len(incidence) > 2):
        minLeaf = min(leaves.keys())            # Find the smallest leaf node...
        parent = leaves[minLeaf][0]
        incidence.pop(minLeaf)                  # Remove it from the incidence list...
        incidence[parent].remove(minLeaf)       # Remove the reference to it from its parent's adjacency list...
        prufer.append(parent)                   # Append its parent node to the Prufer Sequence...

        _incidenceToPrufer(incidence, prufer)   # And make the recursive call.
