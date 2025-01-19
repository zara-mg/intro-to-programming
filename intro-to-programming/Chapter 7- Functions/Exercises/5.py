def describe_city(city, country='Japan'):
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('Tokyo')
describe_city('New York', 'USA')
describe_city('Paris', 'France')