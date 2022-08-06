W = [2, 5, 4, 10, 2, 3, 6]
T = [3, 8, 13, 24, 26, 30, 36]

TF = [3, 8, 13, 24, 26, 30, 32]

sT = sorted(T)

task = 0
done = True
for w, t in zip(W, T):
    task += w

    if task > t:
        done = False

print(done)

done = True
for w, t in zip(W, TF):
    task += w

    if task > t:
        done = False

print(done)
