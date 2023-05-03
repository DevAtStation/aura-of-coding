import requests

while True:
    user_input = input("Enter a pokemon name or \"exit\" to exit): ")
    if user_input == "exit":
        break
    # https://pokeapi.co/api/v2/pokemon/ditto
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{user_input.lower()}")
    if response.status_code == 200:
        data = response.json()
        types = ""
        for type in data['types']:
            types += type['type']['name'] + "/"
        types = types[:-1]
        print(f"{data['name']} is a {types} pokemon")
    else:
        print("Error: ", response.status_code)





""" Example of a GET request
# Make a GET request to the API endpoint
response = requests.get('https://api.example.com/data')

# Check if the request was successful
if response.status_code == 200:
    # Get the response data in JSON format
    data = response.json()
    # Process the data as needed
    print(data)
else:
    print('Error: ', response.status_code)
"""
