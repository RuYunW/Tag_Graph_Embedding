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

def Virtualized():
    pass
