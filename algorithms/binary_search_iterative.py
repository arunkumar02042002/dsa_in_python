# Defining the Binary Search Algorithm - Iterative Method 
def binarySearch(arr, k):

    # Get the length of the array
    n = len(arr)

    # Calculate the initial middle index
    mid = n // 2

    # Set the initial left and right boundaries
    left = 0
    right = n - 1

    # Perform binary search until the left and right boundaries meet
    while left <= right:

        # Calculate the new middle index
        mid = (right - left) // 2 + left

        # Check if the middle element is equal to the search key (k)
        if arr[mid] == k:
            # If found, return the index of the middle element
            return mid
        
        # If the middle element is greater than the search key,
        # narrow the search range to the left half of the array
        elif arr[mid] > k:
            right = mid - 1

        # If the middle element is smaller than the search key,
        # narrow the search range to the right half of the array
        else:
            left = mid + 1
            
    # If the search key is not found in the array, return -1
    return -1

"""Testing Iterative Binary Search ALgorithm"""
arr = list(range(15))
print(binarySearch(arr, 5))
print(binarySearch(arr, 0))
print(binarySearch(arr, 14))
print(binarySearch(arr, 15))