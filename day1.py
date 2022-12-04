with open('day1.input') as file:
    inputlist = [i for i in file.read().strip().split("\n")]


max = 0
count = 0
for item in inputlist:
    if item == "":
        count = 0
    else:
        num = int(item)
        count += num

if count > max:
    max = count

print ("D1",max)