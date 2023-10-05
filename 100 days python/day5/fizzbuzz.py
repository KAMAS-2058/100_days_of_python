## interveiw question 
# very common interview question

for n in range(1,101):
    if n %3 == 0 and n %5 == 0:
        print("FizzBuzz")
    elif n %3 == 0:
        print("fizz")
    elif n %5 == 0:
        print("buzz")
    else:
        print(n)        

for number in range(1,101):
  if number%3==0 and number%5==0:
    print('FizzBuzz')
  elif number %3==0:
    print('Fizz')
  elif number%5==0:
    print('Buzz')
  else:
    print(number)