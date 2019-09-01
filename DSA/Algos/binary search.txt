def binary_search(input_array, value):
    min_index = 0
    max_index = len(input_array)-1
    while(max_index-min_index>=0):
        mid_index = (min_index+max_index)/2
        mid_val = input_array[mid_index]
        if(mid_val==value):
            return mid_index
        elif(mid_val>value):
            max_index = mid_index -1
        elif(mid_val<value):
            min_index = mid_index+1
    return -1