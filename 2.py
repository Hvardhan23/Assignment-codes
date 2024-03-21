class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class NodeOperation:

	def pushNode(self, head_ref, data_val):
		new_node = Node(data_val)
		new_node.next = head_ref
		head_ref = new_node
		return head_ref

	# to print a given linked list
	def printNode(self, head):
		while (head != None):
			print('%d->' % head.data, end="")
			head = head.next
		print("NULL")
		
    #finding length
	def getLen(self, head):
		temp = head
		len = 0
		while (temp != None):
			len += 1
			temp = temp.next
		return len

	def printMiddle(self, head):
		if head is not None:
			slow_ptr = head
			fast_ptr = head
			prev_to_slow = None  # This variable will keep track of the previous node to slow_ptr
			while fast_ptr is not None and fast_ptr.next is not None:
				prev_to_slow = slow_ptr  # Update prev_to_slow before moving slow_ptr and fast_ptr
				slow_ptr = slow_ptr.next
				fast_ptr = fast_ptr.next.next
			print('The middle element(s) is/are: ', slow_ptr.data)
			if fast_ptr is None:
            # If fast_ptr is None, the length of the list is even,
            # so we print the previous element of slow_ptr
				print('The other middle element(s) is/are: ', prev_to_slow.data)

head = None
S1 = NodeOperation()
head = S1.pushNode(head, 5)
head = S1.pushNode(head, 4)
head = S1.pushNode(head, 3)
head = S1.pushNode(head, 2)
head = S1.pushNode(head, 1)
S1.printNode(head)
S1.printMiddle(head)

head = None
S2 = NodeOperation()
head = S2.pushNode(head, 6)
head = S2.pushNode(head, 5)
head = S2.pushNode(head, 4)
head = S2.pushNode(head, 3)
head = S2.pushNode(head, 2)
head = S2.pushNode(head, 1)
S2.printNode(head)
S2.printMiddle(head)