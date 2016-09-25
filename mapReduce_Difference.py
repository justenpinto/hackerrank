# Enter your code here. Read input from STDIN. Print output to STDOUT
# This template is based on the framework supplied for a similar challenge, in a Coursera Data Science course: https://www.coursera.org/course/datasci
# And the code supplied here: https://github.com/uwescience/datasci_course_materials/blob/master/assignment3/wordcount.py
# The map-reduce emulator is provided
# You need to fill out the mapper and reducer functions

import json
import sys
from collections import OrderedDict
class MapReduce:
    def __init__(self):
        self.intermediate = OrderedDict()
        self.result = []

    def emitIntermediate(self, key, value):
        self.intermediate.setdefault(key, [])
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value) 

    def execute(self, data, mapper, reducer):
        for line in data:
            record = json.loads(line)
            mapper(record)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])

        for item in self.result:
            print item

mapReducer = MapReduce()
R = 0
S = 0

def mapper(record):
    global R
    global S
    key = record["key"]
    value = record["value"]
    if key == 1:
        R, S = [int(i) for i in value.split(' ')]
    else:
        if int(key) < R + 2:
            mapReducer.emitIntermediate(int(value), "R")
        else:
            mapReducer.emitIntermediate(int(value), "S")

def reducer(key, list_of_values):
    if "R" in list_of_values and "S" not in list_of_values:
        mapReducer.emit(key)
        return

if __name__ == '__main__':
  inputData = []
  counter = 0
  for line in sys.stdin:
   counter += 1
   inputData.append(json.dumps({"key":counter,"value":line}))
  mapReducer.execute(inputData, mapper, reducer)

