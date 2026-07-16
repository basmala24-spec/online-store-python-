
class breakfast:
    def __init__(self, name, price,calories):
        self.name = name 
        self.price = price
        self.calories = calories


    def __str__(self):
        return f"{self.name}: {self.price}EGP | {self.calories} kcal"
    


breakfast_menu =  {
    "eggs":(("omelette",20, 150),
            ("fried eggs",30, 200),
            ("scrambled eggs",40, 100),
            ("Shakshuka", 45, 250),
            ("Boiled Eggs", 15, 140)),


    "pastries":(("croissant",50, 250),
        ("toast",70, 200),
        ("pancakes",100, 350),
        ("Waffles", 90, 400),
        ("Cinnabon", 85, 450)),


    "sandwiches":(("cheese sandwich",100, 350),
        ("turky sandwich",150, 400),
        ("Club Sandwich", 180, 500),
        ("Foul Sandwich", 15, 220),
        ("Falafel Sandwich", 15, 280)),


    "oriental corner": (("Foul Dish", 30, 350),
        ("Falafel Plate", 25, 400),
        ("Mixed Cheese Plate", 60, 450),
        ("Mesakaa", 40, 320))
    
}



def show_breakfast():
    for category, items in breakfast_menu.items():
        print(f"\n__{category.upper()}__")
        for name, price, calories in items:
            print(breakfast(name, price, calories))

if __name__ == "__main__":
    show_breakfast()


if __name__ == "__main__":
    breakfast_menu()