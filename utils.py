import numpy as np
# from model import *
from keras.layers import LSTM,Dense,Dropout
from keras.models import Sequential

def load_data(cites_path = './data/cora.cites',content_path = './data/cora.content'):
    with open(content_path,'r') as f1:
        lines = f1.readlines()
    x = []
    for i in range(len(lines)):
        x.append(lines[i].split('\t')[0:-1])

    cites = []
    with open(cites_path,'r') as f_cites:
        lines = f_cites.readlines()
    for line in lines:
        cites.append(line.replace('\n','').split('\t'))

    content = []
    with open(content_path,'r') as f_co:
        lines = f_co.readlines()
    for line in lines:
        content.append(line.replace('\n','').split('\t'))

    class_set = set(np.array(content[:])[:,-1])
    return x,cites,content,class_set
# load_data()

# def LSTM():

def front_node_garthing(x,cites,content,class_set):
    temp_frontnode = []
    temp_frontcode = []
    front_node = []
    front_code = []
    temp = []
    # pure_code = []

    for node_id in np.array(x)[:, 0]:  # content第一列顺序
        for line in cites:
            if line[1] == node_id:
                temp_frontnode.append(line[0])
        # 找到所有前序节点temp_frontnode

        for cls in class_set:
            for line in content:
                if line[0] in temp_frontnode and line[-1] == cls:
                    temp.append(list(map(int,line[1:-1])))
            # 节点node某一cls的所有code存入temp
            temp_frontcode.append(temp)
            temp = []

        front_node.append(temp_frontnode)
        front_code.append(temp_frontcode)
        # pure_code += temp_frontcode[1:-1]

        temp_frontnode = []
        temp_frontcode = []

    return front_code

def ave(front_code):
    ave_code = []
    ___ = []
    for i in front_code:  # each node
        for j in i:  # each class
            # ___ is used to save one class ave value
            if len(j) >= 1:
                ___.append((np.sum([k for k in j],axis=0)/len(j)).tolist())
        # each class ave has been calculated, saving in ___
        ave_code.append(___)
        ___ = []

    return ave_code


def behind_node_garthing(x,cites,content,class_set):
    temp_behindnode = []
    temp_behindcode = []
    behind_node = []
    behind_code = []
    temp = []

    for node_id in np.array(x)[:, 0]:  # content第一列顺序
        for line in cites:
            if line[0] == node_id:
                temp_behindnode.append(line[1])
        # 找到所有前序节点temp_frontnode

        for cls in class_set:
            for line in content:
                if line[0] in temp_behindnode and line[-1] == cls:
                    temp.append(list(map(int,line[1:-1])))
            # 节点node某一cls的所有code存入temp
            temp_behindcode.append(temp)
            temp = []

        behind_node.append(temp_behindnode)
        behind_code.append(temp_behindcode)
        # pure_code += temp_frontcode[1:-1]

        temp_behindnode = []
        temp_behindcode = []

    return behind_code

def h_front_cal(x,cites,content,class_set,h_front):
    temp_frontnode = []
    temp_frontcode = []
    front_node = []
    front_code = []
    temp = []
    # pure_code = []

    for node_id in np.array(x)[:, 0]:  # content第一列顺序
        for line in cites:
            if line[1] == node_id:
                temp_frontnode.append(line[0])
        # 找到所有前序节点temp_frontnode

        for cls in class_set:
            for line in content:
                counter = 0
                if line[0] in temp_frontnode and line[-1] == cls:
                    temp.append(h_front[counter])
                counter += 1
            # 节点node某一cls的所有code存入temp
            temp_frontcode.append(temp)
            temp = []

        front_node.append(temp_frontnode)
        front_code.append(temp_frontcode)
        # pure_code += temp_frontcode[1:-1]

        temp_frontnode = []
        temp_frontcode = []

    return front_code


def summ(h,code_length):
    __ = []
    for i in h:
        if len(i) >= 1:
            __.append(np.sum([ j for j in i],axis=0).tolist())
        else:
            __.append([0 for _ in range(code_length)])  # 空用0填补
    # sum each vir_class code within one
    return __

def h_behind_cal(x,cites,content,class_set,h_behind):
    temp_behindnode = []
    temp_behindcode = []
    behind_node = []
    behind_code = []
    temp = []
    # pure_code = []

    for node_id in np.array(x)[:, 0]:  # content第一列顺序
        for line in cites:
            if line[0] == node_id:
                temp_behindnode.append(line[1])
        # 找到所有前序节点temp_frontnode

        for cls in class_set:
            for line in content:
                counter = 0
                if line[0] in temp_behindnode and line[-1] == cls:
                    temp.append(h_behind[counter])
                counter += 1
            # 节点node某一cls的所有code存入temp
            temp_behindcode.append(temp)
            temp = []

        behind_node.append(temp_behindnode)
        behind_code.append(temp_behindcode)
        # pure_code += temp_frontcode[1:-1]

        temp_behindnode = []
        temp_behindcode = []

    return behind_code

def build_model():
    model = Sequential()
    model.add(LSTM(output_dim=32,
                   return_sequences=True,
                   input_shape=(2708,2866),
                   activation='relu'
                   ))
    for i in range(3):
        model.add(LSTM(output_dim=32 * (i + 1),
                       activation='relu',
                       return_sequences=True
                       ))

    for i in range(3):
        model.add(Dense(output_dim=1433,
                        activation='relu'))
        model.add(Dropout(0.5))

    model.compile(loss='mae', optimizer='adam', metrics=['accuracy'])
    model.summary()
    return model


def Virtualized():
    pass

def lstm(h):
    pass
