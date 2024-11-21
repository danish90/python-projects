import json
from pathlib import Path
import os

#define the path using pathlib
downloads_directory = Path(os.path.expanduser("~/Downloads"))
file_path = downloads_directory / "recipes.json"

with open(file_path, "r") as json_file:
    recipes = json.load(json_file)

# print(data) #check that the json is imported correctly

print("--------------This is the recipe finder--------------")

user_ingredients = input("Enter a list of ingredients, separated by commas: ").split(",") #.split with the , splits the string at each comma and makes it into a list of ingredients; this means it defines the variable as a list []
user_ingredients = {ingredient.strip().lower() for ingredient in user_ingredients} #this converts it into a set

matching_recipes =[]
for recipe in recipes:
    ingredients = set(recipe['ingredients'])
    if ingredients.issubset(user_ingredients):
        matching_recipes.append(recipe)

#Now we display the matching recipes
if matching_recipes:
    print("Here are some recipes you can make: ")
    print("")
    for recipe in matching_recipes:
        print(f"Recipe: {recipe['name']}")
        print(f"Ingredients: {", ".join(recipe['ingredients'])}") # ", ".join is a string method that concatenates all elements of a list into a single string - this helps to format it nicely
        print(f"Instructions: {recipe['instructions']}")
        print("")
else:
    print("No matching recipes found.")
