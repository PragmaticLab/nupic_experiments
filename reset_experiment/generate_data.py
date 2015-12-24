import csv
import math

ROWS = 300

def run(filename="reset.csv"):
    print "Generating num data into %s" % filename
    fileHandle = open(filename,"w")
    writer = csv.writer(fileHandle)
    writer.writerow(["rr", "num"])
    writer.writerow(["int", "string"])
    writer.writerow(["R", ""])

    count = 0
    while count < ROWS:
        num = count % 10
        rr = 0
        if num == 1 or num == 6:
            rr = 1
        writer.writerow([rr, num])
        count += 1

    fileHandle.close()
    print "Generated %i rows of output data into %s" % (ROWS, filename)

if __name__ == "__main__":
  run()
