class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LL:
	def __init__(self):	
		self.headNode = None
	seen = []
	def trav(self):
		if(self.headNode):
			checkNode = self.headNode
			print checkNode.data
			while checkNode.next:
				next = checkNode.next
				print next.data
				checkNode = next
	def append(self, Node):
		if(self.headNode):
			checkNode = self.headNode
			while(checkNode.next):
				checkNode = checkNode.next
			checkNode.next = Node
	def Dups(self):
		prev = None
		cur = self.headNode
		while cur:
			if cur.data in self.seen:
				prev.next = cur.next
			else:
				self.seen.append(cur.data)
			prev = cur
			cur = cur.next
	def Dups2(self):
		node1 = self.headNode
		node2 = node1.next
		node2_p = node1
		while node1:
			while node2:
				if node2.data==node1.data:
					node2_p.next = node2.next
				else:
					node2_p = node2
				node2 = node2.next
			node1 = node1.next
			node2 = node1.next
			node2_p = node1

ll = LL()
ll.headNode = Node(1)

ll.append(Node(2))
ll.append(Node(3))
ll.append(Node(4))
ll.append(Node(5))
ll.append(Node(6))
ll.append(Node(7))
ll.append(Node(8))
ll.append(Node(9))
ll.append(Node(10))