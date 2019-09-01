class Q_SNode:
	def __init__(self,data):
		self.data = data
		self.next = None

class Q:
	def __init__(self):
		self.head = self.tail = None
	def enQ(self,val):
		val = Q_SNode(val)
		if self.empty():
			self.head = self.tail = val
		else:
			self.tail.next = val
			self.tail = val
	def deQ(self):
		if not self.empty():
			if self.head == self.tail:
				top = self.head.data
				self.head = self.tail = None
				return top
			top = self.head
			self.head = self.head.next
			return top.data
	def empty(self):
		return self.head == self.tail == None
	def top(self):
		if not self.empty():
			return self.head.data

class stack:
	def __init__(self):
		self.head = None
	def push(self,val):
		val = Q_SNode(val)
		if self.is_empty():
			self.head = val
			return
		val.next = self.head
		self.head = val
	def pop(self):
		if self.is_empty():
			return
		top = self.head
		self.head = top.next
		return top.data
	def is_empty(self):
		return self.head==None
	def top(self):
		if self.is_empty():
			return
		return self.head.data


class llNode:
	def __init__(self,value,weight):
		self.value = value
		self.weight = weight
		self.next = None

class ll:
	def __init__(self):
		self.head = None
	def insert(self,value,weight):
		n = llNode(value,weight)
		if self.head == None:
			self.head = n
		curr_node = self.head
		while curr_node:
			if curr_node.value==value:
				curr_node.weight = weight
				return
			curr_node  = curr_node.next			
		n.next = self.head
		self.head = n
	def dele(self,value):
		if self.head:
			n = self.head
			prev = None
			if n.value==value:
				self.head = n.next
				return
			while n:
				if n.value==value:
					prev.next = n.next
					return
				prev = n
				n = n.next
	def trav(self):
		links = {}
		n = self.head
		while n:
			links[n.value] = n.weight
			n = n.next
		return links

def hash(val):
	return ord(val)%26

class hashT:
	def __init__(self):
		self.arr = [None]*26
	def insert(self,key,value,weight):
		ind = hash(key)
		if self.arr[ind] == None:
			self.arr[ind] = ll()
		self.arr[ind].insert(value,weight)
	def dele(self,key,value):
		ind = hash(key)
		if not self.arr[ind] == None:
			self.arr[ind].dele(value)
	def fetch(self,key):
		ind = hash(key)
		ret = {}
		if not self.arr[ind] == None:
			ret = self.arr[ind].trav()
		return ret



#Adjacency list representation
class diGraph:
	def __init__(self):
		self.HT = hashT()
	def insert(self,Node1,Node2,weight):
		self.HT.insert(Node1,Node2,weight)
	def dele(self,Node1,Node2):
		self.HT.dele(Node1,Node2)
	def neigh(self,Node):
		return self.HT.fetch(Node)
	def is_conn(self,Node1,Node2):
		return Node2 in self.HT.fetch(Node1)
	def route(self,node1,node2):
		q = Q()
		ret = [node1]
		q.enQ(node1)
		curr_node = node1
		while not q.empty():
			nei = self.HT.fetch(curr_node)
			if len(nei):
				for i in nei:
					if i==node2:
						return True
					if not i in ret:
						q.enQ(i)
						ret.append(i)
			q.deQ()
			curr_node = q.top()
		return False

class Graph:
	def __init__(self):
		self.HT = hashT()
	def insert(self,Node1,Node2,weight):
		self.HT.insert(Node1,Node2,weight)
		self.HT.insert(Node2,Node1,weight)
	def dele(self,Node1,Node2):
		self.HT.dele(Node1,Node2)
		self.HT.dele(Node2,Node1)
	def neigh(self,Node):
		return self.HT.fetch(Node)
	def is_conn(self,Node1,Node2):
		return Node2 in self.HT.fetch(Node1)
	#create sub arrays for each level
	#create validation function
	def BFS(self,node):
		q = Q()
		q.enQ(node)
		ret = [node]
		while not q.empty():
			node = q.top()
			neigh = self.neigh(node)
			for i in neigh:
				if not i in ret:
					q.enQ(i)
					ret.append(i)
			q.deQ()
		return ret
	def DFS_stck(self,node):
		s = stack()
		ret = []
		seen = [node]
		s.push(node)
		while not s.is_empty():
			skip = 0
			node = s.top()
			nei = self.neigh(node)
			for i in nei:
				if not i in seen:
					skip = 1
					s.push(i)
					seen.append(i)
					break
			if not skip:
					ret.append(node)
					s.pop()
		return seen





g1 = Graph()

g1.insert('j','c',0)
g1.insert('i','c',0)
g1.insert('g','h',0)
g1.insert('f','e',0)
g1.insert('e','b',0)
g1.insert('e','g',0)
g1.insert('e','h',0)
g1.insert('d','a',0)
g1.insert('d','c',0)
g1.insert('c','b',0)
g1.insert('b','a',0)
g1.insert('b','h',0)
g1.insert('b','g',0)



#g1.BFS('a')

