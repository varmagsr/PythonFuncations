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


# -------------------------------------------------------------
# range() exp1
x = range(3, 6)
for n in x:
  print(n)

# range() exp2
  x = range(3, 20, 2)
  for n in x:
      print(n)

# -------------------------------------------------------------
# slice() exp1

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 3)
print(a[x])


# -------------------------------------------------------------
# format() exp1
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
##https://www.w3schools.com/python/ref_string_format.asp

# -------------------------------------------------------------
# strip() exp1

txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")
# -------------------------------------------------------------
# abs() exp1

x = abs(-7.25)
print(x)
# -------------------------------------------------------------
# upper() exp1
txt = "Hello my friends"
print(txt.upper())

