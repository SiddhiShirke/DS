class Stack_operations:
    def __init__(self):
        self.list = []
    #last in first out
    def is_empty(self):
        if len(self.list)==0:
            return 0
        else:
            return 1
    def  push(self,item):
        self.list.append(item)
        print(self.list)

    def pop(self):
        if (self.is_empty == 0):
            return "List is empty"
        else:
            self.list.pop()
            print("Removing last in element")
            print(self.list)
            
    def  top_item(self):
        if (self.is_empty() == 0):
            return "List is empty"
        else:
            print("Element at the top is :",self.list[len(self.list)-1])
            
obj=Stack_operations()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.pop()
obj.top_item()

        
