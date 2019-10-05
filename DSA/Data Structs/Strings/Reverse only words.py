def reverseOnlyLetters(S: str) -> str:
    def is_alpha(c):
        val = ord(c)
        return (val > 96 and val < 123) or (val > 64 and val < 91)
    ret = [''] * len(S)
    stack = []
    for i in range(len(S)):
        if not is_alpha(S[i]):
            ret[i] = S[i]
        else:
            stack.append(S[i])
    for i in range(len(ret)):
        if ret[i] == '':
            ret[i] = stack.pop(-1)
    return ''.join(ret)

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        i = 0
        j = len(S) - 1
        S_arr = list(S)
        while i < j:
            while i < j - 1 and not S[i].isalpha():
                i += 1
            while i < j - 1 and not S[j].isalpha():
                j -= 1
            if S[i].isalpha() and S[j].isalpha():
                S_arr[i], S_arr[j] = S_arr[j], S_arr[i]
            i += 1
            j -= 1
        return ''.join(S_arr)
