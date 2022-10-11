## -----------------------------------------
# sorting() exp 1
a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a)
print(x)

# reverse sorting() exp1
a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a, reverse=True)
print(x)

## -----------------------------------------
# join() exp 1
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

# join() exp 2

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)
## -----------------------------------------
# replace() exp 1
txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three")

print(x)

# replace() exp 2:Replace the two first occurrence of the word "one":
txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three", 2)

print(x)
