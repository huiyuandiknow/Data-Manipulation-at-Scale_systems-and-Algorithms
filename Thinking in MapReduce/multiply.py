import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def calculate(row, col, value):
    listAB = (row, col)
    mr.emit_intermediate(listAB,value)

def mapper(record):

    global temprow, tempcol
    # key: index
    # value: value in matrix
    matrixName = record[0]
    row = record[1]
    col = record[2]
    value = record[3]
   
    # assign temp row and col
    if matrixName == "a" and row == 0 and col ==0:
	temprow = row
	tempcol = col
    

    while col-tempcol > 1 or (row > temprow and tempcol <4) or (tempcol !=4 and row == 0 and col == 0 and matrixName == "b"):
        tempcol += 1
        for i in range(0,5):
            if matrixName == "a" or matrixName == "b" and col==0 and tempcol==4:
                calculate(temprow, i,0)
            else:
                calculate(i,tempcol,0)

	# update if reaches the end of cool 
        # and if current col isn't 0
	if tempcol == 4 and col != 0: 
	    temprow = row+1
	    tempcol = -1
    # if it's Matrix A, do this
    if matrixName == "a":
    	for k in range(0,5):
	    calculate(row, k, value)
    # if it's Matrix B, do this
    else:  
   	for i in range(0,5):
	    calculate(i,col, value) 
 
    tempcol = col
    temprow = row 

def reducer(key, list_of_values):
    
   # key: word
    # value: list of occurrence counts
   sum = 0
   for i in range(len(list_of_values)/2):
	sum += list_of_values[i]*list_of_values[i+5]

   mr.emit((key+(sum,)))
   #   total += v
   # mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
