import os
import csv
import numpy as np

path = os.path.join('Resources', 'election_data.csv')

total_lines = []
candidates = []
cand_list = []


with open(path) as file:
    next(file, None)
    
    for line in file:
        
        total_lines.append(line)
        total_votes = len(total_lines)

        x = line.rsplit(",")

        name = x[2][:-1]
        candidates.append(name)

    for name in candidates:
        if name not in cand_list:
            cand_list.append(name)
        
    

        
            
            
        


        #if next(file)[2] != file[2]:
        #    candidates.append(line)

print("----------------")
print("Election Results")
print("----------------")
print(f" Total Votes: {total_votes}")

print(cand_list)

print("----------------")




