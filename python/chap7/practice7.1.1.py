A = [2, 4, 9, 15, 22, 26, 29, 33]
B = [3, 7, 11, 14, 19, 23, 32, 35]

i = 0
I = 0
for b in B:
    while A[i] < b and i < len(A) - 1:
        i += 1
    I += i

print(I)
