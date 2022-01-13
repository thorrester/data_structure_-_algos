#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

def two_sum(array, target):

    # We will use a dictionary
    res_dict={}

    for i, a in enumerate(array):
        diff = target - a
        if diff in res_dict:
            return [res_dict[diff], i]
        res_dict[a] = i




if __name__=="__main__":

    array = [3,2,4]
    target = 6
    result = two_sum(array, target) 
    print(result)