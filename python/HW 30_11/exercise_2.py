class Recipe:
    def __init__(self, name, author, recipetype, description, videolink, ingredients, cuisine):
        self.name = name
        self.author = author
        self.recipetype = recipetype
        self.description = description
        self.videolink = videolink
        self.ingredients = ingredients
        self.cuisine = cuisine


class RecipeView:

    def display_recipe(self, recipe):
        print("Recipe Name: ", recipe.name)
        print("Author: ", recipe.author)
        print("Recipe Type: ", recipe.recipetype)
        print("Description: ", recipe.description)
        print("Video Link: ", recipe.videolink)
        print("Ingredients: ", recipe.ingredients)
        print("Cuisine: ", recipe.cuisine)


class RecipeController:
    def __init__(self, recipe, view):
        self.recipe = recipe
        self.view = view

    def update_recipe(self, name, author, recipetype, description, videolink, ingredients, cuisine):
        self.recipe.name = name
        self.recipe.author = author
        self.recipe.recipetype = recipetype
        self.recipe.description = description
        self.recipe.videolink = videolink
        self.recipe.ingredients = ingredients
        self.recipe.cuisine = cuisine


    def get_recipe(self):
        return self.recipe


recipe = Recipe("Spaghetti Carbonara", "John Doe", "Main Dish", "A delicious Italian pasta dish with bacon and eggs.", "https://www.youtube.com/watch?v=6nH2nYsPHQ4", ["spaghetti", "bacon", "eggs", "parmesan cheese", "black pepper"], "Italian")
view = RecipeView()
controller = RecipeController(recipe, view)
controller.update_recipe("Lasagna", "Jane Smith", "Main Dish", "A classic Italian dish with layers of pasta, meat sauce, and cheese.", "https://www.youtube.com/watch?v=1pS4njU0OJw", ["lasagna noodles", "ground beef", "tomato sauce", "ricotta cheese", "mozzarella cheese"], "Italian")
recipe = controller.get_recipe()
view.display_recipe(recipe)