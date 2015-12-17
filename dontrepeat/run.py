import sys
import importlib
import csv
import random
from nupic.frameworks.opf.modelfactory import ModelFactory
from model_params import dontrepeat_model_params
from generate_data import my_map

SIM_COUNT = 500

predictionSteps = 1
model = ModelFactory.create(dontrepeat_model_params.MODEL_PARAMS)
model.enableInference({'predictedField': 'status'})

resultFile = open("output.txt", 'w', 0)
resultWriter = csv.writer(resultFile)
resultWriter.writerow(["predicted", "actual", "correct"])
resultWriter.writerow(["string", "string", "string"])
resultWriter.writerow(["", ""])

count = 0
lastHand = "cathy"
status = "cat"
while count < SIM_COUNT:
    hand = my_map[int(random.random() * 2)]
    print hand, lastHand, status
    row = {
        "hand": hand,
        "lastHand": lastHand,
        "status": status
    }
    result = model.run(row)
    futurePrediction = result.inferences["multiStepBestPredictions"][predictionSteps]
    correct = False
    if futurePrediction == status:
        correct = True
    resultWriter.writerow([futurePrediction, status, correct])
    status = "not_same" if hand != lastHand else "same" # this is added in the next round
    lastHand = hand
    if count % 100 == 0:
        print "count: " + str(count)
    count += 1
