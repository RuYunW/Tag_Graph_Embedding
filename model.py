'''
Tag-graph embedding generation algorithm
'''

from utils import load_data
import numpy as np

# Initialize
x,cites,content,class_set = load_data()
order = []  # Create an empty list
K = 5  # hops
h = [[] for i in range(K+1)]  # temp matrices
# print(x[0][0])  # [[0,...,0],[...],...,[...]]

h[0]+=x[:]

# print(np.array(x)[:,0])
# print(h[0][0][0])
temp_frontnode = []
temp_frontcode = []
front_node = []
front_code = []

for node_id in np.array(x)[:,0]:
    for line in cites:
        if line[1] == node_id:
            temp_frontnode.append(line[0])
            # print(666)
    for line in content:
        if line[0] in temp_frontnode:
            temp_frontcode.append(line[:])
            # print(777)
    front_node.append(temp_frontnode)
    front_code.append(temp_frontcode)
    temp_frontnode = []
    temp_frontcode = []

print(front_node)
print(front_code[0])

# print(class_set)
# len(h[]=2708) = n(node)   len(h[][] = 1433) = n(words) -- feature matrices

# for k in range(K):  # hop数  K
#     for m in range(len(x)):  # 节点个数  M
#         h[][k] = Virtualized()
#         h[][k] = Virtualized()
#         order = h[][k] + h[][k]
#         for u in order:
#              h[][] = LSTM(h[][])
#         h[][] = Sigma()
# z[] = h[][]