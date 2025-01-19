pets = []

pet = {
    'Animal type': 'Dog',
    'Name': 'Nala',
    'Owner': 'Hailey',
}
pets.append(pet)

pet = {
    'Animal type': 'Cat',
    'Name': 'Yuki',
    'Owner': 'Dominic',
}
pets.append(pet)

pet = {
    'Animal type': 'Hamster',
    'Name': 'Mochi',
    'Owner': 'Maya',
}
pets.append(pet)


for pet in pets:
    print(f"\nHere's what I know about {pet['Name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")