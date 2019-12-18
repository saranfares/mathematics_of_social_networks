# ONLY KEEP USERS who have done at least 20 reviews
import json

import numpy as np

MAIN_DIR = "data/"

categories = ["business", "review", "tip", "user"]

# work on businesses file
attributes = {
"business": [ "business_id", "name", "city", "state", "postal_code", "categories", "stars", "review_count"],
"review": ["review_id", "user_id", "business_id", "text", "stars", "useful", "funny", "cool"],
"tip": ["user_id", "business_id", "text"],
"user": ["user_id", "name", "review_count", "yelping_since", "useful", "funny", "elite", "friends", "fans", "average_stars", "compliment_hot", "compliment_more", "compliment_profile", "compliment_cute", "compliment_list", "compliment_plain", "compliment_note", "compliment_cool", "compliment_funny", "compliment_writer", "compliment_photos"]
} 

users_file = open(MAIN_DIR+"user_header.txt", "w")
business_file = open(MAIN_DIR+"bipartite_matrix.txt", "w")
#business_file = open(MAIN_DIR+"business_matrix.txt", "w")

dict_to_write = {"business": {}, "review": {}, "tip": {}, "user": {}}
for item in categories:
    file = item + ".json"

    print("working on ", file)

    # open the input file and read in lines
    f = open(MAIN_DIR + file , "r")
    lines = f.readlines()

    # figure out which attributes to keep using the attributes dict
    attributes_to_keep = attributes[item]

    for attr in attributes_to_keep:
        dict_to_write[item][attr] = []

    for line in lines:
        # read in as json
        # filter out to get only the attributes we want
        l = json.loads(line)
        for atr in attributes_to_keep:
            dict_to_write[item][atr].append(l[atr])

users_list = []
for idx in range(0,len(dict_to_write["user"]["review_count"])):
    if dict_to_write["user"]["review_count"][idx] >=20:
        users_list.append(dict_to_write["user"]["user_id"][idx]) 

num_users = len(users_list)


businesses_list = {}
businesses_dict = {}
count=0
for idx in range(0, len(dict_to_write["review"]["business_id"])):
    business_id = dict_to_write["review"]["business_id"][idx]
    user_id = dict_to_write["review"]["user_id"][idx]
    if business_id not in businesses_list:
        businesses_list[business_id] = count
        count+=1
    if user_id not in businesses_dict.keys():
        businesses_dict[user_id] = []
    else:
        businesses_dict[user_id].append(business_id)

user_indices = {}
count=0
line=""
for user in users_list:
    line += (user+",")
    user_indices[user] = count
    count+=1

users_file.write(line[:-1])

business_list_line = ""
for business in businesses_list.keys():
    business_list_line += (business + ",")
business_file.write(business_list_line[:-1])

num_businesses = len(businesses_list.keys())

# find connections between users (check if they are friends)
count=0
print("len of users ", len(users_list))
for user in users_list:
    zeroes_list = np.zeros(num_businesses)
    line = ""
    if user in businesses_dict.keys():
        for business in businesses_dict[user]:
            idx = businesses_list[business]
            zeroes_list[idx] = 1
    for item in zeroes_list:
        if item == 0:
            line+= ("0,")
        else:
            line+= ("1,")
    print(count)
    count+=1
    business_file.write(user+","+line[:-1])



