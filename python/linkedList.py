class Node(object):

	#initialize method constructor
	#whenever we instatiate node, we will specify the data contained by that node
	def _init_(self, data):

		#initialize data that will be stored in node
		self.data = data

		#initialize reference to next node
		self.nextNode = None


class LinkedList(object):

	def _init_(self):

		#initalize first term
		self.head = None

		#initalize size of list
		self.size = 0


	#inserts data at the beginning of the list
	def insertStart(self, data):

		#increment by one when you insert
		self.size = self.size + 1
		newNode = Node(data)

		#if there is no first node and the list is empty:
		if not self.head:
			self.head = newNode

		else:
			#the new node that is added is now placed at the head of the list
			#using nextNode function
			newNode.nextNode = self.head

	def remove(self, data):
		if self.head is None:
			return

		self.size = self.size -1 

		#start from beginning of list
		currentNode = self.head

		#initialize previous node
		previousNode = None

		while currentNode.data != data:
			previousNode = currentNode
			currentNode = currentNode.nextNode

		#if the node we want to remove is the first node in the list:
		if previousNode is None:

			#the second node now becomes the first node (head)
			self.head = currentNode.nextNode
		else:
			#previous node now points to the 3rd node, skipping the node we want to remove
			previousNode.nextNode = currentNode.nextNode

	def size(self):
		return self.size

	def insertEnd(self, data):

		self.size = self.size + 1
		newNode =  Node(data)

		#initialize variable that we are focusing on as our area of reference
		#we start from the first node because linked list is linear
		actualNode = self.head

		#we need to find the node that has self.nextNode = None
		while actualNode.nextNode is not None:
			actualNode = actualNode.nextNode

		#we have arrived at the end of the list
		actualNode.nextNode = newNode

	def traverseList(self):

		actualNode = self.head

		while actualNode is not None:
			#print out each node from the beginning while not at the end and then increment
			print("%d " %  actualNode.data)
			actualNode = actualNode.nextNode


#instatiate object for the class
linkedlist = LinkedList()

#run throught he insertStart method and pass it the values below
linkedlist.insertStart(12)
linkedlist.insertStart(122)
linkedlist.insertStart(3)
linkedlist.insertEnd(31)

linkedlist.traverseList()
