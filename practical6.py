def bubbleSort(arr):
    for i in range (0,len(arr)-1):
        for j in range (0,len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


def selection (nlist):
    for i in range (len(nlist)- 1):
        index = 0
        for j in range(len(nlist)-i):
            if nlist[j] > nlist[index]:
                index = j
            nlist[len(nlist)-i-1],nlist[index] = nlist[index],nlist[len(nlist)-i-1]
        return nlist

def insertion_sort(list1):
    for i in range(1,len(list1)):
        key = list1[i]
        j = i-1
        while j >= 0 and key < list1[j]:
            list1[j+1] = list1[j]
            j=j-1
        list1[j+1]=key
    return list1


alist=[4,0,30,22,-23,67,1,-7]
n_list = ["apple","orange","melon","banana","pineapple"]
print("Before any  sort",alist)
print("Before any sort",n_list)
choose =int(input("Enter choice Bubble Sort as 1,Insertion Sort as 2, Selecction Sort as 3 : "))
if choose == 1 :
    print("After bubble sort",bubbleSort(alist))
    print("After bubble sort",bubbleSort(n_list))
elif choose==2:
    print("After  insertion sort",insertion_sort(alist))
    print("After  insertion sort",insertion_sort(n_list))
elif choose==3:
    print("After selection  sort",selection(alist))
    print("After selection  sort",selection(n_list))
else:
    print("Invalid choice")

'''print("Before any  sort",alist)
print("After bubble sort",bubbleSort(alist))
print("After selection  sort",selection(alist))
print("After  insertion sort",insertion_sort(alist))
print("Before any sort",n_list)
print("After bubble sort",bubbleSort(n_list))
print("After selection  sort",selection(n_list))
print("After  insertion sort",insertion_sort(n_list))
'''
