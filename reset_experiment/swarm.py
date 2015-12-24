#!/usr/bin/python
import os
import csv
import pprint

from nupic.frameworks.opf.modelfactory import ModelFactory
from nupic.swarming import permutations_runner

SWARM_CONFIG = {
    "includedFields": [
        {
            "fieldName": "rr",
            "fieldType": "int"
        },
        {
            "fieldName": "num",
            "fieldType": "string"
        }
    ],
    "streamDef": {
        "info": "num",
        "version": 1,
        "streams": [
            {
                "info": "num",
                "source": "file://reset.csv",
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
        "predictedField": "num"
    },
    "iterationCount": -1,
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
    outputLabel='num',
    outDir=permWorkDir,
    permWorkDir=permWorkDir,
    verbosity=1
  )
  modelParamsFile = writeModelParamsToFile(modelParams, 'num')

def run_swarm():
    input_file = "reset.csv"
    model_params = swarm_over_data()

if __name__ == "__main__":
    run_swarm()
