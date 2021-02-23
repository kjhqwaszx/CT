## 2798
def blackJack():
    n, m = list(map(int, input().split(' ')))
    cards = list(map(int, input().split(' ')))
    results = 0

    for i in range(0,n):
        for j in range(i+1, n):
            for k in range (j+1, n):
                result = cards[i] + cards[j] + cards[k]
                if result <= m :
                    results = max(result,results)
    print(results)

blackJack()
