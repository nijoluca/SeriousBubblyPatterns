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

  def search(self,x):
      current=self.head
      while current != None:
          if current.data == x:
              return True
          current=current.next
      return False

ll=LinkedList()
ll.push(10)
ll.push(90)
ll.push(78)
ll.push(56)
ll.push(89)

if ll.search(900):
  print("Yes")
else:
  print("No")
