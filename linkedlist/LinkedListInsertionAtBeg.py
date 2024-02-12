class Node:
  def __init__(self,data):
      self.data=data
      self.next=None

class LinkedList:
  def __init__(self):
      self.head=None

  def InsertAtBeg(self,data):
      new_node=Node(data)
      new_node.next=self.head
      self.head=new_node

  def printlist(self):
      current=self.head
      while current:
          print(current.data,end="->")
          current=current.next
      print("None")


linkedlist=LinkedList()
linkedlist.InsertAtBeg(10)
linkedlist.InsertAtBeg(20)
linkedlist.InsertAtBeg(30)

linkedlist.printlist()