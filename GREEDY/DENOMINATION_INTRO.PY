def change(coins,amount):

    coins.sort(reverse= True)

    i=n=count=0

    while amount>0:

        if amount < coins[len(coins)-1]: return -1

        n = amount//coins[i]
        amount -=(n*coins[i])
        count+=n
        i+=1
    

    return count

denominations = list(map(int,input().split()))
cost = int(input())
print(change(denominations,cost))