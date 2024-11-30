import random
from sorting.LinkedList import LinkedList, Node, sort_number_in_file

ll = LinkedList(Node(0))

print(ll.list_values())

def create_file_rand_ints(n:int):
	file = open("values.txt", "w")
	file2 = open("values_control.txt", "w")
	val_list = []
	for i in range(n):
		val_list.append(f"{random.randint(0, 1000)}\n")

	with file as f:
		f.writelines(val_list)
	with file2 as f:
		f.writelines(val_list)
	file.close()
	file2.close()

create_file_rand_ints(100)
sort_number_in_file(ll,"values.txt")

