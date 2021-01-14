# Makes a function that will contain the 
# desired program.

# get dictionairies [done] for retrieving elements

my_dict = input('Please input your username >>')

first = input('What is your firstname?')
Last = input('What is your last name?')
Job = input('What is your Job title?')
Com = input('Which company do u work for?')

my_dict = {
        'First name' : 'Coen',
        'Last name' : 'Meulenkamp',
        'Job title' : 'Learning Coach',
        'Company' : 'Techgrounds'
        }
    
# Output: Techgrounds
for key in my_dict:
    print(key, "-->", my_dict[key])

 
