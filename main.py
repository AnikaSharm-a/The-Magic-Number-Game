###################################
# Title: The Magic Number Game
# Date: 23/9/2021
# Programmer: Anika Sharma
# Purpose: To create a fun and interactive guessing game for the user.
###################################

# Imports
from time import sleep
from random import randint

# Greeting the user 
name = input("Hello! What is your name?: ")
print("\nGreetings", name +"! You're in for a fun time The Magic Number Game. How exciting! \n\n")
sleep(1)

# Introducing the game
print("#"* 30, "\n\tTHE MAGIC NUMBER GAME","\n"+"#"* 30)

print("\nWelcome to the Magic Number Game. Put your guessing skills to the test with this very well known and enjoyed by everyone game.")
sleep(2)

# Printing the rules of this game
print("\nRULES OF THIS GAME: \n1. You have 5 guesses to guess my magic number. \n2. This number will be any integer between a range that you get to choose! \n3. Since this game can sometimes get a bit difficult, I will tell you if your guess is greater or smaller than my number. You're welcome. \n4. Have fun!")
print("-"*30)
sleep(2)



# Telling the user about the cost of playing
print("\n\nTo play this game, you must pay. Each play costs $0.75 without tax. (Our tax value is 10%). Plays must be a whole number greater than 0.\n")

# Asking for the number of times they want to play
num_plays = int(input("How many plays would you like to purchase?: "))

# Making sure that the number they enter is valid
while num_plays <= 0:
  num_plays = int(input("\nInvalid input. Please enter again: "))

# Calculating and printing their cost with tax
initial_cost = num_plays*0.75
final_cost = initial_cost * 1.10

print("\nYOUR COSTS FOR", num_plays, "PLAY(S):","\n"+"-"*30)
print("Your initial cost is: $"+ str(round(initial_cost,2)))
print("Your final cost with tax is: $"+ str(round(final_cost,2)))



# Begin game
print("\n\nYou will pay at the next counter after finishing the game. Let's begin...")
sleep(1)



# Playing the game as many times as the user wanted 
for i in range(num_plays):
  print("\n\n"+"-"*30,"\n\t\tPLAY NUMBER",i+1, "\n"+"-"*30,"\n")

  # Asking the user to pick a range
  print("Now, you have to pick 2 INTEGER numbers in which you want your magic number to be picked from. \nThe second number must be greater than the first.\n")
  
  num1 = int(input("Enter the first integer: "))
  num2 = int(input("Enter the second integer: "))

  while num2 <= num1:
    print("\nInvalid input for second number.")
    num2 = int(input("Pick again: "))

  # Picking a number
  print("\nAwesome! I am picking a number between", num1, "and", num2, "now.")
  sleep(1)

  # Printing dots for effect
  for j in range(3):
    print(".")
    sleep(1)

  # Choosing a number
  magicNum = randint(num1,num2)

  print("\nOk, I've chosen my number. Let's start guessing.\n\n"+"-"*30, "\n")



  # Asking the user for their first guess
  guess = int(input("Give your first guess: "))

  # A counter to keep track of the number of their guesses
  guessCounter = 1



  # Keep going until they run out of guesses
  while guessCounter <= 5:
    
    if guessCounter >= 5 and guess != magicNum:
      print("I'm sorry, you've run out of guesses. My number was", str(magicNum)+". Better luck next time!")
      break



    # If their guess was not between 1 and 50
    if guess > 50 or guess < 1:
      print("I'm sorry, you didn't follow the rules.")
      break
    

    # If they were following the rules
    else:


      # If their guess is the magic number
      if guess == magicNum:
        

        # Checking if the word should be "try" or "tries" 
        if guessCounter == 1:
          word = "try"
        else:
          word = "tries"
        

        # Let them know how many tries they got the number in
        print("AMAZING!!! You got my magic number in", guessCounter, word +"! Wow you are so magical.")
        break


      # If their guess is higher than the magic number
      elif guess > magicNum:
        H_L = "lower"


      # If their guess is lower than the magic number
      else:
        H_L = "higher"
      


      # Printing the hint and number of guesses left
      if guessCounter == 4: # If there is only one guess left
        word = "guess"
      else:
        word = "guesses"


      print("That's not my number. My number is", H_L, "than your guess. You have", 5-guessCounter, word, "left!")
      

      # Asking the user to guess again
      guess = int(input("\nGuess again: "))
      

      # Increasing their guesses by 1
      guessCounter += 1


  # Letting the user know how many plays they have left
  if num_plays-(i+1) == 0:
    print("\n\nThat was your last play!")

  elif num_plays-(i+1) == 1:
    print("\n\nNext is your final play! Good luck.")

  else:
    print("\n\nThat was fun. You have", num_plays-(i+1),"plays left.")



# Ending script
print("\n"+"-"*30, "\nThank you so much for playing! You can pay your cost of","$"+str(round(final_cost, 2)),"at the next counter.")

print("\nEnd of program")