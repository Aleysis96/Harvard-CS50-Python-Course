class Food:
    # Base number of hearts every food starts with
    base_hearts = 1

    def __init__(self, ingredients):
        # Store the list of ingredients
        self.ingredients = ingredients
        # Calculate total hearts based on ingredients
        self.hearts = Food.calculate_hearts(ingredients)

    @classmethod
    def calculate_hearts(cls, ingredients):
        # Start with the base number of hearts
        hearts = cls.base_hearts
        # Add hearts based on each ingredient
        for ingredient in ingredients:
            if "hearty" in ingredient.lower():
                hearts += 2  # Hearty ingredients give 2 extra hearts
            else:
                hearts += 1  # Regular ingredients give 1 extra heart
        return hearts  # Return total hearts after processing all ingredients

    @classmethod
    def from_nothing(cls, hearts):
        # Create a Food object with no ingredients but a specified heart value
        food = cls(ingredients=[])
        food.hearts = hearts
        return food

def main():
    # Create a food item with specific ingredients and print its healing value
    mushroom_skewer = Food(ingredients=["Mushroom", "Hearty Mushroom"])
    print(f"This skewer heals {mushroom_skewer.hearts} hearts!")

    # Create a food item manually with a fixed heart value and print its healing value
    mushroom_skewer = Food.from_nothing(hearts=2)
    print(f"This skewer heals {mushroom_skewer.hearts} hearts!")

main()
