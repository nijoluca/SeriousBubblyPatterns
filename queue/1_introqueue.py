class Queue:
 
  def __init__(self, cap):
      self.cap = cap
      self.front = 0
      self.size = 0
      self.rear = cap - 1
      self.arr = [0] * cap

  
  @classmethod
  def createQueue(cls, cap):
      return cls(cap)


my_queue = Queue.createQueue(5)
print("Queue Capacity:", my_queue.arr)