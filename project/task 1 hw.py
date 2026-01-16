# Beckett Pizza Plaza 4-for-3 Offer
print("🍕 Welcome to Beckett Pizza Plaza! 🍕")
print("Take advantage of our 4-for-3 special today!\n")

# List to store pizza prices
pizza_prices = []  

# Ask user for pizza prices with friendly messages
for count in range(4):
    while True:
        try:
            user_input = float(input(f"Enter the price of Pizza #{count + 1}: £"))
            user_input = round(user_input, 2)  # Keep it neat and tidy
            
            if user_input <= 0:
                print("Hmm, that doesn't look right. Please enter a price above £0.")
            else:
                pizza_prices.append(user_input)
                print(f"Great! Pizza #{count + 1} added at £{user_input:.2f}.\n")
                break
        except:
            print("Oops! Please enter a valid number, like 7.50 or 12.")

# Calculate total cost
total_cost = sum(pizza_prices)

# Find the cheapest pizza (free one)
lowest_price = min(pizza_prices)
free_pizza_index = pizza_prices.index(lowest_price) + 1  # Human-friendly numbering

# Final amount after discount
final_amount = total_cost - lowest_price

# Calculate discount percentage
discount_percent = (lowest_price / total_cost) * 100

# Show the entered prices
print("\nHere’s a summary of your order:")
for i, price in enumerate(pizza_prices, start=1):
    print(f"Pizza #{i}: £{price:.2f}")
    
# Friendly receipt display
print("\n==================== RECEIPT ====================")
print(f"Original Total: £{total_cost:.2f}")
print(f"Good news! Pizza #{free_pizza_index} is on the house! (£{lowest_price:.2f} saved)")
print(f"🎉 Your Total Today: £{final_amount:.2f} (You saved {discount_percent:.0f}%!) 🎉")
print("\nThank you for ordering with Beckett Pizza Plaza! 🍕")
print("Enjoy your pizzas and have a delicious day!\n")
