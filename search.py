# USAGE
# python search.py --index index.csv --query queries_test/ --result-path dataset_test

# import the necessary packages
from pyimagesearch.colordescriptor import ColorDescriptor
from pyimagesearch.searcher import Searcher
import argparse
import cv2
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())

# initialize the image descriptor
cd = ColorDescriptor((8, 12, 3))

# load the query image and describe it
query = cv2.imread(args["query"])
features = cd.describe(query)

# perform the search
searcher = Searcher(args["index"])
results = searcher.search(features)

# display the query
cv2.imshow("Query", cv2.resize(query,(0,0),fx=0.5,fy=0.5))

# loop over the results
i=0
for (score, resultID) in results:
	# load the result image and display it
	i=i+1
	result = cv2.imread(args["result_path"] + "/" + resultID)
	result = cv2.resize(result,(0,0),fx=0.5,fy=0.5)
	cv2.imshow("Result", result)
	cv2.waitKey(0)
	if i==4: break
