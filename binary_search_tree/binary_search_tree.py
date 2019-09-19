import sys
# sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


  def insert(self, value):

    if value == self.value:
      return

    if value < self.value:
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    
    elif value > self.value:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)
    



  def contains(self, target):

    if self.value == target:
      return True

    if self.left and target == self.left.value:
      return True

    if self.right and target == self.right.value:
      return True

    if target < self.value:

      if self.left:
        return self.left.contains(target)
      else:
        return False

    else:
      if self.right:
        return self.right.contains(target)
      else:
        return False


  def get_max(self):

    num = self.value

    #max can only be to the right
    if self.right:
      num = self.right.get_max()
  
    return num


  def for_each(self, cb):
    cb(self.value)

    if self.right:
      self.right.for_each(cb)

    if self.left:
      self.left.for_each(cb)


  # Print all the values in order from low to high
  # Hint:  Use a recursive, depth first traversal
  def in_order_dft(self, node):

    if not node.left and not node.right:
      print(node.value)
      return
    
    if node.left:
      node.in_order_dft(node.left)
      print(node.value)

    if node.right:
      #if there were a node to the left the parent value already printed from above
      if not node.left:
        print(node.value)
      node.in_order_dft(node.right)



  # Print the value of every node, starting with the given node,
  # in an iterative breadth first traversal
  def bft_print(self, node):

    q = Queue()
    q.enqueue(node)

    while q.len() > 0:
      first_node = q.dequeue()
      print(first_node.value)
      if first_node.left:
        q.enqueue(first_node.left)
      if first_node.right:
        q.enqueue(first_node.right)


  # Print the value of every node, starting with the given node,
  # in an iterative depth first traversal
  def dft_print(self, node):
      s = Stack()
      s.push(node)

      while s.len() > 0:
        top_node = s.pop()
        print(top_node.value)
        if top_node.left:
          s.push(top_node.left)
        if top_node.right:
          s.push(top_node.right)


  # STRETCH Goals -------------------------
  # Note: Research may be required

  # Print In-order recursive DFT
  def pre_order_dft(self, node):
      pass

  # Print Post-order recursive DFT
  def post_order_dft(self, node):
      pass

