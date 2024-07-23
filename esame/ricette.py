class RecipeManager:

    def __init__(self) -> None:
        self.ricette = {}
    
    def create_recipe(self, name: str, ingridients: list[str]):
        if name in self.ricette:
            return "La ricetta esiste già."
        self.ricette[name] = ingridients
        return self.ricette
    
    def add_ingredient(self, recipe_name: str, ingredient: str):
        if recipe_name not in self.ricette:
            return "La ricettanon esiste."
        if ingredient in self.ricette[recipe_name]:
            return "L'ingrediente esiste già."
        self.ricette[recipe_name].append(ingredient)
        return self.ricette
    
    def remove_ingredient(self, recipe_name: str, ingredient: str):
        if recipe_name not in self.ricette:
            return "La ricetta non esiste."
        if ingredient not in self.ricette[recipe_name]:
            return "L'ingrediente non esiste."
        self.ricette[recipe_name].remove(ingredient)
        return self.ricette
    
    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str):
        ingredients = self.ricette[recipe_name]
        if old_ingredient not in ingredients:
            return "L'ingrediente non esiste."
        if recipe_name not in self.ricette:
            return "La ricetta non esiste."
        updated_ingredients = [new_ingredient if ingredient == old_ingredient else ingredient for ingredient in ingredients]
        self.ricette[recipe_name] = updated_ingredients
        return self.ricette
    
    def list_recipes(self):
        lista= []
        for k in self.ricette.keys():
            lista.append(k)
        return lista
    
    def list_ingredients(self, recipe_name: str):
        if recipe_name not in self.ricette:
            return "La ricetta non esiste."
        return self.ricette[recipe_name]
    
    def search_recipe_by_ingredient(self, ingredient: str):
        for k, v in self.ricette.items():
            if ingredient in v:
                return self.ricette
    
manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.list_ingredients("Pizza Margherita"))
