'''
Tag-graph embedding generation algorithm
'''

from utils import *
import numpy as np
from numpy import *

# Initialize
x,cites,content,class_set = load_data()
order = []  # Create an empty list
K = 3  # hops
h = [[] for i in range(K+1)]  # temp matrices
# print(x[0][0])  # [[0,...,0],[...],...,[...]]

h[0]+=x[:]
front_code = front_node_garthing(x,cites,content,class_set)
behind_code = behind_node_garthing(x,cites,content,class_set)

temp = []
emb = []
# ave_front_code = ave(front_code)
# ave_behind_code = ave(behind_code)

# len(h[]=2708) = n(node)   len(h[][] = 1433) = n(words) -- feature matrices
h_front = summ(ave(front_node_garthing(x,cites,content,class_set)),x)
h_behind = summ(ave(behind_node_garthing(x,cites,content,class_set)),x)
# h = ave(h_front_cal(x,cites,content,class_set,h_front))
#
for i in h_front:
    print(i)
print(len(h_front))
# exit(0)
order_set = []
M = len(x[:])
# h_sum = sum(h_front)
for k in range(1,K+1):  # hop数  K
    h_front.append(summ(ave(h_front_cal(x, cites, content, class_set,h_front[k-1])),x))
    h_behind.append(summ(ave(h_behind_cal(x, cites, content, class_set,h_behind[k-1])),x))
    temp = []
    for m in range(M):
        temp.append(h_front[k][m]+h_behind[k][m])  # 拼接
    order_set.append(temp)

# op = 'train'  # or test
#
# if op == 'train':
#

