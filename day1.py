with open('day1.input') as file:
    inputlist = [i for i in file.read().strip().split("\n")]

elf1 = 0
elf2 = 0
elf3 = 0
count = 0


for food in inputlist:
    if food =='':
        count = 0 #skips to next elf
    else:
            num = int(food)
            count += num

    if count > elf1: 
        elf3 = elf2
        elf2 = elf1
        max = count
    elif count > elf2:
        elf3 = elf2
        elf2 = count    # Elf with second to most 
    elif count > elf3:
        elf3 = count    # Elf with third to most 

print("The Magic Number",elf1)
print("The Magic Number for Day 2",elf1+elf2+elf3)