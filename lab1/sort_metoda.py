def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        index_of_min = i
        for j in range(i + 1, n):
            if arr[j] < arr[index_of_min]:
                index_of_min = j
        
        arr[i], arr[index_of_min] = arr[index_of_min], arr[i]

    return arr



def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]  
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j] 
            j -= 1
        
        arr[j + 1] = key
        
    return arr



numbers = [19, 2, 31, 45, 6, 11, 121, 27]

list_for_selection = numbers.copy()
list_for_insertion = numbers.copy()

print("Selection:", selection_sort(list_for_selection))
print("Insertion:", insertion_sort(list_for_insertion))
