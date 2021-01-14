# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

# and 
# or
# not   

# Makes a function that will contain the 
# desired program.
numm = int(input("Please input your number: "))
i = 0
while i == 0:

    if numm < 100:
        print( str(numm) + " is pretty low, isn't it")
        numm = int(input("Please input your number: "))
    if numm == 100:
         print("100 is a nice number indeed")
         i = 1
    if numm > 100:
         print("Wow, " + str(numm) +" is a big number!")
         numm = int(input("Please input your number: "))
