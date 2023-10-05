#count from 1 to 100 with a for loop and range 
# only count the even numbers
# add them all up

#first try!
total = 0
for n in range(2, 101, 2):
    total += n 

print(total)

# alternative solution
total2 = 0 

for i in range(2,101):
    if i  % 2 == 0: # if number in list is divisible by two the add to list
        total2 += i