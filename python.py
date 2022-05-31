
print("| Henderson Pizza store |")
print("")

pizzas_available = ['margarita', 'pepperoni', 'meatlovers', 'butter chicken', 'beef and onion', 'hawaiian']
toppings_available = ['jalapeno', 'onions', 'capsicum', 'cheese', 'olives', 'tomatoes']
pizza_prices = {'margarita': 5, 'pepperoni': 7, 'meatlovers': 6, 'butter chicken': 8, 'beef and onion': 7, 'hawaiian': 6.5}
topping_prices = {'jalapeno':3, 'onions': 2, 'capsicum':3, 'cheese':4, 'olives':4, 'tomatoes':4}
total_price = []
finished_order = {}
customers_adress = {}


#asking customer for pizza order
print("Welcome to Henderson Pizza store")
order_pizza = True
while order_pizza:    
    print("could you please choose a pizza you would like to order: ")
    print()
    for pizzas in pizzas_available:
        print(pizzas)
        print()
    while True:
        pizza = input("what type of  pizza would you like to order first?")
        if pizza in pizzas_available:
            print(f"You have ordered a {pizza} pizza.")
            total_price.append(pizza_prices[pizza])
            break
        if pizza not in pizzas_available:
            print(f"I'm sorry but unfortunately we do not have {pizza} in our menu.")

    #asking for extra toppings
    order_topping = True
    print("This is the types of extra toppings that are available:: ")
    for toppings in toppings_available:
        print(toppings)
        print()
    while order_topping:
        other_topping = input("Would you like an other toppings? yes or no?")
        if other_topping == "yes":
            topping = input("Which one would you like to add on to your pizza?")
            if topping in toppings_available:
                finished_order.setdefault(pizza, [])
                finished_order[pizza].append(topping)
                print(f"I have added {topping} to your pizza.")
                total_price.append(topping_prices[topping])
            else:
                print(f"I am sorry, we don't have {topping} available on our menu.")

        elif other_topping == "no":
            break
    other_pizza = input("Would you like to order any other pizzas?")
    if other_pizza == "no":
        for key, value in finished_order.items():
            print(f"\nYou have ordered one{key} pizza with {value}")
        check_order = True
        while check_order:
            print()
            order_correct = input("Is this correct? yes/no ")
            if order_correct == "yes":
                check_order = False
                order_pizza = False
            if order_correct == "no":
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

print("Please provide us with your name, adress and phonenumber")
customers_adress['name'] = input("what is your name?")
customers_adress['street_name'] = input("What is your housenumber and streetname  ?")
customers_adress['postalcode'] = input("What is the postalcode?")
customers_adress['phonenumber'] = input("What is your phonenumber?")
print()
print(f"Thank you for your order {customer_adress['name']}.")
print()
print("We will deliver your order to this adres ASAP")
print()
print(customers_adress['street_name'])
print(customers_adress['postalcode'])
print()
print(f"we will contact you on {customer_adress['phonenumber']} if anything comes up.")   
