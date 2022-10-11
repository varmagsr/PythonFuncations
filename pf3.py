def myfunc(a):
    return len(a)


x = map(myfunc, ('apple', 'banana', 'cherry'))

print(x)

# convert the map into a list, for readability:
print(list(x))


# -------------------------------------------------------------
# getattr()
class Person:
    name = "John"
    age = 36
    country = "Norway"


y = getattr(Person, 'age')


# -------------------------------------------------------------
# setattr()
class Person:
  name = "John"
  age = 36
  country = "Norway"

setattr(Person, 'age', 40)

# -------------------------------------------------------------
# Append()
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")