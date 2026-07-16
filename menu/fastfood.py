# fast food menu
class FastFood:
    def __init__(self, name, price, calories):
        self.name = name
        self.price = price
        self.calories = calories

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}, {self.calories} calories"   


items = [
        ("Burger", 5.99, 550),
        ("Cheeseburger", 6.49, 650),
        ("Bacon Burger", 7.99, 750),
        ("Double Burger", 8.99, 850),
        ("Veggie Burger", 5.99, 450),
        ("Chicken Burger", 6.99, 600),
        ("Fish Burger", 6.49, 500),
        ("Fries", 2.99, 300),
        ("Large Fries", 3.99, 450),
        ("Curly Fries", 3.49, 350),
        ("Sweet Potato Fries", 3.99, 250),
        ("Onion Rings", 3.49, 400),
        ("Soda", 1.99, 150),
        ("Coke", 1.99, 140),
        ("Sprite", 1.99, 150),
        ("Fanta", 1.99, 160),
        ("Lemonade", 2.49, 120),
        ("Iced Tea", 2.49, 100),
        ("Coffee", 1.99, 5),
        ("Hot Chocolate", 2.49, 200),
        ("Chicken Nuggets", 4.99, 250),
        ("Chicken Wings", 6.99, 400),
        ("Chicken Strips", 5.99, 350),
        ("Chicken Sandwich", 6.99, 550),
        ("Grilled Chicken", 7.49, 400),
        ("Fried Chicken", 6.99, 600),
        ("Salad", 3.99, 150),
        ("Caesar Salad", 4.99, 250),
        ("Garden Salad", 3.99, 100),
        ("Cobb Salad", 5.99, 350),
        ("BLT Sandwich", 5.99, 450),
        ("Club Sandwich", 6.99, 500),
        ("Tuna Sandwich", 5.49, 350),
        ("Turkey Sandwich", 5.99, 400),
        ("Ham Sandwich", 5.49, 380),
        ("Roast Beef Sandwich", 6.49, 450),
        ("Sub Sandwich", 7.99, 600),
        ("Wrap", 5.99, 350),
        ("Chicken Wrap", 6.49, 400),
        ("Veggie Wrap", 5.49, 250),
        ("Beef Wrap", 6.99, 500),
        ("Quesadilla", 4.99, 400),
        ("Chicken Quesadilla", 5.99, 450),
        ("Beef Quesadilla", 6.49, 500),
        ("Taco", 2.99, 200),
        ("Chicken Taco", 3.49, 250),
        ("Beef Taco", 3.99, 300),
        ("Burrito", 6.99, 600),
        ("Chicken Burrito", 7.49, 650),
        ("Beef Burrito", 7.99, 700),
        ("Nachos", 4.99, 500),
        ("Loaded Nachos", 6.99, 700),
        ("Pizza", 8.99, 800),
        ("Cheese Pizza", 9.49, 750),
        ("Pepperoni Pizza", 10.99, 850),
        ("Veggie Pizza", 9.99, 700),
        ("Chicken Pizza", 10.49, 800),
        ("Soup", 3.49, 150),
        ("Tomato Soup", 3.49, 120),
        ("Chicken Noodle Soup", 3.99, 180),
        ("Chili", 4.49, 300),
        ("Hot Dog", 3.99, 400),
        ("Corn Dog", 2.99, 350),
        ("Pretzel", 2.49, 200),
        ("Popcorn", 2.99, 150),
        ("Candy", 1.49, 100),
        ("Chocolate Bar", 1.99, 200),
        ("Gummy Bears", 1.49, 150),
        ("Lollipop", 0.99, 50),
        ("Fruit Cup", 2.99, 80),
        ("Yogurt", 1.99, 100),
        ("Parfait", 3.49, 250),
        ("Smoothie", 3.99, 200),
        ("Juice Box", 1.49, 90),
    ]
    
menu = {
        "Burgers": items[0:7],
        "Fries and Sides": items[7:12],
        "Drinks": items[12:20],
        "Chicken Items": items[20:26],
        "Salads": items[26:30],
        "Sandwiches": items[30:37],
        "Wraps": items[37:41],
        "Mexican Food": items[41:52],
        "Pizza": items[52:57],
        "Soups": items[57:61],
        "Other": items[61:74],
    }

def show_fast_food_menu():
    for category, item_list in menu.items():
            print(f"\n{category}:")
            for item in item_list:
                food = FastFood(*item)
                print(food)     
if __name__ == "__main__":
    show_fast_food_menu()