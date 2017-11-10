import numpy as np
from numpy import linalg as LA

from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input

class Vgg16Descriptor:
	def __init__(self, inputshape):
		self.shape = inputshape
		
	def describe(self, img_path):
		input_shape = self.shape
		
		model = VGG16(weights = 'imagenet', input_shape = (input_shape[0], input_shape[1], input_shape[2]), pooling = 'max', include_top = False)
        
		img = image.load_img(img_path, target_size=(input_shape[0], input_shape[1]))
		img = image.img_to_array(img)
		img = np.expand_dims(img, axis=0)
		img = preprocess_input(img)
		feat = model.predict(img)
		norm_feat = feat[0]/LA.norm(feat[0])
		return norm_feat
		