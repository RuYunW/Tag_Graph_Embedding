'''
Tag-graph embedding generation algorithm
'''

from utils import *
import numpy as np
from numpy import *

# Initialize
x,cites,content,class_set = load_data()
order = []  # Create an empty list
K = 5  # hops
h = [[] for i in range(K+1)]  # temp matrices
# print(x[0][0])  # [[0,...,0],[...],...,[...]]

h[0]+=x[:]
front_code = front_node_garthing(x,cites,content,class_set)
behind_code = behind_node_garthing(x,cites,content,class_set)


temp = []
emb = []
ave_front_code = ave(front_code)
ave_behind_code = ave(behind_code)

for i in ave_behind_code:
    print(i)
# len(h[]=2708) = n(node)   len(h[][] = 1433) = n(words) -- feature matrices
# h_front = []
# h_behind = []
# for k in range(K):  # hop数  K
#     for m in range(len(x)):  # 节点个数  M
#         h[][k] = Virtualized()
#         h[][k] = Virtualized()
#         order = h[][k] + h[][k]
#         for u in order:
#              h[][] = LSTM(h[][])
#         h[][] = Sigma()
# z[] = h[][]