def main(a):
    min_v = 10000000
    max_v = -10000000
    for e in a:
        if e < min_v:
            min_v = e
        if e > max_v:
            max_v = e

    print(max_v - min_v)

a = list(range(100))
a[0] = -1
a[-1] = 1000
main(a)