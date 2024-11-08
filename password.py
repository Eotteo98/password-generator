# by making 3 lists of letters, numbers and special symbols. Choose random values from these 3 lists .A random punctuation character can also be chosen from the string.Combine all of these to generate a random password.
# The password must be 6 characters long and no numbers should be next to the symbols.
# EX:  !@AC45
letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbols_list = ["!", "@", "#", "$", "%"] 
import random
letter = random.choice(letter_list)
number = random.choice(number_list)
symbol = random.choice(symbols_list)

letter1 = random.choice(letter_list)
number1 = random.choice(number_list)
symbol1 = random.choice(symbols_list)

print("your password is", number, number1, letter, letter1, symbol , symbol1)

txt1 = "Your password is {}{}{}{}{}{}".format(number, number1, letter, letter1, symbol , symbol1)

print(txt1)


choices = ["rock", "paper", "scissors"]