class TreeOrders:
  def read(self):
    self.key = []
    self.left = []
    self.right = []
    [a, b, c] = [[4,2,5,1,3],[1,3,-1,-1,-1],[2,4,-1,-1,-1]]
    self.key = a
    self.left = b
    self.right = c

  def inOrder(self):
    self.result=[]
    start = 0
    print(start)
    def printInOrder(self):
          
    if self.left[start] != -1:
        start = self.left[start]
        self.inOrder(start)
    self.result.append(self.key[start])
     
    if self.right[start] != -1:
        start= self.right[start]
        
    
    
tree = TreeOrders()
tree.read() 
tree.inOrder()