import random

# rand = random.rand()
rand = random.randint(1,100)
# print(rand)

guess_count  = 0

low = 1
high = 100

print("\t\t\t\t\tW E L C O M E \nINSTRUCTIONS :- You have to guess the number in between 10 guesses otherwise you will lose ")

while guess_count<=9:

  # user_guess = int(input(f"Guess a number between {low} and {high}: "))
  # guess_count += 1 
  try:
    user_guess = int(input(f"\nGuess a number between {low} and {high}: "))
    
    if user_guess > high or user_guess < low:
      print(f"\nPlease enter a number between {low} and {high}")
      continue

    guess_count += 1 
  
  except ValueError:
    
    print("Please enter a number ! ! ! ")
    continue

  if user_guess == rand:
      
      print(f"\nYou got it! The number is {rand}.\nYou took {guess_count} guesses.")
      break

  elif user_guess > rand:
      
      high = user_guess
      print(f"\n\t\t\t\t\t\tToo high!\nRemaining guesses : -  {10 - guess_count}")
      

  else:
      low = user_guess
      print(f"\n\t\t\t\t\t\tToo low!\nRemaining guesses : -  {10 - guess_count}")
      

if guess_count >= 10:
  print("\t\t\t\t\t\tY O U   L O S E")
else:
  print("\t\t\t\t\t\tY O U   W I N")
# print("\n\n! ! ! E N D  ! ! !")