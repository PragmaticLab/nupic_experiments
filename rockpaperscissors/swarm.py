#!/usr/bin/python
import csv
from nupic.frameworks.opf.modelfactory import ModelFactory
from nupic.swarming import permutations_runner

SWARM_CONFIG = {
    "includedFields": [
        {
            "fieldName": "player1",
            "fieldType": "int",
            "maxValue": 2,
            "minValue": 0
        },
        {
            "fieldName": "player2",
            "fieldType": "int",
            "maxValue": 2,
            "minValue": 0
        },
        {
            "fieldName": "scoreBeforeDuel",
            "fieldType": "int",
            "maxValue": 5,
            "minValue": -5
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
        "predictedField": "scoreBeforeDuel"
    },
    "iterationCount": -1,
    "swarmSize": "small"
}


def swarm_over_data():
  return permutations_runner.runWithConfig(SWARM_CONFIG,
    {'maxWorkers': 8, 'overwrite': True})

def run_swarm():
    input_file = "rps.csv"
    model_params = swarm_over_data()

if __name__ == "__main__":
    run_swarm()
