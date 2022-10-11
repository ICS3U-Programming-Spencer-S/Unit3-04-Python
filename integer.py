#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Date: Oct. 11, 2022
# A program used to state if a integer positive, negative, or zero.
# But using If, then, elseif, else statements.


def main():

    # spacer
    print("")

    # Ask for the integer number from the user
    print("This is a program to state if a integer is positive, negative or zero.")
    user_integer = int(input("Enter a integer: "))

    # spacer
    print("")

    # if, elseif, else, then statement
    # to determine if it's a positive, negative or zero
    if user_integer > (0):
        print(f"Your integer {user_integer} is a positive number.")
    elif user_integer < (0):
        print(f"Your integer {user_integer} is a negative number.")
    elif user_integer == (0):
        print("Your integer is zero!")
    else:
        print("Unknown issue")


if "__main__" == __name__:
    main()
