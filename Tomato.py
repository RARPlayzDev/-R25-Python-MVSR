import json

with open("menu.json", "r") as file:
    menu = json.load(file)

cart = {}

def show_menu():
    print("\n--- MENU ---")
    for key, item in menu.items():
        print(f"{key}. {item['name']} - ₹{item['price']}")

def show_cart():
    print("\n--- CART ---")
    if not cart:
        print("Cart is empty")
        return

    total = 0
    for item in cart.values():
        cost = item["price"] * item["qty"]
        total += cost
        print(f"{item['name']} x {item['qty']} = ₹{cost}")

    print(f"Total: ₹{total}")

print("Welcome to Tomato")

while True:
    show_menu()
    show_cart()

    choice = input("\nEnter item number to add (0 to checkout): ")

    if choice == "0":
        break

    if choice in menu:
        qty = int(input("Enter quantity: "))

        if choice in cart:
            cart[choice]["qty"] += qty
        else:
            cart[choice] = {
                "name": menu[choice]["name"],
                "price": menu[choice]["price"],
                "qty": qty
            }

        print("Cart updated")
    else:
        print("Invalid item number")

# Final Bill
print("\n FINAL BILL")
show_cart()
print(" Thank you for ordering!")
