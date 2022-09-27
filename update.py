print("| Henderson Pizza store |")
print("")

pizzas_listed = ['Margarita', 'Pepperoni', 'Meatlovers', 'Butter Chicken', 'Beef And Onion', 'Hawaiian', 'Cheese Supreme', 'Cheese And Garlic', 'Vegetarian', 'Chicken Cranberry', 'Buffalo Chicken', 'Ham And Cheese', 'Peri Peri Chicken']
toppings_listed = ['Jalapeno', 'Onions', 'Capsicum', 'Extra Cheese', 'Olives', 'Tomatoes', 'Mushrooms', 'Spinach', 'Extra Pepperoni', 'Bacon', 'Sausage', 'Pineapple', 'Wedges'  ]
pizza_prices = {'Margarita': 8.50, 'Pepperoni': 8.50, 'Meatlovers': 8.50, 'Butter Chicken': 8.50, 'Beef And Onion': 8.50, 'Hawaiian': 8.50, 'Cheese Supreme': 8.50, 'Cheese And Garlic': 5, 'Vegetarian': 5, 'Chicken Cranberry': 5, 'Buffalo Chicken': 5, 'Ham And Cheese': 5, 'Peri Peri Chicken': 5}
topping_prices = {'Jalapeno':0.50, 'Onions': 0.50, 'Capsicum':0.50, 'Extra Cheese':0.50, 'Olives':0.50, 'Tomatoes':0.50, 'Mushrooms': 0.50, 'Spinach': 0.50, 'Extra Pepperoni': 0.50, 'Bacon': 0.50, 'Sausage': 0.50, 'Pineapple': 0.50, 'Wedges': 0.50}
finished_price = []
order_finished = {}
customer_information = {}


#asking the user to select a pizza from the menu
print("Welcome to Henderson Pizza Store, please select a pizza that you would like to order ")
pizza_ordered = True
while pizza_ordered:    
    print("Could you please choose a pizza that you would like to order from the menu provided: ")
    print()
    for pizzas in pizzas_listed:
        print(pizzas)
        print()
    while True:
        pizza = input("What type of pizza would you like to order first? ").title()
        
        if pizza in pizzas_listed:
            print(f"You have ordered one {pizza} pizza. ")
            finished_price.append(pizza_prices[pizza])
            break
        if pizza not in pizzas_listed:
            print(f"I'm sorry but unfortunately we do not have {pizza} in our menu please try again. ")

    #asking the user to choose extra toppings for their pizza
    order_topping = True
    print("These are the types of extra toppings that are available to put on your pizza:: ")
    for toppings in toppings_listed:
        print(toppings)
        print()
    while order_topping:
        other_topping = input("Would you like to add any extra toppings? yes or no? ")
        if other_topping == "yes" or other_topping == "Yes" or other_topping == "y" or other_topping == "Y":
            topping = input("Which one would you like to add onto your pizza? ").title()
            if topping in toppings_listed:
                order_finished.setdefault(pizza, [])
                order_finished[pizza].append(topping)
                print(f"I have added {topping} onto your pizza. ")
                finished_price.append(topping_prices[topping])
            else:
                print(f"I'm sorry, but we don't have any {topping} available on our menu please try again. ")

        elif other_topping == "no" or other_topping == "No" or other_topping == "n" or other_topping == "N":
            break
    other_pizza = input("Would you like to order any other pizzas? ")
    if other_pizza == "no" or other_pizza == "No" or other_pizza == "n" or other_pizza == "N" :
        for key, value in order_finished.items():
            print(f"\nYou have ordered one {key} pizza with {value} ")
        check_order = True
        while check_order:
            print()
            order_correct = input("Is this correct? yes/no ")
            if order_correct == "yes" or order_correct == "Yes" or order_correct == "y" or order_correct == "Y":
                check_order = False
                pizza_ordered = False
            if order_correct == "no" or order_correct == "No" or order_correct == "n" or order_correct == "N":
                print(order_finished)
                add_remove = input("would you like to add or remove anything you have chosen? ")
                if add_remove == "remove":
                    remove = input("Which pizza would you like to remove? ")
                    del order_finished[remove]
                    print(order_finished)
                if add_remove == "add":
                    check_order = False

#finishing off the customers order
print(f"\nYour total order price is: ${sum(finished_price)} + $3 delivery fee")

print("Please provide us with your name, address, postalcode and phonenumber" )
customer_information['name'] = input("what is your name?")
customer_information['street_name'] = input("What is your housenumber and streetname? ")
customer_information['postalcode'] = input("What is the postalcode? ")
customer_information['phonenumber'] = input("What is your phonenumber? ")
print()
print(f"Thank you for your order {customer_information['name']}. ")
print()
print("We will deliver your order to your address shortly ")
print()
print(customer_information['street_name'])
print(customer_information['postalcode'])
print()
print(f"we will contact you on {customer_information['phonenumber']} if anything comes up thank you. ")
