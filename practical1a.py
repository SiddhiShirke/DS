Array1 =[2,3,5,4,6,1]
print(" Array 1",Array1)


def Sort(arr):
    for i in range (0,len(arr)-1):
        for j in range (0,len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
Sort(Array1)
print("Sorted Array 1",Array1)
def search():
    i =int(input("Enter element to search in the list:"))
    if i in Array1:
        print("The element is in the list")
    else:
        print("The element is not in the list")
search()

def  reverse():
    print("Reversing the list :",Array1[::-1])

reverse()



Array2 = [8,9,7,10]
print("List2 :",Array2)

Sort(Array2)
print("Sorted list 2 :",Array2)

def merge_list(arr1,arr2):
    for i in range(len(arr2)):
        arr1.append(arr2[i])
    print("Merging both the lists :",arr1)
merge_list(Array1,Array2)

