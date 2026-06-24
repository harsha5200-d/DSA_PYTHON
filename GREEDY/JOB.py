class job:

    profit = None
    deadline = None

    def __init__(self,p,d):

        self.profit = p
        self.deadline = d

n = int(input())
l = [None]*n
mx = 0

for i in range(n):
    p,d = map(int,input().split())
    l[i] = job(p,d)

    if max < d:
        mx = d

l.sort(key= lambda j : j.profit ,reverse=True)

res = [-1]*mx
i=0

while i != n :

    if res[(l[i].deadline)-1]==-1