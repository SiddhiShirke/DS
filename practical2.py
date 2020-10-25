class Node:
    def __init__(self, data,next=None):
        self.prev = None
        self.next = next
        self.data = data
        self.head=None
        self.size = 0
        self.tail = None
    def display(self):
        print(self.data)
    def is_empty(self):
        return self.size == 0
        #ADDING AT START
    def add_front(self,value):
        temp = self.head
        self.head = Node(value)
        self.head.next = temp
        self.size += 1

    def get_tail(self):
        last_obj = self.head
        while(last_obj.next != None):
            last_obj = last_obj.next
        return last_obj

#Delete front
    def delete_front(self):
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1

    def find_2nd_last_value(self):
        if (self.size >= 2):
            first = self.head
            temp = self.size-2
            while temp >0:
                first = first.next
                temp -= 1
            return first
        else:
            print("Size not sufficient")
        return None
    
#ADDING LAST
    def add_last(self,value):
        new_value = Node(value)
        self.get_tail().next = new_value
        self.size += 1
#DELETE LAST
    def delete_last(self):
        if   (self.is_empty()):
           print  ("Empty list")
        elif self.size == 1:
            self.head == None
            self.size -= 1
        else:
            Node = self.find_2nd_last_value()
            if Node:
                Node.next =None
                self.size -= 1
    def display(self):
        newest = self.head
        while newest:
            print(newest.data,end=',  ')
            newest = newest.next
        print()
        


    def get_node_at(self,index):
        element_node = self.head
        counter = 0
        if index > self.size-1:
            print("Index out of bound")
            return None
        while(counter < index):
            element_node = element_node.next
            counter += 1
        return element_node
    
 #Deleting in between    
    def remove_between_list(self,position):
        if position > self.size-1:
            print("Index out of bound")
        elif position == self.size-1:
            self.remove_tail()
        elif position == 0:
            self.remove_head()
        else:
            prev_node = self.get_node_at(position-1)
            next_node = self.get_node_at(position+1)
            prev_node.next = next_node
            self.size -= 1

                
    def reverse_list(self):
        first = self.head
        second = first.next
        first.next = None
        first.prev = second
        while second is not None:
            second.prev =second.next
            second.next =first
            first=second
            second = second.prev
        self.head = first
        
    def search (self,search_value):
            index = 0 
            while (index < self.size):
                value = self.get_node_at(index)
                
                if value.data == search_value:
                    print(value.data, "  value found at " , " location   ", str(index) )
                    return True
                index += 1
            print("Not Found")
            return False
    def merge(self,linkedlist_value):
        if self.size > 0:
            last_node = self.get_node_at(self.size-1)
            last_node.next = linkedlist_value.head
            self.size = self.size + linkedlist_value.size
            
        else:
            self.head = linkedlist_value.head
            self.size = linkedlist_value.size        
        

        
obj = Node(1)
obj1 = Node(1)
obj1.add_front(12)
obj1.add_front(11)
obj1.add_front(10)
print("Linked List 1")
obj1.display()
obj.add_front(1)
obj.add_front(2)
obj.add_front(3)
obj.add_front(4)
obj.add_front(5)
obj.add_front(6)
obj.display()
print("Delete from front")
obj.delete_front()
obj.display()
obj.get_tail()
obj.add_last(7)
obj.add_last(8)
obj.add_last(9)
obj.add_last(10)
obj.display()
print("Delete 10 ")
obj.delete_last()
obj.display()
print("Delete 5th element ")
obj.remove_between_list(5)
obj.display()
obj.search(2)
obj.display()
print("Reversing the list")
obj.reverse_list()
obj.display()
print("Merging two linked list")
obj.merge(obj1)
obj.display()

