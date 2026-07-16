
class food:
    def __init__(self, name,price, calories, protien, carbs, fats):
        self.name     = name
        self.calories = calories
        self.protien  = protien
        self.carbs    = carbs
        self.fats     = fats
        self.price    =price


    def calories_for(self, grams):
        return round((self.calories * grams) / 100, 1)
    def protien_for(self, grams):
        return round((self.protien * grams) / 100, 1)
    def carbs_for(self, grams):
        return round((self.carbs * grams) / 100, 1)
    def fats_for(self, grams):
        return round((self.fats * grams) / 100, 1)
    def __str__(self):
        return f"{self.name}  —  {self.calories} kcal / 100g"
    
class salad(food):
    def __init__(self, name,price, calories, protien, carbs, fats, dressing):
        super().__init__(name,price, calories, protien, carbs, fats)
        self.dressing = dressing
    def dres_disc(self):
        return f"{self.name} with {self.dressing}"
    
class salmon(food):
    def __init__(self, name,price, calories, protien, carbs, fats, veggies):
        super().__init__(name,price, calories, protien, carbs, fats)
        self.veggies = veggies
    def choose_veggi(self):
        return f"{self.name} with {self.veggies}"
    
class chicken(food):
    def __init__(self, name,price, calories, protien, carbs, fats, method):
        super().__init__(name,price, calories, protien, carbs, fats)
        self.method = method
    def cook_method(self):
        return f"{self.method} {self.name}"
    
class meat(food):
    def __init__(self, name,price, calories, protien, carbs, fats, level):
        super().__init__(name,price, calories, protien, carbs, fats)
        self.level = level
    def level_of_doneness(self):
        return f"{self.level} {self.name}"
    
dressing_options = ['Olive Oil','Caesar','Lemon Tahini','Ranch']
veggies_options  = ['Broccoli','Spinach','Zucchini','Carrots']
method_options   = ['Roasted','Grilled','Steamed','Pan Seared']
level_options    = ['Rare','Medium Rare','Well Done']
caesar  = salad  ('Salad', 23,    85,  3,  7,  6, None)
salmone = salmon ('Salmon',45,  208, 20,  0, 13, None)
chick   = chicken('Chicken',45, 165, 31,  0,  4, None)
steak   = meat   ('Steak',  34, 271, 26,  0, 18, None)
menu = {
    "Salad": [caesar],
    "Seafood": [salmone],
    "Chicken": [chick],
    "Meat": [steak]
}
extras = {
    0: ("Dressing",    dressing_options, "dressing"),
    1: ("Veggies",     veggies_options,  "veggies"),
    2: ("Method", method_options,   "method"),
    3: ("level",    level_options,    "level"),
}

def healthy_food():
    for z, y in enumerate(menu, 1):
        print(f"[{z}] {y}")
if __name__ == "__main__":
    healthy_food()


# for z, y in enumerate(menu, 1):
#     print(f"[{z}] {y}")
# choice   = int(input("choose your meal: ")) - 1
# grams    = float(input("how many grams?   "))
# selected = menu[choice]
# meal , option, dict_value =extras[choice]
# for v ,x in enumerate(option,1):
#     print(f'[{v}] {x}')
# extra_choice=int(input(f' choose {meal}')) - 1
# setattr(selected,dict_value,option[extra_choice])
# print(f"{selected.name}: {grams}g")
# print(f"  Calories : {selected.calories_for(grams)} kcal")
# print(f"  Protein  : {selected.protien_for(grams)}g")
# print(f"  Carbs    : {selected.carbs_for(grams)}g")
# print(f"  Fats     : {selected.fats_for(grams)}g")

def show_healthy_food():
    print("\n--- Healthy Food Menu ---")
    print("1. Salad")
    print("2. Quinoa Bowl")
    print("3. Veggie Stir-Fry")
    print("4. Smoothie")

if __name__ == "__main__":
    show_healthy_food()
