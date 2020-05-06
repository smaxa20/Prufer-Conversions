import random

# n is the desired number of nodes in the tree
def randomTree(n):
    prüfer = []
    # Prüfer Sequences are of size n-2, so we only need n-2 random numbers
    i = 0
    while i < n-2:
        # Gets a random number from 1 to n
        rand = random.randrange(1, n+1)
        prüfer.append(rand)
        i += 1
    return prüfer
