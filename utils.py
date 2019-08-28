import numpy as np

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

        for cls in class_set:
            for line in content:
                if line[0] in temp_frontnode and line[-1] == cls:
                    temp.append(list(map(int,line[1:-1])))
        temp_frontcode.append(temp)

        temp = []

        front_node.append(temp_frontnode)
        front_code += temp_frontcode
        # pure_code += temp_frontcode[1:-1]

        temp_frontnode = []
        temp_frontcode = []

    return front_code

def ave(front_code):
    ave_code = []
    ___ = []
    for i in front_code:  # each node
        for j in i:  # each class
            if len(j) > 2:
                ___.append(np.sum([k for k in j], axis=0) / len(j))
            else:
                ___.append(j)
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

        for cls in class_set:
            for line in content:
                if line[0] in temp_behindnode and line[-1] == cls:
                    temp.append(list(map(int,line[1:-1])))
        temp_behindcode.append(temp)

        temp = []

        behind_node.append(temp_behindnode)
        behind_code += temp_behindcode

        temp_behindnode = []
        temp_behindcode = []

    return behind_code


def Virtualized():
    pass
