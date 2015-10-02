import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, value)
    mr.emit_intermediate(value, "-"+key)

def reducer(key, value):
        
    newlist = list()
    for v in value: 
	if v[0] == "-":
	    temp = v[1:]
	    v = temp
	if v not in newlist: 
	    newlist.append(v)
	else: 
	    newlist.remove(v)

    for i in newlist: 
	mr.emit((key, i))
	
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
