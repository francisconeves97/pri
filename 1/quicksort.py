def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def partition(array, low, high):
    pivot = array[low]
    leftwall = low

    for i in range(low + 1, high + 1):
        if array[i] < pivot:
            leftwall = leftwall + 1
            swap(array, i, leftwall)
    
    swap(array, low, leftwall)
    return leftwall

def quicksort(array, low, high):
    if low < high:
        pivot_location = partition(array, low, high)
        quicksort(array, low, pivot_location - 1)
        quicksort(array, pivot_location + 1, high)

array = [4,3,6,0]

quicksort(array, 0, 3)

print("array: " + str(array))

