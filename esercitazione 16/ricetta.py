class RecipeManager:

    def __init__(self) -> None:
        self.ricette: dict = {}


    def create_recipe(self, name: str, ingredients: list[str]):
        if name not in self.ricette:
            self.ricette[name] = ingredients
            return self.ricette
        else:
            print("La ricetta già esiste.")
    

    def add_ingredient(self, recipe_name: str, ingredient: str):
        if ingredient not in self.ricette[recipe_name]:
            self.ricette[recipe_name].append(ingredient)
            return self.ricette


    def remove_ingredient(self, recipe_name: str, ingredient: str):
        if ingredient in self.ricette[recipe_name]:
            self.ricette[recipe_name].remove(ingredient)
            return self.ricette
        else:
            print ("L'ingrediente non è presente.")


    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str):
        if old_ingredient in self.ricette[recipe_name]:
            index = self.ricette[recipe_name].index(old_ingredient)
            self.ricette[recipe_name][index] = new_ingredient
            return self.ricette
        else:
            print("L'ingrediente non esiste.")


    def list_recipes(self):
        ricettel: list = []
        for k in self.ricette.keys():
            ricettel.append(k)
        return ricettel


    def list_ingredients(self, recipe_name: str):
        return self.ricette[recipe_name]


    def search_recipe_by_ingredient(self, ingredient: str):
        ricettel: dict = {}
        for k, ingredients in self.ricette.items():
            if ingredient in ingredients:
                ricettel[k] = ingredients
            else:
                continue
        return ricettel
