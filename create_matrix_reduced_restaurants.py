import json
import sys

import numpy as np

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
cutoff = int(sys.argv[1])
for business_id in list_of_businesses:
    info = dict_to_write["business"][business_id]
    if info["categories"] is not None:
        if info["categories"].find("Restaurants") != -1:
            rev_counts.append(info["review_count"])
            if info["review_count"] > cutoff:
                businesses_to_keep.add(business_id)

print("mean review_count is :", np.mean(rev_counts))
print("cutoff review_count is :", cutoff)

output_file = open(MAIN_DIR+"restaurant"+"_matrix.csv", "w")
output_file_header_rows = open(MAIN_DIR+"restaurant"+"_row_labels_matrix.txt", "w")
output_file_header_cols = open(MAIN_DIR+"restaurant"+"_col_labels_matrix.txt", "w")

users_and_their_businesses = {}
users_to_keep = set()
rev_count_cutoff = int(sys.argv[2])
for review_id in list_of_reviews:
    info = dict_to_write["review"][review_id]
    user_review_count = dict_to_write["user"][info["user_id"]]["review_count"]
    if info["business_id"] in businesses_to_keep:
        # keep this review...
        if user_review_count> rev_count_cutoff:
            if info["user_id"] not in users_to_keep:
                users_to_keep.add(info["user_id"])
                users_and_their_businesses[info["user_id"]] = []
            users_and_their_businesses[info["user_id"]].append(info["business_id"])

# write the businesses as the header
bus_dict = {}
bus_list = []
count=0
for item in businesses_to_keep:
    bus_dict[item] = count
    bus_list.append(item)
    output_file_header_cols.write(item + "\n")
    count+=1

num_businesses = len(bus_list)
print("number of businesses kept: ", num_businesses)
# now iterate through all the users we kept and check which businesses we need to write for them each 
print("number of users in matrix: ", len(users_to_keep))
for user in users_to_keep:
    zeroes_list = np.zeros(num_businesses)
    line = ""
    output_file_header_rows.write(user + "\n")
    for business in users_and_their_businesses[user]:
        idx = bus_dict[business]
        zeroes_list[idx] = 1

    for item in zeroes_list:
        if item == 0:
            line+= ("0,")
        else:
            line+= ("1,")
    count+=1
    output_file.write(line[:-1] + '\n')




