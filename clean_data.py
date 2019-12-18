import json

# this script is meant to clean the data + make sure that each line has consistent attributes
MAIN_DIR = "data/"

categories = ["business", "review", "tip", "user"]

# work on businesses file
attributes = {
"business": [ "business_id", "name", "city", "state", "postal_code", "categories", "stars", "review_count"],
"review": ["review_id", "user_id", "business_id", "text", "stars", "useful", "funny", "cool"],
"tip": ["user_id", "business_id", "text"],
"user": ["user_id", "name", "review_count", "yelping_since", "useful", "funny", "elite", "friends", "fans", "average_stars", "compliment_hot", "compliment_more", "compliment_profile", "compliment_cute", "compliment_list", "compliment_plain", "compliment_note", "compliment_cool", "compliment_funny", "compliment_writer", "compliment_photos"]
} 


for item in categories:
    file = item + ".json"
    outfile = item + "_clean.json"

    print("working on ", file)
    print("cleaned data can be found in ", outfile)

    # open the input file and read in lines
    f = open(MAIN_DIR + file , "r")
    lines = f.readlines()

    # open the output file
    output = open(MAIN_DIR + outfile, "w")

    # figure out which attributes to keep using the attributes dict
    attributes_to_keep = attributes[item]

    # add in the data to the csv, only including the attributes we want to keep
    lineCT = 0 
    dict_to_write = {}
    for item in attributes_to_keep:
        dict_to_write[item] = []

    for line in lines:
        # read in as json
        # filter out to get only the attributes we want
        l = json.loads(line)
        for atr in attributes_to_keep:
            dict_to_write[atr].append(l[atr])

        # write the lie to the output file
        lineCT +=1

    line_to_write = json.dumps(dict_to_write)
    output.write(line_to_write + "\n")
    print("the file has ", lineCT, " lines.")

