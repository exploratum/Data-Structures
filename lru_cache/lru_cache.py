from doubly_linked_list import DoublyLinkedList, ListNode

class LRUCache:
  """
  Our LRUCache class keeps track of the max number of nodes it
  can hold, the current number of nodes it is holding, a doubly-
  linked list that holds the key-value entries in the correct 
  order, as well as a storage my_dict that provides fast access
  to every node stored in the cache.
  """
  def __init__(self, limit=10):
    self.limit = limit
    self.holding = 0
    self.dll = DoublyLinkedList()
    self.my_dict = {}

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the end of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    
    #find value in dictionary
    value = self.my_dict.get(key)

    if value != None:
      
      #find corresponding node and move it to end of queue
      current = self.dll.head
      while current:
        if key in current.value.keys():
          self.dll.move_to_end(current)
          return value
        current = current.next

    else:
      return None
      
  

  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):
    
    #check if key already exists, if yes update the value
    if key in self.my_dict:

      #update dictionary
      self.my_dict.update({key:value})


      # update double link list
      current = self.dll.head
      while current:
        if hasattr(current.value, key):
          current.value.key = value
          break

        current = current.next
      
    #if new key  
    else:

      #still have space in linked list
      if self.holding < self.limit:

        #update dictionary
        self.my_dict.update({key:value})

        # update double link list
        self.dll.add_to_tail({key: value})

        self.holding += 1

      #list is full
      else:

        #remove linked list head info from dictionary
        head_key = list(self.dll.head.value.keys())[0]
        self.my_dict.pop(head_key)

        #remove head from linked list
        self.dll.remove_from_head()

        #add new node info in dictionary
        self.my_dict.update({key: value})

        #Add new node at end of queue (tail)
        self.dll.add_to_tail({key: value})

        
        



