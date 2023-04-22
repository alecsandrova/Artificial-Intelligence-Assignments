# banknote_bnn.py
import numpy as np
import keras as K
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'  # suppress CPU msg

class MyLogger(K.callbacks.Callback):
  def __init__(self, n):
    self.n = n   # print loss & acc every n epochs

  def on_epoch_end(self, epoch, logs={}):
    if epoch % self.n == 0:
      curr_loss =logs.get('loss')
      curr_acc = logs.get('accuracy') * 100
      print("epoch = %4d loss = %0.6f acc = %0.2f%%" % \
        (epoch, curr_loss, curr_acc))

def main():
  print("Divorce predictors")
  np.random.seed(1)

  # 1. load data into memory
  train_file = "D:\\01_FACULTATE\\03_SEM1\\04_INTELIGENTA ARTIFICIALA\TEME\\04_Tema_Keras\\divorce\\divorce.txt"
  test_file = "D:\\01_FACULTATE\\03_SEM1\\04_INTELIGENTA ARTIFICIALA\TEME\\04_Tema_Keras\\divorce\\divorce_test.txt"
  train_x = np.loadtxt(train_file, delimiter=';',
  usecols=[0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], dtype=np.float32)
  train_y = np.loadtxt(train_file, delimiter=';',
  usecols=[54], dtype=np.float32)  
  test_x = np.loadtxt(test_file, delimiter=';', 
  usecols=[0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], dtype=np.float32)
  test_y =np.loadtxt(test_file, delimiter=';',
  usecols=[54], dtype=np.float32)
  # 2. define 4-(x-x)-1 deep NN model
  my_init = K.initializers.glorot_uniform(seed=1)
  model = K.models.Sequential()
  model.add(K.layers.Dense(units=8, input_dim=55,
  activation='tanh', kernel_initializer=my_init)) 
  model.add(K.layers.Dense(units=8, activation='tanh',
  kernel_initializer=my_init)) 
  model.add(K.layers.Dense(units=1, activation='sigmoid',
  kernel_initializer=my_init))
  # 3. compile model
  simple_sgd = K.optimizers.SGD(lr=0.01)  
  model.compile(loss='binary_crossentropy',
  optimizer=simple_sgd, metrics=['accuracy'])  
  # 4. train model
  max_epochs = 500
  my_logger = MyLogger(n=50)
  h = model.fit(train_x, train_y, batch_size=32,
  epochs=max_epochs, verbose=0, callbacks=[my_logger])
  # 5. evaluate model
  np.set_printoptions(precision=4, suppress=True)
  eval_results = model.evaluate(test_x, test_y, verbose=0) 
  print("\nLoss, accuracy on test data: ")
  print("%0.4f %0.2f%%" % (eval_results[0], \
  eval_results[1]*100))

  mp = ".\\Models\\banknote_model.h5"
  model.save(mp)
  # 6. make a prediction
  inpts = np.array([[0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]], dtype=np.float32)
  pred = model.predict(inpts)
  print("\nPredicting posibility of divorce: ")
  print(inpts)
  print("Probability that class = 1 (true):")
  print(pred)

if __name__=="__main__":
  main()