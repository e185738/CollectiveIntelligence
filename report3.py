import copy
import random

q1=[1,1,1,1,0,0,0,1,1,0,0,1,1,1,1,1,0,0,1,1,0,1,0,1]
q2=[0,1,1,1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0]
F = [1,1,1,1,0,0,0,1,1,0,0,1,1,1,1,1,0,0,1,1,0,1,0,1]
A = [0]*24
Q = 0.75
q = 0.25
f = 0.50
a = ""

print(q1)

for _ in range(100):
    A = copy.copy(q1)

    for i in range(24):
        if i != 23 and q1[i] == 1 and q1[i + 1] == 0: #粒子ありで、隣が空いている場合
            if F[i+1] == 1 and random.random() <= Q: #隣にフェロモンがある時、確率Qで移動
                A[i] = 0
                A[i+1] = 1
            if F[i+1] == 0 and random.random() <= q: #隣にフェロモンがない時、確率qで移動
                A[i] = 0
                A[i+1] = 1
        if i == 23 and q1[i] == 1 and q1[0] == 0: #配列の最後の時
            if F[0] == 1 and random.random() <= Q:
                A[i] = 0
                A[0] = 1
            if F[0] == 0 and random.random() <= q:
                A[i] = 0
                A[0] = 1

    q1 = copy.copy(A)
    
    for j in range(24): #フェロモン情報の更新
        if q1[j] == 0: #粒子がないマス
            if F[j] == 1 and random.random() <= f: #フェロモンがある時、確率fで蒸発
                F[j] = 0        
        else: #粒子があるマス
            F[j] = 1

    print(q1)


