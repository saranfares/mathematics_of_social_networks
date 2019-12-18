# this script is just intended to read the first line of each file and see what the data looks like...
MAIN_DIR = "data/"
files = ["business.json", "review.json", "tip.json", "user.json"]
for file in files:
    print("file name: ", file)
    f = open(MAIN_DIR + file , "r")
    lines = f.readlines()
    print(lines[0])
    print("\n")
