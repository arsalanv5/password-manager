import random


def save(name_site, passw):
    with open("password.txt", "a") as f:
        f.write(f"{name_site}: {passw}\n")


while True:

    want = input("do you want to add a password? [y/n] ")
    if want == "n":
        break

    length = int(input("Enter the length of the password: "))
    use_numbers = input("Include numbers? [y/n]: ")
    use_symbols = input("Include symbols? [y/n]: ")
    use_capitals = input("Include capital letters? [y/n]: ")

    letters = "abcdefghijklmnopqrstuvwxyz"
    capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()"

    password_char = letters

    if use_numbers == 'y':
        password_char += numbers
    if use_symbols == 'y':
        password_char += symbols
    if use_capitals == 'y':
        password_char += capital_letters

    passw = ""
    for _ in range(length):
        passw += random.choice(password_char)

    print("Generated password:", passw)

    name_site = input("Enter your site/service: ")

    save(name_site, passw)

print("All passwords saved in password.txt")




