class Node:
  def __init__(self,data):
      self.data=data
      self.next=next

class LinkedList:
  def __init__(self):
      self.head=None
  def push(self,data):
      new_node=Node(data)
      new_node.next=self.head
      self.head=new_node

  def identical(self,list2):
      a=self.head
      b=list2.head
      while (a != None and b!=None):
          if (a.data != b.data):
              return False
          a=a.next
          b=b.next
      return (a == None and b==None)


if __name__ == "__main__": 
llist1 = LinkedList() 
llist2 = LinkedList() 


llist1.push(1) 
llist1.push(2) 
llist1.push(3) 
llist2.push(1) 
llist2.push(2) 
llist2.push(3) 


if (llist1.identical(llist2) == True): 
    print("Identical ") 
else: 
    print("Not identical ") 
