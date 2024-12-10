#simple magic 8 ball

import magic8ball_responses as responses_module
import random

#define weights for the response categories
weights = {
    "positive" : 50,
    "neutral"  : 25,
    "negative" : 25
}

def main():

    responses = responses_module.responses

    category = random.choices(
        list(weights.keys()), #convert the weights keys into a list
        weights=list(weights.values()), #set the weights syntax in the random.choices to the values as a list
        k=1 #select 1 value from the list
    )[0] # takes the 1st list value and converts it into a str format

    #get a random response from the chosen category
    if category in responses:
        user_response = random.choice(responses[category])
        user_question = input("What do you want to know: ")
        print(f"Magic 8 Ball says to '{user_question}': {user_response}")
    else:
        print(f"Error: no responses found for category '{category}'")

if __name__ == "__main__":
    main()