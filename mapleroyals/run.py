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
	timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	result = model.run({
		"timestamp": timestamp,
		"players": players
    })
	predictionQueue.put(result.inferences["multiStepBestPredictions"][10])
	prediciton = predictionQueue.get()
	print str(count) + ". predicted: " + str(prediciton) + ", actual: " + str(result) 

	time.sleep(1)
	count += 1

