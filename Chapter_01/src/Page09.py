cast = ["Cleese", "Palin", "Jones", "Idle"]
print(cast)
print(len(cast))
print(type(cast))
print(cast[1])

cast.append("Gilliam")
print(cast)
print(cast.pop())
print(cast)
cast.extend(['Gilliam', "Chapman"])
print(cast)

cast.remove('Chapman')
print(cast)

cast.insert(0,"Chapman")
print(cast)