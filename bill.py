name = input("Enter Customer Name: ")
phone = input("Enter Phone Number: ")

items = []
total = 0

while True:
    item_name = input("Enter Item Name (or type 'done' to finish): ")
    if item_name.lower() == 'done': 
        break
    quantity = int(input(f"Enter quantity of {item_name}: "))
    price = float(input(f"Enter price per item of {item_name}: "))
    item_total = quantity * price
    total += item_total
    items.append((item_name, quantity, price, item_total)) 

print("\n====== Supermarket Bill ======")
print(f"Customer Name : {name}")
print(f"Phone Number  : {phone}")
print("\nItems Purchased:")
print(f"{'Item':15}{'Qty':>5}{'Price':>10}{'Total':>10}")
print("-" * 40)
for item in items:
    print(f"{item[0]:15}{item[1]:>5}{item[2]:>10}{item[3]:>10}")
print("-" * 40)
print(f"{'Total':30}{total:>10.2f}")
print("Thank you for shopping with us!")

