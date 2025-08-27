print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
def divisors(n):
    n = abs(int(n))
    if n == 0:
        return []
    out = []
    for d in range(1, n + 1):
        if n % d == 0:
            out.append(d)
    return out

print(divisors(12))



print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:
def is_factor_of_other(a, b):
    a, b = int(a), int(b)
    if a == 0 or b == 0:
        return False
    return (a % b == 0) or (b % a == 0)

print(is_factor_of_other(3, 12))
print(is_factor_of_other(5, 12))



# -------------------------
# ------------------------------------------------------------- # complete

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
def letter_position(ch):
    return alphabet.index(ch.lower())

print(letter_position("b"))
print(letter_position("o"))



print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
def make_id(name):
    name = name.lower()
    out = ""
    for ch in name:
        out += str(letter_position(ch))
    return out

print(make_id("bob"))



print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:
def make_password(name):
    id_str = make_id(name)
    s = 0
    for d in id_str:
        s += int(d)
    return int(id_str) - s

print(make_password("bob"))



# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
def is_prime(n):
    n = int(n)
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(101))
print(is_prime(150))



print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:
def is_prime_safe(x):
    try:
        n = int(x)
    except (ValueError, TypeError):
        return False
    return is_prime(n)

print(is_prime_safe("abc"))
print(is_prime_safe("103"))
