# Program to implement heap sort
# Remember
# Left child of a max heap = 2i + 1 where i is the parent
# Right child of a max heap = 2I + 2 where i is the parent
# You can find the parent index of any node by using i-1/2 

def heapify(array, n, i):
    """
    n = length or array
    i = index
    """

    # Find largest root among children
    largest = i

    # Find left child of i
    left = 2 * i + 1

    # Find right child of i
    right = 2 * i + 2

    # If left index is less than array length and value at index is less than value at left
    # Largest value is at the left index
    if left < n and array[i] < array[left]:
        # This means the left child is larger than the parent which should not happen in a max heap
        largest = left

    # If right index is less than array length
    # and value at largest index is less than value at right index
    # largest index is rght index
    if right < n and array[largest] < array[right]:
        # This means the parent is less than the right child which should not happen in a max heap
        largest = right

    # If root is not largest, swap with largest and continue
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)

def heapsort(array):
    n = len(array)

    #Build max-heap
    for i in range(n//2, -1, -1):
        heapify(array, n, i)

    for i in range(n-1, 0, -1):
        # Swap
        array[i], array[0] = array[0], array[i]

        # Heapify root element
        heapify(array, i, 0)



if __name__=="__main__":

    array = [3,0,4,6,2,5,1]
    heapsort(array)
    print(array)
