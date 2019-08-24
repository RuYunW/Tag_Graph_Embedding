'''
Tag-graph embedding generation algorithm
'''

from utils import load_data

# Initialize
x = load_data()
order = []  # 创建一个空集合
K = 5
h = [[] for i in range(K+1)]
# print(h)
# print(x[0][0])  # [[0,...,0],[...],...,[...]]
for i in x:
    h[0].append(i)
# print(h[0])

print(len(h[0]))  # len(h[0]=2708)

# for k in range(K):  # hop数  K
#     for m in range(len(x)):  # 节点个数  M
#         h[][k] = Virtualized()
#         h[][k] = Virtualized()
#         order = h[][k] + h[][k]
#         for u in order:
#              h[][] = LSTM(h[][])
#         h[][] = Sigma()
# z[] = h[][]