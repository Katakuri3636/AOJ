def BubbleSort(C, n):
    for i in range(n):
        for j in range(n-1, i, -1):
            if int(C[j][1]) < int(C[j-1][1]):
                C[j],C[j-1] = C[j-1],C[j]

    return C

def SelectionSort(C, n):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if int(C[minj][1]) > int(C[j][1]):
                minj = j
        C[minj], C[i] = C[i], C[minj]

    return C


n = int(input())

cards = input().split()

CB = BubbleSort(cards[:], n)
print(*CB)
print('Stable')

CS = SelectionSort(cards[:], n)
print(*CS)
if CB == CS:
    print('Stable')
else:
    print('Not stable')
