target = [4, 12, 8]

counter = 0
checker = True
while checker:
    new_target = []
    for t in target:
        if t % 2 == 1:
            checker = False
        new_target.append(int(t / 2))
    if checker:
        counter += 1
        target = new_target

print(counter)
