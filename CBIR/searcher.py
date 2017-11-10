import numpy as np
import csv

class Searcher:
	def __init__(self, indexPath1, indexPath2):
		self.indexPath1 = indexPath1
		self.indexPath2 = indexPath2
		
	def search(self, queryFeatures1, queryFeatures2, limit=10):
		results1 = {}
		results2 = {}
		results = {}
		with open(self.indexPath1) as f:
			reader = csv.reader(f)
			for row in reader:
				features = [float(x) for x in row[1:]]
				d = self.chi2_distance(features, queryFeatures1)
				results1[row[0]] = d
			f.close()
		with open(self.indexPath2) as f:
			reader = csv.reader(f)
			for row in reader:
				features = [float(x) for x in row[1:]]
				d = self.chi2_distance(features, queryFeatures2)
				results[row[0]] = d*0.9+results1[row[0]]*0.1
			f.close()
		"""with open(self.indexPath1) as f1:
			with open(self.indexPath2) as f2:
				reader1 = csv.reader(f1)
				reader2 = csv.reader(f2)
			
				for row1 in reader1:
					for row2 in reader2:
					
						features1 = [float(x) for x in row1[1:]]
						features2 = [float(x) for x in row2[1:]]
						
						d1 = self.chi2_distance(features1, queryFeatures1)
						print(queryFeatures2)
						#d2 = self.chi2_distance(features2, queryFeatures2)/1024
						results[row2[0]] = d1
				
			f2.close()
		f1.close()"""
		results = sorted([(v,k) for (k,v) in results.items()])
		return results[:limit]
			
	def chi2_distance(self, histA,histB,eps=1e-10):
		d = 0.5*np.sum([(a-b)**2/(a+b+eps) for (a,b) in zip(histA,histB)])
		return d