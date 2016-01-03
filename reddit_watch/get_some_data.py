import praw
import math
import csv
import datetime
import time


def clean_description(description):
	description = description.replace('\n', ' ')
	return description

def getStatus():
	data = {}
	try:
		r = praw.Reddit(user_agent="faker")
		sub = r.get_subreddit("leagueoflegends")

		data["sub"] = sub.subscribers
		data["online"] = sub.accounts_active
		data["description"] = clean_description(sub.description)

		try:
			hots = sub.get_hot(limit=15)
			votes_list = []
			for i in range(15):
				elem = hots.next()
				votes_list += [elem.score]
			data["max_vote"] = max(votes_list)
			data["min_vote"] = min(votes_list)
			data["avg_vote"] = sum(votes_list) / float(len(votes_list))
		except:
			data["max_vote"] = -1
			data["min_vote"] = -1
			data["avg_vote"] = -1
	except:
		data["sub"] = -1
		data["online"] = -1
		data["description"] = ""
		data["max_vote"] = -1
		data["min_vote"] = -1
		data["avg_vote"] = -1
	return data

if __name__ == "__main__":
	filename = "reddit_lol.csv"
	print "Generating data into %s" % filename
	fileHandle = open(filename, "w", 0)
	writer = csv.writer(fileHandle)
	writer.writerow(["timestamp","sub", "online", "max_vote", "min_vote", "avg_vote"])
	writer.writerow(["datetime","int", "int", "float", "float", "float"])
	writer.writerow(["T", "", "", "", "", ""])
	while True:
		timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		data = getStatus()
		writer.writerow([timestamp, data["sub"], data["online"], data["max_vote"], data["min_vote"], data["avg_vote"]])
		time.sleep(30)
