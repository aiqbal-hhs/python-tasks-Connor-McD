print("| Henderson Pizza store |")
print("")

pizzas_available = ['Margarita', 'Pepperoni', 'Meatlovers', 'Butter Chicken', 'Beef And Onion', 'Hawaiian', 'Cheese Supreme', 'Cheese And Garlic', 'Vegetarian', 'Chicken Cranberry', 'Buffalo Chicken', 'Ham and Cheese', 'Peri Peri Chicken']
toppings_available = ['Jalapeno', 'Onions', 'Capsicum', 'Extra Cheese', 'Olives', 'Tomatoes', 'Mushrooms', 'Spinach', 'Extra Pepperoni', 'Bacon', 'Sausage', 'Pineapple', 'Wedges'  ]
pizza_prices = {'Margarita': 8.50, 'Pepperoni': 8.50, 'Meatlovers': 8.50, 'Butter Chicken': 8.50, 'Beef And Onion': 8.50, 'Hawaiian': 8.50, 'Cheese Supreme': 8.50, 'Cheese And Garlic': 5, 'Vegetarian': 5, 'Chicken Cranberry': 5, 'Buffalo Chicken': 5, 'Ham And Cheese': 5, 'Peri Peri Chicken': 5}
topping_prices = {'Jalapeno':0.50, 'Onions': 0.50, 'Capsicum':0.50, 'Extra Cheese':0.50, 'Olives':0.50, 'Tomatoes':0.50, 'Mushrooms': 0.50, 'Spinach': 0.50, 'Extra Pepperoni': 0.50, 'Bacon': 0.50, 'Sausage': 0.50, 'Pineapple': 0.50, 'Wedges': 0.50}
total_price = []
finished_order = {}
customer_address = {}


#asking customer for pizza order
print("Welcome to Henderson Pizza store")
order_pizza = True
while order_pizza:    
    print("Could you please choose a pizza you would like to order: ")
    print()
    for pizzas in pizzas_available:
        print(pizzas)
        print()
    while True:
        pizza = input("What type of  pizza would you like to order first? ").title()
        
        if pizza in pizzas_available:
            print(f"You have ordered a {pizza} pizza. ")
            total_price.append(pizza_prices[pizza])
            break
        if pizza not in pizzas_available:
            print(f"I'm sorry but unfortunately we do not have {pizza} in our menu. ")

    #asking for extra toppings
    order_topping = True
    print("This is the types of extra toppings that are available:: ")
    for toppings in toppings_available:
        print(toppings)
        print()
    while order_topping:
        other_topping = input("Would you like an other toppings? yes or no? ")
        if other_topping == "yes" or other_topping == "Yes" or other_topping == "y" or other_topping == "Y":
            topping = input("Which one would you like to add on to your pizza? ").title()
            if topping in toppings_available:
                finished_order.setdefault(pizza, [])
                finished_order[pizza].append(topping)
                print(f"I have added {topping} to your pizza. ")
                total_price.append(topping_prices[topping])
            else:
                print(f"I am sorry, we don't have {topping} available on our menu. ")

        elif other_topping == "no" or other_topping == "No" or other_topping == "n" or other_topping == "N":
            break
    other_pizza = input("Would you like to order any other pizzas? ")
    if other_pizza == "no" or other_pizza == "No" or other_pizza == "n" or other_pizza == "N" :
        for key, value in finished_order.items():
            print(f"\nYou have ordered one {key} pizza with {value} ")
        check_order = True
        while check_order:
            print()
            order_correct = input("Is this correct? yes/no ")
            if order_correct == "yes" or order_correct == "Yes" or order_correct == "y" or order_correct == "Y":
                check_order = False
                order_pizza = False
            if order_correct == "no" or order_correct == "No" or order_correct == "n" or order_correct == "N":
                print(finished_order)
                add_remove = input("would you like to add or remove? ")
                if add_remove == "remove":
                    remove = input("Which pizza would you like to remove? ")
                    del finished_order[remove]
                    print(finished_order)
                if add_remove == "add":
                    check_order = False

#finalizing the order
print(f"\nYour total order price is: ${sum(total_price)}")

print("Please provide us with your name, address and phonenumber" )
customer_address['name'] = input("what is your name?")
customer_address['street_name'] = input("What is your housenumber and streetname? ")
customer_address['postalcode'] = input("What is the postalcode? ")
customer_address['phonenumber'] = input("What is your phonenumber? ")
print()
print(f"Thank you for your order {customer_address['name']}. ")
print()
print("We will deliver your order to this address ASAP ")
print()
print(customer_address['street_name'])
print(customer_address['postalcode'])
print()
print(f"we will contact you on {customer_address['phonenumber']} if anything comes up. ")   
