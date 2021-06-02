class node:
	def __init__(self,data=None):
		self.data=data
		self.next=None
		self.prev=None

class Ll:
	def __init__(self):
		self.head=node()
		self.tail=node()

	def apf(self,data):
		nN=node(data)
		nN.next=self.head
		self.head.prev=nN
		self.head=nN

	def ap(self,data):
		nN=node(data)
		if self.head.data==None :
			self.head=nN
		else:
			self.tail.next=nN
		nN.prev=self.tail
		self.tail=nN

	def print_l(self):
		current=self.head
		while current != None:
			if(current.data!=None):
				print(current.data)
			current=current.next

	def print_r(self):
		current=self.tail
		while current != None:
			if(current.data != None):
				print(current.data)
			current=current.prev

	def length(self):
		current=self.head
		s=1
		while current.next!=None:
			s+=1
			current=current.next
		print(s)


b=Ll()
a=[3,2,1,0,-1,-2,2,3,4,5]
for i in a:
	b.ap(i)

b.print_l()
print("\n")

b.length()