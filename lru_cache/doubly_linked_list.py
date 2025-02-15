"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    new_node = ListNode(value, None, None)
    self.length += 1
    if not self.head and not self.tail:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node

  def remove_from_head(self):
    if not self.head and not self.tail:
      return None
    self.length -= 1
    if self.head == self.tail:
      current_head = self.head
      self.head = None
      self.tail = None
      return current_head.value
    current_head = self.head
    self.head = self.head.next
    self.head.prev = None
    return current_head.value

  def add_to_tail(self, value):
    new_node = ListNode(value, None, None)
    self.length += 1
    if not self.tail and not self.head:
      self.tail = new_node
      self.head = new_node
    else:
      new_node.prev = self.tail
      self.tail.next = new_node
      self.tail = new_node

  def remove_from_tail(self):
    pass

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    value = node.value
    if node is self.head:
      self.remove_from_head()
      self.add_to_tail(value)
    else:
      node.delete()
      self.length -= 1
      self.add_to_tail(value)

  def delete(self, node):
    pass
    
  def get_max(self):
    pass