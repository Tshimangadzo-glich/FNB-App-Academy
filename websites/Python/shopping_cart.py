
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy or press q to quit: ")
    if foods.lower() == 'q':
        break
    else:
        prices = float(input(f"Enter the price of the {foods}: R")) 
        foods.append(food) 
        prices.append(price)
        
print("...... YOUR CART ......")

for food in foods:
    print(foods, end= "")
    
for price in prices:
    total += price
    
print("\n")
print(f"Your total is: R{total}")