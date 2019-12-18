import json
import sys

import numpy as np
from scipy import stats

MAIN_DIR = "data/"

categories = ["business", "review", "user"]

# work on businesses file
attributes = {
"business": {"primary": "business_id", "secondary": ["name", "city", "state", "postal_code", "categories", "stars", "review_count"]},
"review": {"primary": "review_id", "secondary": ["user_id", "business_id", "text", "stars", "useful", "funny", "cool"]},
"user": {"primary": "user_id", "secondary": ["name", "review_count", "yelping_since", "useful", "funny", "elite", "friends", "fans", "average_stars"]}
} 

#business_file = open(MAIN_DIR+"business_matrix.txt", "w")

dict_to_write = {"business": {}, "review": {}, "tip": {}, "user": {}}
for item in categories:
    file = item + ".json"

    print("working on ", file)

    # open the input file and read in lines
    f = open(MAIN_DIR + file , "r")
    lines = f.readlines()

    # figure out which attributes to keep using the attributes dict
    attributes_to_keep = attributes[item]["secondary"]
    pk = attributes[item]["primary"]

    for line in lines:
        # read in as json
        # filter out to get only the attributes we want
        l = json.loads(line)
        dict_to_write[item][l[pk]] = {}
        for atr in attributes_to_keep:
            dict_to_write[item][l[pk]][atr] = l[atr]

list_of_businesses = dict_to_write["business"].keys()
list_of_users = dict_to_write["user"].keys()
list_of_reviews = dict_to_write["review"].keys()


businesses_to_keep = set()

rev_counts = []
# city_to_use = sys.argv[1]
count = 0 
for business_id in list_of_businesses:
    info = dict_to_write["business"][business_id]
    if info["categories"] is not None:
        if info["categories"].find("Restaurants") != -1:
            rev_counts.append(info["review_count"])
            if info["review_count"] > 68:
                businesses_to_keep.add(business_id)
                count+=1

print("number of restaurants is ", count)

#mean value
mean= np.mean(rev_counts)

#median value
median = np.median(rev_counts)

#mode value
mode= stats.mode(rev_counts)

# 90th percentile
perc_90 = np.percentile(rev_counts, 90)

# 75th percentile
perc_75 = np.percentile(rev_counts, 25)

print("Mean review_count: ", mean)
print("Median review_count: ", median)
print("Mode review_count: ", mode)
print("90th percentile is: ", perc_90)
print("75th percentile is: ", perc_75)
