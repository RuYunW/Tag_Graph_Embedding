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


# print(len(front_code))


temp = []
emb = []
# ave_front_code = ave(front_code)
# ave_behind_code = ave(behind_code)

# len(h[]=2708) = n(node)   len(h[][] = 1433) = n(words) -- feature matrices
h_front = ave(front_node_garthing(x,cites,content,class_set))
h_behind = ave(behind_node_garthing(x,cites,content,class_set))


h = ave(h_front_cal(x,cites,content,class_set,h_front))
print(len(h))
for i in h:
    print(i)
# for i in h:
#     print(len(i))
print(len(h))
print(len(h_front))

# for k in range(K):  # hop数  K
#     h_front += ave(front_node_garthing(x, cites, content, class_set))
#     h_behind += ave(behind_node_garthing(x, cites, content, class_set))
#
#     for m in range(len(x)):  # 节点个数  M
#         order = h[][k] + h[][k]
#         for u in order:
#              h[][] = LSTM(h[][])
#         h[][] = Sigma()
# z[] = h[][]