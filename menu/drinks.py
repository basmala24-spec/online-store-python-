
class drinks:
    def __init__(self, name, price,calories):
        self.name = name 
        self.price = price
        self.calories = calories


    def __str__(self):
        return f"{self.name}: {self.price}EGP | {self.calories} kcal"
    


drinks_menu = {
    "hot drinks": (
        ("Espresso", 45, 5),
        ("Cappuccino", 65, 120),
        ("Latte", 70, 150),
        ("Flat White", 75, 110),
        ("Turkish Coffee", 35, 10),
        ("Tea", 25, 0),
        ("Green Tea", 30, 0),
        ("Hot Chocolate", 80, 250)),


    "cold drinks": (
        ("Iced Latte", 85, 140),
        ("Iced Americano", 60, 5),
        ("Peach Iced Tea", 55, 90),
        ("Mocha Frappuccino", 95, 380)),


    "fresh juices": (
        ("Orange Juice", 50, 110),
        ("Lemon Mint", 45, 130),
        ("Strawberry Juice", 55, 120),
        ("Mango Juice", 70, 180)),


    "smoothies & shakes": (
        ("Blueberry Smoothie", 90, 210),
        ("Vanilla Milkshake", 100, 450),
        ("Chocolate Milkshake", 110, 520))
}



def show_drinks():
    for category, items in drinks_menu.items():
        print(f"\n__{category.upper()}__")
        for name, price, calories in items:
            print(drinks(name, price, calories))

if __name__ == "__main__":
    show_drinks()

if __name__ == "__main__":
    drinks_menu()