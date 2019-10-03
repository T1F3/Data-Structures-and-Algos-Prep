    def reverseOnlyLetters(self, S: str) -> str:
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

    