import copy

q1=[1,1,1,1,0,0,0,1,1,0,0,1,1,1,1,1,0,0,1,1,0,1,0,1]
A = [0]*len(q1)
q2=[0,1,1,1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0]
f = 0
a2 = ""

print(q2)
for _ in range(100):
    N = 0
    A = copy.copy(q2)

    for i in q2:
        if i == 1 and N != len(q2)-1 and q2[N + 1]==0:
            A[N+1] = 1
            A[N] = 0
            N += 1

        elif N == len(q2)-1 and i == 1 and q2[0] == 0:
            A[len(q2)-1] = 0
            A[0] = 1
            N += 1
        # elif N == len(q1)-1 and A[len(q1)-1] == 1 and A[0] == 0:
        #     A[0] =  1
        else:
            N += 1
            pass
    
    print(A)
    q2 = copy.copy(A)
    f+=1
    print(f)

for j in range(24):
    a2 += str(q2[j])

print(int(a2, 2))

