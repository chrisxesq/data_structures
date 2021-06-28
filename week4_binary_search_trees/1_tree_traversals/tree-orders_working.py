# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self,start):
    if start == -1:
        return 0
    self.inOrder(self.left[start])
    print(self.key[start], end=' ')
    self.inOrder(self.right[start])
    
  def preOrder(self, start):
    if start == -1:
        return 0
    print(self.key[start], end=' ')
    self.inOrder(self.left[start])
    self.inOrder(self.right[start])

  def postOrder(self, start):
    if start == -1:
        return 0
    self.inOrder(self.left[start])
    self.inOrder(self.right[start])
    print(self.key[start], end=' ')

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()

nodes = 5
input = [[4,1,2],[2,3,4],[5,-1,-1],[1,-1,-1],[3,-1,-1]]
result=[]
prep=[]
for _ in input:
    prep.append(_[0])
