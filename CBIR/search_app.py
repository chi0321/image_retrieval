from colordescriptor import ColorDescriptor
from vgg16descriptor import Vgg16Descriptor
from searcher import Searcher
import argparse
import cv2
import numpy as np
class SearchApp():
	def __init__(self, querypath, filename):
		self.querypath = querypath
		self.filename = filename
	
	def searchimg(self, index1='index1.csv', index2='index2.csv', result_path='jpg'):
		cd = ColorDescriptor((8,12,3))
		vd = Vgg16Descriptor((224,224,3))
		query = cv2.imread("./query/" + self.filename)
		feature1 = cd.describe(query)
		feature2 = vd.describe(self.querypath)

		searcher = Searcher(index1,index2)
		results = searcher.search(feature1,feature2)

		result0 = cv2.resize(query,(128,128),interpolation=cv2.INTER_CUBIC)	

		name = locals()
		i = 1

		for (score, resultID) in results:
			name['result%d'%i] = cv2.imread(result_path + "/" + resultID)
			name['result%d'%i] = cv2.resize(name['result%d'%i],(128,128),interpolation=cv2.INTER_CUBIC)	
			i = i + 1
			
		result_0 = np.hstack(name['result%d'%i] for i in range(1,6))
		result_1 = np.hstack(name['result%d'%i] for i in range(6,11))
		result = np.vstack((result_0,result_1))
		cv2.imwrite("./result/%s" % self.filename, result)
		return self.filename