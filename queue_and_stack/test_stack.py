import unittest
from dll_stack import Stack

class QueueTests(unittest.TestCase):
  def setUp(self):
    self.q = Stack()

  def test_len_returns_0_for_empty_queue(self):
    self.assertEqual(self.q.len(), 0)

  def test_len_returns_correct_length_after_push(self):
    self.assertEqual(self.q.len(), 0)
    self.q.push(2)
    self.assertEqual(self.q.len(), 1)
    self.q.push(4)
    self.assertEqual(self.q.len(), 2)
    self.q.push(6)
    self.q.push(8)
    self.q.push(10)
    self.q.push(12)
    self.q.push(14)
    self.q.push(16)
    self.q.push(18)
    self.assertEqual(self.q.len(), 9)
  
  def test_empty_dequeue(self):
    self.assertIsNone(self.q.pop())
    self.assertEqual(self.q.len(), 0)

  def test_dequeue_respects_order(self):
    self.q.push(100)
    self.q.push(101)
    self.q.push(105)
    self.assertEqual(self.q.pop(), 105)
    self.assertEqual(self.q.len(), 2)
    self.assertEqual(self.q.pop(), 101)
    self.assertEqual(self.q.len(), 1)
    self.assertEqual(self.q.pop(), 100)
    self.assertEqual(self.q.len(), 0)
    self.assertIsNone(self.q.pop())
    self.assertEqual(self.q.len(), 0)

if __name__ == '__main__':
  unittest.main()


    
