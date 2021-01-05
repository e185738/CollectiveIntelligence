import copy

q1=[1,1,1,1,0,0,0,1,1,0,0,1,1,1,1,1,0,0,1,1,0,1,0,1]
A = [0]*len(q1)
q2=[0,1,1,1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0]
a2 = ""

print(q1)
for _ in range(100):
    N = 0
    A = copy.copy(q1)

    for i in q1:
        if i == 1 and N != len(q1)-1 and q1[N + 1]==0:
            A[N+1] = 1
            A[N] = 0
            N += 1

        elif N == len(q1)-1 and i == 1 and q1[0] == 0:
            A[len(q1)-1] = 0
            A[0] = 1
            N += 1
        else:
            N += 1
            pass
    
    q1 = copy.copy(A)

for j in range(24):
    a2 += str(q1[j])

print(int(a2, 2))

