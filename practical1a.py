l1 =[1,2,3,4,5,6]
print(" list 1",l1)
l1.sort()
print("Sorted list 1",l1)

def search():
    i =int(input("Enter element to search in the list:"))
    if i in l1:
        print("The element is in the list")
    else:
        print("The element is not in the list")
search()

def  reverse():
    print("Reversing the list :",l1[::-1])

reverse()

l2 = ["dog","cat","mouse","rat"]
print("List2 :",12)

l2.sort()
print("Sorted list 2 :",l2)

def merge_list():
    l3=l1+l2
    print("Merging both the lists :",l3)
merge_list()

