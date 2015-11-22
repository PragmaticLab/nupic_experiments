#!/usr/bin/python

import csv
from nupic.frameworks.opf.modelfactory import ModelFactory
from nupic_output import NuPICFileOutput, NuPICPlotOutput
from nupic.swarming import permutations_runner
import generate_data

PLOT = True
SWARM_CONFIG = {
  "includedFields": [
    {
      "fieldName": "tan",
      "fieldType": "float",
      "maxValue": 10.0,
      "minValue": -10.0
    }
  ],
  "streamDef": {
    "info": "tan",
    "version": 1,
    "streams": [
      {
        "info": "tan.csv",
        "source": "file://tan.csv",
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
    "predictedField": "tan"
  },
  "swarmSize": "medium"
}

def swarm_over_data():
  return permutations_runner.runWithConfig(SWARM_CONFIG,
    {'maxWorkers': 8, 'overwrite': True})

def run_tan_experiment():
  input_file = "tan.csv"
  generate_data.run(input_file)
  model_params = swarm_over_data()
  if PLOT:
    output = NuPICPlotOutput("tan_output", show_anomaly_score=True)
  else:
    output = NuPICFileOutput("tan_output", show_anomaly_score=True)
  model = ModelFactory.create(model_params)
  model.enableInference({"predictedField": "tan"})

  with open(input_file, "rb") as tan_input:
    csv_reader = csv.reader(tan_input)

    csv_reader.next()
    csv_reader.next()
    csv_reader.next()

    for row in csv_reader:
      angle = float(row[0])
      tan_value = float(row[1])
      result = model.run({"tan": tan_value})
      output.write(angle, tan_value, result, prediction_step=1)

  output.close()

if __name__ == "__main__":
  run_tan_experiment()
