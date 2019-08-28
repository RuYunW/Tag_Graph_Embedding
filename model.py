'''
Tag-graph embedding generation algorithm
'''

from utils import load_data,node_garthing
import numpy as np
from numpy import *

# Initialize
x,cites,content,class_set = load_data()
order = []  # Create an empty list
K = 5  # hops
h = [[] for i in range(K+1)]  # temp matrices
# print(x[0][0])  # [[0,...,0],[...],...,[...]]

h[0]+=x[:]
front_code = node_garthing(x,cites,content,class_set)

temp = []
emb = []




# print(type(front_code[0][0][0]))
ave_node = []
___ = []
for i in front_code:  # each node
    for j in i:  # each class
        if len(j) >2:
            ___.append(np.sum([k for k in j],axis=0)/len(j))
        else:
            ___.append(j)
    ave_node.append(___)


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