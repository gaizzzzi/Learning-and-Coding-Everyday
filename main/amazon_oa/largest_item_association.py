class unionfind:
    def __init__(self):
        self.prt = {}
        self.size = {}

    def add(self, x):
        if x in self.prt:
            return
        self.prt[x] = x
        self.size[x] = {x}

    def find(self, x):
        while self.prt[x] != x:
            self.prt[self.prt[x]] = self.prt[x]
            x = self.prt[x]
        return x

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if len(self.size[y]) > len(self.size[x]):
            x, y = y, x
        self.prt[y] = x
        self.size[x].update(self.size[y])
        self.size.pop(y)


def largestItemAssociation(itemAssociation):
    uf = unionfind()
    for item1, item2 in itemAssociation:
        uf.add(item1)
        uf.add(item2)
        uf.union(item1, item2)

    print(uf.prt, uf.size)
    largest_count = 0
    largest_group = None
    largest_group_set = set()
    for item in uf.prt:
        prt = uf.find(item)
        if prt != largest_group and len(uf.size[prt]) >= largest_count:
            if len(uf.size[prt]) > largest_count or not largest_group_set or min(largest_group_set) > min(uf.size[prt]):
                largest_count = len(uf.size[prt])
                largest_group = prt
                largest_group_set = uf.size[prt]
    return sorted(largest_group_set)

itemAssociation = [[1, 2],[3,4],[4,5],[2,6]]
print(largestItemAssociation(itemAssociation))