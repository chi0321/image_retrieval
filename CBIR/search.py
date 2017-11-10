from colordescriptor import ColorDescriptor
from vgg16descriptor import Vgg16Descriptor
from searcher import Searcher
import argparse
import cv2
import numpy as np
from flask import Flask

ap = argparse.ArgumentParser()
ap.add_argument("-c","--index1",required = True,
				help="Path to where the cd computed index will be stored")
ap.add_argument("-v","--index2",required = True,
				help="Path to where the vd computed index will be stored")
ap.add_argument("-q","--query",required = True,
				help="Path to the query image")
ap.add_argument("-r","--result_path",required = True,
				help="Path to the result path")
args = vars(ap.parse_args())

	
cd = ColorDescriptor((8,12,3))
vd = Vgg16Descriptor((224,224,3))

query = cv2.imread(args['query'])
feature1 = cd.describe(query)
feature2 = vd.describe(args['query'])

searcher = Searcher(args["index1"],args["index2"])
results = searcher.search(feature1,feature2)

result0 = cv2.resize(query,(128,128),interpolation=cv2.INTER_CUBIC)	

name = locals()
i = 1

for (score, resultID) in results:
	name['result%d'%i] = cv2.imread(args["result_path"] + "/" + resultID)
	name['result%d'%i] = cv2.resize(name['result%d'%i],(128,128),interpolation=cv2.INTER_CUBIC)	
	i = i + 1
	
result = np.hstack(name['result%d'%i] for i in range(0,11))
name = "Result"
cv2.imshow(name, result)
cv2.waitKey(0)