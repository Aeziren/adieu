import inflect

names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break

i = inflect.engine()

print(f"Adieu, adieu, to {i.join(names)}")
