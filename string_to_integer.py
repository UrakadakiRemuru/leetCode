class Solution:
    def myAtoi(self, s: str) -> int:
        total = ''
        numstr = '1234567890'
        flag = True
        if s == '':
            return 0
        for i, val in enumerate(s):
            if val == ' ':
                if i == len(s) - 1:
                    return 0
                else:
                    pass
            elif val == '-':
                if i != len(s) - 1:
                    if s[i + 1] in numstr:
                        flag = False
                    else:
                        return 0
                elif i == len(s) - 1:
                    return 0
            elif val == '+':
                if i != len(s) - 1:
                    if s[i + 1] in numstr:
                        flag = True
                    else:
                        return 0
                elif i == len(s) - 1:
                    return 0
            elif val in numstr:
                total += val
                if i != len(s) - 1:
                    if s[i + 1] not in numstr:
                        break
            elif val not in numstr or val == '':
                return 0
        if flag == True:
            if not (int(total) < 2 ** 31):
                return 2 ** 31 - 1
            else:
                return int(total)
        else:
            if not -2 ** 31 < int(total) * (-1):
                return -2 ** 31
            else:
                return int(total) * (-1)
