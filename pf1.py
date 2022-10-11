import functools

##-----------------------------------------------------------------
listofnum = [1, 2, 3, 4, 5]

print(functools.reduce(lambda a, b: a + b, listofnum))
print(functools.reduce(lambda a, b: a if a > b else b, listofnum))
##-----------------------------------------------------------------


str = 'My Name is G S R Varma'
print(str.split(' '))
##-----------------------------------------------------------------

# Python program to illustrate
# enumerate function
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print("Return type:", type(obj1))
print(list(enumerate(l1)))

# changing start index to 2 from 0
print(list(enumerate(s1, 2)))

##-----------------------------------------------------------------

expression = 'x*(x+1)*(x+2)'
print(expression)

x = 3

result = eval(expression)
print(result)

##-----------------------------------------------------------------
##zip()   exp 1
name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]

# using zip() to map values
mapped = zip(name, roll_no)

print(set(mapped))

##Zip() exp 2
namee = ['Mukesh', 'Roni', 'Chari']
ages = [24, 50, 18]

for i, (name, age) in enumerate(zip(namee, ages)):
    print(i, name, age)

##Zip() exp 3
stocks = ['reliance', 'infosys', 'tcs']
prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks,
                               prices in zip(stocks, prices)}
print(new_dict)

## unzip() Exp1
# Python code to demonstrate the working of
# unzip

# initializing lists
name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]
marks = [40, 50, 60, 70]

# using zip() to map values
mapped = zip(name, roll_no, marks)

# converting values to print as list
mapped = list(mapped)

# printing resultant values
print("The zipped result is : ", end="")
print(mapped)

print("\n")

# unzipping values
namz, roll_noz, marksz = zip(*mapped)

print("The unzipped result: \n", end="")

# printing initial lists
print("The name list is : ", end="")
print(namz)

print("The roll_no list is : ", end="")
print(roll_noz)

print("The marks list is : ", end="")
print(marksz)

