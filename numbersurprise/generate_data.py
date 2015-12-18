import csv
import math
import random

ROWS = 1000

def run(filename="num.csv"):
    print "Generating num data into %s" % filename
    fileHandle = open(filename,"w")
    writer = csv.writer(fileHandle)
    writer.writerow(["num"])
    writer.writerow(["string"])
    writer.writerow([""])

    count = 0
    while count < ROWS:
        num = "shh" if random.random() > 0.99 else "BOOH"
        writer.writerow([num])
        count += 1

    fileHandle.close()
    print "Generated %i rows of output data into %s" % (ROWS, filename)

if __name__ == "__main__":
  run()
