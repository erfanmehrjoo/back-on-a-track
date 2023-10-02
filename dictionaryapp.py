import requests
import json

# Define the API endpoint
API_ENDPOINT = "https://api.dictionaryapi.dev/api/v2/entries/en/{}"

# Look up a word in the dictionary
def look_up_word(word):
  response = requests.get(API_ENDPOINT.format(word))
  data = json.loads(response.content)
  definition = data[0]["meanings"][0]["definitions"][0]["definition"]
  return definition

# Get the user input
word = input("Enter a word: ")

# Look up the word in the dictionary
definition = look_up_word(word)

# Print the definition
print(definition)