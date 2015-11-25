#!/usr/bin/python
import csv
from nupic.frameworks.opf.modelfactory import ModelFactory
from nupic.swarming import permutations_runner

SWARM_CONFIG = {
  "includedFields": [
    {
      "fieldName": "timestamp",
      "fieldType": "datetime"
    },
    {
      "fieldName": "players",
      "fieldType": "int",
      "maxValue": 1000,
      "minValue": 0
    }
  ],
  "streamDef": {
    "info": "players",
    "version": 1,
    "streams": [
      {
        "info": "lagroyals",
        "source": "file://lagroyals.csv",
        "columns": [
          "*"
        ]
      }
    ]
  },
  "inferenceType": "TemporalMultiStep",
  "inferenceArgs": {
    "predictionSteps": [
      10
    ],
    "predictedField": "players"
  },
  "iterationCount": -1,
  "swarmSize": "medium"
}


def swarm_over_data():
  return permutations_runner.runWithConfig(SWARM_CONFIG,
    {'maxWorkers': 8, 'overwrite': True})

def run_swarm():
  input_file = "lagroyals.csv"
  model_params = swarm_over_data()

if __name__ == "__main__":
  run_swarm()
