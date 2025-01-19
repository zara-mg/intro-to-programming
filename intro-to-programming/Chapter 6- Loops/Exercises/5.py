sandwich_orders = ['cheese', 'beef', 'turkey ham', 'bacon', 'salami', 'lettuce', 'pastrami', ]
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Your {current_sandwich} is being made.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"Your {sandwich} order is ready.")