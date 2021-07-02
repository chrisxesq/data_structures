
import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        if self.n==0:
            print('CORRECT')
            return 0
        else:
            self.key = [0 for i in range(self.n)]
            self.left = [0 for i in range(self.n)]
            self.right = [0 for i in range(self.n)]
            for i in range(self.n):
                [a, b, c] = map(int, sys.stdin.readline().split())
                self.key[i] = a
                self.left[i] = b
                self.right[i] = c

    def inOrder(self, root,list=[]):
        if root == -1:
            return []
        self.inOrder(self.left[root])
        list.append(self.key[root])
        self.inOrder(self.right[root])
        return list
    
def isBST(list):
    ans='CORRECT'
    if len(list)==0: 
        print(ans)
        return 0
    
    for index in range(len(list)):
       try:  
            if list[index]>list[index+1]:
                ans='INCORRECT'
                break
       except:
           pass 
    print(ans)    
        
def main():
    tree = TreeOrders()
    tree.read()
    listi=tree.inOrder(0)
    isBST(listi)
    
    
    #     for i in range(n_nodes):
    #     a, b, c = map(int, input().split())
    #     node = Node(a, b, c)
    #     nodes[i] = node
    # if n_nodes == 0 or IsBinarySearchTree(nodes, n_nodes):
    #     print('CORRECT')
    # else:
    #     print('INCORRECT')
    

    
    

    


threading.Thread(target=main).start()
