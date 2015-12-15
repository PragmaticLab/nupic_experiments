#!/usr/bin/python
import os
import csv
import pprint

from nupic.frameworks.opf.modelfactory import ModelFactory
from nupic.swarming import permutations_runner

SWARM_CONFIG = {
    "includedFields": [
        {
            "fieldName": "player1",
            "fieldType": "string"
        },
        {
            "fieldName": "player2",
            "fieldType": "string"
        },
        {
            "fieldName": "winner",
            "fieldType": "string"
        }
    ],
    "streamDef": {
        "info": "rps",
        "version": 1,
        "streams": [
            {
                "info": "rps",
                "source": "file://rps.csv",
                "columns": [
                    "*"
                ]
            }
        ]
    },
    "inferenceType": "TemporalMultiStep",
    "inferenceArgs": {
        "predictionSteps": [
            1
        ],
        "predictedField": "winner"
    },
    "iterationCount": 3000,
    "swarmSize": "medium"
}

def modelParamsToString(modelParams):
  pp = pprint.PrettyPrinter(indent=2)
  return pp.pformat(modelParams)

def writeModelParamsToFile(modelParams, name):
  cleanName = name.replace(" ", "_").replace("-", "_")
  paramsName = "%s_model_params.py" % cleanName
  outDir = os.path.join(os.getcwd(), 'model_params')
  if not os.path.isdir(outDir):
    os.mkdir(outDir)
  outPath = os.path.join(os.getcwd(), 'model_params', paramsName)
  with open(outPath, "wb") as outFile:
    modelParamsString = modelParamsToString(modelParams)
    outFile.write("MODEL_PARAMS = \\\n%s" % modelParamsString)
  return outPath

def swarm_over_data():
  permWorkDir = os.path.abspath('swarm')
  if not os.path.exists(permWorkDir):
    os.mkdir(permWorkDir)
  modelParams = permutations_runner.runWithConfig(SWARM_CONFIG,
    {'maxWorkers': 8, 'overwrite': True},
    outputLabel='rps',
    outDir=permWorkDir,
    permWorkDir=permWorkDir,
    verbosity=1
  )
  modelParamsFile = writeModelParamsToFile(modelParams, 'rps')

def run_swarm():
    input_file = "rps.csv"
    model_params = swarm_over_data()

if __name__ == "__main__":
    run_swarm()
