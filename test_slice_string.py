tester = "1,2,3,0,0,"
print(tester)

should_be = "1,2,3,0,0"

tester = tester[:-1]
if should_be == tester:
    print("YOU GOT IT")