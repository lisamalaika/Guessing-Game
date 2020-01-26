# my new file
var_1 = "Lisa"
var_2 = "Jessica"
var_3 = "Thomas"

#print(var_1, var_2, var_3)
# create array
names = []
# add variables to array
names.append(var_1)
names.append(var_2)
names.append(var_3)
names.append("Peter")
# loop through array/ printing the variables
for i in range(len(names)):
    print(i + 1, names[i])

#  https://stackoverflow.com/questions/29811082/how-to-print-out-a-numbered-list-in-python-3v

# guessing game
# create number in range 1 to 10
number_guess = 1
# ask the question
print("Guess a number from 1 to 10")
# get user input
user_guess = int(input())
print("You guessed", user_guess)
# evaluate

#guess 1
if number_guess == user_guess:
    print("Congratulations!")
elif user_guess < 0 or user_guess > 11:
    print("You're out of the range!")
else: 
    print("Wrong guess! Guess again")
user_guess = int(input())

# guess 2
if number_guess == user_guess:
    print("Congratulations!")
elif user_guess < 0 or user_guess > 11:
    print("You're out of the range!")
else: 
    print("Wrong guess! Guess again")
user_guess = int(input())

# guess 3
if number_guess == user_guess:
    print("Congratulations!")
elif user_guess < 0 or user_guess > 11:
    print("You're out of the range!")
else: 
    print("Wrong guess! You're out of guesses")
