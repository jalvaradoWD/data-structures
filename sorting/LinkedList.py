from random import randint

class Node:
	def __init__(self, val=None, prev=None, next=None):
		self.val = val
		self.prev = prev
		self.next = next

	def __repr__(self) -> str:
		return f"{self.val}"


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

	def bubble_sort_data(self):
		# [10, 1, 11]
		current = self.head
		counter = 0

		while True:
			while current is not None and current.next is not None:
				if current.val > current.next.val:
					next_val_holder = current.next.val
					current.next.val = current.val
					current.val = next_val_holder
					counter += 1
				current = current.next

			if counter > 0:
				current = self.head
				counter = 0
			else:
				break


	def bubble_sort_memory(self):
		"""
		This is the bubble sort method where the sorting
		happens in the links to a node's memory location,
		rather than having to swap that data values of the
		node.
		"""
		current = self.head
		next_holder = None
		prev_holder = None
		counter = 0
		list_view = self.list_values()

		while True:
			while current.next is not None:
				next_holder = current.next
				if current.val >  next_holder.val:
					if prev_holder is not None:
						prev_holder.next = next_holder
						current.next = next_holder.next
						next_holder.next = current
					counter += 1
				prev_holder = current
				current = next_holder
				list_view = self.list_values()

			if counter > 0:
				current = self.head
				counter = 0
				next_holder = None
				prev_holder = None
				list_view = self.list_values()
			else:
				break

	def get_mid(self, head: Node):
		slow, fast = head, head.next
		while fast and fast.next:
			slow = slow.next # type: ignore
			fast = fast.next.next
		return slow

	def list_values(self):
		current = self.head
		res = []
		while current.next is not None:
			res.append(current.val)
			current = current.next
		res.append(current.val)
		return res



def sort_number_in_file(ll:LinkedList | None, filepath:str):
	file_vals = open(filepath, 'r')

	with file_vals as f:
		for val in f.readlines():
			new_node = Node(int(val[:-1]))
			if ll is None:
				ll = LinkedList(new_node)
			else:
				ll.append(new_node)

	file_vals.close()

	new_file = open(filepath, 'w')
	with new_file as f:
		if ll is not None:
			ll.bubble_sort_data()
			sorted_list = ll.list_values()
			sorted_buffer = []

			for i in sorted_list:
				sorted_buffer.append(f"{i}\n")

			f.writelines(sorted_buffer)
	new_file.close()


ll = LinkedList(Node(0))

for i in range(1000):
	ll.append(Node(randint(0, 1000)))


print(f"Unsorted List:\n{ll.list_values()}\n")

ll.bubble_sort_memory()
print(f"Sorted List:\n{ll.list_values()}\n")
