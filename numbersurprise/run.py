import sys
import importlib
import csv
import random
from Queue import Queue
from nupic.frameworks.opf.modelfactory import ModelFactory
from model_params import num_model_params

SIM_COUNT = 1000

predictionSteps = 1
model = ModelFactory.create(num_model_params.MODEL_PARAMS)
model.enableInference({'predictedField': 'num'})

resultFile = open("output.txt", 'w', 0)
resultWriter = csv.writer(resultFile)
resultWriter.writerow(["isUnusual","score"])
resultWriter.writerow(["string","float"])
resultWriter.writerow(["",""])

count = 0
while count < SIM_COUNT:
	num = "shh" if random.random() > 0.99 else "BOOH"
	row = {
		"num": num
	}
	result = model.run(row)
	futurePrediction = result.inferences["multiStepBestPredictions"][predictionSteps]
	anomalyScore = result.inferences["anomalyScore"]
	isUnusual = num == "BOOH"
	resultWriter.writerow([isUnusual, anomalyScore])
	
	if count % 100 == 0:
		print "count: " + str(count)
	count += 1
