import urllib2
import csv
import time
import datetime

def getPlayersOnline():
	req = urllib2.Request('http://mapleroyals.com/?page=index')
	response = urllib2.urlopen(req)
	the_page = response.read()
	the_page = the_page[the_page.index("Players Online") + 15:]
	the_page = the_page[:the_page.index("<br />")]
	number = int(the_page)
	return number

if __name__ == "__main__":
	filename = "lagroyals.csv"
	print "Generating lagroyal data into %s" % filename
	fileHandle = open(filename,"w")
	writer = csv.writer(fileHandle)
	writer.writerow(["timestamp","players"])
	writer.writerow(["datetime","int"])
	writer.writerow(["T",""])
	for i in range(20):
		timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		players = getPlayersOnline()
		writer.writerow([timestamp, players])
		time.sleep(60)
		fileHandle.flush()
