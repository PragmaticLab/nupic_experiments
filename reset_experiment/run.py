import sys
import importlib
import csv
import random
from Queue import Queue
from nupic.frameworks.opf.modelfactory import ModelFactory
from model_params import num_model_params

predictionSteps = 1
model = ModelFactory.create(num_model_params.MODEL_PARAMS)
model.enableInference({'predictedField': 'num'})

resultFile = open("output.txt", 'w', 0)
resultWriter = csv.writer(resultFile)
resultWriter.writerow(["isReset","score"])
resultWriter.writerow(["string","float"])
resultWriter.writerow(["",""])

csvReader = csv.reader(open('reset.csv'))
# skip header rows
csvReader.next()
csvReader.next()
csvReader.next()


for row in csvReader:
	rr = int(row[0])
	num = row[1]
	row = {
		"rr": rr,
		"num": num
	}
	result = model.run(row)
	futurePrediction = result.inferences["multiStepBestPredictions"][predictionSteps]
	anomalyScore = result.inferences["anomalyScore"]
	isReset = rr == 1
	resultWriter.writerow([isReset, anomalyScore])
