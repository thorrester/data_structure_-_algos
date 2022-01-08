# in this scenario you are given an array of 4 numbers [1,2,3,4]. You must create a new array where each index from the original list is 
# replaced with the product of all number excluding the current index number
# Example: Input: [1,2,3,4], Output: [24, 12, 8, 6]

def prod_excep_self_v1(array):

    result = []
    curr_idx = 0

    for i in range(len(array)):
        result.append(1)
        for j in range(len(array)):
            if j == curr_idx:
                pass
            else:
                result[curr_idx] *= array[j]
        curr_idx +=1

    return result

def prod_excep_self_v2(array):
    n  = len(array)

    if n == 0:
        return
    
    left_array = [1 for i in range(n)]
    right_array = [1 for i in range(n)]

    for i in range(1,n):
        left_array[i] = left_array[i-1]*array[i-1]

    for i in reversed(range(n-1)):
        right_array[i] = right_array[i+1]*array[i+1]

    for i in range(n):
        right_array[i] *= left_array[i]

    return right_array

if __name__=="__main__":

    array = [1,2,3,4]
    result = prod_excep_self_v1(array)
    print(result)

    result = prod_excep_self_v2(array)
    print(result)

    # V1 is O(n^2) due to a nested for loop
    # Try breaking the loop
    # V2 is O(n) since it only consists of for loops
