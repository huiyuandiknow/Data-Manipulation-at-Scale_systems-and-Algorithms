import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: sequence id
    # value: string of nucleotides
    key = record[0]
    value= record[1]
    nucleotides = value[:-10]   
    mr.emit_intermediate(1, nucleotides)

def reducer(key, list_of_values):
    # key: sequence id
    # value: list of strings of nucleotides
    newlist=list(set(list_of_values))
    for i in newlist: 
        mr.emit((i))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
