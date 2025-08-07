class Solution(object):
    def isValid(self, s):
        stack = []
        opening = "([{"
        closing = ")]}"
        i = 0
        while True:
            c = s[i]
            if c in opening:
                stack.insert(0, c)
            elif c in closing:
                if stack:
                    top = stack[0]
                else:
                    return False
                if (c == ")" and top == "(") or (c == "]" and top == "[") or (c == "}" and top == "{"):
                    stack.pop(0)
                else:
                    return False
            i += 1
            if i >= len(s):
                break
        if not stack:
            return True
        else:
            return False


print(Solution().isValid("(])"))