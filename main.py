from drinks import MENU, create_drink
from storage import save_order, save_receipt, load_order_history
from order import Order



def display_menu():
    print("Available drinks:")
    for number, (name, price) in enumerate(MENU.items(), start=1):
        print(f"{number}. {name} - ${price:.2f}")

    print("0. Finish Order")
    print("==============================")



def choose_option(options, question):

    while True:
        print(f"\n{question}")

        for number, option in enumerate(options, start=1):
            print(f"{number}. {option}")

        choice = input("Enter your choice: ").strip()

        if choice.isdigit():
            choice_number = int(choice)

            if 1 <= choice_number <= len(options):
                return options[choice_number - 1]

        print("Invalid choice. Please try again.")


def place_order():
    
    order = Order()
    menu_items = list(MENU.keys())

    while True:
        display_menu()
        choice = input("What would you like to order? ")

        if choice == "0":
            break

        if not choice.isdigit():
            print("Please enter a number.")
            continue

        choice_number = int(choice)

        if not 1 <= choice_number <= len(menu_items):
            print("Invalid choice. Please try again.")
            continue

        drink_name = menu_items[choice_number - 1]

        size = choose_option(
            ["Small", "Medium", "Large"], "Choose your size:"
        )

        milk = choose_option(
            ["Whole", "Oat", "Almond"], "Choose your milk:"
        )

        temperature = choose_option(
            ["Hot", "Iced"], "Hot or Iced?"
        )

        drink = create_drink(drink_name, size, milk, temperature)
        order.add_items(drink)

        print(f"\n{drink_name} added to your order!")

        another = input(
            "\nWould you like to order another item? (yes/no): "
        ).lower()

        if another == "no":
            break

    if order.items:
        print(order.display_receipt())
        save_order(order)
        receipt_path = save_receipt(order)
        print(f"\nYour receipt was saved to: {receipt_path}")

    else:
        print("\nYou did not order anything.")

 
def view_order_history():
    
    history = load_order_history()

    if not history:
        print("\nNo previous orders were found.")
        return

    print("\n========== ORDER HISTORY ==========")

    for number, saved_order in enumerate(history, start=1):
        print(f"\nOrder {number}")

        for item in saved_order["items"]:
            print(
                f"{item['name']} - {item['size']} - "
                f"{item['milk']} milk - {item['temperature']} "
                f"- ${item['price']:.2f}"
            )

        print(f"Total: ${saved_order['total']:.2f}")

    print("===================================")


def main():
    
    print("Welcome to TAS Cafe!")

    while True:
        print("\n1. Place an Order")
        print("2. View Order History")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            place_order()

        elif choice == "2":
            view_order_history()

        elif choice == "3":
            print("\nThank you for visiting TAS Cafe!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
