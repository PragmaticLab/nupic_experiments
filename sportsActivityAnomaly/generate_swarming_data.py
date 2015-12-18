from dataapi import getDataSteam
import csv

def run(filename="exercise.csv"):
    print "Generating exercise data into %s" % filename
    fileHandle = open(filename,"w")
    writer = csv.writer(fileHandle)
    
    writer.writerow(["torso"])
    writer.writerow(["float"])
    writer.writerow([""])

    lines = getDataSteam(10, 5)
    for line in lines:
        writer.writerow(line)
    lines = getDataSteam(3, 2)
    for line in lines:
        writer.writerow(line)
    
    fileHandle.close()

if __name__ == "__main__":
  run()
