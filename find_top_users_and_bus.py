import json

# this script is meant to clean the data + make sure that each line has consistent attributes
MAIN_DIR = "data/"
categories = ["review", "user", "business"]

users = ["U4INQZOPSUaj8hMjLlZ3KA",
            "PKEzKWv_FktMm2mGPjwd0Q",
            "d_TBs6J3twMy9GChqUEXkg",
            "bLbSNkLggFnqwNNzzq-Ijw",
            "cMEtAiW60I5wE_vLfTxoJQ",
            "YMgZqBUAddmFErxLtCfK_w",
            "kmE8w5Y785eZmodsx0V6Ag",
            "tH0uKD-vNwMoEc3Xk3Cbdg"]

businesses = ["X4JNXUYY8wbaaDmk3BPzlWw",
                "iCQpiavjjPzJ5_3gPD5Ebg",
                "K7lWdNUhCbcnEvI0NhGewg",
                "RESDUcs7fIiihp38.d6_6g",
                "DkYS3arLOhA8si5uUEmHOw",
                "P7pxQFqr7yBKMMI2J51udw",
                "cYwJA2A6I12KNkm2rtXd5g"]

data = {}
# work on businesses file
attributes = {
"business": {"primary": "business_id", "secondary": ["name", "city", "state", "postal_code", "categories", "stars", "review_count"]},
"review": {"primary": "review_id", "secondary": ["user_id", "business_id", "text", "stars", "useful", "funny", "cool"]},
"user": {"primary": "user_id", "secondary": ["name", "review_count", "yelping_since", "useful", "funny", "elite", "friends", "fans", "average_stars"]}
} 

data = {"business": {}, "review": {}, "user": {}}
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
        data[item][l[pk]] = {}
        for atr in attributes_to_keep:
            data[item][l[pk]][atr] = l[atr]

for business in businesses:
    print("stats for ", business)
    print("stars: ", data["business"][business]["stars"])
    print("city", data["business"][business]["city"])
    print("review count:", data["business"][business]["review_count"])
for user in users:
    print("stats for ", user)
    print("average stars: ", data["user"][user]["average_stars"])
    print("review count: ", data["user"][user]["review_count"])
    print("fans: ", data["user"][user]["fans"])


