class Node: 
    def __init__ (self, element, next = None ):
        self.element = element
        self.next = next
        
    def display(self):
        print(self.element)

class LinkedList:
    
        
    def __init__(self):
        self.head = None
        self.size = 0
        
    def _len_(self):
        return self.size
    
    def get_head(self):
        return self.head
    
    def is_empty(self):
        return self.size == 0 
    
    def display(self):
        if self.size ==0:
            print("no element")
        first = self.head
        i=3 
        print(first.element.element,"x ^",i,"+",end="")
        first = first.next
        i=2
        while first:
            if i == 0 :
                 print(first.element,"x ^",i)
            else:
                print(first.element,"x ^",i," ",end="+" )
            
            i=i-1
            first = first.next
            
    def add_head(self,e):
        temp = self.head 
        self.head = Node(e)
        self.head.next = temp
        self.size += 1 
        
    def get_tail(self):
        last_object = self.head
        while (last_object.next != None):
            last_object = last_object.next
        return last_object
        
    
            
    def add_tail(self,e):
        new_value = Node(e)
        self.get_tail().next = new_value
        self.size += 1
        
    def get_node_at(self,index):
        element_node = self.head
        counter = 0
        if index == 0:
            return element_node.element
        if index > self.size-1:
            print("Index out of bound")
            return None
        while(counter < index):
            element_node = element_node.next
            counter +=1
        return element_node
polynomial_order = 3

poly1 = LinkedList()
print("Polynomial 1:")

poly1.add_head(Node(int(input("coefficient for power {} : ".format(polynomial_order)))))
for i in reversed(range(polynomial_order)):
     poly1.add_tail(int(input("coefficient for power {} : ".format(i))))

print("\n")
poly2 = LinkedList()
print("Polynomial 2")

poly2.add_head(Node(int(input("coefficient for power {} : ".format(polynomial_order)))))
for i in reversed(range(polynomial_order)):
    poly2.add_tail(int(input("coefficient for power  {}: ".format(i))))

print("Adding cooeficients of polynomial 1 and 2 ")
poly1.display()

poly2.display()
print(poly1.get_node_at(0).element + poly2.get_node_at(0).element, "x^3 + " , 
         poly1.get_node_at(1).element + poly2.get_node_at(1).element, "x^2 + ",
         poly1.get_node_at(2).element + poly2.get_node_at(2).element, "x + ",
         poly1.get_node_at(3).element + poly2.get_node_at(3).element)

