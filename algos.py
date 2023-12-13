data = [4,33,5,77,3,99,6,2,14,7,1,8,12,9,22,10,0,11]

def merge_sort(list):
    if len(list) < 2:
        return list

    left = merge_sort(list[:len(list) // 2])
    right = merge_sort((list[len(list)//2:]))

    return merge(left, right)

def merge(left, right):
    srtd = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            srtd.append(left[i])
            i += 1
        else:
            srtd.append(right[j])
            j += 1

    while i < len(left):
        srtd.append(left[i])
        i += 1

    while j < len(right):
        srtd.append(right[j])
        j += 1

    return srtd

print(data)
print("Merge Sort - New List")
nlist = merge_sort(data)
print(nlist)

def quick_sort(list):
    if len(list) < 2:
        return list

    piv = list[0]
    ltp = []
    gtp = []

    for i in list[1:]:
        if i <= piv:
            ltp.append(i)
        else:
            gtp.append(i)

    return quick_sort(ltp) + [piv] + quick_sort(gtp)

print("")
print("Quick Sort")
print(quick_sort(data))

def binary_search(list, target):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

print("")
print("Binary Search for index of 33")
print(binary_search(nlist, 33))

print("")
print("Merge sort, in place")
def inplace(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]


        inplace(left)
        inplace(right)

        i = 0 # LEft
        j = 0 # right
        k = 0 # Main list

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1


print("Orignal ->", data)
inplace(data)
print("Modified ->", data)