def main(a, v):
    count = 0
    for i, e in enumerate(a):
        if e == v:
            count += 1
            
    print(count)
    
a = list(range(100))
v = 10

main(a, v)

a[20] = v
a[30] = v

main(a,v)
    