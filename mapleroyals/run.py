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
	if players == -1:
		time.sleep(60)
		continue
	timestamp = datetime.datetime.now()
	result = model.run({
		"timestamp": timestamp,
		"players": players
	})
	futurePrediction = int(result.inferences["multiStepBestPredictions"][1])
	predictionQueue.put(futurePrediction)
	prediction = predictionQueue.get()
	print str(timestamp) + ". predicted: " + str(prediction) + ", actual: " + str(players) + ", queuesize: " + str(predictionQueue.qsize())
	print "next is gonna be: " + str(futurePrediction)
	resultWriter.writerow([timestamp, prediction, players])
	futureWriter.writerow([timestamp, players])
	if count % 1000 == 0:
		model.save("/home/ec2-user/HTM_sequential_learner/mapleroyals/production_model")
	time.sleep(60)
	count += 1
