import MapReduce
import sys

"""
Create an inverted index- a dictionary where each word is associated with a list of the document identifiers in which that word appears.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(list):
    # key: text in doc
    # value: document identifier 
    key = list[1] #text
    value = list[0] #docid
    words = key.split()
    for w in words:
		mr.emit_intermediate(w, value)

def reducer(key, list_of_values):
    # key: text
    # value: docid
  
	# remove duplicates
	newlist = list(set(list_of_values))
	mr.emit((key, newlist))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
