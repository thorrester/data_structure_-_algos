# Sorting algorithm that sorts items into buckets or bins
# Conents are then sorted with another agorithm
# Considered scatter-order-gather algo
# [1.2, 0.22, 0.43, 0.36, 0.39, 0.27]

def bucket_sort(array):
    high = max(array)
    size = high/len(array)

    buckets_list = []
    for i in range(len(array)):
        buckets_list.append([])

    for i in range(len(array)):
        buckets_list_idx = int(array[i]/size)
        if buckets_list_idx != len(array):
            buckets_list[buckets_list_idx].append(array[i])
        else:
            buckets_list[buckets_list_idx - 1].append(array[i])

    for bucket in buckets_list:
        # Insertion sort
        # [0.22, 0.36, 0.39, 0.27]
        for i in range(1, len(bucket)):
            var = bucket[i] 
            print(var)
            j = i - 1
            while (j >= 0 and var < bucket[j]): 
                bucket[j+1] = bucket[j]
                j = j - 1
            bucket[j + 1] = var
    
    final_output = []
    for i in range(len(array)):
        final_output = final_output + buckets_list[i]

    return final_output


if __name__=="__main__":

    array = [1.2, 0.22, 0.43, 0.36, 0.39, 0.27]
    result = bucket_sort(array)

    print(result)
