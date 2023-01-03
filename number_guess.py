import random as r

random_number = r.randrange(1,100) 

counts = 1
while(counts<=10):
  print(f'YOU HAVE {10-counts} CHANCES LEFT')
  guess_number = int(input('Guess the Number : '))

  if(random_number == guess_number):
    print('You Won')
    break
  elif(random_number > guess_number):
    print('Hint : Choose a Higher Number')
  else:
    print('Hint : Choose a Lower Number')
  counts = counts + 1
else:
  print('Oops!! You lost , ran out of your chances.')