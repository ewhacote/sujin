def isFair(s):
    if len(s) % 2 != 0 :
        return False
    stack = []
    for ch in s:
        if ch == "(" or ch == "[" or ch == "{":
            stack.append(ch)
        else:
            if len(stack) == 0:
                return False
            else :
                a = stack.pop()
                mini = a+ch
                if mini != "[]" and mini != "()" and mini != "{}":
                    return False
    return True