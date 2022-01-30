#Guessing Number Game
#Core


import random
numbers = random.randrange(1,50)
numberOfGuesses = 0

#Flavour Texts and asking for name
input("Press Enter to Continue.")
playersName = input("Enter the name of the player >")
print("Hello",playersName,".","Lets play a game, a guessing game.")
print("Ill give you 10 guesses that should be enough for you to get it correct.")
print("Im thinking of a number between 1 to 50 what number am i thinking of?.")


loop =True
while numberOfGuesses < 10:
          guess = int(input(">"))

#The Loop here is if the user somehow imputs something that isnt between 1-50
          if guess >=1 and guess <=50:
                    loop = False
          else:
                    print("Ok how hard is it to choose a number between 1 and 50? Try again")


          if guess < numbers and guess >0:
                      print("Unlucky your guess was to low. Try aiming a little higher.") #This is the message that shown if the user guess to low
                      numberOfGuesses = numberOfGuesses+1
          if guess > numbers and guess <51:
                      print("Unlucky your guess was to high. Aim Lower bud.")# This is the message that is shown when the user guesses to high
                      numberOfGuesses = numberOfGuesses+1


          if guess == numbers: #If they guess the number correctly it will sent them to the victory message
                      break
          if numberOfGuesses == 10: #This is if they use up all 10 of their guesses and lose
                    break

if guess == numbers:
          print("")
          print("You guessed correctly. Good job",playersName," you completed my little guessing game. Number of guesses >", str(numberOfGuesses)) # This is the message the user gets if they guess correctly

else:
          print("")
          print("How sad you failed better luck next time", playersName, ".",)# This is the message the user gets if they run out of guesses
          print("The number was >", str(numbers))#The actual number the user had to guess
