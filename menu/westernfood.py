
class westfood:
    def __init__(self,name,price,calories,protien,carbs,fats):
        self.name=name
        self.price=price
        self.calories=calories
        self.protien=protien
        self.carbs=carbs
        self.fats=fats
    def details(self):
        return (f"{self.name} , ${self.price:.2f} , {self.calories} kcal ,"
                f"protein:{self.protien}g , carbs:{self.carbs}g , fats:{self.fats}g")
    

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
    


class hamburger(westfood):
    def __init__(self, name, price, calories, protien, carbs, fats, size=None):
        super().__init__(name, price, calories, protien, carbs, fats)
        self.size = size
    def get_size(self):
        return f"{self.name} with {self.size}"
    


class burrito(westfood):
    def __init__(self, name, price, calories, protien, carbs, fats, topping=None):
        super().__init__(name, price, calories, protien, carbs, fats)
        self.topping = topping
    def get_topping(self):
        return f"{self.name} with {self.topping}"
    


class pizza(westfood):
    def __init__(self, name, price, calories, protien, carbs, fats, dough=None):
        super().__init__(name, price, calories, protien, carbs, fats)
        self.dough =dough 
    def get_dough(self):
        return f"{self.name} with {self.dough}"
    

class pasta(westfood):
    def __init__(self, name, price, calories, protien, carbs, fats, sauce=None):
        super().__init__(name, price, calories, protien, carbs, fats)
        self.sauce = sauce
    def get_sauce(self):
        return f"{self.name} with {self.sauce}"
    

size_options = ['home_made','single','double','triple']
topping_options = ['rize','meat','chicken','pork']
dough_options   = ['napolitan','crust canotto','sicilian','new york']
sauce_options    = ['pomodoro','carbonara','bolognese','bechamel']
burger = hamburger('hamburger',  300, 20,  24, 14, None)
burito = burrito('burrito', 300, 15,  30,  10, None)
pizz  = pizza('pizza', 300, 13,  30,15, None)
spaghetti = pasta('pasta',158 ,  6,  31,  1, None)
menu = [burger,burito,pizz,spaghetti]

extras = {
    0: ("size", size_options),
    1: ("topping", topping_options),
    2: ("dough", dough_options),
    3: ("sauce", sauce_options),
}

def show_western_food():
    for z, y in enumerate(menu, 1):
        print(f"[{z}] {y}")
if __name__ == "__main__":
    show_western_food()
    