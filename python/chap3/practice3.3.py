def main(a):
    min_v = 10000000
    for i, e in enumerate(a):
        if e < min_v:
            min_v = e
    
    second_min = 100000
    for i, e in enumerate(a) :
        if min_v < e and e < second_min:
            second_min = e
            
    print(second_min)
    
a = list(range(100))

main(a)