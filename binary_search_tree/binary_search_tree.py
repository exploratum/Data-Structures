import sys
sys.path.append('../queue_and_stack')
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


  # def in_order_print():

