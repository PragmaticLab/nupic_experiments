#!/usr/bin/python
import csv
from nupic.frameworks.opf.modelfactory import ModelFactory
from nupic.swarming import permutations_runner

SWARM_CONFIG = {
    "includedFields": [
        {
            "fieldName": "number",
            "fieldType": "int",
            "maxValue": 10,
            "minValue": 0
        }
    ],
    "streamDef": {
        "info": "numbers",
        "version": 1,
        "streams": [
            {
                "info": "numbers",
                "source": "file://numbers.csv",
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
        "predictedField": "number"
    },
    "iterationCount": -1,
    "swarmSize": "medium"
}


def swarm_over_data():
  return permutations_runner.runWithConfig(SWARM_CONFIG,
    {'maxWorkers': 8, 'overwrite': True})

def run_swarm():
    input_file = "numbers.csv"
    model_params = swarm_over_data()

if __name__ == "__main__":
    run_swarm()
