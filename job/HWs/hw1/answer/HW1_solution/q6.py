''' This program generates the 1-random.txt file  with this format: "Line 000000 RandNum"
    until "Line 999999 RandNum" using csv and witout it and calculates the 
    execution time.'''
from time import process_time
import os
import csv
import numpy as np

filename = "1-random-normal.txt"
path = os.path.join(os.getcwd(), filename)

print("Generating file in normal way ...")
start = process_time()
start1 = time.time()
with open(path, 'w') as f:
    for lineNum in range(1000000):
        f.write("Line {:0>6}\t{:6f}\n".format(lineNum, 
       	                                  np.random.random()))
end = time.time()
end1 = end -start1;
exec_normal = process_time() - start;
print("Took: {:.2f} s".format(exec_normal))

filename = "1-random-csv.txt"
path = os.path.join(os.getcwd(), filename)
print("Generating file using csv ...")
start = process_time()
with open(filename, 'w') as f:
    csv_handle = csv.writer(f)
    for lineNum in range(1000000):
        csv_handle.writerow(["Line", "{:0>6}".format(lineNum), 
                            np.random.random()])
exec_csv = process_time() - start
print("Took: {:.2f} s".format(exec_csv))


filename = "1-random-normal-fast.txt"
path = os.path.join(os.getcwd(), filename)
print("Generating file in normal way but faster ...")
# First generate the data then write it to file
start = process_time()
with open(path, 'w') as f:
    f.writelines(["Line {:0>6}\t{:6f}\n".format(lineNum, np.random.random())
                  for lineNum in range(1000000)])
exec_fast = process_time() - start
print("Took: {:.2f} s".format(exec_fast))