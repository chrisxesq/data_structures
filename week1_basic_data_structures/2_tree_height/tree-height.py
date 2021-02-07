# python3
from collections import deque
import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

            
        def compute_height(self):
            #iterate the list one time and set key value pair as 
            #[parent node: child nodes]
            
            reference_dict = {}
            for child_aka_index, self.parent in enumerate(self.parent):
                try:
                    reference_dict[self.parent].add(child_aka_index)
                except KeyError:
                    reference_dict[self.parent]={child_aka_index}
            
            #traverse every level of the tree
            #FIFO so a linked list or a deque can save time 
            traverse_nodes = deque(reference_dict[-1])

            #used the root node to set up the deque already 
            reference_dict.pop(-1)
            
            height = 0
            track_traverse_nodes_deque_length = 1

            while True:
              if track_traverse_nodes_deque_length == 0:
                  return height
              height += 1
              track_current_lvl_nodes = track_traverse_nodes_deque_length 
              while track_current_lvl_nodes > 0:
                  current_node = traverse_nodes.popleft()
                  track_current_lvl_nodes -= 1 
                  track_traverse_nodes_deque_length -= 1
                  try:
                      for child in reference_dict[current_node]:
                          traverse_nodes.append(child)
                          track_traverse_nodes_deque_length += 1
                  except KeyError:
                      pass



def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())

threading.Thread(target=main).start()
