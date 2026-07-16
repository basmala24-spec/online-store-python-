import order
import review
import reservation
from discount import DiscountSystem


def get_customer_info():
    print("\n--- Customer Info ---")

    name = input("Enter your name: ").strip()

    while True:
        phone = input("Enter your phone number: ").strip()
        if phone.isdigit():
            break
        print("Invalid phone number!")

    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Please enter a valid age!")

    return {
        "name": name,
        "phone": phone,
        "age": age
    }


def main_menu():
    print("\n=== Five Clovers Restaurant ===")
    print("1. Place an Order")
    print("2. Make a Reservation")
    print("3. Write a Review")
    print("4.apply discount((if found)) ")
    print("5. Exit")


def main():
    customer = get_customer_info()
    discount_system = DiscountSystem()

    while True:
        main_menu()
        choice = input("Choose an option: ")
        

        if choice == '1':
            print(f"\nWelcome {customer['name']} 👋")
            order_system = order.MAIN(discount_system) 
            order_system.start()

        elif choice == '2':
            print(f"\nReservation for {customer['name']}")
            res_system = reservation.system()
            
            res_system.reservation_flow()

        elif choice == '3':
            print(f"\nWrite your review {customer['name']}")
            review.main()

        elif choice == '4':
            print("\n=== Available Discounts ===")
            discount_system.list_discounts()

            code = input("Enter promo code: ").strip()
            total = float(input("Enter order total: "))
            final, saved, msg = discount_system.apply_code(code, total)
            print(msg)
            print(f"Final total: {final}")

        elif choice == '5':
            print("\nThank you for visiting Five Clovers ❤️")
            break

        else:
            print("Invalid choice, try again!")


if __name__ == "__main__":
    main()