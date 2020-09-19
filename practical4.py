#First in first out

class Queue_operation:    
    def __init__(self):
        self.head=None
        self.tail=None
        self.data =[]
        print("Original List")
        print(self.data)
        
    
    def is_empty():
        if len(self.data)==0:
            return 0
        else:
            return 1

    def dequeue(self):
        if  (self.is_empty)==0:
             print ("List is Empty")
        else:
            print("First element",self.data[0])
            self.head=self.data[1]
            self.data.pop(0)
            print("Removed first element")
            print(self.data)
            print("Head = > ",self.head)
            
           
    

    def enqueue(self,e):
        print("Adding  to the last")
        self.data.append(e)
        print(self.data)
        self.head=self.data[0]
        self.tail=e
        print("Tail = > ",self.tail)
        print("Head => ",self.head)
    def get_first_element(self):
        print("Element  to be removed next will be",self.data[0])

    def get_last_element(self):
        print("Element  to be removed last will be",self.data[-1])
        

   
            
ob =Queue_operation()
ob.is_empty
ob.enqueue(1)
ob.enqueue(2)
ob.enqueue(3)
ob.enqueue(4)
ob.dequeue()
ob.enqueue(5)
ob.enqueue(6)
ob.enqueue(7)
ob.dequeue()
ob.enqueue(8)
ob.dequeue()
ob.dequeue()
ob.get_first_element()
ob.get_last_element()

