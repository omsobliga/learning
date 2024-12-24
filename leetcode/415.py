def f(num1, num2):
    num1 = num1[::-1]
    num2 = num2[::-1]
    len1 = len(num1)
    len2 = len(num2)
    i = 0

    result = []
    flag = 0
    multiply = 1

    while i < len1 or i < len2:
        n1, n2 = 0, 0
        if i < len1:
            n1 = int(num1[i])
        if i < len2:
            n2 = int(num2[i])
        flag += n1 + n2

        if flag > 9:
            result.append(flag % 10)
            flag = 1
        else:
            result.append(flag)
            flag = 0

        i += 1
        multiply *= 10

    if flag:
        result.append(flag)

    s = ""
    for r in result:
        s += str(r)

    return s[::-1]


print(f("11", "123"))
print(f("456", "77"))
print(f("0", "0"))
