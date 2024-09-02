def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no swapping occurred, array is already sorted
        if not swapped:
            break
    
    return arr

# Test the optimized bubble sort algorithm
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
sorted_arr = optimized_bubble_sort(arr.copy())
print("Sorted array:", sorted_arr)

# Test with an already sorted array to demonstrate early termination
sorted_arr = [1, 2, 3, 4, 5, 6, 7]
print("\nAlready sorted array:", sorted_arr)
result = optimized_bubble_sort(sorted_arr.copy())
print("Result after optimized bubble sort:", result)