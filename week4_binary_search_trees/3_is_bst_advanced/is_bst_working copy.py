import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)

class Node:
    def __init__(self, a, b, c):
        self.key = a
        self.left = b
        self.right = c

def isBST(root, min, max):
    if root == -1:
        return True
    rootNode = nodes[root]
    rootVal =  rootNode.key
    if rootVal >= min and rootVal < max and \
    isBST(rootNode.left, min, rootNode.key) and \
    isBST(rootNode.right, rootNode.key, max):
        return True
    else:
        return False

def main():
    n_nodes = int(sys.stdin.readline().strip())
    global nodes
    if n_nodes == 0:
        print('CORRECT')
        return
    nodes = [0 for _ in range(n_nodes)]
    for i in range(n_nodes):
      a, b, c = map(int, input().split())
      node = Node(a, b, c)
      nodes[i] = node
    if isBST(0, float('-inf'), float('inf')):
        print('CORRECT')
    else:
        print('INCORRECT')
    return

threading.Thread(target=main).start()


