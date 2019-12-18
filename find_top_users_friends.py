users = ["PKEzKWv_FktMm2mGPjwd0Q", "bLbSNkLggFnqwNNzzq-Ijw", "U4INQZOPSUaj8hMjLlZ3KA", "tH0uKD-vNwMoEc3Xk3Cbdg","UYcmGbelzRa0Q6JqzLoguw"]
MAIN_DIR = "data/"
data = {}
item = "user"
file = item + ".json"
print("working on ", file)

# open the input file and read in lines
f = open(MAIN_DIR + file , "r")
lines = f.readlines()

# figure out which attributes to keep using the attributes dict
for line in lines:
    # read in as json
    # filter out to get only the attributes we want
    l = json.loads(line)
    if l["user_id"] in users:
        data[l["user_id"]] = l["friends"]

    if len(data.keys())==5:
        break;

f = open(MAIN_DIR+"restaurant_row_labels_matrix.txt")
lines = f.readlines()
users_in_1perc = set()
for line in lines
    users_in_1perc.add(line.replace("\n", "")

# get ratio of ego net in 1%
for user in users:
    data[]
















