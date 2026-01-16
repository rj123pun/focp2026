import random  # Used to randomly select positions from the password

# Ask the user to enter their password
password = input("Enter your password: ")

# Check if the password length is at least 9 characters
if len(password) < 9:
    print("Password too short.")
else:
    # Perform the security check 3 times
    for i in range(3):

        # Randomly choose a position within the password length
        pos = random.randint(1, len(password))

        # Ask the user to enter the letter at the chosen position
        guess = input(f"Enter letter at position {pos}: ")

        # Check if the entered letter matches the actual password character
        if guess == password[pos - 1]:
            print("Correct")
            print(2 - i, "checks remaining")  # Show how many attempts are left
        else:
            # If the guess is wrong, stop the security check immediately
            print("Security check failed.")
            break
    else:
        # This runs only if all 3 checks are passed successfully
        print("Security check passed.")
