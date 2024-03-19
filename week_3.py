def dot(v1, v2):

    if (len(v1) == 0 and len(v2) == 0):
        return 0

    result = 0
    longerVector = (len(v1) if len(v1) > len(v2) else len(v2))

    pv1 = []
    pv2 = []

    if (len(v1) != len(v2)):
        for i in range(longerVector):
            if (v1[i] == 0 or v2[i] == 0):
                pv1.append(0)
                pv2.append(0)

    for i in range(longerVector):
        result += v1[i] * v2[i]

    return result


print(dot([0, 2, 3], [4, 5, 6]))  # 32
print(dot([0, 2, 3], [-4, -5, -6]))  # -32
print(dot([-2, -2, -3], [-4, -5, -6]))  # 32
print(dot([-1, 0, 0], [1, 2, 3]))  # 0
print(dot([0, 2, 3], [4, 5]))  # 14
print(dot([], []))  # 0
