class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None
		self.prev = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None
	
	def add_node(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
		else:
			self._add_node_recursive(self.head, new_node)

	def _add_node_recursive(self, current, new_node):
		if(current.next is None):
			current.next = new_node
			new_node.prev = current
			return
		self._add_node_recursive(current.next, new_node)
		
	def contains_list(self, list1, list2):
		return self._contains_list_recursive(list2.head, list1.head)
	
	def _contains_list_recursive(self, current_list2, current_list1):
		if current_list1 is None:
			return True
		if current_list2 is None:
			return False
		if current_list1.data == current_list2.data:
			return self._contains_list_recursive(current_list2.next, current_list1.next)
		return self._contains_list_recursive(current_list2.next, current_list1)
		
	def print_list(self):
		self._print_list_recursive(self.head)
	
	def _print_list_recursive(self, current):
		if current is None:
			return
		print(current.data, end=' ')
		self._print_list_recursive(current.next)


# Створення списків
list1 = DoublyLinkedList()
list1.add_node(1)
list1.add_node(2)
list1.add_node(3)

list2 = DoublyLinkedList()
list2.add_node(0)
list2.add_node(1)
list2.add_node(2)
list2.add_node(3)
list2.add_node(4)

# Роздрукування списків
print("List 1: ", end=" ")
list1.print_list()
print()

print("List 2: ", end=" ")
list2.print_list()
print()

# Перевірка наявності списку list1 в списку list2
if list2.contains_list(list1, list2):
    print("List 1 is a part of List 2")
else:
    print("List 1 is not a part of List 2")