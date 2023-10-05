# making use of the rondomization module in python
# python uses the Mersenne Tister a psydo random number generator (Khan academy)

import random
import module

random_int = random.randint(1,10)
print(random_int)

print(module.pi)

#random.random() is anything between 0.00000 to 0.999999 ...
#when you multiply it by 5 it expands the range to be from zero to 4.99999 
#you would get 0.1 then multiply by 5 to get 0.5 and 0.3 * 5 to get 1.5 and so on
random_float = random.random()*5
print(random_float)


#making heads or tails
random_coin = random.randint(1,2)
print(random_coin)
if random_coin == 1:
    print('heads')
elif random_coin == 2:
    print('tails')

#Banker roulette
names_list = input("what are your names? please type it separated by a comma, pretty please!")
names_list = names_list.split(',')
print(names_list)
loser = random.choice(names_list)
print(loser)

#rock paper scissors
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
     
dirty_dozen = [fruits, vegetables]
     
print(dirty_dozen[1][1])