class List:    
    def __init__(self):
        self.data =[1,2,3]
        print("Original List")
        print(self.data)
    
    def is_empty():
        if len(self.data)==0:
            return 0
        else:
            return 1

    def dequepopleft(self):
        if  (self.is_empty)==0:
             print ("List is Empty")
        else:
            print("First element",self.data[0])
            
            self.data.pop(0)
            print("Removed first element")
            print(self.data)
           
    def dequepopright(self):
        if (self.is_empty)==0:
             print ("List is Empty")
        else:
            print("Last  element",self.data[-1])
            
            self.data.pop()
            print("Removed last element")
            print(self.data)

    def dequeaddleft(self,e):
        print("Adding  to the right")
        self.data.append(e)
        print(self.data)
        

    def dequeaddright(self,e):
        self.data.insert(0,e)
        print("Adding to the left")
        print(self.data)
        #(dequeaddleft(123))
            
ob =List()
ob.is_empty
ob.dequepopleft()
ob.dequepopright()
ob.dequeaddleft(4)
ob.dequeaddright(5)
