def  linear_search(nlist,element):
    index_count = 0
    nlist_size = len(nlist)
    while index_count < nlist_size:
        temp = nlist[index_count]
        if temp == element:
            return index_count
        index_count += 1
    return -1



def binary(item,search,start,end):
    if start >end:
        return -1
    mid = (start+end)//2
    if item[mid] == search:
        return mid
    if search < item[mid]:
        return binary(item,search,start,mid-1)
    else:
        return binary(item,search,mid+1,end)
    
item_list = ["apple","orange","melon","banana","pineapple"]

choose = str(input("Enter your choice for binary or linear search :  ")).lower()


if choose == "binary":
    search_val = "apple"
    print(binary(item_list,search_val,0,len(item_list)))
    
elif choose == "linear":
    print(linear_search(item_list,"pineapple"))
    print(linear_search(item_list,"cherry"))
else:
    print("Invalid choice")


