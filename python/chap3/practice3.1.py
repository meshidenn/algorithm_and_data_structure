
def main(N, v, a):
    found_id = -1
    for i, e in enumerate(a):
        if e == v:
            found_id = i
            break
    print(found_id)
    
N = 100
v = 20

a = list(range(N))

a[9] = v
a[72] = v
main(N, v, a)