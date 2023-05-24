import requests

def search_recipes(query):
    url = f""  #add query url (API)
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        recipes = data["recipes"]
        
        for recipe in recipes:
            print(recipe["title"])
    else:
        print("Error searching for recipes.")

def get_recipe(recipe_id):
    url = f"" #add query url (API)
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        recipe = data["recipe"]
        
        print("Title:", recipe["title"])
        print("Ingredients:")
        for ingredient in recipe["ingredients"]:
            print("- " + ingredient)
        print("Instructions:")
        print(recipe["instructions"])
    else:
        print("Error retrieving recipe details.")

search_recipes("") #add search value

get_recipe("") #add get recipe
