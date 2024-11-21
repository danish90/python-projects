#Random name generator project from Daily Python Projects
#Create a program that reads a list of names from a text file, randomly picks one, and displays it

import random
from pathlib import Path
import os

#define the path using pathlib
downloads_directory = Path(os.path.expanduser("~/Downloads"))
file_path = downloads_directory / "names.txt"

with open(file_path, "a+") as file:
    file.seek(0) #this moves the pointer back to the beginning, as a+ sets it at the very end for appending
    names = [line.strip() for line in file] #stores each line without trailing newline character

# print(len(names)) #check if it imported correctly

#this is the next intermediate project, to create a program that can add a new name, select a random name, show total number of names

def total_names():
    return len(names)

def random_name():
    r_name = random.choice(names)
    print(f"Randomly selected name: {r_name}")

def add_name():
    new_name = input("Enter the new name to add: ")
    names.append(new_name)
    return new_name

def name_options():
    print("Please select an option:")
    print("1. Show the total number of names")
    print("2. Add a new name")
    print("3. Select a random name")
    print("4. Exit")


is_running = True

while is_running:
    name_options()
    user_choice = int(input("Enter your choice (1-4): "))
    if user_choice == 1:
        print("")
        print(f"The total number of names is: {total_names()}")
        print("")
    elif user_choice == 2:
        new_name = add_name()
        print(f"{new_name} has been added to the names file")
        print("")
    elif user_choice == 3:
        random_name()
        print("")
    elif user_choice == 4:
        is_running = False
    else:
        print("That is not a valid choice.")
        print("")




# if __name__ == '_main_':
#     main()
