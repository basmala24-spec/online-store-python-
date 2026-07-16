
from menu.dessert import dessert_menu
from menu.seafood import seafood_menu
from menu.drinks import drinks_menu
from menu.healthyfood import menu as healthy_menu
from menu.westernfood import menu as western_menu
from menu.breakfast import breakfast_menu
from menu.fastfood import items as fastfood_menu
from menu.arabicfood import categories as arabic_menu


class MAIN:
    def __init__(self, discount_system=None):
        self.cart = []
        self.discount_system = discount_system
        


        self.sections = {
            "Desserts": dessert_menu,
            "Seafood": seafood_menu,
            "Drinks": drinks_menu,
            "Healthy": healthy_menu,
            "Western": western_menu,
            "Breakfast": breakfast_menu,
            "Fast Food": fastfood_menu,
            "Arabic Food": arabic_menu
        }

    def show_sections(self):
        print("\n Choose a category:")
        for i, section in enumerate(self.sections.keys(), 1):
            print(f"{i}. {section}")
        print("0. Exit")


    def show_items(self, menu):
        items_list = []


        for category, items in menu.items():
                print(f"\n{category}")

                if not items:
                    print(" No items available")
                    continue

                for item in items:
                    
                        
                        if isinstance(item, tuple):
                            name, price, calories = item
                            class Temp:
                                def __init__(self, n, p, c):
                                    self.name = n
                                    self.price = p
                                    self.calories = c

                                def __str__(self):
                                    return f"{self.name}: {self.price}EGP | {self.calories} kcal"

                            item = Temp(name, price, calories)

                        items_list.append(item)
                        print(f"{len(items_list)}. {item}")

        print("0. Back")
        return items_list
    


    def start(self):
        while True:
            self.show_sections()

            try:
                choice = int(input("Choose category: "))
            except ValueError:
                print(" Please enter a number!")
                continue

            if choice == 0:
                break

            if 1 <= choice <= len(self.sections):
                section_name = list(self.sections.keys())[choice - 1]
                menu = self.sections[section_name]


                

                while True:
                    items = self.show_items(menu)

                    if not items:
                        print(" No items in this category.")
                        break

                    try:
                        item_choice = int(input("Choose item: "))
                    except ValueError:
                        print(" Please enter a valid number!")
                        continue

                    if item_choice == 0:
                        break

                    if 1 <= item_choice <= len(items):
                        selected = items[item_choice - 1]
                        self.cart.append(selected)
                        print(f"Added: {selected.name}")
                    else:
                        print("Invalid choice!")
                    


            else:
                print(" Invalid category!")
        result = self.show_order()
        
        if result:
            subtotal, calories, final_total, saved, code = result
            self.save_order(subtotal, calories, final_total, saved, code)
            




    def show_order(self):
        if not self.cart:
            print("\n No items selected.")
            return None
    
        total_price = sum(item.price for item in self.cart)
        total_calories = sum(item.calories for item in self.cart)
    
        print("\n YOUR ORDER:")
        print("-" * 30)
    
        for i, item in enumerate(self.cart, 1):
            print(f"{i}. {item}")

        print("-" * 30)
        print(f" Subtotal: {total_price:.2f} EGP")
        print(f" Calories: {total_calories} kcal")
        final_total = total_price
        saved=0
        code_used = None
        
        if self.discount_system:
            code = input("\nEnter discount code (or press Enter): ").strip()
    
            if code:
                final_total, saved, msg = self.discount_system.apply_code(code, total_price)
                print(msg)
                code_used = code

            
        print(f"Final Total: {final_total:.2f} EGP")
            
        print("-" * 30)
        return total_price, total_calories, final_total, saved, code_used
            
    

    
    def save_order(self, subtotal, calories, final_total, saved, code):
        with open("order.txt", "a", encoding="utf-8") as file:
            file.write("YOUR ORDER\n")
            file.write("-"*30 + "\n")

            for item in self.cart:
                file.write(f"{item.name} | {item.price} EGP | {item.calories} kcal\n")

            file.write("-"*30 + "\n")
            file.write(f"Subtotal: {subtotal:.2f} EGP\n")
            file.write(f"Calories: {calories} kcal\n")

            if code:
                file.write(f"Discount Code: {code}\n")
                file.write(f"Saved: {saved:.2f} EGP\n")

            file.write(f"Final Total: {final_total:.2f} EGP\n")
            file.write("="*40 + "\n\n")

        
if __name__ == "__main__":
    MAIN().start()




