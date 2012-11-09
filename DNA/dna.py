s = raw_input()

A = 0
C = 1
G = 2
T = 3

out = [0, 0, 0, 0]

for a in s:
    if a=='A':
        out[A] += 1
    elif a=='C':
        out[C] += 1
    elif a=='G':
        out[G] += 1
    elif a=='T':
        out[T] += 1

print out[A], out[C], out[G], out[T]
