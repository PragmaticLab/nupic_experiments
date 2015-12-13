import sys
sys.path.append('model_0')
import model_params
from nupic.frameworks.opf.modelfactory import ModelFactory
from Queue import Queue
import csv

SIM_COUNT = 300

predictionSteps = 1
model = ModelFactory.create(model_params.MODEL_PARAMS)
model.enableInference({'predictedField': 'number'})
# load initialization data
f = open("numbers.csv", 'r')
csvReader = csv.reader(f)
csvReader.next()
csvReader.next()
csvReader.next()
count = 0
for row in csvReader:
	if count % 100 == 0:
		print "processed: " + str(count)
	number = int(row[0])
	result = model.run({
		"number": number
	})
	futurePrediction = int(result.inferences["multiStepBestPredictions"][predictionSteps])
	count += 1

resultFile = open("output.txt", 'w', 0)
resultWriter = csv.writer(resultFile)
resultWriter.writerow(["prediction","actual"])
resultWriter.writerow(["int","int"])
resultWriter.writerow(["",""])

predictionQueue = Queue(maxsize=predictionSteps + 2)
for i in range(predictionSteps):
	predictionQueue.put(-1)

count = 0
while count < SIM_COUNT:
	number = count % 10
	result = model.run({"number": number})
	futurePrediction = result.inferences["multiStepBestPredictions"][predictionSteps]
	predictionQueue.put(futurePrediction)
	prediction = predictionQueue.get()
	resultWriter.writerow([prediction, number])
	count += 1
