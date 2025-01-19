prompt = "\nWhat toppings would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f" Your pizza will have {topping} included.")
        print("")
    else:
        break