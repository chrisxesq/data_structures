import sys, threading

sys.setrecursionlimit(10**7)
#below is the KEY to bypass sig 11
threading.stack_size(2**27)

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
    if rootVal >= min and rootVal < max:
      return isBST(rootNode.left, min, rootNode.key) and isBST(rootNode.right, rootNode.key, max)
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
      a, b, c = map(int, sys.stdin.readline().split())
      nodes[i] = Node(a, b, c)
    if isBST(0, float('-inf'), float('inf')):
        print('CORRECT')
    else:
        print('INCORRECT')
    

threading.Thread(target=main).start()


