import unittest
from laba12_3_2 import DoublyLinkedList

class DoublyLinkedListTest(unittest.TestCase):
    def setUp(self):
        self.list1 = DoublyLinkedList()
        self.list1.add_node(1)
        self.list1.add_node(2)
        self.list1.add_node(3)
        
        self.list2 = DoublyLinkedList()
        self.list2.add_node(0)
        self.list2.add_node(1)
        self.list2.add_node(2)
        self.list2.add_node(3)
        self.list2.add_node(4)

    def test_add_node(self):
        self.assertEqual(self.list1.head.data, 1)
        self.assertEqual(self.list1.head.next.data, 2)
        self.assertEqual(self.list1.head.next.next.data, 3)
        
    def test_contains_list(self):
        self.assertTrue(self.list2.contains_list(self.list1, self.list2))
        
if __name__ == '__main__':
    unittest.main()

