import numpy as np

A = 20
B = 30
C = 40

left = 0
right = 100 + B

target = 100


def func(t):
    return A * t + B * np.sin(C * t * np.pi)


t = (right + left) / 2

while abs(target - func(t)) > 1e-6:
    t = (right + left) / 2
    val = func(t)
    if val < target:
        left = t
    else:
        right = t
    print(t, val, left, right, abs(target - func(t)))

print(left, func(t))
