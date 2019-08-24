
def load_data(cites_path = './data/cora.cites',content_path = './data/cora.content'):
    with open(content_path,'r') as f1:
        lines = f1.readlines()

        '''
        etc……
        '''
    x = []
    for i in range(len(lines)):
        x.append(lines[i].split('\t')[1:-1])
    return x
# load_data()

# def LSTM():
