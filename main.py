import randomTree as rt
import pruferToTree as pt
import treeToPrufer as tp

# Generate random Prufer Sequence
print()
prufer = rt.randomTree(8)
print(prufer)
print("\n\n")

# Generate tree from that Prufer Sequence
tree = pt.pruferToTree(prufer)
edges = tree[0]
matrix = tree[1]
incidence = tree[2]
print(edges)
print()
for x in matrix:
    print(x)
print()
for x,y in incidence.items():
    print(str(x) + " : " + str(y))
print("\n\n")

# edges is a specifically formatted string so we must convert it back to a list of lists of ints
edges = edges.split("\n")
i = 0
while i < len(edges):
    edges[i] = edges[i].split(" ")
    j = 0
    while j < len(edges[i]):
        edges[i][j] = int(edges[i][j])
        j += 1
    i += 1

# Generate the Prufer Sequence again from the tree
pruferFromEdges = tp.edgesToPrufer(edges)
pruferFromMatrix = tp.matrixToPrufer(matrix)
pruferFromIncidence = tp.incidenceToPrufer(incidence)
print(pruferFromEdges)
print(pruferFromMatrix)
print(pruferFromIncidence)
