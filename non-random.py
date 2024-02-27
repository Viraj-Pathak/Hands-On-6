def partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as the pivot
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_nonrandom(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort_nonrandom(arr, low, pivot_index - 1)
        quicksort_nonrandom(arr, pivot_index + 1, high)

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
quicksort_nonrandom(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
