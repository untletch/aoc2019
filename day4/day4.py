def comp(n):
    s = str(n)
    for i in range(len(s) - 1):
        if int(s[i]) > int(s[i + 1]):
            return False
    return True


def rep(n):
    s = str(n)
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False


def num_rep(n):
    count = 1
    s = str(n)
    ans = {}
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
            ans[s[i]] = count
        else:
            count = 1
    for i in ans.values():
        if i == 2:
            return True
    return False


print(num_rep(111122))


def sol():
    count = 0
    for i in range(152085, 670283):
        if len(set(str(i))) == len(str(i)):
            continue
        if comp(i) and num_rep(i):
            count += 1
    return count


print(sol())
