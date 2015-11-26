import sys
sys.path.append('model_0')
import model_params
from nupic.frameworks.opf.modelfactory import ModelFactory
from scrape_data import getPlayersOnline
import time
import datetime
from Queue import Queue
import csv


predictionSteps = 5
# load prev model
if len(sys.argv) >= 2 and sys.argv[1] != "None":
	print "loading old model"
	model = ModelFactory.loadFromCheckpoint(sys.argv[1])
else:
	model = ModelFactory.create(model_params.MODEL_PARAMS)
	model.enableInference({'predictedField': 'players'})
# load initialization data
if len(sys.argv) >= 3 and sys.argv[2] != "None":
	print "initializing model with data"
	f = open(sys.argv[2], 'r')
	csvReader = csv.reader(f)
	# skip header rows
	csvReader.next()
	csvReader.next()
	csvReader.next()
	for row in csvReader:
		timestamp = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
		players = row[1]
		result = model.run({
			"timestamp": timestamp,
			"players": players
		})


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
	futurePrediction = int(result.inferences["multiStepBestPredictions"][5])
	predictionQueue.put(futurePrediction)
	prediction = predictionQueue.get()
	print str(timestamp) + ". predicted: " + str(prediction) + ", actual: " + str(players)
	print "next is gonna be: " + str(futurePrediction)
	resultWriter.writerow([timestamp, prediction, players])
	futureWriter.writerow([timestamp, players])
	if count % 1000 == 0:
		model.save("/home/ec2-user/HTM_sequential_learner/mapleroyals/production_model")
	time.sleep(60)
	count += 1
