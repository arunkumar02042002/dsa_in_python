# Defining the linear search algorithm
def linearSearch(arr, k):

    # Iterate through the elements of the array along with their indices
    for i, value in enumerate(arr):

        # Check if the current element is equal to the search key (k)
        if value == k:
            # If found, return the index of the element
            return i

    # If the search key is not found in the array, return -1
    return -1

myList = list(range(15))
print(linearSearch(myList, 8))
print(linearSearch(myList, 15))