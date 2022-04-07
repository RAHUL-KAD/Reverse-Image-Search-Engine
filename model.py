import streamlit as st
import numpy as np
import pickle
from tqdm import tqdm, tqdm_notebook
import random
import time
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import PIL
from PIL import Image
from numpy.linalg import norm
from sklearn.neighbors import NearestNeighbors

import tensorflow as tf
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions, ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow import keras

import glob
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.decomposition import PCA

image_to_test = '/home/rahul/Desktop/ml_project/image_search/images/test1.png'

filenames = pickle.load(open('/home/rahul/Desktop/ml_project/image_search/Models/filenames-caltech101.pickle', 'rb'))
feature_list = pickle.load(open('/home/rahul/Desktop/ml_project/image_search/Models/features-caltech101-resnet-finetuned.pickle', 'rb'))
finetuned_resnet_model = '/home/rahul/Desktop/ml_project/image_search/Models/resnet_model-finetuned.h5'

ResNet50_model = ResNet50(weights='imagenet',
                         include_top=False,
                         input_shape=(224, 224, 3),
                        pooling='max')

ResNet50_finetuned_model = keras.models.load_model(finetuned_resnet_model)
# process the image so we can pass it through model
def extract_features(image_path, model):
  # img = image.load_img(image_path, target_size=(224, 224))
  image_array = image.img_to_array(image_path)
  
  expanded_image_array = np.expand_dims(image_array, axis=0)
  processed_image = preprocess_input(expanded_image_array)
  features = model.predict(processed_image)
  flattened_features = features.flatten()
  normalized_features = flattened_features / norm(flattened_features)
  return normalized_features

#input_image = extract_features(image_to_test, ResNet50_model)
neighbors = NearestNeighbors(n_neighbors=50,
                             algorithm='brute',
                             metric='euclidean').fit(feature_list)

# input_image = extract_features(image_to_test, ResNet50_finetuned_model)                              
# distances, indices = neighbors.kneighbors([input_image])

# print(distances, indices)

# plt.imshow(mpimg.imread(filenames[indices[0][2]]), interpolation='lanczos')
# plt.show()