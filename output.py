import requests

class test:

    def __init__(self):
        self.url = "http://google.com"
        self.headers = {"Content-Type": "application/json"}


    def Get_Pokemon(self, name):

        r = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{{ name }}",
            headers = self.headers,
            verify=False
        )

        return r.json()
        
    def Get_Type(self, type):

        r = requests.get(
            f"https://pokeapi.co/api/v2/type/{{ type }}",
            headers = self.headers,
            verify=False
        )

        return r.json()
        
    def Get_Ability(self, ability):

        r = requests.get(
            f"https://pokeapi.co/api/v2/ability/{{ ability }}",
            headers = self.headers,
            verify=False
        )

        return r.json()
        