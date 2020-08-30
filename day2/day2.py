from inputs import opcodes


def sol(op):
    for i in range(0, len(op), 4):
        if op[i] == 1:
            op[op[i + 3]] = op[op[i + 1]] + op[op[i + 2]]
        elif op[i] == 2:
            op[op[i + 3]] = op[op[i + 1]] * op[op[i + 2]]
        elif op[i] == 99:
            break
        else:
            return [None]
    return op


assert sol([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
assert sol([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
assert sol([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
assert sol([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]

op1 = opcodes.copy()
for i in range(100):
    for j in range(100):
        op1[1] = i
        op1[2] = j
        s = sol(op1)
        if s[0] != 19690720:
            op1 = opcodes.copy()
        elif s[0] == 19690720:
            print(i, j)
            break
