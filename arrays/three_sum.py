# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets

def three_sum(array):
    # Take advantage of sorting the array
    array.sort() # O(n log n)
    res = []

    # set the 1st value 
    for idx, val in enumerate(array):
        if idx > 0 and val == array[idx-1]:
            continue

        # Set the pointers for the 2 other elements
        l, r = idx + 1, len(array) - 1
        while l<r:
            sum_ = array[idx] + array[l] + array[r]

            # If sum < 0 decrementing the right (largest) value, will only make sum smaller
            if sum_ < 0:
                l += 1

            # If sum > 0 adding to left pointer will only make sum bigger
            elif sum_>0:
                r -= 1
            else:
                # If threesum = 0 then append triplet to list
                res.append([array[idx], array[l], array[r]])

                # Increment the left pointer
                l +=1

                #Evaluate if left point value will result in same value as previous left, if so, keep incrementing up
                while array[l] == array[l-1] and l<r:
                    l+=1

                # Theres no need to adjust the right pointer because incrementing left will change the three sum. 
                # If three sum is then too big, the right pointer will be decremented any way
    return res


if __name__=="__main__":

    array = [-1, 0, 1, 2, -1, -4]
    result = three_sum(array)
    print(result)