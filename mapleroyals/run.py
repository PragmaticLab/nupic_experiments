import sys
sys.path.append('model_0')
import model_params
from nupic.frameworks.opf.modelfactory import ModelFactory
from scrape_data import getPlayersOnline
import time
import datetime
from Queue import Queue
import csv


predictionSteps = 1
model = ModelFactory.create(model_params.MODEL_PARAMS)
model.enableInference({'predictedField': 'players'})

resultFile = open("output.txt", 'w', 0)
resultWriter = csv.writer(resultFile)
resultWriter.writerow(["timestamp","prediction","actual"])
resultWriter.writerow(["datetime","int","int"])
resultWriter.writerow(["T","",""])
futureFile = open("future.txt", 'w', 0)
futureWriter = csv.writer(futureFile)
futureWriter.writerow(["timestamp","players"])
futureWriter.writerow(["datetime","int"])
futureWriter.writerow(["T",""])

predictionQueue = Queue(maxsize=10)
for i in range(predictionSteps):
	predictionQueue.put(-1)
count = 0
while True:
	players = getPlayersOnline()
	timestamp = datetime.datetime.now()
	result = model.run({
		"timestamp": timestamp,
		"players": players
	})
	predictionQueue.put(result.inferences["multiStepBestPredictions"][1])
	prediction = predictionQueue.get()
	print str(timestamp) + ". predicted: " + str(prediction) + ", actual: " + str(players)
	resultWriter.writerow([timestamp, prediction, players])
	futureWriter.writerow([timestamp, players])
	if count % 1000 == 0:
		model.save("production_model")
	time.sleep(60)
	count += 1
