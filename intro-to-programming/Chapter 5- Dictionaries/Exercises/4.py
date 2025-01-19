rivers= {
    'Cagayan river': 'Philippines',
    'Yellow river': 'China',
    'Nile river': 'Egypt',
    'Indus river': 'Pakistan, India',
    'Missouri river': 'USA',
}

for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print(f"- {country.title()}")