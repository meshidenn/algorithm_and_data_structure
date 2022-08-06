N = 125
S = str(N)
l = len(S)

insert_cands = []


def make_cand(cand, depth):
    if depth == 0:
        return cand
    cand1 = cand + [0]
    cand2 = cand + [1]
    get_cand = make_cand(cand1, depth - 1)
    if get_cand is not None:
        insert_cands.append(get_cand)

    get_cand = make_cand(cand2, depth - 1)
    if get_cand is not None:
        insert_cands.append(get_cand)


make_cand(insert_cands, l - 1)

equations = []
for cand in insert_cands:
    equation = []
    for s, c in zip(S, cand):
        equation.append(s)
        if c == 1:
            equation.append("+")
    equation.append(S[-1])
    equation = "".join(equation)
    equations.append(eval(equation))

print(sum(equations))
