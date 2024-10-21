from random import randint  # Importing the randint function to generate a random number.

NUMBER = randint(1, 100)  # Generating a random number between 1 and 100 and storing it in the constant NUMBER.

while True:  # Starting an infinite loop to continuously ask for user input.
    try:
        QUESTION = int(
            input('Guess the number: '))  # Asking the user to guess the number and converting the input to an integer.
        if QUESTION < NUMBER:  # Checking if the guess is smaller than the generated number.
            print('Too small')  # Informing the user that the guess is too small.
        elif QUESTION > NUMBER:  # Checking if the guess is larger than the generated number.
            print('Too big')  # Informing the user that the guess is too big.
        else:
            print('You won!')  # If the guess is correct, print a winning message.
            break  # Exit the loop when the correct guess is made.
    except ValueError:  # Catching the exception if the input is not a valid integer.
        print('It\'s not a number!')  # Informing the user that the input was not a valid number.

