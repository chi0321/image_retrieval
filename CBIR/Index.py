import colordescriptor
import vgg16descriptor
import thetadescriptor
import argparse
import glob
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-d","--dataset",required=True,help="Path to the directory that cntains the images to be indexed.") 
#ap.add_argument("-c","--index1",required=True,help="Path to where the cd computed index will be stored")
#ap.add_argument("-v","--index2",required=True,help="Path to where the vd computed index will be stored")
ap.add_argument("-t","--index3",required=True,help="Path to where the td computed index will be stored")
args = vars(ap.parse_args())
#cd = colordescriptor.ColorDescriptor((8,12,3))
#vd = vgg16descriptor.Vgg16Descriptor((224, 224, 3))
td = thetadescriptor.ImageTheta()

#output1 = open(args["index1"],"w")
#output2 = open(args["index2"],"w")
output3 = open(args["index3"],"w")

for imagePath in glob.glob(args["dataset"]+"/*.jpg"):

	imageID = imagePath[imagePath.rfind("\\")+1:]
	image = cv2.imread(imagePath)
	
#	feature1 = cd.describe(image)
#	feature2 = vd.describe(imagePath)
	feature3 = td.describe(imagePath)
	
#	feature1 = [str(f) for f in feature1]
#	feature2 = [str(f) for f in feature2]
	feature3 = [str(f) for f in feature3]
	
#	output1.write("%s,%s\n" % (imageID, ",".join(feature1)))
#	output2.write("%s,%s\n" % (imageID, ",".join(feature2)))
	output3.write("%s,%s\n" % (imageID, ",".join(feature3)))
	
#output1.close()
#output2.close()
output3.close()