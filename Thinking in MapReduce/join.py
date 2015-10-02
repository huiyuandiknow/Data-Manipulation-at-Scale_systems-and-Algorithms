import MapReduce
import sys
from collections import defaultdict

"""
Word Count Example in the Simple Python MapReduce Framewok
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    # key: identifier- either "line_item" or "order"
    # value: rest of the fields
    
    identifier = record[0]
    orderid = record[1]
    combined = ""
    
    global count, previousid

    if identifier == "line_item":
	if previousid != orderid:
	    count = 1
	combined = int(orderid)*100+1+count
	count += 1
    else:
	count = 1
	combined = int(orderid)*100+1
    previousid = orderid
    
    mr.emit_intermediate(combined, record)    

def reducer(combined, list_of_values):
  
    thisOrderId = combined/100
    
    # determine whether it's order or line item
    if combined % 100 == 1:
	Type = 0
    else:
	Type = 1
    
    if Type == 0:
        global orderlist, previousOrderId
	orderlist = list() 
	for i in list_of_values:
	    orderlist.append(i)
	previousOrderId = thisOrderId

    elif Type == 1 and previousOrderId == thisOrderId:
	itemlist =list()
        for i in list_of_values:
	    itemlist.append(i)

	mr.emit((orderlist[0]+itemlist[0]))	

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
