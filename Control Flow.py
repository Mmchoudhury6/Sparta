print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

print(x[:5])



print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
z = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

print(list(filter(lambda x:x%2==0, z)))



print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

print(list(filter(lambda x:x%2==0, x[:5])))
#or just use for loop

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
x= []
for i in names:
    x.append(i[0])
print(x)






print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
indexlist = []
for i in names:
    x = i.index(" ")
    indexlist.append(x)
print(indexlist)




print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
'''
initial_list = []
for i in names:
    x = i[0]
    y = i[-1]
    initial_list.append(x + y)
print(initial_list)

'''
initial_list = []
for name in names:
    space_index = name.index(" ")
    initials = name[0] + name[space_index + 1]
    initial_list.append(initials)

print(initial_list)


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


# A3a:
for i in list_of_lists:
    if len(i) == len(set(i)):
        print(i)


# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:
x = 0
while x <= 100:
    try:
        x = int(input("enter a number greater than 100\n"))
    except ValueError:
        print("put an integer only please")
        x = 0
        continue

    if x <= 1:
        print("no prime")
    else:
        prime = True
        for i in range(2, x):
            if x % i == 0:
                prime = False
        if prime:
            print("yes prime")
        else:
            print("no prime")

print("thank you for putting in correct number")




print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise


