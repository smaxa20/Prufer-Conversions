def pruferToTree(prufer):
    ignore = []

    # We need to keep track of the original Prufer Sequence to use in building the edges list
    original = []
    for x in prufer:
        original.append(x)

    # The number of nodes in a tree is two more than the length of its Prufer Sequence
    n = len(original) + 2

    _pruferToTree(prufer, ignore, n)



    # Build output - [edges list, adjacency matrix, incidence list].
    output = []

    # Build edges list - they're made up of matching indices of the original Prufer Sequence and the ignore list
    #   plus the last two nodes are adjacent.
    edges = []
    i = 0
    while (i < len(original)):
        edges.append([original[i], ignore[i]])
        i += 1
    edges.append([ignore[len(ignore)-1], ignore[len(ignore)-2]])

    # Making it look pretty and ready to copy and paste to https://csacademy.com/app/graph_editor/.
    output.append(str(edges).replace("], ", "\n").replace(",", "").replace("[", "").replace("]", ""))


    # Build adjacency matrix.
    matrix = []

    # Initialize an empty matrix of size nxn.
    i = 0
    while (i < n):
        matrix.append([])
        j = 0
        while (j < n):
            matrix[i].append(0)
            j += 1
        i += 1

    # For each edge, place a 1 in the matrix at positions X,Y and Y,X (if edges are defined as [X, Y])
    for pair in edges:
        matrix[pair[0]-1][pair[1]-1] = 1
        matrix[pair[1]-1][pair[0]-1] = 1

    output.append(matrix)


    # Build incidence list - dictionary where keys: nodes, and values: a list of adjacent nodes.
    incidence = {}

    # Initialize an empty dictionary of size n
    i = 1
    while (i <= n):
        incidence.setdefault(i, [])
        i += 1

    # For each edge pair, add value Y to value X's incidence list and vice versa (if edges are defined as [X, Y]).
    for pair in edges:
        incidence[pair[0]].append(pair[1])
        incidence[pair[1]].append(pair[0])
    
    output.append(incidence)

    return output

# If a node is not in the Prufer Sequence that we've been deconstructing and not in the ignore list,
#   then remove it from the Prufer Sequence and add it to the ignore list.
# We count up from 1 to n in order to always use the smallest node we can.
def _pruferToTree(prufer, ignore, n):
    node = 1
    while (node <= n):
        if (node not in prufer and node not in ignore):
            if (len(prufer) != 0):
                prufer.pop(0)
            ignore.append(node)
            _pruferToTree(prufer, ignore, n)    # Recursive call with new Prufer Sequence and ignore list
            break
        node += 1


print(pruferToTree([1,3,3,4])[0])
print()
print(pruferToTree([1,3,3,4])[1])
print()
print(pruferToTree([1,3,3,4])[2])
print()
print()
print(pruferToTree([6,2,2,3,3,3])[0])
print()
print(pruferToTree([6,2,2,3,3,3])[1])
print()
print(pruferToTree([6,2,2,3,3,3])[2])