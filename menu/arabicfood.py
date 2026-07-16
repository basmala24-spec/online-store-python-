# Arabic Food Menu
class ArabicFoodMenu:
    def __init__(self, name, price, calories):
        self.name = name
        self.price = price
        self.calories = calories

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}, {self.calories} calories"


categories = {
        "Egypt": [
            ("Koshary", 4.99, 500),
            ("Ful Medames", 3.99, 300),
            ("Molokhia", 5.49, 250),
            ("Mahshi", 6.99, 400),
            ("Hawawshi", 5.99, 550),
            ("Falafel", 4.99, 300),
            ("Taameya", 4.49, 280),
            ("Lentil Soup", 3.49, 120),
            ("Chicken Soup", 3.99, 180),
            ("Beef Soup", 4.49, 250),
            ("Baklava", 2.99, 300),
            ("Basbousa", 2.99, 250),
            ("Kunafa", 3.49, 350),
            ("Halva", 2.49, 200),
            ("Umm Ali", 3.99, 400),
            ("Feteer", 5.99, 450),
            ("Roz Bel Laban", 4.49, 300),
            ("Bamia", 5.49, 250),
            ("Sayadeya", 6.99, 500),
            ("Torly", 3.99, 200),
            ("Falafel", 4.99, 300),
        ],
        "Morocco": [
            ("Tagine", 7.99, 550),
            ("Couscous", 6.49, 450),
            ("Pastilla", 8.99, 600),
            ("Harira", 4.49, 200),
            ("Bissara", 3.99, 150),
            ("Rfissa", 6.99, 500),
            ("Khobz", 1.99, 200),
            ("Msemen", 2.49, 250),
            ("Baghrir", 2.99, 180),
            ("Sellou", 3.49, 300),
            ("Halwa Shebakia", 2.99, 350),
            ("Chebakia", 3.49, 400),
            ("Kaab el Ghazal", 2.49, 250),
            ("Ghriba", 2.99, 280),
            ("Ma'amoul", 3.99, 320),
        ],
        "Lebanon": [
            ("Shawarma", 5.99, 400),
            ("Falafel", 4.99, 300),
            ("Hummus", 3.99, 200),
            ("Tabbouleh", 4.49, 150),
            ("Baba Ghanoush", 4.99, 250),
            ("Kebabs", 6.99, 500),
            ("Lamb Chops", 8.99, 600),
            ("Chicken Kabob", 5.99, 350),
            ("Beef Kabob", 6.49, 450),
            ("Vegetable Kabob", 4.99, 200),
            ("Pita Bread", 1.49, 150),
            ("Rice Pilaf", 2.99, 250),
            ("Fattoush Salad", 4.49, 150),
            ("Greek Salad", 4.99, 200),
            ("Couscous Salad", 3.99, 180),
        ],

        "Syria": [
            ("Kibbeh", 6.99, 450),
            ("Shawarma", 5.99, 400),
            ("Falafel", 4.99, 300),
            ("Hummus", 3.99, 200),
            ("Baba Ghanoush", 4.99, 250),
            ("Tabbouleh", 4.49, 150),
            ("Fattoush", 4.49, 150),
            ("Knafeh", 3.49, 350),
            ("Baklava", 2.99, 300),
            ("Basbousa", 2.99, 250),
        ],
        "Jordan": [
            ("Mansaf", 8.99, 700),
            ("Maqluba", 7.49, 550),
            ("Musakhan", 6.99, 500),
            ("Falafel", 4.99, 300),
            ("Hummus", 3.99, 200),
            ("Tabbouleh", 4.49, 150),
            ("Knafeh", 3.49, 350),
            ("Baklava", 2.99, 300),
            ("Halva", 2.49, 200),
            ("Kunafa", 3.49, 350),
        ],
        "Palestine": [
            ("Maqluba", 7.49, 550),
            ("Musakhan", 6.99, 500),
            ("Falafel", 4.99, 300),
            ("Hummus", 3.99, 200),
            ("Tabbouleh", 4.49, 150),
            ("Knafeh", 3.49, 350),
            ("Baklava", 2.99, 300),
            ("Halva", 2.49, 200),
            ("Kunafa", 3.49, 350),
            ("Basbousa", 2.99, 250),
        ],
        "Tunisia": [
            ("Couscous", 6.49, 450),
            ("Brik", 5.99, 400),
            ("Tajine", 7.99, 550),
            ("Harissa", 2.99, 100),
            ("Merguez", 6.49, 500),
            ("Chakchouka", 4.99, 300),
            ("Lablabi", 3.49, 150),
            ("Mloukhia", 5.49, 250),
            ("Makroudh", 3.99, 350),
            ("Baklava", 2.99, 300),
        ],
        "Algeria": [
            ("Couscous", 6.49, 450),
            ("Tagine", 7.99, 550),
            ("Chorba", 4.49, 200),
            ("Rechta", 6.99, 500),
            ("Mhadjeb", 5.99, 400),
            ("Khobz", 1.99, 200),
            ("Baghrir", 2.99, 180),
            ("Halva", 2.49, 200),
            ("Baklava", 2.99, 300),
            ("Basbousa", 2.99, 250),
        ],
        "Saudi Arabia": [
            ("Kabsa", 7.99, 600),
            ("Mandi", 8.99, 650),
            ("Harees", 5.49, 400),
            ("Tharid", 4.99, 350),
        ],
    }
def show_arabic_food():
    for country, food_list in categories.items():
        print(f"\n{country}:")
        for item in food_list:
            food = ArabicFoodMenu(*item)
            print(food)

if __name__ == "__main__":
    show_arabic_food()