print("Enter the integer for the player to guess.")
winning_number = int(input())
# print(f'The winning number you chose is: {winning_number}')
print('Enter your guess user:')
user_guess = int(input())
if winning_number == user_guess:
    print(f'You guessed it in 1 try, the correct number was {winning_number}')
else:
    if(user_guess > winning_number):
        print('Too high - try again: ')
    else:
        print('Too low - try again: ')
trys = 1
while winning_number != user_guess:
    user_guess = int(input())
    trys += 1
    if winning_number == user_guess:
        print(f'You guessed it in {trys} try, the correct number was {winning_number}')
    else:
        if(user_guess > winning_number):
            print('Too high - try again: ')
        else:
            print('Too low - try again: ')