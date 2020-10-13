def solver(a, b ,target):
    best_sum = float('-inf')
    best_pair = []
    a.sort(key = lambda x:x[1])
    b.sort(key = lambda x:x[1])
    i, j = 0, len(b) - 1
    while i < len(a) and j > -1:
        a_idx, a_num = a[i]
        b_idx, b_num = b[j]
        if a_num + b_num > target:
            j -= 1
        else:
            if best_sum == a_num + b_num:
                best_pair.append([a_idx, b_idx])
            else:
                best_pair = [[a_idx, b_idx]]
                best_sum = a_num + b_num
            i += 1
    return best_pair

a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7

a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10

a = [[1, 8], [2, 7], [3, 14]]
b = [[1, 5], [2, 10], [3, 14]]
target = 20

a = [[1, 8], [2, 15], [3, 9]]
b = [[1, 8], [2, 11], [3, 12]]
target = 20


print(solver(a, b, target))