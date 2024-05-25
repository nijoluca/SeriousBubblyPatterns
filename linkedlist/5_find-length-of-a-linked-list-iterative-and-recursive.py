class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class LinkeList:
  def __init__(self):
    self.head=None
  def push(self,data):
    new_node=Node(data)
    new_node.next=self.head
    self.head=new_node

  def printlist(self):
    last=self.head
    while last:
      print(last.data,end=" ")
      last=last.next
    print(" ")
  def count(self):
    count=0
    last=self.head
    while last:
      count += 1
      last=last.next
    return count

if __name__=='__main__':
  ll=LinkeList()
  ll.push(283)
  ll.push(8548)
  ll.push(45)
  ll.push(34664)
  ll.push(36774)
  ll.printlist()
  c=ll.count()
  print(c)