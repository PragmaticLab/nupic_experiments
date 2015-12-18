from dataapi import getDataSteam
import sys
import importlib
import csv
import random
from Queue import Queue
from nupic.frameworks.opf.modelfactory import ModelFactory
from model_params import exercise_model_params

predictionSteps = 1
model = ModelFactory.create(exercise_model_params.MODEL_PARAMS)
model.enableInference({'predictedField': 'torso'})

resultFile = open("output.txt", 'w', 0)
resultWriter = csv.writer(resultFile)
resultWriter.writerow(["activity_person","torso","score"])
resultWriter.writerow(["string","float","float"])
resultWriter.writerow(["", "",""])

for activity, person in [(10, 5), (10, 6), (5, 6)]:
	activity_person = str(activity) + "_" + str(person)
	for line in getDataSteam(activity, person):
		torso = line[0]
		row = {"torso": torso}
		result = model.run(row)
		futurePrediction = result.inferences["multiStepBestPredictions"][predictionSteps]
		anomalyScore = result.inferences["anomalyScore"]
		resultWriter.writerow([activity_person, torso, anomalyScore])
