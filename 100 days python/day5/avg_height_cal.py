# need to find the average height from user input
# cannot use len() or Sum()
# have to use for loop
# the result has to be rounded

heights = input("Please input the heights you need averaged rounded to the nearest integer:").split()
for i in range(0, len(heights)):
    heights[i]= int(heights[i])

print(heights)
# manually making sum() function
total_height = 0
for height in heights:
    total_height += height
print(total_height)

#manually building counter/ len()
counter = 0
for n in heights:
    counter += 1
print(counter)

avg_height = round(total_height/counter)
print(avg_height)