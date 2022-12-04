
with open('day1.input') as file:
    data = [i for i in file.read().strip().split("\n")]


elf = 0
elf2 = 0    
elf3 = 0    
count = 0
for food in data:
    if food == '':
        count = 0      
    else:
        num = int(food)
        count += num   
    if count > elf: 
        elf3 = elf2
        elf2 = elf
        elf = count
    elif count > elf2:
        elf3 = elf2
        elf2 = count    # Elf with 2nd most 
    elif count > elf3:
        elf3 = count    # Elf with 3rd most 


# Answers
print("Magic Number for Day 1:", elf)
print("Magic Number for Day 2:", elf+elf2+elf3)