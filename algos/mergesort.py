# This py file implements the mergesort algo

# It is considered a divide and conquer algo

# An initial array is divided into two equal parts 
# Each subarray is then divided over and over againi until you are left with arrays with one element
# Then you combine the one element arrays into pairs, sorting them in the process

def merge(array, left_index, right_index, middle):

    # Create copies of each subarray
    left_copy = array[left_index:middle+1]
    right_copy = array[middle+1:right_index+1]

    # Set the pointer defaullt for each copy
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    # Go through each copy until we run out of  elements in one of them
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        # if left value is less than right value, add value to original array at inedex and increment left copy index
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index += 1

        # Else right value is greater than left. Add right value to array at sorted index and increment right copy index
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index += 1

        # Once the sorted value is added to the array, increment the sorted index
        sorted_index +=1

    # In the case we run out of elements in one of the subarrays the while loop will break
    # We need to dd the remaining values of the nonzero length subarray to the original array
    while left_copy_index<len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index += 1
        sorted_index += 1
    
    while right_copy_index<len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index += 1
        sorted_index += 1
    
def merge_sort(array, left_index, right_index):

    # Exit out of merge sort when you have a 1 element array
    if left_index >= right_index:
        return

    # Determnine middle index of array
    middle = (left_index + right_index)//2

    # Perform merge_sort on left side array
    merge_sort(array, left_index, middle)

    # Perform merge_sort on right side of array
    merge_sort(array, middle+1, right_index)

    # Perform merge after merge_sort exits
    merge(array, left_index, right_index, middle)

if __name__=="__main__":

    array = [33, 42, 9, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]
    merge_sort(array, 0, len(array) -1)
    print(array)

    # Solution takes O(n log n) complexity due to splitting an n-sized array through recursion
    # Space complexity is O(n) since the merge function creates an auxilary array
