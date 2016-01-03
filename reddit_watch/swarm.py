#!/usr/bin/python
import os
import csv
import pprint
from nupic.frameworks.opf.modelfactory import ModelFactory
from nupic.swarming import permutations_runner

def modelParamsToString(modelParams):
  pp = pprint.PrettyPrinter(indent=2)
  return pp.pformat(modelParams)

def writeModelParamsToFile(modelParams, name):
  cleanName = name.replace(" ", "_").replace("-", "_")
  paramsName = "%s_model_params.py" % cleanName
  init_f = open('model_params/__init__.py', 'wb')
  init_f.write("\n")
  outDir = os.path.join(os.getcwd(), 'model_params')
  if not os.path.isdir(outDir):
    os.mkdir(outDir)
  outPath = os.path.join(os.getcwd(), 'model_params', paramsName)
  with open(outPath, "wb") as outFile:
    modelParamsString = modelParamsToString(modelParams)
    outFile.write("MODEL_PARAMS = \\\n%s" % modelParamsString)
  return outPath

def swarm_over_data(attr):
  permWorkDir = os.path.abspath('swarm')
  if not os.path.exists(permWorkDir):
    os.mkdir(permWorkDir)
  SWARM_CONFIG = {
    "includedFields": [
    {
      "fieldName": "timestamp",
      "fieldType": "datetime"
    },
    {
      "fieldName": attr['name'],
      "fieldType": attr['type'],
      "maxValue": attr['max'],
      "minValue": attr['min']
    }
    ],
    "streamDef": {
        "info": "lol",
        "version": 1,
        "streams": [
            {
                "info": "reddit_lol",
                "source": "file://reddit_lol.csv",
                "columns": [
                    "*"
                ]
            }
        ]
    },
    "inferenceType": "TemporalAnomaly",
    "inferenceArgs": {
        "predictionSteps": [
            1
        ],
        "predictedField": attr['name']
    },
    "iterationCount": -1,
    "swarmSize": "medium"
  }

  modelParams = permutations_runner.runWithConfig(SWARM_CONFIG,
    {'maxWorkers': 8, 'overwrite': True},
    outputLabel='num',
    outDir=permWorkDir,
    permWorkDir=permWorkDir,
    verbosity=1
  )
  modelParamsFile = writeModelParamsToFile(modelParams, attr['name'])

def run_swarm():
    input_file = "reddit_lol.csv"
    attrs = [{"name": "sub", "type": "int", "max": 850000, "min": 650000},
            {"name": "online", "type": "int", "max": 50000, "min": 5000},
            {"name": "max_vote", "type": "float", "max": 5000, "min": 500},
            {"name": "min_vote", "type": "float", "max": 1500, "min": 0},
            {"name": "avg_vote", "type": "float", "max": 2000, "min": 100}]
    for attr in attrs:
      print "\n\n\n\n\n\nstarting: " + attr['name']
      model_params = swarm_over_data(attr)

if __name__ == "__main__":
    run_swarm()
