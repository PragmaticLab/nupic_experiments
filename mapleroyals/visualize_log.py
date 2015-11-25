import matplotlib.pyplot as plt
from collections import deque
import sys
import csv
import time

WINDOW = 100
plt.ion()
fig = plt.figure()
plt.title('MapleLagyals Online Player Prediction')
plt.xlabel('time [s]')
plt.ylabel('Players [%]')

actHistory = deque([0.0] * WINDOW, maxlen=100)
predHistory = deque([0.0] * WINDOW, maxlen=100)
r = range(WINDOW)
actline, = plt.plot(r, actHistory)
predline, = plt.plot(r, predHistory)
actline.axes.set_ylim(0, 1000)
predline.axes.set_ylim(0, 1000)

f = open(sys.argv[1], 'r')
csvReader = csv.reader(f)
# skip header rows
csvReader.next()
csvReader.next()
csvReader.next()

for row in csvReader:
	predicted = row[1]
	actual = row[2]
	actHistory.append(actual)
	predHistory.append(predicted)
	actline.set_ydata(actHistory)
	predline.set_ydata(predHistory)
	plt.draw()
	plt.legend( ('actual','predicted') )  
	time.sleep(float(sys.argv[2]))

s = raw_input('---LAG ON---')


