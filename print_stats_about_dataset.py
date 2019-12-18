import json

import numpy as np
from scipy import stats

files = ["data/user_clean.json", "data/business_clean.json"]
attributes = [
["review_count", "useful", "funny", "fans", "average_stars", "compliment_hot", "compliment_more", "compliment_profile", "compliment_cute", "compliment_list", "compliment_plain", "compliment_note", "compliment_cool", "compliment_funny", "compliment_writer", "compliment_photos"],
["stars", "review_count"]] 
output_file = ["data/user_stats.csv","data/business_stats.csv"]

count=0
for file in files:
    attributes_to_keep = attributes[count]
    output = open(output_file[count], "w")
    # open the input file and read in lines
    f = open(file, "r")
    lines = f.readlines()

    dataset = {}
    for attr in attributes_to_keep:
        dataset[attr] = []

    for line in lines:
        l = json.loads(line)
        for attr in attributes_to_keep:
            dataset[attr].append(l[attr])

    output_lines = ["", "", ""]
    for attr in attributes_to_keep:
        col = dataset[attr]
        print("ATTRIBUTE: ", attr)
        mean= np.mean(col)
        median = np.median(col)
        print("Mean: ", mean)
        print("Median: ", median)
        output_lines[0] += (attr+",")
        output_lines[1] += (str(mean)+",")
        output_lines[2] += (str(median)+",")

    for output_line in output_lines:
        output.write(output_line[:-1]+"\n")
    count +=1

