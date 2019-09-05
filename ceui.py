from keras.layers import LSTM,Dense,Dropout,Flatten
from keras.models import Sequential
import numpy as np

a = [[[0.5,0.7,0.25],
      [0.6,0.7,0.2],
      [0.3,0.34,0.22],
      [0.435,0.432,0.234]],
     [[0.33,0.45,0.23],
      [0.34,0.21,0.11],
      [0.43,0.3452,0.25],
      [0.657,0.76,0.456]],
     [[0.45,0.15,0.55],
      [0.212,0.234,0.432],
      [0.321,0.543,0.342],
      [0.423,0.56,0.12]],
     [[0.5,0.7,0.25],
      [0.6,0.7,0.2],
      [0.3,0.34,0.22],
      [0.435,0.432,0.234]],
     [[0.33,0.45,0.23],
      [0.34,0.21,0.11],
      [0.43,0.3452,0.25],
      [0.657,0.76,0.456]]]
b = [[1,0,1,2],
     [1,1,0,3],
     [4,2,3,2],
     [1,0,1,4],
     [1,1,0,2]]
# a = a.reshape(len(a),-1)

def build_model():
    model = Sequential()
    model.add(LSTM(
        units = 3,
        return_sequences=True,
        # stateful=True,
        batch_input_shape=(5,4,3),
        # time_step = 3,
        activation='relu'
    ))

    model.add(Dense(output_dim = 3,activation='relu'))

    # model.add(LSTM(32, return_sequences=True, stateful=True,
    #                batch_input_shape=(32, 1, (K*node_num,code_length))))
    model.add(LSTM(32, return_sequences=True))
    model.add(LSTM(32))
    model.add(Dense(4, activation='softmax'))

    # model.add(Dense(
    #     output_dim = 5,
    #     activation='relu',
    # ))
    # model.add(Flatten())
    # model.add(Dropout(0.5))
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    model.summary()
    return model

model = build_model()
model.fit(np.array(a),np.array(b),epochs = 10)
# testX = np.array(a)

# for i in range(len(testX)):
# x = [[[0.5,0.7,0.25],[0.6,0.7,0.2],[0.3,0.34,0.22],[0.435,0.432,0.234]]]
# x = a+a
# print(model.predict(np.array(x)))
# print(np.argmax(model.predict(np.array(x)),axis=1))
# b = [[[0.33,0.45,0.23],[0.34,0.21,0.11],[0.43,0.3452,0.25],[0.657,0.76,0.456]]]
# print(model.predict(np.array(b)))
# print(np.argmax(model.predict(np.array(b)),axis=1))
model.save('ceui.h5')
c = a+a
d = b+b
print(c)
print(d)
 # = [b[0],b[1]]
acc = model.evaluate(np.array(c),np.array(d))
print(acc)
