# insertion algo
def insertion_sort(array):

    # Compare preceding value to current value
    # If preceding value is greater than current, move previous value to the right
    # Start at 1st position in order to use 0th position for previous comparison
    for idx in range(1,len(array)):
        curr_val = array[idx] 
        prev_idx = idx - 1  

        # while previous idx >= 0 and current value < previous value then make 
        while (prev_idx >= 0 and curr_val <= array[prev_idx]): 

            # Move previous value up one
            array[prev_idx+1] = array[prev_idx]

            # move down the list
            prev_idx -= 1 
        
        # Eventualy curr val will not be less than previous or prev index will be greater than 0
        array[prev_idx + 1] = curr_val

if __name__=="__main__":

    array = [3,0,4,6,2,5,1]
    print(array)
    insertion_sort(array)
    print(array)

