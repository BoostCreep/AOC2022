with open('day1.input') as file:
    inputlist = [i for i in file.read().strip().split("\n")]

elf1 = 0
elf2 = 0
elf3 = 0
elf4 = 0
count = 0


for food in inputlist:
    if food =='':
        count = 0 #skips to next elf
    else:
            num = int(food)
            count += num

