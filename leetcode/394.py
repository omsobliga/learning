def f(s):
    l = []
    n = 0
    ss = ""
    for k in s:
        if n > 0 and not (k >= "0" and k <= "9"):
            l.append(n)
            n = 0

        if ss != "" and ((k >= "0" and k <= "9") or k in ["[", "]"]):
            l.append(ss)
            ss = ""

        if k >= "0" and k <= "9":
            n = n * 10 + int(k)
        elif k in ["[", "]"]:
            l.append(k)
        else:
            ss += k

    if ss:
        l.append(ss)

    # print(l)

    result = ""
    stack = []
    for i in l:
        if i != "]":
            stack.append(i)
            # print(i, stack)
        else:
            ss = ""
            flag = False
            while stack:
                # print(stack, ss)
                k = stack[-1]
                if k == "[":
                    if flag:
                        break
                    else:
                        flag = True
                        stack.pop()
                        continue
                elif isinstance(k, int):
                    ss = ss * k
                else:
                    ss = k + ss
                stack.pop()
            stack.append(ss)
            # print(stack)
    return "".join(stack)


print(f("3[a]2[bc]"))
print(f("3[a2[c]]"))
print(f("2[abc]3[cd]ef"))
print(f("abc3[cd]xyz"))
print(f("2[2[y]pq4[2[jk]]e]"))
