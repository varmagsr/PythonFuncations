# for integers
print(round(15))

# for floating point
print(round(51.6))
print(round(51.5))
print(round(51.4))

# when the (ndigit+1)th digit is =5
print(round(2.665, 1))
# ---------------------------------------------------
##Max() exp 1

var1 = "geeks"
var2 = "for"
var3 = "geek"

max_val = max(var1, var2, var3, key=len)
print(max_val)

##Max() exp 2: string with the maximum lexicographic value
var1 = "geeks"
var2 = "for"
var3 = "geek"

max_val = max(var1, var2, var3)
print(max_val)

##Max() exp 3:
lister = [1.2, 1.3, 0.1]
max_values = max(lister)
print(max_values)


##Max() exp 4:
# function to find minimum and maximum position in list


def minimum(a, n):
    # inbuilt function to find the position of maximum
    maxpos = a.index(max(a))

    # printing the position
    print("The maximum is at position", maxpos + 1)


# driver code
a = [3, 4, 1, 3, 4, 5]
minimum(a, len(a))


# ---------------------------------------------------
##Min() exp 1

# printing the minimum of
# 4, 12, 43.3, 19, 100
print(min(4, 12, 43.3, 19, 100))

##Min() exp 2
# find the string with minimum length
s = min("GfG", "Geeks", "GeeksWorld", key = len)
print(s)
