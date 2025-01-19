guests= ['cody', 'cady', 'chesley']

name= guests[0].title()
print(f"{name}, please come to dinner.")

name= guests[1].title()
print(f"{name}, please come to dinner.")

name= guests[2].title()
print(f"{name}, please come to dinner.")

name= guests[1].title()
print(f"\nSorry,{name} can't make it to dinner.")

del(guests[1])
guests.insert(1, 'carlo')

name= guests[0].title()
print(f"{name}, please come to dinner.")

name= guests[1].title()
print(f"{name}, please come to dinner.")

name= guests[2].title()
print(f"{name}, please come to dinner.")

print("\nWe got a bigger table!")
guests.insert(0, 'mariae')
guests.insert(2, 'mariez')
guests.append('maryel')

name= guests[0].title()
print(f"{name}, please come to dinner.")

name= guests[1].title()
print(f"{name}, please come to dinner.")

name= guests[2].title()
print(f"{name}, please come to dinner.")

name= guests[3].title()
print(f"{name}, please come to dinner.")

name= guests[4].title()
print(f"{name}, please come to dinner.")

name= guests[5].title()
print(f"{name}, please come to dinner.")

