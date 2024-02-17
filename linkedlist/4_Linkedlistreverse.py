class Node:
  def __init__(self,data):
      self.data=data
      self.next=None

class LinkedList:
  def __init__(self):
      self.head=None
  def reverse(self):
      prev=None
      current=self.head
      while current != None:
          next=current.next
          current.next=prev
          prev=current
          current=next
      self.head=prev

  def push(self,data):
      new_node=Node(data)
      new_node.next=self.head
      self.head=new_node

  def printlist(self):
      curr=self.head
      while curr != None:
          print(curr.data,end=" ")
          curr=curr.next


llist=LinkedList()
llist.push(10)
llist.push(20)
llist.push(30)
llist.push(40)
llist.printlist()
llist.reverse()

print("\n")
llist.printlist()