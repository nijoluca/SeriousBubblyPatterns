class Node:
  def __init__(self,data):
      self.data=data
      self.next=None
class LinkedList:
  def __init__(self):
      self.head=None
  def push(self,data):
      new_node=Node(data)
      new_node.next=self.head
      self.head=new_node

ll=LinkedList()
ll.push(99399)
ll.push(8848)
ll.push(78838)
ll.push(10)
ll.push(88338)


temp=ll.head
v=[]
while(temp):
  v.append(temp.data)
  temp=temp.next
x=103
if x in v:
  print("Yes")
else:
  print("No")