import json

# this script is meant to clean the data + make sure that each line has consistent attributes
MAIN_DIR = "data/"

categories = ["business", "review", "tip", "user"]

"""
for item in categories:
    file = item + ".json"

    print("working on ", file)

    # open the input file and read in lines
    f = open(MAIN_DIR + file , "r")
    lines = f.readlines()
    print("there are ", len(lines), item)
"""

num_rest = 0
business_lines = (open(MAIN_DIR+"business.json","r")).readlines()
for item in business_lines:
    l = json.loads(item)
    if l['categories'] is not None:
        if "Restaurants" in l["categories"]:
            num_rest+=1

print("there are", num_rest, "lines")
