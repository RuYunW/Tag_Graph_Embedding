'''
Tag-graph embedding generation algorithm
'''

from utils import load_data,LSTM

# Initialize
x = load_data()
order = []  # 创建一个空集合
K = 5
h = []

h[:][0] = x[:]
for k in range(K):  # hop数  K
    for m in range(len(x)):  # 节点个数  M
        h[][k] = Virtualized()
        h[][k] = Virtualized()
        order = h[][k] + h[][k]
        for u in order:
             h[][] = LSTM(h[][])
        h[][] = Sigma()
z[] = h[][]