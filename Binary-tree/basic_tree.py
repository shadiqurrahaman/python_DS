class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    self.root = Node(0)
    
  def push(self,data):
    
