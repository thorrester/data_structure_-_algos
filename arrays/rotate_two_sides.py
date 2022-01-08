import time
# Problem Rotate an array of n elements to the right by k steps.
# Example [0,1,2,3,4,5] -> [3,4,5,0,1,2]


def rotate_array_v1(array, k):

    left_side = array[:k]
    right_side = array[k:]

    return [*right_side,*left_side]

def rotate_array_v2(array, k, n):

    array[:]= array[k:n] + array[0:k]

    return array

if __name__=="__main__":

    array = [0,1,2,3,4,5]
    print(array)
    k = 4

    result1 = rotate_array_v1(array, k)
    print(result1)

    array = [0,1,2,3,4,5]
    result2 = rotate_array_v2(array, k, len(array))
    print(result2)



