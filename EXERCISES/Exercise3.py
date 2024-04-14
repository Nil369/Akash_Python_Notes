# Make a guess game 
n = 18 #user have to guess this number
# Total no. of gusses = 9
# No. of gusses left => Print
# No. of gusses the person took to finish
# GAME OVER if the person finished his totalm number of gusses


print("This is a gusses the number game 😁")
number_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<18:
        print("you enter less number please input greater number.\n")
    elif guess_number>18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses,"no.of guesses he took to finish.")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("Game Over")
  
