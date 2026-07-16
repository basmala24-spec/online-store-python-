
class Dessert:
    def __init__(self, name, price, calories):
        self.name = name
        self.price = price
        self.calories = calories

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}, {self.calories} calories"



dessert_menu = {

    "Egyptian Desserts": [
        Dessert("Kunafa", 3.5, 350),
        Dessert("Basbousa", 3.0, 250),
        Dessert("Umm Ali", 4.0, 400),
        Dessert("Roz Bel Laban", 3.5, 300),
        Dessert("Feteer Meshaltet (Sweet)", 5.5, 450),
        Dessert("Halawa", 2.5, 200),
    ],

    "Levant Desserts": [
        Dessert("Baklava", 3.0, 300),
        Dessert("Maamoul", 3.5, 320),
        Dessert("Knafeh Nabulsi", 3.8, 360),
        Dessert("Atayef", 3.2, 280),
        Dessert("Halawet El Jibn", 3.9, 340),
    ],

    "Moroccan Desserts": [
        Dessert("Chebakia", 3.5, 400),
        Dessert("Sellou", 3.5, 300),
        Dessert("Ghriba", 3.0, 280),
        Dessert("Kaab el Ghazal", 3.2, 250),
    ],

    "Gulf Desserts": [
        Dessert("Luqaimat", 3.0, 330),
        Dessert("Balaleet", 3.5, 350),
        Dessert("Date Cake", 4.0, 370),
    ],

    "International Desserts": [
        Dessert("Chocolate Cake", 4.5, 450),
        Dessert("Cheesecake", 4.8, 420),
        Dessert("Brownies", 3.8, 400),
        Dessert("Ice Cream", 2.5, 200),
        Dessert("Donuts", 2.8, 300),
    ]
}



def show_dessert():
    for category, items in dessert_menu.items():
        print(f"\n {category}:")
        for i, item in enumerate(items, 1):
            print(f"{i}. {item}")


if __name__ == "__main__":
    show_dessert()