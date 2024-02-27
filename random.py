import random

def partition(arr, low, high):
    pivot_index = random.randint(low, high)  # Randomly choose pivot index
    pivot = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Move pivot to the end
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_random(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort_random(arr, low, pivot_index - 1)
        quicksort_random(arr, pivot_index + 1, high)

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
quicksort_random(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
