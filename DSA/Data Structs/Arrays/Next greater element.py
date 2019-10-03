def next_greater_element(arr):
    nge = []
    for i in range(len(arr)):
        nge_i = -1
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[i]:
                nge_i = arr[j]
                break
        nge.append(nge_i)
    return nge

