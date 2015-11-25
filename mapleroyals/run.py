import sys
sys.path.append('model_0')
import model_params
from nupic.frameworks.opf.modelfactory import ModelFactory
from scrape_data import getPlayersOnline
import time
import datetime
from Queue import Queue


predictionSteps = 10
model = ModelFactory.create(model_params.MODEL_PARAMS)
model.enableInference({'predictedField': 'players'})

predictionQueue = Queue(maxsize=10)
for i in range(predictionSteps):
	predictionQueue.put(-1)
count = 0
while True:
	players = getPlayersOnline()
	timestamp = datetime.datetime.now()
	print "1"
	result = model.run({
		"timestamp": timestamp,
		"players": players
	})
	print '2'
	predictionQueue.put(result.inferences["multiStepBestPredictions"][10])
	print "3"
	prediction = predictionQueue.get()
	print str(count) + ". predicted: " + str(prediction) + ", actual: " + str(players)

	time.sleep(1)
	count += 1

