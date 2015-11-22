#!/usr/bin/env python

import csv
import math

ROWS = 3000


def run(filename="tan.csv"):
  print "Generating tan data into %s" % filename
  fileHandle = open(filename,"w")
  writer = csv.writer(fileHandle)
  writer.writerow(["angle","tan"])
  writer.writerow(["float","float"])
  writer.writerow(["",""])

  for i in range(ROWS):
    angle = (i * math.pi) / 50.0
    tan_value = math.tan(angle)
    writer.writerow([angle, tan_value])

  fileHandle.close()
  print "Generated %i rows of output data into %s" % (ROWS, filename)



if __name__ == "__main__":
  run()
