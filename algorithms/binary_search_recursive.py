# Defining the Binary Search Algorithm - Recursive Method 
def binarySearch(arr, left, right, k):

    if left<=right:
        
        # Calculate the middle index
        mid = (right - left) // 2 + left

        # Check if the middle element is equal to the search key (k)
        if arr[mid] == k:
            # If found, return the index of the middle element
            return mid

        # If the middle element is greater than the search key,
        # recursively search in the left half of the array
        if arr[mid] > k:
            return binarySearch(arr, left, mid - 1, k)

        # If the middle element is smaller than the search key,
        # recursively search in the right half of the array
        else:
            return binarySearch(arr, mid + 1, right, k)
        
    # The search key is not found in the array  
    return -1

myList = list(range(15))
print(binarySearch(myList, 0, 14, 5))
print(binarySearch(myList, 0, 14, 0))
print(binarySearch(myList,  0, 14, 14))
print(binarySearch(myList,  0, 14, 15))