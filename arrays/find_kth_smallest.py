# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.
# 
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
# 
# You must find a solution with a memory complexity better than O(n2)

def partition(array, start, end):

def quicksort():




def kth_sorted(matrix, k):

    array = []

    # O(n) complexity
    for i in matrix:    
        array = [*array,*i]

    insertion_sort(array)

    return array[k-1]

if __name__=="__main__":
    matrix = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8
    result = kth_sorted(matrix, k)
    print(result)


