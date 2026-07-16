
class Seafood:
    def __init__(self, name, price, calories):
        self.name = name
        self.price = price
        self.calories = calories

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}, {self.calories} calories"


seafood_menu = {

    "Fish Dishes": [
        Seafood("Grilled Tilapia", 6.5, 300),
        Seafood("Fried Tilapia", 7.0, 450),
        Seafood("Sayadeya Rice with Fish", 8.0, 500),
        Seafood("Baked Salmon", 9.5, 400),
        Seafood("Grilled Sea Bass", 10.0, 420),
        Seafood("Fried Sea Bream", 9.0, 480),
        Seafood("Fish Fillet", 7.5, 350),
        Seafood("Fish Curry", 8.5, 450),
    ],

    "Shrimp Dishes": [
        Seafood("Grilled Shrimp", 9.0, 350),
        Seafood("Fried Shrimp", 9.5, 500),
        Seafood("Butter Garlic Shrimp", 10.5, 550),
        Seafood("Shrimp Pasta", 10.0, 600),
        Seafood("Shrimp Soup", 7.0, 250),
        Seafood("Spicy Shrimp", 9.8, 480),
        Seafood("Shrimp Rice", 9.5, 520),
    ],

    "Calamari & Squid": [
        Seafood("Fried Calamari", 8.5, 450),
        Seafood("Grilled Calamari", 8.0, 300),
        Seafood("Stuffed Squid", 9.5, 500),
        Seafood("Squid Rings", 8.8, 430),
    ],

    "Crab & Lobster": [
        Seafood("Grilled Crab", 11.0, 400),
        Seafood("Crab Soup", 8.0, 300),
        Seafood("Lobster Grilled", 15.0, 600),
        Seafood("Lobster Thermidor", 16.5, 700),
        Seafood("Crab Cakes", 9.5, 450),
    ],

    "Seafood Mix": [
        Seafood("Seafood Mix Grill", 12.0, 650),
        Seafood("Seafood Pasta", 11.0, 600),
        Seafood("Seafood Rice", 10.5, 580),
        Seafood("Seafood Soup", 7.5, 300),
        Seafood("Paella", 13.0, 700),
    ],

    "Sandwiches & Light Meals": [
        Seafood("Fish Sandwich", 5.5, 350),
        Seafood("Shrimp Sandwich", 6.5, 400),
        Seafood("Tuna Sandwich", 4.5, 300),
        Seafood("Fish Burger", 6.0, 450),
    ]
}
def show_seafood():
    print("\n Seafood Menu:\n")
    for category, items in seafood_menu.items():
        print(f"--- {category} ---")
        for i, item in enumerate(items, 1):
            print(f"{i}. {item}")
if __name__ == "__main__":  
    show_seafood()