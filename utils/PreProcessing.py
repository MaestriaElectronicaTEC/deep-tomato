import cv2
import glob
import numpy as np

from tensorflow.keras.preprocessing.image import ImageDataGenerator

#----------------------------------------------------------------------------

def normalize_data(img):
    return (img.astype(np.float32) - 127.5) / 127.5

def load_real_samples(datadir, data_batch_size=64):

    trainAug = ImageDataGenerator(
            rotation_range=20,
            zoom_range=0.05,
            width_shift_range=0.1,
            height_shift_range=0.1,
            shear_range=0.05,
            horizontal_flip=True,
            vertical_flip=True,
            fill_mode="nearest",
            preprocessing_function=normalize_data)

    trainGen = trainAug.flow_from_directory(
            datadir,
            class_mode="input",
            target_size=(48, 48), #TODO: Remove hardcoded dimensions
            color_mode="rgb",
            shuffle=True,
            batch_size=data_batch_size)

    return trainGen

def load_test_data(data_dir):
    img_list = glob.glob(data_dir + '*.png')
    images = list()
    
    for img_path in img_list:
        img = cv2.imread(img_path)
        img = cv2.resize(img, (48, 48), interpolation = cv2.INTER_NEAREST)
        img = (img.astype(np.float32) - 127.5) / 127.5
        images.append(img)
        
    print('Found ' + str(len(images)) + ' images for test.')
    return np.asarray(images)