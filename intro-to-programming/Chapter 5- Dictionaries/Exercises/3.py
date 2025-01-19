glossary= {
    'strings': 'a sequence of characters',
    'variables': 'a placeholder for information',
    'loops': 'a comand used to repeat a part of code until the desired process is complete',
    'dictionary': 'mutable data structures that allowyou to stor key-value pairs',
    'lists': 'a collection which is ordered and changeable',
    'float': 'a function in the Python programming language that converts values into floating point numbers',
    'value': 'a data type that can have one of two possible values: True or False',
    'integer': 'a whole number, positive or negative, without decimals, of unlimited length',
    'tuples': ' a collection of objects separated by commas',
    'key': 'The first item in a key-value pair in a dictionary',

}

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")