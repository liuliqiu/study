class Node:
    def __init__(self, parent, value):
        self.parent = parent
        self.value = value
        self.childs = []

    def get_childs(self, k):
        n = self
        while n:
            v = n.value + self.value
            if v <= k:
                newNode = Node(self, v)
                self.childs.append(newNode)
            n = n.parent


def f(k):
    v = [Node(None, 1)]
    i = 1
    depths = {1: 0}
    while len(depths) < k:
        print(i, len(v), len(depths), sum(depths[i] for i in depths))
        newV = []
        for n in v:
            n.get_childs(k)
            for nn in n.childs:
                if nn.value not in depths:
                    depths[nn.value] = i
            newV += n.childs
        v = newV
        i = i + 1
        if len(depths) == k - 1:
            for i in range(1, k + 1):
                if i not in depths:
                    print(i)
            return sum(depths[i] for i in depths)
    print(depths)
    return sum(depths[i] for i in depths)


print(f(200))
##from Crazy import isprime
##
##Cached={}
##def g(k):
##    if k<=3:
##        return k-1
##    if isprime(k):
##        return min(g(k-1)+1,g(k-2)+1)
##    if k not in Cached:
##        S=min(g(k//i)+g(i) for i in range(2,int(k**0.5)+1) if k%i==0)
##        Cached[k]=min((S,g(k-1)+1,g(k-2)+1))
##    return Cached[k]
##
##def f(k):
##    return sum(g(i) for i in range(1,k+1))
##print(f(20))
