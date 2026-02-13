#question6 
inventory = {
    "Laptop": (999.99, 5),
    "Mouse": (29.99, 15),
    "Keyboard": (79.99, 10),
    "Monitor": (299.99, 8)
} 
print("=====Current Inventory ====")
for item, (price, quantity) in inventory.items(): 
    print(f"{item} - Price: ${price}, Quantity: {quantity}")
    
print("\n")

electronics = {"Laptop", "Monitor"}
accessories = {"Mouse", "Keyboard"}
All_items = electronics | accessories
print(f"All Product categories: {All_items}")

print("\n")

All_prices = [price for item, (price, quantity) in inventory.items()]
print (f"Price List: {All_prices}")
print (f"Sorted prices: {sorted(All_prices)}")
print (f"Lowest price: ${min(All_prices)}")
print (f"Highest price: ${max(All_prices)}")

print("\n")

# Add new product
inventory.update({"headphones": (49.99, 20)})
inventory.update({"Mouse": (29.99, 12)}) # updated quantiy of mouse 
del inventory["Monitor"] # Remove Monitor from inventory

print("=== Final Inventory === ")
for item, (price, quantity) in inventory.items(): 
    print(f"{item} - Price: ${price}, Quantity: {quantity}")


    # NOTE TO PROFESSOR: THE ABOVE CODE WAS CREATED BASED ON MY OWN KNOWLEDGE AND UNDERSTANDING OF PYTHON PROGRAMMING. I DID NOT ATTEND THE LABS SO I HAD TO RELY ON THE INSTRUCTIONS GIVEN IN D2L TO COMPLETE THE LABS.
    