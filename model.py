'''
Tag-graph embedding generation algorithm
'''

from utils import *
import numpy as np
from numpy import *
from keras.layers import LSTM,Dense,Dropout
from keras.models import Sequential

# Initialize
x,cites,content,class_set = load_data()
order = []  # Create an empty list
K = 2  # hops
h = [[] for i in range(K+1)]  # temp matrices
code_length = 1433
# print(x[0][0])  # [[0,...,0],[...],...,[...]]

h[0]+=x[:]
y = np.array(h[0])[:,[i for i in range(1,code_length+1)]].tolist()

# front_code = front_node_garthing(x,cites,content,class_set)
# behind_code = behind_node_garthing(x,cites,content,class_set)

temp = []
emb = []
# ave_front_code = ave(front_code)
# ave_behind_code = ave(behind_code)

h_front = [[] for i in range(K+1)]
h_behind = [[] for i in range(K+1)]
# len(h[]=2708) = n(node)   len(h[][] = 1433) = n(words) -- feature matrices
h_front[0] = summ(ave(front_node_garthing(x,cites,content,class_set)),code_length)
h_behind[0] = summ(ave(behind_node_garthing(x,cites,content,class_set)),code_length)

# h = ave(h_front_cal(x,cites,content,class_set,h_front))

order_set = []
M = len(x[:])  # 2708

# h_sum = sum(h_front)
for k in range(1,K+1):  # hop数  K
    h_front[k] = summ(ave(h_front_cal(x, cites, content, class_set,h_front[k-1])),code_length)
    h_behind[k] = summ(ave(h_behind_cal(x, cites, content, class_set,h_behind[k-1])),code_length)
    temp = []
    for m in range(M):
        temp.append(h_front[k][m]+h_behind[k][m])  # 拼接
    order_set.append(temp)


# for i in order_set:
#     print(len(i))
# print(len(order_set))

# print(len(y))
# print(len(order_set))
# print(len(order_set[0]))
# print(len(order_set[0][0]))
# print(len(y[0]))

model = build_model()
for i in order_set:  # K
    for j in i:
        model.fit(np.array(j),y,batch_size=32,epochs=10,verbose=1)

