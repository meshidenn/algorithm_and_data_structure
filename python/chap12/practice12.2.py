from copy import deepcopy


def argQuick(vec, arg_v, left, right):

    if right - left <= 1:
        return

    i_pivot = int((left + right) / 2)
    pivot = vec[i_pivot]
    vec[right - 1], vec[i_pivot] = vec[i_pivot], vec[right - 1]
    arg_v[right - 1], arg_v[i_pivot] = arg_v[i_pivot], arg_v[right - 1]

    i = deepcopy(left)
    for j in range(left, right):
        if vec[j] < pivot:
            vec[j], vec[i] = vec[i], vec[j]
            arg_v[j], arg_v[i] = arg_v[i], arg_v[j]
            i += 1

    vec[right - 1], vec[i] = vec[i], vec[right - 1]
    arg_v[right - 1], arg_v[i] = arg_v[i], arg_v[right - 1]
    argQuick(vec, arg_v, left, i)
    argQuick(vec, arg_v, i + 1, right)


def main():
    A = [90, 30, 100, 20, 40, 70]
    B = [10, 4, 15, 2, 3, 7]

    arg_a = list(range(len(B)))

    argQuick(A, arg_a, 0, len(B))
    sB = [B[aa] for aa in arg_a]

    num = 0
    pay = 0
    N = 10
    print(sB)
    for b, a in zip(sB, A):
        t_num = num
        t_num += b
        if t_num < N:
            pay += b * a
        else:
            res = N - num
            pay += a * res
            break
        num = t_num

    print(pay)


if __name__ == "__main__":
    main()
