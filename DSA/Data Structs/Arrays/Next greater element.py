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

def next_greater_element(arr):
    nge_stack = [0]
    nge = [-1]*len(arr)
    for i in range(1, len(arr)):
        next = arr[i]
        while nge_stack and next > arr[nge_stack[-1]]:
            nge[nge_stack[-1]] = next
            nge_stack.pop(-1)
        nge_stack.append(i)
    return nge