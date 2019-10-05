#with single pointer/ reverse string
def rem_nums_1(arr, val):
    next_val_ind = 0
    for i in range(len(arr)):
        if arr[i] ==  val:
            arr[i], arr[next_val_ind] = arr[next_val_ind], arr[i]
            next_val_ind += 1
    for i in range(len(arr) // 2):
        arr[i], arr[-i - 1] = arr[-i - 1], arr[i]
    return arr


#with two pointers
class Solution:
    def removeElement(self, arr, val):
        i = 0
        n = len(arr)
        while i < n:
            if arr[i] == val:
                arr[i] = arr[n - 1]
                n -= 1
            else:
                i += 1
        return n

