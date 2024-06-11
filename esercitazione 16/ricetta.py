class RecipeManager:

    def __init__(self) -> None:
        self.ricette: dict = {}

    def create_recipe(self, name: str, ingredients: list[str]):
        if not self.ricette[name]:
            self.ricette[name] = ingredients
        else:
            print("La ricetta già esiste.")
    
    def add_ingredient(self, recipe_name: str, ingredient: str):
        if ingredient not in self.ricette[recipe_name]:
            self.ricette[recipe_name] = ingredient
