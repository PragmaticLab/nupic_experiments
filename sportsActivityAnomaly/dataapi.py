import csv

def getDataSteam(activity, person):
	data = []
	for i in range(1, 61):
		fileName = 'data/a%02d/p%d/s%02d.txt' % (activity, person, i)
		csvReader = csv.reader(open(fileName))
		for row in csvReader:
			data += [[float(row[0])]]
	return data


if __name__ == "__main__":
	print getDataSteam(1, 1)
	print getDataSteam(1, 1)[0]
