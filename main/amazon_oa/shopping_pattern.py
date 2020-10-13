from collections import defaultdict
def shopping_pattern(n, m, p_from, p_to):
    node_map = defaultdict(set)
    for i in range(len(p_from)):
        node_map[p_from[i]].add(p_to[i])
        node_map[p_to[i]].add(p_from[i])

    def find(x):
        while x != prt[x]:
            prt[x] = prt[prt[x]]
            x = prt[x]
        return x

    res = float('inf')
    prt = [i for i in range(n + 1)]
    size = [{i} for i in range(n + 1)]
    has_trio = False
    for i in range(len(p_from)):
        x, y = find(p_from[i]), find(p_to[i])
        if x == y:
            # circle found, check if trio exists
            intersect = node_map[p_from[i]].intersection(node_map[p_to[i]])
            #print(intersect, prt, x)
            for node in intersect:
                if find(node) == x:

                    res = min(res, len(node_map[p_from[i]]) + len(node_map[p_to[i]]) + len(node_map[node]) - 6)
                    has_trio = True
                    print(p_from[i], p_to[i], node, res)
        else:
            # union
            if len(size[x]) > len(size[y]):
                x, y = y, x
            prt[y] = x
            size[x].update(size[y])
            size[y] = set()

    return res if has_trio else -1
n = 6
m = 6
l1 = [1,2,2,3,4,5,2,3]
l2 = [2,4,5,5,5,6,3,4]
print(shopping_pattern(n,m,l1,l2))