#program that reads a list of motivational quotes from a text file and selects one to display every Monday, or any day the user runs the program
#asked claude to generate a list of laid-back, dgaf, zen, and strategic laziness quotes; these are actually pretty good

import random
from pathlib import Path
import os
import datetime as dt

#define the path using pathlib
downloads_directory = Path(os.path.expanduser("~/Downloads"))
input_file_path = downloads_directory / "motivational-quotes.txt"
output_file_path = downloads_directory / "motivational-quotes-upd.txt"

with open(input_file_path, "r") as input_file:
    input_lines = [line.strip() for line in input_file] #removes whitespace including trailing newline character (so \n is removed too)

motivational_quotes = [line for line in input_lines if not line.startswith("#")]

with open(output_file_path, "w") as output_file:
    for line in motivational_quotes:
        output_file.write(line + "\n")

print(f"Lines without comments have been written to '{output_file_path}'")

# print(len(motivational_quotes)) #check if this has been read correctly
# print(help(datetime))

today = dt.datetime.now()
day_of_week = today.strftime("%A") #strftime is a string formatting method that comes with datetime library; it converts a datetime object into a formatted string; else it would look something like 2024-11-19 21:35:16.536791; %A is the format code that returns the full name of the day of week

def is_weekday(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return True
        case "Saturday" | "Sunday":
            return False
        case _:
            return "Error: not a valid day"

# print(is_weekday(day_of_week)) #check if this is working

print("---------------------------------------------------------------")
print("Ready to get motivated? It's a weekday, of course you need it.")
print("")
print(f"🐷🐲🐾Motivational quote of {day_of_week}🐳🦦🦀")
print("")

if is_weekday(day_of_week):
    random_quote = random.choice(motivational_quotes)
    print(f"{random_quote}")
else:
    print(f"Today is {day_of_week}! Since it's a weekend, no motivation is needed to enjoy your life")