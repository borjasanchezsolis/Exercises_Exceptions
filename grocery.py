grocery = {}

while True:

    try:
        item = input()
        # check if item is in the dictionary
    
        if item.upper() in grocery:
            # if it is add 1 in the count
            grocery[item.upper()] += 1
        else:
            # if not, add the time for the 1st time
            grocery[item.upper()] = 1
    except EOFError:
        print()
        break

for item in sorted(grocery.keys()):
    print(grocery[item], item)