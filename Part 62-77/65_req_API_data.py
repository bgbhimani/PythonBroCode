# how to connect API using python
import requests
# Copy the link form pokeapi.co

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}pokemon/{name}"
    response = requests.get(url)
    # print(response)    #http code:200 means the response is OK
    
    if response.status_code == 200:
        # print("Data Retrived")
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrive the data {response.status_code}")
    


pokemon_name = input("Enter the name of Pokemon: ")
pokemon_info = get_pokemon_info(pokemon_name)
# it is the dictionary

if pokemon_info:  #it return True if dic exist
    print(f"Name  = {pokemon_info["name"].capitalize()}")
    print(f"Id    = {pokemon_info["id"]}")
    print(f"Height= {pokemon_info["height"]}")
    print(f"Weight= {pokemon_info["weight"]}")