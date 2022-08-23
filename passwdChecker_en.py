print('Passwrod seciurity level checker\n')

score = 0
specialChars = "!@#$%^&*()?/."
numbers = "1234567890"
lowercase = "abcdefghijklmnouprstuwvzx"
uppercase = "ABCDEFGHIJKLMNOUPRSTUWVZX"
passwd = input("Type your password: ")

for char in passwd:
    if char in numbers:
        score = score + 1
    elif char in specialChars:
        score = score + 2
    elif char in lowercase:
        score += 1
    elif char in uppercase:
        score += 2


if score >= 0 and score < 6:
    print("Your password is very weak!")
elif score >= 6 and score < 11:
    print("Your password is weak")
elif score >= 11 and score < 16:
    print("Your password is good")
elif score >= 16 and score < 19:
    print("Your password is strong")
elif score >= 19:
    print("Your password is really strong!")

input('\nPress ENETER key to exit')