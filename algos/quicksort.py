# This py script implements the quiksort algorithm


# Features of quicksort
# 1. divide and coonquer
# 2. In place
# 3. Unstable

# Quicksort divides and sorts an array by taknig a psuedo-pivot and places elements smaller than the pivot to the left and large than pivot to the right
# The sortng process is repeated for both split arrays until a full sorted array is reached

def partition(array, start, end):
    pivot = array[start]
    low = start+1
    high = end

    while True:

        # if low is less than high and array high value is higher than pivot then move the high index to the left one
        while low <= high and array[high] >= pivot:
            high = high - 1
            # This will run until we reach a high value thats lower than pivot
            # or high is lower than low

        # if low is less than high and the low value is less than pivot then move the low index to the right one
        while low <= high and array[low] <= pivot:
            low = low + 1
            # This will run until we reach a value lower than pivot
            # or high is now lower than low

        # We have found a high value that is less than pivot
        # Have found a low value that is higher than pivot
        # We now need to swap the values
        # Or break and exiit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]

        else:
            break

    # First index is now the point lower than pivot
    # Idx where high was less than pivot is now the pivot value
    array[start], array[high] = array[high], array[start]

    return high



def quick_sort(array, start, end):
    """
    Args
        array: array of  integers to be sorted
        low: low index position. Typically 0
        high: high index position
    """

    if start >= end:
        return

    # Run initial partition and return new hgh value which should be idx where value was less than pivot from right
    high = partition(array, start, end)

    # Run quick sort with a start at 0 and end at where the partiton high was
    quick_sort(array, start, high-1)

    # Run quicksort where start is atthe idx of partition high + 1 and end idx
    quick_sort(array, high+1, end)

if __name__=="__main__":

    arr = [99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
    quick_sort(arr, 0, len(arr)-1)
    print(arr)

    # Average complexity will be O(n log n)
    # Worst case would be O(n^2) which can occur if each partition happens on the edge. Each resulting partitioned array will be n-1 and not halved.
    # Space complexity is O(n) since it is an in-place algo