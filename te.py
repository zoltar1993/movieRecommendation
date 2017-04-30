import math

dic={}
dic.setdefault('1',{})
print(dic)
dic['1']['1']=5
print(dic)

dic.setdefault('1',{})
print(dic)
dic['1']['2']=3
print(dic)


dic.setdefault('2',{})
print(dic)
dic['2']['1']=4
print(dic)

print(dic.items())


C = dict()  # 物品-物品的共现矩阵
N = dict()  # 物品被多少个不同用户购买

for user, items in dic.items():
    for i in items.keys():
        N.setdefault(i, 0)
        N[i] += 1
        C.setdefault(i, {})
        for j in items.keys():
            if i == j: continue
            C[i].setdefault(j, 0)
            C[i][j] += 1


print(C)

W = dict()
for i, related_items in C.items():
    W.setdefault(i, {})
    for j, cij in related_items.items():
        W[i][j] = cij / (math.sqrt(N[i] * N[j]))
print(W)
print(W['2']['1'])