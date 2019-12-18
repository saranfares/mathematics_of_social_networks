f = open("data/bipartite_matrix.txt", "r")

file = f.readlines()

print(len(file))
count=0
for line in file:
    print(line[0:50])
    count+=1
    if count > 4:
        break;
