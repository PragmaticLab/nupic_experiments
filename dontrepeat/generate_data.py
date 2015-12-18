import csv
import math
import random

ROWS = 500

my_map = {1: "cat", 0: "dog"}

def run(filename="dontrepeat.csv"):
    print "Generating dontrepeat data into %s" % filename
    fileHandle = open(filename,"w")
    writer = csv.writer(fileHandle)
    writer.writerow(["hand", "lastHand", "status"])
    writer.writerow(["string", "string", "string"])
    writer.writerow(["", "", ""])

    count = 0
    lastHand = "cathy"
    status = "cat"
    while count < ROWS:
        hand = my_map[int(random.random() * 2)]
        writer.writerow([hand, lastHand, status])
        status = "not_same" if hand != lastHand else "same" # this is added in the next round
        lastHand = hand
        count += 1

    fileHandle.close()
    print "Generated %i rows of output data into %s" % (ROWS, filename)

if __name__ == "__main__":
  run()
