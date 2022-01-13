#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

def two_sum_pointers(array, target):
    res = []

    # We will use a dictionary
    n = len(array)

    # make copy of orig for idx
    lookup_dict = {}
    for idx, val in enumerate(array):
        lookup_dict[val] = idx

    # For the pointer method, the array must be sorted
    array.sort()

    #  Create the left pointer
    l = 0

    # Create the right pointer on largest value
    r = n-1

    while (l<r):

        twosum = array[l] + array[r] 
        if twosum < target:
            l += 1
        
        elif twosum > target:
            r -= 1

        else:
            res.append([lookup_dict[array[l]], lookup_dict[array[r]]])
            l += 1
    return res

if __name__=="__main__":

    array = [3,2,4]
    target = 6
    result = two_sum_pointers(array, target) 
    print(result)

    # O(n) complexity -> only 2 for loops
    # O()