import os
os.chdir('C:/Users/leeha/Documents/pythons/Ripe Mango Detector/')
home_dir = 'C:/Users/leeha/Documents/pythons/Ripe Mango Detector/'
         
import numpy as np
import matplotlib.pyplot as plt
import cv2
import random
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D  

training_data = []
IMG_SIZE = 50
final_input = []
categories = ['Ripe Mango', 'Green Mango']

class Mango:
    # Process images
    def create_training_data():    
        for category in categories:
            path = os.path.join(home_dir, category)
            class_num = categories.index(category)
            for img in os.listdir(path):
                img_array = cv2.imread(os.path.join(path, img))
                img_rgb = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
                new_array = cv2.resize(img_rgb, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
            # plt.imshow(new_array)
            # plt.show()
            # break
    
    def process_input():
        print('Enter image name (include extension):')
        input_img = input()
        input_array = cv2.imread(os.path.join(home_dir, input_img))
        input_rgb = cv2.cvtColor(input_array, cv2.COLOR_BGR2RGB)
        new_input_array = cv2. resize(input_rgb, (IMG_SIZE, IMG_SIZE))
        final_input.append([new_input_array])
        # plt.imshow(new_input_array)
        # plt.show()

    
    def train_model():
        X = []
        y = []
        # Separate training data into features (X) and labels (y)
        for features, label in training_data:
            X.append(features)
            y.append(label)
            
        X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 3)
        y = np.array(y)
        
        # Save training data
        import pickle
        
        pickle_out = open('X.pickle', 'wb')
        pickle.dump(X, pickle_out)
        pickle_out.close()
        
        pickle_out = open('y.pickle', 'wb')
        pickle.dump(y, pickle_out)
        pickle_out.close()
        
        # # Load training data to show if it worked
        # X = []
        # pickle_in = open('X.pickle', 'rb')
        # X = pickle.load(pickle_in)
        
        # print(X[0])
        
        X = pickle.load(open('X.pickle', 'rb'))
        y = pickle.load(open('y.pickle', 'rb'))
        
        X = X/225.0
        
        model = Sequential()
        model.add(Conv2D(32, (3,3), input_shape = (IMG_SIZE, IMG_SIZE,3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))
        
        model.add(Conv2D(64, (3,3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))
        
        # Converts 3D feature maps to 1D feature vectors
        model.add(Flatten())
        model.add(Dense(512))
        model.add(Activation('relu'))
        
        model.add(Dense(1))
        model.add(Activation('sigmoid'))
        
        model.compile(loss='binary_crossentropy',
                      optimizer = 'adam',
                      metrics = ['accuracy'])
        
        model.fit(X, y, batch_size=8, epochs=3, validation_split=0.05)
        
        
        new_input = np.array(final_input).reshape(-1, IMG_SIZE, IMG_SIZE, 3)
        
        new_output = model.predict(new_input)
        output_index = int(new_output[0][0])
        
        if output_index == 0:
            print('\nRipe mango')
        else:
            print('\nNot ripe mango')
            
            
    create_training_data()
    process_input()
    train_model()
