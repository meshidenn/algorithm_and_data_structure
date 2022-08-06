from copy import deepcopy


def argQuick(vec, arg_v, left, right):
    print(left, right)
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
            print(i, j, vec[j], pivot, i_pivot)
            print(vec)

    vec[right - 1], vec[i] = vec[i], vec[right - 1]
    arg_v[right - 1], arg_v[i] = arg_v[i], arg_v[right - 1]
    print(vec, arg_v)
    argQuick(vec, arg_v, left, i)
    argQuick(vec, arg_v, i + 1, right)


def main():
    vec = [9, 3, 10, 2, 4, 7]
    org_vec = deepcopy(vec)
    arg_v = list(range(len(vec)))
    result = list(range(len(vec)))

    argQuick(vec, arg_v, 0, len(vec))

    for i, ai in enumerate(arg_v):
        result[ai] = i

    print(vec)
    print(result)
    print([org_vec[i] for i in result])


if __name__ == "__main__":
    main()
