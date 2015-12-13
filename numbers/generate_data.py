import csv
import math

ROWS = 1000

def run(filename="numbers.csv"):
    print "Generating tan data into %s" % filename
    fileHandle = open(filename,"w")
    writer = csv.writer(fileHandle)
    writer.writerow(["number"])
    writer.writerow(["float"])
    writer.writerow([""])

    count = 0
    while count < ROWS:
        writer.writerow([count % 10])
        count += 1

    fileHandle.close()
    print "Generated %i rows of output data into %s" % (ROWS, filename)

if __name__ == "__main__":
  run()
