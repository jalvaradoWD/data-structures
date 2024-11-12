import random


class Node:
	def __init__(self, val, prev=None, next=None):
		self.val = val
		self.prev = prev
		self.next = next

	def __repr__(self) -> str:
		return f"<Node {self.val}>"


class LinkedList:
	def __init__(self, head: Node, tail: Node | None = None):
		self.head = head
		self.tail = tail

	def append(self, node: Node):
		if self.tail is None:
			self.tail = node
			self.tail.prev = self.head
			self.head.next = self.tail
			return
		elif self.tail:
			self.tail.next = node
			node.prev = self.tail
			self.tail = node

	def prepend(self, node: Node):
		node.next = self.head
		self.head.prev = node
		self.head = node

	def insert(self, node: Node, index: int):
		current = self.head
		counter = 0

		if index == 0:
			self.prepend(node)
			return

		while current.next is not None:
			if counter == index:
				if current.prev is not None:
					current.prev.next = node
				node.prev = current.prev
				node.next = current
				current.prev = node
				current = node
				return
			counter += 1
			current = current.next

		self.append(node)

	def delete(self, index: int):
		current = self.head
		counter = 0

		while current.next is not None:
			if counter == index:
				if current.prev is not None:
					current.prev.next = current.next
				break
			counter += 1
			current = current.next

		if current.prev is not None:
			current.prev.next = current.next

	def bubble_sort(self):
		# [10, 1, 11]
		current = self.head
		test = self.list_values()
		is_sorted = None

		while current is not None and current.next is not None:
			if current.val > current.next.val:
				# if current is greater than next
				# then swap current and next locations
				if current.prev is not None:
					current.prev.next = current.next

				if current.next is not None:
					current.next.prev = current.prev

				current.prev = current.next

				current.next = current.prev.next
				current.prev.next = current
				if current == self.head:
					self.head = current.prev

				is_sorted = False

			current = current.next
			test = self.list_values()

			if current is None and is_sorted == False:
				current = self.head
			elif is_sorted == True:
				break

	def list_values(self):
		current = self.head
		res = []
		while current.next is not None:
			res.append(current)
			current = current.next
		res.append(current)
		return res


ll = LinkedList(Node(2))

test_list = [3,1,56,1,2,3]

for val in test_list:
	ll.append(Node(val))

ll.bubble_sort()
print(ll.list_values())
